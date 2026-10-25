"""Score a judge JSON with the v2.2 engine (rules v2.2 by default, or v2.1 for comparison) and explain every step."""
import sys

from .catalog import ENGINE, GATE_WHY, PENALTY_INFO, TYPE_GATES, UNIVERSAL_NAMES, criterion_names, gates_for, load_weights

if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))
import geo_score_calc as calc  # noqa: E402

FAMILY_LABELS = {
    "answer_def": "Answer-first & definitions", "evidence": "Evidence & insight", "fanout": "Follow-up coverage",
    "tone": "Neutral tone", "comparison": "Comparison & selection", "specs": "Specs & facts", "proof": "Proof",
    "commercial": "Commercial & next step", "freshness": "Freshness", "other": "Stage-neutral",
}


def normalise(judge):
    """Make a pasted/uploaded judge JSON (from any v2.2 Copilot prompt) acceptable to the engine."""
    page = judge.setdefault("page", {})
    raw_t = str(page.get("type") or "article").strip().lower()
    page["type"] = calc.TYPE_ALIASES.get(raw_t, raw_t.replace(" ", "_").replace("/", "_").replace("-", "_"))
    page["stage"] = str(page.get("stage") or "Education").strip().capitalize()
    for c in judge.get("criteria", []):
        if c.get("proposed_level") in ("", "null"):
            c["proposed_level"] = None
        for k in c.get("checks", []):
            k["result"] = str(k.get("result", "")).strip().lower()
    return judge


def _ceiling(cid, p, n, proposed, rules):
    if n == 0:
        return None
    if cid == "U2":
        bonus = p == n and n >= 4 and (True if rules == "v2.2" else proposed == 5)
        return min(p, 4) + (1 if bonus else 0)
    return 5 if p == n else min(4, int(5 * p / n + 0.5))


def explain(judge, rules="v2.2"):
    W = load_weights()
    result = calc.compute(judge, W, allow_missing=True, rules=rules)
    type_key = result["page_type_key"]
    names = criterion_names(type_key)
    judged = {c["id"]: c for c in judge.get("criteria", [])}
    by_id = {r["id"]: r for r in result["criteria"]}

    rows, downgrades = [], []
    for cid, default_w in W["page_types"][type_key].items():
        r = by_id.get(cid)
        c = judged.get(cid, {})
        checks = c.get("checks", [])
        proposed = c.get("proposed_level")
        if rules == "v2.2":
            res, _ = calc.prepare_checks(cid, checks, W, type_key)
        else:
            res = {k.get("id"): k.get("result") for k in checks}
        p = sum(v == "pass" for v in res.values())
        n = sum(v in ("pass", "fail") for v in res.values())
        kind = "Universal" if cid in UNIVERSAL_NAMES else "Type-specific"
        if r is None:
            rows.append({"ID": cid, "Criterion": names.get(cid, cid), "Kind": kind,
                         "Default weight": default_w, "Stage family": "-", "Stage x": None, "Effective weight": 0.0,
                         "Checks passed": f"{p}/{n}", "Ceiling": None, "Judge level": proposed,
                         "Rule adjustments": "Dropped: most checks N/A or not judged", "Final level": None, "Points": 0.0, "Lost": 0.0})
            continue
        pre_gate, _, _, notes = calc.level_from_checks(cid, checks, proposed, W, False, c.get("downgrade_reason"), rules, type_key)
        adj = list(notes)
        if pre_gate is not None and r["level"] < pre_gate:
            adj.append(f"gate effect: level {pre_gate} -> {r['level']}")
        if any("judge downgrade" in a for a in notes):
            downgrades.append({"Criterion": cid, "Name": names.get(cid, cid), "Proposed level": proposed,
                               "Final level": r["level"], "Downgrade reason": c.get("downgrade_reason", "")})
        rows.append({
            "ID": cid, "Criterion": names.get(cid, cid), "Kind": kind,
            "Default weight": default_w, "Stage family": FAMILY_LABELS.get(r["family"], r["family"]), "Stage x": r["m"],
            "Effective weight": r["eff_w"], "Checks passed": r["checks_passed"], "Ceiling": _ceiling(cid, p, n, proposed, rules),
            "Judge level": proposed, "Rule adjustments": "; ".join(adj) if adj else "",
            "Final level": r["level"], "Points": r["points"], "Lost": r["impact_points"],
        })

    triggered = {g["id"]: g for g in judge.get("gates", []) if g.get("triggered")}
    reported = {g["id"]: g for g in judge.get("gates", [])}
    gate_rows = []
    for gid in gates_for(type_key):
        g = W["gates"][gid]
        effects = []
        if g.get("cap", 100) < 100:
            effects.append(f"score max {g['cap']}")
        for k, v in (g.get("max_level") or {}).items():
            if k in W["page_types"][type_key]:
                effects.append(f"{k} max level {v}")
        for k in g.get("zero", []):
            if k in W["page_types"][type_key]:
                effects.append(f"{k} = 0")
        gate_rows.append({"Gate": gid, "Scope": "Universal" if gid not in TYPE_GATES else "This page type",
                          "Rule": g["desc"], "Effect if triggered": ", ".join(effects), "Why it exists": GATE_WHY.get(gid, ""),
                          "Status": "TRIGGERED" if gid in triggered else ("Not triggered" if gid in reported else "Not reported"),
                          "Evidence": (reported.get(gid) or {}).get("evidence", "")})

    applied = {p["id"]: p for p in judge.get("penalties", []) if p.get("applied")}
    reported_p = {p["id"]: p for p in judge.get("penalties", [])}
    pen_rows = []
    for pid, pts in sorted(W["penalties"].items(), key=lambda kv: -kv[1]):
        label, rule = PENALTY_INFO.get(pid, (pid, ""))
        pen_rows.append({"Penalty": label, "Triggered when": rule, "Points": -pts,
                         "Status": "APPLIED" if pid in applied else "Not applied",
                         "Evidence": (reported_p.get(pid) or {}).get("evidence", "")})

    raw = result["raw_score"]
    pen_total = result["penalty_points"]
    steps = [
        ("Level rule", "v2.2: level = check ceiling (raised to anchor floor, then caps); judge may only lower it with a downgrade_reason"
         if rules == "v2.2" else "v2.1: level = min(judge level, check ceiling), then anchors and caps"),
        ("Raw score (sum of points)", raw),
        ("Penalties", -pen_total if pen_total else 0),
        ("After penalties", round(raw - pen_total, 1)),
        ("Gate cap" + (f" ({', '.join(result['gates_triggered'])})" if result["cap"] else ""), result["cap"] if result["cap"] else "none"),
        ("Final score", result["final_score"]),
    ]

    shortfalls = []
    for row in sorted([r for r in rows if r["Lost"]], key=lambda r: -r["Lost"]):
        c = judged.get(row["ID"], {})
        fails = [k for k in c.get("checks", []) if k.get("result") == "fail"]
        tags = c.get("failed_tags") or {}
        shortfalls.append({"id": row["ID"], "name": row["Criterion"], "lost": row["Lost"], "level": row["Final level"],
                           "rationale": c.get("rationale", ""), "adjustments": row["Rule adjustments"],
                           "failed_checks": [{"check": k["id"], "description": k.get("description", ""), "evidence": k.get("evidence", ""),
                                              "owner": {"T": "Template / CMS", "A": "Author"}.get(tags.get(k["id"]), "Author")} for k in fails]})

    evidence = []
    for c in judge.get("criteria", []):
        for k in c.get("checks", []):
            evidence.append({"Criterion": c["id"], "Check": k.get("id"), "Description": k.get("description", ""),
                             "Result": k.get("result"), "Evidence type": k.get("evidence_type", "quote"),
                             "Evidence": k.get("evidence", ""), "Where": k.get("location", ""),
                             "Quote verified": {True: "yes", False: "NOT FOUND", None: ""}.get(k.get("quote_verified"), "")})

    return {"result": result, "rows": rows, "gates": gate_rows, "penalties": pen_rows, "steps": steps,
            "shortfalls": shortfalls, "evidence": evidence, "downgrades": downgrades,
            "weights_version": W.get("version"), "rules": rules}

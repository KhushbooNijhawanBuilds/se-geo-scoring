#!/usr/bin/env python3
"""Deterministic Content GEO Score calculator.

Takes the judge JSON (schema in references/judge-protocol.md §3) and computes:
checks → level ceiling, final levels, stage-adjusted renormalized weights, penalties,
gate caps, final 0–100 score, band, and per-criterion impact points (for prioritizing
recommendations). Stdlib only.

Usage:
  python geo_score_calc.py --judge judge.json [--weights ../assets/weights.json] [--md]
  python geo_score_calc.py --selftest
  python geo_score_calc.py --template pdp            # prints an empty judge JSON skeleton
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WEIGHTS = os.path.join(HERE, "..", "assets", "weights.json")
TYPE_ALIASES = {
    "product detail page": "pdp", "product": "pdp", "pdp": "pdp",
    "range": "range", "product range": "range", "page range": "range",
    "category": "category", "product category": "category", "page category": "category",
    "caas": "caas", "caas block": "caas", "block": "caas", "object description": "caas",
    "editorial": "editorial", "editorial page": "editorial",
    "article": "article", "blog": "article", "article/blog": "article", "blog post": "article",
    "document": "document", "whitepaper": "whitepaper_gateway", "catalog": "document", "guide": "document", "manual": "document",
    "datasheet": "datasheet", "data sheet": "datasheet",
    "case study": "case_study", "case_study": "case_study", "customer story": "case_study",
    "comparison": "comparison", "selection guide": "comparison", "buying guide": "comparison",
    "faq": "faq", "support": "faq", "faq/support": "faq",
    "glossary": "glossary", "solution": "solution", "solution page": "solution", "industry page": "solution",
    "video": "video",
    "news": "news", "press release": "news", "news / press release": "news", "newsroom": "news",
    "calculator": "calculator", "tradeoff tool": "calculator", "calculator / tradeoff tool": "calculator", "tool": "calculator",
    "service": "service", "service page": "service", "services": "service",
    "service project": "service_project", "modernization service": "service_project", "consulting service": "service_project",
    "software": "software_product", "software page": "software_product", "software product": "software_product",
    "software hub": "software_hub", "software portfolio": "software_hub", "software trial": "software_trial",
    "white paper": "whitepaper_gateway", "white paper / technical document": "whitepaper_gateway", "whitepaper gateway": "whitepaper_gateway",
    "white paper document": "whitepaper_doc", "whitepaper doc": "whitepaper_doc",
    "esg report": "esg_report", "sustainability report": "esg_report", "sustainability / esg report": "esg_report",
    "esg hub": "esg_hub", "sustainability hub": "esg_hub", "esg report document": "esg_report_doc",
    "customer success story": "case_study", "product range page": "range", "master range": "range", "blog article": "article",
}
STAGES = ["Awareness", "Education", "Consideration", "Evaluation", "Decision"]


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def family_of(cid, fams):
    for fam, ids in fams.items():
        if cid in ids:
            return fam
    return None


def level_from_checks(cid, checks, proposed):
    app = [c for c in checks if c.get("result") in ("pass", "fail")]
    n, p = len(app), sum(1 for c in app if c["result"] == "pass")
    na_share = 1 - (n / len(checks)) if checks else 1
    if n == 0 or na_share > 0.5:
        return None, n, p  # dropped (N/A)
    if cid == "U2":  # anchor table: passes → level, 5 only with all 4 + judge says 5
        ceiling = min(p, 4) + (1 if p == n and n >= 4 and proposed == 5 else 0)
    else:
        ceiling = 5 if p == n else min(4, round(5 * p / n))
    lvl = ceiling if proposed is None else min(int(proposed), ceiling)
    return max(0, lvl), n, p


def compute(judge, W, allow_missing=False):
    pinfo = judge.get("page", {})
    raw_t = str(pinfo.get("type", "")).strip().lower()
    ptype = TYPE_ALIASES.get(raw_t, raw_t.replace(" ", "_").replace("/", "_"))
    if ptype not in W["page_types"]:
        raise SystemExit(f"Unknown page type '{pinfo.get('type')}'. Known: {sorted(W['page_types'])}")
    stage = str(pinfo.get("stage", "")).strip().capitalize()
    if stage not in STAGES:
        raise SystemExit(f"Unknown stage '{pinfo.get('stage')}'. Use one of {STAGES}")
    defaults = W["page_types"][ptype]
    mult = W["stage_multipliers"][stage]
    judged = {c["id"]: c for c in judge.get("criteria", [])}
    warnings = []

    missing = [cid for cid in defaults if cid not in judged]
    if missing and not allow_missing:
        raise SystemExit(f"Judge output missing criteria {missing}. Re-run the judge, or pass --allow-missing to treat them as N/A.")
    if missing:
        warnings.append(f"Treated as N/A (not judged): {missing}")

    gates = {g["id"]: g for g in judge.get("gates", []) if g.get("triggered")}
    zero_ids, max_levels = set(), {}
    for gid in gates:
        gdef = W["gates"].get(gid, {})
        zero_ids.update(gdef.get("zero", []))
        max_levels.update(gdef.get("max_level", {}))

    rows = []
    for cid, w in defaults.items():
        c = judged.get(cid)
        if not c:
            continue
        lvl, n, p = level_from_checks(cid, c.get("checks", []), c.get("proposed_level"))
        if lvl is None:
            warnings.append(f"{cid} dropped (all/most checks N/A); weight redistributed")
            continue
        if c.get("proposed_level") is not None and int(c["proposed_level"]) > lvl:
            warnings.append(f"{cid}: judge proposed {c['proposed_level']} but checks support max {lvl}; using {lvl}")
        if cid in zero_ids:
            lvl = 0
        if cid in max_levels:
            lvl = min(lvl, max_levels[cid])
        fam = family_of(cid, W["families"])
        rows.append({"id": cid, "default_w": w, "family": fam or "other", "m": mult.get(fam, 1.0) if fam else 1.0,
                     "level": lvl, "checks_passed": f"{p}/{n}", "rationale": c.get("rationale", ""),
                     "confidence": c.get("confidence", "medium")})

    total = sum(r["default_w"] * r["m"] for r in rows)
    raw = 0.0
    for r in rows:
        r["eff_w"] = round(r["default_w"] * r["m"] * 100 / total, 2)
        r["points"] = round(r["level"] / 5 * r["eff_w"], 2)
        r["impact_points"] = round((5 - r["level"]) / 5 * r["eff_w"], 2)
        raw += r["points"]

    pen_total, pen_applied = 0, []
    for pen in judge.get("penalties", []):
        if pen.get("applied") and pen.get("id") in W["penalties"]:
            pen_total += W["penalties"][pen["id"]]
            pen_applied.append(pen["id"])
    pen_total = min(pen_total, W["penalty_cap"]) if "hidden_instructions" not in pen_applied else max(pen_total, 10)

    cap = min([W["gates"][g]["cap"] for g in gates if g in W["gates"]] or [100])
    final = max(0.0, min(cap, raw - pen_total))
    final_i = int(round(final))
    band = next(name for lo, name in W["bands"] if final_i >= lo)
    low_conf_w = sum(r["eff_w"] for r in rows if r["confidence"] == "low")
    return {
        "page": pinfo, "page_type_key": ptype, "stage": stage,
        "raw_score": round(raw, 1), "penalties": pen_applied, "penalty_points": pen_total,
        "gates_triggered": sorted(gates), "cap": cap if cap < 100 else None,
        "final_score": final_i, "band": band, "meets_threshold": final_i >= W["ok_threshold"],
        "confidence": "low (indicative only)" if low_conf_w > 33 else "medium" if low_conf_w > 10 else "high",
        "criteria": sorted(rows, key=lambda r: -r["impact_points"]),
        "warnings": warnings, "weights_version": W.get("version"),
        "disclaimer": "Citation-readiness of content only; actual AI citation also depends on retrieval, off-site consensus and technical access.",
    }


def to_md(res):
    L = [f"**Content GEO Score: {res['final_score']}/100 — {res['band']}**  (raw {res['raw_score']}, penalties −{res['penalty_points']}"
         + (f", capped at {res['cap']} by {', '.join(res['gates_triggered'])}" if res["cap"] else "") + f"; confidence {res['confidence']})",
         "", f"Page type: {res['page_type_key']} · Stage: {res['stage']} · Meets threshold: {'yes' if res['meets_threshold'] else 'no'}", "",
         "| Criterion | Eff. weight | Level (0–5) | Points | Recoverable | Checks | Rationale |", "|---|---|---|---|---|---|---|"]
    def natkey(r):
        pre, _, num = r["id"].partition("-") if "-" in r["id"] else (r["id"][0], "", r["id"][1:])
        return (pre != "U", pre, int(num) if num.isdigit() else 0)
    for r in sorted(res["criteria"], key=natkey):
        L.append(f"| {r['id']} | {r['eff_w']} | {r['level']} | {r['points']} | {r['impact_points']} | {r['checks_passed']} | {r['rationale'][:120]} |")
    if res["warnings"]:
        L += ["", "Warnings:"] + [f"- {w}" for w in res["warnings"]]
    L += ["", f"_{res['disclaimer']}_"]
    return "\n".join(L)


def template(ptype, W):
    key = TYPE_ALIASES.get(ptype.lower(), ptype)
    crit = [{"id": cid, "checks": [{"id": "c1", "result": "pass|fail|na", "evidence": "", "location": ""}],
             "rationale": "", "proposed_level": 0, "confidence": "high"} for cid in W["page_types"][key]]
    return {"page": {"id": "", "type": key, "stage": "Evaluation", "topic": "", "industry": "", "target_prompts": [], "prompts_inferred": True},
            "criteria": crit, "gates": [{"id": g, "triggered": False, "evidence": ""} for g in W["gates"]],
            "penalties": [{"id": p, "applied": False, "evidence": ""} for p in W["penalties"]],
            "out_of_scope_observations": [], "stage_fit": {"fits": True, "note": ""}}


def selftest(W):
    ok = True
    for t, ws in W["page_types"].items():
        s = sum(ws.values())
        if s != 100:
            print(f"FAIL weights for {t} sum to {s}"); ok = False
    allfam = [i for ids in W["families"].values() for i in ids]
    if len(allfam) != len(set(allfam)):
        print("FAIL criterion appears in two families"); ok = False
    j = template("pdp", W)
    for c in j["criteria"]:
        c["checks"] = [{"id": "c1", "result": "pass"}, {"id": "c2", "result": "fail"}]
        c["proposed_level"] = 5
    r = compute(j, W)
    assert r["final_score"] == round(sum(x["points"] for x in r["criteria"])), r
    lv = {x["id"]: x["level"] for x in r["criteria"]}
    assert lv["U2"] == 1 and lv["PDP-1"] == min(4, round(2.5)), lv  # judge's 5 is capped by checks
    j["gates"][0]["triggered"] = True
    r2 = compute(j, W)
    assert r2["final_score"] <= 59 and next(x for x in r2["criteria"] if x["id"] == "U8")["level"] == 0
    print("SELFTEST OK" if ok else "SELFTEST FAILED")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--judge")
    ap.add_argument("--weights", default=DEFAULT_WEIGHTS)
    ap.add_argument("--md", action="store_true", help="markdown score card instead of JSON")
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--template", metavar="PAGE_TYPE")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    W = load(a.weights)
    if a.selftest:
        sys.exit(0 if selftest(W) else 1)
    if a.template:
        print(json.dumps(template(a.template, W), indent=2)); return
    if not a.judge:
        ap.error("--judge is required")
    res = compute(load(a.judge), W, a.allow_missing)
    print(to_md(res) if a.md else json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Deterministic Blog SEO Score v1 calculator (stdlib only, Python 3.9+).

Mirrors geo_score_calc.py (Content GEO Score v2.1): checks -> level ceiling (half-up),
anchors and caps from seo_weights.json, criteria with >half na dropped and weights
renormalised, gate caps (lowest wins), penalties (capped at -10 except hidden/spam),
band. Adds a separate pass/fail Technical eligibility block. Never blends with GEO.

Judge JSON:
  {"page": {"url": ..., "title": ..., "keyword": ...},
   "criteria": [{"id": "S1", "proposed_level": 3, "rationale": "", "confidence": "high",
                 "checks": [{"id": "c1", "result": "pass|fail|na", "evidence": "..."}]}],
   "gates": [{"id": "SG1", "triggered": false, "evidence": ""}],
   "penalties": [{"id": "keyword_stuffing", "applied": false, "evidence": ""}],
   "eligibility": [{"id": "E1", "result": "pass|fail|na", "evidence": ""}]}

Usage:
  python3 seo_score_calc.py --judge judge.json [--weights seo_weights.json] [--md]
  python3 seo_score_calc.py --selftest
  python3 seo_score_calc.py --template
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_WEIGHTS = os.path.join(HERE, "seo_weights.json")
DISCLAIMER = ("On-page SEO quality and hygiene only. It does not predict rankings: links, click behaviour, "
              "site authority and Core Web Vitals are outside the score (see Needs data).")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _half_up(x):
    return int(x + 0.5)


def _anchor_met(req, res):
    if isinstance(req, dict) and "any" in req:
        return sum(1 for v in res.values() if v == "pass") >= req["any"]
    vals = [res.get(c) for c in req]
    return all(v in ("pass", "na") for v in vals) and any(v == "pass" for v in vals)


def _apply_caps(lvl, caps, res):
    applied = []
    for cap in caps or []:
        hit = False
        if "unless_pass" in cap:
            hit = any(res.get(c) == "fail" for c in cap["unless_pass"])
        if "if_all_fail" in cap:
            hit = all(res.get(c) == "fail" for c in cap["if_all_fail"])
        if hit and lvl > cap["max"]:
            lvl = cap["max"]
            applied.append(cap.get("why", f"cap {cap['max']}"))
    return lvl, applied


def level_from_checks(cid, checks, proposed, W=None):
    """Returns (level or None if dropped, n applicable, p passed, notes)."""
    W = W or {}
    res = {c.get("id"): c.get("result") for c in checks}
    app = [c for c in checks if c.get("result") in ("pass", "fail")]
    n, p = len(app), sum(1 for c in app if c["result"] == "pass")
    na_share = 1 - (n / len(checks)) if checks else 1
    if n == 0 or na_share > 0.5:
        return None, n, p, []
    ceiling = 5 if p == n else min(4, _half_up(5 * p / n))
    lvl = ceiling if proposed is None else min(int(proposed), ceiling)
    start, why = lvl, []
    anchors = (W.get("level_anchors") or {}).get(cid)
    if anchors:
        for L in (4, 3):
            req = anchors.get(str(L))
            if req and _anchor_met(req, res) and lvl < L:
                why.append(f"anchor: checks meet the level-{L} definition (judge proposed {proposed})")
                lvl = L
                break
    lvl, applied = _apply_caps(lvl, (W.get("level_caps") or {}).get(cid), res)
    why += [f"rubric cap: {a}" for a in applied]
    notes = [f"level {start} -> {lvl} ({'; '.join(why)})"] if lvl != start else []
    return max(0, lvl), n, p, notes


def eligibility_status(elig, W):
    E = W["eligibility"]
    rows, blocking_fail, warn, unknown = [], [], [], []
    got = {e["id"]: e for e in elig or []}
    for eid, d in E.items():
        e = got.get(eid, {"result": "na", "evidence": "not checked"})
        rows.append({"id": eid, "name": d["name"], "result": e.get("result", "na"), "evidence": e.get("evidence", "")})
        if e.get("result") == "fail":
            (blocking_fail if d["blocking"] else warn).append(eid)
        elif e.get("result") not in ("pass", "fail") and d["blocking"]:
            unknown.append(eid)
    status = ("Not eligible" if blocking_fail else "Eligible with warnings" if warn
              else "Eligible (unverified: " + ", ".join(unknown) + ")" if unknown else "Eligible")
    return status, rows


def compute(judge, W, allow_missing=False):
    crit = W["criteria"]
    judged = {c["id"]: c for c in judge.get("criteria", [])}
    warnings = []
    missing = [cid for cid in crit if cid not in judged]
    if missing and not allow_missing:
        raise SystemExit(f"Judge output missing criteria {missing}. Re-run the judge, or pass --allow-missing.")
    if missing:
        warnings.append(f"Treated as N/A (not judged): {missing}")
    unknown = [cid for cid in judged if cid not in crit]
    if unknown:
        warnings.append(f"Ignored unknown criteria {unknown}")

    gates = {g["id"]: g for g in judge.get("gates", []) if g.get("triggered")}
    zero_ids = set()
    for gid in gates:
        zero_ids.update(W["gates"].get(gid, {}).get("zero", []))

    rows = []
    for cid, d in crit.items():
        c = judged.get(cid)
        if not c:
            continue
        lvl, n, p, notes = level_from_checks(cid, c.get("checks", []), c.get("proposed_level"), W)
        if lvl is None:
            warnings.append(f"{cid} dropped (more than half its checks N/A); weight redistributed")
            continue
        if c.get("proposed_level") is not None and int(c["proposed_level"]) > lvl and not notes:
            warnings.append(f"{cid}: judge proposed {c['proposed_level']} but checks support max {lvl}; using {lvl}")
        for note in notes:
            warnings.append(f"{cid}: {note}; using {lvl}")
        if cid in zero_ids:
            lvl = 0
        failed = [ch["id"] for ch in c.get("checks", []) if ch.get("result") == "fail"]
        rows.append({"id": cid, "name": d["name"], "default_w": d["weight"], "level": lvl,
                     "checks_passed": f"{p}/{n}", "failed_checks": failed, "rationale": c.get("rationale", ""),
                     "confidence": c.get("confidence", "medium")})

    total = sum(r["default_w"] for r in rows) or 1
    raw = 0.0
    for r in rows:
        r["eff_w"] = round(r["default_w"] * 100 / total, 2)
        r["points"] = round(r["level"] / 5 * r["eff_w"], 2)
        r["recoverable"] = round((5 - r["level"]) / 5 * r["eff_w"], 2)
        raw += r["points"]

    pen_total, pen_applied = 0, []
    for pen in judge.get("penalties", []):
        if pen.get("applied") and pen.get("id") in W["penalties"]:
            pen_total += W["penalties"][pen["id"]]
            pen_applied.append(pen["id"])
    uncapped = [p for p in pen_applied if p in W.get("penalty_uncapped", [])]
    pen_total = max(pen_total, 10) if uncapped else min(pen_total, W["penalty_cap"])
    if uncapped:
        warnings.append(f"FLAG: {uncapped} applied - penalty cap lifted; escalate for manual review")

    cap = min([W["gates"][g]["cap"] for g in gates if g in W["gates"]] or [100])
    final = max(0.0, min(cap, raw - pen_total))
    final_i = int(final + 0.5)
    band = next(name for lo, name in W["bands"] if final_i >= lo)
    borderline = any(abs(final_i - b) <= 3 for b in (40, 70, 90))
    low_conf_w = sum(r["eff_w"] for r in rows if r["confidence"] == "low")
    status, erows = eligibility_status(judge.get("eligibility"), W)
    return {
        "page": judge.get("page", {}),
        "raw_score": round(raw, 1), "penalties": pen_applied, "penalty_points": pen_total,
        "gates_triggered": sorted(gates), "cap": cap if cap < 100 else None,
        "final_score": final_i, "band": band, "meets_threshold": final_i >= W["ok_threshold"],
        "borderline": borderline,
        "confidence": "low (indicative only)" if low_conf_w > 33 else "medium" if low_conf_w > 10 else "high",
        "criteria": sorted(rows, key=lambda r: -r["recoverable"]),
        "eligibility_status": status, "eligibility": erows,
        "needs_data": W.get("needs_data", []),
        "warnings": warnings, "weights_version": W.get("version"), "disclaimer": DISCLAIMER,
    }


def to_md(res):
    L = [f"**Blog SEO Score: {res['final_score']}/100 — {res['band']}**  (raw {res['raw_score']}, penalties −{res['penalty_points']}"
         + (f", capped at {res['cap']} by {', '.join(res['gates_triggered'])}" if res["cap"] else "")
         + f"; confidence {res['confidence']})" + ("  Borderline: confirm with 3 runs, use the median." if res["borderline"] else ""),
         "", f"**Technical eligibility: {res['eligibility_status']}** (reported beside the score, not in points)", "",
         "| Criterion | Name | Eff. weight | Level (0–5) | Points | Recoverable | Checks | Rationale |",
         "|---|---|---|---|---|---|---|---|"]
    for r in sorted(res["criteria"], key=lambda r: int(r["id"][1:])):
        L.append(f"| {r['id']} | {r['name']} | {r['eff_w']} | {r['level']} | {r['points']} | {r['recoverable']} | {r['checks_passed']} | {r['rationale'][:110]} |")
    L += ["", "| Eligibility | Check | Result | Evidence |", "|---|---|---|---|"]
    for e in res["eligibility"]:
        L.append(f"| {e['id']} | {e['name']} | {e['result']} | {str(e['evidence'])[:100]} |")
    if res["warnings"]:
        L += ["", "Warnings:"] + [f"- {w}" for w in res["warnings"]]
    L += ["", "Needs data (site level, not scored): " + "; ".join(f"{n['item']} [{n['source']}]" for n in res["needs_data"]),
          "", f"_{res['disclaimer']}_"]
    return "\n".join(L)


def template(W):
    return {"page": {"url": "", "title": "", "keyword": "", "keyword_inferred": True},
            "criteria": [{"id": cid, "proposed_level": 0, "rationale": "", "confidence": "high",
                          "checks": [{"id": f"c{i}", "result": "pass|fail|na", "evidence": ""} for i in range(1, d["checks"] + 1)]}
                         for cid, d in W["criteria"].items()],
            "gates": [{"id": g, "triggered": False, "evidence": ""} for g in W["gates"]],
            "penalties": [{"id": p, "applied": False, "evidence": ""} for p in W["penalties"]],
            "eligibility": [{"id": e, "result": "pass|fail|na", "evidence": ""} for e in W["eligibility"]]}


def selftest(W):
    ok = True

    def check(cond, msg):
        nonlocal ok
        if not cond:
            print("FAIL", msg)
            ok = False
    s = sum(d["weight"] for d in W["criteria"].values())
    check(s == 100, f"weights sum to {s}")
    for cid, d in W["criteria"].items():
        check(3 <= d["checks"] <= 6, f"{cid} has {d['checks']} checks (need 3-6)")
    stray = [k for k in list(W["level_anchors"]) + list(W["level_caps"]) if not k.startswith("_") and k not in W["criteria"]]
    check(not stray, f"anchors/caps reference unknown criteria {stray}")
    # all pass + proposed 5 -> 100, Excellent, eligible
    j = template(W)
    for c in j["criteria"]:
        c["checks"] = [dict(ch, result="pass", evidence="x") for ch in c["checks"]]
        c["proposed_level"] = 5
    j["eligibility"] = [dict(e, result="pass") for e in j["eligibility"]]
    r = compute(j, W)
    check(r["final_score"] == 100 and r["band"] == "Excellent" and r["eligibility_status"] == "Eligible", r["final_score"])
    # half-up: 2 of 4 -> 3 ; 1 of 4 -> 1 (1.25) ; 3 of 5 -> 3
    four = [{"id": f"c{i}", "result": v} for i, v in enumerate(["pass", "pass", "fail", "fail"], 1)]
    check(level_from_checks("S5", four, 5, W)[0] == 3, "2/4 should give 3")
    check(level_from_checks("S5", four[:1] + [dict(four[2], id="c2"), dict(four[2], id="c3"), dict(four[2], id="c4")], 5, W)[0] == 1, "1/4 -> 1")
    # judge proposal lower than ceiling is respected
    check(level_from_checks("S5", four, 2, W)[0] == 2, "proposal 2 respected")
    # drop when > half na
    nas = [{"id": "c1", "result": "pass"}, {"id": "c2", "result": "na"}, {"id": "c3", "result": "na"}]
    check(level_from_checks("S12", nas, 5, W)[0] is None, "S12 with 2/3 na should drop")
    # cap: S2 c1 fail -> 0
    s2 = [{"id": "c1", "result": "fail"}] + [{"id": f"c{i}", "result": "pass"} for i in range(2, 7)]
    check(level_from_checks("S2", s2, 4, W)[0] == 0, "S2 cap")
    s2b = [{"id": "c1", "result": "pass"}, {"id": "c2", "result": "fail"}] + [{"id": f"c{i}", "result": "pass"} for i in range(3, 7)]
    check(level_from_checks("S2", s2b, 4, W)[0] == 3, "S2 length cap -> 3")
    # anchor: S1 c1+c2+c4 pass, c3,c5 fail -> ceiling 3 (3/5=3), judge proposes 2 -> anchor raises to 3
    s1 = [{"id": "c1", "result": "pass"}, {"id": "c2", "result": "pass"}, {"id": "c3", "result": "fail"},
          {"id": "c4", "result": "pass"}, {"id": "c5", "result": "fail"}]
    check(level_from_checks("S1", s1, 2, W)[0] == 3, "S1 anchor")
    # gates: lowest cap wins; SG5 zeroes S5
    j["gates"][3]["triggered"] = True   # SG4 49
    j["gates"][4]["triggered"] = True   # SG5 59
    r2 = compute(j, W)
    check(r2["final_score"] == 49 and r2["cap"] == 49, f"gate cap {r2['final_score']}")
    check(next(x for x in r2["criteria"] if x["id"] == "S5")["level"] == 0, "SG5 zeroes S5")
    # penalties capped at 10, hidden lifts the cap
    j["gates"] = [dict(g, triggered=False) for g in j["gates"]]
    for p in j["penalties"]:
        p["applied"] = p["id"] in ("keyword_stuffing", "self_ranking", "superseded_no_notice", "fluff_intro", "boilerplate_dominant")
    r3 = compute(j, W)
    check(r3["penalty_points"] == 10 and r3["final_score"] == 90, f"penalty cap {r3['penalty_points']}")
    for p in j["penalties"]:
        p["applied"] = p["id"] in ("hidden_text_or_links", "keyword_stuffing", "fluff_intro")
    r4 = compute(j, W)
    check(r4["penalty_points"] == 15, f"uncapped penalties {r4['penalty_points']}")
    # eligibility blocking fail
    j["eligibility"][1]["result"] = "fail"
    check(compute(j, W)["eligibility_status"] == "Not eligible", "E2 fail -> Not eligible")
    j["eligibility"][1]["result"] = "pass"
    j["eligibility"][5]["result"] = "fail"
    check(compute(j, W)["eligibility_status"] == "Eligible with warnings", "E6 fail -> warnings")
    # renormalisation when a criterion is dropped
    j2 = template(W)
    for c in j2["criteria"]:
        c["checks"] = [dict(ch, result="pass") for ch in c["checks"]]
        c["proposed_level"] = 5
    j2["criteria"][11]["checks"] = [{"id": "c1", "result": "na"}, {"id": "c2", "result": "na"}, {"id": "c3", "result": "pass"}]
    r5 = compute(j2, W)
    check(abs(sum(x["eff_w"] for x in r5["criteria"]) - 100) < 0.1 and r5["final_score"] == 100, "renormalisation")
    print("SELFTEST OK" if ok else "SELFTEST FAILED")
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--judge")
    ap.add_argument("--weights", default=DEFAULT_WEIGHTS)
    ap.add_argument("--md", action="store_true", help="markdown score card instead of JSON")
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--template", action="store_true")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    W = load(a.weights)
    if a.selftest:
        sys.exit(0 if selftest(W) else 1)
    if a.template:
        print(json.dumps(template(W), indent=2))
        return
    if not a.judge:
        ap.error("--judge is required")
    res = compute(load(a.judge), W, a.allow_missing)
    print(to_md(res) if a.md else json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

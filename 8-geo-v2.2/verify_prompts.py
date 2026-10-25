#!/usr/bin/env python3
"""Verification (v2.2).
0. engine selftest passes.
1. For every page-type key: the STEP 4 table in prompts/copilot_prompt_<key>_v2.2.txt equals the effective
   weights computed by geo_score_calc.compute(); JSON page.type == key; listed criterion ids == weights.json;
   every criterion appears in STEP 1.
2. Backward compatibility: every v2.1 pilot judge file (research/final-scoring/judgeA/<id>.json) run through the
   v2.2 engine with rules="v2.1" reproduces the v2.1 CSV final score (the v2.2 rules are reported by rerun_testrun.py).
Writes verification_report.md; exits 1 on any mismatch."""
import csv, glob, json, os, re, sys
from collections import defaultdict
from common import W, KEYS, STAGES, ROOT, FINAL, calc, eff_weights

fails, lines = [], []


def check_prompts():
    lines.append("## 1. Prompt stage-weight tables vs geo_score_calc.compute()\n")
    lines.append("| key | criteria | cells checked | max abs diff | page.type | ids | result |\n|---|---|---|---|---|---|---|")
    for k in KEYS:
        txt = open(os.path.join(ROOT, "prompts", f"copilot_prompt_{k}_v2.2.txt"), encoding="utf-8").read()
        sect = txt.split("STEP 4 - COMPUTE")[1].split("If a criterion is dropped")[0]
        table = {}
        for ln in sect.splitlines():
            parts = ln.split()
            if len(parts) == 6 and parts[0] in W["page_types"][k]:
                table[parts[0]] = [float(x) for x in parts[1:]]
        ew = eff_weights(k)
        ok, cells, mx = True, 0, 0.0
        if set(table) != set(W["page_types"][k]):
            ok = False; fails.append(f"{k}: table ids {sorted(table)} != weights ids")
        for cid, vals in table.items():
            for s, v in zip(STAGES, vals):
                d = abs(v - ew[s][cid]); mx = max(mx, d); cells += 1
                if d > 1e-9:
                    ok = False; fails.append(f"{k} {cid} {s}: prompt {v} != engine {ew[s][cid]}")
        m = re.search(r'\{"page": \{"type": "([^"]+)"', txt)
        pt_ok = bool(m and m.group(1) == k)
        idl = re.search(r"Use these ids\. Criteria: ([^.]+)\.", txt).group(1).split(", ")
        ids_ok = idl == list(W["page_types"][k])
        step1 = txt.split("STEP 1")[1].split("STEP 2")[0]
        s1_ok = all(re.search(rf"^{re.escape(c)} ", step1, re.M) for c in W["page_types"][k])
        if not (pt_ok and ids_ok and s1_ok):
            ok = False; fails.append(f"{k}: page.type ok={pt_ok}, id list ok={ids_ok}, step1 ok={s1_ok}")
        sums = {s: round(sum(ew[s].values()), 2) for s in STAGES}
        lines.append(f"| {k} | {len(table)} | {cells} | {mx:.2f} | {'ok' if pt_ok else 'BAD'} | {'ok' if ids_ok and s1_ok else 'BAD'} | {'MATCH' if ok else 'MISMATCH'} (sums {', '.join(f'{v:.2f}' for v in sums.values())}) |")


def check_pilots():
    lines.append("\n## 2. Backward compatibility: v2.1 pilot (judgeA JSON -> v2.2 engine with rules=v2.1 -> v2.1 CSV final score)\n")
    rows = {r["﻿ID"] if "﻿ID" in r else r["ID"]: r for r in csv.DictReader(open(os.path.join(FINAL, "SE_GEO_scored_inventory_v2.1.csv"), encoding="utf-8"))}
    by_type = defaultdict(list)
    lines.append("| id | key | stage | CSV final | recomputed | stored _result.json | result |\n|---|---|---|---|---|---|---|")
    for f in sorted(glob.glob(os.path.join(FINAL, "judgeA", "*.json"))):
        pid = os.path.basename(f)[:-5]
        if pid.endswith("_result") or pid.startswith("_"):
            continue
        j = calc.load(f)
        r = calc.compute(j, W, allow_missing=True, rules="v2.1")
        stored = calc.load(f.replace(".json", "_result.json"))["final_score"] if os.path.exists(f.replace(".json", "_result.json")) else None
        csvf = int(rows[pid]["GEO score (final, v2.1)"]) if pid in rows else None
        ok = csvf == r["final_score"] and (stored is None or stored == r["final_score"])
        if not ok:
            fails.append(f"pilot {pid}: csv {csvf} recomputed {r['final_score']} stored {stored}")
        by_type[r["page_type_key"]].append(ok)
        lines.append(f"| {pid} | {r['page_type_key']} | {r['stage']} | {csvf} | {r['final_score']} | {stored} | {'MATCH' if ok else 'MISMATCH'} |")
    lines.append("\n| key | pilots reproduced | all match | >= 3 per type |\n|---|---|---|---|")
    for k in KEYS:
        v = by_type.get(k, [])
        lines.append(f"| {k} | {len(v)} | {'yes' if v and all(v) else ('n/a (untested)' if not v else 'NO')} | {'yes' if len(v) >= 3 else ('fewer than 3 pilots exist' if v else 'no pilots')} |")


def check_doc():
    """The standard's per-type effective-weight tables equal the engine (all 26 keys)."""
    doc = open(os.path.join(ROOT, "GEO_Scoring_Standard_All_Types_v2.2.md"), encoding="utf-8").read()
    ok_keys = 0
    for k in KEYS:
        sect = doc.split(f"### `{k}` - ")[1].split("**Effective weights by stage**")[1].split("**Gates that apply:**")[0]
        ew = eff_weights(k); seen = set(); bad = False
        for ln in sect.splitlines():
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cells) == 6 and cells[0] in W["page_types"][k]:
                seen.add(cells[0])
                if any(abs(float(v) - ew[s][cells[0]]) > 1e-9 for s, v in zip(STAGES, cells[1:])):
                    bad = True
        if bad or seen != set(W["page_types"][k]):
            fails.append(f"standard table mismatch for {k}")
        else:
            ok_keys += 1
    lines.append(f"\n## 1b. Standard (GEO_Scoring_Standard_All_Types_v2.2.md) effective-weight tables vs engine\n\n{ok_keys}/{len(KEYS)} keys match exactly.\n")


def check_selftest():
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ok = calc.selftest(W)
    lines.append(f"## 0. Engine selftest\n\n`geo_score_calc.py --selftest`: {buf.getvalue().strip()}\n")
    if not ok:
        fails.append("engine selftest failed")


if __name__ == "__main__":
    check_selftest(); check_prompts(); check_doc(); check_pilots()
    head = ["# Verification report (generated by verify_prompts.py)\n", f"Weights: {W['version']}\n",
            f"**Result: {'ALL CHECKS PASS' if not fails else str(len(fails)) + ' MISMATCHES'}**\n"]
    if fails:
        head += ["Mismatches:\n"] + [f"- {x}" for x in fails] + [""]
    open(os.path.join(ROOT, "verification_report.md"), "w", encoding="utf-8").write("\n".join(head + lines) + "\n")
    print("\n".join(head))
    sys.exit(1 if fails else 0)

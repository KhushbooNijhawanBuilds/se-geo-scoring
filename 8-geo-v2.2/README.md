# 8-geo-v2.2: SE Content GEO Score v2.2, all page types

v2.2 applies the 17 fixes from the 60-page test run (`../7-geo-all-types/test-run/prompt_fixes_v2.2.md`); see `CHANGELOG-v2.2.md`. v2.1 (`../4-scoring-project-v2.1/`, `../7-geo-all-types/`) is untouched. Weights are unchanged (`weights_version` 2.2-2026-10-25).

**What changed for judges:** the judge no longer picks levels. The calculator sets each level to the check ceiling (with anchors and caps). The judge can only lower a level, with a `downgrade_reason` that names the weak passed check. Stages come from a per-type stage test, unless the user supplies one. Absence/layout checks may pass on a judge note. A missing block fails its checks instead of being na.

| File | What it is |
|---|---|
| `engine/geo_score_calc.py`, `engine/weights.json` | The v2.2 calculator and weights (copied from v2.1, then changed). `--rules v2.1` reproduces v2.1 exactly. |
| `GEO_Scoring_Standard_All_Types_v2.2.md` | The business-readable standard: overview, the 26 type sections, Appendix A (classifier + boundary rules), B (validation), C (source gaps). |
| `prompts/copilot_prompt_<key>_v2.2.txt` | 26 self-sufficient Copilot judge prompts. Each ends with a JSON block in the calculator's input shape. |
| `catalog.py` | Criterion names and checks, metadata per type, and the stage tests (`STAGE_TEST`). It holds no weights. |
| `common.py` | Loads `engine/weights.json`, imports the v2.2 engine, merges the catalogue and computes effective weights with the engine's `compute()`. |
| `build_prompts.py`, `build_docs.py` | Generate the prompts and the standard. |
| `verify_prompts.py` -> `verification_report.md` | Runs the engine selftest, checks that the prompt and standard weight tables equal the engine for all 26 keys, and confirms v2.1 pilot reproduction with `rules=v2.1`. |
| `rerun_testrun.py` -> `testrun_rerun_v2.2.md/.csv` | Re-scores the 62 test-run judge JSONs. It separates the level-rule effect from the other v2.2 engine rules. |
| `CHANGELOG-v2.2.md` | Each fix and what changed, with file and line. |

Rebuild after any change to `engine/weights.json` or `catalog.py`:

```
python3 build_prompts.py && python3 build_docs.py && python3 verify_prompts.py && python3 rerun_testrun.py
```

Score a judge JSON:

```
python3 engine/geo_score_calc.py --judge judge.json --md            # v2.2 rules
python3 engine/geo_score_calc.py --judge judge.json --rules v2.1 --md   # v2.1 level logic, for comparison
python3 engine/geo_score_calc.py --selftest
```

These types are still untested on SE pages: pdp, category, caas, editorial, document, datasheet, comparison, faq, glossary, video and whitepaper_doc.

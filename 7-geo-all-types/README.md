# 7-geo-all-types — SE Content GEO Score v2.1, all page types

This folder documents and packages exactly what the v2.1 engine does. The scoring logic is unchanged.

The source of truth is `../4-scoring-project-v2.1/GEO Elec Project/skill/geo-research/`, made of `assets/weights.json`, `scripts/geo_score_calc.py` and `references/*.md`.

| File | What it is |
|---|---|
| `GEO_Scoring_Standard_All_Types_v2.1.md` | A business-readable standard. It covers the overview (method, bands, levels, stages, U1–U10, gates G1–G13, penalties, judge rules) and one section for each of the 26 page-type keys. Appendices hold the decision tree, the validation status and the source gaps. |
| `prompts/copilot_prompt_<key>_v2.1.txt` | 26 self-sufficient Copilot judge prompts, one per key. You give the prompt a URL (and optionally a question); Copilot infers the topic, industry, stage and fan-outs. Each prompt ends with a JSON block in the calculator's input shape (`page.type` = key). |
| `catalog.py` | The hand-curated criterion names and checks (with a source tag for each) plus metadata per type. It holds no weights. |
| `common.py` | Loads `weights.json`, imports `geo_score_calc`, merges the catalogue and computes effective weights with the engine's own `compute()`. |
| `build_prompts.py` | Generates every prompt from one template derived from `3-prompts/copilot_prompt_blog_v2.1.txt`. |
| `build_docs.py` | Generates the standard. Every table comes from `weights.json`, the engine and the pilot CSV. The prose is hand-written in the script and in `source_gaps.md`. |
| `verify_prompts.py` | Checks that each prompt's stage-weight table equals the engine's values, along with the `page.type` and id lists. It also re-scores every pilot judge JSON and writes `verification_report.md`. |

Rebuild everything after any change to `weights.json` or `catalog.py`:

```
python3 build_prompts.py && python3 build_docs.py && python3 verify_prompts.py
```

To score the JSON block from a prompt, save it as `judge.json` and run:

```
python3 ../4-scoring-project-v2.1/GEO\ Elec\ Project/skill/geo-research/scripts/geo_score_calc.py --judge judge.json --md
```

Checks marked DERIVED, or "v1 split", in the standard were not written as binary checks in the source; see Appendix C. The following types are untested on SE pages: pdp, category, caas, editorial, document, datasheet, comparison, faq, glossary, video and whitepaper_doc.

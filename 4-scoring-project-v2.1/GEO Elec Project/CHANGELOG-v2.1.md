# SE Content GEO Scoring Standard — v2.1 (20 Oct 2026)

Bug-fix release of v2.0 (19 Oct 2026). The logic, weights and judge answers are unchanged; only how the code turns checks into levels, one gate, the tooling and the reference docs changed. All 61 scorings were re-computed from the existing judge JSONs.

## Fixes

| # | Bug (v2.0) | Fix (v2.1) | Files |
|---|---|---|---|
| 1 | Code ignored the rubric's level anchors. With exactly 2 of 4 (or 2 of 5) checks passing, banker's rounding gave level 2 even where the rubric defines that combination as level 3 | Anchors for U1, U3–U10 applied in code from the checks (`level_anchors`); ceiling rounds halves up | `scripts/geo_score_calc.py`, `assets/weights.json` |
| 2 | Caps written in criterion text ("U3 ≤ 2 if c5 fails", "SOL-5 c2 fail → ≤ 2", "undated → ≤ 1", …) relied on the judge remembering them | Encoded in `level_caps` and enforced by the calculator | same |
| 3 | Gate G1 (contradiction) zeroed DOC-6 "Customer language", a leftover from a draft numbering in which DOC-6 meant consistency | G1 zeroes U8 and BLK-4 only | `assets/weights.json`, `references/scoring-framework.md` |
| 4 | `consolidate.py` crashed: 8 pages had failed capture metadata (KeyError), and it used `statistics.correlation` (Python 3.10+) | Tolerates missing fields, computes Pearson itself, re-scores from judge JSONs, always writes a CSV | `research/final-scoring/consolidate.py` |
| 5 | Crawler-gap ratio missing for pages 4, 20, 21, 43, 44, 45, 47, 48 | Rebuilt from each rendered file's header and `corpus/index.json` (formula verified on all 50 intact entries). New finding: #21 Massmart has a crawler gap (0.65) | `research/corpus/rendered/index_rendered.json` |
| 6 | Final scores mixed methods: A/B mean for 13 double-judged pages, Judge A alone for 47 | Final = Judge A for every page; Judge B reported beside it with the two-judge mean as a sensitivity check | `consolidate.py` |
| 7 | Reference docs out of sync: v1 multiplier table, intake sheets without v2 types, judge protocol describing the old ceiling, SKILL.md pointing at v1 page types, one statistic mis-attributed | Multiplier table regenerated from `weights.json`; intake rows for news, service, software, calculator, white paper, ESG; judge protocol §3 rewritten; SKILL.md 2.1; Indig/Ahrefs attribution corrected; status banner on the type-analysis files | `references/*.md`, `SKILL.md`, `research/type-analysis/*.md` |

## Effect on scores

- 28 criterion levels changed on 18 scorings (14 of 61 final scores moved by 1–2 points; 47 unchanged). Mean change +0.07 points.
- Raised by anchors: e.g. white-paper gateways U8/U10 (2 → 3), solution U5/U6 (2 → 3).
- Lowered by caps: U3 to 2 where key facts sit only in tabs/carousels/widgets (solution, service, software hubs); one undated case study U9 to 1.
- One band change: #54 Davos/WEF release 38 → 40 (Poor → Average), because its fan-out checks meet the U6 level-3 definition. No page crosses the 70 threshold.
- `--legacy-levels` reproduces all 74 v2.0 judge results exactly (verified).

## Not fixed here (needs people, not code)

Human calibration raters, worked exemplars for the low-κ criteria (U2, U8, U10, U7, U1), pilots for PDP/Category/CaaS/Editorial/Datasheet, a 3-judgement median for pages within ±3 of a band edge (blog #02 at 71, Judge B 65), and quarterly validation against real AI answers.

## Outputs

`research/final-scoring/SE_GEO_scored_inventory_v2.1.xlsx` (and `.csv`), `agreement.md`, `agreement.json`; every `judgeA|B/<id>_result.json` and `<id>_score.md` regenerated.

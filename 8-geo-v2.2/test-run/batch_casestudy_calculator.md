# Batch: case studies (19-24) and calculators (31-36), GEO v2.2

Independent blind judge, using the v2.2 prompts (`copilot_prompt_case_study_v2.2.txt`, `copilot_prompt_calculator_v2.2.txt`). Page text came from `corpus/rendered/<file>`, which was richer for all 12 pages and had a matching URL header. I also used `corpus/<file>` for checks, because the plain copy holds the `<title>`/meta and the `ZZ_` placeholders. A script confirmed that every pass quote appears verbatim in the page text: 0 misses. Levels, caps and scores come from `engine/geo_score_calc.py` (rules v2.2). The earlier runs were opened only after all 12 pages had been judged.

Judge files: `test-run/judge/NN.json`. Results: `test-run/result/NN_result.json`.

| ID | key | stage | v2.2 score | band | prev run (stage) | v2.1 (stage) | diff vs prev / vs v2.1 | gates; penalties | top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|---|
| 19 | case_study | Consideration | **35** | Poor | 29 (Consideration) | 34 (Consideration) | +6 / +1 | G8; pen: template_artifact | CS-3 (+22.3); CS-1 (+10.4); CS-7 (+6.7) |
| 20 | case_study | Evaluation | **49** | Average | 42 (Evaluation) | 49 (Evaluation) | +7 / +0 | -; pen: cta_overload | CS-3 (+15.0); CS-1 (+9.0); CS-7 (+7.5) |
| 21 | case_study | Evaluation | **49** | Average | 44 (Evaluation) | 52 (Evaluation) | +5 / -3 | G1; pen: cta_overload | CS-3 (+10.0); CS-5 (+8.7); CS-7 (+7.5) |
| 22 | case_study | Evaluation | **50** | Average | 47 (Evaluation) | 55 (Consideration) | +3 / -5 | -; pen: - | CS-3 (+10.0); CS-5 (+8.7); CS-4 (+5.7) |
| 23 | case_study | Evaluation | **56** | Average | 54 (Evaluation) | 62 (Evaluation) | +2 / -6 | -; pen: template_artifact | CS-7 (+7.5); CS-1 (+6.7); U3 (+5.7) |
| 24 | case_study | Evaluation | **35** | Poor | 29 (Consideration) | 33 (Evaluation) | +6 / +2 | G8; pen: cta_overload | CS-3 (+25.0); CS-7 (+7.5); CS-1 (+6.7) |
| 31 | calculator | Evaluation | **40** | Average (borderline) | 28 (Evaluation) | 35 (Consideration) | **+12** / +5 | -; pen: - | CALC-1 (+11.1); CALC-2 (+10.1); CALC-3 (+7.8) |
| 32 | calculator | Evaluation | **64** | Average | 49 (Evaluation) | 64 (Evaluation) | **+15** / +0 | -; pen: template_artifact | CALC-2 (+10.1); CALC-3 (+3.9); U5 (+3.5) |
| 33 | calculator | Evaluation | **59** | Average | 59 (Evaluation) | 59 (Consideration) | +0 / +0 | G1; pen: template_artifact | CALC-3 (+3.9); U8 (+3.5); CALC-2 (+3.4) |
| 34 | calculator | Consideration | **51** | Average | 44 (Consideration) | 43 (Evaluation) | +7 / +8 | -; pen: template_artifact | CALC-3 (+15.2); CALC-2 (+7.9); U1 (+3.7) |
| 35 | calculator | Consideration | **62** | Average | 52 (Consideration) | 66 (Evaluation) | +10 / -4 | -; pen: template_artifact | CALC-3 (+6.1); CALC-2 (+5.3); U5 (+4.0) |
| 36 | calculator | Consideration | **16** | Poor | 13 (Consideration) | 16 (Evaluation) | +3 / +0 | G13, G6, G9; pen: - | CALC-1 (+16.2); CALC-3 (+15.2); CALC-2 (+13.2) |

Page 31 lands exactly on 40, which is borderline. The standard says to confirm it with 3 independent runs and take the median.

## Medians

| | case_study (6) | calculator (6) | all 12 |
|---|---|---|---|
| v2.2 (this run) | 49 | 55 | 49.5 |
| previous run (7-geo-all-types) | 43 | 46.5 | 44 |
| v2.1 final | 50.5 | 51 | 50.5 |

- v2.2 scores higher than the previous run on 11 of 12 pages; page 33 is unchanged. The median rises by about 5.
- v2.2 is close to v2.1: the median is 1 point lower, and the largest gap is 8 points (page 34).

## Stages (stage test)

- **Case studies:**
  - Page 22 (YVR) is Evaluation. This is the prompt's own example; v2.1 had Consideration.
  - Page 19 (McLaren) is Consideration under rule 2: a partnership/sponsorship showcase with no quantified result.
  - Page 24 (Zicaffè) is Evaluation. The previous run used Consideration. It has a named customer and a deployed offer, and it is not a sponsorship. See the ambiguity section.
- **Calculators:**
  - Pages 34, 35 and 36 are Consideration ("comparison" in the H1, rule 1). v2.1 had Evaluation.
  - Pages 32 and 33 are Evaluation (rule 2: price or size one design).
  - Page 31 falls back to the default, Evaluation: it computes a single metric, which matches no rule.

## Diffs over 10 points vs the previous run

- **32 (+15).** The previous judge marked the hidden tool-panel text NOT FOUND:
  - "About this tool": method, scope, the line "should not be used as formal quotations".
  - The cost breakdown and the NVIDIA rack-density ranges.
  - The white-paper CTAs.

  The v2.2 rule says hidden tool-panel text counts for CALC-1..5. That moves:
  - U1 c1, U2 c1/c4 and U10 c3 to pass.
  - CALC-3 c1-c3 and CALC-5 c2/c3 to pass.
  - CALC-3 from 1 to 4, U2 from 2 to 4, U1 from 2 to 3.

  Two checks went the other way: CALC-3 c4 now fails (results are only in the widget) and CALC-4 c4 fails (HV/MV/LV/OCP are not expanded).
- **31 (+12).** The previous run triggered **G6** (max 59). That did not cap the score but it set U3, and it failed CALC-3 c1 because 0.417 "appears only as widget output". In v2.2 the widget's own visible text is a text equivalent: inputs, the mix percentages, 0.417 and the benchmark factors in kg/kWh. So G6 does not fire, CALC-3 rises from 1 to 3, and U2 c1/c4 pass on the intro ("Use this TradeOff Tool…", "Learn what changes can be made…").
- **35 (+10, at the threshold).** The previous run triggered **G1** on the widget message "failure rate … 80.0%. Consider reducing this to 100% or below". v2.2 explicitly treats this as a runtime-output error: the template_artifact penalty (-2), not G1. U8 therefore goes from 0 to 4. CALC-3 c1 now passes on the default-scenario outputs ($70.1k / $43.9k).

Smaller, systematic differences against the previous run:
- U10 is higher on almost every page. Product cards and white-paper links count as a descriptive CTA or next-stage link.
- Under the v2.2 level rule, a 5 becomes 4 only through an explicit downgrade, so many criteria sit at 4 rather than 3.

## Gates and penalties found

- **G1, page 21:** "Over 155 BMS systems installed" vs "more than 250 of their stores". This is the standard's own example.
- **G1, page 33:** "A PUE of 1.8 would be considered typical" vs "A PUE of 1.4 would be considered typical". Also the standard's example.
- **G8, pages 19 and 24:** no quantified customer outcome.
- **G6, G9 and G13, page 36:** the tool iframe renders empty.
- **template_artifact:**
  - Pages 19 and 23: `ZZ_` placeholders.
  - Pages 33 and 35: "Lorum ipsum" UI kit.
  - Page 34: `#VALUE!`.
  - Pages 32 and 35: self-contradicting tool messages.
- **cta_overload:** pages 20, 21 and 24. Related-content widgets were excluded under judge rule 7, so they do not count toward cta_overload on the calculators.

## Remaining prompt ambiguity

1. **CS stage rule 2 vs 3 on pages without numbers (24 Zicaffè).** Rule 2 needs "no quantified result AND an approach or partnership showcase". A deployment story with no numbers meets only the first half, so it falls to Evaluation, where G8 and the empty CS-3 punish it. The previous judge chose Consideration. The prompt should state what to do when there are no results but there is a real deployment.
2. **Calculator stage when no rule matches (31).** A single-metric estimator ("emission factor") is not sizing, pricing or ROI. Rule 2 could be widened to "computes a metric for one chosen configuration" to make Evaluation explicit.
3. **Results that exist only in the widget.** CALC-3 c1 (a complete example in text/table) and c4 (results not only in the UI) overlap when the default-scenario numbers appear only as widget text. Judges can pass c1 and fail c4, or fail both, as the previous run did. Say whether widget-rendered text satisfies c1.
4. **Whether related-content widgets count for U10 c3/c4.** Judge rule 7 excludes related-content widgets, but U10 c4 asks for links to next-stage content, which usually live in "Related TradeOff Tools". I counted them for c4 and not for cta_overload. The prompt should say so explicitly.
5. **The level-5 to 4 downgrade ("not exceptional") is discretionary.** I applied it to every all-pass criterion. A judge who does not will score about +1 to +3 higher. Either make it mechanical or drop it.
6. **CS-6 card-grid cap (22).** "Card grids alone" was read as: c2 (role in text) fails, so downgrade to 2. Confirm that this is the trigger.
7. **U2 c2 (who).** Pages 32, 33 and 35 name a segment such as "data center deployments" or "retail stores" but no job role. I passed c2 and downgraded the criterion. Say whether a segment is enough.
8. **CS-3 c3 baseline.** For page 22, decide whether a year-on-year period ("between 2022 and 2023") counts as a baseline. I failed it.

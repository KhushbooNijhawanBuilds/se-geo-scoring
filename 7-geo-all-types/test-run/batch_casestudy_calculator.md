# Batch test: Customer success story (19–24) and Calculator / TradeOff Tool (31–36)

Judge: per-type prompts `copilot_prompt_case_study_v2.1.txt` and `copilot_prompt_calculator_v2.1.txt`, scored blind on corpus text (rendered version used for all 12 pages because it was richer; 20 was also checked against the raw file). Text in `[hidden]` tabs/panels was counted for the type criteria, as the prompt says, but it fails U3 c5 when key facts exist only there. Every pass quote was checked by script as a verbatim substring of the page text. Scores come from `geo_score_calc.py`. Files: `judge/<NN>.json`, `result/<NN>_result.json`.

| ID | type key | stage used (v2.1 stage) | new score | band | v2.1 score | diff | gates / penalties | top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|
| 19 | case_study | Consideration (Consideration) | 29 | Poor | 34 | -5 | G8 / pen: template_artifact, cta_overload | CS-3 (L0, +22.3); CS-1 (L1, +10.4); CS-7 (L0, +6.7) |
| 20 | case_study | Evaluation (Evaluation) | 42 | Average | 49 | -7 | – / pen: cta_overload | CS-3 (L2, +15.0); CS-1 (L1, +9.0); CS-7 (L0, +7.5) |
| 21 | case_study | Evaluation (Evaluation) | 44 | Average | 52 | -8 | G1 / pen: cta_overload | CS-3 (L3, +10.0); CS-5 (L0, +8.7); CS-7 (L0, +7.5) |
| 22 | case_study | Evaluation (Consideration) | 47 | Average | 55 | -8 | G6 | CS-3 (L3, +10.0); CS-5 (L0, +8.7); CS-4 (L1, +5.7) |
| 23 | case_study | Evaluation (Evaluation) | 54 | Average | 62 | -8 | – | CS-7 (L0, +7.5); CS-1 (L2, +6.7); CS-3 (L4, +5.0) |
| 24 | case_study | Consideration (Evaluation) | 29 | Poor | 33 | -4 | G8 / pen: cta_overload | CS-3 (L0, +22.3); CS-1 (L2, +7.8); CS-7 (L0, +6.7) |
| 31 | calculator | Evaluation (Consideration) | 28 | Poor | 35 | -7 | G6 | CALC-3 (L1, +15.6); CALC-1 (L1, +11.1); CALC-2 (L2, +10.2) |
| 32 | calculator | Evaluation (Evaluation) | 49 | Average | 64 | -15 | – | CALC-3 (L1, +15.6); CALC-2 (L2, +10.2); U1 (L2, +4.7) |
| 33 | calculator | Evaluation (Consideration) | 59 | Average | 59 | 0 | G1 / pen: template_artifact | CALC-3 (L4, +3.9); U8 (L0, +3.5); CALC-2 (L4, +3.4) |
| 34 | calculator | Consideration (Evaluation) | 44 | Average | 43 | +1 | – / pen: template_artifact | CALC-3 (L0, +15.2); CALC-2 (L2, +7.9); CALC-1 (L3, +6.5) |
| 35 | calculator | Consideration (Evaluation) | 52 | Average | 66 | -14 | G1 | CALC-3 (L1, +12.1); CALC-2 (L3, +5.3); U5 (L1, +4.0) |
| 36 | calculator | Consideration (Evaluation) | 13 | Poor | 16 | -3 | G6, G9, G13 | CALC-1 (L0, +16.2); CALC-3 (L0, +15.2); CALC-2 (L0, +13.2) |

## Per-type medians

| type key | new median | v2.1 median | median diff |
|---|---|---|---|
| case_study (n=6) | 43.0 | 50.5 | -7.5 |
| calculator (n=6) | 46.5 | 51.0 | -4.5 |

Ranking within each type stays close to v2.1. Case studies, from best to worst: 23 > 22 > 21 > 20 > 19 ≈ 24, the same order as v2.1. Calculators: 33 is top under both, 36 is bottom under both, and 32 and 35 drop the most. The new prompts score lower overall: −6 on average, and 10 of 12 pages are lower. No page changes band, except that 32 stays Average but falls from the 60s into the 40s.

## Differences over 10 points

- **32 Data center capital cost calculator (−15).** The difference comes from CALC-3 (worked example) at L1 and CALC-2 (assumptions) at L2. The page has a long list of assumptions, but most items carry no value or unit (e.g. "All chillers have variable frequency drives"). No source or data year is given, and the currency is "local" with no price year. So CALC-2 c2, c3 and c5 fail. The only visible results are the default-state UI figures ("Cooling: $ 10.3 M (11.7%)"). There is no complete inputs→outputs example and no benchmark such as $/W ranges. The v2.1 run put only +7.8 recoverable on CALC-3, which suggests it accepted the default UI state as a worked example. The new prompt's c1 ("complete example ... in text/table") and c4 ("not only a chart/UI") made me stricter. U1 c1 also failed: the opening names what is modelled but not its drivers, per the new U1 rule.
- **35 Edge UPS fleet management calculator (−14).** Mainly G1 (cap 59). The widget prints "The total failure rate of your assets is 80.0%. Consider reducing this to 100% or below.", which contradicts itself, so I triggered G1. That accounts for ~−7 by itself (raw 52.1 is under the cap, so the cap was not the binding factor). The rest of the gap: U8 is forced to 0 by G1; U5 is at L1 because the sources (Ponemon, Salary.com) have no year; CALC-3 is at L1 because there is no example, only a salary range. The stage was Consideration (comparing two approaches), not v2.1's Evaluation, so CALC-3 and CALC-2 carry less weight. That shift in itself would have *raised* the score. It is debatable whether a dynamic widget warning should count as page content for G1. Without G1, the page would be at roughly 55–56.

Smaller but systematic (−4 to −8) on the case studies:
- CS-1 c3/c4 (answer-shaped summary within the first ~150 words) and CS-7 (methodology) fail on almost every SE story.
- The judge-applied CS-6 "card grid alone ≤ 2" rule bit on 22.
- I triggered G1 on 21 because the counts disagree: "Over 155 BMS systems installed" vs "more than 250 of their stores" vs "hundreds of stores". This is a strict reading; v2.1 did not flag it. Without it, 21 would be ~50.
- I triggered G6 on 22, where the story narrative exists only in video and "Read the full story". This is also strict; v2.1 had no gate.

## Stage disagreements (6 of 12)

The prompts' stage rules are loose enough that the blind judge and v2.1 split on half the pages:
- 22: Evaluation vs Consideration.
- 24: Consideration vs Evaluation. I read it as an approach showcase.
- 31 and 33: Evaluation vs Consideration.
- 34, 35, 36: Consideration vs Evaluation. These are "compare" tools.

## Ambiguous or broken prompt wording to fix

1. **U9 anchor references a check that does not exist (case_study).** STEP 2c says `U9: 3 = c1+c2; 4 = c1+c2+c3`, but case_study U9 has only c1 and c2. The calculator then raised 22's U9 to 4 without any c3 being checked. The anchor should be removed or a c3 added. Other per-type prompts that have a 2-check U9 should be checked for the same problem.
2. **G1 says "U8 = 0", but the calculator logs it as an override.** The warning "U8: level 0 -> 3 (anchor ...)" appears before gates are applied. The final level is 0, so the result is correct, but the log reads like the judge was overruled. The order of anchors vs gates should be stated in the prompt, or the warning should be suppressed when a gate sets the level.
3. **The G13 cap is similarly logged as an anchor bump on U7 (36).** The final level is correctly 2.
4. **Stage guidance for calculators is ambiguous.** "Evaluation (sizing/ROI/TCO for a decision) or Consideration (comparing approaches)" does not settle cases like a "comparison calculator" that computes TCO (34/35/36), or a sizing tool (33) that v2.1 called Consideration. A tie-break rule is needed, e.g. "if the H1 says *comparison*, use Consideration".
5. **Case-study stage rule is circular.** It says "Evaluation by default; Consideration for approach showcases and brand partnerships", and then repeats the same text as "Natural stages". "Approach showcase" is not defined, so 24 could go either way.
6. **"Title/H1" in CS-1 c1/c2 is unclear.** Most SE stories have a slogan H1 and the customer name only in the `<title>`, which is meta. CS-2 says "meta-only facts fail", but CS-1 does not say whether the title tag counts. I counted the title for c1. Say explicitly.
7. **"Every pass needs a verbatim quote" vs structural checks.** U3 c3 (paragraph length), U8 c3 (no contradiction) and U1 c3 (position) are proven by absence or layout, not by a quote. I used a representative verbatim sentence. The prompt should allow an observation for these checks.
8. **Hidden/tab text rule (rule 7) vs U3 c5 for calculators.** Almost all of a TradeOff Tool's knowledge sits in `[hidden]` widget panels. Those panels count for CALC criteria but fail U3 c5 every time, and they invite G6 ("tool knowledge only inside the widget"). For 32–35 I did not trigger G6 because the panel text exists. For 31 and 36 I did trigger it. The line between "panel text counts" and "G6: only inside widget" needs a clear rule.
9. **The G1 threshold is unclear for live widget state.** On 35 a dynamic warning message, and on 34 a "#VALUE!" error, are runtime artefacts. Whether they count as content contradictions (G1) or template artefacts (penalty) should be specified. I applied G1 on 35 and template_artifact on 34.
10. **Typo:** the calculator anchors line says `U5: 4 = any 4` without saying "any 4 checks". It is readable, but loose.

## Notes

- Both medians fell, and the largest drops come from my stricter readings plus gates v2.1 did not raise (G1 on 21 and 35, G6 on 22 and 31). These are the cases to settle with a second blind judge.
- The prompts could not be applied consistently on two points: the stage tie-breaks (item 4) and the G6/hidden-panel boundary (item 8).

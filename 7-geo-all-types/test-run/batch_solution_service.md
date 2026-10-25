# Batch test: Solution (07–12) and Service (37–42) pages, per-type prompts v2.1

Judged blind from the corpus text, using `corpus/rendered/<file>` when it was richer (all but 38 and 42, where the server text was longer). Each judge followed `prompts/copilot_prompt_<key>_v2.1.txt`. A script checked that every PASS quote appears verbatim in the page text. Scores come from `geo_score_calc.py --judge judge/NN.json` and are saved in `result/NN_result.json`.

| ID | type key | stage used | new score | band | v2.1 score | diff | gates / penalties | top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|
| 07 | solution | Consideration (v2.1: Evaluation) | 33 | Poor | 22 | +11 | - | SOL-7 (+13.6); SOL-5 (+10.8); SOL-4 (+9.9) |
| 08 | solution | Consideration | 15 | Poor | 19 | -4 | G6 | SOL-2 (+12.9); SOL-7 (+10.8); SOL-4 (+9.9) |
| 09 | solution | Consideration | 29 | Poor | 39 | -10 | fluff_density | SOL-7 (+10.8); SOL-2 (+10.3); U1 (+7.2) |
| 10 | solution | Consideration (v2.1: Awareness) | 37 | Poor | 45 | -8 | - | SOL-7 (+13.6); SOL-2 (+12.9); U7 (+6.5) |
| 11 | solution | Consideration | 46 | Average | 41 | +5 | - | SOL-5 (+10.8); SOL-4 (+8.0); SOL-7 (+5.4) |
| 12 | solution | Consideration | 25 | Poor | 26 | -1 | - | SOL-7 (+13.6); SOL-5 (+10.8); SOL-2 (+10.3) |
| 37 | service | Evaluation | 48 | Average | 51 | -3 | - | SVC-2 (+11.9); SVC-3 (+8.9); SVC-7 (+6.3) |
| 38 | service_project | Consideration | 39 | Poor | 45 | -6 | cta_overload | SVC-7 (+10.3); SVC-4 (+7.6); SVC-2 (+6.7) |
| 39 | service_project | Consideration | 51 | Average | 45 | +6 | - | SVC-1 (+9.4); SVC-2 (+8.4); SVC-7 (+8.2) |
| 40 | service_project (v2.1: service) | Consideration | 17 | Poor | 19 | -2 | G13 | SVC-1 (+12.5); SVC-7 (+10.3); SVC-6 (+9.5) |
| 41 | service | Evaluation | 41 | Average | 43 | -2 | - | SVC-2 (+9.0); SVC-3 (+8.9); SVC-7 (+8.4) |
| 42 | service_project | Consideration (v2.1: Decision) | 31 | Poor | 25 | +6 | G13 | SVC-1 (+15.7); SVC-7 (+8.2); SVC-4 (+7.6) |

## Per-type median

| type key | n | new median | v2.1 median |
|---|---|---|---|
| solution | 6 | 31.0 | 32.5 |
| service | 2 | 44.5 | 47.0 |
| service_project | 4 | 35.0 | 35.0 |
Overall: the new scores track v2.1 closely. 11 of 12 are within ±10, and the mean absolute difference is 5.3. No band changed except 10 (Average → Poor, -8) and 38 (Average → Poor, -6). Two scores are borderline under the standard's rule (within 3 of 40, so 3 runs are needed): 38 = 39 and 41 = 41.

## Differences > 10 points

- **07 (+11, 33 vs 22).** The main cause is the stage. v2.1 scored this page at *Evaluation* (a product-solution page). The prompt says to default to Consideration "if the content gives no clear signal", and this page has no specs or proof, so I used Consideration. That moves weight from SOL-2/SOL-5 to U1/U6/U2, where the page does fairly well (definition under a question H2, title matches the prompt). I also passed U1 c1 and U6 c1 on the "What are EcoStruxure rack systems for AI?" paragraph, which a stricter judge could fail.
- **09 (-10, at the threshold).** The difference comes from penalties: I applied `fluff_density` ("global leaders … difficult to match", "most comprehensive portfolio", "best-in-class") where v2.1 applied cta_overload + self_ranking. I also failed U9 c2 because "GRI G4 guidelines" is presented as current although G4 has been superseded. Most of the substantive content is in hidden tabs, so U3 c5 fails and U3 is capped at 2.

## Type-key and stage decisions (classifier rule, Appendix A step 9)

- 37 EcoCare and 41 MSS: recurring → `service`.
- 38 EcoFit, 39 EcoConsult and 42 EcoFit drive services: modernization/consulting → `service_project`.
- **40 Cybersecurity services: ambiguous.** The H1 offer is "design, configuration and implementation services *with maintenance* of cybersecurity controls". That is a project plus a recurring part. I chose `service_project` because design/implementation is the main deliverable, while v2.1 used `service`. Neither choice changes the score much (17 vs 19), since the page is thin under either key.
- 42: v2.1 used *Decision*. The page has no ordering or contract content, so I followed the prompt's default (Consideration).

## Prompt wording issues found

1. **The solution stage default conflicts with "Evaluation for product-solution pages".** The prompt does not say what makes a page a "product-solution page". 07 is a product-family page under /solutions/ and has no specs, and the choice between the two stages moves the score by about 10 points. A concrete test would fix this, for example "Evaluation only if the page has a spec table or named SKUs with parameters".
2. **Appendix A step 9 (recurring vs one-off) has no rule for mixed offers** (40, and the "Combine with EcoCare membership" cross-sell on 38). Suggested rule: classify by the H1 offer, and when it is mixed, by the first deliverable listed.
3. **The SVC-2 c5 "Conditions (tier, region, contract)" check is kept unchanged in the `service_project` variant**, while c1–c4 were rewritten. It is unclear whether c5 should apply to projects. I judged it as written.
4. **G12 depends on "no SVC-2 check passes".** On 42, a related-links list ("Extended warranty", "EcoStruxure Service Plan for drives") passes SVC-2 c3/c4 and so prevents the gate. The prompt should say that a link label alone is not a commitment.
5. **The U2 rule "5 only if all four in the first block" is mentioned only inside Step 2b,** while U2's check list has no "first block" check. Judges may miss it.
6. **The U1 c2 rule is a solution-only rule.** The service prompts instead say "c1 needs the definition in the BODY". On service pages with slogan H1s (37 "Improve uptime with EcoCare…", 39 "Turn complexity into confident decisions…"), c2 has no tie-break rule. I passed c2 when the title/H1 contained the service name.
7. **Footnotes with superscripts but no visible text** (37 ¹²³) fail SVC-6 c5 and cap SVC-6 at 3. That is correct by the rule, but the rule only says "resolves to visible text". The prompt does not say whether a footnote block that only appears after JS rendering counts.
8. **The SOL-7 and SVC-1 c5 / SOL-2 c5 "in HTML not in a tab" checks overlap with U3 c5.** The same hidden-tab fact is penalised 2–3 times (for example 08 and 09). This is not broken, but it is worth knowing when comparing scores.

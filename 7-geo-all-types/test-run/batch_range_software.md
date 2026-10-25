# Batch test: range + software pages (IDs 13–18, 43–48) with the per-type v2.1 prompts

Judged 2026-10-24 by an independent judge, blind to the v2.1 scores until after all 12 judge files were written. The input for each page was corpus/<file> plus corpus/rendered/<file>, used together, because the rendered capture adds content that the raw capture lacks. Examples: the Galaxy "10 kW to 1500 kW" line, the EcoStruxure IT "cutting emissions by 30%" story, and the PowerLogic members that sit only in hidden tabs. A script checked every pass quote against that text, and all 12 pages passed (0 misses). Scores come from the official `geo_score_calc.py`, and the judge files are in `judge/<NN>.json` and `result/<NN>_result.json`.

How each page type was chosen (Appendix A): 13–18 are master ranges, so `range`. 43, 44, 47 and 48 have 3 or more software product cards, so `software_hub`. 45 is one platform (EcoStruxure IT) and its tiles describe capabilities rather than products, so `software_product`. On 46 the trial sign-up (choose a country) is the main content, so `software_trial`. Each stage is the prompt's default for its type.

## Results

| ID | type key | stage used | new score | band | v2.1 score | diff | gates / penalties | top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|
| 13 | range | Consideration | 21 | Poor | 19 | +2 | G10 | RNG-2 (15.62), RNG-1 (13.02), U1 (6.94) |
| 14 | range | Consideration | 26 | Poor | 33 | -7 | G1 / pen: cta_overload | RNG-1 (13.02), RNG-2 (12.5), U1 (5.21) |
| 15 | range | Consideration | 32 | Poor | 33 | -1 | G1 | RNG-1 (13.02), RNG-2 (12.5), RNG-9 (6.3) |
| 16 | range | Consideration | 16 | Poor | 22 | -6 | — | RNG-2 (15.62), RNG-1 (13.02), RNG-9 (10.5) |
| 17 | range | Consideration | 32 | Poor | 37 | -5 | — | RNG-1 (13.02), RNG-9 (6.3), RNG-2 (6.25) |
| 18 | range | Consideration | 17 | Poor | 12 | +5 | G10 | RNG-2 (15.62), RNG-1 (13.02), RNG-9 (8.4) |
| 43 | software_hub | Consideration | 22 | Poor | 26 | -4 | — / pen: boilerplate, cta_overload | SW-7 (16.87), SW-6 (8.44), U1 (8.43) |
| 44 | software_hub | Consideration | 22 | Poor | n/a (not scored) | n/a | — / pen: boilerplate, cta_overload | SW-7 (16.87), SW-6 (8.44), U1 (8.43) |
| 45 | software_product | Evaluation | 30 | Poor | 33 | -3 | — / pen: template_artifact, cta_overload | SW-2 (13.08), SW-3 (10.71), SW-1 (8.56) |
| 46 | software_trial | Decision | 33 | Poor | 24 | +9 | G13 | SW-3 (14.56), SW-5 (12.48), SW-1 (9.98) |
| 47 | software_hub | Consideration | 35 | Poor | 28 | +7 | — / pen: template_artifact | SW-7 (8.44), SW-6 (8.44), U1 (8.43) |
| 48 | software_hub | Consideration | 35 | Poor | 25 | +10 | — | SW-7 (8.44), SW-6 (8.44), U1 (8.43) |

All 12 pages fall in the Poor band. The mean absolute difference over the 11 pages that have a v2.1 score is 5.4 points, and no difference is above 10 points.

### Median by type

| type key | n | median new score |
|---|---|---|
| range | 6 | 23.5 |
| software_hub | 4 | 28.5 |
| software_product | 1 | 30 |
| software_trial | 1 | 33 |

(The v2.1 median for range was 27.5, so this run is 4 points lower.)

## #44
The text exists, but `44_software-page.md`, at URL `/solutions/software/by-industry/`, is **byte-identical to #43** in both the raw and the rendered capture. The by-industry URL serves the main software portfolio page, so #44 gets the same score as #43 (22). The boilerplate penalty is applied to both pages, since they share 100% of their text. v2.1 probably skipped #44 as a duplicate. I recommend recording it as a duplicate URL (redirect or alias) rather than as a separate page.

## Differences of 10 points or more (none above 10; the two largest)
- **#48 (+10), #47 (+7):** v2.1 scored these pages 25 and 28. This run gives more credit to SW-1 (capabilities, 4 of 5 checks), to SW-7 c1 and c2 (cards grouped by need: "Energy source, load and grid management software"), to U2 (all 4 checks: "For large and critical buildings" plus the Citycon/campus outcome) and to U3 (descriptive H2s and bullet lists). It is also strict on the hero statistics, which have no numbers in the text (U3 c5, SW-6 c4), and on the "ZZ_Paragraph" template leftover on #47 (−2). The difference comes from check-level judgement on SW-1 and U3, not from a rule change.
- **#46 (+9):** I gave pass on SW-5 c2 ("free trials" is a price statement) and c4 ("Please select your country below:" is how to get the trial), U1 c1–c3 and U8. Because SW-5 carries 31% of the Decision weights, two passes there move the score a lot. G13 (thin page) still applies.
- **#14 (−7):** I triggered G1 for an internal contradiction: the card labelled "Galaxy VS Accessories" describes a "20 to 150 kW … 3-phase UPS", and VXL appears as "(400V)" in one place and "(400V or 480V)" in another. G1 sets U8 to 0. The cap of 59 does not bind at this score.
- **#16 (−6), #17 (−5):** these come from strict RNG-9 calls. On #16 fewer than 75% of members carry a rating, and member descriptors such as "Protection devices" give no function. The "Asset Advisor for drives" and mySchneider cards count as off-topic (RNG-9 c5).
- **#15:** G1 is also triggered: the range-level claim "from 16 to 6300 A" conflicts with "PowerPact … from 15 to 600 A". The score is almost the same as v2.1 (−1).

## Ambiguous or broken prompt wording
1. **Range U7 c4.** The check reads "named fairly … (na otherwise)", but the range prompt adds "Rule: c4 is na". The rule always overrides the check, so the check text is dead wording. Keep one of the two.
2. **G1 has no materiality threshold.** Small inconsistencies, such as 15 A against 16 A or a mislabelled card, trigger a gate that sets U8 to 0 and caps the score at 59. Different judges will disagree on these cases. Add a line such as "a material contradiction about a rating, scope or claim".
3. **RNG-9 "members".** The prompt does not say whether accessory, battery and app cards count as members, which changes the 75% and 50% thresholds. c1 ("every member") then fails on any single weak card.
4. **The Appendix A software rule leaves "3+ product cards" open.** On #45, 4 capability tiles sit next to named modules (IT Expert, IT Advisor, DCE, NetBotz), which could be read as a hub. Say that the cards must be distinct products.
5. **SW-3 c1, "software deployment model".** Pages such as #45 say "on-premise, at the edge, or in hybrid environments" about the infrastructure, not the software. The prompt should say that only statements about how the software itself is deployed count.
6. **G11 on trial pages.** "None of … trial terms": it is unclear whether a bare "free" counts. I judged that it does, so G11 was not triggered on #46. Under v2.1 both readings are possible.
7. **Hub rule "SW-1 applies to each product descriptor".** The rule does not say whether all descriptors or most of them must qualify, which matters on #43 (9 tools have one-liners, 10 portfolio cards are labels only).
8. **U9 c4 (cadence)** can never pass when c1 (date) fails. It is redundant on undated pages and duplicates the U9 cap of 1.
9. **The software prompts have no U5,** while the range prompt has U5 c1–c5. This may be intended, but the standard should say so; otherwise it looks like the criterion was dropped.
10. **Stage wording is fine.** The defaults are clear for every type, and no stage outside the natural ones was needed.

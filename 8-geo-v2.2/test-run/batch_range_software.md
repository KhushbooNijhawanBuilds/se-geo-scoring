# Batch: range + software pages (IDs 13-18, 43-48) — GEO v2.2 independent judge

Text source: corpus/<file> for all 12 (richer than rendered/ in every case; URL headers matched). Judged blind; all evidence quotes script-verified against the page text (0 missing).

| ID | key | stage | v2.2 | band | prev run | v2.1 | Δprev | Δv2.1 | gates | top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|---|---|
| 13 | range | Consideration | 21 | Poor | 21 | 19 | +0 | +2 | G10 | RNG-2 15.6; RNG-1 13.0; U1 6.9 |
| 14 | range | Consideration | 27 | Poor | 26 | 33 | +1 | -6 | - | RNG-2 15.6; RNG-1 13.0; U1 6.9 |
| 15 | range | Consideration | 36 | Poor | 32 | 33 | +4 | +3 | - | RNG-1 13.0; RNG-2 12.5; U1 5.2 |
| 16 | range | Consideration | 18 | Poor | 16 | 22 | +2 | -4 | - | RNG-2 15.6; RNG-1 13.0; RNG-9 8.4 |
| 17 | range | Consideration | 30 | Poor | 32 | 37 | -2 | -7 | - | RNG-2 15.6; RNG-1 13.0; RNG-5 5.7 |
| 18 | range | Consideration | 21 | Poor | 17 | 12 | +4 | +9 | G10 | RNG-2 15.6; RNG-1 13.0; RNG-9 6.3 |
| 43 | software_hub | Consideration | 21 | Poor | 22 | 26 | -1 | -5 | - | SW-7 16.9; SW-1 11.6; SW-6 8.4 |
| 44 (dup of 43) | software_hub | Consideration | 21 | Poor | 22 | — (not in v2.1 CSV; dropped as duplicate) | -1 | n/a | - | SW-7 16.9; SW-1 11.6; SW-6 8.4 |
| 45 | software_product | Evaluation | 30 | Poor | 30 | 33 | +0 | -3 | - | SW-2 13.1; SW-5 9.6; SW-3 8.6 |
| 46 | software_trial | Decision | 24 | Poor | 33 | 24 | -9 | +0 | G13 | SW-5 25.0; SW-3 14.6; SW-1 10.0 |
| 47 | software_hub | Consideration | 28 | Poor | 35 | 28 | -7 | +0 | - | SW-7 16.9; SW-6 8.4; U1 6.3 |
| 48 | software_hub | Consideration | 26 | Poor | 35 | 25 | -9 | +1 | - | SW-7 16.9; SW-6 8.4; U1 6.3 |

**Medians:** v2.2 25.0 | prev run 28.0 | v2.1 26.0

## Diffs > 10 vs previous run
None. Largest moves: #46 -9 (SW-5 c3 failed: only a bare 'free', <2 trial terms; SW-5 level 3->1), #47 -7 and #48 -9 (SW-7 c2/c4 failed: products grouped by heading but no which-product-for-which-need guidance and Expert vs Advisor / Microgrid Operation vs Advisor not explained; SW-7 is the heaviest hub weight at 21.1), #15 +4 and #18 +4 (v2.2 check-ceiling levels lift U8/U9/RNG-6), #14 +1 (prev run applied G1 cap 59 + U8=0; this run treats the VXL 400V vs 400V/480V and mislabelled 'Galaxy VS Accessories' card as U8 c3 fail, not material G1).

## Notes
- #44 is a duplicate of #43: its final_url redirects to /work/software/ and the corpus text is identical apart from the header line; scored anyway, identical result (21).
- Key choice: 13-18 range (master ranges, stage rule 1 -> Consideration). 43/44, 47, 48 software_hub (3+ distinct, separately named products). 45 software_product (Evaluation: security facts stated). 46 software_trial (Decision fixed).
- G10 fired on #13 (no rating with unit anywhere) and #18 (label-only member cards). G13 fired on #46 (U8 max 2; no score effect).
- template_artifact applied on all pages except #46 (card text rendered twice; #45 whole section twice; #47 live 'ZZ_Paragraph Title'). cta_overload on #43/44.

## Remaining prompt ambiguity
1. template_artifact vs scrape artefact: card teaser + repeated H3/label is likely a CMS card pattern (title + hover text). The prompt does not say whether a repeated card *title* (vs whole card text) counts; I applied it whenever card text appeared twice, which costs every range/hub page -2.
2. U1 c1 on hub/benefit-led pages (#47/#48): a function sentence ('Monitor, analyze, control...') vs a definition. 'Directly answer the primary question' could pass it; 'define the subject' fails it. Judged fail.
3. SW-7 c2 on hubs: whether grouping products under need-named H2s ('Building management software' / 'Power management software') counts as 'which product for which need' guidance. Judged fail; this alone is ~5 pts on #47/#48.
4. U8 c4 when the only visible link text is a generic heading ('See product details'): fail or na (links not visible)? Applied fail where 'Read more'/'visit:' text exists, na otherwise.
5. U9 c3 'where relevant' on range pages without legacy members: na vs fail is unclear; judged fail throughout.
6. RNG-9 member set when a non-family-name range appears (Symmetra PX on Galaxy): treated as a member.
7. 'Hero statistics with labels but no numbers' (#47/#48): U3 c5 (facts only in images) or SW-6 c4; counted once under U3 c5 and also SW-6 c4 because SW-6 c4 is a visibility-of-numbers check — possible double count.

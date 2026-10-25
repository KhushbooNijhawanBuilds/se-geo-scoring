# Batch test: White paper and ESG pages (IDs 25-30, 55-60)

Judge: strict, independent, blind to the earlier scores. Prompts: `prompts/copilot_prompt_<key>_v2.1.txt`. Scores come from the official `geo_score_calc.py`.
Inputs: server text `corpus/<file>`, plus `corpus/rendered/<file>` for the white papers. For #59 and #60 the PDF text is `*_sustainability-esg-report.pdf.md`.
Files: `judge/<NN>.json`, `judge/<NN>_doc.json`, `result/<NN>_result.json`.

## Results

| ID | Type key | Stage used | New score | Band | v2.1 score | Diff | Gates | Top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|
| 25 | whitepaper_gateway | Education | 18 | Poor | 34 | **-16** | G6, G13 | WP-2 17.4; DOC-8 9.9; WP-1 9.2 |
| 26 | whitepaper_gateway | Consideration | 33 | Poor | 46 | **-13** | G6 | WP-2 15.3; DOC-8 8.7; U1 7.1 |
| 27 | whitepaper_gateway | Education | 15 | Poor | 32 | **-17** | G6, G13 | WP-2 17.4; WP-1 11.6; DOC-8 9.9 |
| 28 | whitepaper_gateway | Education | 28 | Poor | 36 | -8 | G6 | WP-2 17.4; DOC-8 9.9; WP-3 9.2 |
| 29 | whitepaper_gateway | Education | 38 (borderline 40) | Poor | 42 | -4 | G6 | WP-2 17.4; DOC-8 7.5; WP-1 6.9 |
| 30 | whitepaper_gateway | Education | 30 | Poor | 36 | -6 | G6 | WP-2 17.4; DOC-8 9.9; WP-3 9.2 |
| 55 | esg_hub | Evaluation | 14 | Poor | 20 | -6 | G6, G13 | ESG-1 26.1; ESG-2 14.6; ESG-5 12.2 |
| 56 | esg_report | Evaluation | 11 | Poor | 16 | -5 | G2, G6, G13 | ESG-1 28.2; ESG-2 16.8; ESG-3 8.6 |
| 57 | esg_report | Evaluation | 11 | Poor | 16 | -5 | G2, G6, G13 | ESG-1 28.2; ESG-2 16.8; ESG-3 8.6 |
| 58 | esg_report | Evaluation | 6 | Poor | 9 | -3 | G2, G6, G13 | ESG-1 28.2; ESG-2 16.8; ESG-3 8.6 |
| 59 | esg_report (bare PDF) | Evaluation | 0 | Poor | 2 | -2 | G2, G6 | ESG-1 28.2; ESG-2 16.8; DOC-7 9.4 |
| 59_doc | esg_report_doc | Evaluation | 69 (borderline 70) | Average | 70 | -1 | none | ESG-1 9.5; DOC-7 6.2; DOC-1 4.2 |
| 60 | esg_report (bare PDF) | Evaluation | 0 | Poor | 2 | -2 | G2, G6 | ESG-1 28.2; ESG-2 16.8; DOC-7 9.4 |
| 60_doc | esg_report_doc | Evaluation | 67 | Average | 68 | -1 | none | DOC-4 8.4; DOC-7 6.2; ESG-1 4.8 |

Penalties: `template_artifact` -2 on 25-30 and 56-58 (the metadata block and a truncated copy of the abstract are rendered twice) and on 55 (live "ZZ_" placeholders). `superseded_no_notice` -3 on 59_doc and 60_doc.

## Medians by type

| Type key | n | New median | v2.1 median |
|---|---|---|---|
| whitepaper_gateway | 6 | 29 | 36 |
| esg_hub | 1 | 14 | 20 |
| esg_report (gateway) | 5 | 6 | 9 |
| esg_report_doc | 2 | 68 | 69 |

The ranking matches v2.1: every gateway is Poor and the PDF layer is about 70. The new scores run lower on every page. The document scores are almost the same, so the derived ESG document checks reproduce the pilot.

## Differences above 10 points

- **#25 (-16), #27 (-17): G13 plus stricter checks.**
  - G13 triggered: the abstracts are general assertions ("impossible without data centers", "tremendous potential") with no substantive facts, so U7 and U8 are capped at 2. v2.1 did not apply G13 to these pages, but it did apply it to #28 and #30, which I did not. That is the inverse choice, and it shows G13 is unreliable on abstract-only pages.
  - U1 c1 fails: the abstract opens with background, not the thesis.
  - WP-1 c1 fails: the abstract is not a single instance.
  - DOC-7 c2 and U8 c3 fail on the version mismatch: page says 1.0, file is V1.1 (#25); page 1.1, file V1.2 (#27).
  - The template_artifact penalty takes another 2 points.
- **#26 (-13): stage and strict checks.**
  - I used Consideration because the paper weighs DC against the AC/double-conversion architecture. Re-running at Education also gives 33, so the stage choice did not cause the gap.
  - The rest comes from: U1 c1 fail (background lead), WP-1 c5 fail (the conclusion "better data center designs" is generic), U10 c1 fail, DOC-7 c4 fail (released Mar 2023, more than 24 months ago) and the -2 penalty.

## Ambiguous or broken prompt wording

1. **G6 refers to a criterion that does not exist (esg_report, esg_report_doc).** G6 says "-> U3 max 2", but neither type has U3. esg_report Step 2d even says "Caps ... none for this type". Only the max-59 part of G6 can apply.
2. **The same fact is counted twice (esg_report_doc).** "Bookmarks/outline" is both ESG-5 c2 and DOC-4 c5, so a PDF with no outline loses twice (#60_doc).
3. **Derived DOC-4 checks can't be judged from pasted text.**
   - c2 (tagged PDF) and c5 (bookmarks) are visible only in extraction metadata. A Copilot judge reading the text cannot see them, so these should be `na` when the input is pasted text.
   - c1 "Real text layer on every page" fails any designed report that has one blank or image-only page. Both PDFs have exactly 1 such page out of 222-260. I failed it under the "torn -> fail" rule. Suggested rewording: "no scanned content pages".
4. **ESG-5 c5 "Cross-references are accurate" can never pass.** Printed page numbers don't match PDF pages in the extracted text, so "missing evidence = fail" fails it every time. Suggestion: make it `na` unless it can be checked.
5. **Currency checks need outside knowledge, which Judge Rule 1 forbids.** DOC-7 c4 "this is the current edition" and the `superseded_no_notice` penalty both need to know a newer edition exists. I applied them to the 2023 and 2022 reports, using the hub's list of editions as context. v2.1 did the same.
6. **Two DOC-7 checks are unclear.**
   - c3 "change note when the version is above 1.0" does not say whether the page version or the file version counts (#25: page 1.0, file V1.1).
   - c5 "current edition stated": the SE template's "Latest version" label exists only as a hidden element. It's unclear whether hidden labels count.
7. **WP-1 c1 "a single instance" overlaps the template_artifact penalty.**
   - The SE download template always outputs a second, truncated (hidden) copy of the abstract, so WP-1 c1 fails on every SE white paper.
   - That same duplication also triggers the template_artifact penalty ("a whole section rendered twice"). One template defect is penalised twice.
   - v2.1 applied neither to the white papers, and the boilerplate penalty instead to 56-58.
   - Decide whether hidden duplicates count.
8. **An anchor loophole lets U1 reach 4 with no content sections.** With no sections, U1 c4 is `na`, and "na counts as met" in the level-4 anchor (c1+c2+c3+c4). #29 gets U1 = 4 with no sections and no takeaways.
9. **G2 and G6 overlap on report gateways.** A download stub with no KPIs triggers G6 ("gateway with no KPIs", cap 59). It also arguably triggers G2 (the results asked for are never given, cap 39). v2.1 applied G2 only to #58; I applied it to 56-60. The prompt should say which one applies to KPI-less stubs.
10. **Bare PDF gateways (#59, #60).** "Every HTML check fails" makes the score exactly 0, yet v2.1 reported 2. Either the v2.1 run passed some checks or it handled the `superseded_no_notice` penalty differently.
11. **Wording copied from the white paper template.** esg_report DOC-5 c3 gives the example "White paper 126", which doesn't fit ESG pages.
12. **whitepaper_doc was not exercised.** The corpus has no white paper PDF text, so the doc layer for 25-30 is untested.
13. **Data problem: the rendered ESG files are mismatched.** The `corpus/rendered/` files for 55-58 belong to other pages (by their own URL header: 55 is the H1 2026 page, 56 the Impact report, 57 the 2025 report, 58 the H1 2026 page). I used the server text for 55-58.

# Batch: white paper gateways + ESG reports (GEO v2.2, blind re-judge)

Judge: independent strict run with the v2.2 copilot prompts (`whitepaper_gateway`, `esg_hub`, `esg_report`, `esg_report_doc`), page text from `corpus/`. `rendered/` was not used: it is shorter for 25-30, has the wrong URL for 55-58 and does not exist for 59-60. A script checked every quote against the source text (whitespace normalised): 0 misses. Scored 2026-10-25. No earlier judge, result or CSV file was opened until all 14 judge files were written.

Keys (Appendix A): 25-30 are HTML download pages for a white paper, so `whitepaper_gateway` (rule 2). 55 is a report library, so `esg_hub`. 56-58 are single ESG report pages, so `esg_report`. 59-60 are bare PDF URLs, so `esg_report` with every HTML check failing (rule 1). 59_doc and 60_doc are the PDF text, scored with `esg_report_doc`. Stage: the ESG types always use Evaluation (R10). For 25-30 the stage test (rule 1, compares options) matched nothing clearly, so all use Education. See ambiguity A1 for 26.

| ID | key | stage | v2.2 score | band | prev run (stage) | v2.1 | Δ prev | Δ v2.1 | gates / penalties | top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|---|---|
| 25 | whitepaper_gateway | Education | 29 | Poor | 18 (Education) | 34 | +11 | -5 | G13, G6 / template_artifact | WP-2 (+17.4); DOC-8 (+9.9); U1 (+8.3) |
| 26 | whitepaper_gateway | Education | 35 | Poor | 33 (Consideration) | 46 | +2 | -11 | G13, G6 / template_artifact | WP-2 (+17.4); DOC-8 (+9.9); U1 (+8.3) |
| 27 | whitepaper_gateway | Education | 27 | Poor | 15 (Education) | 32 | +12 | -5 | G13, G6 / template_artifact | WP-2 (+17.4); DOC-8 (+9.9); U1 (+8.3) |
| 28 | whitepaper_gateway | Education | 30 | Poor | 28 (Education) | 36 | +2 | -6 | G13, G6 / template_artifact | WP-2 (+17.4); DOC-8 (+9.9); U1 (+8.3) |
| 29 | whitepaper_gateway | Education | 40 | Average | 38 (Education) | 42 | +2 | -2 | G6 / template_artifact | WP-2 (+17.4); U1 (+8.3); DOC-8 (+7.5) |
| 30 | whitepaper_gateway | Education | 37 | Poor | 30 (Education) | 36 | +7 | +1 | G13, G6 / template_artifact | WP-2 (+17.4); DOC-8 (+9.9); U1 (+5.5) |
| 55 | esg_hub | Evaluation | 16 | Poor | 14 (Evaluation) | 20 | +2 | -4 | G13, G6 / template_artifact | ESG-1 (+26.1); ESG-2 (+14.6); ESG-5 (+12.2) |
| 56 | esg_report | Evaluation | 16 | Poor | 11 (Evaluation) | 16 | +5 | +0 | G13, G6 / template_artifact | ESG-1 (+28.2); ESG-2 (+16.8); ESG-3 (+8.6) |
| 57 | esg_report | Evaluation | 14 | Poor | 11 (Evaluation) | 16 | +3 | -2 | G13, G6 / template_artifact | ESG-1 (+28.2); ESG-2 (+16.8); ESG-3 (+8.6) |
| 58 | esg_report | Evaluation | 10 | Poor | 6 (Evaluation) | 9 | +4 | +1 | G13, G6 / template_artifact | ESG-1 (+28.2); ESG-2 (+16.8); ESG-3 (+8.6) |
| 59 | esg_report | Evaluation | 0 | Poor | 0 (Evaluation) | 2 | +0 | -2 | G13, G6 | ESG-1 (+28.2); ESG-2 (+16.8); DOC-7 (+9.4) |
| 60 | esg_report | Evaluation | 0 | Poor | 0 (Evaluation) | 2 | +0 | -2 | G13, G6 | ESG-1 (+28.2); ESG-2 (+16.8); DOC-7 (+9.4) |
| 59_doc | esg_report_doc | Evaluation | 85 | Good | 69 (Evaluation) | 70 | +16 | +15 | - | DOC-7 (+4.6); DOC-4 (+4.2); U7 (+3.2) |
| 60_doc | esg_report_doc | Evaluation | 80 | Good | 67 (Evaluation) | 68 | +13 | +12 | - | DOC-4 (+8.4); DOC-7 (+4.6); U7 (+3.2) |

**Medians, all 14:** v2.2 28.0 · prev run 16.5 · v2.1 33.0  
**White paper gateways 25-30:** v2.2 32.5 · prev 29.0 · v2.1 36.0  
**ESG HTML 55-60:** v2.2 12.0 · prev 8.5 · v2.1 12.5  
**ESG PDF text 59_doc / 60_doc:** v2.2 82.5 · prev 68.0 · v2.1 69.0

Two layers, never averaged: 59 = 0 (bare PDF) next to 59_doc = 85; 60 = 0 next to 60_doc = 80.

Borderline: **29 = 40** is within 3 of the Average/Poor line. The standard asks for 3 independent runs and the median.

## Diffs over 10 points vs the previous run, and why
- **25 (+11, 18 → 29)** and **27 (+12, 15 → 27)**. These are not gate changes: both runs trigger G6 and G13. The previous run gave WP-3 = 0. This run passes WP-3 c1 (3+ topics beyond the title: renewables/digitalisation/AI supply-demand for 25; renewables/HVAC/EV charging for 27) and c4 (one intent), so the ceiling is 3. WP-1 rose from 1/0 to 3/2: 25 passes c1 (98 words, not truncated), c2 and c6; 27 passes c1 and c2. U10 rose from 1 to 3 because c1/c2 pass on notes (an abstract-level explainer fits Education). Most of the gap comes from c1/c2 notes on U10 and the WP-3 coverage credit. The previous run was harsher on both. Under the v2.2 ceiling rule, these passes lift levels directly.
- **59_doc (+16, 69 → 85)**. ESG-1 rose from 3 to 5: all 5 checks pass. The section 8.1 GHG table gives Scope 1, Scope 2 market-based (location-based in a footnote) and Scope 3 in tCO2e, with years, 99% coverage and the change vs the 2021 base. DOC-1 rose from 3 to 4 and ESG-5 from 4 to 5. The supplied extraction metadata (`outline_entries: 307`) makes the bookmarks check judgeable (pass); c5 is na. The previous run applied `superseded_no_notice` (v2.1 did too). This run did not. Rule 11 limits currency to what the supplied content states, and the PDF text names no later edition. That penalty alone is about 3 points.
- **60_doc (+13, 67 → 80)**. Same pattern: ESG-1 4 → 5, DOC-1 3 → 4, ESG-5 3 → 4, and no `superseded_no_notice`. DOC-4 stays 1: the PDF is untagged and the extracted words are split.

Smaller systematic shifts: on 25-30, DOC-5 fell from 3 to 1. The meta descriptions end in '...' (c4 fail), the file names are code-only (c2) and no 'White paper NNN' wording appears in the text (c3). U8 and U7 are capped at 2 by G13 on 5 of 6 gateways. The previous run left U8 at 4 on 26, 28 and 30 because it did not trigger G13 there. This run counts at most 2 substantive facts on 26, 28 and 30, so G13 fires. On 56-58 this run did not trigger G2 (the previous run did). v2.2 says a KPI-less download stub is G6, not G2.

## Remaining prompt ambiguity
1. **A1 Stage test for 26.** The abstract contrasts DC distribution with the 'AC/DC/AC conversion stage required in a traditional double conversion UPS'. That can be read as comparing architectures (Consideration; the previous run chose this) or not (Education, the fallback this run chose). The rule needs an explicit example of a contrast that does not count as comparing options.
2. **G13 counting on abstract-only gateways.** It is unclear whether a 'named finding' includes the paper announcing its own topics ('describes the eight most common challenges', 'there are 5 areas ... power converter design, UPS bypass ...'). This one call decides G13 on 26, 28 and 30, which caps U7 and U8 at 2 and moves about 4-6 points.
3. **DOC-7 c3 / esg DOC-7 c3 for version 1 / 1.0.** This run marked it na when the version is 1.0. The text 'when the version is above 1.0' implies na, but the 'missing block = fail' rule could be read the other way. The prompt should say explicitly that it is na at v1.0.
4. **template_artifact for the repeated metadata block.** Every se.com download page repeats the title and metadata block. On white papers the repeat carries a truncated abstract; on ESG pages it is only the metadata. This run applied −2 to all of them. The penalty is identical on every page, so it is a template issue. A rule saying whether a metadata-only repeat counts as 'a whole section rendered twice' would remove the doubt.
5. **Bare-PDF gateway (59, 60).** 'Every HTML check fails' conflicts with the general rule that link checks (U8 c4, U10 c4) are na when links are not visible. This run failed them all (score 0 either way, because every check fails). G13 'thin page' also fires on an empty page. The prompt should say whether G13 applies on top of G6 there.
6. **superseded_no_notice on archived PDF editions.** The esg_report prompt says to apply it 'for archived editions'. Rule 11 says to judge only from the supplied content. A PDF never states its own supersession, so the outcome depends on whether hub text (55 lists 2025/2024 reports) counts as 'supplied' for 59_doc and 60_doc. Previous runs applied it; this run did not.
7. **Level-5 downgrade (b3) is discretionary.** 'Not exceptional' evidence has no test. This run downgraded U7/U8 on 29, U8 on 59_doc/60_doc and DOC-5 on 56-58 (about 1 point each), and kept ESG-1 to ESG-4 at 5 on the PDFs (assured first-party data).

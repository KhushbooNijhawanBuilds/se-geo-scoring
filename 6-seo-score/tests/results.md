# Blog SEO Score v1 — test run on the 6 corpus blogs (2026-10-23)

Judge: Claude, strict mode, single run. Inputs: corpus markdown (`4-scoring-project-v2.1/.../research/corpus/0N_blog-article.md`) plus the live HTML fetched with curl on 2026-10-23 (`tests/html/0N.html`), because the corpus markdown strips links, image filenames, canonical, robots and JSON-LD fields. Mechanical checks come from `seo_extract.py` (`tests/extract/`); judged checks and quotes are in `build_judges.py` → `0N_seo_judge.json`; scores are computed by `seo_score_calc.py` → `0N_seo_result.json`. The target keyword was **inferred** by the judge for every page (none was supplied), so S6 results are indicative.

The GEO column is the existing Content GEO Score v2.1 (final), shown **for reference only**. The two scores are never blended.

| # | Page (H1) | SEO score | Band | Gates | Top 3 gaps (recoverable pts) | Eligibility | GEO v2.1 (reference only) |
|---|---|---|---|---|---|---|---|
| 01 | Modular, prefabricated data centers enter the AI era and boldly go whe | **64** | Average | - | S1 Search intent match (+8.4; failed c1,c2); S9 Originality and first-hand value (+6.6; failed c1,c2,c4); S2 SEO title tag (+4.0; failed c2) | Eligible | 37 (Poor) |
| 02 | Data center community opposition: How cooling design affects water, no | **71** | Good | - | S8 E-E-A-T: author, expertise, sourcing (+4.8; failed c2); S9 Originality and first-hand value (+4.4; failed c1,c4); S2 SEO title tag (+4.0; failed c2) | Eligible | 71 (Good) |
| 03 | AI infrastructure deployment: Demand is easy. Execution is hard. | **49** | Average | SG4 (raw 69.0) | S7 Topical coverage and depth (+8.4; failed c1,c2,c3); S1 Search intent match (+5.6; failed c4); S9 Originality and first-hand value (+4.4; failed c2,c4) | Eligible | 47 (Average) |
| 04 | AI is moving faster than infrastructure. Leaders need a new strategy. | **73** | Good | - | S9 Originality and first-hand value (+6.6; failed c1,c2,c4); S2 SEO title tag (+4.0; failed c2,c4); S1 Search intent match (+2.8; failed -) | Eligible | 53 (Average) |
| 05 | Using treated and recycled water in Indian data centre cooling | **73** | Good | - | S9 Originality and first-hand value (+6.6; failed c1,c2,c4); S8 E-E-A-T: author, expertise, sourcing (+4.8; failed c2); S2 SEO title tag (+4.0; failed c2,c4) | Eligible | 69 (Average) |
| 06 | The next decade of AI infrastructure: Why Europe has an opportunity to | **75** | Good | - | S1 Search intent match (+5.77; failed c2); S2 SEO title tag (+4.12; failed c2); S7 Topical coverage and depth (+2.89; failed c3) | Eligible | 39 (Poor) |
Eligibility notes (all six identical, same WordPress/Yoast template): HTTP 200 with no redirect; meta robots `index, follow`; no X-Robots-Tag; one absolute HTTPS self-canonical; no hreflang (single-language blog, so E4 is na); HTTP 301s to HTTPS; viewport present (mobile content parity not rendered, so E6 is only partly verified). Warning, not scored: robots.txt disallows `/wp-content/themes/` and `/wp-content/plugins/` (CSS/JS). Google advises against blocking rendering resources, so route this to SE Digital.

## Levels per criterion

| Criterion | 01 | 02 | 03 | 04 | 05 | 06 |
|---|---|---|---|---|---|---|
| S1 | 2 | 4 | 3 | 4 | 4 | 3 |
| S2 | 3 | 3 | 3 | 3 | 3 | 3 |
| S3 | 4 | 4 | 3 | 4 | 5 | 4 |
| S4 | 3 | 4 | 4 | 4 | 4 | 4 |
| S5 | 4 | 4 | 4 | 4 | 4 | 3 |
| S6 | 4 | 4 | 5 | 4 | 5 | 4 |
| S7 | 4 | 4 | 2 | 4 | 4 | 4 |
| S8 | 4 | 3 | 4 | 4 | 3 | 4 |
| S9 | 2 | 3 | 3 | 2 | 2 | 4 |
| S10 | 4 | 4 | 4 | 4 | 4 | 4 |
| S11 | 3 | 4 | 4 | 4 | 4 | 4 |
| S12 | 3 | 5 | 5 | 5 | 5 | drop |
| S13 | 0 | 0 | 4 | 1 | 4 | 4 |
| S14 | 5 | 3 | 5 | 5 | 3 | 5 |
## What the run shows

- **Template issues ([T]) show up on every page.** Every SEO title runs 78–115 characters because " - Schneider Electric Blog" (25 characters) is appended (S2 c2). Hero images are stock files with names like `GettyImages-…`/`AdobeStock_…` (S13 c3). Articles 01 and 02 have empty `alt=""` on the hero image (S13 c1). The comment form, "Top picks" and related-post titles render as `<h2>` inside `<article>` (S5 c4). `dateModified` was bumped to 2026-10-16 between 04:29 and 06:15 on articles 01–04, which looks like a batch re-save, and no "Updated" label is shown (S10 c4 fails where the bump is 7 days or more after publication). This is not treated as the fake-freshness gate, because there is no evidence of intent. The authors of articles 02 and 05 sit behind a "Guest Blogger" byline, and the JSON-LD author is "Guest Blogger" too (S8 c2, S14 c2/c3).
- **Author issues ([A]):** title/H1/meta promises that the page does not deliver (03: "3 operational priorities", gate SG4 → capped at 49); slogan H1s and slugs (01 and 04, plus the slug typo "infrastucture" in 04); intros that hold back the answer (01, 06); missing first-hand or first-party evidence (S9 on all six); unsourced statistics (01); and tracking parameters on internal links (`utm_source=reddit` in 02 and 05, `sourceId=` in 01).
- **SEO and GEO diverge** in the places the research predicts. Articles 01 and 06 are Poor on GEO (no answer up front, little evidence) but Average/Good on SEO, because the head, markup and URL hygiene that GEO does not score are sound. Article 03 is low on both. The table is a management signal, not a reason to merge the scores.

## Calibration check

The first pass (v1 draft weights, no extra caps) scored 66 / 75 / 49 / 73 / 75 / 77 (mean 69). That is not ">80 everywhere", but it sits above the intended 35–65 band for unoptimised pages. Two evidence-based caps were added (see the Standard, section 4.3):

1. **S2 max 3 when the title fails the length band (c2).** Zyppy found rewrite rates of 76% above 60 characters and 99.9% above 70, so a title that is almost certainly rewritten should not reach "strong".
2. **S8 max 3 when the byline does not link to the named author's own bio (c2).** Google asks for bylines that lead to information about the author.
3. (Also added, no effect on this sample) **S9 max 3 when there is neither first-hand experience (c1) nor first-party data (c2).**

After the change: 64 / 71 / 49 / 73 / 73 / 75 (mean 67.5, range 49–75). No page reaches 80, and the only gated page drops to 49. The sample is a set of recent, Yoast-templated posts by named SE staff. They are not "unoptimised", which explains why they sit a few points above the band. Weights were **not** tuned to hit a number. A larger random sample, including old and thin posts, is needed before freezing (see the open questions in the Standard).

## Self-test

`python3 ../seo_score_calc.py --selftest` → `SELFTEST OK`. It checks that weights sum to 100, every criterion has 3–6 checks, half-up rounding, judge proposals are respected, criteria with more than half na are dropped and the weights renormalised, the anchors and caps (including the calibration caps), the lowest gate cap wins, SG5 zeroes S5, penalties cap at −10 with the hidden-text cap lift, and eligibility status logic.

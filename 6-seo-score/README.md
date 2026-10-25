# 6-seo-score: SE Blog SEO Score v1

A standalone on-page SEO score (0–100) for Schneider Electric blog articles. It is built the same way as the Content GEO Score v2.1 (binary checks with quotes → levels 0–5 → weights → gates → penalties → bands), but it is **never blended** with GEO.

## Files

| File | What it is |
|---|---|
| `SEO_Scoring_Standard_v1.md` | The rubric: purpose, scope, 14 criteria with weights and reasons, every check with its pass rule and basis, level rules, gates, penalties, technical eligibility, needs-data items, excluded myths, evidence table, limitations |
| `seo_weights.json` | Weights, anchors, caps, gates, penalties, bands, eligibility and needs-data definitions (read by the calculator) |
| `seo_score_calc.py` | Deterministic calculator (Python 3.9+, stdlib only). Judge JSON in → score, band, per-criterion level/points/recoverable, gates, penalties, eligibility status |
| `seo_extract.py` | Deterministic extractor (stdlib only). Pulls the measurable facts (URL parts, title/meta length and estimated px, H1 count, headings, alt text, filenames, links with anchors/UTM/rel, dates, JSON-LD fields, OG, canonical, robots) and returns the **computed** checks, so mechanical checks are not left to the AI |
| `copilot_prompt_blog_seo_v1.txt` | Self-sufficient Copilot prompt: the user gives only a blog URL (plus an optional keyword); Copilot judges every check and outputs the report plus JSON in the calculator's shape |
| `tests/` | Test run on the 6 corpus blogs: `html/` (live HTML, 2026-10-23), `extract/` (extractor output), `build_judges.py` (judged verdicts and quotes, merged with computed checks), `0N_seo_judge.json`, `0N_seo_result.json`, `results.md` |

## How to run

```bash
cd "6-seo-score"
python3 seo_score_calc.py --selftest                         # SELFTEST OK
python3 seo_score_calc.py --template > my_judge.json         # empty judge skeleton

# 1. extract facts and computed checks (HTML preferred; the corpus .md alone loses links/filenames/markup)
curl -s -A "Mozilla/5.0" -o page.html "<blog url>"
python3 seo_extract.py --html page.html --url "<blog url>" --keyword "target phrase" > extract.json
#    or: python3 seo_extract.py --md path/to/0N_blog-article.md --html page.html --keyword "..."

# 2. the judge (Copilot prompt or a human) fills the judged checks; copy the computed checks from extract.json
# 3. score
python3 seo_score_calc.py --judge my_judge.json --md         # markdown score card
python3 seo_score_calc.py --judge my_judge.json              # full JSON

# reproduce the test run
python3 tests/build_judges.py && for i in 1 2 3 4 5 6; do python3 seo_score_calc.py --judge tests/0${i}_seo_judge.json --md; done
```

## Computed vs judged

Mechanical checks (title/meta length, brand position, slug format, H1 count, subhead density, template headings, topic placement with a keyword, date match, internal-link count/anchors/UTM, rel, alt presence, filenames, JSON-LD fields, OG) are computed by `seo_extract.py`. Meaning checks (intent, coverage, E-E-A-T, originality, descriptive headings, meta accuracy, slug spelling) are judged with quotes. The full map is in the Standard, section 6. The judge may override a computed result only with an `override:` reason.

## Test results (2026-10-23)

| Blog | SEO | Band | GEO v2.1 (reference) |
|---|---|---|---|
| 01 Modular prefab data centers | 64 | Average | 37 |
| 02 Community opposition & cooling | 71 | Good | 71 |
| 03 AI infrastructure deployment (SG4 → cap 49) | 49 | Average | 47 |
| 04 AI infrastructure planning | 73 | Good | 53 |
| 05 Recycled water, Indian data centres | 73 | Good | 69 |
| 06 AI infrastructure in Europe | 75 | Good | 39 |

All six: **Eligible** (with the caveat that mobile parity was not rendered). Details and calibration notes are in `tests/results.md`.

# Content GEO Score (standard v2.2, all page types)

Scores how ready a page's content is to be understood, trusted and quoted by AI answer engines, using the
SE Content GEO Scoring Standard **v2.2** for all 26 page types, and shows exactly how the score was calculated.

The AI judge (Google Gemini) only answers each pass/fail check with evidence. **The calculator sets every level**
(v2.2 rule) and computes weights, penalties, gate caps and the final score in code (`engine/geo_score_calc.py`).

## Setup (once)

1. Install Python 3.9 or later (https://www.python.org/downloads/).
2. Put your Google Gemini API key (from https://aistudio.google.com/apikey) in a secrets file:
   copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and replace the placeholder with your key.
   (Or set the `GEMINI_API_KEY` environment variable, or paste the key in the sidebar for one session.)
   **Never share, zip or commit `secrets.toml`.** It is excluded by `.gitignore`.
3. Start the app:
   - Mac: double-click `start_mac.command` (first run installs everything into `.venv`).
   - Windows: double-click `start_windows.bat`.
   - Manually: `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt && .venv/bin/streamlit run app.py`
4. Open http://localhost:8501.

The Replay tab works without an API key.

## Scoring a page

Mandatory fields (marked *):
- **Page URL** (or paste the page text in the expander: use this for se.com / Medium pages that block automated requests,
  pages that load content with JavaScript, and PDFs).
- **Content type**: one of the 26 types, or **Auto-detect** (the model classifies the page with the standard's
  decision tree, Appendix A, and reports the type key, the rule that matched and why).
- **Buyer-journey stage**: a stage, or **Detect automatically** (the judge applies the v2.2 stage test for the type;
  the result shows the rule and the content signal). A stage you choose always wins; the app still notes the stage the test would give.
- **Topic** and **Industry**.

Recommended: target question(s) a buyer asks AI. Optional: audience, country.

Model: `gemini-2.5-pro` (default) or `gemini-2.5-flash`; effort high by default (mapped to the Gemini thinking
budget). Change the default by setting `GEMINI_MODEL` in `secrets.toml` or the environment.

## Page types

Tested on SE pages (10 inventory types): `article` (blog), `solution`, `range`, `case_study`, `whitepaper_gateway`,
`calculator`, `service`, `service_project`, `software_product`, `software_hub`, `software_trial`, `news`,
`esg_hub`, `esg_report`, `esg_report_doc`.

Not yet tested (logic from the standard, results are indicative): `whitepaper_doc`, `pdp`, `category`, `caas`,
`editorial`, `document`, `datasheet`, `comparison`, `faq`, `glossary`, `video`.

The judge's instructions for each type are the v2.2 Copilot prompt for that type (`standard/prompts/`), with the
Copilot-only parts (open the URL, compute the score, write a report) replaced by the app's intake and JSON output.
So checks, gates, caps, anchors, stage tests and the checks that may pass on a judge note are exactly v2.2.

## Results

- Score, band, raw score, penalties, gate cap, confidence, borderline warning.
- **How the score was calculated**: per criterion the checks passed, ceiling, judge level, rule adjustments
  (anchor floor, caps, v2.2 check rules, gate effects), final level, effective weight, points and recoverable points;
  accepted judge downgrades with their reason; calculator notes.
- **How this page type is scored** (also an expander under the Content type picker): what AI extracts, default and natural stages, the stage test, criteria with weights, gates, common SE failures, tested or not and the pilot median. Generated from the v2.2 sources.
- Gates, penalties, top gaps ([Template / CMS] vs [Author] fixes), evidence for every check (quote or note; quotes are verified against the page).
- Downloads: the judgement JSON and the score result JSON.

The sidebar toggle **Scoring rules v2.2 / v2.1** re-scores the same judgement with the older v2.1 level logic for comparison
(same weights). v2.2 is the default.

## Copilot workflow (no API key)

1. Open `standard/prompts/copilot_prompt_<type>_v2.2.txt` for the page type (Appendix A in
   `standard/appendix_a_page_type_decision_tree.md` helps you choose) and paste it into Copilot with the page URL.
2. Copy the JSON block Copilot returns at the end of its answer.
3. In the app, open **Replay**, paste the JSON and click **Show calculation**. The app's calculator gives the exact score.

JSON from any of the 26 v2.2 prompts is accepted (`downgrade_reason`, `evidence_type: "note"`, `proposed_level: null`).
Saved judgements and v2.1 judge files also replay.

## Files

| Path | What it is |
|---|---|
| `app.py` | The Streamlit app |
| `geoscore/capture.py` | Fetches the page and extracts text and signals |
| `geoscore/judge.py` | Builds the per-type v2.2 prompt, the type classifier, calls Google Gemini, verifies quotes |
| `geoscore/explain.py` | Runs the calculator and explains every step |
| `geoscore/type_info.py` | The "How this page type is scored" panel |
| `geoscore/catalog.py` | Page types, groups, gates, penalties, names |
| `geoscore/standard_v22.py` | Copy of the v2.2 catalogue (criteria, checks, stage tests) |
| `engine/geo_score_calc.py`, `engine/weights.json` | The v2.2 calculator and weights (`--selftest` to check) |
| `standard/` | The v2.2 standard, Appendix A and the 26 Copilot prompts |
| `examples/` | Example judgements for the Replay tab |

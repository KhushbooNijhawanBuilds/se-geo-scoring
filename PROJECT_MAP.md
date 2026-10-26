# Project map — SE Content GEO Score & Blog SEO Score

What each folder holds, and how to run it. Repo: `KhushbooNijhawanBuilds/se-geo-scoring`.

## Get it on the other laptop

```bash
git clone https://github.com/KhushbooNijhawanBuilds/se-geo-scoring.git
cd se-geo-scoring
```

The app's API key is **not** in the repo (it's gitignored). On the new laptop you add it once — see "Run the app" below.

## The two current, authoritative things

| Use this for | Folder |
| --- | --- |
| **GEO scoring — the latest standard, engine, prompts, test results** | `8-geo-v2.2/` |
| **The app you demo** | `2-streamlit-app/geo-score-app/` |
| **Prompts to paste into Copilot, named by content type** | `9-prompts-by-content-type/` |
| **SEO scoring (blogs only, separate score)** | `6-seo-score/` |

Everything else is background, source material, or older versions kept for traceability.

## Folder by folder

### `8-geo-v2.2/` — GEO scoring, current version (v2.2)
- `GEO_Scoring_Standard_All_Types_v2.2.md` — the full standard: all 26 page types, every criterion and check, weights per stage, deal-breakers, penalties, pilot results.
- `HOW_THE_SCORE_IS_CALCULATED.md` — the method in plain language, with a worked example. **Good to show in the presentation.**
- `CHANGELOG-v2.2.md` — the 17 fixes vs v2.1.
- `engine/geo_score_calc.py` — the calculator (the maths). `engine/weights.json` — the weights.
- `prompts/` — the 26 Copilot prompts (one per page type).
- `catalog.py`, `common.py`, `build_prompts.py`, `build_docs.py`, `verify_prompts.py` — scripts that generate the standard and prompts from the weights so they can't drift.
- `test-run/` — all 60 SE pages scored: the judge answers (`judge/`), the results (`result/`), the five `batch_*.md` write-ups, and `GEO_v2.2_vs_previous_vs_v2.1.xlsx` (results by page and by type). **The spreadsheet is good for the presentation.**

Run the calculator on one page's judge file:
```bash
cd 8-geo-v2.2
python3 engine/geo_score_calc.py --judge test-run/judge/02.json --md
python3 engine/geo_score_calc.py --selftest          # check it works
python3 engine/geo_score_calc.py --template faq       # empty judge form for a type
```

### `2-streamlit-app/geo-score-app/` — the web app
Runs on **Google Gemini** (default model `gemini-2.5-flash`).
- `app.py` — the Streamlit UI.
- `geoscore/` — the app logic: `judge.py` (calls Gemini), `explain.py` (turns judge answers into the score card), `capture.py` (fetches a page), `type_info.py` (the "How this page type is scored" panel), `catalog.py` / `standard_v22.py` (the per-type data), `__init__.py`.
- `engine/` — a copy of the v2.2 calculator and weights the app uses.
- `standard/` — a copy of the standard, Appendix A, and the 26 prompts.
- `examples/` — sample judge JSONs for the Replay tab.
- `requirements.txt` — Python packages. `README.md` — app setup. `.streamlit/` — config + `secrets.toml.example`.
- `start_mac.command` / `start_windows.bat` — double-click launchers.
- `geo-score-app.zip` (in `2-streamlit-app/`) — the app zipped up, no key inside.

### `9-prompts-by-content-type/` — ready-to-paste prompts
One file per content type, named in plain English (e.g. "Blog article - GEO prompt v2.2.txt"). `GEO v2.2/` has all 26; `SEO v1/` has the blog SEO prompt. **This is what you paste into GitHub Copilot in the demo.** Open the file for your page type, paste it, then give the page URL.

### `6-seo-score/` — blog SEO score (separate from GEO)
`SEO_Scoring_Standard_v1.md` (the standard), `seo_score_calc.py` (calculator), `seo_extract.py` (measures title length, meta, headings, links, alt text from a page), `copilot_prompt_blog_seo_v1.txt` (the prompt), `seo_weights.json`, `tests/` (6 SE blogs scored).

### `1-deck/` — the presentation slides
The slide files behind the Content GEO Score deck. Also published as a Slides artifact on claude.ai.

### `7-geo-all-types/` — GEO v2.1 all-types (superseded by `8-geo-v2.2/`)
The first all-types build. Kept for history; use `8-geo-v2.2/` instead.

### `3-prompts/` — early v2.1 blog prompts (superseded)
The original blog scoring + recommendations prompts. Use `9-prompts-by-content-type/` instead.

### `4-scoring-project-v2.1/` — the v2.1 research project
`GEO Elec Project/` — the full research base: `skill/geo-research/` (the original skill, scripts, references, weights), `research/` (academic + industry notes, the corpus of 60 SE page captures, the scored inventory CSV/XLSX), the SE source docs (playbook, toolkit, URL inventory), `CHANGELOG-v2.1.md`. `GEO_Scoring_Review.md` is the QA review. `GEO Elec Project v2.1.zip` is a zipped copy.

### `5-original-zip/` — the untouched original input
The "GEO Elec Project" exactly as first received, before any fixes. Reference only.

### `reports/` and `research_notes/`
`reports/Blog SEO scoring standard.md` — the SEO research report. `research_notes/` — the raw research notes behind the SEO score.

## Run the app (on the other laptop)

1. Install Python 3.10+ (3.11 is fine).
2. In a terminal:
   ```bash
   cd 2-streamlit-app/geo-score-app
   python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Add your Gemini key: copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and put your key in it:
   ```
   GEMINI_API_KEY = "your-key-from-aistudio.google.com/apikey"
   ```
4. Start it:
   ```bash
   streamlit run app.py
   ```
   It opens at `http://localhost:8501`. (On Mac you can instead double-click `start_mac.command`.)

The **Replay tab** works with no key: paste a Copilot answer's JSON block and it shows the full calculation.

## Demo flow for the presentation (no app needed)
1. Open the right prompt from `9-prompts-by-content-type/GEO v2.2/`.
2. Paste it into GitHub Copilot, then give the page URL.
3. Copilot returns the score and a JSON block.
4. (Optional) paste that JSON into the app's Replay tab to show the exact maths.

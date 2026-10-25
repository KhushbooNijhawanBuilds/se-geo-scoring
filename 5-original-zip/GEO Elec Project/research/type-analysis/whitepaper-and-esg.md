# Type analysis: white paper / technical document and sustainability / ESG report

*Content GEO Score Agent, type-logic proposal v2 (doc_esg). Prepared 2026-10-19. Builds on skill `geo-research` v1.0 (scoring-framework U1–U10, page-types §7 Document, judge-protocol). Nothing in the skill folder was edited. The proposed weights live in the session scratchpad (`agents/doc_esg/weights_doc_esg_v2.json`). The pilot judge JSONs are in `research/type-analysis/pilot/` (`25…30_judge.json`, `55…60_judge.json`, `59_doc_judge.json`, `60_doc_judge.json`).*

> **What the score means.** It measures how ready the **content** is to be cited. It does not predict citations. Retrieval rank, off-site consensus and technical access decide whether a page is cited at all. A recent 468k-citation study found retrieval explains about 32% of ChatGPT's within-site citation choice, against 2.8% for page properties (arXiv 2610.15033, Oct 2026). The content score is therefore necessary but not sufficient.

---

## 1. Executive summary

**Decision on gateway vs document.** The scoring unit is the **URL**.
- Every document asset gets a **Gateway score**: the HTML download or landing page. This is the headline Content GEO Score.
- When the document text is supplied, it also gets a separate **Document score**.
- The two scores are reported **side by side and never averaged** in v1. They have different owners and different fixes (web template and content owner vs. document author), and no evidence yet supports a blend ratio.
- A URL that serves a bare PDF gets Gateway ≈ 0, because the HTML layer is absent (gate G6), plus its Document score. The gap between the two numbers is the actionable signal: for #59 it is "Gateway 1 / Document 70".

**Proposed logic.** Five new type keys, all reusing U1–U10 and DOC-x with documented changes:
- `whitepaper_gateway`: 13 criteria. The main new ones are WP-1 abstract quality, WP-2 HTML key findings and WP-3 questions answered.
- `whitepaper_doc`: document module.
- `esg_hub` and `esg_report` (gateway): new ESG-1 HTML KPI layer, ESG-2 targets & progress, ESG-3 reporting basis, ESG-4 assurance & ratings, ESG-5 navigation & machine-readable companions.
- `esg_report_doc`: document module.

New rules:
- Gate **G8 "thin gateway"**: U7 and U8 are capped at level 2 when the HTML carries fewer than 3 substantive facts. Added after calibration round 1.
- Penalties: **placeholder_text** (−2) and **superseded_no_notice** (−3).
- A proposed sixth stage, **"Verification"**, for non-buyer stakeholders (investors, raters, procurement assessors). It was simulated; ESG pages are piloted at Evaluation.

**Pilot results** (v2, 14 scorings, 320 verbatim quotes all verified as substrings):

| Group | Scores |
|---|---|
| White-paper gateways (Education) | 28–44, median 34 |
| ESG hub | 16 |
| ESG report gateways (Evaluation) | 10–19 |
| Bare-PDF URLs #59/#60, gateway layer | 1 |
| Bare-PDF URLs #59/#60, document module | 70 (2023) / 68 (2022) |

No page meets the 70 threshold.

**What the scores measure.** The download-page component is one template for all ten HTML pages. For ESG pages the score measures the template almost entirely; the spread of 10–19 comes from title wording, missing period and version notes. For white papers, about half the variance is author-level, mainly abstract quality, version consistency and age.

What-if simulations:
- **White paper #28:** rewriting only the abstract field (answer-first, with quantified findings) lifts it from 33 to about 71. Adding gateway template fields (H1, key findings, authors, related links, descriptive CTA) reaches about 80.
- **ESG #56:** an author-only KPI sentence reaches about 60. A KPI and targets template reaches about 80.

So the main fix is **a gateway template change plus an authoring standard**, not page-by-page rewriting.

**SE-wide patterns**:
- No H1.
- The abstract is duplicated in the server HTML (template).
- Code-style file names (`WP180_V1.1_EN.pdf`) and no "white paper" label.
- No key findings, authors or related links on any gateway.
- Version on the page differs from the file name on 2 of 6 white papers.
- 4 of 6 white papers are older than 24 months.
- The ESG pages carry **zero KPIs in HTML**. Unfinished CMS placeholders (`ZZ_Paragraph Title`) are visible to crawlers.
- The same report has three names ("Sustainability Report", "Sustainable Development Report", "Impact Report").
- Archived reports are bare PDFs that cannot signal they are superseded. The 2022 PDF's GHG values were later restated in the 2023 edition.
- A WebSearch for SE's own ESG prompts surfaces third-party pages (an investor-forum PDF fiche, an AI-extracted report aggregator, trade press) rather than se.com HTML.

---

## 2. Corpus audit

### 2.1 Method
- **Input:** server-HTML converted to markdown (corpus files 25–30 and 55–58, captured 2026-10-19).
- **Rendered-page checks:** #55 and #28 were checked in a browser on 2026-10-19. The rendered text matched, except that the duplicated blocks and the `ZZ_` placeholders are hidden from humans but present in the server HTML.
- **#59/#60:** the coordinator reported that the user approved the download. The extracted PDF text (`59_/60_sustainability-esg-report.pdf.md`) was **sampled by grep**, not read whole. Sampled sections: cover, TOC, letter, highlights, 1.2 SSI tables, 1.10/1.11 frameworks, 3.2–3.3 GHG and net-zero, 7.x assurance, 8.1 indicator tables.
- **Signals:** `python -I scripts/geo_content_check.py --file <md> --format md --pretty` was run on every file.
- **Checker limitations** (for SE Digital and skill maintenance; not scored):
  1. The corpus header comment is read as the "lead sentence" and its JSON counts as "quotes".
  2. The word "report" counts as an attribution phrase, so ESG pages show a misleading 14–17 attribution phrases.
  3. `kW/rack` is not recognised as a unit.
  4. In the PDF markdown, lines starting with `#11` are parsed as headings, so H1 = "recalls 23 24 14 25".

### 2.2 White papers (download pages), stage Education, persona: data center designers, operators and sustainability leads (inferred)

Prompts are *inferred* (1 seed + 4–5 fan-outs per page; full lists are in the judge JSONs).

| # | Page (doc ref, release, version) | Seed prompt (inferred) | What an AI can extract from the HTML today | Strongest GEO element | Weakest GEO elements | Prompt fit (fan-outs answered in HTML) |
|---|---|---|---|---|---|---|
| 25 | Data Centers are Essential to AI-driven Decarbonization of Power Sector (WP180, 26 Mar 2024, v1.0) | How can data centers and AI help decarbonize the power sector? | Thesis only: "data centers will allow smart management of supply and demand to mitigate carbon footprint" | Clear thesis, neutral voice | Background-first abstract (98 w); no numbers; **version 1.0 on page vs `WP180_V1.1_EN.pdf`**; > 24 months old; one-sided (no trade-offs) | 2/5 |
| 26 | Necessary Considerations for Designing DC Architectures in Data Centers (WP47, 20 Mar 2023, v1) | Design considerations for DC distribution in data centers | **The 5 focus areas** (power converter design, UPS bypass, isolation & earthing, DC fault modeling, protection selection); DC removes the AC/DC/AC stage | Best abstract in the set: names audience, approach and an enumerated finding | 5-sentence wall paragraph; vague conclusion ("allows for better data center designs"); 3.5 years old; no standards | 2/5 |
| 27 | Data Centers are Essential to AI-driven Decarbonization of Buildings (WP169, 26 Mar 2024, v1.1) | How do data centers and AI support building decarbonization? | Levers named: HVAC occupancy control, EV-charging load control, embodied carbon | Covers 3/5 fan-outs at sentence level | **Copy errors break terms** ("respectsbuilding", "likeEV", "buildings.Predictive"); "tremendous potential"; **v1.1 on page vs `WP169_V1.2_EN.pdf`**; 31 months old | 3/5 |
| 28 | Retrofitting Existing Power Systems for AI Clusters (WP126, 21 May 2026, v1.1) | How to retrofit data center power for AI clusters | One fact: AI models "can require megawatts of power at hundreds of kW/rack" | Highly prompt-aligned title; current date; version consistent | **65-word** abstract; "Guidance is provided…" with no guidance stated; no findings | 1/5 |
| 29 | Quantifying Data Center Scope 3 GHG Emissions to Prioritize Reduction Efforts (WP99, 25 May 2023, v1) | How to calculate data center Scope 3 emissions | "Scope 3 becomes a data center's largest contributor"; method (single hypothetical data center); named calculator | Only gateway stating a **method + original tool** (DOC-8 = 3) | Calculator named but not linked; "first comprehensive attempt" (unanchored claim); 8-sentence paragraph; 3.4 years old | 1/5 |
| 30 | Direct Liquid Cooling System Challenges in Data Centers (WP210, 6 Aug 2025, v1.1) | Challenges of direct liquid cooling in data centers | DLC "preferred cooling method for extreme chip power densities"; "eight most common … challenges" (not listed) | Current; DLC acronym defined; balanced framing | **64-word** abstract; the eight challenges are never named | 1/5 |

### 2.3 Sustainability / ESG pages, stage Evaluation (proxy; see §4.3), personas: investors and ESG analysts, rating agencies, customer procurement sustainability assessors (inferred)

| # | Page | Seed prompt (inferred) | What an AI can extract today | Strongest | Weakest | Prompt fit |
|---|---|---|---|---|---|---|
| 55 | Sustainability reports hub | Schneider Electric sustainability performance 2025 | That Q3 2026 results exist (16 Oct 2026) and the list of report years | **Freshness**: dated quarterly entries, editions by year (DOC-7 = 4) | **No KPI at all**; "Sustainability results for Q3 2026 are in" with no results; **3 `ZZ_Paragraph Title/Content` placeholders** in server HTML; annual cards are image-only (alt text only); "Check the answers" / "Find out more"; meta self-labels "best-in-class"; the Disclosure Dashboard that the PDFs point to is not surfaced | 0/5 |
| 56 | 2025 Sustainability Report download page (19 May 2026, v1.0, 15.5 MB) | SE 2025 sustainability report key figures | Title, date, size | Descriptive title and file name; current | Summary line "Sustainable Development Report" (a label, and a different name for the same report); 0 KPIs | 0/5 |
| 57 | Sustainability Report H1 2026 download page (30 Jul 2026, v1.1) | SE H1 2026 sustainability results | Title, date | Consistent naming; period in title | "Sustainability Report H1 2026 Results" only; v1.1 with no change note | 0/4 |
| 58 | Sustainability Impact Report download page (30 Jul 2026, v1.3, 23.9 MB) | What is the Schneider Sustainability Impact program and its results? | Nothing beyond the title | Date visible | **No period** in title or file name ("Impact Report.pdf"); subject never defined (G2); v1.3 with no change note | 0/4 |
| 59 | 2023 Sustainability Report: **bare PDF URL** (260 pp, ~158k words, tagged, 307 bookmarks) | SE 2023 scope 1 2 3 emissions | Gateway layer: nothing (no HTML). **Document:** full GRI-coded GHG table (Scope 1 112,792 tCO2e, market/location-based, 4 years), SSI baseline/progress/target table, GRI/SASB/TCFD basis, reasonable assurance on Scope 1-2 and limited on Scope 3 by a named auditor | Document disclosure depth (ESG-1 to ESG-5 = 4) | No gateway; highlights page lacks scope totals; **units split in text layer ("TCO e 2")**; **SSI chart values extract in the wrong order relative to the header**, a misquote risk; SASB cross-reference "pages 294 to 295" vs TOC p.228 (URD pagination leftover); cover says "Sustainable Development Report" vs metadata "Sustainability Report" | Doc 4/4 |
| 60 | 2022 Sustainability Report: **bare PDF URL** (222 pp, ~140k words, **untagged, no bookmarks**) | SE 2022 scope 1 2 3 emissions | Gateway: nothing. Document: clean GHG table (Scope 1 119,617 tCO2e), targets, assurance | Indicator table extracts cleanly with units | Untagged: split words ("Susta inable"), chart junk in text ("NO DATA SUPPLIED", French chart labels); **2022 values restated in the 2023 edition (2023 report lists 2022 Scope 1 = 119,447 after the SF6 GWP update) with no notice possible inside the 2022 PDF** | Doc 4/4 |

### 2.4 Cross-page patterns: template vs author

| Issue | Pages | Level | Owner |
|---|---|---|---|
| No H1; title rendered as H2 ×3; abstract duplicated + truncated copy + metadata block ×3 in server HTML | 25–30, 56–58 | **Template** (download-page component) | SE Digital → out-of-scope observation; affects U3 c1 |
| No slots for key findings, authors/owner, "questions this paper answers", related documents/tools, change note, document-type label | 25–30, 56–58 | **Template** | SE Digital + content design |
| Download control = raw file name + size (no descriptive CTA) | all download pages | Template (label) + author (file name) | Both |
| Meta description = abstract auto-truncated with "…" (WP) or a bare label (ESG) | all | Template (WP) / author field (ESG) | Both |
| Code-only file names (`WP99_V1_EN.pdf`, `SPD_WP126_V1_1_EN.pdf`) | 25–30 | **Author/DAM** | Document owner |
| Version on page ≠ version in file name | 25, 27 | **Author/DAM data entry** | Document owner |
| Abstract written background-first; no quantified findings; < 90 words | all WP; short: 28, 30 | **Author** | Document author |
| Copy errors (merged words) | 27 | Author | Document author |
| Stale (> 24 months), no review or supersession signal | 25, 26, 27, 29; 59, 60 | Author/owner (review cadence) | Document owner |
| Zero KPIs in HTML on ESG pages | 55–58 | Template **and** author (no KPI component; the description field is unused) | Sustainability/IR + SE Digital |
| CMS placeholder components published | 55 | Author/publisher QA | Hub owner |
| Three names for one report family; period missing (Impact Report) | 56, 58, 59, 60 | Author | Sustainability/IR |
| Archived editions linked as bare PDFs (2022/2023) while 2025 has a gateway | 55, 59, 60 | Linking decision | Hub owner + SE Digital |
| Text-layer quality (tagging, reading order, units) | 59, 60 | Authoring/production (InDesign export) | Report production agency |

**What this means for the standard.** The ESG gateways score 10–19 because the template has no place for facts. Scoring them page by page will flag the same gaps every time, so **fix the template once and require an authoring standard** (intake fields in §4.6). The standard should keep scoring per URL anyway, because the author-level gaps (abstract quality, version mismatch, naming, period, review age) still discriminate, and the score will measure adoption once the template changes.

---

## 3. External research and exemplars

Evidence labels: [C] controlled/causal · [L] large-sample correlational · [O] official · [P] practitioner opinion · [S] small sample · [Obs] own observation.

### 3.1 How AI engines treat white papers and PDFs

| Finding | Source (date) | Label | Implication |
|---|---|---|---|
| PDFs were 3.1% of cited URLs across ChatGPT/Gemini/Perplexity (main dataset). Title–query match gave +14.1% citations per SD (+26.4% in the B2B niche set), best-paragraph match +15.5%. FAQ blocks −3.4% within site. Retrieval explains 32% of within-site variation vs 2.8% for page properties | arXiv 2610.15033 "What Drives AI Citations?" (Oct 2026; 468k citations, Jun–Sep 2026) | [L]/[C-obs] | PDFs are cited, but rarely. The HTML title and an answer-shaped abstract paragraph are the measurable levers (U1, WP-1) |
| PDF cited in 35.4% of captures when published alone vs **60.4% with a companion HTML evidence page**. With both present, 51.7% of PDF-package citations still went to the PDF itself. Image-only or scrambled-reading-order PDFs extract poorly | MaxAEO "Can AI cite PDFs and videos? A 384-answer test" (8–10 Jul 2026; 8 engines, 2 runs) | [S], vendor, directional | Supports **two modules**: the gateway lifts discovery and citation, and the PDF still gets cited, so its text layer matters (DOC-4) |
| Google: "Making sure that important content is available in textual form"; structured data must match visible text | Google Search Central, *AI features and your website* (updated 2025-12-10) | [O] | HTML text layer for key findings/KPIs (WP-2, ESG-1) |
| Google can index PDF text (encoded document formats) | Google Search Central, *File types indexable by Google* | [O] | PDFs are not invisible. They are a weaker passage source |
| Microsoft: avoid PDFs for core information; lists, tables, snippable answers | Microsoft Advertising blog (8 Oct 2025; already in evidence base) | [O] | G6 interpretation for gateways |
| Gated assets are invisible to retrieval. Recommended pattern: ungate abstract, summary and key findings; gate the deep dive | Search Engine Land (gating & AI, 2025–26); Firebrand (Jan 2026); several vendor blogs | [P] | DOC-9 (conditional), house rule "Gate the deep dive, not the knowledge" |
| AI Overviews/AI Mode cite HTML "almost exclusively"; Perplexity most PDF-friendly | Subscribe PR blog (9 Aug 2026) | [P], vendor, no method | Directional only; not used for weights |

### 3.2 How AI answers ESG questions about companies

| Finding | Source (date) | Label | Implication |
|---|---|---|---|
| LLM extraction of airline emission KPIs from sustainability reports: **HTML sources gave better extraction than PDFs**. Explicit KPI terms in the prompt raised accuracy from < 30% to > 70% | Martín-Domingo et al., *Transportation Research Interdisciplinary Perspectives* 33:101599 (2025), 16 airline groups, GPT-4/o3-mini/DeepSeek R1 | [C-small], peer-reviewed | ESG-1: KPIs as HTML text with **canonical metric names** ("Scope 1 GHG emissions (tCO2e)") |
| ESG QA benchmark: LLMs struggle with factual consistency and traceability on corporate sustainability reports | ESGBench, arXiv 2511.16438 (Nov 2025) | [C] | Period, basis and boundary next to each KPI (ESG-1 c3, ESG-3) |
| Standard-aligned extraction pipelines reach up to 0.95 accuracy | EulerESG, arXiv 2511.21712 (Nov 2025; from abstract/snippet) | [C] (not read in full) | Framework-coded tables (GRI/ESRS codes) aid machine reading |
| 55% of surveyed institutional investors already use GenAI to evaluate companies' ESG performance; 61% plan to within 5 years | Workiva survey via ESG Today (11 Mar 2024; ~100+ investors) | [S], vendor | Non-buyer stakeholders ask AI about SE, which supports a "Verification" stage |
| What a SERP returns for SE's own ESG prompts: a French investor-forum "Say on Climate" fiche (PDF), an **AI-extracted report aggregator** (sustainabilityreports.com, which itself flags "may contain inaccuracies"), ditchcarbon, trade press, wire releases. No se.com HTML KPI page | WebSearch "Schneider Electric scope 1 2 3 emissions 2025" and "…sustainability performance 2025 results" (2026-10-19) | [Obs] | The answer gap is filled by third parties. **Owned HTML KPIs are the only content lever for accuracy** (Consensus Principle) |
| Frameworks AI answers reference: GHG Protocol scopes (market vs location), SBTi validation, CDP score, GRI/SASB/TCFD/ISSB, CSRD/ESRS, assurance level | SE 2022/2023 reports (sampled); ABB and Siemens pages below | [Obs] | ESG-2 to ESG-4 checks |
| ESRS digital tagging: EFRAG XBRL taxonomy (Set 1) published Aug 2024. Revised-ESRS taxonomy draft consulted autumn 2026. **No tagging obligation for 2026 reports; earliest FY2027** (dates still shifting) | XBRL International; BDO; PwC Germany blog (Sep 2026) | [P]/[O-secondary] | Machine-readable companions are *recommended* (ESG-5 c3), not required. Re-check the Official Journal before making them mandatory |
| EU Directive 2024/825 (Empowering Consumers for the Green Transition) bans generic environmental claims in B2C commercial practices, applying from 27 Sep 2026 | From prior knowledge, **[VERIFY with Legal]** | [O] (unverified here) | U7 on ESG pages: no generic "best-in-class / green" self-labels without substantiation |

### 3.3 Exemplars (fetched 2026-10-19)

| Exemplar | What it does well | What it lacks | Lesson for SE |
|---|---|---|---|
| **Siemens DEGREE page** (siemens.com/…/sustainability/degree/) | HTML KPI sentences with baseline and period, e.g. "…an overall reduction of 66% for Scope 1 & 2 emissions compared to the base year 2019"; 14 targets as H3s grouped under 4 impact areas; CSRD mentioned; links to Sustainability Statement PDF | No table; no SBTi or assurance mention | ESG-1/ESG-2 pattern: **target heading + baseline + progress sentence** |
| **ABB "Annual Reporting Suite 2024" press release** (27 Feb 2025) | Headline ESG KPIs with targets and baselines in HTML (Scope 1-2 −78% vs 2019; Scope 3 −8% vs 2022; targets 2030/2050) | No assurance or framework mention | Results press releases are the HTML ESG layer engines can read. SE's hub links them but does not summarise them |
| **Google 2026 Environmental Report page** | H1 + summary + 6 figure cards with units and footnoted methodology; "Explore the report with AI" | No emissions by scope or targets in HTML | Highlights layer + methodology footnotes; shows even best-in-class tech hubs omit scopes |
| **Vertiv white-paper landing page** (liquid cooling) | H1, topic bullets ("Three key types of liquid cooling") | **Gated form**, no authors, no date, no findings | Counter-example: topics ≠ findings; gating hides knowledge |
| **Uptime Institute Global Data Center Survey 2025** | Public executive summary and press release with key findings; full report gated | n/a | "Gate the deep dive, not the knowledge" done right |

---

## 4. Proposed logic per type

### 4.1 Gateway vs document scoring (standard rule)

| Situation at the URL | Headline Content GEO Score | Document module | Gates |
|---|---|---|---|
| HTML gateway + PDF (text not supplied) | Gateway logic (`whitepaper_gateway` / `esg_report` / `esg_hub`) | "Not assessed" | G6 if the gateway carries no key findings/KPIs |
| HTML gateway + PDF text supplied | Gateway logic | `whitepaper_doc` / `esg_report_doc`, reported alongside | Plus **G1 cross-check**: KPI/finding on the gateway ≠ document → G1 on the gateway |
| **Bare PDF URL** (no HTML) | Gateway logic with every HTML-layer check failing "NOT FOUND – bare PDF" (score ≈ 0–5, G6) | Document module from extracted text | Penalty `superseded_no_notice` for archived editions |
| Gated asset | Gateway logic + DOC-9 active | Only if the text is supplied | G6 if knowledge is behind the form |

**Rationale.** Engines cite both layers (MaxAEO: about 52/48 split). The HTML layer improves discovery and extraction accuracy (MaxAEO; airline study). Owners and fixes differ. A blended number would hide which layer to fix. *Open question:* a blend for dashboards (§7).

**Metadata vs fact contradictions.** A version or file-name mismatch fails U8 c3 and DOC-7 c2 but does **not** trigger G1. G1 is reserved for subject-matter facts an engine could repeat as an answer. ESG KPI mismatches between HTML and report **do** trigger G1, because of compliance and greenwashing risk.

### 4.2 White paper: gateway (`whitepaper_gateway`)

**What AI extracts:**
- the title (matched to "how to / what are" prompts)
- the abstract's opening sentences as the answer
- key findings and numbers
- what the paper covers (fan-out match)
- publisher, author and date
- a link to the PDF as a second citable source

**Must-haves:**
- prompt-aligned H1
- an answer-first abstract of 100–200 words
- 3–5 quantified key findings in HTML
- "questions this paper answers"
- authors, method and references
- release date, version and change note
- descriptive file name and CTA
- related papers and tools linked

**Common failures (all seen in the corpus):**
- background-first abstract
- "guidance is provided" with no guidance
- findings only in the PDF
- code file names
- version mismatch
- no review of papers older than 2 years

| ID | Criterion | W | Family | Binary checks (pass definition) | Anchor notes | Rationale / evidence |
|---|---|---|---|---|---|---|
| U1 | Answer-first title & abstract lead | 12 | answer_def | c1 first 1–2 abstract sentences state the paper's answer/thesis for the seed prompt (not background) · c2 title/H1 wording matches prompt intent (descriptive, not brand-first) · c3 key message in the top block (above metadata) · c4 any content sections open with a direct answer · c5 summary/takeaways block | Standard U1 anchors | Title–query +14–26% (arXiv 2610.15033) [L]; 44% of ChatGPT citations from top 30% [L] |
| WP-1 | Abstract quality (new) | 10 | answer_def | c1 90–220 words (100–200 ±10%), single instance, not truncated · c2 problem/context named · c3 audience named (role/segment) · c4 approach/method/contents stated · c5 main conclusion stated specifically (not "guidance is provided") · c6 copy-clean (no merged words/encoding errors) | Checks → level | Absorbs U2 (what/who/when/outcome) for documents; best-paragraph match +15.5% [L] |
| WP-2 | Key findings in HTML (new; replaces part of DOC-1) | 14 | evidence | c1 findings enumerated as discrete items (list or enumerated sentence) · c2 ≥ 2 quantified findings with units/conditions · c3 placed above the download block · c4 ≥ 1 non-commodity finding (SE analysis/model/field data, with condition) · c5 findings state the implication/action | Level ≤ 1 → G6 | MaxAEO +25 pts citation with an HTML evidence page [S]; HTML > PDF extraction [C-small]; Google "textual form" [O] |
| WP-3 | Questions answered / coverage (new) | 8 | fanout | c1 ≥ 3 specific topics beyond restating the title · c2 topics as question-style/descriptive headings · c3 ≥ 3 of 5 inferred fan-outs answered by ≥ 1 sentence in HTML · c4 one primary intent | Anchors: 2 topics named · 3 c1+c3 · 4 c1–c3 · 5 all | Fan-out retrieval [O]; 26–50% coverage sweet spot [L] |
| U4 | Factual density | 8 | specs | Standard U4. Exempt general acronyms (AI, IT, EV, HVAC, UPS) from c4 | — | Specs/numbers OR 8.6+ [C] |
| DOC-8 | Methodology, authorship & references *(revised for gateway)* | 10 | evidence | c1 named author(s) with role · c2 method/assumptions stated · c3 references/standards by number · c4 original/first-party evidence with conditions · c5 organizational accountability (publisher + doc number) | Whitepaper sub-type keeps U5 checks inside DOC-8 | Evidence-backed claims OR 2–46 [C]; 69% technical buyers use AI, 6% trust it → verifiability [L] |
| DOC-7 | Version, date, supersession *(revised)* | 8 | freshness | c1 visible release/update date · c2 **page version = file-name version** · c3 change note when version > 1.0 · c4 released or reviewed ≤ 24 months before scoring · c5 related/superseding editions linked or "current edition" stated | — | Recency OR 14+ [C]; old date worse than none [C] |
| DOC-5 | Title, file name & metadata *(revised)* | 4 | other | c1 descriptive title · c2 descriptive file name (subject words, not code-only) · c3 document type in words on the page ("White paper 126") · c4 meta description is a complete, non-truncated summary sentence | — | SE Toolkit Ch.7 [SE] |
| U3 | Extractable structure | 6 | other | Standard U3; c5 fails if findings live only in the PDF (→ U3 ≤ 2) | — | Self-containment +56% [C] |
| U8 | Entity clarity & consistency | 6 | other | Standard U8; c3 includes metadata consistency | G8 caps at 2 on thin pages | Consistent vs contradictory OR 1.7–4.1 [C] |
| U7 | Neutral tone | 4 | tone | Standard U7 (c4 N/A unless the paper compares options) | G8 caps at 2 | Promotion OR up to 362 against [C] |
| U10 | Stage fit & next step | 6 | commercial | c1 depth fits Education/Consideration · c2 audience language · c3 **descriptive download CTA** ("Download white paper 126: Retrofitting…, PDF 1.4 MB") · c4 links to related papers, TradeOff tools and solution pages | — | SE CTA rule [SE] |
| DOC-9 | Gate the deep dive, not the knowledge | 4 | other | Only if gated: c1 key findings visible before the form · c2 definitions/framework visible · c3 form asks only what is needed. All N/A if ungated → weight redistributed | — | [P]; house rule |
| | **Total** | **100** | | | | |

- **Natural stages:** Education (default) and Consideration. Flag Decision.
- **Sensitivity:** at Consideration, scores move by ≤ 2 points.

### 4.3 Sustainability / ESG

**What AI extracts.** For prompts like "Schneider Electric scope 1 2 3 emissions", "…sustainability performance 2025", "Is SE SBTi validated?" or "…CDP score":
- emissions by scope with period and basis (market/location)
- % change vs baseline
- targets (year, baseline, validation)
- progress and program scores
- reporting frameworks
- assurance level and provider
- ratings
- report edition and date
- where the data or GRI index lives

**Who asks:**
- investors and ESG analysts
- rating agencies
- **customer procurement assessors** (supplier Scope 3 and decent-work checks)
- media, employees and candidates

**Stage proposal.**
- The five buyer stages fit only the procurement persona (Evaluation: supplier proof).
- Propose a **6th stage "Verification"** (stakeholder due diligence). Multipliers: answer_def 1.0, evidence 1.3, fanout 1.0, tone 1.1, comparison 1.0, specs 1.4, proof 1.3, commercial 0.5, freshness 1.3.
- This needs a one-line change to `STAGES` in `geo_score_calc.py`.
- Until then, **score ESG at Evaluation**. Simulated "Verification" changed pilot scores by 0–1 points (all ESG criteria are near 0 on the HTML side, and 70/68 for the documents either way), so the interim choice is safe.

**Must-haves (gateway):**
- 40–60-word answer paragraph with the headline result
- HTML KPI table: Scope 1, Scope 2 (market and location), Scope 3, total vs baseline, with period and boundary
- targets table: baseline year, target year, progress %, SBTi status, on/off track
- reporting basis and assurance block
- contents and companion links: data dashboard, GRI/ESRS index, CDP response, previous editions
- canonical report name with period

**Common failures:**
- KPI-free download pages
- placeholders
- three names for one report
- missing period
- versions with no change note
- archived bare PDFs
- restatements with no notice

**ESG IDs (new):**

| ID | Criterion | Checks (pass definition) | Family |
|---|---|---|---|
| ESG-1 | Headline KPI layer | c1 ≥ 3 headline KPIs with value + unit · c2 GHG **by scope** (1, 2 with market/location basis, 3) in tCO2e · c3 each KPI has reporting period + boundary/coverage · c4 KPIs as table/list rows that extract with label, unit and value aligned (one metric per row; not image/chart-only) · c5 YoY or vs-baseline comparison | specs |
| ESG-2 | Targets, baselines & progress | c1 named targets · c2 baseline year + target year per target · c3 current progress per target · c4 external validation (SBTi) **or** status incl. missed/at-risk targets · c5 link to transition plan / target methodology | proof |
| ESG-3 | Reporting basis & methodology | c1 frameworks named (CSRD/ESRS, GRI, ISSB/TCFD, SASB) · c2 GHG Protocol + market/location basis · c3 reporting period and organizational boundary · c4 restatements/methodology changes disclosed or linked | evidence |
| ESG-4 | Assurance & ratings | c1 external assurance level + provider · c2 scope of assured indicators · c3 third-party ratings/validations with date (CDP, MSCI, EcoVadis, SBTi) · c4 assurance statement included/linked | evidence |
| ESG-5 | Navigation & machine-readable companions | Gateway/hub: c1 each report entry states type + period + release date · c2 1–2-sentence description of contents · c3 links to companions (data annex XLSX/CSV, GRI/ESRS index HTML, CDP response; XBRL when available) · c4 descriptive anchors · c5 current vs archived editions labelled. *Document module:* c1 TOC with pages · c2 bookmarks/outline · c3 content index (GRI/SASB/TCFD/ESRS) · c4 companion data referenced · c5 cross-references accurate | other |

**Weights:**

| ID | `esg_hub` | `esg_report` (gateway) | `esg_report_doc` | Rationale |
|---|---|---|---|---|
| U1 (answer-first: company + report + period in title; headline result first) | 12 | 10 | — | Title/paragraph match [L] |
| DOC-1 (document: highlights with KPIs + basis in first 5 pages; points to HTML home) | — | — | 12 | Answer-first inside long PDFs; first 30% of page [L] |
| ESG-1 | 20 | 22 | 18 | Numbers/specs strongest cue [C]; HTML > PDF for ESG KPI extraction [C-small]; third parties fill the gap [Obs] |
| ESG-2 | 12 | 14 | 10 | Targets/progress are the second-most asked ESG facts [Obs]; evidence-backed claims [C] |
| ESG-3 | 6 | 10 | 12 | Traceability failures in ESG QA (ESGBench) [C] |
| ESG-4 | 6 | 8 | 10 | Verifiability for low-trust audiences [L] |
| ESG-5 | 14 | 8 | 6 | Hub's job is routing; companions aid machine reading [P] |
| U3 (structure; no placeholders) | 8 | — | — | Self-containment [C] |
| DOC-4 (text-extractable file) | — | — | 12 | Scrambled reading order → poor extraction (MaxAEO) [S]; observed misquote risk in #59 |
| DOC-7 (edition, period vs release date, change note, cadence, supersession) | 8 | 10 | 8 | Freshness [C]; restatement risk [Obs] |
| U8 (canonical naming, metric consistency) | 4 | 6 | 6 | Consistency [C]; G1 for KPI contradictions |
| DOC-5 | — | 4 | — | Title/file name |
| U7 (no generic green claims; misses disclosed) | 4 | 4 | 6 | Promotion hurts [C]; EU 2024/825 [O, verify] |
| U10 (routing to hub/IR/data/press release) | 6 | 4 | — | House CTA rule |
| **Total** | **100** | **100** | **100** | |

### 4.4 Document modules (optional, when the PDF text is supplied)

**`whitepaper_doc`** (weights): DOC-1 14 · DOC-2 12 · DOC-3 8 · DOC-4 10 · DOC-5 6 · DOC-6 8 · DOC-7 10 · DOC-8 14 · U4 8 · U8 5 · U7 5 = 100.

**DOC-1 is redefined for the document module:**
- c1 executive summary with key findings on pages 1–2
- c2 ≥ 2 quantified findings in it
- c3 questions/scope stated
- c4 link back to the HTML gateway URL
- c5 findings in prose (not only in infographics)

DOC-9 moves to the gateway logic. Not piloted: no white-paper PDF text was supplied.

**`esg_report_doc`**: see §4.3. Piloted on #59/#60.

**Judge sampling protocol** for documents over 20k words: sample the first 6 pages, the highlights, the TOC, the GHG/KPI section, the targets table, the methodology/assurance section and the indicator annex. Record which sections were read in `stage_fit.note`. Confidence is medium if any of these is missing.

### 4.5 DOC-x changes (explained)

| ID | Change | Why |
|---|---|---|
| DOC-1 | Gateway context: **decomposed** into U1 + WP-1 + WP-2 + WP-3 (44 points vs 18). Document context: redefined as an in-document summary layer + link back to the gateway | When the gateway *is* the scored page, one 18-point criterion cannot carry the whole page |
| DOC-5 | Adds c3 "document type in words" and c4 "meta description complete, not truncated" | All 6 white-paper pages fail both; this is wording, so in scope |
| DOC-7 | Adds c2 page version = file version · c4 24-month review window (white papers) / current edition (ESG) · c5 supersession links. ESG variant: reporting period distinct from release date | Version mismatches on 25/27; restated 2022 values |
| DOC-8 | Gateway variant: author, method, references, original evidence, accountability are visible **on the HTML page** | Verifiability for low-trust technical buyers |
| DOC-9 | Conditional: all-N/A when ungated (weight redistributed) | SE white papers are ungated; the criterion still guards the gated case |

### 4.6 Gates, caps, penalties

| ID | Trigger | Effect | Justification |
|---|---|---|---|
| G6 *(interpretation for gateways)* | Gateway has no key findings (WP-2 ≤ 1) or no KPIs (ESG-1 ≤ 1) in HTML, or the URL is a bare PDF | U3 ≤ 2; overall ≤ 59 | Existing gate. Fired on all 12 gateway scorings. Not binding at current levels, but the right flag |
| G1 *(ESG extension)* | KPI on gateway/hub ≠ KPI in report or press release for the same period and basis | U8 = 0; ≤ 59 | ESG misstatement is a compliance and greenwashing risk |
| G2 | Subject/period never defined (U1 = 0) | ≤ 39 | Fired on #58 |
| **G8 (new, v2)** | Thin gateway: < 3 substantive factual statements (finding, mechanism, figure or KPI) in HTML | U7, U8 max level 2 (no cap) | Calibration: consistency/tone passed vacuously on empty pages (§5.2) |
| **placeholder_text (new)** | Unfinished CMS components (`ZZ_…`, "Lorem ipsum", "[Title]") in server HTML, even if hidden | −2 | Crawlers read them (#55). Content QA defect, not manipulation, so not the −10 hidden-instruction penalty |
| **superseded_no_notice (new)** | Newer edition exists and the asset neither links nor labels it (bare archived PDFs always) | −3 | Old values get quoted as current. 2022 Scope 1 was later restated (119,617 → 119,447) |
| Existing | stuffing −3, fluff −2 (> 1.5/100w), boilerplate −2, CTA overload −1, self-ranking −3, hidden instructions −10 | unchanged | None fired except as noted |

### 4.7 Recommendation templates (fix library additions)

| Failed check | Recommendation (Owner) |
|---|---|
| WP-2 c1–c2 | Add a **"Key findings"** list (3–5 bullets) under the abstract. Each bullet is self-contained and states one quantified result with its condition, e.g. "AI training racks can draw [VERIFY: kW]/rack, [VERIFY]× a typical enterprise rack." (Document author + SE Digital for the slot) |
| U1 c1 / WP-1 c5 | Rewrite the first 2 abstract sentences as the answer, keeping the title's query words. BEFORE "The IT industry is developing large generative AI models at a fast pace." → AFTER "Retrofitting an existing data center for AI clusters requires [VERIFY: 3 main changes] because AI racks draw [VERIFY] kW each, far above the [VERIFY] kW the existing distribution was designed for." (Author) |
| WP-3 c2 | Add **"Questions this paper answers"** as 3–5 question-style H3s with a one-sentence answer each (Author + template) |
| DOC-8 c1–c3 | Add an "Authors & method" line: names + roles, method/assumptions, and standards/references by number (Author) |
| DOC-7 c2–c5 | Align page and file version. Add "What changed in v1.1". Review papers older than 24 months (substantive update, never a date bump). Link newer/older editions (DAM owner) |
| DOC-5 c2–c4 / U10 c3 | Descriptive file name (`SE-WP126-Retrofitting-Power-Systems-for-AI-Clusters-v1.1-EN.pdf`). Label "White paper 126". Full meta sentence. CTA "Download the white paper (PDF, 1.4 MB)" (DAM + template) |
| U10 c4 | Link the related TradeOff Tool by name (#29 → "Data Center Lifecycle CO2e Calculator") and 2–3 related papers/solution pages (Author) |
| ESG-1 | Add an HTML **KPI table** (metric · value · unit · period · basis · vs baseline), sourced from the assured indicator table. Values come only from the published report: [VERIFY with Sustainability controller]. (Sustainability/IR + template) |
| ESG-2 | Add a targets table: target · baseline year · target year · latest progress · SBTi status · on/off track, including missed or at-risk targets (Sustainability) |
| ESG-3/ESG-4 | Add a "Reporting basis & assurance" block: frameworks, GHG basis, period/boundary, assurance level + provider + scope, ratings with date, restatement notes (Sustainability/IR) |
| ESG-5 / U10 | List the Disclosure Dashboard (data), GRI/ESRS index, CDP response, press release and previous editions with descriptive anchors (Hub owner) |
| U1 (hub) | Replace "Sustainability results for Q3 2026 are in" with a 40–60-word answer paragraph: program score + 3 KPIs + date [VERIFY], updated with each quarterly release (Hub owner) |
| placeholder_text | Remove or populate `ZZ_` components before publishing; add a CMS pre-publish check (Hub owner / SE Digital) |
| superseded_no_notice | Give archived editions an HTML gateway that says "Superseded by the [year] report; 2022 GHG values were restated in the 2023 report (SF6 GWP AR6)" and links forward (Sustainability + DAM) |
| DOC-4 | Production brief for the report agency: tagged PDF, real tables (units not as split subscripts), chart values also in tables, reading order checked, bookmarks, cross-references re-paginated for the extract (Report production) |

### 4.8 Intake-sheet fields

| Type | Extra fields (★ = mandatory for this type) |
|---|---|
| White paper | ★ doc ref / WP number · ★ title · ★ release date + version (+ change note) · ★ gated Y/N · authors + roles · 3–5 key findings (author-supplied, with source page) · target prompts / questions answered · method/standards · related tools/papers/solution pages · supersedes / superseded-by · PDF text supplied Y/N (document module) · languages |
| ESG report / hub | ★ report type (annual / half-year / quarterly / impact / CSRD sustainability statement / CDP / TCFD) · ★ reporting period · ★ release date + version (+ change note) · ★ canonical report name · headline KPI sheet (metric, value, unit, period, basis, assured Y/N; source = Sustainability controller) · targets (baseline, target year, progress, SBTi status) · frameworks · assurance level/provider/scope · restatements · previous/next edition URLs · data annex / GRI-ESRS index / CDP URLs · stakeholder audience (investor / rater / procurement / media) · Legal/claims review status · PDF text supplied Y/N |

---

## 5. Pilot scores and calibration

Weights: `weights_doc_esg_v2.json` (scratchpad). Calculator: `python -I scripts/geo_score_calc.py --judge <judge> --weights <weights> --md`. Quotes: 320 evidence spans checked by `verify_quotes.py` (whitespace/case-normalized substring); **0 not found**.

### 5.1 Pilot table (v2)

| # | Page | Logic | Stage | Score | Band | Gates / penalties | Top 3 gaps (recoverable points) |
|---|---|---|---|---|---|---|---|
| 25 | WP180 power-sector decarbonization | whitepaper_gateway | Education | **31** | Poor | G6 | WP-2 key findings (17.4) · DOC-8 method/authors (9.9) · U1 answer-first (8.3) |
| 26 | WP47 DC architectures | whitepaper_gateway | Education | **44** | Average | G6 | WP-2 (10.5) · DOC-8 (9.9) · U1 (8.3) |
| 27 | WP169 buildings decarbonization | whitepaper_gateway | Education | **28** | Poor | G6 | WP-2 (17.4) · DOC-8 (9.9) · U1 (8.3) |
| 28 | WP126 retrofitting for AI clusters | whitepaper_gateway | Education | **33** | Poor | G6, G8 | WP-2 (17.4) · DOC-8 (9.9) · U1 (8.3) |
| 29 | WP99 data center Scope 3 | whitepaper_gateway | Education | **40** | Average | G6 | WP-2 (17.4) · U1 (8.3) · WP-3 (5.5) |
| 30 | WP210 DLC challenges | whitepaper_gateway | Education | **34** | Poor | G6, G8 | WP-2 (17.4) · DOC-8 (9.9) · U1 (8.3) |
| 55 | Sustainability reports hub | esg_hub | Evaluation | **16** | Poor | G6, G8; placeholder −2 | ESG-1 KPIs (26.1) · ESG-2 targets (14.6) · ESG-5 navigation (9.7) |
| 56 | 2025 Sustainability Report page | esg_report | Evaluation | **19** | Poor | G6, G8 | ESG-1 (28.2) · ESG-2 (16.8) · ESG-3 (8.6) |
| 57 | H1 2026 Sustainability Report page | esg_report | Evaluation | **17** | Poor | G6, G8 | ESG-1 (28.2) · ESG-2 (16.8) · ESG-3 (8.6) |
| 58 | Sustainability Impact Report page | esg_report | Evaluation | **10** | Poor | G2, G6, G8 | ESG-1 (28.2) · ESG-2 (16.8) · ESG-3 (8.6) |
| 59 | 2023 report, bare PDF URL: **gateway** | esg_report | Evaluation | **1** | Poor | G6, G8; superseded −3 | ESG-1 (29.2) · ESG-2 (17.4) · ESG-3 (8.9) |
| 59 | 2023 report: **document module** | esg_report_doc | Evaluation | **70** | Good | superseded −3 | ESG-1 units garbled (4.8) · DOC-7 no date/successor (4.6) · DOC-1 highlights lack scopes (4.2) |
| 60 | 2022 report, bare PDF URL: **gateway** | esg_report | Evaluation | **1** | Poor | G6, G8; superseded −3 | as #59 |
| 60 | 2022 report: **document module** | esg_report_doc | Evaluation | **68** | Average | superseded −3 | DOC-4 untagged / chart junk (6.3) · ESG-1 (4.8) · DOC-7 (4.6) |

All judgements have high confidence. #59/#60 were initially scored at low confidence from URL metadata only (gateway 2/100). The PDF text then became available (user-approved download, per the coordinator), so the gateway absence is certain and the document module was added. Prompts are inferred.

### 5.2 Calibration

**Round 1 → round 2 (one adjustment):**

| # | v1 | v2 | Change |
|---|---|---|---|
| 28 | 37 | 33 | G8: U7 4→2, U8 4→2 (one substantive fact in HTML) |
| 30 | 38 | 34 | G8 (two facts) |
| 57 | 20 | 17 | G8: U8 4→2 |
| 58 | 11 | 10 | G8 |
| 59/60 gateway | 2 (low conf.) | 1 (high) | Judge update after PDF text: naming inconsistency, PDF title metadata |
| 25, 26, 27, 29, 55, 56 | unchanged | | Not thin, or already ≤ 2 |

**Why G8.** In v1 a 65-word abstract or an empty ESG page got U8 = 4 ("no contradictions") and U7 = 4 ("no hype"), because there was nothing to contradict or hype. That inflated the thinnest pages and compressed their gap to richer gateways. After G8, #28/#30 (fact-light) sit below #26/#29 (fact-bearing), which matches expert reading.

**Does the score discriminate?**
- **White papers (28–44, 16-point spread).** Yes, on author-level factors:
  - abstract quality (WP-1 2–4)
  - stated method/original tool (#29 DOC-8 = 3)
  - version mismatch (#25/#27 U8 = 2)
  - age (DOC-7 1–3)
  - copy errors (#27)

  The ranking 26 > 29 > 30 ≈ 28 > 25 > 27 matches a reading of which abstract an engine could quote as an answer.
- **ESG gateways (10–19).** Barely. They are the same template with no fact slots. The remaining spread is title period, version note and subject definition. **This is a template finding**: the fix is a KPI/targets component, after which ESG-1 to ESG-4 will discriminate between authors.
- **Bare PDFs.** Gateway 1 for both, a structural fact. The document module separates them on extractability (2023 tagged with bookmarks vs 2022 untagged with chart junk). Disclosure criteria are equal (4) because both derive from the audited Universal Registration Document.

**Non-discriminating criteria in this sample:**

| Criterion | Pages | Decision |
|---|---|---|
| WP-2 | 0 on 5/6 | **Kept.** It is the main evidence-backed lever (MaxAEO, airline study, Google) and the main template gap |
| ESG-1 to ESG-4 (gateways) | 0 on all | **Kept**, for the same reason. Siemens and ABB show it is feasible, and SE's PDFs already hold the facts |
| U10 | 2 on all WPs | **Kept.** It discriminates once a CTA and related links exist |
| U1 | 2 on all WPs | **Kept.** No SE abstract is answer-first, which is a finding in itself |
| DOC-5 | 1 on all WPs | **Kept at 4.** Low weight; mostly DAM/template |

**Headroom simulations** (SIMULATED levels, not real content; scratch `sim_*.json`):

| Page | Author-only fixes (current template) | Template + author |
|---|---|---|
| #28 white paper | 33 → **71** (answer-first abstract with findings, method, descriptive file name, version note) | **80** |
| #56 ESG report | 19 → **60** (description field carries 5 KPIs, period, basis, assurance) | **80** |

For white papers the abstract field is the biggest single lever. For ESG the template is the binding constraint.

**Inflation watch.** HTML gateway median is 18–34, well below the 40–60 gold-set target. That is expected for unoptimized download pages, not judge harshness: no page states more than 1 quantified fact in HTML. The document module at 68–70 shows the rubric does reward substance where it exists.

**Next.** Run human double-rating on these 14 scorings (κ per criterion, target ≥ 0.6). G8's "substantive statement" count is the most judgement-dependent rule, so watch its κ. Then run outcome validation with a fixed panel on the white-paper and ESG prompts (≥ 7 runs per engine).

---

## 6. Proposed weights JSON fragment (merge into `assets/weights.json`; selftest passes)

```json
{
  "families_additions": {
    "answer_def": ["WP-1"],
    "evidence":   ["WP-2", "ESG-3", "ESG-4"],
    "fanout":     ["WP-3"],
    "specs":      ["ESG-1"],
    "proof":      ["ESG-2"]
  },
  "page_types": {
    "whitepaper_gateway": {"U1": 12, "WP-1": 10, "WP-2": 14, "WP-3": 8, "U4": 8, "DOC-8": 10, "DOC-7": 8, "DOC-5": 4, "U3": 6, "U8": 6, "U7": 4, "U10": 6, "DOC-9": 4},
    "whitepaper_doc":     {"DOC-1": 14, "DOC-2": 12, "DOC-3": 8, "DOC-4": 10, "DOC-5": 6, "DOC-6": 8, "DOC-7": 10, "DOC-8": 14, "U4": 8, "U8": 5, "U7": 5},
    "esg_hub":            {"U1": 12, "ESG-1": 20, "ESG-2": 12, "ESG-3": 6, "ESG-4": 6, "ESG-5": 14, "U3": 8, "DOC-7": 8, "U7": 4, "U8": 4, "U10": 6},
    "esg_report":         {"U1": 10, "ESG-1": 22, "ESG-2": 14, "ESG-3": 10, "ESG-4": 8, "ESG-5": 8, "DOC-7": 10, "U8": 6, "DOC-5": 4, "U7": 4, "U10": 4},
    "esg_report_doc":     {"DOC-1": 12, "ESG-1": 18, "ESG-2": 10, "ESG-3": 12, "ESG-4": 10, "ESG-5": 6, "DOC-4": 12, "DOC-7": 8, "U8": 6, "U7": 6}
  },
  "gates": {
    "G8": {"cap": 100, "max_level": {"U7": 2, "U8": 2}, "desc": "Thin gateway: < 3 substantive factual claims in HTML; consistency/tone passes are vacuous (U7, U8 max 2)"}
  },
  "penalties": {"placeholder_text": 2, "superseded_no_notice": 3},
  "stage_multipliers_proposed": {
    "Verification": {"answer_def": 1.0, "evidence": 1.3, "fanout": 1.0, "tone": 1.1, "comparison": 1.0, "specs": 1.4, "proof": 1.3, "commercial": 0.5, "freshness": 1.3}
  }
}
```

Notes:
- Each ID belongs to exactly one family. DOC-5, DOC-9, ESG-5, U3 and U8 stay "other" (multiplier 1.0).
- Add aliases `"white paper gateway"`, `"esg report"`, `"esg hub"` to `TYPE_ALIASES`. The existing alias `"whitepaper" → document` should then point to `whitepaper_gateway` or `whitepaper_doc` depending on input mode.
- The "Verification" stage needs `STAGES` extended in `geo_score_calc.py`.

---

## 7. Open questions and risks

1. **Blend or not.** Should dashboards show one "asset score" (e.g. 0.5 × gateway + 0.5 × document)? Recommendation: no blend until outcome validation. Always show the pair.
2. **Threshold per type.** 70 for gateways may be unreachable without the template change. Consider 60 for gateways until the template v2 ships, and keep 70 for documents.
3. **Ownership.** The download-page component (SE Digital), DAM metadata (file names, versions, meta descriptions), Sustainability/IR (KPIs) and the report agency (PDF production) all need named owners, or recommendations will stall.
4. **ESG KPI copy is regulated content.** HTML KPIs must come from the assured indicator set and match the PDF/URD exactly (G1 risk). They need Legal/claims review (EU 2024/825 timing to be verified by Legal). The quarterly hub refresh adds an update burden; an old visible number is worse than none.
5. **Restatements.** The 2023 edition restates 2022 GHG values. Archived PDFs will keep being quoted. The fix is HTML archive gateways with restatement notes, not editing old PDFs.
6. **G8 reliability.** "Substantive statement" counting is judge-dependent. Measure κ and, if needed, tie it to deterministic signals (numbers with units + enumerated findings).
7. **Stage model.** The "Verification" stage needs a script change and Score Agent deck sign-off. Until then ESG uses Evaluation; the simulation shows ≤ 1-point difference on the pilot.
8. **Evidence strength.** The PDF vs HTML evidence is directional:
   - MaxAEO: small vendor test, 2 runs.
   - Airline study: 16 companies.
   - arXiv 2610.15033: one consumer and one B2B niche, not industrial.
   - No controlled study yet on ESG answer sourcing.

   Weights are priors to calibrate.
9. **Digital tagging (ESRS XBRL).** The timeline is unsettled (earliest FY2027). Keep it as a recommended companion, not a check requirement.
10. **Document-module sampling.** 150k-word reports cannot be judged whole. The sampling protocol (§4.4) must be fixed and versioned, or scores will vary by which pages the judge reads.
11. **Server vs rendered HTML.** Hidden duplicates and placeholders exist only for crawlers. Scoring uses server HTML; confirm this policy with SE Digital.
12. **Checker fixes** (skill maintenance, not done here): strip HTML comments, drop "report" from attribution phrases, add `kW/rack`-style units, ignore `#NN` lines in PDF markdown.

*Disclaimer: citation-readiness of content only; actual AI citation also depends on retrieval, off-site consensus and technical access.*

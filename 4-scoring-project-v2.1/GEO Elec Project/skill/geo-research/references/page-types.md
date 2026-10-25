# Page-Type Scoring Logic (v1.0, Oct 2026). See `page-types-v2.md` for the v2.0 standard types

Each page type launches its own logic: **criteria + default weights (sum = 100) + binary checks + must-haves + common failures**. Universal criteria U1–U10 are defined in `scoring-framework.md`. Stage multipliers are applied afterwards (`buyer-journey.md`).

Weights are **evidence-informed starting points**, not fitted to data. Calibrate them against SE gold-set pages (see `judge-protocol.md` §6) before locking.

Contents: 1 PDP · 2 Product Range · 3 Product Category · 4 CaaS / reusable block · 5 Editorial (common logic) · 6 Article / blog · 7 Document · 8 Case study · 9 Comparison / selection guide · 10 FAQ / support · 11 Glossary · 12 Solution / industry landing · 13 Video asset · 14 Image / visual module · 15 How to classify an unknown page

> PIM/OfferDAM note: on PDP, range and category pages many fields (specs, descriptions, documents) come from PIM/OfferDAM, not Builder.io. Recommendations for those fields must be tagged **Owner: PIM champion**. Editorial blocks are tagged **Owner: content owner**.

---

## 1. Product Detail Page (PDP)

**What AI extracts:** product identity (name, ref/SKU, brand), key specs with units, primary application, compatibility and accessories, standards and certifications, availability/where to buy, lifecycle, and answers to specific questions ("Is X compatible with Y?", "What is the breaking capacity of…?"). PDPs are cited mainly for **transactional and navigational** intents (≈25% / 22% of citations), rarely for informational ones. AI shopping surfaces consume the PDP *as data*, so completeness and consistency beat prose style.

| ID | Criterion | W | Checks (pass/fail + quote) |
|---|---|---|---|
| U1 | Answer-shaped product summary | 10 | 40–80-word summary at top; follows the 3-part answer shape (subject + primary function → citable differentiator → target application/audience); ≥2 quantified specs in it |
| U2 | What / Who / When / Outcome | 6 | see U2 |
| PDP-1 | Spec table completeness & quality | 16 | Specs in an HTML-text table/list (not image/PDF-only); attribute name + value + unit; grouped (electrical / mechanical / environmental / communication); no "N/A" filler; covers the category's key attributes (≈ ≥ 8–10 top specs; ≥ 95% of required attributes for Level 5) |
| PDP-2 | Applications & use cases | 8 | ≥ 3 specific application noun phrases ("for EV charging and PV installations where DC fault currents can occur"); environments/conditions; exclusions or when not to use |
| PDP-3 | Compatibility & ecosystem | 7 | Compatible accessories / complementary products; protocols and software compatibility; predecessor/successor refs; each named with a descriptive link |
| PDP-4 | Standards & certifications | 6 | Standards cited by number (+ edition where relevant): IEC/UL/EN/CE/UKCA/RoHS/REACH/PEP/EPD/IEC 62443…; proof document linked |
| PDP-5 | Product Q&A | 7 | ≥ 3 (Level 5: ≥ 5) real buyer questions; direct answer in the first sentence, 40–80 words total; answers name the product; sourced from support, sales or prompt research |
| PDP-6 | Differentiation & selection vs siblings | 5 | "Choose this if…" statement; how it differs from range siblings or the previous generation (quantified); link to the range comparison |
| PDP-7 | Proof | 4 | Substantive reviews/ratings (B2C) or references, installed base, case-study links with metrics (B2B) |
| PDP-8 | Commercial & lifecycle facts | 5 | Where to buy / availability, warranty, lifecycle status (active / EOL / replaced by [named ref]), substitutes |
| PDP-9 | Documents & media described | 5 | Datasheet, manual, CAD/BIM, EPD linked with descriptive anchors; key facts from them mirrored in HTML; videos/images have descriptive titles + 3–4-bullet summaries |
| U4 | Factual density & specificity | 6 | |
| U7 | Neutral tone | 5 | |
| U8 | Entity clarity & consistency | 6 | Prose values = table values; model code paired with plain name |
| U9 | Freshness & currency | 4 | |

**Gates:** G3 (no quantified specs in text → ≤ 40). G1 (prose vs table contradiction → ≤ 59).
**Common failures:** marketing-only description ("innovative, reliable, smart"); specs only in PDF or image; specs hidden in collapsed tabs; boilerplate shared across hundreds of SKUs; no use cases; no compatibility info; discontinued status not stated; prose and table disagree.
**Expected-facts checklist (U6 helper):** what it is · rating(s) · key dimensions/weight · operating conditions · standards · application · compatibility · availability/lifecycle · documents.
**Evidence notes:** E-GEO (e-commerce GEO study): rewrites that align with user intent, state competitive differentiation and surface review evidence work; storytelling (−4.0 rank) and minimalist copy hurt. OpenAI's product feed and Google Merchant "conversational attributes" (Q&A, document links, parts & accessories) reward the same facts. Keep page, feed and datasheet consistent.

---

## 2. Product Range page (product family / series)

> **v2.0 (19 Oct 2026):** logic for range, article/blog, case study and solution pages is **superseded by `page-types-v2.md`**, which also adds news, service, software, calculator, white paper and ESG. The section below is kept for history. Use v2 for scoring.


**What AI extracts:** what the family is and who it is for; member variants and how they differ; selection axes (rating, poles, curve, communication); ecosystem; standards; migration from legacy ranges. Answers prompts such as "What is the [range] series?" and "Which [range] model should I choose for…?"

| ID | Criterion | W | Checks |
|---|---|---|---|
| U1 | Range definition & scope | 10 | "[Range] is a family of … for …" in the first sentence; scope stated (ratings, voltages, number of variants) |
| U2 | What / Who / When / Outcome | 6 | |
| RNG-1 | Variant comparison table with "best for" | 16 | HTML table; rows = variants, columns = decision attributes with units; a "best for" column |
| RNG-2 | Selection guidance in text | 12 | Decision path in prose or list ("If you need X and Y, choose Z"); not configurator-only |
| RNG-3 | Applications / segments + references | 8 | Named segments and applications; ≥ 1 reference or case link |
| RNG-4 | Quantified differentiators | 8 | Range-level claims with numbers and the basis of measurement ("up to 30% smaller footprint vs previous generation, measured as…") |
| RNG-5 | Ecosystem & migration | 7 | Accessories, software, compatible ranges; legacy range names + migration path (answers "replacement for [legacy]") |
| RNG-6 | Common standards | 5 | |
| RNG-7 | Range FAQ | 6 | Selection, compatibility and migration questions; FAQ rules |
| U3 | Extractable structure | 6 | |
| U5 | Evidence | 4 | |
| U7 | Neutral tone | 4 | |
| U8 | Entity consistency | 5 | Every member PDP linked by name |
| U9 | Freshness | 3 | |

**Common failures:** carousel/hero pages with no text; selection only via a configurator; no comparison table; no "best for" framing; legacy names missing.

---

## 3. Product Category page (e.g. circuit breakers, EV chargers, PLCs)

**What AI extracts:** category definition, types/sub-types, selection criteria, short lists. Google AI Mode leans towards official category and product pages. The category page should carry a compact **guide layer**, not just a product grid.

| ID | Criterion | W | Checks |
|---|---|---|---|
| U1 | Definition + main types | 10 | 50–100-word answer-first intro: what the category is, main types |
| U2 | Context | 5 | |
| CAT-1 | "How to choose" with thresholds | 16 | 4–8 selection criteria, each explained with units/thresholds (breaking capacity, trip curve, pole count, ambient temperature…) |
| CAT-2 | Type comparison table + "best for" | 14 | Residential / commercial / industrial; AC/DC; etc. |
| CAT-3 | Featured ranges, neutral positioning | 8 | One-line factual "best for" per range; no self-congratulation |
| CAT-4 | Standards / regulations | 5 | |
| CAT-5 | Category FAQ | 7 | Definitions, differences between types, sizing |
| CAT-6 | Links to guides / glossary / tools | 4 | Descriptive anchors |
| U4 | Factual density | 6 | |
| U6 | Fan-out coverage & focus | 7 | |
| U7 | Neutral tone | 7 | |
| U9 | Freshness | 5 | New standards/generations reflected |
| U10 | Stage fit | 6 | |

**Common failures:** product grid only; SEO text block at the bottom; "We offer a wide range of high-quality…"; no selection criteria.

---

## 4. CaaS / reusable content block (object descriptions, modules)

AI never sees a "block". It sees the passage inside its host page. **A block must stand alone as a passage and must not create duplication or contradiction across pages.** This covers the SE Toolkit's short, medium and long object descriptions (title + subtitle + description + CTA), banners, benefit blocks, spec snippets, FAQ modules, sustainability statements and CTA blocks.

| ID | Criterion | W | Checks |
|---|---|---|---|
| BLK-1 | Self-containment | 22 | Subject named explicitly (no "this product", "our solution"); makes sense when lifted alone |
| BLK-2 | One idea + descriptive heading | 10 | Single message; the title describes it (not a campaign name) |
| BLK-3 | Factual specificity | 18 | Claim has a number, unit, condition or timeframe; outcome–solution–timeframe link ("reduced energy costs by 15% in six months with [named module]") |
| BLK-4 | Consistency with canonical data | 15 | Matches PDP/spec/claim source; dated or versioned |
| BLK-5 | Parameterization / non-duplication | 10 | Not identical boilerplate across many pages; variables (product, rating, region) filled in |
| BLK-6 | Neutral tone | 10 | |
| BLK-7 | Localization correctness | 5 | Units, standards (IEC vs UL) and regional availability caveats correct for the country |
| BLK-8 | Descriptive CTA | 5 | CTA names what the user gets ("Read the Le Grand Monarque Hotel case study"), not "Learn more" |
| BLK-9 | One primary outcome | 5 | Medium/long forms: a single lead outcome, headline and body aligned; long forms use scannable bullets |

**Scoring note:** with < 40 words, quotation and source checks are N/A. Also run a **host-page assembly check**: redundancy across blocks, conflicting claims, answer block placed first.
**Banner/hero test (SE Toolkit):** if an AI reads only the banner, can it explain what, who, when and outcome? If not, BLK-1 ≤ 3 and BLK-9 ≤ 3.

---

## 5. Editorial page — common logic

Use for editorial pages that don't fit a more specific type (articles use §6, solution pages §12, case studies §8). This is the base logic that the editorial family shares.

| ID | Criterion | W |
|---|---|---|
| U1 | Answer-first & prompt alignment | 16 |
| U2 | What / Who / When / Outcome | 8 |
| U3 | Extractable structure & self-containment | 10 |
| U4 | Factual density | 10 |
| U5 | Evidence, attribution & expertise | 12 |
| U6 | Fan-out coverage & focus | 12 |
| U7 | Neutral tone | 8 |
| U8 | Entity clarity & consistency | 6 |
| U9 | Freshness | 8 |
| U10 | Stage fit & next step | 10 |

**Template-goal note (SE UX templates):** a *GEO Power Page* is judged as is. For a *GEO Optimized Template* whose primary goal is conversion, the agent still scores the GEO elements but must not recommend removing conversion elements. It recommends a GEO-ready top block instead.

---

## 6. Article / blog (thought leadership, editorial article)

> **v2.0 (19 Oct 2026):** logic for range, article/blog, case study and solution pages is **superseded by `page-types-v2.md`**, which also adds news, service, software, calculator, white paper and ESG. The section below is kept for history. Use v2 for scoring.


**What AI extracts:** definitions, explanations, how-it-works passages, statistics, expert quotes, step lists. Articles get about 45% of citations for informational queries. ChatGPT is the most article-oriented engine. Blogs answer broad exploratory prompts ("why does X matter", "what's changing in Y").

| ID | Criterion | W | Checks |
|---|---|---|---|
| U1 | Insight/answer in paragraph 1 | 14 | The intro is a summary that could be quoted alone; context follows the insight |
| ART-1 | Key-takeaways block | 6 | 3–5 standalone bullets near the top or bottom that match the article's real claims |
| ART-2 | Title & subheads: descriptive, prompt-aligned, non-clickbait | 6 | Each H2 names one idea, mirrors how people ask ("How Microgrids Reduce Outage Risk", not "A New Era Begins") |
| U3 | Extractable structure | 10 | |
| U4 | Factual density | 8 | Numbers instead of superlatives; hedges cut ("many experts believe") |
| U5 | Evidence & attribution | 12 | Stats with named source + year; ≥ 1 named expert quote; standards named |
| ART-3 | Non-commodity insight | 6 | Original data, first-hand field experience, SE-specific perspective; not a rewrite of what is already online |
| U6 | Fan-out coverage & focus | 10 | One primary intent; ~500–2,000 words typical |
| U7 | Neutral tone | 7 | |
| U8 | Entities & descriptive links | 5 | Products/standards named; companion articles cross-referenced by title |
| U9 | Freshness | 8 | Visible "Published / Updated" dates; stats refreshed at least yearly |
| U10 | Stage fit & next step | 8 | |

**SE blog checklist mapping:** core insight in para 1 → U1 · scene-setting after the point → U1 · one idea per subheading, descriptive → ART-2 · numbers not superlatives → U4 · data attributed → U5 · entities named → U8 · descriptive anchors → U8 · takeaways block → ART-1 · visible update date → U9.

---

## 7. Document (datasheet, whitepaper, catalog, guide, manual, PDF)

**What AI extracts:** specs, ratings, tolerances, procedures, compliance details, methodology, conclusions. Most of SE's technical authority lives in documents. 77–86% of engineers value datasheets most. The principle is **HTML-first, PDF-also**. If the agent receives only the PDF, it scores the document and flags that the HTML gateway is unknown.

| ID | Criterion | W | Checks |
|---|---|---|---|
| DOC-1 | HTML gateway / summary layer | 18 | Indexable landing page (or ungated summary) with title, 100–200-word abstract, key specs/findings as bullets/table, questions the document answers, date/version, download link |
| DOC-2 | Lead with the fact; one topic per heading | 12 | Each section opens with the spec/fact; headings read like the question they answer; multi-topic sections split |
| DOC-3 | Specs in tables | 12 | Parallel attributes in rows/columns; consistent labels and units across the library; one value per cell |
| DOC-4 | Text-extractable, structured file | 8 | Real text layer (not scanned); real heading hierarchy; single-column where possible; tables are real tables (authoring decision) |
| DOC-5 | Descriptive title, filename & metadata | 6 | "SmartUPS-SMX3000-Datasheet-EN.pdf"; document title set; not "Document1" |
| DOC-6 | Customer language | 8 | Model codes paired with plain names ("Smart-UPS SMX3000RMLV2U (3000VA/2700W rack-mount UPS)"); acronyms defined at first use; customer phrasing ("operating temperature range", not "env. spec") |
| DOC-7 | Version, date, changelog, supersession | 10 | Visible "Rev. N, updated Month YYYY"; changelog; superseded versions retired or marked |
| DOC-8 | Methodology / test conditions / references | 8 | Whitepapers: method, references, named authors; datasheets: test conditions and standards for ratings |
| DOC-9 | Gate the deep dive, not the knowledge | 6 | If gated: key findings, definitions and frameworks visible before the gate |
| U8 | Consistency with PDP / spec DB | 7 | |
| U7 | Neutral tone | 5 | |

Sub-types: **datasheet** (move 4 points from DOC-8 to DOC-3) · **whitepaper** (keep DOC-8; add the U5 quote/source checks inside DOC-8) · **catalog** (DOC-1 needs per-range HTML equivalents; a 400-page catalog must not be the only source) · **manual/installation guide** (DOC-2 counts numbered steps; safety warnings required).

---

## 8. Case study / customer story

> **v2.0 (19 Oct 2026):** logic for range, article/blog, case study and solution pages is **superseded by `page-types-v2.md`**, which also adds news, service, software, calculator, white paper and ESG. The section below is kept for history. Use v2 for scoring.


| ID | Criterion | W | Checks |
|---|---|---|---|
| CS-1 | Outcome-led title + 100–150-word summary | 14 | "[Customer type]: [result] with [solution]"; summary covers who, problem, solution, result, timeline |
| CS-2 | Customer profile | 8 | Industry, size, country, application |
| CS-3 | Quantified results with baseline & timeframe | 20 | Before/after metrics; timeframe; one primary outcome leads |
| CS-4 | Challenge → solution → results structure | 8 | |
| CS-5 | Attributed customer quote | 8 | Named person and role |
| CS-6 | Products/solutions named & linked | 8 | Exact product/module names (e.g. "EcoStruxure™ Building Activate Energy Management module") |
| CS-7 | Metric methodology / verifiability | 6 | How savings were measured |
| U2 | Context | 6 | |
| U7 | Neutral tone | 6 | |
| U8 | Entity consistency | 6 | |
| U9 | Freshness | 4 | |
| U10 | Next step | 6 | Descriptive CTA to the solution/range |

---

## 9. Comparison page / selection or buying guide

Technology comparisons ("SF6-free vs SF6 switchgear") and selection guides are more citable than "us vs competitor" pages. Self-published "alternatives" pages are rarely cited. Neutrality is essential.

| ID | Criterion | W | Checks |
|---|---|---|---|
| CMP-1 | Neutral comparison table | 20 | Same attributes and units for every option; sources for competitor/alternative data |
| CMP-2 | Explicit criteria + "choose X if…" verdicts | 16 | |
| CMP-3 | Honest trade-offs | 10 | Limitations of the SE option included |
| U1 | Answer-first verdict | 10 | Bottom line up front |
| U5 | Sources / test data | 10 | |
| U4 | Factual density | 8 | |
| U6 | Fan-out coverage | 8 | Cost, maintenance, compliance, installation differences |
| U7 | Neutral tone | 6 | |
| U9 | Freshness | 6 | Dated; reviewed quarterly |
| U10 | Stage fit & next step | 6 | |

Penalty: self-ranking with own brand #1 and no transparent criteria (−3).
Guides add: numbered steps; worked example with numbers; sizing formula in text; safety notes and standards.

---

## 10. FAQ / support / knowledge-base article

| ID | Criterion | W | Checks |
|---|---|---|---|
| FAQ-1 | Real buyer questions as headings | 12 | Natural-language questions sourced from support, sales or prompts; real heading tags |
| FAQ-2 | Direct answer first | 22 | First sentence answers (< 25 words); total 40–80 words; no "it depends" when a concrete answer exists; does not end in a CTA instead of an answer |
| FAQ-3 | Self-contained, one entity per answer | 12 | Product/range named; no keyword stacking |
| FAQ-4 | Lists/tables for steps, specs, comparisons | 10 | |
| FAQ-5 | Applies-to & identifiers | 10 | Models, references and error codes in text |
| FAQ-6 | One page per topic/product | 6 | Not a global mega-FAQ |
| U4 | Specificity | 10 | Values, intervals ("3–5 years"), test cadence |
| U9 | Freshness | 10 | Reviewed within 90–120 days; updated immediately after product or policy changes |
| FAQ-7 | Links to docs & next step | 8 | |

---

## 11. Glossary / definition page

| ID | Criterion | W |
|---|---|---|
| GLO-1 | Definition in the first sentence ("X is …") | 28 |
| GLO-2 | Formula, units, governing standard | 16 |
| GLO-3 | Example / application | 14 |
| GLO-4 | Disambiguation & related terms (e.g. kVA vs kW) | 14 |
| U5 | Sources | 8 |
| GLO-5 | Links to products/guides | 8 |
| U7 | Neutral tone | 6 |
| U9 | Freshness | 6 |

---

## 12. Solution / industry landing page (e.g. data center power, microgrids, F&B)

> **v2.0 (19 Oct 2026):** logic for range, article/blog, case study and solution pages is **superseded by `page-types-v2.md`**, which also adds news, service, software, calculator, white paper and ESG. The section below is kept for history. Use v2 for scoring.


| ID | Criterion | W | Checks |
|---|---|---|---|
| SOL-1 | Problem quantified | 12 | Pain point with data (cost of downtime, energy share, regulation deadline) |
| U1 | Answer-first definition of the solution | 8 | |
| U2 | What / Who / When / Outcome | 6 | |
| SOL-2 | Architecture explained in text | 14 | Components and how they fit, in words (not diagram-only) |
| SOL-3 | Components named & linked | 8 | |
| SOL-4 | Outcomes quantified | 12 | |
| SOL-5 | Proof | 12 | Case studies, references, third-party validation |
| U5 | Standards / sources | 6 | |
| SOL-6 | FAQ | 6 | |
| U7 | Neutral tone | 6 | |
| U10 | Stage fit & CTA | 6 | |
| U9 | Freshness | 4 | |

---

## 13. Video asset (YouTube + embed): from SE Toolkit Ch. 5 / Ch. 10

| ID | Criterion | W | Checks |
|---|---|---|---|
| VID-1 | AI-friendly video type | 12 | Tutorial, how-to, FAQ, comparison, case study, expert insight (brand films score low) |
| VID-2 | Descriptive, intent-framed title | 12 | Factual; question or "how to" form; product + brand named |
| VID-3 | Description | 16 | 2-paragraph summary incl. the questions answered; bullets; 300+ words; link to the SE page |
| VID-4 | Answer early | 12 | Problem + short answer in the first 30–90 s (check the transcript) |
| VID-5 | Transcript / captions | 14 | Human-reviewed .SRT; product names and acronyms correct; voice-over present |
| VID-6 | Chapters | 10 | Question-style titles; start at 00:00; ≥ 3 timestamps |
| VID-7 | Published on an SE page with text context | 12 | Embedded on a crawlable SE page with title + 3–4-bullet summary (+ transcript if possible) |
| VID-8 | Fact-based, consistent terminology, recap | 12 | |

---

## 14. Image / visual module (applies inside any page; scored within U3, PDP-9 or BLK)

- Informative images have alt text of 80–140 characters that describes purpose in context, without stuffing, and unique per variant.
- An explanatory paragraph sits next to or below the image, plus a caption (second independent text signal).
- Descriptive filename consistent with the alt text.
- Diagrams/infographics have their own alt text and are explained in text. Data shown in a chart is also given as a table or text.
- Failures: empty alt on informative images; identical alt across colour variants; keyword-dump alt text.

---

## 15. Classifying an unknown page

1. Has a SKU/reference + spec table → PDP.
2. Lists several variants of one named family → Range.
3. Lists several families/types under a generic noun → Category.
4. A module under ~150 words reused across pages → CaaS block.
5. A downloadable file or its gateway → Document.
6. Named customer + results → Case study.
7. Two or more options side by side, or "how to choose" → Comparison / selection guide.
8. Q&A pairs as the main content → FAQ / support.
9. Defines one term → Glossary.
10. Industry/segment problem + an architecture of offers → Solution page.
11. Dated narrative/opinion/explainer → Article/blog.
12. Otherwise → Editorial (common logic).

If the declared page type conflicts with the content, score with the declared logic, then flag the mismatch and give the score under the better-fitting type.

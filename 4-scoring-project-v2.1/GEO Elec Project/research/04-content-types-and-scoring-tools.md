# 04 – Content-Type GEO Best Practices & Existing Scoring Tools/Rubrics

*Research slice for the Content GEO Score Agent. Compiled 2026-10-13. Scope: content-level signals only; technical SEO (robots.txt, rendering, speed, crawl) is excluded except where a content decision (e.g. "key facts only in a PDF or image") directly determines extractability.*

**Evidence grading used in this report**
- **[P] Primary / peer-reviewed / official platform documentation** (arXiv/ACL/NeurIPS papers, Google/Microsoft/OpenAI docs).
- **[S] Large-sample vendor study** (Semrush, Ahrefs, Wix, Peec, Surfer, Growth Memo/AirOps). These are correlational and the vendors have commercial interests, but they are the best large-N data available.
- **[V] Vendor/agency practitioner guidance.** Plausible and widely repeated, but not tested.

Agent weights should rely mostly on [P] and [S]. [V] items work better as checks than as heavily weighted criteria.

---

## 1. Executive summary

1. **AI engines cite passages, not pages.** Microsoft's Bing/Ads guidance [P] says assistants "parse" pages into pieces, judge each piece for authority and relevance, and assemble answers from several sources. Google [P] says AI Overviews and AI Mode use *query fan-out*: they issue many related sub-queries and pull supporting pages for each one. The scoring agent's basic unit should therefore be the self-contained, extractable passage: a heading framed as a question or topic, an answer-first sentence, and supporting facts.
2. **A small set of content properties is consistently linked to citation**, across a peer-reviewed experiment and large observational studies:
   - Adding **quotations, statistics and cited sources** gives roughly +28–43% visibility in the GEO paper (Aggarwal et al., KDD 2024) [P]. **Keyword stuffing hurts** (−9%).
   - **Clarity and summarization** (+33%), **E-E-A-T signals** (+31%), **Q&A format** (+25%), **section structure** (+23%) and **structured elements** (+22%). Source: Semrush, 304k cited URLs [S].
   - **Answer position:** 44% of ChatGPT citations come from the first 30% of the page (the "ski ramp" pattern). Definitive language, entity density and direct definitions also help. Source: Growth Memo/AirOps [S].
   - **Facts coverage and upfront intent alignment**, measured by Surfer's AI Search Score [S]. Cited pages had a fact-coverage ratio of 0.31 vs 0.24 for non-cited pages.
   - **Focused pages beat "ultimate guides."** Pages that covered 26–50% of fan-out sub-queries were cited more than pages covering 100% [S].
3. **Caveat that keeps the scores honest.** C-SEO Bench (NeurIPS 2025) [P] found that most white-hat "conversational SEO" rewrites give close to zero gain once retrieval rank is controlled. Retrieval rank was the dominant factor. Off-site brand mentions also correlate with AI visibility (0.66) much more than backlinks (0.22) [S]. **A content score measures citation-readiness, not guaranteed citation.** The agent should say so, and should not promise lift.
4. **Page type and intent decide which format gets cited** (Wix, 1.06M citations) [S]:
   - Informational queries: articles take 45% of citations.
   - Commercial/comparative queries: listicles take 41%, and third-party lists far outperform self-promotional ones.
   - Transactional queries: product pages take 25%, category pages 15%.
   - Navigational queries: product pages take 22%, category pages 18%.
   - Google AI Mode leans toward official brand category and product pages. Perplexity over-indexes on discussions/UGC. ChatGPT leans toward articles and listicles (Peec) [S].
   - The scoring rubric must therefore be **page-type × journey-stage specific**, not a single universal checklist.
5. **For PDPs, AI shopping surfaces read structured product data and on-page facts together:**
   - Google's Shopping Graph via Merchant Center, including the new 2026 "conversational attributes": Q&A, document links, parts & accessories, variant axes [V/P-secondary].
   - The OpenAI product feed spec: factual plain-text description, category path, material, dimensions, weight, GTIN/MPN, reviews [P].
   - Perplexity's merchant program and Amazon Rufus [V].
   - Content implications: attribute completeness; spec facts with units in HTML; use-case/application language ("42 dB dishwasher for open-plan kitchens", not "quiet"); compatibility; standards/certifications; Q&A; and **consistency between visible copy, specs, structured data and feeds**.
6. **B2B industrial buyers depend heavily on AI but trust it little.**
   - 69% of technical buyers use GenAI somewhere in purchasing, but only ~6% find AI summaries "enough" (2026 State of Marketing to Engineers) [S].
   - Datasheets remain the most valuable content for engineers (77–86%) [S].
   - Implication: datasheets and specs must exist as text-extractable HTML with a summary layer. Every claim should be verifiable through standards, test conditions and units.
7. **Existing tools fall into two families:**
   - **Brand-visibility monitors** that measure outcomes: HubSpot AEO Grader, Semrush AI Visibility, Profound, Peec, Otterly, Scrunch, AthenaHQ.
   - **Page-content scorers** that measure inputs: Frase GEO Score, Surfer AI Search Score, Writesonic GEO Content Score, Semrush Content Toolkit, Conductor AI Content Score, MarketMuse, Clearscope.
   - None publishes weights for page-level GEO scoring, and none is page-type or buyer-journey aware. **That gap is the differentiation opportunity for this agent.**
8. **LLM-as-judge design.** Use decomposed, per-criterion scoring with **binary or checklist sub-items rolled up into anchored 0–4 levels**. Require **verbatim evidence quotes** (checked in code), reasoning before score, and deterministic weighting in code rather than by the LLM. Calibrate against a human-labelled gold set (Cohen's κ), lock the prompt, and do not pass prior scores into re-scoring. Supporting work: CheckEval (+0.45 inter-model agreement), RULERS (evidence-anchored scoring), Prometheus (rubric + reference answer, r=0.90 with humans), and Zheng et al. (position/verbosity/self-preference biases).

---

## 2. Per-page-type GEO playbook

### 2.0 Cross-cutting principles (apply to every page type)

| Principle | What to check | Evidence |
|---|---|---|
| Answer-first / BLUF | First 1–2 sentences under H1 and under each H2 answer the implied question directly. Key definitions and conclusions sit in the top 30% of the page. | Growth Memo/AirOps ski-ramp [S]; Surfer "upfront intent alignment" [S]; Microsoft [P] |
| Self-contained passages | Each section makes sense when lifted alone: no "as mentioned above", and pronouns resolve to named entities. | Microsoft [P]; iPullRank [V] |
| Descriptive, question-shaped headings | H2/H3s name the topic or question ("What makes this breaker suitable for DC PV strings?"), not "Learn more" or "Overview". | Microsoft [P]; Semrush section structure +23% [S] |
| Specific, measurable claims | Numbers with units, conditions and standards. No unanchored superlatives ("next-gen", "cutting-edge"). | Microsoft [P]; GEO paper statistics +33% [P] |
| Cite sources / attribution | Claims link to standards bodies, test reports, third-party research. Quotations are attributed to named experts. | GEO paper cite sources +28%, quotations +43% [P] |
| Non-promotional, factual tone | Descriptive and comparative language rather than hype. Semrush's correlation pointed the other way, so measure tone, but weight it modestly. | GEO paper (authoritative/fluency help) [P]; Semrush [S] (ambiguous) |
| Entity density & terminology | Product names, standards (IEC 60947-2, UL 489), technical terms, synonyms ("rated current / In / nominal current"). | GEO paper technical terms +18% [P]; Growth Memo entity density [S]; Microsoft synonyms [P] |
| Structured elements | Tables, lists, Q&A blocks, key-takeaways boxes, rendered as HTML text and not images. | Semrush [S]; Frase, Writesonic [V]; Microsoft [P] |
| No key info locked away | Critical facts not only in images, PDFs, collapsed tabs or carousels. | Microsoft [P] (content consequence, not a crawl check) |
| E-E-A-T / Who-How-Why | Named author or reviewer with role, date, sourcing, evidence of first-hand experience such as testing or field data. | Google helpful-content questions [P]; Semrush E-E-A-T +31% [S]; Writesonic authority signal [V] |
| Freshness | Visible "last updated" date, current standards versions, current product status. | Ahrefs: cited URLs ~26% fresher than organic [S] (weak and correlational) |
| Focus over exhaustiveness | One primary intent per page, covering 2–3 related angles well. Not a 10,000-word catch-all. | AirOps/Growth Memo 815k pairs [S] |
| Consistency | Same facts across page copy, spec table, structured data, feed and datasheet. | OpenAI feed spec and Google "structured data must match visible content" [P] |
| Domain fit | Adjust emphasis by domain. In the GEO paper, statistics worked best for Law/Gov/Debate, citations for Facts/Statements, authoritative tone for Science, fluency for Business/Health. | GEO paper Table 3 [P] |

---

### 2.1 Product Detail Page (PDP)

**What AI engines extract or cite.**
- Product identity: name, reference/SKU, brand, GTIN/MPN.
- Key specifications with units.
- Primary use case and applications.
- Compatibility and accessories.
- Certifications and standards.
- Price and availability (B2C).
- Ratings and review themes.
- Answers to specific questions ("Is X compatible with Y?", "What is the breaking capacity of…?").

PDPs are cited mainly for **transactional (25%) and navigational (22%)** intents and rarely for informational ones (3%) (Wix [S]). Google AI Mode cites official brand product and category pages more than other engines do (Peec [S]). The Peec study also notes that later ChatGPT models shifted retrieval toward product pages. In AI shopping (Google Shopping Graph, ChatGPT shopping, Perplexity, Rufus), the PDP is often *consumed as data* to ground the answer rather than shown as a citation link. Completeness and consistency therefore matter more than prose style.

**Citable elements / must-haves**
1. **Answer-shaped summary (40–80 words)** at the top. It states what the product is, who it is for, its primary application, and 2–3 differentiating specs with units. Example: "A 4-pole 63 A residual-current circuit breaker, Type B, for EV charging and PV installations where DC fault currents can occur; complies with IEC 62423."
2. **HTML specification table.** Attribute name, value and unit in text. Grouped by category (electrical, mechanical, environmental, communication). Standardized attribute names and no blank or "N/A" filler.
3. **Attribute completeness** against the category's attribute schema. Vendors suggest ≥95% fill on top SKUs [V]. Feed fields to mirror: description (plain, factual, ≤5,000 characters), product category path, material, dimensions (product, not package), weight, GTIN/MPN (OpenAI spec [P]).
4. **Applications / use cases**, written as Feature + Benefit + Context noun phrases ("for retrofit in residential consumer units", "for harsh industrial environments IP66"). This follows the Rufus/COSMO noun-phrase logic [V] and Microsoft's "42 dB dishwasher for open-concept kitchens" example [P].
5. **Compatibility & ecosystem.** Compatible accessories, replacement and successor parts, required complementary products, software/firmware compatibility, communication protocols. This mirrors Google Merchant Center's "parts & accessories" conversational attribute [V].
6. **Standards, certifications, approvals.** Listed with standard number and edition (IEC/UL/CE/UKCA/RoHS/REACH, EPD/PEP environmental declarations, cybersecurity certifications such as IEC 62443).
7. **On-page Q&A/FAQ (3–8 real questions)** taken from sales/support logs, reviews and AI prompt research. Answers are 1–3 sentences, self-contained, and include the product name. This mirrors the Merchant Center Q&A conversational attribute [V] and Semrush's Q&A +25% [S].
8. **Selection/differentiation context.** How this variant differs from siblings in the range ("choose this if…"). Link to range page and comparison.
9. **Documents linked with descriptive anchors**: datasheet, installation guide, CAD/BIM, EPD, declarations of conformity. Key facts from them are also summarized in HTML. Mirrors the Merchant Center document-link attribute [V].
10. **Reviews/ratings or proof** (B2C) with substantive reviews. Short, empty reviews add almost nothing [V]. For B2B: references, installed-base claims with numbers, case-study links.
11. **Commercial facts** where relevant (B2C/distributor): price, availability, where to buy, warranty, return policy.
12. **Lifecycle status:** active, end-of-life, or replaced by a named successor. This prevents AI from recommending discontinued parts.

**Common failures**
- Marketing-only description ("innovative, reliable, smart") with no numbers.
- Specs only in a PDF datasheet or an image.
- Specs inside collapsed tabs.
- Inconsistent units or attribute names across sibling SKUs.
- Missing use cases.
- No compatibility info.
- Duplicate boilerplate copy across hundreds of SKUs.
- Contradictions between page and feed or schema.
- Discontinued status not stated.

**Example checks (agent)**
- Does the first paragraph name the product type, primary application and ≥2 quantified specs?
- What % of category-required attributes are present with units?
- Are ≥3 applications stated as noun phrases?
- Is there a compatibility section?
- Are ≥1 relevant standards cited by number?
- Are there ≥3 Q&As matching likely prompts?
- Do spec values in prose match the table?
- Is there any unanchored superlative?

---

### 2.2 Product Range page (a product family/series)

**What gets extracted:** range positioning (what the family is and who it is for), the member variants and how they differ, selection axes (rating, poles, curve, communication), the range's ecosystem, and its standards. Ranges answer prompts like "What is the [range] series?" and "Which [range] model should I choose for…?".

**Must-haves**
1. Definition-style opening: "[Range] is a family of … for …". Include the scope (current ratings, voltages, number of variants).
2. **Variant comparison table** (HTML): rows = variants, columns = decision attributes, plus "best for" per row.
3. **Selection guidance**: a decision path ("If you need X and Y, choose Z") in text, not only an interactive configurator.
4. Applications/segments served, with examples or references.
5. Range-level differentiators, quantified (e.g. "up to 30% smaller footprint than previous generation, measured as …").
6. Standards/certifications common to the range.
7. Ecosystem: accessories, software, compatible ranges.
8. FAQ covering selection, compatibility and migration from legacy ranges.
9. Links to every member PDP and to documents.

**Common failures:** carousel or hero-banner pages with no text, configurator-only selection, no table, no "best for" framing, legacy range names missing (so migration prompts are not answered).

---

### 2.3 Product Category page (e.g. "Circuit breakers", "EV chargers", "PLCs")

**What gets extracted:** category definitions, types and sub-types, selection criteria, top options, and short lists. Category pages take 12% of commercial, 15% of transactional and 18% of navigational citations (Wix [S]). Google AI Mode favours them most (Peec [S]). In ecommerce, buying guides and comparisons earn most citations and category pages earn a "modest, steady" rate [S/V]. **The category page should therefore carry a compact guide layer.**

**Must-haves**
1. 50–100 word answer-first intro: what the category is and the main types.
2. **"How to choose" block**: 4–8 selection criteria with explanations and units/thresholds (e.g. breaking capacity, trip curve, pole count, ambient temperature).
3. **Type/sub-category comparison table** with "best for" framing (residential vs commercial vs industrial; AC vs DC).
4. Featured ranges with one-line "best for" positioning. Keep it factual, not self-congratulatory, because third-party lists are cited about 4× more than self-promotional ones [S].
5. Relevant standards and regulations for the category.
6. FAQ (definitions, differences between types, sizing).
7. Links to deep guides, glossary terms and calculators.
8. Freshness: new standards and new product generations reflected.

**Common failures:** product grid only, SEO text block at the bottom with keyword stuffing, generic "We offer a wide range of high-quality…" copy, no selection criteria.

---

### 2.4 CaaS / reusable content blocks (content-as-a-service modules)

These are reusable modules (benefit blocks, spec snippets, FAQ modules, standards blurbs, brand claims, sustainability statements, CTA blocks) injected into many pages. AI engines never see a "block". They see the passage in its host page. **The block must stand alone as a passage and must not create duplication or contradiction across pages.**

**Must-haves / checks**
1. **Self-containment:** names its subject explicitly, with no dependence on surrounding context ("this product" → named product or variable).
2. **One idea per block,** with a descriptive heading included in the block.
3. **Factual atomicity:** each claim has a number, unit, condition and source (claim registry ID).
4. **Parameterization:** product name, ratings and region inserted dynamically, so the same block does not produce identical text on 500 pages (avoids near-duplicate dilution).
5. **Single source of truth:** a block's claims match the canonical spec or claim database. Version and date stamped.
6. **Localization-ready:** units, standards (IEC vs UL) and regulatory references vary by country.
7. **Rendered as HTML text,** not an image or a script-only widget.
8. **Format type tagged** (definition, Q&A, stat, quote, how-to step, comparison row) so the agent can score each block against the criteria for its format.

**Common failures:** generic brand boilerplate ("A global leader in…") repeated everywhere; claims without a date or source; blocks that contradict PDP specs; FAQ modules reused verbatim on unrelated pages.

**Scoring note:** score blocks on a reduced criterion set (self-containment, specificity, attribution, consistency, tone). Then score the host page for how blocks are assembled (redundancy, conflicts).

---

### 2.5 Editorial pages – common logic (applies to articles, guides, solution pages, case studies, glossary)

Shared criteria:
- Clear primary question or intent.
- Answer-first lead and summary/TL;DR (Frase, Writesonic and Semrush all reward key-takeaways/summary blocks).
- Question-shaped H2s that match likely fan-out sub-queries (focused, 2–3 angles).
- Self-contained sections.
- Statistics with sources, expert quotations, original data.
- Named author/reviewer with credentials, published/updated dates.
- Non-promotional tone.
- Internal links to products/ranges as the "next step".
- Google's helpful-content questions as a quality floor: originality, value beyond the obvious, accurate title, author info, first-hand experience.

### 2.6 Article / blog pages

**What gets extracted:** definitions, explanations, how-it-works passages, statistics, expert quotes, step lists. Articles take **45% of informational citations** (Wix [S]). ChatGPT is the most article-focused engine.

**Must-haves**
1. Title/H1 aligned to the primary prompt. Title-to-query semantic alignment distinguished "core" AI Overview sources (Surfer [S]). The H1 should match the title (Microsoft [P]).
2. 40–60 word direct answer or definition in the first paragraph.
3. Key-takeaways box (3–5 bullets).
4. H2s phrased as the questions buyers ask next (fan-out), each opening with a 1–2 sentence answer.
5. ≥1 statistic per major section with source and year. ≥1 named expert quote. Original data (surveys, test results, field data) where possible. Original research is reported as cited far more than standard posts [S, unverified].
6. Tables/lists for comparisons and steps.
7. Author byline + bio + reviewer for technical/safety (YMYL-adjacent: electrical safety) topics. Dates.
8. FAQ at end for residual questions.
9. Focused scope: 1 primary intent, not an "ultimate guide" to everything.

**Common failures:** long story-led intros, clickbait titles, no numbers, unsourced stats, generic AI-written content without first-hand experience, multiple intents blended, conclusions only at the bottom.

### 2.7 Documents (datasheets, whitepapers, catalogs, guides, PDFs)

**What gets extracted:** specs, figures, methodology, conclusions. HTML gives better structural signals than PDF, and Microsoft explicitly says to avoid relying on PDFs for core information [P]. Gated PDFs are invisible to AI engines. Engineers value datasheets most (77–86%) [S], and ~57% of engineer information searches end on the manufacturer's site [S, 2020].

**Must-haves**
1. **HTML gateway/landing page for each document**: title, 100–200 word abstract, key findings or key specs as bullets/tables, the questions the document answers, methodology (whitepapers), date/version, author/owner, download link. If the document is gated, gate only the full PDF. The summary stays public.
2. **Text-extractable PDF**: real text, not scanned. Tagged headings and logical hierarchy. Document title metadata. Language set. Tables as real tables.
3. Descriptive file name and title ("Type B RCCB selection guide – IEC 62423 – 2026 edition"), not "DOC12345_v3.pdf".
4. Version/edition and validity date. Superseded documents point to the current one.
5. For datasheets: same attribute names and units as the PDP (consistency check). Key specs mirrored on the PDP.
6. For catalogs: per-range HTML equivalents. Don't make a 400-page catalog the only source.
7. For whitepapers: executive summary, key statistics with methodology, references, named authors.

**Common failures:** PDF-only knowledge; scanned images; generic titles; no landing page; gated summaries; outdated editions still live without notice.

### 2.8 Other page types likely in scope

| Page type | What AI extracts | Key citable elements | Typical stage/intent |
|---|---|---|---|
| **Solution / industry landing page** (e.g. "Data center power", "Microgrids") | Problem framing, approach, architecture components, outcomes | Problem statement with quantified pain; solution architecture explained in text (not just a diagram); components listed with links; outcomes with numbers; references/case studies; standards; FAQ | Education–Consideration; informational/commercial |
| **Case study / customer story** | Named outcome, metric, timeframe, context | Title "[Customer type]: [result] with [solution]"; 100–150 word summary (who, problem, solution, result, timeline); customer profile (industry, size, country); challenge/solution/results sections; before/after metrics with timeframe; attributed customer quote; products used, linked; methodology for metrics | Evaluation–Decision; commercial |
| **Comparison page** (product A vs B, range vs range, technology vs technology) | Differences, "best for" verdicts | Neutral comparison table with same attributes and units; criteria explained; "choose A if… / B if…"; honest trade-offs; date. Note: self-published "alternatives/comparison" pages are cited less than 3% of the time [S], while neutral listicles do better. Technology comparisons (e.g. "Air-insulated vs SF6-free switchgear") are more citable than "us vs competitor" pages. | Consideration–Evaluation; comparative |
| **Selection / how-to / buying guide** | Steps, criteria, decision trees, calculations | Numbered steps; criteria with thresholds; worked example with numbers; sizing formulas in text; links to products; safety warnings and standards | Consideration–Evaluation; informational/commercial |
| **FAQ / support / knowledge-base article** | Exact Q→A | One question per page or anchored Q&A; answer in the first sentence; error codes and model numbers as text; steps; applies-to product list; date | Decision–post-purchase; informational/navigational |
| **Glossary / definition page** | Definitions | "X is …" sentence in the first line; formula/units; standard reference; example; related terms; disambiguation (e.g. "kVA vs kW") | Awareness–Education; informational |
| **Calculator/tool pages** | Methodology and results logic | Explain the formula and assumptions in text; example results; limits of validity | Evaluation; informational/transactional |
| **Sustainability / EPD / compliance pages** | Verifiable claims | Quantified claims with methodology (LCA standard, scope), third-party verification, dates | Evaluation–Decision |

### 2.9 Ecommerce / AI shopping specifics (B2C and distributor channels)

- **Google AI Mode / Shopping Graph:** grounded by Merchant Center feeds; on-page Product markup is a secondary/verification signal [V]. In May 2026 Google added optional "conversational attributes" [V]: Q&A pairs, document links (manuals, spec sheets), parts & accessories relationships, item-group title, variant axes, popularity rank. *Content implication:* PDP copy should contain the same Q&A, document links and accessory relationships, so feed and page reinforce each other.
- **ChatGPT shopping (OpenAI product feed spec) [P]:** required fields are item_id, title, description (factual plain text), url, brand, seller, image, availability, price. Optional: GTIN/MPN, product_category path, material, dimensions, weight, condition, reviews (count/rating), returns. Raw Q&A and reviews are *not* part of the feed contract, so they must be on the page to be used.
- **Perplexity shopping [V]:** merchant program plus open-web retrieval. Rankings are reportedly driven by relevance, data completeness and merchant signals. Recommendations are not paid.
- **Amazon Rufus/COSMO [V]:** intent/noun-phrase optimization ("high-speed blender for green smoothies"); complete backend attributes (intended use, target audience); bullets that answer shopper questions; fix complaints that recur in reviews.
- **Consistency across page, feed and schema** is repeatedly cited as a confidence factor [V/P].

### 2.10 B2B industrial buying specifics (engineers, specifiers, distributors, contractors)

- Buyers ask AI detailed technical-constraint questions (ratings, tolerances, certifications, compatibility, lead time) and use AI to shortlist and verify suppliers [V].
- **AI use is high but trust is low.** 69% of technical buyers use GenAI and only ~6% find AI summaries sufficient (2026 SMTE [S]). 20% of B2B buyers report reduced confidence from inaccurate AI info (Forrester via secondary [S]). Implication: content must be *verifiable*, with standards numbers, test conditions, downloadable proof, and named engineers or reviewers.
- **Preferred content:** datasheets (77–86%), technical articles (60%), reviews/testimonials (50%), CAD drawings (45%), demo videos (42%) [S].
- **Personas differ by stage:**
  - Specifiers/consultants: standards, compliance, BIM/CAD, specification text.
  - Design engineers: specs, selection, compatibility.
  - Procurement/distributors: availability, references, lifecycle, substitutes.
  - Facility/plant managers: TCO, uptime, case studies.
  - Contractors/installers: installation, wiring, troubleshooting.
- **Distributor amplification:** distributors' PDPs often outrank or out-cite manufacturers. Manufacturer content should be the canonical, most complete source and should be syndicated consistently.

---

## 3. Buyer-journey stage × intent mapping

| Stage | Typical AI prompts (examples) | Dominant intent | Content types most cited | Content signals that matter most | Primary page types to score |
|---|---|---|---|---|---|
| **Awareness** | "Why does my facility have power quality issues?", "What is a microgrid?" | Informational (problem/definition) | Articles (45% of informational), glossary, explainers, third-party media | Definitions in the first sentence; plain-language explanation; statistics on problem size; neutral tone; entity clarity; authority (author, sources) | Article, glossary, solution page (problem framing) |
| **Education** | "How does a Type B RCD work?", "What standards apply to EV charging installations?" | Informational (how/why) | Articles, guides, whitepapers, standards explainers | Fan-out H2s; step/mechanism explanations; diagrams explained in text; standards cited by number; expert quotes; original data | Article, document gateway, guide, glossary |
| **Consideration** | "Best types of energy meters for commercial buildings", "AC vs DC coupled PV storage" | Commercial / comparative | Listicles (41% of commercial), category pages (12%), discussions/UGC, comparisons | Selection criteria; comparison tables; "best for" framing; balanced pros/cons; third-party validation; coverage of options including non-brand | Category page, range page, selection guide, comparison page |
| **Evaluation** | "Compare [range A] vs [range B] breaking capacity", "Is [product] compatible with [protocol]?", "Which UPS for a 200 kW data hall?" | Comparative / transactional-research | Product pages, category pages, case studies, datasheets, reviews | Attribute completeness; spec tables; compatibility; certifications; case studies with metrics; TCO/ROI data; documents accessible | PDP, range page, case study, datasheet, comparison, calculator |
| **Decision** | "Where to buy [ref]?", "[ref] price/lead time", "[ref] installation manual", "replacement for [legacy ref]" | Transactional / navigational | Product pages (25% transactional, 22% navigational), category pages, homepage, support pages | Exact identifiers (ref, GTIN); availability/where-to-buy; warranty/support; lifecycle/substitutes; installation docs; clear CTA; reviews | PDP, support/FAQ, document, distributor locator |
| *(Post-purchase / retention)* | "[ref] error code E05", "how to commission…" | Informational / navigational | Support KB, manuals, community | Error codes in text; step lists; applies-to lists; dates | Support/FAQ, documents |

**How to use this in the agent**
- **Stage modifies weights.** Awareness/Education raise Answer-first, Definitions, Authority & sourcing, and Original data. Consideration/Evaluation raise Comparison & selection, Spec completeness, Proof. Decision raises Identifiers, Commercial facts, Lifecycle and CTA clarity.
- **Stage-fit check.** Flag a mismatch, e.g. a page tagged "Awareness" that is mainly a product pitch, or a PDP tagged "Decision" with no availability or where-to-buy.
- **Intent-format fit.** For commercial prompts, AI prefers list/comparison formats. For informational prompts, articles. For transactional prompts, PDPs/category pages. The agent should advise on *format* as well as *content*.
- **Promotional penalty by stage.** Self-promotion is most damaging at Awareness/Consideration, where third-party/neutral sources dominate. It is more acceptable at Decision.

---

## 4. Existing scoring tools & rubrics – comparison

### 4.1 Page-content scorers (input-side; closest to what we're building)

| Tool | Scope | Dimensions scored | Weights / scale / thresholds | How scores become recommendations | Notes |
|---|---|---|---|---|---|
| **Frase GEO Score** | Page/URL, editor | Free checker lists 5: **Citability** (quotable statements/data), **Content Structure** (headings, lists, tables), **Clear Definitions**, **Key Takeaways**, **Data & Citations**. Editor version: backing up claims, readability, structure for extraction. Combined SEO+GEO score. | 0–100; >80 strong, 60–79 solid, <60 headroom. Weights not published. | Per-area suggestions (where to add references, simplify dense passages, restructure); edit and refresh. | Closest public analogue to a content GEO score |
| **Surfer Content Score (AI Search Score)** | Page, editor | **Facts Coverage** (facts/entities/concepts commonly in AI answers for the topic) + **Upfront Intent Alignment** (answers primary question early; what, who for, why). SEO Score separate (terms, coverage, structure). | 0–100; <33 not optimized, 33–66 reasonable, >66 ready; target 70+ or 10–20 above competitors. Weights not published. | Missing facts/terms list, intent guidance. | Backed by a citation study: fact coverage 0.31 vs 0.24 |
| **Writesonic GEO Content Score** | Page | **Schema markup** (Article/FAQ/Product/HowTo), **Key takeaways** (TL;DR), **Authority signal** (named author with role/credentials) + other categories | 0–100; issue counts per signal; weights not published. | Issues grouped by category with explanation and fix; one-click "Optimize" applies fixes; dismissible issues recalc score. | Good UX pattern: issue → explanation → fix |
| **Semrush Content Toolkit / AI Search Optimizer** (+ AI Readiness Audit 25+ on-page factors) | Page | Derived from a 13-parameter study. Positive: **clarity & summarization (+33%)**, **E-E-A-T (+31%)**, **Q&A format (+25%)**, **section structure (+23%)**, **structured data elements (+22%)**. Non-promotional tone came out negative (−26%), probably confounded. | Not published | Add top summary; strengthen author/sources; Q&A; headings/lists/tables. | Only text visible on the page was evaluated: a purely content-level study, useful for our scope |
| **Conductor AI Content Score** | Page | Writing-style consistency, creativity/originality, grammar, structure/readability, clarity/coherence, topical authority & relevance | Weights not published; "no universal good score"; topical depth weighted above grammar | Writing Assistant suggestions | LLMs convert qualitative factors into scores |
| **MarketMuse Content Score** | Page vs topic model | Topical coverage: 1 point per topic mention, max 2 per topic, across 50 topics → 0–100 | Target Content Score derived from competitors; "no perfect score" | Missing topics list | Coverage-only; transparent formula |
| **Clearscope Content Grade** | Page vs SERP | Relevant term inclusion; term importance 1–10 from top-ranking pages | Letter grades (A++…); A+ typical for top pages | Term checklist with ranges | SEO-oriented; weak for GEO |
| **Yoast / Rank Math** | WordPress | Readability/SEO; llms.txt generation; AI traffic tracking (Rank Math); schema aggregation (Yoast) | n/a | n/a | Not GEO content scorers |
| **Otterly GEO Audit 2.0** | Page/site | 25+ factors: crawler access, JS readability, page speed, "AI readiness" | Prioritized fix-lists | Mostly technical (out of scope) | |
| **Scrunch page audit / AXP** | Page | Citation blockers, AI-crawler view | — | Fixes | Mostly technical |
| **AthenaHQ / Profound / Goodie** | Brand + content | Content gaps from prompt tracking; content agents (Profound 50+ templates: listicles, how-tos, comparisons); Goodie: structure/keywords/schema recommendations | — | Gap-driven briefs | Recommendations are prompt-gap-driven, not page rubrics |

### 4.2 Brand-visibility monitors (output-side; useful for validating our score)

| Tool | Measures | Method | Weights |
|---|---|---|---|
| **HubSpot AEO Grader** | Brand score /100 | Structured prompts to GPT, Perplexity, Gemini; cross-validated; deterministic scoring with schema validation | **Sentiment 40** (overall, by topic, source credibility), **Presence quality 20** (incl. mention depth 0–10), **Brand recognition 20**, **Share of voice 10** (% voice + rank bonus), **Market competition 10** (Leader/Challenger/Niche; Innovator/Disruptor/Traditionalist) |
| **Semrush AI Visibility Toolkit** | AI Visibility 0–100 vs competitors; mentions; SoV; cited domains; prompt-level gaps | Prompt sampling across ChatGPT, AI Mode, AIO, Gemini, Perplexity | Not published |
| **Profound, Peec, Otterly, AthenaHQ, Scrunch, BrightEdge (AI Catalyst), Conductor** | Citation rate, mention rate, SoV, sentiment, cited URLs, AI bot traffic | Prompt panels; crawler logs | Not published |

**Use for our agent:** run the target AI prompts through a monitor (or our own panel) before and after edits, and check that changes in content score track changes in citation rate. That is the only real validation of a content score.

### 4.3 Official/quasi-official rubrics

| Source | What it offers the agent |
|---|---|
| **Google helpful-content self-assessment** [P] | Content & quality (original info, comprehensive, insightful beyond obvious, adds value vs sources, accurate non-exaggerated title, bookmark-worthy, magazine-quality, better than competitors, no spelling/style issues, not mass-produced); Expertise (clear sourcing, author info, written/reviewed by expert, no factual errors); People-first (intended audience, first-hand experience, satisfies goal); **Who/How/Why** (bylines, how produced incl. AI use, why created). Usable directly as binary checks. |
| **Google Search Quality Rater Guidelines (Sept 2025 ed.)** [P] | Page Quality scale Lowest → Low → Medium → High → Highest. Judged on purpose, main content quality and amount, website/creator reputation, E-E-A-T (Trust is central). YMYL raises the bar. Electrical safety and energy content is arguably YMYL-adjacent. Our 0–4 anchors can borrow the "Lowest/Low/Medium/High/Highest" language. |
| **Google AI features guidance** [P] | No special AI optimization or schema required. Keep important content in text. Structured data must match visible text. Keep Merchant Center current. Fan-out explained. |
| **Microsoft Bing/Ads "Optimizing content for inclusion in AI search answers" (Oct 2025)** [P] | The most concrete official content checklist: aligned title/description/H1; descriptive H2/H3; Q&A blocks; lists/tables; avoid walls of text, hidden tabs, PDF-only and image-only info; precise claims with context; synonyms; avoid decorative symbols and unanchored claims; 1–2 sentence direct answers; self-contained sentences. |
| **GEO paper (Aggarwal et al., KDD 2024)** [P] | Measured effects of 9 rewrite strategies (see §1). Domain-specific best strategies. Lower-ranked sources benefit most (Cite Sources +115% for rank-5 sources). |
| **C-SEO Bench (NeurIPS 2025)** [P] | A counterweight: content rewrites alone rarely move citations once retrieval rank is fixed. Scores are necessary but not sufficient. |

**Gap analysis:** no existing tool (a) varies criteria by page type, (b) weights by buyer-journey stage, (c) handles B2B technical attributes (standards, compatibility, lifecycle), (d) scores reusable CaaS blocks, (e) checks document gateways, or (f) publishes anchored descriptors and evidence. These are the agent's differentiators.

---

## 5. LLM-as-judge rubric design guidance

### 5.1 Principles (with evidence)

1. **Decompose; don't ask for a global score.** Holistic scores vary between runs. Multi-dimensional scoring aggregated afterwards is more stable [V/P]. CheckEval [P, EMNLP 2025] broke criteria into yes/no checklist items and raised average agreement across 12 evaluator models by 0.45, with lower variance and better human correlation.
2. **Binary sub-checks roll up to anchored levels.** Hamel Husain [V-expert] argues for pass/fail over Likert: adjacent points are inconsistent and raters drift to the middle. Track gradual quality as "k of n checks passed". Recent work shows Likert can match pairwise only when judges are well calibrated on fine scales (κ>0.7) [P]. **Recommendation:** each criterion = 3–6 binary checks → deterministic mapping to a 0–4 level with written anchors. The LLM answers checks; code computes levels.
3. **Anchor every level with concrete descriptors and ideally examples.** Prometheus [P, ICLR 2024] showed that a rubric with per-score descriptions plus a reference answer for a perfect score lets a 13B judge reach r=0.897 with humans. Include one short exemplar passage per level for the main criteria, drawn from your own domain and varied across topics.
4. **Evidence first, then reasoning, then score.** Ask the judge to quote verbatim evidence (or state "NOT FOUND"), explain briefly, then decide. Reasoning before the verdict improves accuracy and auditability. G-Eval [P] uses CoT evaluation steps. RULERS [P, 2026] showed that fixed criteria + traceable evidence + calibration beat prompt-only scoring and were more robust to rubric rewording. **Verify quotes in code** (substring match against the page text). Unverifiable quotes → criterion flagged, score capped.
5. **Absence must score low.** Tell the judge: "If evidence is not present in the provided content, the check fails. Do not infer from brand reputation or likely intent." This counters leniency and authority bias, which judges show even with binary prompts [P].
6. **Weights live in code, not in the prompt.** The LLM scores criteria. A deterministic function applies page-type × stage weights, caps and gates. This keeps scores reproducible and lets weights be tuned without re-prompting.
7. **Gates and caps for critical failures.** E.g. PDP with no spec facts → overall capped at 40. Key info only in an image or PDF → extractability criterion = 0. A factual contradiction → trust capped. This prevents averaging from hiding deal-breakers.
8. **Bias controls:**
   - Position bias (Zheng et al. [P]): don't present competitor pages in a fixed order. For pairwise comparison against competitors, swap order and accept a result only when it is consistent across both orders.
   - Verbosity bias: state that length is not quality, and score "focus" explicitly.
   - Self-preference: if the agent also *generates* rewrites, judge with a different model family, or at least a separate prompt/context.
   - Anchoring: never pass previous scores into a re-score (2026 anchoring-bias study [P]).
9. **Determinism & variance:**
   - Temperature 0 (or low).
   - Structured JSON output with schema validation and retries. HubSpot's grader uses the same pattern.
   - Optionally run 3 samples and take the median per criterion. Report variance; flag criteria with high variance for human review.
   - G-Eval-style probability weighting if logprobs are available.
10. **Calibrate against humans before trusting the scores:**
    - Build a gold set of 50–150 pages per major page type, labelled by 2–3 SEO/content/product experts on the same rubric.
    - Compute Cohen's/Fleiss' κ (human-human, then judge-human). Target κ ≥ 0.6 per criterion. Rewrite criteria that don't reach it.
    - Use expert critiques ("critique shadowing") as few-shot examples.
    - Lock the prompt and version it. Re-calibrate when the model changes.
11. **Avoid score inflation:**
    - Calibrate so a typical current page lands at 40–60 and 85+ is rare.
    - Show the score distribution of the gold set.
    - Require evidence for every point awarded.
    - Use "Highest" anchors that need exceptional evidence, such as original data or named experts.
12. **Validate against outcomes.** Correlate content scores with citation rates from a prompt panel (target prompts × engines) over time. Content scores should predict *citation-readiness*. If a criterion shows no relationship, reduce its weight.
13. **Make recommendations traceable.** Each failed check maps to a specific recommendation template, rated for impact (weight × gap) and effort. Draft rewrites quote the original passage and propose a replacement, following the Writesonic/Frase "issue → why → fix" pattern. Sort by impact ÷ effort, adjusted for the business objective/CTA input.

### 5.2 Suggested judge output schema (per criterion)

```json
{
  "criterion_id": "PDP-02_spec_completeness",
  "checks": [
    {"id": "c1", "question": "Is there an HTML spec table or list with ≥10 attributes?", "result": "pass|fail|na",
     "evidence": "<verbatim quote or NOT FOUND>", "location": "section/heading"}
  ],
  "reasoning": "<≤60 words>",
  "level": 0-4,               // computed in code from checks, judge may only propose
  "confidence": "high|medium|low",
  "recommendations": [{"issue": "...", "fix": "...", "example_rewrite": "...", "impact": "H|M|L", "effort": "H|M|L"}]
}
```

### 5.3 Prompt skeleton (per criterion or per small group)

1. Role and scope: "You evaluate citation-readiness of *content* for AI answer engines. Ignore technical SEO."
2. Context: page type, topic, industry, stage, audience, country, target prompts.
3. Criterion definition + anchored levels 0–4 + 1 exemplar per level.
4. Binary checks with definitions of pass/fail and what counts as evidence.
5. Rules: quote verbatim; missing = fail; no outside knowledge about the brand; length ≠ quality; promotional adjectives are not evidence.
6. Output JSON only.

---

## 6. Proposed draft scoring framework

### 6.1 Architecture

- **Universal criteria (U1–U10)** apply to all page types with type-specific weights.
- **Type-specific criteria** (PDP-, RNG-, CAT-, BLK-, ART-, DOC-, CS-, CMP-, FAQ-, GLO-, SOL-) add to or replace universal ones.
- **Stage multipliers** adjust weights (×0.5 to ×1.5) and then renormalize to 100.
- **Gates/caps** for critical failures.
- **Scale:** 0–4 per criterion (0 Absent, 1 Weak, 2 Adequate, 3 Strong, 4 Exemplary). This mirrors Lowest→Highest in the SQRG and avoids a 5-point midpoint trap. Overall = Σ(weight × level/4), on a 0–100 scale.
- **Bands:** 0–39 Not citation-ready · 40–59 Partially ready · 60–79 Citation-ready · 80–100 Best-in-class. Similar to Frase (60/80) and Surfer (66/70).

### 6.2 Universal criteria – definitions, anchors, evidence

| ID | Criterion | 0 – Absent | 1 – Weak | 2 – Adequate | 3 – Strong | 4 – Exemplary | Evidence to check (binary sub-checks) |
|---|---|---|---|---|---|---|---|
| U1 | **Answer-first & intent alignment** | Primary question never directly answered | Answer exists but buried below fold or after long intro | Direct answer within first ~150 words but vague or hedged | Direct, specific answer in first 1–2 sentences; title/H1 match target prompt | As 3 + every major section also opens with its own direct answer; key-takeaways/summary block | First-sentence answer? Title–H1–prompt alignment? Summary block? Section lead answers? |
| U2 | **Extractable structure** | Wall of text / image-only | Some headings, generic labels ("Overview") | Descriptive H2/H3s; some lists | Question/topic-shaped headings; lists and tables used where content is list- or table-like | As 3 + Q&A blocks; every section self-contained (no cross-references, named subjects) | Heading descriptiveness ratio; tables present where comparisons exist; "as mentioned above"-type dependencies; paragraph length |
| U3 | **Specificity & factual density** | Generic claims only | Few numbers, no units/conditions | Key claims quantified | Most claims quantified with units, conditions, standards | As 3 + no unanchored superlatives; precise terminology plus synonyms | Count quantified claims per 300 words; superlatives without support; units present |
| U4 | **Evidence & attribution** | No sources | Vague references ("studies show") | ≥1 cited source | Statistics sourced with year; standards cited by number; ≥1 attributed expert quote | As 3 + original/first-party data (tests, field data, surveys) with methodology | Links/refs to authoritative sources; quote attribution; data methodology |
| U5 | **Topical completeness (focused)** | Misses core facts | Covers <50% of expected core facts/sub-questions | Covers core facts; misses key fan-out questions | Covers core + 2–3 most likely follow-up questions | As 3 without sprawl; clear single intent; links out for adjacent intents | Expected-facts checklist (generated from target prompts + competitor answers); off-intent sections |
| U6 | **E-E-A-T & provenance** | No author/owner, no date | Brand-only attribution | Date present; organization identified | Named author/reviewer with role; updated date; experience signals | As 3 + credentials linked; testing or field experience described; "how produced" transparency | Byline, role, date, reviewer, experience statements |
| U7 | **Tone & neutrality** | Pure sales copy | Mostly promotional | Mixed | Mostly factual/descriptive; balanced trade-offs | Neutral, expert, acknowledges limitations and when *not* to use the product | Promotional adjective density; presence of trade-offs/limits |
| U8 | **Entity clarity & consistency** | Product/brand/topic entities ambiguous | Inconsistent naming | Consistent naming | Consistent naming + identifiers (ref, standard IDs) + disambiguation | As 3 + facts consistent with spec DB/feed/other pages (no contradictions) | Name variants; identifier presence; cross-check contradictions (gate) |
| U9 | **Freshness & currency** | Outdated facts/standards | No date; some dated references | Date present | Updated within 12 months for volatile topics; current standard editions | As 3 + changelog/version; lifecycle status stated | Date; standard edition years; superseded references |
| U10 | **Journey-stage & audience fit** | Wrong content for stage | Partly mismatched | Fits stage | Fits stage + audience/job-role language | As 3 + clear next step (CTA) appropriate to stage and business objective | Stage-signals checklist (see §3); CTA type vs stage |

**Gates/caps:**
- Contradiction between page facts and specs/feed → U8 = 0 and overall capped at 59.
- Key facts available only in image or PDF → U2 ≤ 1.
- Misleading or harmful safety information → overall capped at 39 and escalated to human review.

### 6.3 Type-specific criteria and default weights (sum = 100 before stage adjustment)

**PDP**

| ID | Criterion | Weight | Level 4 descriptor | Key checks |
|---|---|---|---|---|
| U1 | Answer-first product summary | 12 | 40–80 word summary: type, primary application, ≥3 quantified specs, differentiator | |
| PDP-1 | Spec table completeness & quality | 18 | ≥95% of category-required attributes present in HTML with units; standardized names; no filler | Attribute coverage % vs category schema |
| PDP-2 | Applications & use cases | 10 | ≥3 specific application noun phrases + environments + exclusions | |
| PDP-3 | Compatibility & ecosystem | 8 | Accessories, complementary products, protocols, successor/predecessor listed with links | |
| PDP-4 | Standards & certifications | 8 | All relevant standards with number/edition + downloadable proof | |
| PDP-5 | Product Q&A | 8 | ≥5 real-question Q&As, self-contained answers naming the product | |
| PDP-6 | Differentiation / selection vs siblings | 6 | "Choose this if…" + link to range comparison | |
| PDP-7 | Proof (reviews/references/case links) | 5 | Substantive reviews or named references with metrics | |
| PDP-8 | Commercial & lifecycle facts | 5 | Availability/where-to-buy, warranty, lifecycle status, substitutes | |
| PDP-9 | Document accessibility | 5 | Datasheet/manual/CAD/EPD linked with descriptive anchors; key facts mirrored in HTML | |
| U3, U7, U8 | Specificity, tone, consistency | 15 (5/4/6) | | |

**Product Range**

| Criterion | Weight |
|---|---|
| U1 Range definition & scope | 12 |
| RNG-1 Variant comparison table with "best for" | 18 |
| RNG-2 Selection guidance (decision path in text) | 14 |
| RNG-3 Applications/segments + references | 10 |
| RNG-4 Quantified differentiators | 8 |
| RNG-5 Ecosystem & migration from legacy ranges | 8 |
| RNG-6 Standards common to the range | 6 |
| RNG-7 FAQ | 6 |
| U2/U4/U7/U8/U9 | 18 (4/4/3/4/3) |

**Product Category**

| Criterion | Weight |
|---|---|
| U1 Answer-first category definition + types | 12 |
| CAT-1 "How to choose" criteria with thresholds | 18 |
| CAT-2 Type comparison table + "best for" | 16 |
| CAT-3 Featured ranges with neutral positioning | 8 |
| CAT-4 Standards/regulations | 6 |
| CAT-5 FAQ | 8 |
| CAT-6 Links to guides/glossary/tools | 4 |
| U3/U5/U7/U9/U10 | 28 (6/6/6/4/6) |

**CaaS / reusable block** (scored per block; host page aggregates)

| Criterion | Weight |
|---|---|
| BLK-1 Self-containment (named subject, no context dependency) | 25 |
| BLK-2 Single idea + descriptive heading | 10 |
| BLK-3 Factual specificity with source/claim ID | 20 |
| BLK-4 Consistency with canonical data | 20 |
| BLK-5 Parameterization / non-duplication | 10 |
| BLK-6 Tone/neutrality | 10 |
| BLK-7 Localization correctness (units, standards per country) | 5 |

Host-page assembly check: redundancy across blocks, conflicting claims, order (answer block first).

**Article / blog**

| Criterion | Weight |
|---|---|
| U1 Answer-first + key takeaways | 16 |
| U2 Fan-out headings & self-contained sections | 14 |
| U4 Statistics, citations, expert quotes, original data | 16 |
| U5 Focused completeness | 12 |
| U6 Author/reviewer, dates, experience | 12 |
| U3 Specificity | 8 |
| U7 Neutral tone | 8 |
| ART-1 Title–query alignment & non-clickbait | 6 |
| U10 Stage fit + next step | 8 |

**Document (datasheet / whitepaper / catalog / guide)**

| Criterion | Weight |
|---|---|
| DOC-1 HTML gateway exists with abstract & key facts | 22 |
| DOC-2 Text-extractable, tagged structure, real tables | 16 |
| DOC-3 Descriptive title/filename/metadata, version/date | 12 |
| DOC-4 Key findings/specs summarized (bulleted/tabled) | 14 |
| DOC-5 Methodology & references (whitepapers) / test conditions (datasheets) | 12 |
| DOC-6 Consistency with PDP/spec DB | 10 |
| DOC-7 Ungated summary (if gated) | 6 |
| U9 Currency / supersession notice | 8 |

Datasheets shift weight from DOC-5 methodology toward attribute completeness (reuse PDP-1).

**Case study**

| Criterion | Weight |
|---|---|
| CS-1 Outcome-led title and 100–150 word summary | 16 |
| CS-2 Customer profile (industry, size, country, application) | 10 |
| CS-3 Quantified results with baseline and timeframe | 22 |
| CS-4 Challenge/solution/results structure | 10 |
| CS-5 Attributed customer quote | 10 |
| CS-6 Products/solutions used, linked | 10 |
| CS-7 Methodology for metrics / verifiability | 8 |
| U7/U9 | 14 (8/6) |

**Comparison / selection guide**

| Criterion | Weight |
|---|---|
| CMP-1 Neutral comparison table (same attributes and units) | 22 |
| CMP-2 Explicit criteria & "choose X if" verdicts | 18 |
| CMP-3 Honest trade-offs/limitations | 12 |
| U1 Answer-first verdict | 12 |
| U4 Sources/test data | 12 |
| U3 Specificity | 8 |
| U9 Date/currency | 6 |
| U10 Stage fit/next step | 10 |

**FAQ/support KB:** U1 answer in first sentence 25; applies-to products/identifiers 15; steps/structure 15; specificity (codes, values) 15; currency 10; self-containment 10; links to docs 10.

**Glossary:** definition-first sentence 30; formula/units/standard 20; example 15; disambiguation/related terms 15; sources 10; links to products/guides 10.

**Solution/industry page:** problem quantified 14; architecture explained in text 16; components linked 10; outcomes quantified 14; proof/case studies 14; standards/regulation 8; FAQ 8; tone 8; stage fit/CTA 8.

### 6.4 Stage multipliers (applied to criterion weights, then renormalized)

| Criterion family | Awareness | Education | Consideration | Evaluation | Decision |
|---|---|---|---|---|---|
| Answer-first / definitions (U1, GLO) | 1.4 | 1.3 | 1.0 | 0.9 | 0.9 |
| Evidence/original data/authority (U4, U6) | 1.3 | 1.4 | 1.1 | 1.0 | 0.8 |
| Neutral tone (U7) | 1.4 | 1.3 | 1.2 | 1.0 | 0.7 |
| Comparison/selection (CMP, CAT-1/2, RNG-1/2, PDP-6) | 0.6 | 0.9 | 1.5 | 1.4 | 1.0 |
| Spec completeness/compatibility/standards (PDP-1/3/4) | 0.6 | 0.8 | 1.1 | 1.5 | 1.3 |
| Proof (case studies, reviews, references) | 0.7 | 0.9 | 1.2 | 1.4 | 1.2 |
| Commercial/lifecycle/CTA (PDP-8, U10 CTA) | 0.5 | 0.6 | 0.9 | 1.1 | 1.5 |

### 6.5 Recommendation generation logic

1. For each criterion: gap = (4 − level)/4 × effective weight → **impact points**.
2. Map each failed binary check to a recommendation template, e.g. PDP-3 fail → "Add a 'Compatible with' section listing accessories, protocols and successor references."
3. Personalize with the inputs:
   - **Target prompts:** show which prompt is unanswered.
   - **Competitors:** which facts or format competitors provide, e.g. "Competitor pages include a variant comparison table."
   - **Job role:** specifier → standards/BIM; procurement → availability/substitutes.
   - **Business objective and CTA:** align the next-step block.
4. Effort estimate (L/M/H) per template. Sort by impact ÷ effort.
5. Provide **rewrite exemplars**: original quoted passage → proposed answer-first, quantified version. Mark facts that need SME validation as `[VERIFY]`, and never invent specs.
6. Report: overall score + band; per-criterion level with evidence quotes; top 5 recommendations; gates triggered; confidence; and the disclaimer that the score measures citation-readiness, not guaranteed AI citation.

### 6.6 Validation plan (summary)

- Gold set per page type (≥50 pages), 2–3 expert raters, κ per criterion.
- Judge-vs-human agreement ≥ 0.6 κ before production.
- Outcome validation: correlate scores with citation rate on a fixed prompt panel across ChatGPT, Perplexity, AI Overviews/AI Mode, Copilot and Gemini, in before/after edit experiments. Re-weight criteria annually or on model changes.

---

## 7. Sources

**Primary / peer-reviewed / official**
- Aggarwal et al., *GEO: Generative Engine Optimization* (KDD 2024) – https://arxiv.org/abs/2311.09735 ; full results https://arxiv.org/html/2311.09735v3
- Puerto et al., *C-SEO Bench: Does Conversational SEO Work?* (NeurIPS 2025) – https://arxiv.org/abs/2506.11097
- Google Search Central – Creating helpful, reliable, people-first content – https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central – AI features and your website – https://developers.google.com/search/docs/appearance/ai-features
- Google Search Quality Rater Guidelines (Jan 2025 PDF copy) – https://ppc.land/content/files/2025/04/searchqualityevaluatorguidelines.pdf ; overview https://ppc.land/search-quality-rater-guidelines/
- Microsoft Advertising blog – Optimizing your content for inclusion in AI search answers (Oct 2025) – https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers
- OpenAI Commerce – Product Feed reference – https://developers.openai.com/commerce/specs/feed
- Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (NeurIPS 2023) – https://arxiv.org/html/2306.05685v4
- Liu et al., *G-Eval* (EMNLP 2023) – https://arxiv.org/pdf/2303.16634v2.pdf
- Kim et al., *Prometheus* (ICLR 2024) – https://arxiv.org/abs/2310.08491v2 ; https://github.com/kaistAI/Prometheus
- Lee et al., *CheckEval* (EMNLP 2025) – https://arxiv.org/abs/2403.18771
- *From Rubrics to Reliable Scores: Evidence-Grounded Text Evaluation with LLM Judges* (RULERS, 2026) – https://arxiv.org/abs/2601.08654
- *Anchoring Bias in LLM-as-a-Judge Systems* (2026) – https://arxiv.org/pdf/2608.25869
- *Aligning with Human Judgement: Pairwise Preference in LLM Evaluators* – https://arxiv.org/pdf/2403.16950

**Large-sample studies (vendor)**
- Semrush – How we built a content optimization tool for AI search [study] – https://semrush.com/blog/content-optimization-ai-search-study
- Wix Studio AI Search Lab – Content types most cited by LLMs – https://www.wix.com/studio/ai-search-lab/research/content-types-most-cited-by-llms
- Peec AI – Content types cited most by engine – https://docs.peec.ai/research/content-types-cited-most-by-engine
- Ahrefs – AI assistants prefer fresher content (17M citations) – https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content
- Surfer – How AI Overviews choose sources – https://surferseo.com/blog/how-ai-overviews-choose-sources ; Content coverage study – https://surferseo.com/blog/content-coverage-study
- Growth Memo (Kevin Indig) – Shorter, focused content wins in ChatGPT – https://www.growth-memo.com/p/shorter-focused-content-wins-in-chatgpt ; coverage: https://searchengineland.com/chatgpt-citations-content-study-469483 ; https://www.practicalecommerce.com/studies-reveal-ai-citation-clues
- Profound – AI platform citation patterns – https://www.tryprofound.com/blog/ai-platform-citation-patterns
- SE Ranking – How to optimize for AI Mode – https://seranking.com/blog/how-to-optimize-for-ai-mode/
- TREW Marketing / GlobalSpec – State of Marketing to Engineers (2025/2026) – https://www.trewmarketing.com/blog/2025-state-of-marketing-to-engineers-research ; https://advertising.globalspec.com/state-of-marketing-to-engineers-research-report
- Elektor/TREW – Engineer preferences in Europe – https://elektormagazine.com/articles/decoding-engineer-preferences-insights-into-technical-buying-behavior-in-europe
- MarketingProfs – Content habits of engineers – https://www.marketingprofs.com/charts/2021/44146/the-content-habits-and-preferences-of-engineers
- TraceParts survey – https://info.traceparts.com/news/banner-ads/a-survey-conducted-by-traceparts-is-giving-industrial-marketing-experts-a-clearer-insight-into-the-needs-of-engineers-and-designers/
- Digital Commerce 360 – Forrester B2B buying & AI 2026 – https://digitalcommerce360.com/2026/01/22/forrester-b2b-buying-ai-2026/

**Tool documentation**
- HubSpot AEO Grader – https://hubspot.com/aeo-grader
- Frase GEO Score – https://www.frase.io/tools/geo-score ; https://www.frase.io/blog/geo-scoring-in-frase
- Surfer Content Score – https://docs.surferseo.com/en/articles/6109757-answering-your-most-frequent-content-score-questions
- Writesonic GEO Content Score – https://docs.writesonic.com/changelog/geo-content-score
- Semrush AI Visibility Toolkit – https://www.semrush.com/kb/1493-ai-visibility-toolkit ; AI SEO metrics https://de.semrush.com/kb/1594-ai-seo-metrics
- Conductor AI Content Score – https://www.conductor.com/academy/ai-content-score/
- MarketMuse Content Score – https://docs.marketmuse.com/marketmuse-terminology/what-is-content-score/
- Clearscope grading – https://clearscope.io/support/articles/how-does-clearscope-grade-your-content
- Otterly GEO Audit – https://help.otterly.ai/what-does-the-geo-audit-do
- Profound vs Scrunch (Conductor) – https://www.conductor.com/compare/profound-vs-scrunch/ ; AthenaHQ/Scrunch – https://www.airops.com/blog/scrunch-vs-athena-comparison-2026
- Goodie – https://www.higoodie.com/features/ai-search-optimization
- BrightEdge recommendations – https://www.brightedge.com/node/154

**Ecommerce / AI shopping (practitioner)**
- Google Merchant Center conversational attributes – https://searchengineland.com/google-launches-ai-performance-insights-and-conversational-attributes-in-merchant-center-478108 ; https://limelightmarketing.com/blogs/merchant-center-conversational-attributes/ ; https://www.channable.com/blog/google-conversational-attributes
- Google AI Mode shopping – https://www.productsup.com/blog/inside-google-shopping-ai-mode-how-it-works-and-what-powers-it/ ; https://www.channable.com/blog/google-shopping-ai-mode
- Perplexity shopping – https://www.shopify.com/blog/perplexity-shopping ; https://fortune.com/2024/11/18/perplexity-ai-ceo-shopping-product-recommendation-search-tools
- Amazon Rufus/COSMO – https://sellermetrics.app/amazon-listing-optimization-for-rufus/ ; https://ppc.land/rufus-shows-5-products-not-50-what-brands-must-know-about-amazons-ai-filter/
- PDP optimization for AI – https://www.nudgenow.com/blogs/optimizing-pdps-for-ai-search ; https://www.yotpo.com/blog/optimize-product-pages-for-ai-search.md
- Ecommerce citations by page type – https://aleydasolis.com/en/ai-search/ecommerce-ai-search-citations-optimization

**B2B / industrial / journey (practitioner)**
- GEO for manufacturing – https://lseo.com/generative-engine-optimization/generative-engine-optimization-geo-for-manufacturing-industrial/ ; https://aha.elliance.com/2024/12/08/manufacturing-generative-engine-optimization-geo-for-industrial-companies/
- Mapping prompts to buyer journey – https://lseo.com/answer-engine-optimization-services/mapping-prompt-classes-to-the-buyer-journey-for-aeo/ ; https://beomniscient.com/blog/mapping-content-to-buyer-intent-in-ai-search/
- Case studies for AI citation – https://www.texta.ai/blog/case-study-pages-making-them-ai-citation-worthy
- Whitepapers/PDFs for AI search – https://www.webtures.com/insights/how-to-optimise-whitepapers-and-reports-for-ai-search/ ; https://maxaeo.ai/blog/gated-content-ai-search/
- Query fan-out / passages – https://ipullrank.com/resources/webinars/query-fan-out-webinar ; https://www.getpassionfruit.com/research/is-query-fan-out-a-marketing-buzzword-or-something-relevant ; https://hartzer.it.com/content-chunking-and-passage-retrieval/

**LLM-as-judge practice**
- Hamel Husain – Binary vs Likert – https://hamel.dev/blog/posts/evals-faq/why-do-you-recommend-binary-passfail-evaluations-instead-of-1-5-ratings-likert-scales.html
- Simon Willison on critique shadowing – https://simonwillison.net/2024/Oct/30/llm-as-a-judge
- Eugene Yan – Evaluating LLM-evaluators – https://eugeneyan.com/writing/llm-evaluators/
- GoDaddy – Calibrating scores of LLM-as-a-judge – https://www.godaddy.com/resources/news/calibrating-scores-of-llm-as-a-judge
- Kinde – LLM-as-a-judge done right – https://kinde.com/learn/ai-for-software-engineering/best-practice/llm-as-a-judge-done-right-calibrating-guarding-debiasing-your-evaluators/

*Limitations: several vendor primary pages (Growth Memo full report, Semrush AI Visibility methodology, Writesonic full factor list, HubSpot sub-components, Microsoft LLM-scoring white paper) were paywalled, truncated or binary and could not be fully verified. Figures marked [S]/[V] are correlational or vendor-reported. Weights in §6 are reasoned starting points to be calibrated, not empirically derived.*

# Customer Success Story & Calculator / TradeOff Tool: GEO analysis, scoring logic and pilot

> **Status (20 Oct 2026):** design record. Pilot scores in this file were computed before the v2.0/v2.1 standard (some on server HTML, with older gate IDs). For current scores use `research/final-scoring/` and `final-scoring/SE_GEO_scored_inventory_v2.1.csv`; for current logic use `skill/geo-research/references/page-types-v2.md`.

*Prepared 2026-10-19 for the Content GEO Score Agent (global standard). Builds on the `geo-research` skill v1.0: U1–U10, the judge protocol and `weights.json`. Nothing in the skill folder was edited.*

**Inputs**
- Corpus files 19–24 (customer stories) and 31–36 (TradeOff Tools), which are server HTML converted to markdown.
- Browser checks of the rendered pages, run on 2026-10-19.
- External research on 26 sources (§3).

**Artefacts**
- Pilot judge JSONs: `research/type-analysis/pilot/NN_judge.json` (19–24, 31–36).
- Score cards: `pilot/scorecards/`.
- Sensitivity runs: `pilot/sensitivity/` (21R, 33R).
- Merged draft weights: `pilot/weights_casecalc_draft.json`. A working copy is in the session scratchpad `agents/case_calc/`.

> Scores measure citation-readiness of the content only. Whether an AI engine actually cites a page also depends on retrieval, off-site consensus and technical access.

---

## 1. Executive summary

**1. Both page types score Poor to Average on what AI crawlers receive. The main cause is the template, not the writing.**
- **Customer stories: 9–54** (median 29).
  - Four of the six stories use the newer campaign template (QDS web components). In those, the narrative is client-rendered inside shadow DOM, which non-JS crawlers (GPTBot, ClaudeBot, PerplexityBot) don't execute.
    - Affected: McLaren, Massmart, Rubis Photosol, Zicaffè.
    - Missing from the crawlable text: the hero summary, the challenge/solution/results story and the customer quotes.
    - What remains in server HTML: stat cards, product-card grids, empty tab labels and placeholder blocks ("ZZ_Heading").
  - Only Blackstone (older template, full story in text) and Vancouver Airport (one answer-shaped sentence with two dated metrics) reach Average.
- **Calculators: 11–17**, all Poor.
  - Every TradeOff Tool page follows the same template: a 1–2 sentence "Use this TradeOff Tool to…" intro, then white-paper and tool cards.
  - The tool runs in an iframe at a separate URL whose raw HTML is about 5 words.
  - Inside that tool sits exactly what an engine would cite, all invisible to crawlers:
    - "About this tool" text and model provenance (Data Center Science Center).
    - A numeric assumptions list (e.g. 290 W/socket CPU, 1,300 W/socket GPU, 0.8 W/TB storage).
    - Input definitions and typical values (safety margin 10–20%; PUE).
    - Default results (790 kW IT → 1,110 kW utility input).
    - The version date ("TT1 Version 4 – 10-September-2024").

**2. The logic discriminates once the content exists.** In the sensitivity runs, the same judge criteria applied to the rendered text give:
- Massmart: 32 → 55.
- Power-sizing calculator: 16 → 71 raw, capped at 59 because the tool contradicts itself on "typical PUE" (1.8 vs 1.4).

**3. Proposed logic**
- **Case study v1.1.** A revision of §8 with explained changes:
  - Adds U3 at weight 8, because hidden/video/tab narratives are the dominant failure.
  - Moves CS-1 to the answer_def family.
  - Re-balances CS-5, CS-6, U2, U7, U8 and U10.
  - New gate **G7**: no quantified outcome in text → ≤ 59.
  - New penalty **placeholder_text** (−2).
- **Calculator v1.0.** A new type with 13 criteria: five type-specific (CALC-1 method 16, CALC-2 assumptions 13, CALC-3 worked example/benchmarks 15, CALC-4 inputs/outputs defined 7, CALC-5 interpretation 6), plus U1, U2, U3, U5, U7, U8, U9 and U10.
  - New gate **G8**: method, assumptions and example results all absent from text → ≤ 39 and U3 ≤ 2.

**4. Quick wins, which are template-level and SE-wide**
1. Server-render the campaign-template story components → SE Digital.
2. Add a crawlable "How this calculator works" block to the TradeOff Tool template:
   - formula/logic
   - assumptions with sources and years
   - one worked example
   - typical ranges
   - limits
   - version/date
3. Put the outcome sentence ("[Customer] [result + unit] [period] with [named offer]") in the H1/summary of every story.
4. Purge "ZZ_" placeholders.
5. Show a project/results date.

---

## 2. Corpus audit

### 2.0 How the audit was run

**Checker.** `geo_content_check.py --format md --pretty` was run on each corpus file. It was also run on body-only copies with the header comment and footer stripped, because the checker counts the header comment as the "lead" and includes the "Need help?" footer.

**Checker artefacts to know about.** These are recorded for the skill owner.
- Words, lead sentence and "Quotes: 3" are inflated by the header comment.
  - Body-only word counts: stories 93–475 words; calculators 197–263 words.
- The fluff ratio counts title, meta and footer words such as "Next-generation Automation".
  - McLaren: 2.53/100 words on the full file vs 1.46 on body only.
  - Zicaffè: 1.99 vs 3.23.
- The vague-CTA detector found nothing because CTAs are plain text in the markdown. The counts were done manually.
- `date labels: ['updated']` on Blackstone is a false positive from "automatically updated".
- H1 = 0 on calculators 31 and 33–36 is caused by the malformed markup. Following the brief, the H1 is treated as present and equal to the page title.

**Rendered check.** I ran a browser check on 2026-10-19, which is out of scope for the score but explains the gaps.
- **Customer stories:**
  - The story text sits in QDS web components (shadow DOM), not in the server HTML: hero, "The challenge", "The solution", "The results" and testimonials.
  - This was confirmed on McLaren, Massmart, Rubis Photosol and Zicaffè. Vancouver's rendered page adds almost nothing.
  - The tab panels for Overview/Challenges/Solutions/Results contain only CSS in server HTML.
- **Calculators:**
  - The tool iframe (`/work/solutions/system/s1/…/trade-off-tools/<tool>/`) returns 5 words of raw HTML. Its client-rendered content includes "About this tool", "Assumptions", definitions, defaults and version.
  - Checked on power sizing (33). The capital-cost tool (32) showed the same architecture, with default cost breakdowns (e.g. "Power: $ 44.6 M (50.6%)").

### 2.1 Customer success stories (19–24)

Prompts are inferred: one seed prompt, then fan-out prompts. All scores are pilot v1.1 scores on server text.

**19 McLaren Racing**
- Stage: Consideration. Body: 137 words. Score: **9**.
- Prompts: How does McLaren Racing use SE technology? · Which SE products does McLaren use? · How do F1 teams manage factory/trackside energy? · Examples of motorsport teams using power monitoring · What results has McLaren achieved?
- **What an AI would extract:** "80,000 parts…", "20+ years… relationship", "56,304 sqm" and six product names. None of it is an outcome.
- **Strongest:** exact product names (Masterpact™ MTZ/NW/M, PowerLogic™, EcoStruxure Power Monitoring Expert).
- **Weakest:**
  - Slogan H1 "Innovation in motion".
  - No story in text.
  - Vanity statistics.
  - Published placeholders ("ZZ_Label", "ZZ_Heading", alt "ZZ_aprimo image alt text").
  - Brand spelled "Netbotz™".
- **Fit:** fails every prompt. G2 and G7 apply.

**20 Blackstone**
- Stage: Evaluation. Body: 475 words. Score: **49**.
- Prompts: How did Blackstone cut energy costs across portfolio companies? · Examples of PE firms using energy management software · What is EcoStruxure Resource Advisor used for? · How much did Blackstone save? · How to manage sustainability data across a multi-site portfolio
- **What an AI would extract:**
  - "15% reduction of CO2".
  - The challenge/solution/results bullets.
  - Two quotes attributed to the CSO.
  - The role of Resource Advisor: "captures and normalizes energy and utility data".
- **Strongest:** the only story told fully in text, with a substantive named quote and the product's role explained.
- **Weakest:**
  - "Tens of millions" is vague. The precise "$60 million… over six years" is **only in the meta description**.
  - No baseline or period for the 15%.
  - Promo blocks interrupt the story.
  - Bullets are flattened into run-on paragraphs.
  - No date.
- **Fit:** answers the "what was done" fan-outs. The "how much" fan-out gets only a vague answer.

**21 Massmart**
- Stage: Evaluation. Body: 143 words. Score: **32**.
- Prompts: How did Massmart reduce store energy costs? · Examples of retailers using BMS to save energy · How much can a BMS save in retail? · What is EcoStruxure Building Operation? · Multi-site retail energy management case study (South Africa)
- **What an AI would extract:** "Over 155 BMS systems installed…", "Annualized energy cost savings of R15 million (ZAR)" and a product list.
- **Strongest:**
  - One strong metric with currency and a time basis.
  - An H1 that states the problem solved.
- **Weakest:**
  - Empty tabs (Overview/Challenges/Solutions/Results).
  - No country stated in text.
  - Rendered text says "more than 250 of their stores", which needs reconciling with "155 BMS systems".
- **Fit:** "how much" is answered; "how" is not.

**22 Vancouver Airport (YVR)**
- Stage: Consideration. Body: 186 words. Score: **54**.
- Prompts: Examples of airports reducing emissions with energy management · How is YVR reaching net zero by 2030? · How much has YVR reduced emissions? · What software do airports use to track carbon? · Airport decarbonization strategies
- **What an AI would extract:** "YVR is cutting emissions… reducing 530t CO₂e/year since 2021 and lowering emissions by 18 % from 2022–23." This one sentence is almost an ideal citable outcome sentence.
- **Strongest:** two metrics, each with a timeframe and a baseline year, attributed to EcoStruxure.
- **Weakest:**
  - "BOLD Pursuit" slogan heading.
  - No solution narrative (which software did what).
  - No quote.
  - Latest data is from 2023 and the page is undated.
  - Depth is pushed to an e-book.
- **Fit:** best fit for the "examples of…" seed prompt. Weak on the "how/what software" fan-outs.

**23 Rubis Photosol**
- Stage: Evaluation. Body: 115 words. Score: **26**.
- Prompts: How does Rubis Photosol keep solar parks at high uptime? · Predictive maintenance for solar farm transformers · What is EcoCare for Electrical Distribution? · How to achieve 99% uptime in PV plants · Condition-based maintenance case study
- **What an AI would extract:** a strong profile: "50 solar parks… 600 MWp", "leading independent producer of photovoltaic energy in France", and the goal "Aiming to maintain a 99% uptime rate".
- **Strongest:** the best customer-profile paragraph in the set.
- **Weakest:**
  - No achieved result (99% is a target).
  - "ZZ_Paragraph Title / ZZ_Paragraph Content" placeholders.
  - The story, including four "results in hours, not months" articles and a quote, is client-rendered.
- **Fit:** profile prompts only. G7 applies.

**24 Zicaffè**
- Stage: Evaluation. Body: 93 words. Score: **9**.
- Prompts: How did Zicaffè digitalize coffee production? · F&B plants using software-defined automation · What is EcoStruxure Automation Expert? · Benefits of open automation in F&B · Coffee plant automation case study
- **What an AI would extract:** three unquantified benefits and four product names.
- **Strongest:** products are named.
- **Weakest:**
  - Slogan H1.
  - Industry and location stated only in the meta.
  - The tautology "Data digitization digitalizes operations".
  - Two H1s.
  - "Zicaffe" vs "Zicaffè".
  - "TeSys contractors", which an SME should check (likely a misnomer for contactors).
  - The quote and story are client-rendered.
- **Fit:** fails. G7 applies, plus the fluff penalty.

**Cross-page patterns (stories)**

| Pattern | Pages | Level | Owner |
|---|---|---|---|
| Story, hero summary and quotes rendered client-side (QDS shadow DOM); server HTML has only stat/product cards | 19, 21, 23, 24 (22 thin in both) | **Template** | SE Digital (tech) + content (provide text equivalents) |
| Overview/Challenges/Solutions/Results tabs with no panel text in HTML | 21, 23 | Template | SE Digital |
| Published placeholders ("ZZ_…") in headings, cards and alt text | 19, 23 | Template QA / author | Web publishing QA |
| Slogan H1 instead of outcome headline ("Innovation in motion", "A SUSTAINABLE business plan", "BOLD Pursuit") | 19, 20, 22, 24 | Author (campaign style) | Content owner |
| Stat cards with vanity numbers (relationship years, floor area, parts) instead of outcomes | 19 | Author | Content owner |
| Best facts only in meta description (Blackstone "$60 million… six years"; Zicaffè "Sicilian coffee company") | 20, 24 | Author | Content owner |
| No publish date, project date or results period | 6/6 | Template (no date field) | SE Digital + content |
| No measurement method for any metric | 6/6 | Author / process | Content owner + customer |
| Product cards list offers without their role in the project | 19, 21, 22, 24 | Template (card grid) | Content owner |
| Vague CTAs ("Read more", "Learn more", "Discover more") | 20, 21, 23, 24 | Template | Content owner |

### 2.2 Calculator / TradeOff Tool pages (31–36)

**All six pages: same template.**
- **What an AI would extract:** a "Use this TradeOff Tool to …" sentence, plus white-paper card titles with one-line summaries.
- **Common strengths:**
  - Title and H1 match the tool query exactly.
  - White-paper cards are descriptive, numbered ("White paper 3 presents methods for calculating power and cooling requirements") and self-contained.
- **Common gaps:**
  - No formula or logic.
  - No assumptions or default values.
  - No worked example.
  - No typical ranges.
  - No input definitions.
  - No version or date.
  - Generic CTAs ("Start calculation", "Learn more", "Explore now").
- G8 applies to all six.

| # | Page | Stage | Body words | Seed prompt / fan-out (inferred) | Page-specific notes | Score |
|---|---|---|---|---|---|---|
| 31 | Site electricity emission factor | Consideration | 200 | How do you calculate a site's electricity emission factor? · effect of on-site generation and offsets · typical grid factor (kgCO2e/kWh) · reduce Scope 2 · location- vs market-based | Best intro: names the three drivers (utility supply, on-site generation, offsets). No role or segment named | **17** |
| 32 | Data center capital cost | Evaluation | 235 | How much does a data center cost per MW? · main CapEx drivers · liquid vs air cooling CapEx · power vs cooling cost split · cost of a 1 MW data center | Highest-demand prompt, emptiest answer: "Analyze key cost drivers" without naming any. The tool shows default splits (e.g. power 50.6%, liquid- vs air-cooled) invisibly. Intro duplicated; "Tradeoff" vs "TradeOff"; no WP numbers | **11** |
| 33 | Data center power sizing | Consideration | 197 | How to calculate data center power requirements · power per AI/GPU server · typical PUE · safety margin · IT load vs utility input | WP 3 card describes the method source but doesn't say the tool uses it. The tool holds the complete assumptions list (§2.0) | **16** |
| 34 | Single-phase UPS efficiency | Evaluation | 237 | How much does UPS efficiency affect electricity cost? · comparison · how to calculate UPS losses · carbon of losses · when to replace an older UPS | 57–65% of words shared with page 36, so the boilerplate penalty applies | **14** |
| 35 | Edge UPS fleet management | Evaluation | 202 | In-house vs outsourced edge UPS fleet? · fleet management cost · remote monitoring benefits · downtime cost · managed vs DIY cost | Frames the outsourced option as "a partner like Schneider Electric". Related-tool name differs from the canonical tool name | **13** |
| 36 | Three-phase UPS efficiency | Evaluation | 263 | Three-phase UPS efficiency and cost? · eco-mode vs double conversion · comparison · UPS kWh losses · carbon in AI data centers | Near-duplicate of 34. WP 157 card has a stray ", Many" | **14** |

**Cross-page patterns (calculators)**
- **Template issues, which explain about 95% of the gap.** Owner: SE Digital plus the TradeOff Tools team.
  - The knowledge is trapped in the iframe app.
  - The parent page carries no method, assumptions, example or date.
  - Related-content grids replace explanatory content.
  - Generic CTA labels.
  - Duplicated single- and three-phase pages.
- **Author-level issues:**
  - The intro promises "insights", "smarter design decisions" or "informed decisions" without naming a driver or a number.
  - No audience or role named (31).
  - Naming drift: Tradeoff/TradeOff; "Single-phase UPS efficiency calculator" vs "…comparison calculator"; "DCIM monitoring value calculator (for distributed IT)".
  - The tool's own text contradicts itself (typical PUE "1.8" and "1.4"). Fix this before mirroring the text onto the page.
- **Opportunity.** SE already owns citable, first-party, numeric methodology, the kind of data engines prefer (specs and numbers [C]).
  - Mirroring it into the HTML is a low-effort, high-impact template change.
  - In the sensitivity run, page 33 goes from 16 to 59. With the PUE contradiction fixed it reaches 71 (Good).

---

## 3. External research & exemplars

The research was run by a sub-agent on 2026-10-19 with generic queries and no downloads.

**Evidence labels**
- **[C]** controlled/causal study
- **[L]** large-sample correlational
- **[O]** official platform statement
- **[P]** practitioner opinion or consensus

**Overall caveat:** no independent study isolates citation rates for case studies or calculators as page types. The evidence is strong only on crawlability (official statements and logs) and on facts and numbers in general (controlled studies). Element-level advice for these two types is mostly practitioner opinion.

### 3.1 Sources

| # | Claim (paraphrased) | Source (date) | Label |
|---|---|---|---|
| R1 | Major AI crawlers fetch HTML without executing JavaScript (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot and others). Some download JS files but don't run them. Gemini (Googlebot infrastructure) and AppleBot do render. Recommendation: server-render critical content | Vercel/MERJ, "The rise of the AI crawler", vercel.com/blog/the-rise-of-the-ai-crawler (2024-12-17) | [L] |
| R2 | Google renders JS in a queued second phase. "Not all bots can run JavaScript"; server-side or pre-rendering recommended | developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics (upd. 2026-03-04) | [O] |
| R3 | Google AI features have no extra technical requirements beyond indexing and snippet eligibility. Make important content available in textual form; structured data must match visible text | developers.google.com/search/docs/appearance/ai-features (upd. 2025-12-10) | [O] |
| R4 | Google can associate iframe content with the parent page (`indexifembedded`), but this is "not always trivial". Put content on the page if it must be indexed in context. A third-party test shows a parent can rank for iframe-only text | Google robots-meta doc (upd. 2026-03-24) [O]; Mueller via seroundtable.com (2017) [O, second-hand]; searchengineland.com "How Googlebot handles iframes" [C-lite, summary only] | [O]/[C-lite] |
| R5 | Bing: AI systems may not render hidden content in tabs or expandable menus. Don't rely on PDFs or images alone for core information. Use self-contained passages, lists, tables and Q&A | Microsoft Advertising blog, "Optimizing your content for inclusion in AI search answers" (2025-10-08) | [O] |
| R6 | Anthropic's web-fetch tool does not support JavaScript-rendered sites (API tool; not necessarily every crawler) | platform.claude.com docs, web fetch tool (current) | [O] |
| R7 | Conflicting signal: a single-site log reports OpenAI bots starting to render JS (2026-09-25), unconfirmed. Other 2026 tests show ChatGPT, Claude and Perplexity reporting only HTML values | geotoolbox.ai/blog/javascript-seo (2026-10-04/13), citing DEV Community, Forge, searchVIU and Search Engine World tests | [P/L mixed] |
| R8 | Statistics, quotations and cited sources raised visibility in a benchmark engine ("up to 40%"); domain-dependent | Aggarwal et al., GEO, KDD 2024, arxiv.org/abs/2311.09735 | [C] (contested on newer models; see skill evidence base) |
| R9 | Headline that answers the query: 41% vs 29% citation. Retrieval position 1 cited 58% vs 14% at position 10. Pages covering 26–50% of fan-out beat 100% coverage | Growth Memo × AirOps, 16,851 queries / 353,799 pages (2026-04-13) | [L] |
| R10 | Case studies: before/after metrics, timeframe, customer context, products used, quote, challenge→solution→results, 100–150-word summary, results-led title | texta.ai "case study pages: making them AI citation-worthy" (2026-03-17) | [P], vendor, unsourced numbers |
| R11 | State sample size, data source and measurement method for case metrics | addlly.ai "how to earn AI search citations" (undated; snippet only) | [P], vendor |
| R12 | Gated or PDF-only assets are effectively invisible; publish findings in HTML. One anecdote: 4.1x AI citation share after ungating | maxaeo.ai/blog/gated-content-ai-search; conductor.com/academy/gated-content-ai-discoverability; guptadeepak.com (2025) | [P] |
| R13 | Video: engines cite transcripts and surrounding text, not footage. YouTube is #1 cited domain in Gemini but around #90 in ChatGPT | pepper.inc (undated); averi.ai citing Profound (undated) | [P] |
| R14 | "Tools" page type: 5.7% of LLM-referred sessions (rank 5) across 28 B2B SaaS firms; case studies not broken out. Internal inconsistencies noted | tripledart.com/research/which-pages-do-llms-cite (Q1 2026) | [L]-lite, vendor |
| R15 | Calculator "citable shell": definition, formula in text, worked example, benchmarks, interpretation, FAQ. Tools without server-rendered explanation are a "citation dead zone" | maxaeo.ai/blog/interactive-tools-ai-citations (2026-07-13) | [P], vendor, no data |
| R16 | Calculator pages may resist AI summarisation because users need their own inputs | Practitioner commentary (various) | [P], unverified |
| R17 | Top-cited-domain trackers show no calculator sites in top tiers | llmpulse.ai/data-studies/top-cited-domains (2026-07) | [L] |

### 3.2 Exemplars

**Competitor case studies** (text inventory)
- **Siemens / Novva Data Centers** (news.siemens.com, 2024-07-22). The strongest of the four.
  - Has: results-led title; named customer and site; challenge and solution in text, including the controls deployed; partner named; date.
  - Annual metrics: kWh/yr, t CO2e/yr, $/yr, and a homes-equivalent.
  - Quote attributed by role.
  - Missing: baseline period and measurement method.
- **ABB / Swisscolocation** (new.abb.com, 2020-09-03).
  - Has: named customer, location and Tier III context; exact configuration ("DPA 250 S4", 3×50 kW modules); a 9% headline; a named CEO quote.
  - But: the 9% is *expected*, not measured; no baseline; the ROI calculation is mentioned but not shown.
- **Siemens / HOYINN Data Center** (references.siemens.com, completed 2025).
  - Has: a structured objectives → solution → benefits template; products; metrics (~60% shorter project cycle, 30% less floor area).
  - Missing: quote, baseline and method. Extra detail sits in a PDF.
- **Vertiv / anonymized payments company** (vertiv.com, 2023-12).
  - Has: a good "Case Summary" box and three result bullets (50% white space, PUE < 1.28, 20% carbon).
  - But: the customer is anonymized, there is no quote and no baseline, and detail sits in a PDF.
- **Takeaway:** no competitor states a baseline and a measurement method. An SE story with a summary box, an outcome sentence, a baseline and period, a named quote, product roles, a date and a method statement would beat all four on these elements.

**Calculator exemplars**
- **EPA GHG Equivalencies Calculator, "Calculations and References"** (epa.gov, upd. 2026-08-04). The gold standard. It has:
  - full formulas
  - emission factors with numbers and line-loss adjustment
  - worked examples
  - dataset versions (eGRID2022, IPCC AR5)
  - references
  - limitations
- **Omni Calculator, Electricity Cost.**
  - Has: definition; formula in text (kWh = W × h; cost = kWh × price); input explanation; worked example; FAQ; named author and reviewers.
  - Missing: benchmarks, sources and a visible date.
- **NerdWallet Mortgage Calculator.**
  - Has: input explanations, a glossary, a numeric example and default assumptions.
  - Missing: formula, sources and a date. This shows that domain authority can mask weak method text.

### 3.3 What the research implies for the logic

| Implication | Weighting consequence |
|---|---|
| Text presence of the core content in crawlable text is the strongest-supported factor for both types (R1–R6) | U3 added to case study logic (8) and kept in calculator logic. **G7** and **G8** guard the extreme cases. "Content decision vs tech" boundary kept: rendering → SE Digital; text-equivalents → content |
| Numbers, specs and definitions are strong cues [C] (skill evidence base); decorative statistics are not | CS-3 stays the heaviest case criterion (20); CALC-2 + CALC-3 = 28 points of calculator weight; vanity numbers explicitly fail |
| A headline/title that answers the query [L] | CS-1 kept at 14 and moved to answer_def; calculator U1 at 10 with a type-specific c1 |
| Quotes and methodology are [C] contested / [P] | CS-5 trimmed 8→7; CS-7 kept at 6 as a differentiator (no competitor has it) |
| Freshness is strong [C] but SE templates show no dates | U9 kept (4 in case studies, 5 in calculators: model version and data vintage are part of the method's credibility) |
| No page-type citation data exists | All weights are priors; validate quarterly (judge-protocol §6) |

---

## 4. Proposed logic

Conventions follow `page-types.md`.
- U1–U10 are used as defined in `scoring-framework.md`. Only type-specific *interpretations* are added here.
- Checks → level ceiling = round(5 × passes ÷ applicable checks); level 5 needs all checks to pass. When torn between two levels, pick the lower.
- New criterion families: CS-1 → answer_def (changed from "other") · CS-2, CS-4, CS-6, U3 → other · CS-3, CS-5, CS-7 → proof (unchanged) · CALC-1 → evidence · CALC-2, CALC-3 → specs · CALC-4 → answer_def · CALC-5 → comparison.

### 4.1 Case study / customer story: logic v1.1 (revises §8)

**What AI extracts.** A case study gets cited for prompts like "examples of [industry] doing X", "how did [customer] achieve Y" and "does [offer] work / what results". The engine needs:
1. a one-sentence outcome claim: customer + result with unit + period + named offer
2. the customer profile (sector, scale, location)
3. what was deployed and how
4. a quotable customer statement
5. how the number was measured
6. a date

Engines quote text, not video, stat-card images or tab widgets.

**Must-haves**
- Outcome-led H1 or summary.
- A 40–150-word answer-shaped summary in text.
- ≥ 1 customer outcome with unit, baseline and period.
- Narrative in HTML text.
- Products named, with their role.
- A visible date.

**Common failures (SE corpus)**
- Slogan H1.
- Story only in video, client-rendered components or tabs.
- Vanity stat cards.
- Precise metric only in the meta description.
- Placeholders.
- No date.
- No method.
- Product grid without roles.
- "Read more" CTAs.

| ID | Criterion | W | Checks (pass definition) | Anchor notes | Family | Rationale / evidence |
|---|---|---|---|---|---|---|
| CS-1 | Outcome-led title + answer-shaped summary | 14 | c1 Title/H1 names the customer (or anonymised type) · c2 Title/H1 states the outcome or the solved problem, not a slogan · c3 a 40–150-word prose summary in text within the first ~150 body words · c4 the summary covers ≥ 4 of who / problem / solution (named) / result / timeframe · c5 the summary contains a quantified result with a timeframe (a citable "X achieved Y in Z with W" sentence) | 5 = all, and the summary sentence is quotable verbatim | answer_def (**changed**) | Answer-first and headline–query match [L]; ~44% of ChatGPT citations come from the first 30% of a page [L]; R9, R10 |
| CS-2 | Customer profile | 8 | c1 industry/sector explicit in body · c2 size/scale (sites, MW, assets, area, staff) · c3 country/region · c4 application/scope of the deployment | Meta-only facts fail | other | Context lets engines match "examples in [industry/country]" fan-outs [P] R10 |
| CS-3 | Quantified results with baseline & timeframe | 20 | c1 ≥ 1 customer outcome with unit (energy, cost, CO2e, uptime, time) · c2 ≥ 2 distinct quantified outcomes · c3 baseline/reference stated (before/after, % vs a named year) · c4 timeframe/period (since YYYY, annualised, over N years) · c5 result explicitly attributed to the named offer · c6 the primary outcome leads (title/summary/first stat) | Vanity or context numbers (years of relationship, floor area, parts) and targets ("aiming to") **fail** c1/c2. 5 needs all six plus a specific (not family-level) attribution | proof | Specs and numbers are the strongest cues [C]; decorative stats don't help [C]; no competitor states a baseline (§3.2) |
| CS-4 | Challenge → solution → results narrative in text | 8 | c1 specific challenge stated · c2 what was deployed, where, how, by whom (partner) · c3 results stated in text · c4 segmented under labels/headings, and each section names the customer | Tab labels with no panel text = fail | other | Self-contained passages +56% factual correctness [C]; Bing hidden-content guidance [O] R5 |
| CS-5 | Attributed customer quote | 7 (was 8) | c1 ≥ 1 direct customer quote in text · c2 speaker named · c3 role and organisation · c4 substantive content (reason, fact or outcome), not generic praise | Vendor-employee quotes don't count | proof | Quotation +43% in GEO 2024 [C] but did not replicate on newer models [C]; trimmed by 1 |
| CS-6 | Offers named, with their role | 7 (was 8) | c1 exact commercial names (™ consistent) · c2 the role of the main offer(s) in the project is explained in text · c3 each offer presented as a named card/link (destination named) | 0 none · 1 family only ("EcoStruxure") · 2 named in a list/cards only · 3 named + role of the main offer · 4 c1–c3 · 5 + module/version precision | other | Entity clarity for "what product did X use" fan-outs [P]; card grids pass c1/c3 only |
| CS-7 | Metric methodology / verifiability | 6 | c1 how the result was measured (metering, bills, M&V protocol, GHG Protocol scope) · c2 measurement boundary/period · c3 data source or third-party verification | | proof | Evidence-backed claims win pairwise (OR 2–46) [C]; R11 [P]; a differentiator vs competitors |
| U2 | What / Who / When / Outcome | 4 (was 6) | Standard. Case interpretation: what = offer deployed; who = customer/segment; when = scenario; outcome | | answer_def | Overlaps CS-1/CS-2, so reduced |
| U3 | Extractable structure & self-containment | **8 (new)** | Standard. Case interpretation: **c5 fails when the narrative, quote or results exist only in video, stat-card images, carousels, tab widgets or a PDF.** c3 fails when there is no prose at all | If c5 fails → U3 ≤ 2 | other | The dominant SE failure (4 of 6 pages); R1, R5, R12, R13 |
| U7 | Neutral tone | 5 (was 6) | Standard. Slogan headings and promo inserts inside the story fail c3; c4 usually N/A | | tone | Promotion hurts [C] |
| U8 | Entity clarity & consistency | 5 (was 6) | Standard. Check customer spelling, product names, figures across stat cards/prose/meta | G1 if stat card and prose disagree | — | |
| U9 | Freshness | 4 | Standard. Case interpretation: c1 publish date **or** project/results date visible; c2 results data ≤ 3 years old or dated; c3 usually N/A; c4 reviewed in the last 12 months | | freshness | Recency strong [C]; undated stories can't be placed in time |
| U10 | Stage fit & next step | 4 (was 6) | Standard; descriptive CTA to the solution/range | | commercial | Weak evidence that CTAs drive citation |

**Sum = 100.**

**Effective weights**
- At Evaluation: CS-3 24.96 · CS-1 11.23 · CS-5 8.73 · CS-7 7.49 · CS-2 7.13 · CS-4 7.13 · U3 7.13 · CS-6 6.24 · U7 4.46 · U8 4.46 · U9 3.92 · U10 3.92 · U2 3.21.
- At Consideration: CS-3 22.3 · CS-1 13.01 · CS-5 7.81 · CS-7 6.69.

**Changes vs v1.0, with reasons**
1. **+U3 (8).** The pilot shows hidden or video-led narratives are the main failure, and v1.0 had no criterion that sees them. The rule is kept to the *content decision* (no text equivalent). Rendering itself stays out of scope.
2. **CS-1 → answer_def family.** CS-1 is the case-study form of U1, so stage multipliers should treat it the same way. Effect: −0.9 points at Evaluation.
3. **CS-5 −1, CS-6 −1, U2 −2, U7 −1, U8 −1, U10 −2 to fund U3.**
   - CS-5: quote evidence is contested.
   - U2: overlaps CS-1 and CS-2.
   - U10: weakest evidence.
4. **Explicit pass definitions.** Vanity numbers and targets fail CS-3. Meta-only facts fail. Card grids reach at most 2 on CS-6.
5. **G7** and **placeholder_text** (below).

**Pilot effect (v1.0 → v1.1)**
- Scores move −4 to 0 points.
- The ranking is unchanged.
- U3 mainly separates text stories (Blackstone 2, YVR 2) from widget stories (McLaren 0, Massmart 1).

**Natural stages**
- **Evaluation** is the default.
- **Consideration** for approach showcases ("examples of airports…") and brand-partnership stories.
- **Decision** for references backing a specific purchase.
- Mismatch: **Awareness**.

**Gates, caps and penalties**

| ID | Trigger | Effect | Justification |
|---|---|---|---|
| **G7 (new)** | No quantified customer outcome anywhere in the body text. Targets, vanity numbers and meta-only numbers don't count | overall ≤ 59 | A story with no outcome is a testimonial. Without the gate, a well-written outcome-free story (CS-3 and CS-7 = 0, everything else maxed) can reach about 68 at Evaluation and about 71 ("Good") at Consideration. Parallel to G3 for PDPs. Concrete facts are the strongest cue [C] |
| G6 (clarify) | Add explicitly: "story only in a video, image or PDF with no text summary/transcript" | U3 ≤ 2, ≤ 59 | R5, R12, R13 |
| G2 | The page never states what was delivered or achieved | ≤ 39 | Triggered on McLaren |
| **placeholder_text (new penalty)** | Template residue published ("ZZ_", lorem ipsum, "Paragraph Title", placeholder alt text) | −2 | Visible to every crawler; damages entity clarity and trust; found on 2 of 6 stories. [P]/QA hygiene |
| cta_overload, fluff_density | Standard | −1 / −2 | Count CTAs manually on markdown corpora. Compute fluff on body text, not title, meta or footer |

**Recommendation templates (case study).** Never invent metrics. Use `[VERIFY]` and `[SME]`.

**R-CS1: outcome sentence + summary.** Place it right under the H1.
- BEFORE: H1 "Innovation and artisanship in every cup"
- AFTER: H1 "[Customer] [verb] [metric + unit] in [period] with [exact offer]". Then a 60–120-word summary covering who (sector, size, country), problem, what was deployed and where, the result with baseline and period, and the partner.
- Owner: content owner.

**R-CS3: metric block.** Format each outcome as: metric · unit · baseline (year/value) · period · scope · source.
- Example skeleton: "Annual energy cost: −R15 million (ZAR) per year vs [baseline year] across [N] stores [VERIFY]".
- Move meta-only facts into the body (Blackstone "$60 million… over six years" [VERIFY]).

**R-CS4: text equivalent of the story.**
- Write challenge, solution and results as HTML text under descriptive H2s, e.g. "How Massmart standardised building management across 250 stores".
- Add a transcript or summary for the video.
- Never leave tab panels empty in HTML.
- Ask SE Digital to server-render QDS components.

**R-CS5: quote.** Use the existing approved testimonial in HTML text, with name, role and organisation. Prefer a quote that contains a reason or a result.

**R-CS6: role per offer.** Format: "[Offer] — [what it did in this project] — [scope]". Example: "EcoStruxure Resource Advisor — normalises energy and utility data across 20+ portfolio companies".

**R-CS7: method line.** "Savings measured from utility bills, [period], normalised for [weather/occupancy]; verified by [party]" [VERIFY with customer].

**R-U9: dates.** Show "Published / Updated" and "Results period".

**R-QA: placeholders.** Purge "ZZ_*" placeholders and fix entity spelling (NetBotz, Zicaffè, "contactors" [SME]).

**Intake-sheet fields (case study, adds to §B)**
- Customer name, approval to name, industry, size/scale, country.
- Project dates (start, go-live, results period).
- Primary outcome: metric, unit, baseline (value, year), period, scope.
- Secondary outcomes.
- Measurement method and verifier.
- Offers used, with the role of each.
- Partner/integrator.
- Approved quote: speaker, role, approval Y/N.
- Video URL and whether a transcript is available (Y/N).
- Template (QDS campaign / legacy).
- Publish/update date.
- Related solution page.

### 4.2 Calculator / TradeOff Tool: logic v1.0 (new type `calculator`)

**What AI extracts.** Engines can't run the tool. They cite the knowledge around it [P R15; O R3/R5]:
- what is calculated and from which drivers
- the formula or logic
- the assumptions with values and sources
- typical results and benchmarks (e.g. typical PUE, cost per MW)
- a worked example
- definitions of inputs and metrics
- limits of validity
- the model version and date

Prompts are mostly Education to Evaluation ("how to calculate…", "how much does… cost", "what is a typical…", "X vs Y TCO").

**Must-haves**
- The answer kernel in the intro: what is calculated, its drivers and the core relationship.
- A "How it works" method.
- An assumptions list with numbers and data vintage.
- One worked example in text or a table.
- Typical ranges.
- Input and output definitions.
- Scope and limitations.
- Model version and date.

**Common failures**
- Intro only invites people to use the tool.
- Tool knowledge exists only inside the iframe/JS app.
- Results shown only as charts.
- Related-content grid instead of explanation.
- Near-duplicate sibling pages.
- Generic CTAs.
- Undated models.

| ID | Criterion | W | Checks (pass definition) | Anchor notes | Family | Rationale / evidence |
|---|---|---|---|---|---|---|
| U1 | Answer-first & prompt alignment | 10 | Standard c1–c5. **Calculator interpretation of c1:** the opening states what is calculated **and** the drivers/inputs or the core relationship ("utility input power depends on IT load, safety margin and PUE"). A bare "Use this tool to estimate X" passes c3 only | | answer_def | Answer-first [L]; title–query similarity [L] R9 |
| U2 | What / Who / When / Outcome | 4 | Standard; outcome = the decision the result informs, stated concretely | | answer_def | Context test (SE Toolkit) |
| CALC-1 | Method / formula in crawlable text | 16 | c1 calculation logic stated (formula or step-by-step: inputs → intermediate → outputs) · c2 variables named with units · c3 model provenance stated (who built it; which white paper/standard it implements) · c4 scope/limits of validity · c5 a simple case could be reproduced by hand (constants given) | 5 = all; a link to a white paper without saying the tool implements it fails c3 | evidence | Method in text is the citable asset (R15 [P]; EPA/Omni exemplars). Not in text means not extractable (R1, R2, R6) |
| CALC-2 | Assumptions & default values | 13 | c1 key assumptions listed in text · c2 each has a value + unit · c3 source **and** vintage/year of the assumption data · c4 default scenario values stated · c5 regional/currency/price-year basis stated (N/A if region-independent) | | specs | Concrete numbers are the strongest cue [C]; sourced statistics [C] R8; EPA exemplar |
| CALC-3 | Worked example & representative results | 15 | c1 ≥ 1 complete example (inputs → outputs with units) in text/table · c2 typical ranges/benchmarks · c3 key drivers/sensitivity quantified ("power is 50.6% of CapEx in the default case") · c4 results given in text/table, not only chart/UI | Example numbers must come from the tool or an SME [VERIFY] | specs | Answers "how much / typical" prompts directly; all exemplars have one (R15, §3.2) |
| CALC-4 | Inputs & outputs defined | 7 | c1 every required input listed · c2 inputs defined (meaning, how to obtain, unit, range) · c3 output metrics defined (PUE, emission factor, TCO) · c4 acronyms expanded at first use | | answer_def | Definitions double the chance of being a cited passage [L]; glossary-type fan-outs |
| CALC-5 | Interpretation & decision guidance | 6 | c1 how to read the result (good vs poor) · c2 "choose/do X if…" or trade-off rule · c3 levers to improve the result named · c4 uncertainty/limitations of interpretation | | comparison | Converts a number into an answer for comparison prompts; Bing Q&A guidance [O] |
| U3 | Extractable structure & self-containment | 6 | Standard. **c5 fails when tool knowledge exists only in the interactive widget/iframe/JS.** c2 expects a list/table of inputs, assumptions or results | If c5 fails → ≤ 2 | other | R1–R6 |
| U5 | Evidence, attribution & expertise | 5 | Standard; c3 (quote) usually N/A. c2 includes method standards (e.g. PUE definition standards, GHG Protocol) | | evidence | Provenance of the model = expertise visible in content |
| U7 | Neutral tone | 4 | Standard; c4 applies to make-vs-buy tools (both options named fairly) | | tone | Promotion hurts [C] |
| U8 | Entity clarity & consistency | 4 | Standard; tool naming (TradeOff Tool™), sibling-tool names, figures consistent with the tool | Contradiction → G1 | — | |
| U9 | Freshness | 5 | Standard. **Calculator interpretation:** c1 model version/date visible; c2 data vintage ≤ 2 years or stated; c4 reviewed yearly | | freshness | Recency strong [C]; cost and emission factors age fast |
| U10 | Stage fit & next step | 5 | Standard; descriptive CTAs ("Open the power sizing calculator", "Read White Paper 3: Calculating Total Power Requirements") | | commercial | |

**Sum = 100.**

**Effective weights**
- At Evaluation: CALC-3 19.51 · CALC-2 16.91 · CALC-1 13.88 · U1 7.81 · CALC-5 7.29 · CALC-4 5.46 · U3 5.20 · U9 4.77 · U10 4.77 · U5 4.34 · U7 3.47 · U8 3.47 · U2 3.12.
- At Consideration: CALC-1 16.19 · CALC-3 15.18 · CALC-2 13.16 · U1 9.20 · CALC-5 8.28.

**Natural stages**
- **Consideration** and **Evaluation**.
- **Education** for "how to calculate" tools (power sizing, emission factor).
- Mismatch: **Awareness**.
- Add "Calculator / tool" to the buyer-journey type × stage matrix.

**Classifier addition (page-types §15):** "The primary element is an interactive widget that computes outputs from user inputs → Calculator / tool". Score the parent page's text. An iframe at a separate URL is a separate document.

**Gates, caps and penalties**

| ID | Trigger | Effect | Justification |
|---|---|---|---|
| **G8 (new)** | CALC-1, CALC-2 and CALC-3 are all level 0: the method, assumptions and example results are all absent from crawlable text | overall ≤ 39 and U3 ≤ 2 | A calculator page's only citable value is the knowledge behind the tool; tone, links and a good title can't compensate. Aligned with G3 (PDP without specs ≤ 40). Set to 39 so the band reads **Poor**. Not binding in the pilot (raw 12–18) but prevents a polished intro plus card grid from reaching Average. Evidence: R1–R6 [O/L], R15 [P] |
| G1 | The tool or page contradicts itself (e.g. two "typical PUE" values) | U8 = 0; ≤ 59 | Triggered in sensitivity run 33R |
| boilerplate | > 40% of body text shared with a sibling tool page | −2 | Pages 34/36 share 57–65% |
| cta_overload | ≥ 3 generic CTAs ("Start calculation", "Calculate now", "Learn more", "Explore now") | −1 | Template-wide |

**Recommendation templates (calculator).** Add these as a standard crawlable "About this calculator" module in the parent-page template. The tool team already holds the text.

**R-C1: answer kernel intro (40–60 words).**
- BEFORE: "Use this TradeOff Tool to estimate the power required by a data center with traditional, or AI/HPC servers."
- AFTER: "The data center power sizing calculator estimates the IT load of a server mix (traditional CPU and AI/HPC GPU servers, storage, networking) and the utility input power needed to support it, which is IT load plus a safety margin multiplied by PUE. Typical inputs: server quantity and mix, storage, PUE and a 10–20% safety margin." [VERIFY with the Data Center Science Center]

**R-C2: "How the calculator works".**
- Write the formula or steps in text, for example "IT load = Σ(servers × W/socket × sockets) + storage (W/TB × TB) + networking (% of server power)…" [VERIFY].
- State the model provenance: "Based on mathematical models by the Schneider Electric Data Center Science Center; method described in White Paper 3."

**R-C3: "Key assumptions" list.** Copy the tool's list and add each value's source and year. For example: CPU server 290 W/socket; GPU server 1,300 W/socket (8-GPU H100-class server, 2024); external storage 0.8 W/TB (2024 SSD); networking 10% (CPU) / 8.8% (GPU); mainframe 10,000 W. [VERIFY current values]

**R-C4: "Worked example" table.** Use the default scenario: 1,000 traditional + 10 AI/HPC servers, 20% margin, PUE 1.40 → 790 kW IT capacity, 1,110 kW utility input. Breakdown: CPU servers 38%, physical infrastructure 29%. [VERIFY]
- Capital-cost tool: give the default case's MW, density and cooling with cost per MW and the power/cooling split. [SME]

**R-C5: "Typical results and how to read them".** Give the typical PUE range with its source. **First resolve the 1.4 vs 1.8 contradiction** inside the tool. Add "If your result is above X, consider…" and levers.

**R-C6: definitions.** Turn the tool's input glossary into an HTML definition list.

**R-C7: version line.** Format: "Model version 4, updated September 2024; data year 2024; next review [date]". Update the data, not just the date.

**R-C8: de-duplicate siblings.** For the single- and three-phase pages, keep one shared method section that states the differences, or keep two pages each with phase-specific assumptions and examples.

**R-C9: descriptive CTAs.** Examples: "Open the power sizing calculator", "Read White Paper 3: Calculating Total Power Requirements".

**R-Tech (SE Digital, out of scope for the score):**
- Server-render the iframe app's explanatory panels, or inline them on the parent page.
- Consider WebApplication schema matching the visible text (low priority [O R3]).

**Intake-sheet fields (calculator)**
- Tool name and canonical short name.
- Tool URL and iframe URL.
- Model version and date.
- Owner team.
- Methodology source (white paper number and title).
- Core formula/logic (SME text).
- Input list with units, ranges and defaults.
- Output metrics with definitions.
- Assumptions with value, unit, source and data year.
- Default scenario and its outputs.
- Typical result ranges with source.
- Region/currency/price-year basis.
- Known limitations.
- Sibling tools.
- Target prompts.
- Review cadence.

---

## 5. Pilot scores & calibration

The judge followed `judge-protocol.md`:
- binary checks, each with a verbatim quote or NOT FOUND
- the proposed level
- scoring with `geo_score_calc.py --weights pilot/weights_casecalc_draft.json`

All **665 checks** were verified by script as substrings of the corpus file, with whitespace and case normalised. **0 pass-quotes failed.** The page's natural stage is used.

### 5.1 Results

| Page | Type | Stage | Score | Band | Raw | Gates/penalties | Top 3 gaps (recoverable effective points) |
|---|---|---|---|---|---|---|---|
| 19 McLaren Racing | Case study | Consideration | **9** | Poor | 11.4 | G2, G7; placeholder −2 | CS-3 (22.3), CS-1 (10.4), CS-5 (7.8) |
| 20 Blackstone | Case study | Evaluation | **49** | Average | 50.5 | CTA −1 | CS-3 (15.0), CS-1 (9.0), CS-7 (7.5) |
| 21 Massmart | Case study | Evaluation | **32** | Poor | 32.6 | CTA −1 | CS-3 (15.0), CS-5 (8.7), CS-7 (7.5) |
| 22 Vancouver Airport | Case study | Consideration | **54** | Average | 54.3 | — | CS-5 (7.8), CS-7 (5.4), CS-2/CS-4/U3 (4.5 each) |
| 23 Rubis Photosol | Case study | Evaluation | **26** | Poor | 28.0 | G7; placeholder −2 | CS-3 (25.0), CS-5 (8.7), CS-7 (7.5) |
| 24 Zicaffè | Case study | Evaluation | **9** | Poor | 10.8 | G7; fluff −2 | CS-3 (25.0), CS-1 (9.0), CS-5 (8.7) |
| 31 Emission factor calc. | Calculator | Consideration | **17** | Poor | 17.7 | G8; CTA −1 | CALC-1 (16.2), CALC-3 (15.2), CALC-2 (13.2) |
| 32 Capital cost calc. | Calculator | Evaluation | **11** | Poor | 11.8 | G8; CTA −1 | CALC-3 (19.5), CALC-2 (16.9), CALC-1 (13.9) |
| 33 Power sizing calc. | Calculator | Consideration | **16** | Poor | 17.2 | G8; CTA −1 | CALC-1 (16.2), CALC-3 (15.2), CALC-2 (13.2) |
| 34 1-phase UPS efficiency | Calculator | Evaluation | **14** | Poor | 16.5 | G8; CTA −1; boilerplate −2 | CALC-3 (19.5), CALC-2 (16.9), CALC-1 (13.9) |
| 35 Edge UPS fleet | Calculator | Evaluation | **13** | Poor | 14.0 | G8; CTA −1 | CALC-3 (19.5), CALC-2 (16.9), CALC-1 (13.9) |
| 36 3-phase UPS efficiency | Calculator | Evaluation | **14** | Poor | 16.5 | G8; CTA −1; boilerplate −2 | CALC-3 (19.5), CALC-2 (16.9), CALC-1 (13.9) |
| *21R Massmart, rendered text (sensitivity)* | Case study | Evaluation | *55* | *Average* | 56.3 | CTA −1 | CS-3 (10.0), CS-5 (8.7), CS-7 (7.5) |
| *33R Power sizing + iframe text (sensitivity)* | Calculator | Consideration | *59* | *Average* | 70.6 | **G1 cap 59** (typical PUE 1.8 vs 1.4); CTA −1 | CALC-5 (5.0), U1 (3.7), U8 (3.7) |

**Criterion levels per page**

Each cell shows the level, with the effective weight in brackets.

| Case | 19 | 20 | 21 | 22 | 23 | 24 | 21R |
|---|---|---|---|---|---|---|---|
| CS-1 | 1 (13) | 1 (11) | 2 (11) | 4 (13) | 2 (11) | 1 (11) | 4 |
| CS-2 | 2 | 4 | 4 | 2 | 4 | 1 | 4 |
| CS-3 | 0 (22) | 2 (25) | 2 (25) | 4 (22) | 0 (25) | 0 (25) | 3 |
| CS-4 | 0 | 4 | 0 | 2 | 1 | 0 | 4 |
| CS-5 | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| CS-6 | 2 | 4 | 2 | 2 | 3 | 2 | 4 |
| CS-7 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| U2 | 1 | 4 | 4 | 4 | 3 | 1 | 4 |
| U3 | 0 | 2 | 1 | 2 | 2 | 1 | 4 |
| U7 | 0 | 2 | 0 | 2 | 3 | 0 | 2 |
| U8 | 2 | 4 | 4 | 4 | 4 | 2 | 4 |
| U9 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| U10 | 1 | 3 | 3 | 4 | 2 | 1 | 3 |

| Calculator | 31 | 32 | 33 | 34 | 35 | 36 | 33R |
|---|---|---|---|---|---|---|---|
| U1 | 3 | 2 | 3 | 3 | 3 | 3 | 3 |
| U2 | 2 | 3 | 3 | 3 | 3 | 3 | 3 |
| CALC-1 / 2 / 3 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 | 4/4/4 |
| CALC-4 | 1 | 0 | 0 | 1 | 0 | 1 | 5 |
| CALC-5 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| U3 | 2 | 2 | 2 | 2 | 2 | 2 | 4 |
| U5 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| U7 | 3 | 3 | 3 | 3 | 3 | 3 | 4 |
| U8 | 4 | 1 | 4 | 4 | 2 | 4 | 0 (G1) |
| U9 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| U10 | 2 | 2 | 2 | 2 | 2 | 2 | 3 |

### 5.2 Calibration notes

**1. Spread and discrimination.**
- **Case studies: 9–54** (45-point spread). The ranking matches expert expectation on server text: YVR ≈ Blackstone > Massmart > Rubis > McLaren ≈ Zicaffè.
  - YVR has the best citable outcome sentence.
  - Blackstone has the only complete text story and quote.
- **Calculators: 11–17.** This narrow spread is **expected and correct**: the six pages are the same template with no method text. The only variations are intro quality (U1/U2), naming (U8) and duplication.
- **Discrimination on the content axis is shown by the sensitivity runs.**
  - Calculator: 33 → 33R goes from 16 to 59, or 71 raw without the contradiction.
  - Case study: 21 → 21R goes from 32 to 55.

**2. Band calibration.**
- The pilot medians are below the 35–60 "typical un-optimised" target: about 29 for stories and about 14 for calculators. On rendered text, 21R lands at 55, inside the target. The low medians therefore reflect missing server text, not judge harshness.
- **Decision needed (§7 Q1):** should production score server HTML (what non-JS AI crawlers get) or rendered text (what Google and Gemini get)?

**3. Before/after (v1.0 → v1.1, case studies).**

| Page | 19 | 20 | 21 | 22 | 23 | 24 | 21R |
|---|---|---|---|---|---|---|---|
| v1.0 | 13 | 52 | 34 | 56 | 29 | 9 | 54 |
| v1.1 | 9 | 49 | 32 | 54 | 26 | 9 | 55 |

- The ranking is unchanged.
- The differences come from U3 (which rewards text stories and penalises widget stories), the placeholder penalty and G7. G7 is non-binding here because both pages are already below 59.
- v1.1 lifts the rendered Massmart page (+1) and lowers the hidden-story pages, which is the intended direction.

**4. Stage sensitivity.** The same judgements were scored at all five stages.
- Stories move by ≤ 9 points. The biggest move is Rubis: 35 at Awareness vs 26 at Evaluation, because missing proof weighs more at Evaluation.
- Calculators move by ≤ 6 points.
- No rank inversions, and no counter-intuitive effects. Evaluation-stage tools sit 2–3 points below Consideration-stage tools because the spec-family multiplier (1.5) increases the weight of the missing assumptions and examples. This is intended.

**5. Non-discriminating criteria in this pilot, and why each is kept.**
- **CS-7 (0–1 everywhere).**
  - Kept at 6.
  - It is a differentiator: no competitor exemplar has it either.
  - It carries the verifiability evidence.
  - Review after 30+ pages.
- **U9 (0 on 5/6 stories; 0 on all calculators).**
  - Kept.
  - Freshness evidence is strong [C], and the gap is template-wide (no date field), so it should keep showing up until the template changes.
- **CALC-1/2/3/5 and U5 (0 on all calculators).**
  - Kept.
  - They define the type, and the zeros are the finding.
  - The sensitivity run shows they move to 2–5 when the content exists.
- **U7 = 3 and U10 = 2 (constant on calculators).**
  - Kept at low weights (4 and 5).
  - They will separate pages when tools add vendor-biased make-vs-buy framing or descriptive CTAs.

**6. Gates.**
- G7 and G8 are **not binding** in the pilot, because the raw scores are already below their caps. They act as safety nets for future pages with polished prose but no outcomes or method.
- G1 *was* binding in 33R, through a real contradiction in SE's tool text. It is worth fixing before any content is mirrored.
- G2 on McLaren is redundant with the raw score. That is acceptable.

**7. Rule clarifications adopted during calibration.** These are wording changes, not weight changes, so no second re-score was needed beyond the v1.0 → v1.1 comparison.
- Calculator U1 c1 needs drivers or a relationship, not just "use this tool". This lowered 32 by 1 level on U1.
- U3 c3 fails when there is no prose at all. Otherwise empty pages would pass "short paragraphs".
- CS-3 fails vanity numbers and targets.
- Facts that appear only in the meta description fail content checks. They are reported as quick wins instead.
- Count fluff and CTAs on body text.

**8. Judge variance.** A single judge pass was used. Borderline items for a 3-run median in production:
- U7 on thin pages: 0 vs 1.
- CS-6 card-only pages: 2.
- YVR CS-3: 4 vs 5.

---

## 6. Proposed weights JSON fragment

This is to merge into `assets/weights.json`. Run `--selftest` afterwards; it passes on the draft file. Note that it **replaces** `case_study`.

```json
{
  "families": {
    "answer_def": ["U1", "U2", "GLO-1", "CS-1", "CALC-4"],
    "evidence":   ["U5", "ART-3", "DOC-8", "CALC-1"],
    "specs":      ["PDP-1", "PDP-3", "PDP-4", "RNG-6", "CAT-4", "DOC-3", "U4", "GLO-2", "CALC-2", "CALC-3"],
    "comparison": ["CMP-1", "CMP-2", "CMP-3", "CAT-1", "CAT-2", "CAT-3", "RNG-1", "RNG-2", "PDP-6", "CALC-5"]
  },
  "page_types": {
    "case_study": {"CS-1": 14, "CS-2": 8, "CS-3": 20, "CS-4": 8, "CS-5": 7, "CS-6": 7, "CS-7": 6,
                   "U2": 4, "U3": 8, "U7": 5, "U8": 5, "U9": 4, "U10": 4},
    "calculator": {"U1": 10, "U2": 4, "CALC-1": 16, "CALC-2": 13, "CALC-3": 15, "CALC-4": 7, "CALC-5": 6,
                   "U3": 6, "U5": 5, "U7": 4, "U8": 4, "U9": 5, "U10": 5}
  },
  "gates": {
    "G6": {"cap": 59, "max_level": {"U3": 2}, "desc": "Core content only in gated asset/image/PDF/video without an HTML text equivalent"},
    "G7": {"cap": 59, "desc": "Case study with no quantified customer outcome anywhere in the text"},
    "G8": {"cap": 39, "max_level": {"U3": 2}, "desc": "Calculator/tool page: method, assumptions and example results all absent from crawlable text (CALC-1, CALC-2, CALC-3 all level 0)"}
  },
  "penalties": {"placeholder_text": 2}
}
```

**Script and alias notes**
- Add the aliases `"calculator"`, `"tool"`, `"tradeoff tool"` and `"interactive tool"` → `calculator` to `TYPE_ALIASES` in `geo_score_calc.py`. Without them, type "calculator" works only through the fallback.
- Add a calculator row to the type × stage matrix in `buyer-journey.md`.
- Add §8 changes and a new §16 "Calculator / tool" to `page-types.md`.
- Add G7, G8, the clarified G6 and placeholder_text to `scoring-framework.md` §4.

**Checker notes** (`geo_content_check.py`)
- Strip `<!-- -->` header comments before computing the lead.
- Exclude the site footer.
- Detect plain-text CTAs.
- Add a "ZZ_ / lorem / placeholder" detector.

---

## 7. Open questions & risks

1. **Scoring mode: server HTML vs rendered DOM.** This is the largest driver of scores for both types: +23 points on Massmart and +43 raw on power sizing.
   - Recommendation: score the content as rendered (content quality), and add a mandatory **"server-text parity" check**. If rendered text exceeds server text by a material amount (e.g. > 30%), report both scores and route to SE Digital.
   - Until decided, the pilot scores reflect what GPTBot, ClaudeBot and PerplexityBot receive. That is the right view for ChatGPT, Claude and Perplexity, and pessimistic for Google, Gemini and AI Mode, which render JS and may associate iframe content with the parent page (R2, R4).
   - Evidence that OpenAI may start rendering JS is unconfirmed (R7). Re-check quarterly.
2. **Iframe at a separate URL.** Google may fold it into the parent; other engines won't. The content fix (mirror the method on the parent page) is valid either way.
3. **Evidence strength.** No study isolates case-study or calculator citation rates. Element advice is mostly [P], and vendor statistics (e.g. "45% citation rate for case studies") are unsourced and **not** used.
   - Validate with a Profound prompt panel before and after fixing 2–3 pages per type: ≥ 7 runs per prompt per engine, with control pages.
4. **Stage choice.** YVR and McLaren were scored at Consideration and the rest at Evaluation. Stage moves scores by up to 9 points. The intake sheet should make stage mandatory, with type defaults (case study → Evaluation; calculator → Consideration or Evaluation).
5. **Customer approvals.** CS-3, CS-5 and CS-7 fixes depend on customers approving metrics, baselines and quotes. The intake sheet should capture approval status. Recommendations must use [VERIFY] placeholders, and never invent numbers.
6. **Tool-text quality.** The 33 tool contradicts itself on typical PUE (1.8 vs 1.4), and the iframe design system leaks placeholder strings ("Lorum ipsum", "This is an option") into the DOM. Audit all TradeOff Tools before mirroring their text. 32's default cost scenario does not state its MW basis in the visible results, so an SME must supply it.
7. **Data currency in assumptions.** Values such as 2024 GPU and SSD power figures age quickly. U9 for calculators should be judged on data vintage, not just the page date. The tool team needs a yearly review cadence.
8. **Possible contradiction to check.** Massmart says "155 BMS systems" in server text and "more than 250 of their stores" in rendered text.
9. **Thin-page tone scoring.** U7 scores 0 when there is no informational voice at all (McLaren, Zicaffè). That conflates "absent" with "promotional". It has a small effect (≤ 6 points); keep it under review in κ calibration.
10. **Single judge, single rater.** κ against human raters (protocol §6) has not been measured yet. The pilot levels should be reviewed by a content owner and a data-center SME before these weights are locked as v1.1.
11. **Personal data.** The judge JSONs quote names and roles that appear on public pages (customer testimonial attribution). Keep them out of shared summaries where the role is sufficient.

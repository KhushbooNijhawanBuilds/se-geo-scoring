# Solution & Service Pages: GEO Scoring Logic, Corpus Audit and Pilot (draft SOL v1.1 + SVC v1.0, 2026-10-19)

**Scope.** Two page types: **Solution page** (corpus #07–12) and **Service page** (#37–42).
**Builds on.** `skill/geo-research` v1.0: U1–U10, the gates, the judge protocol, and `page-types.md` §12 (SOL v1.0).
**Skill folder.** Not edited. Everything here is a proposal.

**Pilot artifacts.**
- Judge JSONs: `research/type-analysis/pilot/NN_judge.json` (NN = 07–12, 37–42).
- Score cards: `pilot/scorecards/NN_scorecard.md`.
- Merged weights: `pilot/weights_sol_svc_v2.json`.

The scratch weights for v1 and v2 are in the session scratchpad (`agents/solution_service/`).

**Evidence labels** (as in the skill):
- **[C]** controlled
- **[L]** large correlational / survey
- **[O]** official platform guidance
- **[P]** practitioner
- **[SE]** SE house guidance

---

## 1. Executive summary

**1. SE solution and service pages are hubs, not answers.** All 12 pages use the same CMS pattern:
- a slogan H1, a hero video and tabbed navigation;
- carousels and card grids of 10–15-word teasers, often cloned and truncated with "...";
- stat tiles;
- a global "Need help?" product-sales block.

Body text is about 220–950 words per page (checker count minus about 60 template words), most of it teaser copy. An AI engine can name the offer but cannot explain:
- what it is;
- how it works;
- what it includes;
- for whom, under what terms;
- with what proof.

**2. Pilot scores.** Final logic, natural stage per page:

| Type | Scores | Mean | SD | Bands |
|---|---|---|---|---|
| Solution | 14–37 | 26.8 | 7.9 | all Poor |
| Service | 8–39 | 26.0 | 9.7 | all Poor |

These scores are consistent with the sibling analyses: range 12–36, software 22–30, calculators 11–17.

To check that the logic is not simply harsh, two competitor exemplars were scored *indicatively* (non-verbatim). Both land in Average:
- Eaton UPS services: 52.
- Vertiv AI Hub: 43.

They have exactly what SE lacks: numeric response commitments, technician numbers, eligible models, and kW-per-rack reference-design tables.

**3. Solution logic (SOL v1.1), 14 criteria.** Revised from v1.0. Main changes:
- **SOL-2** (how it works) absorbs SOL-3 (components) and moves to the *specs* family.
- **SOL-6 FAQ** is retired in favour of format-agnostic **U6** fan-out coverage.
- New **SOL-7 Applicability, scope & fit** (10).
- New **SOL-8 Implementation path & delivery model** (5).
- **U3** added (6) because template extraction failures are the #1 SE issue.
- Problem framing (**SOL-1**) drops from 12 to 7 and moves to the *evidence* family, so it still counts at Awareness.

**4. Service logic (SVC v1.0, new), 13 criteria.** Two variants:

| Variant | For | SVC-1 | SVC-2 | SVC-4 |
|---|---|---|---|---|
| `service` | Recurring / contract services: maintenance plans, monitoring, MSS | 13 | 12 | 8 |
| `service_project` | Modernization, retrofit, consulting, studies | 15 | 8 | 10 |

The criteria:
- SVC-1 Scope & deliverables
- SVC-2 Service levels & performance commitments
- SVC-3 Eligible assets & prerequisites
- SVC-4 Process
- SVC-5 Plans, contract & commercial model (8)
- SVC-6 Outcomes with basis (10)
- SVC-7 Proof & delivery credentials (9)

New gate **G-SVC** (cap 40): no deliverable and no service-level fact in text. Without it, such a page could still reach 79–85.

**5. SE-wide patterns.**

| Pattern | Pages affected |
|---|---|
| No service levels (response time, coverage, SLAs) | 6/6 service pages |
| No IEC 62443 on any of the 3 OT-cyber pages (#12, #40, #41) | 3/3 |
| No visible date | 12/12 |
| Outcome stats as "up to X%" without basis | 5 pages |
| Unresolved footnote markers on those stats | #37, #39 |
| Published CMS placeholders ("ZZ_Paragraph Title", "ZZ_aprimo image alt text") | #10, #11 |
| Superseded framework (GRI G4) | #09 |

Many of the largest recurring losses are **template-level** and fixable once per component (not quantified):
- hero answer slot;
- carousel/tab text exposure;
- stat-tile basis line;
- date field;
- service-specific CTA block.

The rest are **author-level**: missing definitions, scope, SLAs, eligible models, proof metrics and standards.

**6. Calibration.**
- Both types discriminate (SD 7.9 / 9.7), and the ranking matches expert reading.
- Near-constant criteria are kept as standards: U9, SVC-2, SVC-7, U10. They are evidence-backed, and competitors pass them.
- One recalibration (the project-service variant) moved 3 pages by +1 to +2 points.

**Caveat.** The corpus extractor drops `aria-hidden` carousel slides and tab panels. On #37, the live server HTML has about 2 more feature blocks and 3 more customer names (sensitivity about +3–4 points). Re-extract before locking the gold set (§7).

---

## 2. Corpus audit

### 2.0 Method notes

- Each page was read in full. `geo_content_check.py --format md --pretty` was run on all 12; outputs are in the scratchpad `signals/`. Prompts are *inferred*: 1 seed + 4 fan-out per page, listed in each judge JSON.
- **Checker artifacts on this corpus.** Report these to the skill owner; the skill was not edited.
  - `Quotes: 3` on every page comes from the JSON in the header comment.
  - `next-generation` is counted on every page from the footer link "Next-generation Automation".
  - Vague-CTA detection returns 0 because corpus links are plain text. Vague CTAs were counted manually.
  - Word counts include about 60 template words ("Need help?" block and footer).
- **Spot-check of live pages (WebFetch, 2026-10-19).**

| Page | Extra content in live server HTML (not in corpus) | Effect |
|---|---|---|
| #07 | 2 more product cards | No numbers either way |
| #41 | Blog titles | No numbers either way |
| #37 | "Emergency support" and "Condition-based maintenance" blocks; 3 more success-story names | Would flip SVC-1 c1 and SVC-2 c4 to pass |

  The cause is that the corpus extractor drops `aria-hidden` slides and panels. Non-JS crawlers do receive them, but often as cloned or duplicated text.

### 2.1 Solution pages (#07–12)

#### Page-by-page

| # | Page (stage) | What an AI would extract / quote | Strongest GEO element | Weakest GEO elements | Prompt fit (seed / fan-out) | Score |
|---|---|---|---|---|---|---|
| 07 | EcoStruxure rack solutions for AI (Evaluation) | "EcoStruxure rack solutions support modular and scalable systems for AI." Product names: NetShelter Open Architecture, Power Shelf, Rack PDU Advanced, NetBotz. "supporting MGX and ORV3 architectures" | Clean answer-first intro naming the components and MGX/ORV3 support | **Zero numbers** on an AI-density page: no kW/rack, voltage or power-shelf rating. Reference designs only linked (likely PDF). No proof. No problem statement | Seed: named only. "kW per rack?" fails. "Reference designs for GB200?" fails (Vertiv answers with a table). "How does DC busbar/power shelf work?" fails | **22** |
| 08 | Industrial automation solutions (Consideration) | Little to quote. "Our industrial automation solutions enable the scalable design and operation of connected systems with best-in-class cybersecurity." | H1 matches topic; industries listed | Slogan opener. EcoStruxure Plant layers only as tab labels. Software cards = image + name, cloned. Partner-program recruitment mixed in. No outcome numbers | Seed: names the offer family only. Architecture, ROI and PLC/DCS integration all fail | **14** |
| 09 | Water & wastewater (Consideration) | "Our solutions save up to 30% on energy consumption…". "City of Conroe… up to 70% greater engineering efficiency with EcoStruxure Automation Expert". Water-cycle scope sentence | Most facts of the set: quantified outcomes, named utilities (Kunming, Aquapolo, Veolia), water-cycle scope, microgrid fit statement | Sprawl into factories, AR, DCS ROI and a cyber article. **GRI G4 cited as current** (superseded 2018). "global leaders… difficult to match". 6 vague CTAs. Architecture hidden in tabs | Seed: yes. Energy-savings fan-out: yes, no basis. Microgrids: yes. Architecture: no. Cases: names only | **36** |
| 10 | Commercial real estate (Awareness) | "Blackstone saved $10M and reduced emissions by 15%…". "buildings drive 37% of emissions" (unsourced) | Strong named references: Blackstone, 150 Holborn, 180 George St/Lendlease/Arup | No solution named at all. **"ZZ_Paragraph Title / ZZ_Paragraph Content" published.** Quote attribution with no quote text. Fluff 1.8/100 w. Decision CTAs on an Awareness page | Seed: partial. "Share of building emissions": yes, unsourced. "Grid-interactive buildings?": teaser. "ROI of retrofits": one case | **25** |
| 11 | Smart hospital room management (Consideration) | "EcoStruxure Connected Room Solutions for Healthcare provides an integrated patient experience…, reduces nurse calls…, integrates clinical and facilities systems". "10 million healthcare workers shortage projected by 2030" (WHO) | Best intro of the set: problem then definition. Sourced statistic. BMS / clinical integration described in text | No quantified outcome ("Reduce length of stay" is a heading). No proof. **Placeholder alt "ZZ_aprimo image alt text".** Sources ² and ³ orphaned. Duplicated bullets | Seed: yes. Room functions: yes. BMS integration: yes. Benefits in numbers: no. Controllers: names only | **37** |
| 12 | Cybersecurity solutions (Consideration) | "From consulting to optimization, our certified experts deliver OT cybersecurity strategies, resilient architectures, and managed security services…". Assess list (maturity, asset inventory, vulnerability, risk) | Clear 4-phase engagement (Assess → Design → Implement → Manage); NIS2/CRA named | **No IEC 62443.** No outcomes, proof or problem data. Teaser cards truncated and cloned. "certified experts" without certifying body | Seed: yes. "What does an assessment include?": yes. MSS: yes, briefly. IEC 62443: fails. NIS2: teaser | **27** |

#### Cross-page patterns (solution)

| Pattern | Pages | Criterion hit |
|---|---|---|
| Slogan or benefit H1/opener; definition absent or late | 08, 09, 10, 12 (07 and 11 are the exceptions) | U1 |
| Architecture never explained in prose; layers only as tab or card labels | 6/6 (11 partly) | SOL-2 |
| No quantified parameter (kW, MW, sites, response) anywhere | 6/6 | SOL-2 c4 |
| Outcomes absent, or "up to" without basis | 6/6 | SOL-4 |
| Proof = names without metrics, or none | 6/6 (09 and 10 have one metric each) | SOL-5 |
| No standards by number (IEC 62443, ASHRAE, IEC 61850…) | 6/6 (09 cites a superseded GRI G4) | U5 c2 |
| Hidden content in tabs | 08, 09, 10, 11, 12 | U3 c5 |
| No date | 6/6 | U9 |
| Generic sales CTA block (Product Selector / Quote / Where to buy) | 6/6 | U10 c3 |

#### Template-level vs author-level (solution)

| Template / component (fix once in Builder.io → all pages) | Author-level (fix per page) |
|---|---|
| Hero has no "answer paragraph" slot; the H1 field is used for a slogan | No "X is a … that … for …" definition |
| Card/carousel teaser text is truncated ("...") and slides are cloned. Inactive slides are `aria-hidden` | No how-it-works paragraph; no component table with roles |
| Tabs: only the first panel is in reading order (value areas, product layers) | No numbers: density, scale, capacity, outcomes with basis |
| Stat tile: number + fragment, footnote text not rendered | Problem statistics unsourced (10) or missing (07, 08, 12) |
| No date field | References without results; quotes missing (10) |
| Global "Need help?" block is product-sales oriented, even on Awareness pages | Placeholders published (10, 11), stale GRI G4 (09), self-praise (08, 09) |
| Alt-text field accepts placeholders ("ZZ_aprimo image alt text") | Off-topic insight cards (09), partner recruitment (08) |

### 2.2 Service pages (#37–42)

#### Page-by-page

| # | Page (stage, variant) | What an AI would extract / quote | Strongest GEO element | Weakest GEO elements | Prompt fit | Score |
|---|---|---|---|---|---|---|
| 37 | EcoCare (Evaluation, service) | "Up to 75% less electrical failure risk and unplanned downtime". "Up to 20% OpEx savings compared to traditional calendar-based service plans". "Our Connected Services Hub team monitor the health of your assets and systems 24/7…" | Quantified outcomes with a baseline (calendar-based plans). Eligible equipment families named (8 cards) | Nothing under the H1. Body never says what EcoCare *is*. Plans, features and how-it-works are tabs with no text in the corpus. **Footnotes ¹²³ unresolved.** No response time. Typo "Singe-Phase" | "What does EcoCare include?": partial. "Response time/SLA?": fails. "Which equipment?": categories only. "CBM vs calendar maintenance?": one stat | **34** |
| 38 | EcoFit modernization (Consideration, project) | "EcoFit can extend asset life by up to 25%…". "pre-engineered retrofit solutions for MV and LV circuit breakers, contactors, and protection relays". "Replace your aging or unsupported PLCs with the modern Modicon platform." | Best of the set: descriptive H2 per service line, each opening with a concrete statement. Migration path named | "Savings up to 90%" with no basis (of what?). No duration or downtime. No references or credentials. 7 vague CTAs | "Options to modernize instead of replace?": yes. "What does a retrofit include / how long?": fails. "Asset-life gain?": yes. "Take-back?": yes | **39** |
| 39 | EcoConsult (Consideration, project) | Offer names (Audit, Electrical Digital Twin, for Data Centers, Systems Studies). "Up to 90%* safety risk mitigation" | Offer lines named; 3 numbered steps | Body never defines EcoConsult ("vendor-agnostic" is only in the meta). **Asterisks never explained.** Which studies (arc flash, short circuit)? Unstated. "What to expect" tab empty | "What does an audit include?": fails. "Digital twin?": one line. "Studies and standards?": fails | **23** |
| 40 | Cybersecurity services (Consideration, service) | Article teasers only ("Securing operational technology (OT)", "Building a cybersecurity strategy") | H1 matches topic | It is a **navigation/article hub**: no service named or described. Services carousel empty in text. G-SVC triggered | All service fan-outs fail | **8** |
| 41 | Managed security services (Evaluation, service) | "Our managed security services (MSS) combine cybersecurity and operational technology expertise…". Capability lists. "Detection use cases and response playbooks developed for industrial environments, not adapted from IT." | Clear definition + three capability sections in lists. 24x7 MDR named | "How does a managed security service work?" is answered **only by an image**. No SLA, SOC location, onboarding, pricing model or IEC 62443. Promo fluff | Seed: yes. "24x7 and response time?": hours only. "Which OT assets/tools?": fails. "IEC 62443?": fails | **27** |
| 42 | EcoFit drive services (Decision, project) | "Flexible options to modernize and extend the life of aging Altivar 61 and Altivar 71 variable speed drives." "certified drive experts" | Names the legacy models (Altivar 61/71). Two options (life extension vs replacement) | Successor not named ("latest drive technology"). No scope of life extension, downtime or lifecycle status. Brand-first H1. Generic benefit headings | "Altivar 71 replacement?": fails (no successor). "Life extension includes?": fails. "Still supported?": implicit only | **25** |

#### Cross-page patterns (service)

| Pattern | Pages | Criterion hit |
|---|---|---|
| **No numeric service level**: response, restore, visit frequency, duration, downtime | 6/6 (only "24/7" / "24x7" coverage on #37 and #41) | SVC-2 |
| No eligible models / multi-vendor statement / prerequisites | 6/6 (42 names Altivar 61/71) | SVC-3 |
| No contract or pricing model, and no regional availability | 6/6 | SVC-5 c3/c4 |
| No proof with results; no technician or SOC credentials; no standards (NFPA 70B/70E, IEC 62443, ISO 27001) | 6/6 (37 names one customer and the hub) | SVC-7 |
| Process = labels without explanation, or an image | 37, 39, 41 | SVC-4 |
| "Up to X%" outcomes without basis; footnotes/asterisks unresolved | 37, 38, 39 | SVC-6 c3/c5 |
| Definition missing from body (only in meta description) | 37, 39, 40 | U1, U2 |
| Cross-sell blocks repeated (EcoCare/EcoFit/EcoConsult) | 37, 38, 39 | U6 focus (not scored in SVC); boilerplate watch |

#### Template-level vs author-level (service)

| Template (service-page component set) | Author-level |
|---|---|
| In-page tab bar ("Overview / Service plans / Success stories / Features / How it works"). Panels are not in reading order, or are empty in server HTML | No "[Service] is a [type] that [does X] for [assets], delivered by [team]" opener |
| Stat tiles with footnote markers whose source text is not rendered | No SLA table; no eligible-asset list; no tier comparison |
| "How it works" component shows step labels only, or an image (#41) | No basis for outcome numbers; "Savings up to 90%" ambiguous |
| Same global product-sales CTA block on service pages ("Product Selector", "Where to buy?") | No standards; "certified experts" unqualified |
| Cross-sell blocks with identical copy across EcoCare/EcoFit/EcoConsult | Hub page (#40) published as a "service page" with no service content |

---

## 3. External research & exemplars

### 3.1 How AI engines treat solution and service (landing) pages

| Finding | Source (date) | Label | Implication for the logic |
|---|---|---|---|
| Assistants split pages into sections and judge each for clarity and directness. Key answers hidden in tabs or expandable menus may not be rendered. Replace vague terms with measurable facts ("decibel rating", not "quiet"). Q&A pairs and comparison tables are liftable | Microsoft Advertising blog, K. Madhavan, *Optimizing Your Content for Inclusion in AI Search Answers* (8 Oct 2025) | [O] | U3 c5 and tab-hidden facts; SVC-2/SOL-2 numbers; U1 answer-first |
| Non-commodity, experience-based content is the long-run lever. No special chunking or schema is needed for AI features. Don't create fan-out variant pages | Google Search Central, *Optimizing your website for generative AI features on Google Search* (last updated 2026-07-10) | [O] | Proof (SOL-5/SVC-7) and first-party facts weigh more than format. FAQ is not required (SOL-6 retired → U6) |
| B2B AI agents: first-party answer rates 79% for pricing, 93% for integrations, 92% for security. With hidden pricing, agents cite a third party in 45% of runs (18% with public pricing) | K. Indig / Growth Memo, 100 B2B products (13 Jul 2026), via research/02 | [P] | SVC-5 c3 (pricing *model*), SOL-7 c4 / SVC-3 (integration and compatibility) |
| 94% of B2B buyers fact-check AI research. Transparent pricing has been buyers' #1 vendor request every year since 2023. 83% shortlist three or fewer products | TrustRadius *2026 B2B Buying Disconnect Report* (15 Jul 2026; n = 1,862 buyers), via MarketScale (6 Aug 2026) | [L] survey | Verifiable claims (SOL-4/SVC-6 c3 basis, c5 footnotes); pricing-model transparency |
| Use-case precision, not brand recognition, decides whether a vendor is noticed (7% brand) | Semrush survey (Jul 2026, n = 519), via research/02 | [L] survey | SOL-7 Applicability & fit; SVC-3 eligible assets |
| 94% of B2B buyers used GenAI in a recent purchase. About 51% of software buyers start research in an AI chatbot | Forrester 2026 (secondhand); G2 (Apr 2026, n = 1,076) | [L] | Stage weighting: services are researched in AI at Evaluation |
| In one vertical (travel), *landing pages* were 73.4% of AIO and 71.2% of ChatGPT cited URLs. Format-level studies put product pages third (13.7–16.3%) behind listicles and articles | Salt Agency travel study (2026; page returned 403, summary via search); Wix AI Search Lab / DeltaV (2026, via search summaries) | [L] (vertical- and definition-dependent) | Landing/solution pages *can* be cited, but only when they carry answer content. No basis for down-weighting the type |
| Field-service buyer checklists emphasize response time, availability, coverage and scalability across regions, technician certification, and contingency during critical events | Crane Pi field-service guide; Field Nation vendor scorecard (undated vendor guides) | [P] weak | SVC-2, SVC-3 and SVC-7 check content. No independent survey found (gap) |
| Concrete specs/numbers, recency, neutral tone, evidence-backed claims and self-contained passages are the replicated content factors. "Add statistics" as decoration does not replicate | Skill `evidence-base.md` (SIGIR 2026, C-SEO Bench, E-GEO, HOPE 2025) | [C] | Weights favour facts (SVC-1/2/3, SOL-2/4) over format. Outcome checks require a basis |

**Gap.** No study isolates what buyers ask AI about *industrial services* specifically. The SVC fan-out is inferred from:
- the field-service checklists above [P];
- the B2B agent study [P];
- competitor page structures.

Treat SVC weights as priors to validate with Profound prompt panels.

### 3.2 Exemplars (WebFetch 2026-10-19; content as data)

| Exemplar | What it does that SE pages don't | What it still misses | Indicative score* |
|---|---|---|---|
| **Eaton, UPS services** (eaton.com/us/en-us/catalog/services/ups-services.html) | Response tiers "2-, 4- and 8-hour response time commitments 24x7x365". On-time KPI (99%). Footprint ("250 plus… factory-trained field technicians"; 38,000+ PM visits/year). Eligible models (9395/9390/9355/9155). Eaton-only statement. EOSL program. Contract vs T&M priority. US/Canada coverage. Named customer quotes with roles | No tiers comparison (in a PDF brochure). No pricing. Detailed response times in an XLSX. Technician count inconsistent (250+ vs "more than 240"). No date, no FAQ | **52 (Average)**, `service`, Evaluation |
| **Vertiv, AI Hub** (vertiv.com/en-us/solutions/ai-hub/) | Reference-design table with kW/rack, rack count, total MW, GPU platform and cooling type (e.g. 142 kW/rack, 10 MW, GB300, liquid + air). Retrofit vs new-build designs (applicability). Partner test data with conditions (Intel Gaudi3 tested at 160 kW, facility water 17–45 °C) | No definition at top. Problem not quantified in prose. No outcomes or standards. No date. Table partly garbled in text | **43 (Average)**, `solution`, Evaluation |
| **ABB, Cement Care** service agreements | Tier/module **comparison table** (Rapid Response / Lifecycle Management / Performance Improvement / Contract Management). 5-step set-up process. Eligible asset classes | No numeric response time ("guaranteed response time" only). No outcome numbers. Process graphic dated 2018 | not scored |
| **Rockwell, OT threat detection (MDR)** | Definition first ("a managed OT SOC offering designed for industrial environments"). Named integrations (IDS, firewall, EDR, IAM). Reporting cadence (monthly reports, quarterly reviews). 6-question FAQ. ISO 27001 | No SLA, SOC location, tiers, pricing, outcomes or IEC 62443 | not scored |
| Vertiv regional service-package pages (summaries only; fetch returned 404) | Named tiers (Basic / Essential / Preferred), 4-hour or 2-hour emergency response by region, PM visits/year | Regional inconsistency | not scored |

\*Indicative: levels assigned from WebFetch extracts (paraphrased, not verbatim-verified), confidence *low*. Use them only to show that the logic reaches mid-band for fact-bearing pages; they are not pilot scores. Script: scratchpad `exemplars.py`.

**What the exemplars teach.** No competitor is complete; each excels at one block. The citable assets are the *numbers in HTML*:
- response hours;
- technician counts;
- kW/rack tables;
- model lists.

None publishes prices. ABB's comparison table and Rockwell's FAQ show the format; Eaton shows the facts. A Schneider page combining all four would be best-in-class.

---

## 4. Proposed logic

### 4.0 Conventions

- U1–U10 are used exactly as defined in `scoring-framework.md` §2. Type-specific *interpretation notes* are added where needed; the U criteria are not redefined.
- Each type criterion has 3–5 binary checks. The level ceiling = round(5 × p/n), and 5 requires all checks (calculator rule). Where noted, **anchor caps** add a judge-applied maximum: the judge proposes ≤ the cap, and the calculator takes the lower value.
- **N/A** is allowed only where stated, e.g. "no footnote markers".
- **Interpretation note for all three U criteria below.** Cloned carousel slides, teasers truncated with "...", and tab panels without text **fail U3 c5** (key info hidden) and **U3 c4** (fragments without subject).
- **U1 c2 rule.** Pass if the title *or* H1 contains the seed prompt's core noun phrase in the user's words. Fail if the H1 is a slogan **and** the title is brand-first or vague.
- **U10 c3 rule.** The global "Need help?" block does not pass. A pass needs a topic-specific descriptive CTA ("Check how our solutions helped Veolia Water…", "Download our [NIS2] eGuide").
- **U9 rule.** Undated pages get level ≤ 1 even when facts are current.

### 4.1 Solution / industry landing page: SOL v1.1 (revises `page-types.md` §12)

**What AI extracts.**
- What the solution is and which offers compose it.
- The problem it addresses (with data).
- How it works (architecture, integration).
- For which segments, applications and scale.
- Outcomes with numbers.
- References.
- How to start (phases, delivery model).

Solution pages answer category-level Consideration prompts: "solutions for X in industry Y", "how do I reduce Z in Y". They also answer branded "what is [EcoStruxure X]" prompts. AI Mode favours official category-level brand pages [L]. Landing pages are cited when they carry answer content [L, vertical].

**Must-haves.**
1. A 40–60-word definition under the H1.
2. A sourced problem statistic.
3. A how-it-works paragraph plus a component table with roles.
4. Applications, scope and fit.
5. ≥ 2 outcomes with basis.
6. ≥ 1 named reference with a metric.
7. Phases and delivery model.
8. Standards by number.
9. A visible date.

**Common failures (SE pilot).**
- Slogan H1.
- Card/tab hubs with no prose.
- Zero numbers.
- "Up to" claims without basis.
- References without results.
- Placeholders.
- Stale frameworks.
- Product-sales CTA block on Awareness pages.

**Natural stages.** Awareness → Consideration. Product-solution pages (e.g. #07) also serve Evaluation.

#### Criteria (default weights, sum = 100)

| ID | Criterion | W | Family | Binary checks (pass definition) | Anchor notes | Weight rationale (evidence) |
|---|---|---|---|---|---|---|
| U1 | Answer-first definition & prompt alignment | 10 | answer_def | Standard c1–c5 (see U1 c2 rule §4.0) | Standard | Relevance and answer-first are the strongest content factors [C][L]. Failed on 4/6 SE pages. Raised from 8 |
| U2 | What / Who / When / Outcome | 6 | answer_def | Standard c1–c4 | U2 table | SE banner test [SE]. Unchanged |
| U3 | Extractable structure & self-containment | 6 | other | Standard c1–c5 + §4.0 interpretation | c5 fail on key facts → ≤ 2 | Self-containment +56% [C]. Microsoft: tabs may not render [O]. #1 SE template failure. **New in SOL** |
| U5 | Evidence: sources & standards | 4 | evidence | Standard c1–c5. c2 counts sector standards and regulations (IEC 62443, NIS2, ASHRAE 170, IEC 61850…) | Standard | Substance counts, decoration does not [C, contested]. Partly covered by SOL-1 c3 and SOL-5. 6 → 4 |
| U6 | Fan-out coverage & focus | 6 | fanout | Standard c1–c4. c4 expected facts = must-haves 1–7. An FAQ is one way to pass c2 | Standard | Fan-out [O]; focused coverage of 26–50% of sub-topics wins [L]. **Replaces SOL-6 FAQ** (FAQ evidence contested: +25% [L] vs ≈0 [C]) |
| U7 | Neutral tone | 6 | tone | Standard. c4 N/A unless the page compares options | Standard | Promotion OR up to 362 against [C]. Unchanged |
| U9 | Freshness | 3 | freshness | Standard. c3 N/A | Undated → ≤ 1 | Strong evidence [C], but solution pages are evergreen and the gap is template-level. 4 → 3 |
| U10 | Stage fit & next step | 3 | commercial | Standard + U10 c3 rule | Standard | Constant across SE pages (template CTA block). Kept as a standard. 6 → 3 |
| SOL-1 | Problem quantified & sourced | 7 | **evidence** (was other) | c1 the specific problem for the named segment is stated (not generic "challenges") · c2 ≥ 1 quantified problem fact (number + unit/timeframe) relevant to the segment · c3 that fact is attributed to a named source (+ year) visible on the page · c4 the problem is stated in the top block (≤ ~150 words after H1) | c3 fail → ≤ 3 | Problem data drives Awareness/Education prompts. The evidence family raises it there (×1.2/1.4) and lowers it at Evaluation. 12 → 7 because Consideration prompts ask *what/how/outcome* |
| SOL-2 | How it works: architecture & components in text | 13 | **specs** (was other) | c1 prose (≥ 2 sentences) explains how ≥ 2 components work together (power/data/control flow, layers) · c2 ≥ 3 components named canonically, each with a one-line functional role (not adjectives) · c3 interoperability named: protocols, standards, third-party / legacy systems or platforms it integrates with · c4 ≥ 1 quantified technical parameter (capacity, density, scale, ratings) · c5 architecture info is in HTML text, not only in an image, video, PDF, tab or truncated teaser | c1 and c4 both fail (catalogue only) → ≤ 2 | Concrete specs and comparisons are the strongest selection cue [C]. Integrations are a top B2B agent task [P]. Vertiv's kW/rack table is the most citable competitor asset. **Absorbs SOL-3**; 14 → 13 |
| SOL-4 | Outcomes quantified with basis | 11 | other | c1 ≥ 2 quantified outcomes · c2 ≥ 1 quantified outcome attributed to a named offer or component · c3 ≥ 1 outcome states its basis: baseline/comparison, conditions/scope, measurement method, or a visible source · c4 outcome KPIs are ones the persona measures (cost, uptime/MTTR, kWh/%, CO2, payback) for this segment · c5 every footnote/asterisk marker on an outcome resolves to visible text (N/A if no markers) | c3 fail → ≤ 3. Level ≥ 4 needs c3 and c5 | Numbers +62% absorption [L]. Evidence-backed claims OR 2–46 [C]. Buyers fact-check (94%) [L]. 12 → 11, with new basis checks |
| SOL-5 | Proof: references & validation | 10 | proof | c1 ≥ 1 named customer reference · c2 ≥ 1 reference with a quantified result on this page · c3 the reference is relevant to this segment/solution · c4 named third-party validation (certification body, standard compliance, analyst/award by name, named partner validation with specifics) · c5 reference context (site type/size/country) or a named, attributed quote (person + role + text) | c2 fail → ≤ 2 | Evidence-backed OR 2–46 [C]; proof weighted ×1.2–1.4 at Consideration/Evaluation. 12 → 10 (SOL-7 takes part of the "use-case" signal) |
| SOL-7 | Applicability, scope & fit | 10 | **comparison** (new) | c1 ≥ 3 specific applications/use cases with context (site type, process, environment) · c2 scope boundaries: size/scale range, new-build vs retrofit, single site vs portfolio, regions · c3 fit guidance: "choose X when/if…", variants differentiated by need, or when it is not suited · c4 compatibility with the installed base: brownfield, multi-vendor, prerequisites | Checks-based | Use-case precision decides vendor notice (7% brand) [L]. Consideration "best for" framing [SE]. Vertiv's retrofit vs new-build designs. **New** |
| SOL-8 | Implementation path & delivery model | 5 | **commercial** (new) | c1 engagement phases/steps in order · c2 each phase states what happens or is delivered · c3 delivery model: who delivers (SE teams, certified partners, alliance integrators) and which lifecycle services · c4 numeric timeline, effort or deployment indication | Checks-based | Decision-stage need (commercial ×1.5) [SE stage signals]. #12 shows it is easy. Practitioner-level evidence → low weight. **New** |

Retired: SOL-3 (merged into SOL-2 c2), SOL-6 (FAQ → U6).

**Gates / caps / penalties (SOL).**
- Standard G1–G6 apply. G2 is the backstop for pages that never define the solution.
- **No new SOL gate.** A solution page with no architecture *and* no outcomes could reach about 76 only if every other criterion were perfect. That is implausible, because SOL-5 c2 then supplies a quantified result. Revisit after the 30-page gold set.
- **Penalty `template_artifact` (−2).** Placeholder/test text (e.g. "ZZ_…", "lorem ipsum", placeholder alt text) or a section rendered twice verbatim. The name and definition are aligned with `range-and-software.md`. Card-title clones are scored in U3, not penalized twice.

**Recommendation templates (SOL, most frequent failures).**

| Failed check | Recommendation |
|---|---|
| U1 c1 / U2 c1 | Add a 40–60-word answer paragraph under the H1: **"[Solution] is a [category] that combines [components] to [primary function + citable differentiator] for [segment/application]."** Keep the slogan as a sub-headline. *Template: add an "answer paragraph" field to the solution hero.* |
| SOL-2 c1/c2/c4 | Add an H2 "How [solution] works" with 3–5 sentences (flow across layers) and an HTML table: *Component · Role · Key parameter (unit) · Link*. Example for #07: rack → rack PDU → power shelf → busbar, with `[VERIFY: kW per rack range, input voltage, shelf rating]`. Move reference-design key figures from the PDF into the table. |
| SOL-4 c3/c5 | For each "up to X%": state basis, conditions and source in one line under the tile. "Up to 30% energy savings vs. [baseline], measured at [site type], [year] `[SME]`". Render footnote text in HTML. Remove figures that cannot be sourced. |
| SOL-5 c2 | Give each reference card a result line: "[Customer], [site type, country]: [metric] in [timeframe] with [named offer]". Add one attributed quote (name, role, text). |
| SOL-7 | Add "Where it applies": 3–5 applications with context, scale range, new-build vs retrofit, and "Choose [offer A] if… / [offer B] if…". |
| U5 c2 | Cite governing standards and regulations by number (e.g. IEC 62443-2-4/3-3 for OT cyber, `[VERIFY]` sector standards). Replace GRI G4 with GRI Standards (2021) `[SME]`. |
| SOL-8 | Add a numbered "How to get started" list (Assess → Design → Implement → Operate), with what each step delivers, who delivers it and typical duration `[SME]`. |
| U3 c5 (template) | Expose tab panels and carousel slides as text in reading order. Don't truncate teaser text in the HTML. → SE Digital for rendering; content owner for teaser length. |
| template_artifact | Remove "ZZ_" placeholders. Write real alt text (80–140 chars) describing purpose. Add a pre-publish QA rule in Builder.io. |

**Intake-sheet fields (Solution page; adds to section A).**
- Problem statement + source and year.
- Named offers/components with roles.
- Integration protocols, standards and third-party systems.
- Target segments/applications + scale range + new-build/retrofit.
- Quantified outcomes + basis/method/source for each.
- References (customer, site, metric, timeframe, quote approval).
- Engagement phases + delivery model (SE / partners) + typical duration.
- Governing standards/regulations.
- Last substantive update.
- Template used (hero answer slot available? Y/N).

### 4.2 Service page: SVC v1.0 (new)

**What AI extracts.**
- What the service is.
- What is included / excluded.
- For which equipment (models, multi-vendor).
- Service levels: response time, coverage hours, remote vs on-site, visits/year, reporting.
- How it works (steps, onboarding).
- Plans/tiers and the contract/pricing model.
- Where it is available.
- Results with basis.
- Who delivers it (credentials) and proof.

Typical prompts:
- "What does [service] include?"
- "[vendor] UPS service response time"
- "Does [vendor] service third-party switchgear?"
- "OT MSS providers with 24/7 SOC"
- "Altivar 71 replacement"
- "How much does a UPS maintenance contract cost?"

**Must-haves.**
1. A definition opener.
2. A deliverables list (with exclusions/options).
3. A service-level table (hours, response, other KPIs, with conditions).
4. Eligible assets/models + prerequisites/migration.
5. Numbered process with roles and the starting point.
6. Plans compared + contract/pricing model + availability.
7. Outcomes with basis and resolved footnotes.
8. References with results + delivery credentials + standards.
9. A visible date.

**Common failures (SE pilot).**
- Definition only in the meta description.
- Tabs with no text.
- No SLA numbers.
- Eligible assets as categories only.
- No pricing model or availability.
- "Up to" claims with unresolved footnotes.
- No credentials or standards.
- Article hubs labelled as service pages.

**Natural stages.** Consideration → Evaluation → Decision (Post-purchase for renewals).

**Variants.**

| Variant | Covers | SVC-2 reading |
|---|---|---|
| `service` (default) | Recurring/contract services: maintenance and monitoring plans, MSS, support | c1 coverage hours; c2 response time |
| `service_project` | One-off projects: modernization/retrofit, consulting, studies, start-up | c1 lead time to start / scheduling window; c2 duration or downtime/outage window with a number; c3 deliverable turnaround or performance guarantee / warranty on work; c4 support during and after the project; c5 conditions |

#### Criteria

| ID | Criterion | W service | W project | Family | Binary checks (pass definition) | Anchor notes | Weight rationale (evidence) |
|---|---|---|---|---|---|---|---|
| U1 | Answer-first service definition | 10 | 10 | answer_def | Standard c1–c5 + §4.0 rule. c1 needs the definition in the **body** (meta does not count) | Standard | Relevance and answer-first [C][L]. Missing from body on 3/6 pages |
| U2 | What / Who / When / Outcome | 4 | 4 | answer_def | Standard | U2 table | Overlaps U1 / SVC-6, so low weight |
| U3 | Extractable structure & self-containment | 6 | 6 | other | Standard + §4.0 interpretation (tab bars with empty panels fail c5) | c5 fail on key facts → ≤ 2 | Tabs/stat tiles are the service template's core failure [O][C] |
| U7 | Neutral tone | 5 | 5 | tone | Standard. c4 N/A | Standard | Promotion hurts [C]. Services are bought at Evaluation (tone ×1.0) |
| U9 | Freshness | 3 | 3 | freshness | Standard. c3 relevant for modernization of legacy ranges (lifecycle status, named successor) | Undated → ≤ 1 | Recency [C]. SLAs and availability change, so dated terms matter |
| U10 | Stage fit & next step | 3 | 3 | commercial | Standard + U10 c3 rule (a service CTA must name the service: "Request an EcoCare assessment for [asset]") | Standard | Template constant. Kept as a standard |
| SVC-1 | Scope & deliverables | 13 | 15 | specs | c1 ≥ 3 concrete included activities/deliverables in text (e.g. "24/7 remote monitoring", "thermal inspection", "arc-flash study report") · c2 deliverables are specific: what is done, to what, or which artifact the customer receives (not a benefit) · c3 remote vs on-site split, or frequency/cadence (visits/year, continuous, monthly report) · c4 exclusions, limits, options or add-ons stated · c5 the scope is on this page in HTML text, not only in a tab, brochure, PDF or child page | Checks-based | "What's included" is the seed sub-question of every service prompt [inferred]. Concrete facts strongest [C]. Microsoft: measurable facts [O]. Hidden info → third-party fallback 45% [P] |
| SVC-2 | Service levels & performance commitments | 12 | 8 | specs | c1 coverage hours stated · c2 response or time-to-site / time-to-respond as a number with its unit · c3 another measurable commitment (restore/resolution time, on-time %, visits/year, report turnaround, detection-to-notification) · c4 escalation path described: who acts when (remote → on-site dispatch, SOC → customer) · c5 conditions of the commitments stated (tier, region, contract) | No numeric commitment (c2 and c3 fail) → ≤ 2 | Buyers' field-service checklists put response time and coverage first [P]. Eaton and Vertiv publish 2/4/8-hour tiers. Numbers are the strongest cue [C]. Lower for projects, where duration/downtime replaces SLAs |
| SVC-3 | Eligible assets & prerequisites | 9 | 9 | specs | c1 equipment/system categories covered named · c2 specific ranges/models/generations named (e.g. Altivar 61/71, Galaxy, Masterpact) · c3 multi-vendor / third-party coverage stated (yes/no, which) · c4 eligibility conditions or migration path stated (connectivity/gateway, age, firmware, successor platform) | Checks-based | Compatibility and integration are top agent tasks (93% first-party answer rate) [P]. Use-case precision [L]. "Replacement for [legacy]" is a Decision prompt [SE] |
| SVC-4 | Process / how it works | 8 | 10 | other | c1 steps listed in order · c2 each step explained (what happens / what is delivered), not a label · c3 roles: who does what (customer vs SE hub, field engineer, consultant) · c4 how the engagement starts (first step, e.g. site audit / connection) | Checks-based | Microsoft: numbered steps are liftable [O]. "How does [service] work" is a standard fan-out. Higher for projects |
| SVC-5 | Plans, contract & commercial model | 8 | 8 | commercial | c1 named tiers/plans/options listed (or one plan explicitly stated) · c2 differences between options stated (table preferred) · c3 contract/pricing model described: subscription/annual/per-asset/fixed-price study/T&M/outcome-based, or price drivers or an indicative range (prices not required) · c4 geographic availability stated (countries/regions, or "varies by country — see [named page]") | Checks-based | Transparent pricing is buyers' #1 request (4 years) [L]. Hidden pricing → third-party citation 45% [P]. ABB tier table. Scoring the *model*, not the price, keeps this feasible for SE |
| SVC-6 | Outcomes quantified with basis | 10 | 10 | other | c1 ≥ 2 quantified outcomes · c2 attributed to this named service (page-level context counts) · c3 ≥ 1 outcome has a basis: baseline/comparison, conditions, method or visible source · c4 KPIs the buyer measures (downtime, MTTR, OpEx, energy, asset life, risk) relevant to the scope · c5 every footnote/asterisk on an outcome resolves to visible text (N/A if none) | c3 fail → ≤ 3. Level ≥ 4 needs c3 and c5 | Numbers +62% absorption [L]. 94% of buyers fact-check [L]. Unresolved "*" invites misquotation (G4-adjacent risk) |
| SVC-7 | Proof & delivery credentials | 9 | 9 | proof | c1 ≥ 1 named customer reference relevant to the service · c2 ≥ 1 reference with a quantified result on this page · c3 delivery credentials: number/qualification/certification of engineers, named hub/SOC/service centres, installed base serviced · c4 service-relevant standards/certifications by number (NFPA 70B/70E, IEC 62443-2-4, ISO 27001, IEC 60364…) · c5 attributed customer quote (name + role + text) or named third-party validation | c2 fail → ≤ 2 | Evidence-backed OR 2–46 [C]. Eaton's technician and visit numbers are its most citable trust facts. "certified" without a body = style cue, ignored by LLMs [C] |

Sums: `service` = 100; `service_project` = 100.

**Gates / caps / penalties (SVC).**
- Standard G1–G6.
- **G-SVC (new, cap 40).** Trigger: SVC-1 c1 **and** c2 fail **and** SVC-2 has no passing check. In words: the page never states what is delivered or any service level.
  - Justification: without the gate, such a page scores up to **79–85** (computed with all other criteria at level 5; scratchpad `headroom.py`). It parallels G3 (PDP without specs, cap 40).
  - In the pilot it triggered on #40; non-binding there (8).
  - The gate ID is namespaced to avoid the G7/G8 collision between the sibling proposals (§7).
- **Penalty `template_artifact` (−2).** As in SOL.
- **Hub rule.** If the page lists articles or child services without describing any service (#40), score it with the declared logic and flag "better fit: hub/category". Recommend either adding a service-overview block (definition, offer table with one-line scope per service, links) or re-typing it as a hub.

**Recommendation templates (SVC).**

| Failed check | Recommendation |
|---|---|
| U1 c1 (definition only in meta) | Put the definition in the first body paragraph: **"[Service] is a [service type] that [what is done] for [eligible assets], delivered by [team] [remotely/on site]."** Example for #37: "EcoCare is a service plan that combines 24/7 remote monitoring by the Connected Services Hub with condition-based maintenance for [VERIFY: eligible equipment]." |
| SVC-1 c1/c5 | Replace the tab bar with an always-visible H2 "What's included" list (6–10 deliverables) plus "Optional add-ons" and "Not included". |
| SVC-2 | Add an HTML table "Service levels": *Commitment · Value · Unit · Applies to (plan/region)*: coverage hours, response time `[SME/Legal: per plan and region]`, visits/year, report cadence. If commitments vary by country, give the range and link to country pages. Projects: typical duration and downtime window per job type. |
| SVC-3 | Add "Eligible equipment": ranges/models (incl. legacy generations), multi-vendor yes/no, prerequisites (gateway, connectivity, firmware). Modernization pages name the successor (e.g. "replaced by [VERIFY: Altivar successor range]"). |
| SVC-4 | Turn step labels into a numbered list with 1–2 sentences each, a role per step and the starting point ("1. Site audit by a field engineer (half a day) `[SME]`…"). Replace process images (#41) with text. |
| SVC-5 | Add a plan comparison table (*Plan · Included · Service levels · Best for*) and one line on the contract model ("annual subscription per asset", "fixed-price study"). State availability by region. |
| SVC-6 c3/c5 | Render footnotes as text under the stat tiles: basis, sample and year `[SME]`. Rewrite ambiguous tiles ("Savings up to 90%" → "Up to 90% less [material/CO2/cost] than full replacement, [VERIFY basis]"). |
| SVC-7 | Add a reference with a result, and a "Who delivers" block: number of field engineers / hub / SOC locations, certifications (e.g. IEC 62443-certified practitioners `[VERIFY]`, NFPA 70E-trained), and service standards (NFPA 70B, IEC 62443-2-4). |

**Intake-sheet fields (Service page; adds to section A).**
- Service name + variant (recurring / project).
- Plans/tiers and differences.
- Included / excluded / add-ons.
- Eligible equipment (ranges, models, legacy generations, multi-vendor Y/N, prerequisites).
- Service levels per plan and region + source document + legal clearance to publish (Y/N).
- Process steps + roles + starting point + typical duration.
- Contract/pricing model (+ price drivers or indicative range if publishable).
- Countries where available.
- Outcome claims + basis/sample/year (footnote text).
- References with metrics + quote approval.
- Delivery organization facts (engineers, hubs/SOC, certifications).
- Applicable standards.
- Last substantive update.

### 4.3 Stage-family mapping for new and moved IDs

| ID | Family | Effect (multipliers A / Ed / C / Ev / D) |
|---|---|---|
| SOL-1 | evidence (was other) | 1.2 / 1.4 / 1.1 / 1.0 / 0.8 |
| SOL-2 | specs (was other) | 0.7 / 0.9 / 1.1 / 1.5 / 1.3 |
| SOL-4 | other (unchanged) | 1.0 |
| SOL-5 | proof (unchanged) | 0.7 / 0.9 / 1.2 / 1.4 / 1.2 |
| SOL-7 | comparison (new) | 0.6 / 0.9 / 1.5 / 1.4 / 1.0 |
| SOL-8 | commercial (new) | 0.5 / 0.6 / 0.9 / 1.1 / 1.5 |
| SVC-1, SVC-2, SVC-3 | specs | 0.7 / 0.9 / 1.1 / 1.5 / 1.3 |
| SVC-4, SVC-6 | other | 1.0 |
| SVC-5 | commercial | 0.5 / 0.6 / 0.9 / 1.1 / 1.5 |
| SVC-7 | proof | 0.7 / 0.9 / 1.2 / 1.4 / 1.2 |
| SOL-3, SOL-6 | retired | — |

---

## 5. Pilot scores & calibration

All quotes were verified as substrings of the corpus file: 0 failures across 344 quoted spans (720 checks in total). Normalization: whitespace, case, zero-width characters, and non-breaking hyphen/curly-apostrophe variants.
- Judge: a single judge (this analysis), temperature-equivalent strict reading.
- Confidence: high on all pages (full server text). The `aria-hidden` caveat in §2.0 applies.

### 5.1 Scores (final logic v2: SOL v1.1, SVC v1.0 with project variant)

| Page | Type key | Stage (natural) | Score | Band | Gates / penalties | Top 3 gaps (recoverable eff. points) |
|---|---|---|---|---|---|---|
| #07 AI rack solutions | solution | Evaluation | **22** | Poor | — | SOL-5 (12.3), SOL-7 (12.3), SOL-2 (10.3) |
| #08 Industrial automation | solution | Consideration | **14** | Poor | — | SOL-2 (12.9), SOL-7 (10.8), SOL-4 (9.9) |
| #09 Water & wastewater | solution | Consideration | **36** | Poor | cta_overload −1 | SOL-2 (10.3), SOL-7 (8.1), U1 (7.2) |
| #10 Commercial real estate | solution | Awareness | **25** | Poor | fluff_density −2, template_artifact −2 | U1 (11.5), SOL-2 (9.3), U7 (8.6) |
| #11 Hospital room mgmt | solution | Consideration | **37** | Poor | template_artifact −2 | SOL-5 (10.8), SOL-4 (9.9), SOL-7 (8.1) |
| #12 Cybersecurity solutions | solution | Consideration | **27** | Poor | — | SOL-5 (10.8), SOL-7 (10.8), SOL-2 (10.3) |
| #37 EcoCare | service | Evaluation | **34** | Poor | — | SVC-2 (11.9), SVC-1 (9.7), SVC-3 (9.0) |
| #38 EcoFit | service_project | Consideration | **39** | Poor | cta_overload −1 | SVC-7 (10.3), SVC-2 (8.4), SVC-4 (7.6) |
| #39 EcoConsult | service_project | Consideration | **23** | Poor | — | SVC-1 (12.5), SVC-7 (10.3), SVC-2 (8.4) |
| #40 Cybersecurity services (hub) | service | Consideration | **8** | Poor | G-SVC (cap 40, non-binding) | SVC-1 (13.6), SVC-2 (12.5), SVC-7 (10.3) |
| #41 Managed security services | service | Evaluation | **27** | Poor | — | SVC-2 (11.9), SVC-3 (11.2), SVC-7 (10.5) |
| #42 EcoFit drive services | service_project | Decision | **25** | Poor | — | SVC-1 (10.2), SVC-7 (9.4), SVC-2 (9.1) |

**Level matrix: solution.** Each cell is level (effective weight).

| Criterion | #07 | #08 | #09 | #10 | #11 | #12 | Spread |
|---|---|---|---|---|---|---|---|
| U1 | 3 (7.9) | 1 (9.0) | 1 (9.0) | 1 (14.4) | 3 (9.0) | 2 (9.0) | 1–3 |
| U2 | 2 (4.7) | 1 (5.4) | 4 (5.4) | 3 (8.6) | 4 (5.4) | 3 (5.4) | 1–4 |
| U3 | 2 (5.3) | 1 (5.4) | 2 (5.4) | 1 (6.2) | 2 (5.4) | 3 (5.4) | 1–3 |
| U5 | 0 (3.5) | 0 (4.0) | 1 (4.0) | 0 (4.9) | 1 (4.0) | 1 (4.0) | 0–1 |
| U6 | 2 (5.3) | 1 (6.0) | 2 (6.0) | 2 (7.4) | 3 (6.0) | 3 (6.0) | 1–3 |
| U7 | 2 (5.3) | 0 (6.5) | 0 (6.5) | 0 (8.6) | 2 (6.5) | 2 (6.5) | 0–2 |
| U9 | 1 (2.9) | 1 (3.0) | 0 (3.0) | 1 (3.1) | 1 (3.0) | 1 (3.0) | 0–1 |
| U10 | 2 (2.9) | 2 (2.4) | 2 (2.4) | 2 (1.5) | 2 (2.4) | 4 (2.4) | 2–4 |
| SOL-1 | 0 (6.1) | 0 (7.0) | 2 (7.0) | 3 (8.6) | 4 (7.0) | 0 (7.0) | 0–4 |
| SOL-2 | 2 (17.1) | 0 (12.9) | 1 (12.9) | 0 (9.3) | 3 (12.9) | 1 (12.9) | 0–3 |
| SOL-4 | 0 (9.7) | 0 (9.9) | 3 (9.9) | 2 (11.3) | 0 (9.9) | 0 (9.9) | 0–3 |
| SOL-5 | 0 (12.3) | 2 (10.8) | 3 (10.8) | 3 (7.2) | 0 (10.8) | 0 (10.8) | 0–3 |
| SOL-7 | 0 (12.3) | 1 (13.6) | 2 (13.6) | 1 (6.2) | 2 (13.6) | 1 (13.6) | 0–2 |
| SOL-8 | 0 (4.8) | 0 (4.1) | 1 (4.1) | 0 (2.6) | 0 (4.1) | 3 (4.1) | 0–3 |

**Level matrix: service.**

| Criterion | #37 | #38 | #39 | #40 | #41 | #42 | Spread |
|---|---|---|---|---|---|---|---|
| U1 | 1 (7.5) | 3 (9.5) | 1 (9.5) | 1 (9.5) | 3 (7.5) | 2 (7.8) | 1–3 |
| U2 | 3 (3.0) | 4 (3.8) | 2 (3.8) | 1 (3.8) | 4 (3.0) | 3 (3.1) | 1–4 |
| U3 | 2 (5.0) | 3 (5.7) | 2 (5.7) | 2 (5.7) | 3 (5.0) | 1 (5.2) | 1–3 |
| U7 | 2 (4.2) | 2 (5.7) | 0 (5.7) | 2 (5.7) | 2 (4.2) | 0 (3.0) | 0–2 |
| U9 | 1 (2.7) | 1 (3.1) | 1 (3.1) | 1 (3.1) | 1 (2.7) | 1 (3.1) | 1–1 |
| U10 | 2 (2.7) | 3 (2.6) | 3 (2.6) | 1 (2.6) | 1 (2.7) | 2 (3.9) | 1–3 |
| SVC-1 | 2 (16.2) | 3 (15.7) | 1 (15.7) | 0 (13.6) | 3 (16.2) | 2 (17.0) | 0–3 |
| SVC-2 | 1 (14.9) | 0 (8.4) | 0 (8.4) | 0 (12.5) | 1 (14.9) | 0 (9.1) | 0–1 |
| SVC-3 | 1 (11.2) | 2 (9.4) | 1 (9.4) | 0 (9.4) | 0 (11.2) | 2 (10.2) | 0–2 |
| SVC-4 | 2 (6.6) | 1 (9.5) | 2 (9.5) | 0 (7.6) | 1 (6.6) | 1 (8.7) | 0–2 |
| SVC-5 | 1 (7.3) | 2 (6.8) | 2 (6.8) | 0 (6.8) | 0 (7.3) | 2 (10.5) | 0–2 |
| SVC-6 | 3 (8.3) | 3 (9.5) | 2 (9.5) | 0 (9.5) | 0 (8.3) | 0 (8.7) | 0–3 |
| SVC-7 | 2 (10.4) | 0 (10.3) | 0 (10.3) | 0 (10.2) | 0 (10.4) | 0 (9.4) | 0–2 |

### 5.2 Does it discriminate?

**Spread.** Solution 14–37 (SD 7.9); service 8–39 (SD 9.7). The ranking matches an expert reading.

Solution: **11 ≈ 09 > 12 > 10 > 07 > 08**.
- #11 has the only real definition + sourced problem + integration text.
- #09 has the most facts but sprawls and is stale.
- #08 is an image-card hub.

Service: **38 > 37 > 41 > 42 > 39 > 40**.
- #38 has descriptive service sections.
- #37 has outcome numbers with a baseline but no definition or SLA.
- #40 is an article hub.

**Band.** All are Poor. This is not a leniency problem: the inflation watch fails in the *strict* direction. Two checks argue that the content, not the logic, drives this:
1. **Indicative exemplars** with real facts score in Average: Eaton 52, Vertiv 43.
2. **Sibling types on the same template** score in the same range (range 12–36, software 22–30, calculators 11–17).

A gold set of only SE template pages cannot test the upper bands. Add 3–5 strong external or rewritten pages per type before locking (§7).

**Non-discriminating criteria** (all, or all but one, at the same level):

| Criterion | Pattern | Decision |
|---|---|---|
| U9 (both types) | All level 1 (no dates; #09 is 0 for GRI G4) | **Keep as a standard.** Recency is one of the strongest cues [C]. The fix is one template field. Weight already lowered to 3 |
| U10 (both types) | Mostly 2 (template CTA block) | **Keep at 3.** It flags the product-sales CTA block on service and Awareness pages. Cheap template fix |
| SVC-2 | 0–1 on all 6 | **Keep as a standard (12/8).** It is the sharpest gap vs competitors (Eaton, Vertiv publish hours) and a top buyer question. A page passing it would be clearly more citable |
| SVC-7 | 0 on 5/6 | **Keep.** Proof is a replicated cue [C], and Eaton's technician/visit facts show it is publishable |
| U5 (solution) | 0–1 | **Keep at 4.** IEC 62443 is absent from all three OT-cyber pages, and that is exactly what the criterion should catch |
| SOL-8 | 0 on 4/6 | **Keep at 5.** #12 proves feasibility. Low weight reflects practitioner-level evidence |

### 5.3 Counter-intuitive effects found → one recalibration (before/after)

1. **Project services were penalized for SLA-type checks that don't apply to them.** Before (v1, all services on one weight set):
   - SVC-2 cost #38 12.5 points, mostly for "coverage hours / response time".
   - For a retrofit or consulting project, the buyer asks "how long, how much downtime", not "what response time".

   **Change:** the `service_project` variant.
   - SVC-2 12 → 8, re-read as lead time / duration / downtime.
   - SVC-1 13 → 15.
   - SVC-4 8 → 10.

   Re-score:

   | Page | v1 | v2 |
   |---|---|---|
   | #38 | 37 | **39** |
   | #39 | 22 | **23** |
   | #42 | 24 | **25** |
   | Other 9 pages | — | unchanged |

   Ranking unchanged. The SVC-2 levels did not change, because none of these pages states a duration or downtime either.
2. **SOL-2 anchor wording.** v1 capped SOL-2 at 2 whenever c1 (prose explanation) failed. That would also cap a Vertiv-style reference-design *table* with kW/rack, which is the most citable asset in the category. **Change:** the cap applies only when c1 **and** c4 (quantified parameter) both fail, i.e. a catalogue without facts. No pilot score changed. Vertiv's indicative score uses the refined anchor.
3. **Checked, no change.** SOL-7 sits in the comparison family, so at Consideration it carries the highest effective weight (13.6). Kept, because shortlisting by use-case fit is the dominant Consideration behaviour [L]. Re-check on the 30-page set.
4. **Checked, no change.** Stage effects behave as intended:
   - #10 at Awareness: U1 effective weight 14.4; proof/commercial reduced.
   - #07 at Evaluation: SOL-2 17.1.
   - #42 at Decision: SVC-5 10.5.

### 5.4 Judge notes for κ calibration

Borderline checks where two raters may differ:
- U1 c2 (title vs H1 rule).
- U2 c3 "when" (weak triggers).
- SOL-2 c1 (is a 4-phase lifecycle an "architecture"? Ruled no for #12).
- SOL-7 c1 (are industry tiles "applications with context"? Ruled yes for #08).
- SVC-1 c2 (is "life extension of Altivar 61/71" specific? Ruled yes).
- SVC-7 c3 ("certified experts" without a body: ruled fail).

Pages within ±3 of the 40 band edge (#38 39, #11 37, #09 36) need the protocol's 3-judgement median before any reporting.

---

## 6. Proposed weights JSON fragment

Merge into `assets/weights.json` after review. The full file is in `pilot/weights_sol_svc_v2.json`. Gate and penalty IDs are namespaced to avoid collisions.

```json
{
  "families": {
    "evidence":   ["+ SOL-1"],
    "specs":      ["+ SOL-2", "+ SVC-1", "+ SVC-2", "+ SVC-3"],
    "comparison": ["+ SOL-7"],
    "commercial": ["+ SOL-8", "+ SVC-5"],
    "proof":      ["(SOL-5 already)", "+ SVC-7"]
  },
  "page_types": {
    "solution":        {"U1": 10, "U2": 6, "U3": 6, "U5": 4, "U6": 6, "U7": 6, "U9": 3, "U10": 3,
                        "SOL-1": 7, "SOL-2": 13, "SOL-4": 11, "SOL-5": 10, "SOL-7": 10, "SOL-8": 5},
    "service":         {"U1": 10, "U2": 4, "U3": 6, "U7": 5, "U9": 3, "U10": 3,
                        "SVC-1": 13, "SVC-2": 12, "SVC-3": 9, "SVC-4": 8, "SVC-5": 8, "SVC-6": 10, "SVC-7": 9},
    "service_project": {"U1": 10, "U2": 4, "U3": 6, "U7": 5, "U9": 3, "U10": 3,
                        "SVC-1": 15, "SVC-2": 8, "SVC-3": 9, "SVC-4": 10, "SVC-5": 8, "SVC-6": 10, "SVC-7": 9}
  },
  "gates": {
    "G-SVC": {"cap": 40, "desc": "Service page with no concrete deliverable and no service-level fact in text (SVC-1 c1 and c2 fail, and SVC-2 has no passing check)"}
  },
  "penalties": {"template_artifact": 2}
}
```

**Calculator alias additions** (for `geo_score_calc.py` TYPE_ALIASES):
- `"service"`, `"service page"`, `"services"` → `service`
- `"project service"`, `"modernization service"`, `"consulting service"` → `service_project`

**Calculator note.** The anchor caps ("c2 fail → ≤ 2", etc.) are judge-applied through `proposed_level`. Encoding them in the calculator would make them deterministic; this is suggested for v1.1 of the script.

`--selftest` passes with this file (sums 100; no criterion in two families).

**Also update `page-types.md` §12.** Replace with SOL v1.1. Add §12b Service (SVC). Remove SOL-3/SOL-6. Add the intake rows to `intake-sheets.md` §B and the recommendation rows to `recommendations-playbook.md` §4.

---

## 7. Open questions / risks

1. **Corpus fidelity (high).** `build_corpus.py` skips `aria-hidden="true"` elements. SE carousels and tabs mark inactive slides/panels that way, so the corpus understates content that non-JS crawlers *do* receive. Verified on #37: two feature blocks and three customer names are missing.
   - Before the gold set is locked, re-extract with hidden elements kept but de-duplicated, and re-score.
   - The template finding still stands: hidden or cloned text is weak for extraction, and Microsoft warns tabbed content may not be rendered [O].
2. **Gate/penalty ID collisions across type analyses.** `range-and-software.md` uses G7/G8 (cap 49) and `casestudy-and-calculator.md` uses G7 (cap 59) / G8 (cap 39) with different meanings. This file uses `G-SVC`. Penalty `template_artifact` is shared; align definitions. The integrator should namespace all type gates (G-RNG, G-SW, G-CS, G-CALC, G-SVC) before merging.
3. **Can SE publish SLAs and pricing models?** SVC-2 and SVC-5 assume SE may state response times, coverage and contract models in HTML, at least as ranges per region. This needs Legal / Service BU confirmation.
   - If not publishable, keep the criteria but accept "commitments vary by country — see [named page]" as passing c5/c4 only. The score will then honestly show the gap.
   - Third parties fill hidden facts: 45% fallback [P].
4. **Global vs country pages.** Service levels and availability differ by country. Decide whether the global page carries ranges and the country pages carry exact values, and score country pages with A6 (country) in the intake.
5. **Hub pages.** #40 (and arguably #08) are navigation hubs. Propose a light "Hub / overview" logic, or route hubs to Category, rather than scoring them as Service/Solution. Decide alongside the software_hub variant in the sibling analysis.
6. **Single-judge pilot.** κ is not yet measured. Borderline checks are listed in §5.4. Run 2–3 human raters plus the 3-judgement median on #09, #11 and #38 (within ±3 of 40).
7. **Gold-set ceiling.** All 12 pages are Poor, so the upper anchors (levels 4–5, bands 70+) are untested on SE content. Add rewritten SE pages (a Scalpel rewrite of #37 and #07) and 2–3 competitor pages per type, with verbatim judging.
8. **Evidence gaps.** No controlled or large study on AI citation of *service* pages specifically. SVC weights rest on general factors [C], B2B agent behaviour [P] and buyer surveys [L]. Validate quarterly with Profound prompt panels: ≥ 7 runs per prompt per engine, with control pages. Priority prompts:
   - "[service] response time"
   - "what does [service] include"
   - "replacement for Altivar 71"
   - "OT MSS IEC 62443"
9. **Stale and incorrect facts found during the audit** (route to content owners, not scored elsewhere):
   - GRI G4 (#09).
   - "Singe-Phase UPS" typo (#37).
   - Orphaned sources ² ³ (#11).
   - Quote attribution without quote text (#10).
   - Footnote text not rendered (#37, #39).
10. **Checker improvements** (skill owner):
    - Ignore the header-comment JSON for quote counting.
    - Exclude the footer and "Need help?" block from word and fluff counts.
    - Detect plain-text CTA labels ("Learn more", "Discover more") in markdown input.
    - Flag unresolved footnote markers (¹²³, *) as a deterministic signal.
11. **Out-of-scope observations → SE Digital** (not scored):
    - JSON-LD is WebPage/Organization only (no Service/FAQ).
    - Cloned carousel markup.
    - Empty alt text (#12).
    - Hero videos without transcripts (#10, #38, #42).
    - Reference designs probably PDF-only (#07).

*Citation-readiness of content only. Actual AI citation also depends on retrieval, off-site consensus and technical access.*

**Sources** (accessed 2026-10-19; also see skill `sources.md`):
- Microsoft Advertising blog, "Optimizing Your Content for Inclusion in AI Search Answers" (8 Oct 2025): https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers
- Google Search Central, "Optimizing your website for generative AI features on Google Search" (updated 2026-07-10): https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- TrustRadius 2026 B2B Buying Disconnect Report, via MarketScale (6 Aug 2026): https://www.marketscale.com/industries/software-and-technology/94-of-b2b-buyers-fact-check-ai-research-before-trusting-it-trustradius-finds
- Indig / Growth Memo, B2B AI-agent study (13 Jul 2026); Semrush B2B AI survey (Jul 2026); Forrester 2026: see `research/02-industry-studies-and-platforms.md` §5.2
- Salt Agency, travel-sector AI citation page types (2026; 403 on fetch, search summary only): https://salt.agency/blog/travel-sector-ai-visibility-data-study/
- G2 buyer survey (Apr 2026), via search summary: https://www.marketscale.com/industries/marketing-tech/b2b-buyers-are-forming-vendor-shortlists-before-ever-talking-to-sales-and-ai-is-why.md
- Field-service partner checklists [P]: https://service.cranepi.com/articles/10-questions-ask-when-searching-field-service-partner-strategic-guide ; https://fieldnation.com/resources/labor-vendor-scorecard
- Exemplars:
  - https://www.eaton.com/us/en-us/catalog/services/ups-services.html
  - https://www.vertiv.com/en-us/solutions/ai-hub/
  - https://new.abb.com/process-automation/process-automation-service/service-agreements/cement-care
  - https://www.rockwellautomation.com/en-au/capabilities/industrial-cybersecurity/ot-threat-detection-services.html
  - Vertiv service-package pages (search summary only; 404 on fetch): https://www.vertiv.com/en-in/campaigns/vertiv-service-package

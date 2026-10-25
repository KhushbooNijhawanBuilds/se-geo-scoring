# Page-Type Scoring Logic v2.0 — SE Content GEO Scoring Standard (19 Oct 2026)

Authoritative logic for the 10 SE inventory page types: blog article, news/press release, solution, service, product range, software, customer story, calculator, white paper, sustainability/ESG. It **supersedes** `page-types.md` §2 (range), §6 (article), §8 (case study) and §12 (solution). Other types (PDP, category, CaaS, editorial, document/datasheet, comparison, FAQ, glossary, video) remain in `page-types.md` v1.

Weights are in `assets/weights.json` v2.0, which is the single source of truth. Universal criteria U1–U10, anchors, scale and bands are in `scoring-framework.md`. Each logic was derived from:
- an audit of 6 live SE examples
- external research and competitor exemplars
- pilot scoring

The full rationale and evidence for each type is in `GEO Elec Project/research/type-analysis/*.md`.

---

## 0. Application rules for all types (v2.0)

**R1 — What is scored.** Score the **rendered page content**: what a visitor sees after the page loads. That includes text inside web components (shadow DOM), same-origin iframes and collapsed tabs/accordions, marked `[hidden]` in the capture. The content owner controls this. Header, navigation, mega-menu, footer, cookie banner and breadcrumbs are excluded.

**R2 — Hidden vs visible.** Text that exists only in a collapsed tab, accordion, carousel slide, interactive tool panel or video can earn credit on the type criteria. However, **U3 c5 fails** when *key* facts exist only there, so U3 ≤ 2 (Microsoft: AI systems may not render hidden content).

**R3 — Crawler gap (reported, not scored).** Compare server-HTML words with rendered words. If server/rendered < 0.7, or the H1, primary outcome, method or key facts are missing server-side, add the out-of-scope observation **"Crawler gap: x% of the content is invisible to non-JS AI crawlers (GPTBot/OAI-SearchBot, ClaudeBot, PerplexityBot) → SE Digital"**. Report the server-HTML score alongside when the gap is material.

**R4 — Template vs author.** Tag every failed check `[T]` (caused by the CMS template/component and fixed once for all pages) or `[A]` (author/owner content). Recommendations route `[T]` to SE Digital / template owner, `[A]` to the content owner, PIM-sourced fields to the PIM champion, and facts to SME.

**R5 — U4 c2 fact-density threshold** (quantified facts per 100 words, genuine facts only; repeated numbers count once):
- ≥ 1.0 for article, news, editorial, solution, service, case study, software hub, ESG hub, glossary
- ≥ 2.0 for all others (range, software product, calculator, white paper, ESG report, PDP, datasheet)

**R6 — Link checks.** Link-anchor checks (U8 c4, U10 c4) are N/A when the capture shows no link labels.

**R7 — Placeholders and duplication.** The penalty `template_artifact` (−2) applies to:
- live placeholder text ("ZZ_…", lorem ipsum, "Paragraph Title", placeholder alt text)
- a whole section rendered twice

Card-title clones are scored in the type criterion (e.g. RNG-9 c4, U3), not penalized twice.

**R8 — Gate registry v2.0.** Caps are applied after the weighted sum; the lowest cap wins.

| Gate | Applies to | Trigger | Effect |
|---|---|---|---|
| G1 | all | Factual contradiction (incl. ESG KPI mismatch HTML vs report) | U8 = 0; ≤ 59 |
| G2 | all | Primary subject/question never answered or defined | ≤ 39 |
| G3 | PDP, datasheet | No quantified specs in text | ≤ 40 |
| G4 | all | Misleading/unsafe technical or safety statement | ≤ 39 + SME escalation |
| G5 | all | Title/H1 promise not delivered | ≤ 49 |
| G6 | all | Core content only in gated asset / image / video / PDF / widget with no HTML text equivalent (incl. bare PDF URL; gateway with no findings/KPIs) | U3 ≤ 2; ≤ 59 |
| G7 | article, news | No visible publication date | ≤ 59 |
| G8 | case_study | No quantified customer outcome in body text | ≤ 59 |
| G9 | calculator | CALC-1, CALC-2, CALC-3 all level 0 | U3 ≤ 2; ≤ 39 |
| G10 | range | No rating/capacity/size with unit for the range or any member | ≤ 49 |
| G11 | software_product, software_trial | None of: deployment model, integrations/protocols, security facts, licensing/pricing/trial terms | ≤ 49 |
| G12 | service, service_project | SVC-1 c1 and c2 fail **and** no SVC-2 check passes | ≤ 40 |
| G13 | all | Thin page: < 3 substantive factual statements | U7, U8 max 2 (no cap) |

**R9 — Penalties** (max −10 total, except hidden_instructions):

| Penalty | Deduction |
|---|---|
| keyword_stuffing | −3 |
| fluff_density (> 1.5/100 words of body text) | −2 |
| boilerplate (> 40% of text shared with sibling pages) | −2 |
| cta_overload (≥ 3 vague CTAs) | −1 |
| self_ranking | −3 |
| template_artifact | −2 |
| superseded_no_notice (an older edition with no link to or label for the newer one) | −3 |
| hidden_instructions | −10 + flag |

**R10 — Stage.** Use the declared stage. Otherwise use the type's natural stage below, labelled *inferred*. ESG pages use **Evaluation** (supplier/stakeholder verification) until a dedicated stage is approved.

**R11 — Two-layer documents.** White papers and ESG reports get a **Gateway score** for the HTML page; this is the headline score. When the PDF text is supplied they also get a **Document score**. The two are reported side by side and never averaged.

---

## 1. Blog article — key `article` (v2)

**What AI extracts:**
- the thesis/answer in the first 30% of the page
- definitions and how-it-works passages
- quantified context with source
- frameworks and checklists
- named expert perspective
- trade-offs

Cited for "why does X matter / how does X work / what's changing in Y".

**Natural stages:** Awareness, Education (Consideration for selection-style posts). Flag Decision unless it is a how-to.

| ID | Criterion | W | Checks (pass = …) |
|---|---|---|---|
| U1 | Insight/answer in paragraph 1 | 14 | Framework c1–c5. A Summary block directly under the byline counts as "first 100 words". c4 passes if ≥ 80% of H2s open with a direct answer |
| ART-1 | Key-takeaways block (quality) | 5 | c1 a block of 3–5 bullets near the top or bottom · c2 each bullet is a standalone sentence naming its subject · c3 ≥ 1 bullet carries a specific fact/number/recommendation · c4 bullets match the body's claims, with nothing truncated and no new claims. Level 0 if there is no block |
| ART-2 | Title & subheads: descriptive, prompt-aligned, consistent | 7 | c1 H1 names the topic in searcher language (no pun/slogan/clickbait) · c2 H1, SEO title and meta describe the same topic and angle · c3 ≥ 60% of H2s describe their section · c4 ≥ 1/3 of H2s are phrased as or mirror a buyer question · c5 any explicit title promise ("3 priorities") is delivered as visible structure |
| U3 | Extractable structure | 8 | Framework. Template H2s ("Top picks", "Add a comment") are excluded from c1 |
| U4 | Factual density | 10 | Framework (R5: ≥ 1.0/100w). c3 is judged on the informational sections; the closing offer paragraph is judged under U7 |
| U5 | Evidence & expertise | 12 | Framework. c3 passes only for a quote from a named person *other than the author*. c5 needs a named human author whose role/experience is visible ("Guest Blogger" fails) |
| ART-3 | Non-commodity insight | 10 | c1 first-hand observation with a specific detail · c2 original framework/typology/decision rule/step sequence · c3 SE first-party data or analysis with conditions/method · c4 a clear, defensible thesis in one quotable sentence beyond consensus · c5 practical, audience-specific implications. Level 5 needs c3 + c1 |
| U6 | Fan-out coverage & focus | 10 | Framework |
| U7 | Neutral tone | 7 | Framework; a single descriptive closing offer paragraph is allowed |
| U8 | Entities & descriptive links | 4 | Framework |
| U9 | Freshness | 5 | Framework. Level 5 only with a visible "Updated" date plus refreshed statistics |
| U10 | Stage fit & next step | 8 | Framework. c3/c4 pass when the CTA names a specific SE asset |

**Gates:** G7. **Common SE failures:**
- `[A]` narrative/biographical openings, slogan/pun H1s, unsourced numbers, no takeaways, no standards by number, promotional ambition lines, a CTA naming no asset
- `[T]` "Top picks" and "Add a comment" H2s inside the article; "Guest Blogger" byline

---

## 2. News / press release — key `news` (new)

**What AI extracts:**
- who announced what, when and where
- the named offer and its category
- headline numbers with their basis
- availability and roadmap
- partner/customer names
- attributed quotes
- company descriptor (from the About block)
- findings (for research releases)

ChatGPT cites owned newsrooms about 18% of the time; Google AI surfaces cite them rarely.

**Stage by release subtype** (intake field):

| Release subtype | Stage |
|---|---|
| Launch / reference design / partnership with an offer | Consideration (Evaluation if spec-led) |
| Research / study | Education |
| Corporate / event / award / financial | Awareness |

Flag Decision.

| ID | Criterion | W | Checks |
|---|---|---|---|
| NEWS-1 | Headline & summary deck as the answer layer | 12 | c1 headline names company + named offer/partner + concrete action (not "advances") · c2 headline or deck states the single most important specific fact · c3 a deck of 2–4 bullets, each a standalone factual sentence naming its subject · c4 headline uses the category/topic noun phrase a searcher would use |
| U2 | Lede: What / Who / When / Outcome | 12 | Framework, judged on headline + deck + first paragraph |
| NEWS-2 | Temporal anchoring & dateline | 8 | c1 visible date with the month written out or in ISO format (numeric DD/MM fails) · c2 dateline city · c3 relative timing ("this fall", "early next year") resolved to an absolute date/quarter · c4 milestones stated absolutely and consistent with the release date (incl. attachments) |
| U4 | Factual density | 10 | Framework (R5: ≥ 1.0/100w; repeated numbers count once) |
| NEWS-3 | Claim substantiation | 12 | c1 quantified performance claims state their basis (study/test/pilot/baseline/conditions) · c2 "first/only/leading/pioneering" claims scoped (category, geography, as-of date) or evidenced · c3 independent validation named: customer/pilot site, partner test, third party, or a standard **by number** · c4 the evidence asset is named by title/ID **and** its key findings appear in the HTML (N/A if there is no asset) |
| NEWS-4 | Substantive attributed quotes | 7 | c1 ≥ 1 quote with name, title and organization · c2 ≥ 1 quote contains a specific, checkable fact/mechanism · c3 a third-party voice with name and role · c4 quotes name the offer/topic explicitly |
| NEWS-5 | Offer facts & availability | 9 | c1 availability: markets + timing · c2 price/pricing model or how to obtain/join · c3 key specs/capabilities with units or named elements · c4 maturity explicit (pilot/GA/roadmap/validated to …). Research releases: c2/c4 N/A. Corporate/event/financial: criterion N/A (dropped) |
| NEWS-6 | Entity anchoring: About block & canonical bridge | 7 | c1 "About [company]" block in the HTML · c2 entity facts given (size, reach, sector; a slogan alone fails) · c3 the offer's canonical destination named by title in text (not "visit the web" or the PDF only) · c4 partner/third-party entities described at first mention |
| U3 | Extractable structure | 7 | Framework. Template H2s (Spokespeople, Attached files, Share) are excluded. c1 fails when visible subheads are plain text |
| U6 | Fan-out coverage | 6 | Framework; roundups of several announcements fail c3 |
| U7 | Neutral tone | 6 | Framework; c2 passes on any stated limitation or scope limit |
| U8 | Entity consistency | 4 | One canonical offer name |

U1, U5, U9 and U10 are replaced by NEWS-1/U2, NEWS-3/NEWS-4, NEWS-2 and NEWS-6 c3 respectively. **Gates:** G7; G6 if the announcement facts are only in the attached PDF.

**Common SE failures:**
- `[T]` numeric date; subheads not marked as headings; About block missing (5 of 6 releases)
- `[A]` relative timing, unscoped superlatives, quotes without facts, "visit the web", inconsistent offer naming, main finding missing from the headline

---

## 3. Solution / industry page — key `solution` (v1.1)

**What AI extracts:**
- what the solution is and which offers compose it
- the problem (with data)
- how it works (architecture/integration)
- segments, applications and scale
- outcomes with numbers
- references
- how to start

Answers category-level Consideration prompts and branded "what is [EcoStruxure X]". **Natural stages:** Awareness → Consideration (Evaluation for product-solution pages).

| ID | Criterion | W | Checks |
|---|---|---|---|
| U1 | Answer-first definition & prompt alignment | 10 | Framework. c2 passes if the title *or* H1 contains the seed prompt's core noun phrase; it fails if the H1 is a slogan **and** the title is brand-first/vague |
| U2 | What / Who / When / Outcome | 6 | Framework |
| U3 | Extractable structure | 6 | Framework (R2). Cloned carousel slides, "…"-truncated teasers and empty tab panels fail c4/c5 |
| U5 | Evidence: sources & standards | 4 | Framework; c2 counts sector standards/regulations (IEC 62443, NIS2, ASHRAE 170, IEC 61850…) |
| U6 | Fan-out coverage | 6 | Framework; c4 expected facts = SOL must-haves |
| U7 | Neutral tone | 6 | Framework |
| U9 | Freshness | 3 | Framework; undated → ≤ 1 |
| U10 | Stage fit & next step | 3 | Framework. The global "Need help?" block does **not** pass c3; a topic-specific descriptive CTA does |
| SOL-1 | Problem quantified & sourced | 7 | c1 specific problem for the named segment · c2 ≥ 1 quantified problem fact · c3 attributed to a named source (+ year) · c4 stated in the top block (≤ ~150 words after the H1). c3 fail → ≤ 3 |
| SOL-2 | How it works: architecture & components | 13 | c1 prose (≥ 2 sentences) on how ≥ 2 components work together · c2 ≥ 3 components named canonically, each with a functional role · c3 interoperability named (protocols, standards, third-party/legacy systems) · c4 ≥ 1 quantified technical parameter · c5 in HTML text, not only image/video/PDF/tab/teaser. c1 and c4 both fail → ≤ 2 |
| SOL-4 | Outcomes quantified with basis | 11 | c1 ≥ 2 quantified outcomes · c2 ≥ 1 attributed to a named offer · c3 ≥ 1 states its basis (baseline, conditions, method or source) · c4 KPIs the persona measures · c5 every footnote/asterisk resolves to visible text (N/A if there are none). c3 fail → ≤ 3; level ≥ 4 needs c3 + c5 |
| SOL-5 | Proof: references & validation | 10 | c1 ≥ 1 named customer reference · c2 ≥ 1 reference with a quantified result on this page · c3 reference relevant to the segment · c4 named third-party validation · c5 reference context or a named, attributed quote. c2 fail → ≤ 2 |
| SOL-7 | Applicability, scope & fit | 10 | c1 ≥ 3 specific applications with context · c2 scope boundaries (scale range, new-build vs retrofit, single site vs portfolio, regions) · c3 fit guidance ("choose X when…", when it is not suited) · c4 compatibility with the installed base (brownfield, multi-vendor, prerequisites) |
| SOL-8 | Implementation path & delivery model | 5 | c1 phases in order · c2 what each phase delivers · c3 who delivers (SE teams, certified partners) + lifecycle services · c4 numeric timeline/effort indication |

SOL-3 is merged into SOL-2, and SOL-6 (FAQ) into U6.

**Common SE failures:**
- `[T]` slogan H1 with no answer slot; cloned/truncated teaser cards; empty tab panels; stat-tile footnotes that never render; "Need help?" product-sales block; no date field
- `[A]` zero sourced numbers; "up to X%" without basis; references without results; GRI G4 cited as current

---

## 4. Service page — keys `service` (recurring) / `service_project` (modernization, retrofit, consulting)

**What AI extracts:**
- what the service is and what is included/excluded
- eligible equipment (models, multi-vendor)
- service levels (response time, coverage hours, remote vs on-site, visits/year)
- how it works
- plans and contract/pricing model
- availability
- results with basis
- delivery credentials and proof

**Natural stages:** Consideration → Evaluation → Decision (Post-purchase for renewals).

| ID | Criterion | W service / project | Checks |
|---|---|---|---|
| U1 | Answer-first service definition | 10 / 10 | Framework; c1 needs the definition in the **body** (meta doesn't count) |
| U2 | What / Who / When / Outcome | 4 / 4 | Framework |
| U3 | Extractable structure | 6 / 6 | Framework (R2); tab bars with empty panels fail c5 |
| U7 | Neutral tone | 5 / 5 | Framework |
| U9 | Freshness | 3 / 3 | Framework; undated → ≤ 1 |
| U10 | Stage fit & next step | 3 / 3 | The CTA must name the service ("Request an EcoCare assessment for [asset]") |
| SVC-1 | Scope & deliverables | 13 / 15 | c1 ≥ 3 concrete included activities/deliverables · c2 deliverables are specific (what is done, to what, artifact received), not benefits · c3 remote vs on-site split, or frequency/cadence · c4 exclusions/limits/options/add-ons · c5 scope in HTML on this page (not only a tab/brochure/PDF/child page) |
| SVC-2 | Service levels & commitments | 12 / 8 | c1 coverage hours · c2 response/time-to-site as a number + unit · c3 another measurable commitment (restore time, visits/year, report turnaround, detection-to-notification) · c4 escalation path · c5 conditions (tier/region/contract). No numeric commitment → ≤ 2. *Project variant:* c1 lead time to start · c2 duration or downtime window with a number · c3 turnaround/guarantee/warranty on work · c4 support during and after · c5 conditions |
| SVC-3 | Eligible assets & prerequisites | 9 / 9 | c1 equipment categories named · c2 specific ranges/models/generations named · c3 multi-vendor/third-party coverage stated · c4 eligibility conditions or migration path |
| SVC-4 | Process / how it works | 8 / 10 | c1 steps in order · c2 each step explained · c3 roles (customer vs SE hub/engineer) · c4 how the engagement starts |
| SVC-5 | Plans, contract & commercial model | 8 / 8 | c1 named tiers/plans (or one plan stated) · c2 differences stated (table preferred) · c3 contract/pricing model or price drivers (prices not required) · c4 geographic availability |
| SVC-6 | Outcomes quantified with basis | 10 / 10 | Same as SOL-4 c1–c5, applied to the named service |
| SVC-7 | Proof & delivery credentials | 9 / 9 | c1 named relevant customer reference · c2 a reference with a quantified result · c3 delivery credentials (engineer numbers/qualifications, named hubs/SOC/centres, installed base) · c4 service standards by number (NFPA 70B/70E, IEC 62443-2-4, ISO 27001…) · c5 attributed quote or named third-party validation. c2 fail → ≤ 2 |

**Gates:** G12.

**Hub rule:** a page listing articles or child services without describing a service (e.g. #40) is scored with the declared logic and flagged "better fit: hub/category".

**Common SE failures:**
- `[A]` no service levels on any page; definition only in the meta; eligible assets as categories only; no pricing model/availability; IEC 62443 missing on OT-cyber services; unresolved "up to" footnotes
- `[T]` empty tab panels; stat tiles

---

## 5. Product range / master range — key `range` (v1.1)

**What AI extracts:**
- what the family is and who it is for
- members (variants, or sub-ranges on master ranges) and how they differ
- selection axes with thresholds
- ecosystem/protocols
- standards
- legacy names and successors

Master ranges use the same logic; the members are sub-ranges, and each needs one decision-relevant figure plus a "best for". **Natural stages:** Consideration (master ranges), Evaluation (single ranges).

| ID | Criterion | W | Checks |
|---|---|---|---|
| U1 | Range definition & scope | 10 | Framework. c1 = definition with category noun + application; c2 = H1/title names the range **and** the category noun ("Discover X" fails); c5 = "range at a glance" |
| U2 | What / Who / When / Outcome | 5 | Framework |
| RNG-1 | Member comparison table with "best for" | 10 | c1 HTML-text table (not image/PDF/configurator) · c2 rows = members, ≥ 3 shared decision attributes · c3 values with units, one per cell · c4 "best for" column · c5 covers all members shown |
| RNG-2 | Selection guidance in text | 12 | c1 explicit conditional choice statements for ≥ 2 members ("Choose VL for 200–500 kW…"); card "Ideal for…" lines don't count · c2 selection axes named with thresholds + units · c3 selection possible from text alone (not only via the Product Selector) · c4 overlapping members disambiguated |
| RNG-3 | Applications, segments & references | 6 | c1 ≥ 3 named segments/applications · c2 applications attached to specific members · c3 ≥ 1 named reference with a metric |
| RNG-4 | Quantified differentiators | 5 | c1 ≥ 1 range-level claim with number + unit · c2 measurement basis stated · c3 no unanchored superlatives |
| RNG-5 | Ecosystem, compatibility & protocols | 6 | c1 accessories with function · c2 protocols/connectivity named · c3 cross-range compatibility · c4 monitoring/management software named |
| RNG-6 | Standards & certifications | 5 | c1 ≥ 1 product standard by number · c2 mapped to members/regions (IEC vs UL) · c3 certifications/declarations named |
| RNG-7 | Range FAQ | 4 | c1 ≥ 3 Q&As · c2 cover selection/compatibility/migration · c3 direct answer first, range/member named |
| RNG-8 | Lifecycle, legacy names & migration | 6 | c1 former names stated ("formerly Vigirex") · c2 successor path for legacy members · c3 lifecycle status of members · c4 generation identifiers |
| RNG-9 | Member descriptors | 11 | Over product members: c1 every member has a descriptor beyond its name (category noun + function) · c2 ≥ 75% carry a key rating with unit · c3 ≥ 50% state an application/"best for" · c4 descriptors unique (no double/triple rendering or copy-paste) · c5 no off-topic cards inside the range content |
| U3 | Extractable structure | 5 | Framework |
| U5 | Evidence | 3 | Framework |
| U7 | Neutral tone | 4 | Framework (c4 N/A) |
| U8 | Entity consistency | 5 | Framework; includes brand casing and the master-range ↔ range relationship |
| U9 | Freshness | 3 | Framework |

**Gates:** G10.

**Common SE failures:**
- `[T]` "Discover X" H1; card text rendered 2–3×; off-topic drive/app promos; KPI labels with no numbers; no date
- `[A]` no comparison table or choice statements; standards and legacy names missing; selection delegated to the Product Selector

---

## 6. Software page — keys `software_product` / `software_hub` / `software_trial`

**What AI extracts:**
- category definition
- capabilities mapped to modules
- integrations/protocols
- deployment model and requirements
- security/compliance
- licensing/pricing logic and trial terms
- proof
- product map
- versions and former names

In B2B agent tests these facts are answered first-party in about 79–93% of runs when present. With pricing hidden, a third party answers 45% of the time.

**Classifier:**
- **Hub:** ≥ 3 software products each with its own card.
- **Product:** one product's capabilities are the main content.
- **Trial:** a sign-up/download/licence action is the main content.

**Natural stages:**
- **Product:** Evaluation.
- **Hub:** Consideration.
- **Trial:** Decision.

| ID | Criterion | Checks | product / hub / trial |
|---|---|---|---|
| U1 | Answer-first definition | Framework ("[Product] is a [category] software that [function] for [audience], deployed [model]") | 10 / 12 / 12 |
| U2 | What / Who / When / Outcome | Framework | 5 / 6 / 6 |
| SW-1 | Capabilities & use cases | c1 ≥ 3 capabilities as concrete functions (verb + object + context) · c2 mapped to named modules/editions/products · c3 ≥ 1 with a measurable parameter · c4 use cases named · c5 no label-only tiles. Hubs: applies to each product descriptor | 12 / 12 / 12 |
| SW-2 | Integrations, protocols & interoperability | c1 named protocols/standards (BACnet, Modbus, SNMP, OPC UA, MQTT, IEC 61850…) · c2 named third-party systems/device families · c3 integration method (API, connectors, gateways) · c4 "agnostic/open" claims backed by specifics (N/A if there is no claim) | 11 / 6 / — |
| SW-3 | Deployment, architecture & requirements | c1 **software** deployment model (SaaS/on-prem/hybrid/edge) · c2 scale/limits or architecture · c3 system requirements stated or linked by name · c4 implementation/onboarding path | 9 / 4 / 14 |
| SW-4 | Security, privacy & compliance | c1 concrete controls · c2 certifications by number (IEC 62443-x-x, ISO/IEC 27001, SOC 2) · c3 privacy/residency · c4 named security resource (trust center, vulnerability disclosure) | 9 / 4 / 6 |
| SW-5 | Licensing, pricing model & trial | c1 licence model · c2 price/range or an explicit price-driver/channel statement · c3 trial with ≥ 2 terms (duration, scope, cost, data, expiry) · c4 how to acquire/activate | 11 / 4 / 26 |
| SW-6 | Proof & quantified outcomes | c1 named customer + achieved quantified outcome · c2 outcome with baseline/timeframe/method · c3 third-party validation with year · c4 page statistics attributed and **visible as numbers** | 8 / 8 / — |
| SW-7 | Product/edition map & selection | c1 products/editions with one-line differentiation · c2 "which product for which need" · c3 comparison table of editions/products · c4 relationships explained (Expert vs Advisor; on-prem vs cloud; SE vs AVEVA) | 5 / 16 / — |
| SW-8 | Versions, lifecycle & former names | c1 current version/what's new with date · c2 former names stated · c3 support lifecycle or release notes named | 4 / 6 / — |
| U3 | Extractable structure | Framework | 4 / 8 / 6 |
| U7 | Neutral tone | Framework | 4 / 5 / — |
| U8 | Entity consistency | Framework | 4 / 5 / 6 |
| U9 | Freshness | Framework | 4 / 4 / 6 |
| U10 | Stage fit & next step | Framework (trial only) | — / — / 6 |

**Gates:** G11 (product and trial pages).

**Common SE failures:**
- `[A]` no protocols, deployment model, certifications or licensing on any page; "agnostic/multi-vendor" with no specifics; trial page with no terms
- `[T]` benefit-label tiles; KPI counters with no values in the HTML; logo walls as images; "ZZ_" placeholder; duplicated DCIM section
- **Redirect:** the "software by industry" URL redirects to the portfolio hub

---

## 7. Customer success story — key `case_study` (v1.1)

**What AI extracts:**
- a one-sentence outcome: customer + result with unit + period + named offer
- customer profile
- what was deployed and how
- a quotable customer statement
- how the number was measured
- a date

Engines quote text, not video, stat-card images or tab widgets. **Natural stages:** Evaluation (default); Consideration for approach showcases and brand partnerships; Decision for purchase references. Flag Awareness.

| ID | Criterion | W | Checks |
|---|---|---|---|
| CS-1 | Outcome-led title + answer-shaped summary | 14 | c1 title/H1 names the customer (or anonymized type) · c2 title/H1 states the outcome or problem solved (not a slogan) · c3 40–150-word prose summary in the first ~150 body words · c4 summary covers ≥ 4 of who/problem/solution/result/timeframe · c5 summary contains a quantified result with timeframe |
| CS-2 | Customer profile | 8 | c1 industry in body · c2 size/scale · c3 country/region · c4 application/scope. Meta-only facts fail |
| CS-3 | Quantified results with baseline & timeframe | 20 | c1 ≥ 1 customer outcome with unit · c2 ≥ 2 distinct quantified outcomes · c3 baseline stated · c4 timeframe/period · c5 result attributed to the named offer · c6 the primary outcome leads. Vanity numbers (years of relationship, floor area, parts) and targets **fail** c1/c2 |
| CS-4 | Challenge → solution → results in text | 8 | c1 specific challenge · c2 what was deployed, where, how, by whom · c3 results in text · c4 segmented under labels, each section naming the customer. Tab labels with no panel text fail |
| CS-5 | Attributed customer quote | 7 | c1 a direct customer quote in text · c2 speaker named · c3 role + organization · c4 substantive (reason/fact/outcome). Vendor-employee quotes don't count |
| CS-6 | Offers named with their role | 7 | c1 exact commercial names · c2 role of the main offer explained in text · c3 each offer as a named card/link. Card grids alone reach at most 2 |
| CS-7 | Metric methodology / verifiability | 6 | c1 how the result was measured · c2 measurement boundary/period · c3 data source or third-party verification |
| U2 | What / Who / When / Outcome | 4 | Framework |
| U3 | Extractable structure | 8 | Framework (R2). c5 fails when narrative, quote or results exist only in video, stat-card images, carousels, tab widgets or a PDF |
| U7 | Neutral tone | 5 | Framework; slogan headings and promo inserts fail c3 |
| U8 | Entity consistency | 5 | Framework; stat cards vs prose vs meta (G1 if they disagree) |
| U9 | Freshness | 4 | c1 publish date or project/results date visible · c2 results ≤ 3 years old or dated |
| U10 | Stage fit & next step | 4 | Descriptive CTA to the solution/range |

**Gates:** G8; G6 for a story told only in video/image/PDF.

**Common SE failures:**
- `[T]` story, summary and quotes rendered client-side (4 of 6); empty tab panels in the server HTML; "ZZ_" placeholders
- `[A]` slogan H1; vanity stat cards; best metric only in the meta description; no date; no method; product grid without roles

---

## 8. Calculator / TradeOff Tool — key `calculator` (new)

**What AI extracts:** engines can't run the tool, so they cite the knowledge around it:
- what is calculated and from which drivers
- the formula/logic
- assumptions with values and sources
- typical results/benchmarks
- a worked example
- input/metric definitions
- limits
- model version/date

**Natural stages:** Consideration, Evaluation; Education for "how to calculate" tools. Flag Awareness.

| ID | Criterion | W | Checks |
|---|---|---|---|
| U1 | Answer-first | 10 | Framework. c1 = the opening states what is calculated **and** its drivers/core relationship; a bare "Use this tool to estimate X" passes only c3 |
| U2 | What / Who / When / Outcome | 4 | Outcome = the decision the result informs |
| CALC-1 | Method / formula | 16 | c1 calculation logic (formula or steps: inputs → intermediates → outputs) · c2 variables with units · c3 model provenance (who built it; which white paper/standard it implements) · c4 scope/limits of validity · c5 a simple case could be reproduced by hand |
| CALC-2 | Assumptions & default values | 13 | c1 key assumptions listed · c2 each with value + unit · c3 source **and** data year · c4 default scenario values · c5 region/currency/price-year basis (N/A if region-independent) |
| CALC-3 | Worked example & representative results | 15 | c1 ≥ 1 complete example (inputs → outputs with units) in text/table · c2 typical ranges/benchmarks · c3 key drivers/sensitivity quantified · c4 results in text/table, not only a chart/UI |
| CALC-4 | Inputs & outputs defined | 7 | c1 every required input listed · c2 inputs defined (meaning, unit, range) · c3 output metrics defined · c4 acronyms expanded |
| CALC-5 | Interpretation & decision guidance | 6 | c1 how to read the result · c2 "choose/do X if…" or trade-off rule · c3 levers to improve the result · c4 uncertainty/limits of interpretation |
| U3 | Extractable structure | 6 | Framework (R2). c5 fails when tool knowledge exists only inside the widget/iframe/hidden panel |
| U5 | Evidence | 5 | Framework; c3 usually N/A; c2 includes method standards (PUE definitions, GHG Protocol) |
| U7 | Neutral tone | 4 | Framework |
| U8 | Entity consistency | 4 | Tool naming; figures consistent with the tool (G1 on contradictions, e.g. two "typical PUE" values) |
| U9 | Freshness | 5 | c1 model version/date visible · c2 data year ≤ 2 years old or stated · c4 reviewed yearly |
| U10 | Stage fit & next step | 5 | Descriptive CTAs ("Open the power sizing calculator", "Read White Paper 3") |

CALC criteria are judged on the rendered page, including the tool's panels (R1). If that knowledge sits only inside the tool UI or a hidden panel, U3 ≤ 2 and the crawler gap is flagged.

**Gates:** G9.

**Common SE failures:**
- `[T]` the tool runs in an iframe whose raw HTML has about 5 words; the method, assumptions, defaults and model version live only in the tool panels
- `[A]` an intro that only invites use; related-content card grids instead of explanation; near-duplicate single-/three-phase pages; contradictory typical values

---

## 9. White paper / technical document — keys `whitepaper_gateway` (headline) + `whitepaper_doc` (when the PDF text is supplied)

**What AI extracts from the gateway:**
- the title (matched to "how to / what are" prompts)
- the abstract's opening as the answer
- key findings with numbers
- coverage
- publisher/author/date
- the PDF as a second citable source

**Natural stages:** Education (default), Consideration. Flag Decision.

| ID | Criterion | W | Checks |
|---|---|---|---|
| U1 | Answer-first title & abstract lead | 12 | c1 first 1–2 abstract sentences state the thesis/answer, not background · c2 title matches prompt intent · c3 key message above the metadata block · c4 any sections open with an answer · c5 summary/takeaways |
| WP-1 | Abstract quality | 10 | c1 90–220 words, a single instance, not truncated · c2 problem named · c3 audience named · c4 approach/contents stated · c5 main conclusion stated specifically (not "guidance is provided") · c6 copy-clean |
| WP-2 | Key findings in HTML | 14 | c1 findings enumerated · c2 ≥ 2 quantified findings with units/conditions · c3 above the download block · c4 ≥ 1 non-commodity SE finding · c5 implications/actions stated. Level ≤ 1 triggers G6 |
| WP-3 | Questions answered / coverage | 8 | c1 ≥ 3 specific topics beyond the title · c2 as question-style/descriptive headings · c3 ≥ 3 of 5 inferred fan-outs answered by ≥ 1 sentence · c4 one primary intent |
| U4 | Factual density | 8 | Framework (R5: ≥ 2.0); general acronyms exempt from c4 |
| DOC-8 | Methodology, authorship & references | 10 | c1 named authors with role · c2 method/assumptions · c3 references/standards by number · c4 first-party evidence with conditions · c5 publisher + document number |
| DOC-7 | Version, date, supersession | 8 | c1 visible release/update date · c2 page version = file-name version · c3 change note when version > 1.0 · c4 released/reviewed ≤ 24 months ago · c5 related/superseding editions linked or "current edition" stated |
| DOC-5 | Title, file name & metadata | 4 | c1 descriptive title · c2 descriptive file name (not code-only) · c3 document type in words ("White paper 126") · c4 complete, non-truncated meta description |
| U3 | Extractable structure | 6 | Framework; c5 fails if findings live only in the PDF |
| U8 | Entity consistency | 6 | Includes metadata consistency (a version mismatch fails c3 but is not G1) |
| U7 | Neutral tone | 4 | Framework |
| U10 | Stage fit & next step | 6 | c3 descriptive download CTA ("Download white paper 126: Retrofitting…, PDF 1.4 MB") · c4 links to related papers, TradeOff tools and solutions |
| DOC-9 | Gate the deep dive, not the knowledge | 4 | Only if gated; otherwise all N/A and the weight is redistributed |

**Document module `whitepaper_doc`:** DOC-1 14 · DOC-2 12 · DOC-3 8 · DOC-4 10 · DOC-5 6 · DOC-6 8 · DOC-7 10 · DOC-8 14 · U4 8 · U8 5 · U7 5. Here DOC-1 means:
- c1 an executive summary with key findings on pages 1–2
- c2 ≥ 2 quantified findings in it
- c3 scope/questions stated
- c4 a link back to the gateway URL
- c5 findings in prose, not only in infographics

**Common SE failures:**
- `[T]` no H1 (title rendered 3× as lower headings); abstract duplicated; no key-findings, author or related-links slot; code file names
- `[A]` background-first abstracts; "guidance is provided" with no guidance; page version ≠ file version; 4 of 6 papers older than 2 years with no review note

---

## 10. Sustainability / ESG — keys `esg_hub`, `esg_report` (gateway, headline), `esg_report_doc` (PDF text)

**Facts AI extracts** (e.g. for "SE scope 1 2 3 emissions", "SE sustainability performance 2025", "Is SE SBTi validated?"):
- emissions by scope with period and basis
- % vs baseline
- targets with baseline/target year
- progress
- frameworks
- assurance level and provider
- ratings
- edition/date
- where the data and index live

Audiences: investors/ESG analysts, rating agencies, **customer procurement assessors**, media. Stage: **Evaluation** (R10).

| ID | Criterion | Checks | hub / report / report_doc |
|---|---|---|---|
| U1 | Answer-first | Company + report + period in the title; headline result first | 12 / 10 / — |
| DOC-1 | Highlights layer (document) | KPIs + basis in the first 5 pages; points to the HTML home | — / — / 12 |
| ESG-1 | Headline KPI layer | c1 ≥ 3 headline KPIs with value + unit · c2 GHG **by scope** (1; 2 market/location; 3) in tCO2e · c3 each KPI with period + boundary · c4 KPIs as rows that extract cleanly (label/unit/value; not chart-only) · c5 YoY or vs-baseline comparison | 20 / 22 / 18 |
| ESG-2 | Targets, baselines & progress | c1 named targets · c2 baseline year + target year · c3 current progress per target · c4 external validation (SBTi) or status incl. missed/at-risk · c5 link to transition plan/methodology | 12 / 14 / 10 |
| ESG-3 | Reporting basis & methodology | c1 frameworks named (CSRD/ESRS, GRI, ISSB/TCFD, SASB) · c2 GHG Protocol + market/location basis · c3 period + organizational boundary · c4 restatements/methodology changes disclosed | 6 / 10 / 12 |
| ESG-4 | Assurance & ratings | c1 assurance level + provider · c2 scope of assured indicators · c3 ratings/validations with date (CDP, MSCI, EcoVadis, SBTi) · c4 assurance statement included/linked | 6 / 8 / 10 |
| ESG-5 | Navigation & machine-readable companions | Hub/gateway: c1 each entry gives type + period + release date · c2 1–2-sentence contents description · c3 companion links (data annex XLSX/CSV, GRI/ESRS index, CDP; XBRL) · c4 descriptive anchors · c5 current vs archived labelled. Document: c1 TOC with pages · c2 bookmarks · c3 content index · c4 companion data referenced · c5 accurate cross-references | 14 / 8 / 6 |
| U3 | Extractable structure | Framework (no placeholders) | 8 / — / — |
| DOC-4 | Text-extractable file | Tagged PDF, real tables, reading order, bookmarks | — / — / 12 |
| DOC-7 | Edition, period vs release date, change note, supersession | Framework DOC-7 (ESG variant: reporting period distinct from release date) | 8 / 10 / 8 |
| U8 | Canonical naming & metric consistency | G1 on KPI contradictions | 4 / 6 / 6 |
| DOC-5 | Title / file name | — | — / 4 / — |
| U7 | Neutral tone | No generic green claims; misses disclosed | 4 / 4 / 6 |
| U10 | Routing to hub/IR/data/press release | — | 6 / 4 / — |

A bare PDF URL is scored with the gateway logic, where every HTML check fails ("NOT FOUND — bare PDF"), together with the document module.

**Penalties:** `superseded_no_notice` (−3) for archived editions; `template_artifact` for "ZZ_" components.

**Common SE failures:**
- `[T]` KPI-free download pages; placeholder text on the hub
- `[A]` three names for one report; missing period; versions without a change note; 2022 values restated in 2023 with no notice in the 2022 file

**Measured on the 2023 / 2022 PDFs:** the documents themselves score 70 / 68.
- **2023:** tagged, 307 bookmarks.
- **2022:** untagged, no bookmarks.

---

## 11. Classifier additions (extends `page-types.md` §15)

- A dated corporate announcement with dateline, spokesperson quotes and a media contact → **news**.
- The primary element is an interactive widget computing outputs from inputs → **calculator** (score the page text, including the tool panels).
- A service offer (maintenance, monitoring, consulting, modernization, managed service) → **service** (recurring) or **service_project** (one-off).
- Software → **software_hub** (≥ 3 product cards) · **software_product** · **software_trial** (sign-up/download/licence action).
- Document download page → **whitepaper_gateway** (white papers, technical guides) · **esg_report** (sustainability/ESG report pages) · **esg_hub** (report library).
- Bare PDF URL → the gateway logic of its type plus its document module.

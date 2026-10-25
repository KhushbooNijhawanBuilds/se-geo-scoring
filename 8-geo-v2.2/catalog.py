"""Hand-curated catalogue of criterion names, binary checks and per-type metadata for the
SE Content GEO Score v2.2. Weights, families, stage multipliers, gates, penalties, anchors and
caps are NOT stored here: build_docs.py / build_prompts.py read them from weights.json and
compute effective weights with geo_score_calc.py itself.

Sources (abbreviations used in SRC):
  FW   = skill/geo-research/references/scoring-framework.md (U1-U10)
  V2   = references/page-types-v2.md (10 inventory types)
  V1   = references/page-types.md (pdp, category, caas, editorial, document, datasheet, comparison, faq, glossary, video)
  TA   = research/type-analysis/*.md (only where V2/V1 leave a check unstated)
  BLOG = 3-prompts/copilot_prompt_blog_v2.1.txt (verified wording, used for the article key)
  DER  = derived here: the source gives the criterion (and sometimes a phrase list) but no binary
         checks; the phrase list was split into checks, or checks were written from the criterion name.
"""

# ---------------------------------------------------------------------------
# Universal criteria (framework wording; {fd} = U4 c2 threshold, {cadence} = U9 c4 cadence)
# ---------------------------------------------------------------------------
U = {
    "U1": ("Answer-first & prompt alignment", [
        "The first 1-2 sentences under the H1 (or the first 100 words) directly answer the primary question or define the subject.",
        "The H1/title wording matches the intent of the target prompt (descriptive, not brand-first or clever).",
        "The key message sits in the top 2-3 components (hero, banner, intro), not below the fold.",
        "Each major H2 section opens with a 1-2 sentence direct answer (40-60-word answer paragraph).",
        "A summary or key-takeaways block exists where the format allows.",
    ]),
    "U2": ("Context clarity: What / Who / When / Outcome", [
        "What it is: explicit definition or category (\"X is a ...\").",
        "Who it is for: role, segment or industry named.",
        "When it applies: scenario, trigger or application named.",
        "Outcome: a concrete result stated, owned by the offer (not \"helps you ...\").",
    ]),
    "U3": ("Extractable structure & self-containment", [
        "Descriptive H2/H3s, one idea per heading, ideally phrased as the question a buyer asks (generic labels like \"Overview\" fail).",
        "Lists for features/attributes, numbered steps for procedures, HTML-text tables for specs and comparisons with more than 2 data dimensions.",
        "Paragraphs of at most 3-4 sentences; no walls of text.",
        "Sections stand alone: subjects named; no \"as mentioned above\", \"this product\" or \"our solution\" without the name.",
        "No key fact exists only in an image, video, PDF, carousel, collapsed tab or gated form.",
    ]),
    "U4": ("Factual density & specificity", [
        "Key claims are quantified (numbers with units, ranges, timeframes, conditions).",
        "At least {fd} genuine quantified facts per 100 words (count each distinct fact once).",
        "No unanchored superlatives or marketing abstractions (\"innovative\", \"industry-leading\", \"next-gen\", \"seamless\", \"designed to help\").",
        "Precise terminology plus the customer-facing synonym (model code + plain name); acronyms defined at first use.",
        "Outcomes are specific (\"reduces peak demand charges by 10-15%\"), not generic (\"significant savings\").",
    ]),
    "U5": ("Evidence, attribution & expertise", [
        "Statistics attributed to a named source with a year.",
        "Standards or regulations cited by number where relevant (e.g. IEC 60947-2, UL 489, IEC 61850, IEC 62443).",
        "At least one attributed expert or customer quotation (na where the format does not allow quotes).",
        "First-party or original evidence (test results, field data, deployments, case metrics) with method or conditions.",
        "Provenance: a named author, reviewer or owner, or clear organizational accountability for technical/safety content.",
    ]),
    "U6": ("Fan-out coverage & focus", [
        "The target prompt is answered.",
        "Most of the 3-5 fan-out questions have a dedicated section or a direct answer.",
        "One primary intent; adjacent topics are linked out, not crammed in.",
        "Covers the facts a buyer at this stage needs (expected facts for this page type: {expected}).",
    ]),
    "U7": ("Neutral, non-promotional tone", [
        "Informational, expert voice (an advisor, not a brand talking about itself).",
        "Trade-offs, limitations or \"when not to use / when to choose another option\" are present.",
        "No hype, clickbait or stacked CTAs inside informational sections.",
        "Alternatives or competitors are named fairly where the page makes comparative or selection claims (na otherwise).",
    ]),
    "U8": ("Entity clarity & consistency", [
        "Products, ranges, standards and the brand are named explicitly and consistently (one canonical name each, consistent trademark use).",
        "Identifiers present where relevant (reference/SKU, model codes, standard numbers, versions).",
        "No internal contradictions (prose vs table vs summary, block vs page, page vs linked datasheet if provided).",
        "Descriptive link text that names the destination (na if links are not visible in the input).",
    ]),
    "U9": ("Freshness & currency", [
        "A visible publication or update date, or revision/version.",
        "Facts, statistics and standard editions are current (nothing superseded or discontinued presented as current).",
        "Lifecycle or availability status stated where relevant (active / end-of-life / replaced by a named successor; na otherwise).",
        "Updated within the cadence for this page type ({cadence}).",
    ]),
    "U10": ("Journey-stage fit & next step", [
        "Depth and content match the declared stage.",
        "Language matches the declared audience/job role.",
        "A descriptive, intent-based next-step CTA that names a specific asset, placed after the informational content and fitting the stage.",
        "Links to the logical next-stage content (e.g. guide -> range -> PDP; na if links are not visible in the input).",
    ]),
}

# ---------------------------------------------------------------------------
# Type-specific criteria: id -> (name, [checks], source, notes)
# notes = rule text that applies to the criterion (judge-applied unless encoded in level_caps)
# ---------------------------------------------------------------------------
T = {
    # ---- article (V2 §1 / BLOG) ----
    "ART-1": ("Key-takeaways block (quality)", [
        "A block of 3-5 takeaway items near the top or bottom.",
        "Each item is a standalone sentence that names its subject.",
        "At least one item carries a specific fact, number or concrete recommendation.",
        "Items match the body's claims: nothing truncated, no new claims.",
    ], "V2", ""),
    "ART-2": ("Title & subheads: descriptive, prompt-aligned, consistent", [
        "H1 names the topic in searcher language (no pun, slogan or clickbait).",
        "H1, SEO title (HTML <title>) and meta description describe the same topic and angle (pass if only the H1 is available and nothing contradicts it).",
        "At least 60% of content H2s describe their section.",
        "At least one third of H2s are phrased as, or mirror, a question a buyer asks.",
        "Any explicit promise in the HTML <title> or meta (e.g. \"3 priorities\") is delivered as visible structure (an undelivered <title>/meta-only promise fails here; G5 is only for an undelivered visible H1 promise).",
    ], "V2", ""),
    "ART-3": ("Non-commodity insight", [
        "A first-hand observation with a specific detail (number, scale or situation).",
        "An original framework, typology, decision rule or step sequence.",
        "First-party data or analysis with conditions or method.",
        "A clear, defensible thesis in one quotable sentence that goes beyond consensus.",
        "Practical, audience-specific implications (what to do, when).",
    ], "V2", ""),
    # ---- news (V2 §2) ----
    "NEWS-1": ("Headline & summary deck as the answer layer", [
        "Headline names company + named offer/partner + a concrete action (not \"advances\").",
        "Headline or deck states the single most important specific fact.",
        "A deck of 2-4 bullets, each a standalone factual sentence naming its subject.",
        "Headline uses the category/topic noun phrase a searcher would use.",
    ], "V2", ""),
    "NEWS-2": ("Temporal anchoring & dateline", [
        "Visible date with the month written out or in ISO format (numeric DD/MM fails).",
        "Dateline city.",
        "Relative timing (\"this fall\", \"early next year\") resolved to an absolute date or quarter.",
        "Milestones stated absolutely and consistent with the release date (including attachments).",
    ], "V2", ""),
    "NEWS-3": ("Claim substantiation", [
        "Quantified performance claims state their basis (study, test, pilot, baseline or conditions).",
        "\"First / only / leading / pioneering\" claims are scoped (category, geography, as-of date) or evidenced.",
        "Independent validation named: customer/pilot site, partner test, third party, or a standard by number.",
        "The evidence asset is named by title/ID and its key findings appear in the HTML (na if there is no asset).",
    ], "V2", ""),
    "NEWS-4": ("Substantive attributed quotes", [
        "At least one quote with name, title and organization.",
        "At least one quote contains a specific, checkable fact or mechanism.",
        "A third-party voice with name and role.",
        "Quotes name the offer/topic explicitly.",
    ], "V2", ""),
    "NEWS-5": ("Offer facts & availability", [
        "Availability: markets + timing.",
        "Price/pricing model, or how to obtain/join.",
        "Key specs/capabilities with units or named elements.",
        "Maturity explicit (pilot / GA / roadmap / validated to ...).",
    ], "V2", "Research releases: c2 and c4 are na. Corporate/event/financial releases: mark every check na (criterion dropped)."),
    "NEWS-6": ("Entity anchoring: About block & canonical bridge", [
        "An \"About [company]\" block in the HTML.",
        "Entity facts given (size, reach, sector; a slogan alone fails).",
        "The offer's canonical destination named by title in the text (not \"visit the web\" or the PDF only).",
        "Partner/third-party entities described at first mention.",
    ], "V2", ""),
    # ---- solution (V2 §3) ----
    "SOL-1": ("Problem quantified & sourced", [
        "A specific problem for the named segment.",
        "At least one quantified problem fact.",
        "The problem fact is attributed to a named source (+ year).",
        "The problem is stated in the top block (within about 150 words after the H1).",
    ], "V2", ""),
    "SOL-2": ("How it works: architecture & components", [
        "Prose (2+ sentences) on how at least 2 components work together.",
        "At least 3 components named canonically, each with a functional role.",
        "Interoperability named (protocols, standards, third-party/legacy systems).",
        "At least one quantified technical parameter.",
        "All of this is in page text, not only in an image, video, PDF or \"...\"-truncated teaser (text in a collapsed tab counts here; tab-only key facts are penalised once, under U3 c5).",
    ], "V2", ""),
    "SOL-4": ("Outcomes quantified with basis", [
        "At least 2 quantified outcomes.",
        "At least one outcome attributed to a named offer.",
        "At least one outcome states its basis (baseline, conditions, method or source).",
        "KPIs the persona measures.",
        "Every footnote/asterisk resolves to visible text (na if there are none).",
    ], "V2", ""),
    "SOL-5": ("Proof: references & validation", [
        "At least one named customer reference.",
        "At least one reference with a quantified result on this page.",
        "The reference is relevant to the segment.",
        "Named third-party validation.",
        "Reference context, or a named, attributed quote.",
    ], "V2", ""),
    "SOL-7": ("Applicability, scope & fit", [
        "At least 3 specific applications with context.",
        "Scope boundaries (scale range, new-build vs retrofit, single site vs portfolio, regions).",
        "Fit guidance (\"choose X when ...\", when it is not suited).",
        "Compatibility with the installed base (brownfield, multi-vendor, prerequisites).",
    ], "V2", ""),
    "SOL-8": ("Implementation path & delivery model", [
        "Phases in order.",
        "What each phase delivers.",
        "Who delivers (SE teams, certified partners) + lifecycle services.",
        "A numeric timeline or effort indication.",
    ], "V2", ""),
    # ---- service (V2 §4) ----
    "SVC-1": ("Scope & deliverables", [
        "At least 3 concrete included activities/deliverables.",
        "Deliverables are specific (what is done, to what, which artifact is received), not benefits.",
        "Remote vs on-site split, or frequency/cadence.",
        "Exclusions, limits, options or add-ons.",
        "Scope is in text on this page, not only in a brochure, PDF or child page (text in a collapsed tab counts here; tab-only key facts are penalised once, under U3 c5).",
    ], "V2", ""),
    "SVC-2": ("Service levels & commitments", [
        "Coverage hours.",
        "Response/time-to-site as a number + unit.",
        "Another measurable commitment (restore time, visits/year, report turnaround, detection-to-notification).",
        "Escalation path.",
        "Conditions (tier, region, contract).",
    ], "V2", ""),
    "SVC-3": ("Eligible assets & prerequisites", [
        "Equipment categories named.",
        "Specific ranges/models/generations named.",
        "Multi-vendor/third-party coverage stated.",
        "Eligibility conditions or a migration path.",
    ], "V2", ""),
    "SVC-4": ("Process / how it works", [
        "Steps in order.",
        "Each step explained.",
        "Roles (customer vs SE hub/engineer).",
        "How the engagement starts.",
    ], "V2", ""),
    "SVC-5": ("Plans, contract & commercial model", [
        "Named tiers/plans (or one plan stated).",
        "Differences between plans stated (table preferred).",
        "Contract/pricing model or price drivers (prices are not required).",
        "Geographic availability.",
    ], "V2", ""),
    "SVC-6": ("Outcomes quantified with basis", [
        "At least 2 quantified outcomes of the named service.",
        "At least one outcome attributed to the named service.",
        "At least one outcome states its basis (baseline, conditions, method or source).",
        "KPIs the persona measures.",
        "Every footnote/asterisk resolves to visible text (na if there are none).",
    ], "V2", "Same as SOL-4 c1-c5, applied to the named service."),
    "SVC-7": ("Proof & delivery credentials", [
        "A named, relevant customer reference.",
        "A reference with a quantified result.",
        "Delivery credentials (engineer numbers/qualifications, named hubs/SOC/centres, installed base).",
        "Service standards by number (NFPA 70B/70E, IEC 62443-2-4, ISO 27001 ...).",
        "An attributed quote or named third-party validation.",
    ], "V2", ""),
    # ---- range (V2 §5) ----
    "RNG-1": ("Member comparison table with \"best for\"", [
        "An HTML-text table (not image, PDF or configurator).",
        "Rows = members, with at least 3 shared decision attributes.",
        "Values with units, one per cell.",
        "A \"best for\" column.",
        "The table covers all members shown.",
    ], "V2", ""),
    "RNG-2": ("Selection guidance in text", [
        "Explicit conditional choice statements for at least 2 members (\"Choose VL for 200-500 kW ...\"); card \"Ideal for ...\" lines don't count.",
        "Selection axes named with thresholds + units.",
        "Selection is possible from the text alone (not only via the Product Selector).",
        "Overlapping members are disambiguated.",
    ], "V2", ""),
    "RNG-3": ("Applications, segments & references", [
        "At least 3 named segments/applications.",
        "Applications attached to specific members.",
        "At least one named reference with a metric.",
    ], "V2", ""),
    "RNG-4": ("Quantified differentiators", [
        "At least one range-level claim with number + unit.",
        "The measurement basis is stated.",
        "No unanchored superlatives.",
    ], "V2", ""),
    "RNG-5": ("Ecosystem, compatibility & protocols", [
        "Accessories with their function.",
        "Protocols/connectivity named.",
        "Cross-range compatibility.",
        "Monitoring/management software named.",
    ], "V2", ""),
    "RNG-6": ("Standards & certifications", [
        "At least one product standard by number.",
        "Standards mapped to members/regions (IEC vs UL).",
        "Certifications/declarations named.",
    ], "V2", ""),
    "RNG-7": ("Range FAQ", [
        "At least 3 Q&As.",
        "They cover selection, compatibility or migration.",
        "Direct answer first, with the range/member named.",
    ], "V2", ""),
    "RNG-8": ("Lifecycle, legacy names & migration", [
        "Former names stated (\"formerly Vigirex\").",
        "Successor path for legacy members.",
        "Lifecycle status of members.",
        "Generation identifiers.",
    ], "V2", ""),
    "RNG-9": ("Member descriptors", [
        "Every member has a descriptor beyond its name (category noun + function).",
        "At least 75% of members carry a key rating with unit.",
        "At least 50% state an application or \"best for\".",
        "Descriptors are unique: different members do not share copy-pasted text (the same card rendered twice is penalised once, by the template_artifact penalty, not here).",
        "No off-topic cards inside the range content.",
    ], "V2", "Judged over the product members only: variants or sub-ranges of the named family (sub-ranges on master ranges). Accessory, battery, software/app and service cards are NOT members: judge them under RNG-5 (ecosystem); they fail c5 only if they are unrelated to the range."),
    # ---- software (V2 §6) ----
    "SW-1": ("Capabilities & use cases", [
        "At least 3 capabilities as concrete functions (verb + object + context).",
        "Capabilities mapped to named modules/editions/products.",
        "At least one capability with a measurable parameter.",
        "Use cases named.",
        "No label-only tiles.",
    ], "V2", ""),
    "SW-2": ("Integrations, protocols & interoperability", [
        "Named protocols/standards (BACnet, Modbus, SNMP, OPC UA, MQTT, IEC 61850 ...).",
        "Named third-party systems/device families.",
        "Integration method (API, connectors, gateways).",
        "\"Agnostic/open\" claims backed by specifics (na if there is no such claim).",
    ], "V2", ""),
    "SW-3": ("Deployment, architecture & requirements", [
        "Software deployment model (SaaS / on-prem / hybrid / edge) - only statements about where the software itself runs count, not where the customer's infrastructure sits.",
        "Scale/limits or architecture.",
        "System requirements stated or linked by name.",
        "Implementation/onboarding path.",
    ], "V2", ""),
    "SW-4": ("Security, privacy & compliance", [
        "Concrete security controls.",
        "Certifications by number (IEC 62443-x-x, ISO/IEC 27001, SOC 2).",
        "Privacy/data residency.",
        "A named security resource (trust center, vulnerability disclosure).",
    ], "V2", ""),
    "SW-5": ("Licensing, pricing model & trial", [
        "Licence model.",
        "Price/range, or an explicit price-driver/channel statement.",
        "Trial with at least 2 terms (duration, scope, cost, data, expiry).",
        "How to acquire/activate.",
    ], "V2", ""),
    "SW-6": ("Proof & quantified outcomes", [
        "Named customer + an achieved quantified outcome.",
        "Outcome with baseline, timeframe or method.",
        "Third-party validation with year.",
        "Page statistics are attributed and visible as numbers.",
    ], "V2", ""),
    "SW-7": ("Product/edition map & selection", [
        "Products/editions with one-line differentiation.",
        "\"Which product for which need\" guidance.",
        "A comparison table of editions/products.",
        "Relationships explained (e.g. Expert vs Advisor; on-prem vs cloud; SE vs AVEVA).",
    ], "V2", ""),
    "SW-8": ("Versions, lifecycle & former names", [
        "Current version / what's new, with date.",
        "Former names stated.",
        "Support lifecycle or release notes named.",
    ], "V2", ""),
    # ---- case study (V2 §7) ----
    "CS-1": ("Outcome-led title + answer-shaped summary", [
        "Title/H1 names the customer (or an anonymized customer type). Title/H1 = the visible H1 or the HTML <title>; either one passes.",
        "Title/H1 states the outcome or problem solved (not a slogan). The visible H1 or the HTML <title> may pass it.",
        "A 40-150-word prose summary within the first ~150 body words.",
        "The summary covers at least 4 of who / problem / solution / result / timeframe.",
        "The summary contains a quantified result with timeframe.",
    ], "V2", ""),
    "CS-2": ("Customer profile", [
        "Industry stated in the body.",
        "Size/scale.",
        "Country/region.",
        "Application/scope.",
    ], "V2", "Meta-only facts fail."),
    "CS-3": ("Quantified results with baseline & timeframe", [
        "At least one customer outcome with unit.",
        "At least 2 distinct quantified outcomes.",
        "Baseline stated.",
        "Timeframe/period stated.",
        "Result attributed to the named offer.",
        "The primary outcome leads.",
    ], "V2", "Vanity numbers (years of relationship, floor area, parts) and targets fail c1/c2."),
    "CS-4": ("Challenge -> solution -> results in text", [
        "A specific challenge.",
        "What was deployed, where, how, by whom.",
        "Results in text.",
        "Segmented under labels, each section naming the customer.",
    ], "V2", "Tab labels with no panel text fail."),
    "CS-5": ("Attributed customer quote", [
        "A direct customer quote in text.",
        "Speaker named.",
        "Role + organization.",
        "Substantive (reason, fact or outcome).",
    ], "V2", "Vendor-employee quotes don't count."),
    "CS-6": ("Offers named with their role", [
        "Exact commercial names of the offers.",
        "Role of the main offer explained in text.",
        "Each offer shown as a named card/link.",
    ], "V2", "Card grids alone reach at most level 2 (judge-applied: downgrade to proposed_level 2 with downgrade_reason naming c3, the card check)."),
    "CS-7": ("Metric methodology / verifiability", [
        "How the result was measured.",
        "Measurement boundary/period.",
        "Data source or third-party verification.",
    ], "V2", ""),
    # ---- calculator (V2 §8) ----
    "CALC-1": ("Method / formula", [
        "Calculation logic (formula or steps: inputs -> intermediates -> outputs).",
        "Variables with units.",
        "Model provenance (who built it; which white paper/standard it implements).",
        "Scope/limits of validity.",
        "A simple case could be reproduced by hand.",
    ], "V2", ""),
    "CALC-2": ("Assumptions & default values", [
        "Key assumptions listed.",
        "Each assumption with value + unit.",
        "Source and data year.",
        "Default scenario values.",
        "Region/currency/price-year basis (na if region-independent).",
    ], "V2", ""),
    "CALC-3": ("Worked example & representative results", [
        "At least one complete example (inputs -> outputs with units) in text/table.",
        "Typical ranges/benchmarks.",
        "Key drivers/sensitivity quantified.",
        "Results in text/table, not only a chart/UI.",
    ], "V2", ""),
    "CALC-4": ("Inputs & outputs defined", [
        "Every required input listed.",
        "Inputs defined (meaning, unit, range).",
        "Output metrics defined.",
        "Acronyms expanded.",
    ], "V2", ""),
    "CALC-5": ("Interpretation & decision guidance", [
        "How to read the result.",
        "A \"choose/do X if ...\" or trade-off rule.",
        "Levers to improve the result.",
        "Uncertainty/limits of interpretation.",
    ], "V2", ""),
    # ---- white paper gateway (V2 §9) ----
    "WP-1": ("Abstract quality", [
        "90-220 words and the visible abstract is not truncated (a hidden or truncated second copy is penalised once, by the template_artifact penalty, not here).",
        "Problem named.",
        "Audience named.",
        "Approach/contents stated.",
        "Main conclusion stated specifically (not \"guidance is provided\").",
        "Copy-clean (no merged words or encoding errors).",
    ], "V2", ""),
    "WP-2": ("Key findings in HTML", [
        "Findings enumerated as discrete items.",
        "At least 2 quantified findings with units/conditions.",
        "Findings placed above the download block.",
        "At least one non-commodity SE finding (SE analysis, model or field data, with condition).",
        "Implications/actions stated.",
    ], "V2", "WP-2 at level 1 or below means the core content is only in the PDF: trigger G6."),
    "WP-3": ("Questions answered / coverage", [
        "At least 3 specific topics beyond the title.",
        "Topics given as question-style or descriptive headings.",
        "At least 3 of the 5 inferred fan-outs answered by at least one sentence in the HTML.",
        "One primary intent.",
    ], "V2", ""),
    # ---- ESG (V2 §10) ----
    "ESG-1": ("Headline KPI layer", [
        "At least 3 headline KPIs with value + unit.",
        "GHG emissions by scope (1; 2 market/location; 3) in tCO2e.",
        "Each KPI with reporting period + boundary.",
        "KPIs as rows that extract cleanly (label / unit / value; not chart-only).",
        "Year-on-year or vs-baseline comparison.",
    ], "V2", ""),
    "ESG-2": ("Targets, baselines & progress", [
        "Named targets.",
        "Baseline year + target year.",
        "Current progress per target.",
        "External validation (SBTi) or status, including missed/at-risk targets.",
        "Link to the transition plan/methodology.",
    ], "V2", ""),
    "ESG-3": ("Reporting basis & methodology", [
        "Frameworks named (CSRD/ESRS, GRI, ISSB/TCFD, SASB).",
        "GHG Protocol + market/location basis.",
        "Reporting period + organizational boundary.",
        "Restatements/methodology changes disclosed.",
    ], "V2", ""),
    "ESG-4": ("Assurance & ratings", [
        "Assurance level + provider.",
        "Scope of assured indicators.",
        "Ratings/validations with date (CDP, MSCI, EcoVadis, SBTi).",
        "Assurance statement included or linked.",
    ], "V2", ""),
    "ESG-5": ("Navigation & machine-readable companions", [
        "Each report entry gives type + period + release date.",
        "A 1-2-sentence description of the contents.",
        "Companion links (data annex XLSX/CSV, GRI/ESRS index, CDP; XBRL).",
        "Descriptive anchors.",
        "Current vs archived editions labelled.",
    ], "V2", ""),
    # ---- PDP (V1 §1; checks split from the phrase list) ----
    "PDP-1": ("Spec table completeness & quality", [
        "Specs in an HTML-text table or list (not image/PDF-only).",
        "Each spec gives attribute name + value + unit.",
        "Specs grouped (electrical / mechanical / environmental / communication).",
        "No \"N/A\" filler.",
        "Covers the category's key attributes (about 8-10 top specs or more).",
    ], "V1-split", "Level 5 needs at least 95% of the category's required attributes (judge-applied)."),
    "PDP-2": ("Applications & use cases", [
        "At least 3 specific application noun phrases (\"for EV charging and PV installations where DC fault currents can occur\").",
        "Environments/operating conditions stated.",
        "Exclusions or when not to use.",
    ], "V1-split", ""),
    "PDP-3": ("Compatibility & ecosystem", [
        "Compatible accessories / complementary products.",
        "Protocols and software compatibility.",
        "Predecessor/successor references.",
        "Each named with a descriptive link.",
    ], "V1-split", ""),
    "PDP-4": ("Standards & certifications", [
        "Standards cited by number, with edition where relevant (IEC / UL / EN / CE / UKCA / RoHS / REACH / PEP / EPD / IEC 62443 ...).",
        "Proof document linked.",
    ], "V1-split", ""),
    "PDP-5": ("Product Q&A", [
        "At least 3 real buyer questions (5 or more for level 5).",
        "The first sentence of each answer answers directly.",
        "Answers are 40-80 words in total.",
        "Answers name the product.",
        "Questions sourced from support, sales or prompt research.",
    ], "V1-split", ""),
    "PDP-6": ("Differentiation & selection vs siblings", [
        "A \"Choose this if ...\" statement.",
        "How it differs from range siblings or the previous generation, quantified.",
        "Link to the range comparison.",
    ], "V1-split", ""),
    "PDP-7": ("Proof", [
        "Substantive reviews/ratings (B2C) or references / installed base (B2B).",
        "Case-study links with metrics.",
    ], "V1-split+DER", ""),
    "PDP-8": ("Commercial & lifecycle facts", [
        "Where to buy / availability.",
        "Warranty.",
        "Lifecycle status (active / EOL / replaced by a named reference).",
        "Substitutes.",
    ], "V1-split", ""),
    "PDP-9": ("Documents & media described", [
        "Datasheet, manual, CAD/BIM, EPD linked with descriptive anchors.",
        "Key facts from those documents mirrored in the HTML.",
        "Videos/images have descriptive titles + 3-4-bullet summaries.",
    ], "V1-split", ""),
    # ---- category (V1 §3) ----
    "CAT-1": ("\"How to choose\" with thresholds", [
        "4-8 selection criteria are given.",
        "Each criterion is explained with units/thresholds (breaking capacity, trip curve, pole count, ambient temperature ...).",
    ], "V1-split", ""),
    "CAT-2": ("Type comparison table + \"best for\"", [
        "An HTML-text table compares the category's types (e.g. residential / commercial / industrial; AC / DC).",
        "Shared attributes with units for every type.",
        "A \"best for\" statement per type.",
    ], "DER", ""),
    "CAT-3": ("Featured ranges, neutral positioning", [
        "A one-line factual \"best for\" per featured range.",
        "No self-congratulation.",
    ], "V1-split", ""),
    "CAT-4": ("Standards / regulations", [
        "Governing standards/regulations cited by number.",
        "Standards mapped to types or regions (e.g. IEC vs UL).",
    ], "DER", ""),
    "CAT-5": ("Category FAQ", [
        "FAQ answers definition questions.",
        "FAQ answers differences between types.",
        "FAQ answers sizing questions.",
    ], "V1-split", ""),
    "CAT-6": ("Links to guides / glossary / tools", [
        "Links to selection guides, glossary entries or tools.",
        "Descriptive anchors.",
    ], "V1-split", ""),
    # ---- CaaS (V1 §4) ----
    "BLK-1": ("Self-containment", [
        "Subject named explicitly (no \"this product\", \"our solution\").",
        "Makes sense when lifted alone.",
    ], "V1-split", "Banner/hero test: if an AI reading only the banner cannot say what, who, when and outcome, BLK-1 <= 3 (judge-applied)."),
    "BLK-2": ("One idea + descriptive heading", [
        "A single message.",
        "The title describes it (not a campaign name).",
    ], "V1-split", ""),
    "BLK-3": ("Factual specificity", [
        "The claim has a number, unit, condition or timeframe.",
        "Outcome-solution-timeframe link (\"reduced energy costs by 15% in six months with [named module]\").",
    ], "V1-split", ""),
    "BLK-4": ("Consistency with canonical data", [
        "Matches the PDP/spec/claim source.",
        "Dated or versioned.",
    ], "V1-split", ""),
    "BLK-5": ("Parameterization / non-duplication", [
        "Not identical boilerplate across many pages.",
        "Variables (product, rating, region) filled in.",
    ], "V1-split", ""),
    "BLK-6": ("Neutral tone", [
        "Informational, expert voice (an advisor, not a brand talking about itself).",
        "Trade-offs or limitations present where relevant (na for very short blocks).",
        "No hype, clickbait or stacked CTAs.",
    ], "DER", "No checks in the source; derived from U7."),
    "BLK-7": ("Localization correctness", [
        "Units correct for the country.",
        "Standards correct for the country (IEC vs UL).",
        "Regional availability caveats stated where relevant.",
    ], "V1-split", ""),
    "BLK-8": ("Descriptive CTA", [
        "The CTA names what the user gets (\"Read the Le Grand Monarque Hotel case study\"), not \"Learn more\".",
    ], "V1-split", ""),
    "BLK-9": ("One primary outcome", [
        "A single lead outcome.",
        "Headline and body aligned.",
        "Long forms use scannable bullets (na for short forms).",
    ], "V1-split", "Banner/hero test failure -> BLK-9 <= 3 (judge-applied)."),
    # ---- document family (V1 §7, V2 §9-10, TA) ----
    "DOC-1": ("HTML gateway / summary layer", [
        "An indexable landing page or ungated summary exists.",
        "It gives the document title.",
        "A 100-200-word abstract.",
        "Key specs/findings as bullets or a table.",
        "The questions the document answers.",
        "Date/version.",
        "A download link.",
    ], "V1-split", ""),
    "DOC-2": ("Lead with the fact; one topic per heading", [
        "Each section opens with the spec/fact.",
        "Headings read like the question they answer.",
        "Multi-topic sections are split.",
    ], "V1-split", "Manuals/installation guides: numbered steps and safety warnings are required."),
    "DOC-3": ("Specs in tables", [
        "Parallel attributes in rows/columns.",
        "Consistent labels and units across the library.",
        "One value per cell.",
    ], "V1-split", ""),
    "DOC-4": ("Text-extractable, structured file", [
        "Real text layer (not scanned).",
        "Real heading hierarchy.",
        "Single-column layout where possible.",
        "Tables are real tables.",
    ], "V1-split", ""),
    "DOC-5": ("Descriptive title, filename & metadata", [
        "Descriptive file name (e.g. \"SmartUPS-SMX3000-Datasheet-EN.pdf\").",
        "Document title set.",
        "No placeholder title (e.g. \"Document1\").",
    ], "V1-split", ""),
    "DOC-6": ("Customer language", [
        "Model codes paired with plain names (\"Smart-UPS SMX3000RMLV2U (3000VA/2700W rack-mount UPS)\").",
        "Acronyms defined at first use.",
        "Customer phrasing (\"operating temperature range\", not \"env. spec\").",
    ], "V1-split", ""),
    "DOC-7": ("Version, date, changelog, supersession", [
        "Visible \"Rev. N, updated Month YYYY\".",
        "A changelog.",
        "Superseded versions retired or marked.",
    ], "V1-split", ""),
    "DOC-8": ("Methodology / test conditions / references", [
        "Method (white papers) or test conditions for ratings (datasheets) stated.",
        "References or the standards behind the ratings cited by number.",
        "Named authors (white papers; na for datasheets).",
    ], "V1-split", ""),
    "DOC-9": ("Gate the deep dive, not the knowledge", [
        "Key findings visible before the form.",
        "Definitions/framework visible before the form.",
        "The form asks only what is needed.",
    ], "TA", "Only if the asset is gated; otherwise mark all checks na (criterion dropped, weight redistributed)."),
    # ---- comparison (V1 §9) ----
    "CMP-1": ("Neutral comparison table", [
        "Same attributes and units for every option.",
        "Sources given for competitor/alternative data.",
    ], "V1-split", ""),
    "CMP-2": ("Explicit criteria + \"choose X if ...\" verdicts", [
        "Decision criteria stated explicitly.",
        "A \"choose X if ...\" verdict for each option.",
    ], "DER", ""),
    "CMP-3": ("Honest trade-offs", [
        "Trade-offs stated for each option.",
        "Limitations of the SE option included.",
    ], "V1-split+DER", ""),
    # ---- FAQ (V1 §10) ----
    "FAQ-1": ("Real buyer questions as headings", [
        "Natural-language questions sourced from support, sales or prompts.",
        "Questions are real heading tags.",
    ], "V1-split", ""),
    "FAQ-2": ("Direct answer first", [
        "The first sentence answers (under 25 words).",
        "Answers total 40-80 words.",
        "No \"it depends\" when a concrete answer exists.",
        "The answer does not end in a CTA instead of an answer.",
    ], "V1-split", ""),
    "FAQ-3": ("Self-contained, one entity per answer", [
        "Product/range named in the answer.",
        "No keyword stacking.",
    ], "V1-split", ""),
    "FAQ-4": ("Lists/tables for steps, specs, comparisons", [
        "Numbered lists for steps (na if no procedure).",
        "Tables for specs or comparisons (na if none).",
    ], "DER", ""),
    "FAQ-5": ("Applies-to & identifiers", [
        "Models/references the answer applies to, in text.",
        "Error codes in text (na unless troubleshooting).",
    ], "V1-split", ""),
    "FAQ-6": ("One page per topic/product", [
        "The page covers one topic/product (not a global mega-FAQ).",
    ], "V1-split", ""),
    "FAQ-7": ("Links to docs & next step", [
        "Links to the relevant documents (manual, datasheet) with descriptive anchors.",
        "A next step stated.",
    ], "DER", ""),
    # ---- glossary (V1 §11, no checks in source) ----
    "GLO-1": ("Definition in the first sentence (\"X is ...\")", [
        "The first sentence defines the term (\"X is ...\").",
        "The definition names the category and the distinguishing property.",
        "The definition stands alone without the rest of the page.",
    ], "DER", ""),
    "GLO-2": ("Formula, units, governing standard", [
        "Formula given in text (na if the term is not quantitative).",
        "Units stated.",
        "Governing standard cited by number.",
    ], "DER", ""),
    "GLO-3": ("Example / application", [
        "At least one worked or concrete example.",
        "An application context named.",
    ], "DER", ""),
    "GLO-4": ("Disambiguation & related terms", [
        "Confusable terms disambiguated (e.g. kVA vs kW).",
        "Related terms named or linked.",
    ], "DER", ""),
    "GLO-5": ("Links to products/guides", [
        "Links to relevant products or guides.",
        "Descriptive anchors.",
    ], "DER", ""),
    # ---- video (V1 §13) ----
    "VID-1": ("AI-friendly video type", [
        "The video is a tutorial, how-to, FAQ, comparison, case study or expert insight (brand films fail).",
    ], "V1-split", ""),
    "VID-2": ("Descriptive, intent-framed title", [
        "Factual title.",
        "Question or \"how to\" form.",
        "Product + brand named.",
    ], "V1-split", ""),
    "VID-3": ("Description", [
        "A 2-paragraph summary including the questions answered.",
        "Bullets.",
        "300+ words.",
        "Link to the SE page.",
    ], "V1-split", ""),
    "VID-4": ("Answer early", [
        "Problem + short answer in the first 30-90 seconds (check the transcript).",
    ], "V1-split", ""),
    "VID-5": ("Transcript / captions", [
        "Human-reviewed captions (.SRT).",
        "Product names and acronyms correct.",
        "Voice-over present.",
    ], "V1-split", ""),
    "VID-6": ("Chapters", [
        "Question-style chapter titles.",
        "Chapters start at 00:00.",
        "At least 3 timestamps.",
    ], "V1-split", ""),
    "VID-7": ("Published on an SE page with text context", [
        "Embedded on a crawlable SE page.",
        "With a title + 3-4-bullet summary.",
        "Transcript on the page.",
    ], "V1-split", ""),
    "VID-8": ("Fact-based, consistent terminology, recap", [
        "Fact-based (specific facts, not brand claims).",
        "Consistent terminology.",
        "A recap at the end.",
    ], "DER", ""),
}

# ---------------------------------------------------------------------------
# Per-type overrides of names/checks, and type rules attached to criteria
#   checks: full replacement list ; name: replacement name ; rule: extra rule text ; src
# ---------------------------------------------------------------------------
BLOG_U = {  # verbatim from copilot_prompt_blog_v2.1.txt
    "U1": ("Insight / answer in paragraph 1", [
        "The first 1-2 sentences under the H1 (or the first 100 words) directly answer the target prompt or define the subject. A Summary block directly under the byline counts.",
        "The H1/title wording matches the intent of the target prompt (descriptive, not brand-first or clever).",
        "The key message sits in the top 2-3 components (hero, deck, intro).",
        "At least 80% of H2 sections open with a 1-2 sentence direct answer.",
        "A summary or key-takeaways block exists.",
    ]),
    "U3": ("Extractable structure and self-containment", [
        "Descriptive H2/H3s, one idea per heading (generic labels like \"Overview\" fail).",
        "Lists for features/attributes, numbered steps for procedures, tables for comparisons with more than 2 dimensions.",
        "Paragraphs of at most 3-4 sentences; no walls of text.",
        "Sections stand alone: subjects named; no \"as mentioned above\", \"the above\", or unnamed \"this product / our solution\".",
        "No key fact exists only in an image, video, PDF, carousel, collapsed tab or gated form.",
    ]),
    "U4": ("Factual density and specificity", [
        "Key claims are quantified (numbers with units, ranges, timeframes, conditions).",
        "At least 1.0 genuine quantified facts per 100 words (count each distinct fact once).",
        "No unanchored superlatives or marketing abstractions in the informational sections (\"innovative\", \"industry-leading\", \"seamless\", \"game-changing\").",
        "Precise terminology plus the plain-language synonym; acronyms defined at first use.",
        "Outcomes are specific (\"cuts commissioning from 6 to 4 weeks\"), not generic (\"significant savings\").",
    ]),
    "U5": ("Evidence, attribution and expertise", [
        "Statistics attributed to a named source with a year.",
        "Standards or regulations cited by number where relevant (e.g. IEC 60947-2, NFPA 70E, ISO/IEC 27001).",
        "At least one quote from a named person OTHER than the author.",
        "First-party or original evidence (test results, field data, deployments) with method or conditions.",
        "A named human author whose role or experience is visible (\"Guest Blogger\" or \"Admin\" fails).",
    ]),
    "U6": ("Fan-out coverage and focus", [
        "The target prompt is answered.",
        "Most of the 3-5 fan-out questions have a dedicated section or a direct answer.",
        "One primary intent; adjacent topics are linked out, not crammed in.",
        "Covers the facts a reader at this stage needs (e.g. prerequisites, costs, limits, how it works).",
    ]),
    "U7": ("Neutral, non-promotional tone", [
        "Informational, expert voice (an advisor, not a brand talking about itself).",
        "Trade-offs, limitations or \"when not to use\" are present.",
        "No hype, clickbait or stacked CTAs in informational sections (one descriptive closing offer is allowed).",
        "Alternatives or competitors are named fairly where the page makes comparative claims (na otherwise).",
    ]),
    "U8": ("Entity clarity and consistency", [
        "Products, brands and standards are named explicitly and consistently (one canonical name each).",
        "Identifiers present where relevant (model codes, standard numbers, versions, product URLs).",
        "No internal contradictions (prose vs table vs summary).",
        "Descriptive link text that names the destination (na if links are not visible in the input).",
    ]),
    "U9": ("Freshness", [
        "A visible publication or update date.",
        "Facts, statistics and standard editions are current (nothing superseded presented as current).",
        "Lifecycle or availability status stated where relevant (na otherwise).",
        "Updated within the cadence for blogs (at least yearly).",
    ]),
    "U10": ("Stage fit and next step", [
        "Depth and content match the declared stage.",
        "Language matches the declared audience.",
        "A descriptive next-step CTA that names a specific asset, placed after the informational content.",
        "Links to the logical next-stage content (na if links are not visible in the input).",
    ]),
}
BLOG_T = {"ART-1": "Key-takeaways block (quality)", "ART-2": "Title and subheads", "ART-3": "Non-commodity insight"}

WP_DOC7 = ("Version, date, supersession", [
    "Visible release/update date.",
    "Page version = file-name version.",
    "A change note when the version is above 1.0 (use the higher of the page version and the file-name version).",
    "Released or reviewed within the last 24 months.",
    "Related/superseding editions linked, or \"current edition\" stated (a hidden \"Latest version\" label counts as text).",
])
ESG_DOC7 = ("Edition, period vs release date, change note, supersession", [
    "Visible release/update date.",
    "Reporting period stated, distinct from the release date.",
    "Change note / restatements flagged when values changed.",
    "The page/file itself says whether this is the current edition (\"latest\", \"superseded by ...\", or an edition list on the page); judge only what the supplied content states, never outside knowledge.",
    "Related/superseding editions linked, or \"current edition\" stated.",
])
WP_DOC5 = ("Title, file name & metadata", [
    "Descriptive title.",
    "Descriptive file name (subject words, not code-only).",
    "Document type in words on the page (\"White paper 126\").",
    "Complete, non-truncated meta description.",
])
ESG_DOC5 = ("Title, file name & metadata", [
    "Descriptive title.",
    "Descriptive file name (subject words, not code-only).",
    "Document type in words on the page (\"Sustainability report 2024\", \"Universal Registration Document 2024\").",
    "Complete, non-truncated meta description.",
])
WP_DOC8 = ("Methodology, authorship & references", [
    "Named author(s) with role.",
    "Method/assumptions stated.",
    "References/standards cited by number.",
    "First-party evidence with conditions.",
    "Publisher + document number.",
])
WPDOC_DOC1 = ("Executive summary layer (document)", [
    "An executive summary with key findings on pages 1-2.",
    "At least 2 quantified findings in it.",
    "Scope/questions stated.",
    "A link back to the gateway URL.",
    "Findings in prose, not only in infographics.",
])
ESGDOC_DOC1 = ("Highlights layer (document)", [
    "A highlights/summary section with headline KPIs within the first 5 pages.",
    "Highlight KPIs give their basis (scope, period, boundary).",
    "Report scope/questions stated.",
    "Points back to the HTML report home.",
    "Highlights in text, not only in infographics.",
])
ESGDOC_DOC4 = ("Text-extractable file", [
    "No scanned content pages (a blank or image-only cover/divider page does not fail it). na unless extraction metadata or page images are supplied.",
    "Tagged PDF. na unless extraction metadata is supplied.",
    "Tables are real tables (rows and columns extract in order).",
    "Reading order and units extract cleanly (no split subscripts or chart junk).",
])  # v2.2: "Bookmarks/outline" removed here; it is judged once, under ESG-5 c2
ESGDOC_ESG5 = ("Navigation & machine-readable companions (document)", [
    "Table of contents with page numbers.",
    "Bookmarks/outline (the only place bookmarks are judged). na unless extraction metadata is supplied.",
    "Content index (GRI / SASB / TCFD / ESRS).",
    "Companion data referenced.",
    "Cross-references are accurate. na unless a printed-page to PDF-page mapping or extraction metadata is supplied.",
])
SVCP_SVC2 = ("Service levels & commitments (project variant)", [
    "Lead time to start.",
    "Duration or downtime window with a number.",
    "Turnaround, guarantee or warranty on the work.",
    "Support during and after the project.",
    "Conditions of the project commitments (scope boundary, site/outage prerequisites, contract or warranty terms).",
])
CS_U9 = ("Freshness & currency", [
    "Publish date or project/results date visible.",
    "Results are at most 3 years old, or dated.",
])
CALC_U9 = ("Freshness & currency", [
    "Model version/date visible.",
    "Data year at most 2 years old, or stated.",
    "Lifecycle or availability status stated where relevant (na otherwise).",
    "Reviewed at least yearly.",
])
WP_U1 = ("Answer-first title & abstract lead", [
    "The first 1-2 abstract sentences state the thesis/answer, not background.",
    "The title matches the prompt intent.",
    "The key message sits above the metadata block.",
    "Any content sections open with an answer.",
    "A summary/takeaways block exists.",
])
WP_U10 = ("Stage fit & next step", [
    "Depth fits Education/Consideration.",
    "Language matches the declared audience.",
    "A descriptive download CTA (\"Download white paper 126: Retrofitting ..., PDF 1.4 MB\").",
    "Links to related papers, TradeOff tools and solutions (na if links are not visible in the input).",
])

OVR = {
    "article": {**{k: {"name": v[0], "checks": v[1], "src": "BLOG"} for k, v in BLOG_U.items()},
                **{k: {"name": v, "src": "BLOG"} for k, v in BLOG_T.items()},
                "U9": {"name": BLOG_U["U9"][0], "checks": BLOG_U["U9"][1], "src": "BLOG", "rule": "Level 5 only with a visible \"Updated\" date plus refreshed statistics (judge-applied)."}},
    "news": {
        "U2": {"name": "Lede: What / Who / When / Outcome", "rule": "Judged on headline + deck + first paragraph."},
        "U4": {"rule": "Repeated numbers count once."},
        "U3": {"rule": "Template H2s (Spokespeople, Attached files, Share) are excluded. c1 fails when visible subheads are plain text, not headings."},
        "U6": {"rule": "Roundups of several announcements fail c3."},
        "U7": {"rule": "c2 passes on any stated limitation or scope limit."},
        "U8": {"rule": "One canonical offer name throughout."},
    },
    "solution": {
        "U1": {"name": "Answer-first definition & prompt alignment", "rule": "c2 passes if the title OR the H1 contains the seed prompt's core noun phrase; it fails if the H1 is a slogan AND the title is brand-first/vague."},
        "U3": {"rule": "\"...\"-truncated teasers and empty tab panels fail c4/c5. Cloned carousel slides are duplicates: template_artifact penalty only."},
        "U5": {"name": "Evidence: sources & standards", "rule": "c2 counts sector standards/regulations (IEC 62443, NIS2, ASHRAE 170, IEC 61850 ...)."},
        "U6": {"rule": "c4 expected facts = the SOL must-haves (problem, architecture, outcomes, proof, scope, implementation)."},
        "U9": {"rule": "Undated -> U9 max 1."},
        "U10": {"rule": "The global \"Need help?\" block does NOT pass c3; a topic-specific descriptive CTA does."},
    },
    "service": {
        "U1": {"name": "Answer-first service definition", "rule": "c1 needs the definition in the BODY (the meta description does not count)."},
        "U3": {"rule": "Tab bars with empty panels fail c5."},
        "U9": {"rule": "Undated -> U9 max 1."},
        "U10": {"rule": "c3: the CTA must name the service (\"Request an EcoCare assessment for [asset]\")."},
    },
    "range": {
        "U1": {"name": "Range definition & scope", "rule": "c1 = definition with category noun + application; c2 = H1/title names the range AND the category noun (\"Discover X\" fails); c5 = a \"range at a glance\" block."},
        "U7": {"checks": ["Informational, expert voice (an advisor, not a brand talking about itself).", "Trade-offs, limitations or \"when not to use / when to choose another option\" are present.", "No hype, clickbait or stacked CTAs inside informational sections.", "Not judged on range pages: always na (member comparison is judged under RNG-1/RNG-2)."]},
        "U8": {"rule": "Includes brand casing and the master-range <-> range relationship."},
    },
    "software_product": {"U1": {"name": "Answer-first definition", "rule": "Target shape: \"[Product] is a [category] software that [function] for [audience], deployed [model]\"."}},
    "software_hub": {"U1": {"name": "Answer-first definition", "rule": "Target shape: \"[Product] is a [category] software that [function] for [audience], deployed [model]\"."},
                     "SW-1": {"rule": "Hubs: judge SW-1 over the product descriptors; a check passes when at least half of the product cards meet it (label-only cards still fail c5 if they are more than half)."}},
    "software_trial": {"U1": {"name": "Answer-first definition", "rule": "Target shape: \"[Product] is a [category] software that [function] for [audience], deployed [model]\"."}},
    "case_study": {
        "U3": {"rule": "c5 fails when the narrative, quote or results exist only in video, stat-card images, carousels, tab widgets or a PDF."},
        "U7": {"rule": "Slogan headings and promo inserts fail c3."},
        "U8": {"rule": "Compare stat cards vs prose vs meta (G1 only if they materially disagree - see G1)."},
        "U9": {"name": CS_U9[0], "checks": CS_U9[1], "src": "V2"},
        "U10": {"rule": "c3: descriptive CTA to the solution/range."},
    },
    "calculator": {
        "U1": {"rule": "c1 = the opening states what is calculated AND its drivers/core relationship; a bare \"Use this tool to estimate X\" passes only c3."},
        "U2": {"rule": "Outcome (c4) = the decision the result informs."},
        "U3": {"rule": "c5 fails when tool knowledge exists only inside the widget, iframe or a hidden panel. Hidden-panel text still counts for CALC-1..5 and is a text equivalent (no G6); G6 only when the knowledge is not in any text at all."},
        "U5": {"rule": "c3 is usually na; c2 includes method standards (PUE definitions, GHG Protocol)."},
        "U8": {"rule": "Tool naming; figures consistent with the tool (G1 on material contradictions in page text, e.g. two different \"typical PUE\" values; widget/runtime output errors are template_artifact, not G1)."},
        "U9": {"name": CALC_U9[0], "checks": CALC_U9[1], "src": "V2 (c3 from framework)"},
        "U10": {"rule": "c3: descriptive CTAs (\"Open the power sizing calculator\", \"Read White Paper 3\")."},
    },
    "whitepaper_gateway": {
        "U1": {"name": WP_U1[0], "checks": WP_U1[1], "src": "V2"},
        "U4": {"rule": "General acronyms (AI, IT, EV, HVAC, UPS) are exempt from c4."},
        "U3": {"rule": "c5 fails if the findings live only in the PDF."},
        "U8": {"rule": "Includes metadata consistency (a version mismatch fails c3 but is not G1)."},
        "U7": {"rule": "c4 is na unless the paper compares options."},
        "U10": {"name": WP_U10[0], "checks": WP_U10[1], "src": "V2"},
        "DOC-8": {"name": WP_DOC8[0], "checks": WP_DOC8[1], "src": "V2"},
        "DOC-7": {"name": WP_DOC7[0], "checks": WP_DOC7[1], "src": "V2"},
        "DOC-5": {"name": WP_DOC5[0], "checks": WP_DOC5[1], "src": "V2"},
    },
    "whitepaper_doc": {
        "DOC-1": {"name": WPDOC_DOC1[0], "checks": WPDOC_DOC1[1], "src": "V2"},
        "DOC-7": {"name": WP_DOC7[0], "checks": WP_DOC7[1], "src": "V2 (gateway DOC-7 reused; module text gives no DOC-7 checks)"},
        "DOC-8": {"name": WP_DOC8[0], "checks": WP_DOC8[1], "src": "V2 (gateway DOC-8 reused; V1 says keep U5 checks inside DOC-8)"},
        "DOC-5": {"name": WP_DOC5[0], "checks": WP_DOC5[1], "src": "V2 (gateway DOC-5 reused)"},
    },
    "esg_hub": {
        "U1": {"rule": "Company + report + period in the title; headline result first."},
        "U3": {"rule": "No placeholders (\"ZZ_\" components fail c4)."},
        "U8": {"name": "Canonical naming & metric consistency", "rule": "G1 on KPI contradictions (HTML vs report)."},
        "U7": {"rule": "No generic green claims; misses disclosed."},
        "U10": {"rule": "c3/c4: routing to the hub, investor relations, data annex or press release."},
        "DOC-7": {"name": ESG_DOC7[0], "checks": ESG_DOC7[1], "src": "V2 (ESG variant of DOC-7; checks DER)"},
    },
    "esg_report": {
        "U1": {"rule": "Company + report + period in the title; headline result first."},
        "U8": {"name": "Canonical naming & metric consistency", "rule": "G1 on KPI contradictions (HTML vs report)."},
        "U7": {"rule": "No generic green claims; misses disclosed."},
        "U10": {"rule": "c3/c4: routing to the hub, investor relations, data annex or press release."},
        "DOC-7": {"name": ESG_DOC7[0], "checks": ESG_DOC7[1], "src": "V2 (ESG variant of DOC-7; checks DER)"},
        "DOC-5": {"name": ESG_DOC5[0], "checks": ESG_DOC5[1], "src": "V2 lists DOC-5 with no checks; white-paper DOC-5 adapted (ESG example in c3)"},
    },
    "esg_report_doc": {
        "DOC-1": {"name": ESGDOC_DOC1[0], "checks": ESGDOC_DOC1[1], "src": "V2 phrase + DER (mirrors whitepaper_doc DOC-1)"},
        "DOC-4": {"name": ESGDOC_DOC4[0], "checks": ESGDOC_DOC4[1], "src": "V2 phrase + DER"},
        "ESG-5": {"name": ESGDOC_ESG5[0], "checks": ESGDOC_ESG5[1], "src": "V2 (document variant)"},
        "DOC-7": {"name": ESG_DOC7[0], "checks": ESG_DOC7[1], "src": "V2 (ESG variant of DOC-7; checks DER)"},
        "U8": {"name": "Canonical naming & metric consistency", "rule": "G1 on KPI contradictions (HTML vs report)."},
        "U7": {"rule": "No generic green claims; misses disclosed."},
    },
    "service_project": {
        "U1": {"name": "Answer-first service definition", "rule": "c1 needs the definition in the BODY (the meta description does not count)."},
        "U3": {"rule": "Tab bars with empty panels fail c5."},
        "U9": {"rule": "Undated -> U9 max 1."},
        "U10": {"rule": "c3: the CTA must name the service (\"Request an EcoCare assessment for [asset]\")."},
        "SVC-2": {"name": SVCP_SVC2[0], "checks": SVCP_SVC2[1], "src": "V2"},
    },
    "pdp": {
        "U1": {"name": "Answer-shaped product summary", "rule": "c1 passes only for a 40-80-word summary at the top in the 3-part answer shape (subject + primary function -> citable differentiator -> target application/audience) with at least 2 quantified specs."},
        "U8": {"rule": "Prose values = table values; model code paired with the plain name."},
    },
    "range_": {},
    "category": {
        "U1": {"name": "Definition + main types", "rule": "c1: a 50-100-word answer-first intro saying what the category is and its main types."},
        "U9": {"rule": "New standards/generations reflected (c2)."},
    },
    "caas": {},
    "document": {}, "datasheet": {},
    "comparison": {
        "U1": {"name": "Answer-first verdict", "rule": "Bottom line up front."},
        "U5": {"name": "Sources / test data"},
        "U6": {"rule": "c4 expected facts: cost, maintenance, compliance and installation differences."},
        "U9": {"rule": "Dated; reviewed quarterly."},
    },
    "faq": {
        "U4": {"name": "Specificity", "rule": "Values, intervals (\"3-5 years\"), test cadence."},
        "U9": {"rule": "Reviewed within 90-120 days; updated immediately after product or policy changes."},
    },
    "glossary": {"U5": {"name": "Sources"}},
}

# ---------------------------------------------------------------------------
# Per-type metadata
# ---------------------------------------------------------------------------
CADENCE = {"article": "blogs: at least yearly", "faq": "FAQ: every 90-120 days", "comparison": "competitive pages: quarterly",
           "document": "documents: twice a year", "datasheet": "documents: twice a year", "calculator": "tools: at least yearly"}
DEFAULT_CADENCE = "general content: every 6-12 months"

GATE_TYPES = {"G3": ["pdp", "datasheet"], "G7": ["article", "news"], "G8": ["case_study"], "G9": ["calculator"],
              "G10": ["range"], "G11": ["software_product", "software_trial"], "G12": ["service", "service_project"]}
UNIVERSAL_GATES = ["G1", "G2", "G4", "G5", "G6", "G13"]

GATE_PROMPT = {
    "G1": "Material factual contradiction in the content (prose vs table vs summary, block vs page, or HTML vs a provided spec/report){zero}; score max 59. Material = two statements on the page give conflicting values for a figure, spec/rating, date, scope or claim a buyer would rely on (e.g. \"over 155 sites\" vs \"more than 250 sites\" for the same count; \"16-6300 A\" for a range whose listed members stop at 600 A). Not material: wording or naming variation, rounding (15 A vs 16 A of the same value), a mislabelled card whose facts are right, or a metadata/version mismatch (judge that under U8 c3 / DOC-7). Widget or runtime output errors (\"#VALUE!\", a tool message such as \"reduce 80% to 100%\") are the template_artifact penalty, never G1.",
    "G2": "The primary question is never answered or the subject never defined -> max 39. A download/gateway page that names the document and its subject but gives no findings or KPIs is G6, not G2; trigger G2 there only if the page never says what the document is about.",
    "G3": "No quantified specs in the page text -> max 40.",
    "G4": "Misleading or unsafe technical/safety statement -> max 39; flag for an expert.",
    "G5": "Title/H1 promise not delivered (clickbait / intent mismatch) -> max 49. G5 concerns the visible H1 (and deck); an unfulfilled promise only in the HTML <title> or meta description is judged under the title checks (ART-2 c5, U1 c2), not G5.",
    "G6": "Core content only in an image, video, PDF, widget or gated asset with no text equivalent on the page (text in a collapsed tab, accordion or hidden tool panel IS a text equivalent: penalise tab-only facts once, under U3 c5){g6}{g6u3}; max 59.",
    "G7": "No visible publication date -> max 59.",
    "G8": "No quantified customer outcome in body text (targets, vanity and meta-only numbers do not count) -> max 59.",
    "G9": "Method, assumptions and example results all absent from the page text (CALC-1, CALC-2 and CALC-3 all level 0) -> U3 max 2; max 39.",
    "G10": "No rating, capacity or size with a unit for the range or any member -> max 49.",
    "G11": "None of: deployment model, integrations/protocols, security facts, licensing/pricing/trial terms -> max 49. A bare \"free\" (\"free trial\", \"free download\") counts as a trial term for G11 (cost), so G11 does not fire; SW-5 c3 still needs at least 2 terms.",
    "G12": "No concrete deliverable and no service-level fact (SVC-1 c1 and c2 fail AND no SVC-2 check passes) -> max 40. A link label alone (\"Extended warranty\") is not a commitment and does not pass SVC-2.",
    "G13": "Thin page (fewer than 3 substantive factual statements) -> U7 and U8 max 2.",  # text built in common.gate_text
}
G6_EXTRA = {"whitepaper_gateway": " (incl. WP-2 at level 1 or below, or a bare PDF URL)",
            "esg_hub": " (incl. a gateway with no KPIs or a bare PDF URL; a KPI-less download stub is G6, not G2)", "esg_report": " (incl. a gateway with no KPIs or a bare PDF URL; a KPI-less download stub is G6, not G2)",
            "esg_report_doc": " (incl. KPIs given only as infographics or images with no text values)",
            "news": " (incl. announcement facts only in the attached PDF)", "case_study": " (incl. a story told only in video/image/PDF)",
            "calculator": " (incl. tool knowledge only inside the widget with no text anywhere; hidden tool-panel text is a text equivalent)"}

# v2.2 fix 7: G13 decision rule (used by common.gate_text)
G13_RULE = ("A substantive factual statement is specific and checkable: a number with a unit or date, a named standard, a named customer/product with what it does, or a named finding. "
            "General assertions (\"impossible without data centers\", \"tremendous potential\"), slogans, navigation and metadata (title, date, file size, document number) do not count. "
            "Count across all visible and hidden page text once; on abstract-only gateways count the abstract plus any findings: fewer than 3 -> trigger G13.")

# family grouping for the document, in the requested order
GROUPS = [
    ("Inventory type 1 - Blog article", ["article"]),
    ("Inventory type 2 - Solution / industry page", ["solution"]),
    ("Inventory type 3 - Product range / master range", ["range"]),
    ("Inventory type 4 - Customer success story", ["case_study"]),
    ("Inventory type 5 - White paper / technical document", ["whitepaper_gateway", "whitepaper_doc"]),
    ("Inventory type 6 - Calculator / TradeOff Tool", ["calculator"]),
    ("Inventory type 7 - Service page", ["service", "service_project"]),
    ("Inventory type 8 - Software page", ["software_product", "software_hub", "software_trial"]),
    ("Inventory type 9 - News / press release", ["news"]),
    ("Inventory type 10 - Sustainability / ESG", ["esg_hub", "esg_report", "esg_report_doc"]),
    ("Other type - Product detail page", ["pdp"]),
    ("Other type - Product category", ["category"]),
    ("Other type - CaaS / reusable block", ["caas"]),
    ("Other type - Editorial (common logic)", ["editorial"]),
    ("Other type - Document and datasheet", ["document", "datasheet"]),
    ("Other type - Comparison / selection guide", ["comparison"]),
    ("Other type - FAQ / support", ["faq"]),
    ("Other type - Glossary / definition", ["glossary"]),
    ("Other type - Video asset", ["video"]),
]

META = {
    "article": dict(label="Blog / article", noun="blog article", src="page-types-v2.md §1",
        when="A dated narrative, opinion or explainer (blog post, thought leadership, editorial article).",
        extracts="The thesis/answer in the first 30% of the page; definitions and how-it-works passages; quantified context with source; frameworks and checklists; named expert perspective; trade-offs. Cited for \"why does X matter / how does X work / what's changing in Y\".",
        natural="Awareness, Education (Consideration for selection-style posts). Flag Decision unless it is a how-to.",
        default="Education",
        stage_rule="Awareness (trend, opinion, \"why it matters\"), Education (explains how something works or how to approach it), Consideration (compares approaches or solution types), Evaluation (compares specific products or vendors, specs, proof), Decision (pricing, buying, implementation, contact).",
        failures="[A] narrative/biographical openings, slogan/pun H1s, unsourced numbers, no takeaways, no standards by number, promotional ambition lines, a CTA naming no asset. [T] \"Top picks\" and \"Add a comment\" H2s inside the article; \"Guest Blogger\" byline.",
        read="the full article text (headings, lists, tables, image alt text, link labels, author, visible date)"),
    "news": dict(label="News / press release", noun="press release", src="page-types-v2.md §2",
        when="A dated corporate announcement with dateline, spokesperson quotes and a media contact.",
        extracts="Who announced what, when and where; the named offer and its category; headline numbers with their basis; availability and roadmap; partner/customer names; attributed quotes; the company descriptor (About block); findings for research releases.",
        natural="Consideration, Evaluation, Education, Awareness (set by the stage test). Flag Decision.",
        default="Consideration",
        stage_rule="Set the stage from the release subtype: launch, reference design or partnership with an offer -> Consideration (Evaluation if spec-led); research or study -> Education; corporate, event, award or financial -> Awareness. State the subtype.",
        failures="[T] numeric date; subheads not marked as headings; About block missing (5 of 6 releases). [A] relative timing, unscoped superlatives, quotes without facts, \"visit the web\", inconsistent offer naming, main finding missing from the headline.",
        read="the full release text (headline, deck, dateline, body, quotes, About block, media contact, attachments named)",
        extra="Exclude from every check (template, not release content): spokesperson bio blocks (\"Related Spokespeople\"), attached-files lists, share bars and the authentication (Wiztrust) block. The About block counts only for NEWS-6; it is excluded from the U4 c2 density count."),
    "solution": dict(label="Solution / industry page", noun="solution page", src="page-types-v2.md §3",
        when="An industry/segment problem plus an architecture of offers (e.g. data center power, microgrids, F&B).",
        extracts="What the solution is and which offers compose it; the problem (with data); how it works (architecture/integration); segments, applications and scale; outcomes with numbers; references; how to start.",
        natural="Awareness -> Consideration (Evaluation for product-solution pages).", default="Consideration",
        stage_rule="Awareness (problem/trend framing only), Consideration (solution approach and offers for a segment - the usual case), Evaluation (product-solution page with specs and proof).",
        failures="[T] slogan H1 with no answer slot; cloned/truncated teaser cards; empty tab panels; stat-tile footnotes that never render; \"Need help?\" product-sales block; no date field. [A] zero sourced numbers; \"up to X%\" without basis; references without results; GRI G4 cited as current.",
        read="the full rendered page text, including tab panels and carousel slides (mark text that is only in a collapsed tab/carousel as hidden)",
        extra="SOL-3 is merged into SOL-2 and SOL-6 (FAQ) into U6."),
    "service": dict(label="Service page (recurring)", noun="service page", src="page-types-v2.md §4",
        when="A recurring service offer: maintenance, monitoring, managed service, support contract. Mixed offers: classify by the offer named in the H1; if the H1 names both, by the first deliverable listed in the H1/intro (\"design, implementation ... with maintenance\" -> service_project). Cross-sells (\"Combine with EcoCare membership\") are ignored.",
        extracts="What the service is and what is included/excluded; eligible equipment; service levels (response time, coverage hours, remote vs on-site, visits/year); how it works; plans and contract/pricing model; availability; results with basis; delivery credentials and proof.",
        natural="Consideration -> Evaluation -> Decision (Post-purchase for renewals).", default="Evaluation",
        stage_rule="Consideration (exploring service approaches), Evaluation (plans, service levels, eligibility, proof - the usual case), Decision (ordering, contract, contact).",
        failures="[A] no service levels on any page; definition only in the meta; eligible assets as categories only; no pricing model/availability; IEC 62443 missing on OT-cyber services; unresolved \"up to\" footnotes. [T] empty tab panels; stat tiles.",
        read="the full rendered page text, including tab panels",
        extra="Hub rule: a page listing articles or child services without describing a service is scored with this logic and flagged \"better fit: hub/category\"."),
    "service_project": dict(label="Service page (project: modernization, retrofit, consulting)", noun="service page", src="page-types-v2.md §4",
        when="A one-off service project: modernization, retrofit, consulting, assessment. Mixed offers: classify by the offer named in the H1; if the H1 names both, by the first deliverable listed in the H1/intro. Cross-sells are ignored.",
        extracts="As for recurring services, with project lead time, duration/downtime window and warranty on the work instead of recurring service levels.",
        natural="Consideration -> Evaluation -> Decision.", default="Consideration",
        stage_rule="Consideration (exploring the project approach - the usual case), Evaluation (scope, timeline, proof), Decision (ordering, contact).",
        failures="As for service: no numeric commitments, scope only in tabs/brochures, no references with results.",
        read="the full rendered page text, including tab panels",
        extra="Hub rule: a page listing articles or child services without describing a service is scored with this logic and flagged \"better fit: hub/category\"."),
    "range": dict(label="Product range / master range", noun="range page", src="page-types-v2.md §5",
        when="Lists several variants (members) of one named product family; master ranges list sub-ranges.",
        extracts="What the family is and who it is for; members and how they differ; selection axes with thresholds; ecosystem/protocols; standards; legacy names and successors.",
        natural="Consideration (master ranges), Evaluation (single ranges with specs). Flag Awareness.", default="Consideration",
        stage_rule="Consideration for master ranges and family overviews; Evaluation for a single range with specs.",
        failures="[T] \"Discover X\" H1; card text rendered 2-3x; off-topic drive/app promos; KPI labels with no numbers; no date. [A] no comparison table or choice statements; standards and legacy names missing; selection delegated to the Product Selector.",
        read="the full rendered page text, including member cards and tabs"),
    "software_product": dict(label="Software product page", noun="software page", src="page-types-v2.md §6",
        when="One software product's (or one platform's) capabilities are the main content, even when its modules have their own tiles.",
        extracts="Category definition; capabilities mapped to modules; integrations/protocols; deployment model and requirements; security/compliance; licensing/pricing logic; proof; versions and former names.",
        natural="Evaluation (Consideration acceptable).", default="Evaluation",
        stage_rule="Evaluation by default (Consideration if the page only frames the category).",
        failures="[A] no protocols, deployment model, certifications or licensing; \"agnostic/multi-vendor\" with no specifics. [T] benefit-label tiles; KPI counters with no values in the HTML; logo walls as images; \"ZZ_\" placeholder.",
        read="the full rendered page text"),
    "software_hub": dict(label="Software hub / portfolio", noun="software hub page", src="page-types-v2.md §6",
        when="At least 3 distinct, separately named software products, each with its own card (portfolio or use-case hub). Capability tiles or modules of one platform are not products: a page about one platform with module tiles is software_product.",
        extracts="The product map and which product fits which need; one-line capabilities per product; proof; versions and former names.",
        natural="Consideration.", default="Consideration", stage_rule="Consideration by default.",
        failures="[T] benefit-label tiles; KPI counters with no values; duplicated sections. [A] no product map/selection guidance; no proof with numbers.",
        read="the full rendered page text, including every product card"),
    "software_trial": dict(label="Software trial / download / licence page", noun="software trial page", src="page-types-v2.md §6",
        when="A sign-up, download or licence action is the main content.",
        extracts="Licence model, price drivers, trial terms (duration, scope, cost, data, expiry), how to activate, deployment and requirements.",
        natural="Decision.", default="Decision", stage_rule="Decision by default.",
        failures="[A] trial page with no terms; no licence model. [T] form-only pages.",
        read="the full rendered page text, including the form labels"),
    "case_study": dict(label="Customer success story", noun="customer story", src="page-types-v2.md §7",
        when="A named (or anonymized) customer plus results.",
        extracts="A one-sentence outcome (customer + result with unit + period + named offer); customer profile; what was deployed and how; a quotable customer statement; how the number was measured; a date.",
        natural="Evaluation (default); Consideration for approach showcases and brand partnerships; Decision for purchase references. Flag Awareness.", default="Evaluation",
        stage_rule="Evaluation by default; Consideration for approach showcases and brand partnerships; Decision for purchase references.",
        failures="[T] story, summary and quotes rendered client-side (4 of 6); empty tab panels; \"ZZ_\" placeholders. [A] slogan H1; vanity stat cards; best metric only in the meta description; no date; no method; product grid without roles.",
        read="the full rendered story text, including stat cards, quotes and tabs"),
    "calculator": dict(label="Calculator / TradeOff Tool", noun="calculator page", src="page-types-v2.md §8",
        when="The primary element is an interactive widget computing outputs from inputs (score the page text, including the tool panels).",
        extracts="Engines cannot run the tool, so they cite the knowledge around it: what is calculated and from which drivers; the formula/logic; assumptions with values and sources; typical results/benchmarks; a worked example; input/metric definitions; limits; model version/date.",
        natural="Consideration, Evaluation; Education for \"how to calculate\" tools. Flag Awareness.", default="Evaluation",
        stage_rule="Evaluation (sizing/ROI/TCO for a decision) or Consideration (comparing approaches); Education for \"how to calculate\" tools.",
        failures="[T] the tool runs in an iframe whose raw HTML has about 5 words; method, assumptions, defaults and model version live only in tool panels. [A] an intro that only invites use; related-content card grids instead of explanation; near-duplicate single-/three-phase pages; contradictory typical values.",
        read="the full rendered page text, including the tool's panels, input labels, default values and any text in the tool iframe"),
    "whitepaper_gateway": dict(label="White paper gateway (HTML page)", noun="white paper page", src="page-types-v2.md §9",
        when="The HTML landing/download page of a white paper or technical guide. This is the headline score.",
        extracts="The title (matched to \"how to / what are\" prompts); the abstract's opening as the answer; key findings with numbers; coverage; publisher/author/date; the PDF as a second citable source.",
        natural="Education (default), Consideration. Flag Decision.", default="Education",
        stage_rule="Education by default; Consideration if the paper compares approaches or options.",
        failures="[T] no H1 (title rendered 3x as lower headings); abstract duplicated; no key-findings, author or related-links slot; code file names. [A] background-first abstracts; \"guidance is provided\" with no guidance; page version != file version; 4 of 6 papers older than 2 years with no review note.",
        read="the gateway page text (title, abstract, findings, metadata block, download label and file name)",
        extra="Two-layer rule: the gateway score is the headline. If the PDF text is supplied, score it separately with the whitepaper_doc prompt; report both side by side, never averaged. DOC-9 applies only if the asset is gated (otherwise all checks na)."),
    "whitepaper_doc": dict(label="White paper document (PDF text)", noun="white paper PDF", src="page-types-v2.md §9 (document module)",
        when="The text of the white paper PDF itself, when supplied (scored beside the gateway, never averaged).",
        extracts="The executive summary and findings, methodology, specs/tables, version and authorship from the file.",
        natural="Education (default), Consideration.", default="Education",
        stage_rule="Education by default; Consideration if the paper compares approaches or options.",
        failures="Not piloted (no white-paper PDF text supplied in the pilot).",
        read="the PDF text (if the URL is a PDF open it; otherwise ask for the PDF or its pasted text)",
        extra="Two-layer rule: this is the Document score; the gateway (whitepaper_gateway) remains the headline score."),
    "esg_hub": dict(label="Sustainability / ESG hub (report library)", noun="ESG hub page", src="page-types-v2.md §10",
        when="A sustainability report library or ESG landing hub.",
        extracts="Emissions by scope with period and basis; % vs baseline; targets with baseline/target year; progress; frameworks; assurance level and provider; ratings; edition/date; where the data and index live.",
        natural="Evaluation (R10: ESG pages use Evaluation until a dedicated stage is approved).", default="Evaluation",
        stage_rule="Always Evaluation (R10), unless the user declares another stage.",
        failures="[T] KPI-free download pages; placeholder text on the hub. [A] three names for one report; missing period; versions without a change note.",
        read="the full hub text (report entries, KPIs, links and labels)"),
    "esg_report": dict(label="Sustainability / ESG report gateway", noun="ESG report page", src="page-types-v2.md §10",
        when="The HTML page of one sustainability/ESG report (headline score). A bare PDF URL is scored with this logic (every HTML check fails \"NOT FOUND - bare PDF\") together with esg_report_doc.",
        extracts="As for the ESG hub, for one report edition.",
        natural="Evaluation (R10).", default="Evaluation", stage_rule="Always Evaluation (R10), unless the user declares another stage.",
        failures="[T] KPI-free download pages. [A] missing period; versions without a change note; 2022 values restated in 2023 with no notice in the 2022 file.",
        read="the report gateway text (title, KPIs, targets, methodology, assurance, download labels)",
        extra="Two-layer rule: the gateway score is the headline; the PDF is scored with esg_report_doc and reported beside it, never averaged. Penalties: superseded_no_notice for archived editions; template_artifact for \"ZZ_\" components."),
    "esg_report_doc": dict(label="Sustainability / ESG report document (PDF text)", noun="ESG report PDF", src="page-types-v2.md §10",
        when="The text of the sustainability/ESG report PDF, when supplied.",
        extracts="Scope 1/2/3 emissions with basis, targets and progress, frameworks, assurance, indexes and companions from the file.",
        natural="Evaluation (R10).", default="Evaluation", stage_rule="Always Evaluation (R10), unless the user declares another stage.",
        failures="Untagged PDFs with no bookmarks; units garbled in extraction (\"TCO e 2\"); no release date or successor link; highlights without scopes.",
        read="the PDF text (for documents over 20k words read: the first 6 pages, highlights, TOC, GHG/KPI section, targets table, methodology/assurance section and indicator annex; say which sections were read)",
        extra="Two-layer rule: this is the Document score, reported beside the esg_report gateway score, never averaged."),
    "pdp": dict(label="Product detail page (PDP)", noun="product page", src="page-types.md §1",
        when="Has a SKU/reference + a spec table.",
        extracts="Product identity (name, ref/SKU, brand); key specs with units; primary application; compatibility and accessories; standards and certifications; availability/where to buy; lifecycle; answers to specific questions. AI shopping surfaces consume the PDP as data.",
        natural="Evaluation, Decision. Flag Awareness, Education.", default="Evaluation",
        stage_rule="Evaluation (specs, compatibility, proof) or Decision (where to buy, lifecycle, ordering).",
        failures="Marketing-only description; specs only in PDF or image; specs hidden in collapsed tabs; boilerplate shared across hundreds of SKUs; no use cases; no compatibility info; discontinued status not stated; prose and table disagree.",
        read="the full rendered page text including the spec table, tabs, documents list and Q&A",
        expected="what it is, rating(s), key dimensions/weight, operating conditions, standards, application, compatibility, availability/lifecycle, documents"),
    "category": dict(label="Product category page", noun="category page", src="page-types.md §3",
        when="Lists several families/types under a generic noun (e.g. circuit breakers, EV chargers, PLCs).",
        extracts="Category definition, types/sub-types, selection criteria, short lists. The page should carry a compact guide layer, not just a product grid.",
        natural="Consideration (Evaluation). Flag Awareness.", default="Consideration", stage_rule="Consideration by default (Evaluation if spec-led).",
        failures="Product grid only; SEO text block at the bottom; \"We offer a wide range of high-quality ...\"; no selection criteria.",
        read="the full rendered page text, including the guide layer and product grid labels"),
    "caas": dict(label="CaaS / reusable content block", noun="content block", src="page-types.md §4",
        when="A module under about 150 words reused across pages (object descriptions, banners, benefit blocks, spec snippets, FAQ modules, CTA blocks).",
        extracts="AI never sees a block; it sees the passage inside its host page. A block must stand alone and must not create duplication or contradiction across pages.",
        natural="Any (inherits the host page).", default="Consideration", stage_rule="Use the host page's stage; if unknown, use Consideration and label it inferred.",
        failures="Unnamed subjects (\"this solution\"); campaign-name titles; boilerplate across many pages; \"Learn more\" CTAs; IEC/UL mismatches for the country.",
        read="the block text (title, subtitle, description, CTA) and, if available, its host page",
        extra="With fewer than 40 words, quotation and source checks are na. Also run a host-page assembly check: redundancy across blocks, conflicting claims, answer block placed first. G1 zeroes BLK-4 for this type."),
    "editorial": dict(label="Editorial page (common logic)", noun="editorial page", src="page-types.md §5",
        when="An editorial page that fits no more specific type (articles, solutions and case studies have their own logic).",
        extracts="Answer-first passages, facts, sources and structure, judged with the universal criteria only.",
        natural="Not defined in the source (inferred from content).", default="Education",
        stage_rule="Infer from content: Awareness (problem/why), Education (how it works), Consideration (approaches/options), Evaluation (specific offers, proof), Decision (buying/contact).",
        failures="Not specified in the source.",
        read="the full page text",
        extra="Template-goal note: for a GEO Optimized Template whose primary goal is conversion, still score the GEO elements; never recommend removing conversion elements."),
    "document": dict(label="Document (catalog, guide, manual, generic PDF)", noun="document", src="page-types.md §7",
        when="A downloadable file or its gateway that is not a white paper, ESG report or datasheet (catalog, guide, manual).",
        extracts="Specs, ratings, tolerances, procedures, compliance details, methodology, conclusions. Principle: HTML-first, PDF-also.",
        natural="Datasheet/manual: Evaluation, Decision, Post-purchase (flag Awareness); whitepaper-like documents: Education, Consideration.", default="Evaluation",
        stage_rule="Evaluation or Decision for manuals, catalogs and technical guides; Education for explanatory guides.",
        failures="Scanned PDFs; no HTML gateway; generic file names; no revision/date; key knowledge behind a form.",
        read="the gateway page and/or the document text; if only the PDF is available score it and flag that the HTML gateway is unknown",
        extra="Sub-types: catalog (DOC-1 needs per-range HTML equivalents); manual/installation guide (DOC-2 counts numbered steps; safety warnings required)."),
    "datasheet": dict(label="Datasheet", noun="datasheet", src="page-types.md §7 (datasheet sub-type)",
        when="A product datasheet (PDF or HTML). Same as document with 4 points moved from DOC-8 to DOC-3.",
        extracts="Specs, ratings with test conditions, dimensions, standards, ordering references.",
        natural="Evaluation, Decision, Post-purchase. Flag Awareness.", default="Evaluation",
        stage_rule="Evaluation by default; Decision when the datasheet is used for ordering/specifying.",
        failures="Specs only as images; inconsistent units/labels; no revision/date; values that disagree with the PDP.",
        read="the datasheet text (and the PDP if provided, for the consistency check)"),
    "comparison": dict(label="Comparison / selection or buying guide", noun="comparison page", src="page-types.md §9",
        when="Two or more options side by side, or a \"how to choose\" guide.",
        extracts="Neutral comparison tables, explicit criteria, \"choose X if\" verdicts and trade-offs. Technology comparisons are more citable than \"us vs competitor\" pages.",
        natural="Consideration, Evaluation. Flag Awareness.", default="Consideration", stage_rule="Consideration (technology/approach comparisons) or Evaluation (specific products or vendors).",
        failures="Self-ranking with own brand #1 and no transparent criteria; no sources for competitor data; no SE limitations.",
        read="the full page text, including comparison tables",
        extra="Guides add: numbered steps; a worked example with numbers; sizing formula in text; safety notes and standards."),
    "faq": dict(label="FAQ / support / knowledge-base article", noun="FAQ page", src="page-types.md §10",
        when="Q&A pairs are the main content (FAQ, support or knowledge-base article).",
        extracts="Direct answers to real buyer questions, identifiers (models, error codes), steps and values.",
        natural="Education, Decision, Post-purchase.", default="Education",
        stage_rule="Education (how/what questions), Decision (ordering, compatibility, availability), or Post-purchase support scored as Decision.",
        failures="Global mega-FAQs; answers that end in a CTA; \"it depends\" answers; no identifiers.",
        read="the full Q&A text"),
    "glossary": dict(label="Glossary / definition page", noun="glossary page", src="page-types.md §11",
        when="The page defines one term.",
        extracts="A one-sentence definition, formula/units/standard, an example and the disambiguation from related terms.",
        natural="Awareness, Education. Flag Decision.", default="Education", stage_rule="Education by default; Awareness for problem/trend terms.",
        failures="Not specified in the source.",
        read="the full page text"),
    "video": dict(label="Video asset (YouTube + embed)", noun="video", src="page-types.md §13 (SE Toolkit Ch. 5 / Ch. 10)",
        when="A video asset scored with its title, description, transcript/captions, chapters and embedding page.",
        extracts="The title, description, transcript and the text context on the embedding page.",
        natural="Not defined in the source (inferred from the video type).", default="Education",
        stage_rule="Infer from the video type: Education (tutorial/how-to/explainer), Consideration (comparison), Evaluation (case study, product demo), Awareness (brand/trend).",
        failures="Brand films; no transcript; no chapters; videos embedded without text context.",
        read="the video page (title, description, chapters) and the transcript if available; ask for the transcript only if it cannot be read"),
}

# ---------------------------------------------------------------------------
# v2.2 fix 17: software has no U5 (decision, kept from v2.1 weights)
# ---------------------------------------------------------------------------
SOFTWARE_U5_NOTE = ("No U5 criterion for software types (deliberate, v2.2 decision): the U5 evidence checks are already scored inside the "
                    "software criteria - attributed statistics and third-party validation with year (SW-6 c3/c4), customer outcomes with baseline "
                    "(SW-6 c1/c2), standards and certifications by number (SW-2 c1, SW-4 c2) - and authorship/quotes add little on product pages. "
                    "Adding U5 would double-count these and require re-weighting the pilot-calibrated tables.")
for _k in ("software_product", "software_hub", "software_trial"):
    META[_k]["extra"] = (META[_k].get("extra", "") + " " + SOFTWARE_U5_NOTE).strip()

# ---------------------------------------------------------------------------
# v2.2 fix 2: concrete stage test per type. Applied in order; first match wins.
# A stage supplied by the user always overrides the test.
# ---------------------------------------------------------------------------
STAGE_TEST = {
    "article": "1) The post compares named products/vendors or gives specs/proof for a named offer -> Evaluation. 2) It compares approaches or solution types (\"AC vs DC coupling\", \"3 ways to ...\") -> Consideration. 3) It explains how something works or how to do/approach it (steps, framework, \"how to\", checklist) -> Education (e.g. \"three questions to ask this week ... start with a facility assessment\" = Education). 4) It frames a trend, risk or opinion (\"why X matters\", \"what's changing\") with no method -> Awareness. Pricing/buying/implementation-only posts -> Decision (flag it).",
    "news": "Decide the subtype from the headline + first paragraph. 1) Launch, reference design or partnership with an offer AND the release gives at least 3 specs/capabilities with units or named elements (NEWS-5 c3 would pass with 3+ items) -> Evaluation (e.g. a reference design with power, density and cooling figures). 2) Launch, reference design or partnership with an offer, fewer than 3 such specs -> Consideration. 3) Research, survey or study findings -> Education. 4) Corporate, event, award, financial or people news -> Awareness. State the subtype.",
    "solution": "1) Evaluation only if the page has a spec table, or at least 2 named SKUs/ranges each with a quantified parameter, AND a reference or proof item (e.g. a rack-system page listing kW per rack and named PDUs with ratings plus a customer result). A product-family page under /solutions/ without specs is NOT Evaluation. 2) The page only frames the problem/trend and names no offer -> Awareness. 3) Otherwise (solution approach and offers for a segment) -> Consideration.",
    "service": "1) The page is mainly an order/contract/contact form, a renewal page or a price list -> Decision. 2) The page names plans/tiers, service levels or eligible equipment (any SVC-2, SVC-3 or SVC-5 check would pass) -> Evaluation. 3) Otherwise (exploring service approaches, no plans or levels) -> Consideration.",
    "service_project": "1) The page is mainly an order/quote request or contact form -> Decision. 2) The page states a project scope with a timeline/duration or numeric commitment AND a reference with a result (SVC-2 c1/c2 and SVC-7 c2 would pass) -> Evaluation. 3) Otherwise (exploring the project approach) -> Consideration. A page with no ordering or contract content is never Decision.",
    "range": "1) Master range (lists sub-ranges or ranges) or family overview -> Consideration. 2) A single range whose members carry ratings with units in a table or member cards -> Evaluation. 3) A single range page with no member ratings -> Consideration.",
    "software_product": "1) The page states at least one of deployment model, integrations/protocols, security facts or licensing (G11 would not fire) -> Evaluation. 2) The page only frames the software category or problem -> Consideration.",
    "software_hub": "Consideration (fixed). Use Evaluation only if the user declares it.",
    "software_trial": "Decision (fixed). Use another stage only if the user declares it.",
    "case_study": "1) The story is framed around a purchase or contract reference (order, deployment contract, \"selected X\") with product references -> Decision. 2) The story names no quantified result for a named offer AND reads as an approach or brand-partnership showcase (sponsorship, co-innovation, sustainability journey with targets only) -> Consideration. 3) Otherwise (named customer + deployed offer + results) -> Evaluation. Example: YVR net-zero story with 530 t CO2e/year for EcoStruxure = Evaluation.",
    "calculator": "1) The H1/title or opening says it compares options or approaches (\"comparison\", \"vs\", \"trade-off\", \"which ...\") -> Consideration, even if it outputs TCO/cost. 2) It sizes, prices or computes ROI/TCO/savings for one chosen option -> Evaluation. 3) It explains how a metric is calculated (\"how to calculate PUE\") -> Education.",
    "whitepaper_gateway": "1) The title or abstract compares approaches, architectures or options (\"X vs Y\", \"comparing\", \"choosing between\") -> Consideration. 2) Otherwise -> Education.",
    "whitepaper_doc": "Use the stage of the gateway (same test): compares approaches/options -> Consideration; otherwise Education.",
    "esg_hub": "Always Evaluation (R10), unless the user declares another stage.",
    "esg_report": "Always Evaluation (R10), unless the user declares another stage.",
    "esg_report_doc": "Always Evaluation (R10), unless the user declares another stage.",
    "pdp": "1) The page's main content is where to buy, availability, lifecycle/substitutes or ordering references -> Decision. 2) Otherwise (specs, compatibility, proof) -> Evaluation.",
    "category": "1) The page lists types/families with ratings or a spec-led comparison table (CAT-2 c2 would pass) -> Evaluation. 2) Otherwise -> Consideration.",
    "caas": "Use the host page's stage. If the host is unknown -> Consideration (inferred).",
    "editorial": "1) Specific named offers with specs or proof -> Evaluation. 2) Compares approaches/options -> Consideration. 3) Explains how something works -> Education. 4) Problem/trend framing only -> Awareness. 5) Buying/contact only -> Decision.",
    "document": "1) Explanatory guide (how something works, principles) -> Education. 2) Ordering catalog, price list or spare-parts list -> Decision. 3) Otherwise (manuals, technical guides, catalogs with specs) -> Evaluation.",
    "datasheet": "1) The user says it is used for ordering/specifying, or it is mainly ordering references -> Decision. 2) Otherwise -> Evaluation.",
    "comparison": "1) Compares specific named products, ranges or vendors -> Evaluation. 2) Compares technologies or approaches (\"Type A vs Type B RCD\") -> Consideration.",
    "faq": "1) Most questions are about ordering, compatibility, availability or post-purchase support (installation, error codes) -> Decision. 2) Otherwise (how/what questions) -> Education.",
    "glossary": "1) The term names a problem, risk or trend (\"power quality issues\") -> Awareness. 2) Otherwise -> Education.",
    "video": "1) Case study or product demo -> Evaluation. 2) Comparison -> Consideration. 3) Tutorial, how-to or explainer -> Education. 4) Brand or trend film -> Awareness.",
}
assert set(STAGE_TEST) == set(META), set(STAGE_TEST) ^ set(META)
for _k, _t in STAGE_TEST.items():
    META[_k]["stage_rule"] = _t

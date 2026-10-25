# Product Range & Software Pages — GEO Scoring Logic, Corpus Audit and Pilot (draft v1.1, 2026-10-19)

> **Status (20 Oct 2026):** design record. Pilot scores in this file were computed before the v2.0/v2.1 standard (some on server HTML, with older gate IDs). For current scores use `research/final-scoring/` and `final-scoring/SE_GEO_scored_inventory_v2.1.csv`; for current logic use `skill/geo-research/references/page-types-v2.md`.

*Scope: Content GEO Score Agent, page types **Product range page** (se.com master ranges, corpus #13–18) and **Software page** (corpus #43–48). Method follows `skill/geo-research` (scoring-framework, page-types, judge-protocol, buyer-journey, weights.json). The skill folder was not edited. Draft weights: `scratchpad/agents/range_software/weights_range_software.json` (merged copy of `assets/weights.json`). Judge files: `research/type-analysis/pilot/NN_judge.json`.*

*This score measures **citation-readiness of the content only**. Whether AI actually cites a page also depends on retrieval, off-site consensus and technical access.*

---

## 1. Executive summary

- **All 11 unique pages score Poor.**
  - Range pages: **12–36**, median 28.
  - Software pages: **22–30**, median 26.
  - The scores are low because SE master-range and software pages are mostly **navigation hubs built from cards**. Their text names products but rarely says how members differ, which one to choose, or what the software integrates with, how it is deployed, what security certifications it has, or how it is licensed. A buyer's AI assistant needs exactly those facts.
- **Biggest SE-wide gaps (systemic, not page-specific):**
  1. **No comparison table or explicit selection guidance.** 0 of 6 range pages have one. RNG-1 and RNG-2 together carry about 29% of the effective weight at Consideration.
  2. **No visible dates or lifecycle status.** 0 of 11 pages.
  3. **No standards.** Only 1 of 6 range pages cites one (UL 489).
  4. **Software decision facts are missing**: integrations/protocols, deployment model, certifications and licensing. These are the questions AI agents check first; when they are missing, agents fall back to third parties.
  5. **Template defects visible to crawlers:**
     - card text rendered 2–3×;
     - generic "Discover X" H1s and "Explore our offer" / "See product details" H2s;
     - unrelated cross-promotions ("EcoStruxure Asset Advisor for drives" on UPS and breaker pages);
     - KPI labels whose numbers are missing from the HTML;
     - a live "ZZ_Paragraph Title" placeholder;
     - a whole section duplicated on the DCIM page.
- **Where SE is strong:**
  - **Galaxy:** kW band and application per member, efficiency stated with its operating mode, and an honest limitation.
  - **PacT:** ratings and voltages for every sub-range, UL 489, a former name ("formerly Vigirex"), and trip-unit compatibility.
  - **Software hub:** former names (SoMachine, Unity Pro, Ecodial, Rapsody) and hardware compatibility.
  - **DCIM page:** opens with a definition of DCIM, names security controls, and quantifies one named customer.
- **Proposed logic:**
  - **Range v1.1** revises §2:
    - adds **RNG-8 Lifecycle, legacy names & migration** and **RNG-9 Member descriptors**;
    - re-scopes **RNG-5** to ecosystem, compatibility and protocols, and moves it to the *specs* family;
    - reduces RNG-1, RNG-3, RNG-4, RNG-7, U2, U3 and U5;
    - interprets master ranges with sub-ranges as the rows.
  - **Software (new)** has 8 SW criteria and 3 sub-variants: **software_product** (single product or platform), **software_hub** (portfolio or use-case hub) and **software_trial** (trial, download or conversion page).
  - New **gates G7/G8** (cap 49) and a **template_artifact** penalty (−2).
- **Calibration.** The range logic discriminates (spread 24 points), and the order matches expert intuition except for Line (36) vs Galaxy (32), which are within judge noise. Software spread is narrow (22–30) because the gaps are systemic, not because the logic is blind. A headroom simulation shows Galaxy and DCIM reaching **70–71 (Good)** once the top recommended fixes are applied. One recalibration was made (§5.3).
- **#44 is a duplicate of #43.** `/work/solutions/software/by-industry/` 301-redirects to `/work/software/`, and the corpus files differ only in the header line. It was scored once. The "software by industry" intent currently has no page.

---

## 2. Corpus audit

### 2.0 Method notes

- **Checker** (`geo_content_check.py --format md --pretty`) was run on each page. Treat these three signals as artefacts:
  - `fluff: next-generation` on every page comes from the footer link "Next-generation Automation", not from the body copy.
  - `Quotes: 2–3` come from the header comment's meta JSON.
  - The 21-item list is the footer navigation.
- **Lists and tables:** no range or software page has a table. The only real content lists are on #18, #46, #47 and #48.
- **Word counts:** body text is 317–1,103 words, of which about 100 are shared chrome ("Need help?" block plus footer).

### 2.1 Product range pages (#13–18)

#### Prompts used (inferred: 1 seed + fan-out)

| # | Seed prompt | Fan-out |
|---|---|---|
| 13 Smart-UPS | What is APC Smart-UPS and which one for a server rack? | Smart-UPS vs On-Line · Li-ion option · SNMP/NMC monitoring · runtime extension · VA/W range |
| 14 Galaxy | Which Galaxy UPS for a 500 kW data center? | VX vs VXL · VS power range/voltages · eConversion efficiency · Li-ion · Symmetra PX replacement |
| 15 PacT | What does PacT Series include; which breaker for 4000 A? | MTZ vs NW · UL 489 breakers · VigiPacT vs Vigirex · MicroLogic compatibility · MV VCB 24 kV |
| 16 9 Series | What is the 9 Series; which Acti9 device do I need? | iC60 rating · RCBO vs RCCB · Resi9 vs Acti9 · AFDD options · Multi9 for OEMs |
| 17 Line Series | What is Line Series; which Canalis system? | KS vs KT · busbar vs cable · iBusway for DC · KBA vs KBB · harsh environments 6300 A |
| 18 PowerLogic | What is PowerLogic; which meter/relay? | ION9000 vs PM8000 · Modbus / IEC 61850 compatibility · P5 vs P3 · class A PQ meter · AccuSine sizing |

#### Page-by-page audit

| # | What an AI would extract / quote | Strongest GEO elements | Weakest GEO elements | Prompt performance (seed / fan-out) |
|---|---|---|---|---|
| **13 Smart-UPS** (18) | "APC Smart-UPS™ is trusted throughout the world to protect equipment and critical data…"; member lines "Ideal UPS for servers, point-of-sale, routers…"; NMC via "web browser, command line interface, or SNMP" | Application per member; SNMP named | **No number with a unit anywhere** (G7). Tagline "The most trusted UPS in the world"; no VA/W, topology or Li-ion facts; off-topic drives promo; "Discover" H1 | Seed: partial (what), no choice basis. Fan-out: SNMP yes; On-Line vs others implied only; VA range, Li-ion models, runtime: no |
| **14 Galaxy** (32) | Per-member kW bands: VS 10–150 kW, VL 200–500 kW, VX 500–1500 kW, VXL 500–1250 kW, each with data-center size; "efficiency up to 99% in eConversion mode"; "eConversion is not available for Galaxy VXL 480V" | Best member descriptors in the corpus; quantified efficiency with condition; honest limitation | **500 kW falls in VL, VX and VXL, and the page gives no tie-breaker.** VXL voltage shown as "(400V)" and "(400V or 480V)"; "Galaxy VS Accessories" card describes the UPS ratings; VL paragraph repeats a sentence; Symmetra PX listed with no status or relation | Seed: AI can shortlist but not decide. VS range: yes. VX vs VXL: weak. Symmetra replacement: no |
| **15 PacT** (35) | Scope "from 16 to 6300 A in low voltage and up to 40.5 kV"; sub-range ratings/voltages (MasterPact 630–6300 A ≤ 415 VAC; ComPact 16–3200 A ≤ 690 VAC; PowerPact 15–600 A ≤ 480 VAC); UL 489; "(formerly Vigirex)"; MicroLogic compatibility | Densest facts in the corpus; legacy name; compatibility; UL-market choice cue | Hype ("world-class" ×5, "legendary", "future-proof"); casing inconsistency (EvoPacT/EvoPact, FuPact/FuPacT, Masterpact/MasterPact, Compact/ComPact); 6 identical "See product details" H2s; no MTZ vs NW guidance | Seed 4000 A: AI can list MTZ/NW/UL/Navy/DC but not choose. UL 489: yes. Vigirex: yes. MicroLogic: yes. MTZ vs NW: "advanced digital features" only |
| **16 9 Series** (23) | "final level of protection in the electrical distribution in homes and buildings"; Acti9 ratings (63/100/40/125 A); device types (RCCB, RCBO, AFDD, SPD Type 2/3) | Segment split Resi9 = homes / Acti9 = buildings / Multi9 = OEMs; identifiers | Resi9 cards are tautological ("Resi9 Protection Protection devices"); two RCBOs and two arc-fault devices not differentiated; emotional copy ("feel safe everywhere at every moment"); no standards; typo "Telecom nd IT" | Seed: segment-level only. iC60 rating: yes. RCBO vs RCCB: names only. AFDD: listed, not explained |
| **17 Line Series** (36) | "busbar trunking system… up to 6300A"; plug-and-play decentralized architecture; ratings KN 160 A, KS 1000 A, KT/KR 6300 A; KR for harsh environments | Neutral, explanatory tone; environment differentiates KT vs KR; segments named | Line Series ↔ Canalis relationship never stated; "optimized compared to a cable solution" not quantified; no standard (busbar trunking standard), no accessories/tap-offs, no connectivity despite "connected" | Seed: AI can pick by current rating. Busbar vs cable: claim only. KBA vs KBB: "(1 or 2 circuits)" partial |
| **18 PowerLogic** (12) | Product names only (P7/P5/P3/P1, ION9000, PM8000…, AccuSine, DVR), each rendered three times; tab labels with no panel content | Model codes paired with category nouns | **No facts at all** (G7): no accuracy class, protocols, ratings or standards; H1 = brand only; key info apparently in tabs | Seed: fails. Modbus/IEC 61850: fails (a classic fan-out). ION9000 vs PM8000: fails |

#### Cross-page patterns (ranges)

- **Done well, consistently:**
  - Every member is named and almost always paired with a category noun.
  - Applications are usually attached to members.
  - Self-contained card lines ("Canalis KS Busbar trunking system for power distribution up to 1000 A") are quotable as is.
- **Done badly, consistently:**
  - No comparison table.
  - No explicit "choose X if…" statements.
  - No FAQ.
  - No dates or lifecycle status.
  - Standards almost absent.
  - Legacy names rare (only PacT).
  - Protocols absent (a fatal gap for PowerLogic).
  - Lead copy is promotional; the meta description is often more factual than the visible text (e.g. Line Series, PacT).

#### Template-level vs author-level issues (ranges)

| Level | Issue | Pages | Owner |
|---|---|---|---|
| **Template** | "Discover X" / brand-only H1 (no category noun) | 13, 14, 15, 17 (16, 18 brand-only) | Template + content owner |
| Template | Generic H2s "Explore our offer", "See product details" (up to 6× per page) | 13–17 | Template |
| Template | Card text rendered 2–3× in server HTML (visible line + heading + sr-only) | 13–18 | SE Digital (out of scope) + RNG-9 c4 |
| Template | Off-topic cross-promotion block ("EcoStruxure Asset Advisor for drives") | 13, 14, 16 | Template/campaign owner |
| Template | Same "Need help?" block and footer on every page (about 100 words) | all 11 | n/a (chrome); below the boilerplate penalty threshold |
| Template | No slot for a comparison table, FAQ, standards or "last updated" | 13–18 | Template |
| Template | Video hero ("Choose a video") with no text equivalent | 13, 15–18 | SE Digital |
| Template | Tab labels without panel content in server HTML | 18 | SE Digital |
| **Author / PIM** | Tautological or empty card descriptors | 16 (Resi9), 18 | PIM champion |
| Author / PIM | Wrong card text (accessories card carries UPS ratings), VXL voltage inconsistency, repeated sentence | 14 | PIM champion / content owner |
| Author | Brand casing inconsistency | 15 | Content owner |
| Author | Superlatives / emotional copy | 13, 15, 16, 18 | Content owner |
| Author | Missing legacy/successor mapping (Symmetra PX, MasterPact NW→MTZ) | 14, 15 | SME / PIM |

### 2.2 Software pages (#43–48)

#### Prompts used (inferred)

| # | Seed prompt | Fan-out |
|---|---|---|
| 43 Portfolio hub | What industrial software does Schneider Electric offer? | Unity Pro replacement · electrical-design software (Ecodial/ETAP/Caneco) · SE–AVEVA relationship · licensing · data-center/UPS software |
| 44 | = #43 (redirect) | — |
| 45 DCIM | Is EcoStruxure IT cloud or on-premise; what does it integrate with? | What is EcoStruxure IT · protocols (SNMP/Modbus/BACnet) · IEC 62443 / ISO 27001 · pricing/licensing · IT Expert vs IT Advisor vs Data Center Expert |
| 46 Trials | Does EcoStruxure IT offer a free trial? | Trial length · what's included · hardware / credit card needed · requirements · country availability |
| 47 Ops mgmt | Which SE software manages operations in large buildings? | Building Operation vs Building Advisor · PME vs Power Operation · BACnet support · predictive HVAC maintenance · cloud vs on-prem |
| 48 Energy mgmt | Which energy management software for large commercial buildings? | Resource Advisor vs PME · demand response · EV load management · Microgrid Operation vs Advisor · portfolio benchmarking / ISO 50001 |

#### Page-by-page audit

| # | What an AI would extract / quote | Strongest | Weakest | Prompt performance |
|---|---|---|---|---|
| **43 Portfolio hub** (26) | Tool one-liners: "Programming software for Modicon PACs (formerly Unity Pro)", "Setup software to configure Altivar, Altistart, Lexium and TeSys…", "compatible with Harmony and Magelis HMI"; Microsoft "30-year global partnership" | Former names, which suit migration prompts; hardware compatibility | H1 "Our agnostic software portfolio" with no definition; 10 flagship products are **name-only cards** (AVEVA, ETAP, Planon…); 6 category headings and 7 persona tabs **with no content**; SE–AVEVA relationship not explained; fluff 1.23/100w; vague CTAs ("View now" ×8) | Seed: an AI gets a list, not a map. Unity Pro: yes. Electrical design: names only. AVEVA: no. Licensing: link label only |
| **45 DCIM** (30) | "Data center infrastructure management (DCIM) software is used to monitor, measure, and manage data centers…"; "EcoStruxure IT is Schneider Electric's comprehensive DCIM software platform."; "mandatory two-factor authentication and high encryption standards"; "GDPR-compliant"; Wellcome Sanger "5-10% savings" (expected) | Category definition first; security controls; named customer figure | **No protocols or vendors** behind "Supports multi-vendor ecosystems."; software deployment model not stated (the "on-premise, at the edge, or in hybrid" phrase describes the *infrastructure*, so an AI may misread it); modules (IT Expert, IT Advisor, Data Center Expert, NetBotz) appear only in a forum blurb; no licensing/pricing/trial link; no certification number; whole H2 block duplicated; label-only tiles; typos | Seed: misanswerable (deployment ambiguity) / integrations unanswered. Definition: yes. Security certs: no. Pricing: no, so third parties will answer. Module comparison: no |
| **46 Trials** (22) | "free trials… designed to meet your DCIM needs"; list of about 75 country links | H1 matches the navigational intent; confirms a free trial exists | No trial length, scope, products, hardware needs, eligibility or expiry; "Belgium (French)" listed twice | Seed: yes. All fan-out: no |
| **47 Ops mgmt** (27) | Module one-liners (Building Operation, Building Advisor, PME, Power Operation, Power Advisor, Microgrid Operation); bullets ("Automate HVAC, lighting, and blinds based on occupancy…") | Functions mapped to named modules; good headings and lists; KPI footnotes name sources (150 Holborn / Sidara, Sofia, Aspiria) | **KPI labels have no numbers** in HTML ("Power uptime¹"); **"ZZ_Paragraph Title" placeholder live**; H1 "Operations Management" omits "software" and "large buildings" (the title tag has them); unnamed, unquantified case; no protocols (BACnet), deployment or security | Seed: list of modules, OK. Module comparison: weak. BACnet: no. Cloud/on-prem: no |
| **48 Energy mgmt** (26) | Module one-liners incl. Resource Advisor, EV Charging Expert, Microgrid Advisor; "participate in demand response programs"; "grid code compliance" | Functions mapped to modules; use cases (demand response, grid services) | KPI numbers missing; Citycon case unquantified with an unattributed superlative ("smartest and most energy-efficient real estate on the market"); Microgrid Operation/Advisor each listed twice with different copy; no integrations, security or licensing | Seed: candidate list, no selection basis. Demand response: yes. Resource Advisor vs PME: no |

#### Cross-page patterns (software)

- **Done well:**
  - Function-level one-liners per module, phrased as verb + object.
  - Former product names on the hub.
  - Category definition on the DCIM page.
  - Footnoted KPI sources (the right practice, but the values are missing).
- **Done badly, everywhere:**
  - None of the 5 pages names a protocol or integration method, a certification by number, a licensing model, system requirements or a version.
  - Proof is unquantified or projected.
  - No "which module for which need" guidance.
  - No dates.
- **Template-level issues:**
  - KPI counter components whose values are missing from server HTML (#47, #48).
  - Tab/persona components with no server-side content (#43).
  - Duplicated H2 block (#45).
  - Logo walls as images only (#45, #47, #48).
  - "ZZ_" placeholder slots published (#47).
  - Generic H1 slots (#47, #48).
- **Author-level issues:**
  - Unsupported "agnostic" / "multi-vendor" claims.
  - Promotional voice.
  - Typos.
  - Duplicate module entries.
  - Unquantified case blurbs.
- **#44 duplicate.** The inventory lists two URLs for one page. Recommend deduplicating the inventory, and deciding whether a real "software by industry" page should exist. Today the redirect means the industry intent is not served.

---

## 3. External research and exemplars

Accessed 2026-10-19 unless dated. Labels: [C] controlled · [L] large-sample correlational · [O] official · [P] practitioner.

### 3.1 B2B software and AI answers

| Finding | Source (date) | Label |
|---|---|---|
| 51% of B2B software buyers start research in an AI chatbot more often than in Google (29% in Apr 2025). **#1 use case: comparing vendor strengths and weaknesses (41%)**. 69% changed vendor because of chatbot guidance. 45% find review-site citations most confidence-inspiring | G2 "Answer Economy" (survey Mar 2026, n=1,076; release 15 Apr 2026) via https://aijourn.com/new-g2-research-half-of-b2b-software-buyers-now-start-their-research-with-ai-chatbots/ | [L] vendor survey |
| AI chat ranks #1 for shortlisting, review sites #2, vendor sites #3. Example prompt bundles constraint + use case + compatibility ("CRM for a hospital that works on iPads") | G2, Tim Sanders (6 Oct 2025) https://learn.g2.com/ai-search-surging-for-b2b-buyers | [L] |
| 63% used AI in buying; **94% of AI users fact-check the output** | TrustRadius 2026 Buying Disconnect (15 Jul 2026) via https://agilebrandguide.com/trustradius-bridging-the-b2b-buying-disconnect-ai-trust-and-go-to-market-strategies-for-2026/ | [L] secondary |
| 100 B2B products × pricing/integrations/security tasks × 5 runs: first-party answer rates **79% / 93% / 92%**. Pricing = 77% of all third-party citations. **Hidden price → 45% of runs cite a third party**; even with a public price, 18%. Access errors push fallback to 77%. Advice: real prices or price drivers in HTML text, not only in JS or calculators | Indig & Kaufman, Growth Memo "Where AI agents get stuck on your site" (13 Jul 2026) https://www.growth-memo.com/p/where-ai-agents-get-stuck-on-your | [L] structured test (partly paywalled; engines not disclosed) |
| ChatGPT software citations (35k URLs, Dec 2025): vendor/other 70.4%, UGC 17.1%, review platforms 8.6% (13.2% at evaluation stage). G2 family = 84% of review-platform citations | G2/Indig (13 Feb 2026) https://learn.g2.com/do-software-review-platforms-show-up-more-in-the-bottom-of-the-funnel | [L], one engine, one month |
| B2B SaaS "best/alternatives" queries: review platforms 7.3% of citations; vendor pages 24% (ChatGPT) vs 12% (Perplexity) | Growfusely (28 Jul 2026) https://growfusely.com/blog/ai-citation-analysis-b2b-software/ | [L] small |
| Review-platform share in AIO: 34.5% of AIOs cite at least one review platform, but 93% of those sit in the source block, not the answer (SE Ranking, Dec 2025). Gartner Peer Insights vs G2 share conflicts across studies | Omnibound compilation (7 Oct 2026) https://www.omnibound.ai/blog/do-review-sites-g2-capterra-drive-ai-citations-b2b | [L] secondary |
| SaaS GEO practice: pricing in text with "who this tier is for", integration directory, trust center (SOC 2 / ISO 27001), balanced comparison tables, consistent facts across site, review sites and marketplaces. **No controlled evidence**; nothing found on changelogs | e.g. https://www.prosemedia.com/blog/saas-seo-ai-search-playbook | [P] |

### 3.2 Range / product-family selection

| Finding | Source | Label |
|---|---|---|
| Passage-level selection. Measurable specifics ("42 dB" not "quiet"). Comparison tables for feature comparisons. **Don't hide key answers in tabs, expandable menus, images or PDFs.** Short Q&A pairs | Microsoft Bing Ads blog, Krishna Madhavan (8 Oct 2025) https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers | [O] |
| No special requirements for AI features; keep important content in text; AI Mode fans out across sub-topics | Google Search Central "AI features and your website" (upd. 10 Dec 2025) https://developers.google.com/search/docs/appearance/ai-features | [O] |
| Variant data model (ProductGroup, `variesBy`) and Merchant Center conversational attributes incl. **related products: substitute / compatible / accessory**. These are the official hooks for variant axes and legacy → replacement mapping (no documented ranking boost) | Google product-variants docs (Feb 2024); Merchant Center attributes (GML, 20 May 2026) via productsup.com | [O] |
| **Format effect is small; position is large.** Across 2,400 tests (3 engines), answer accuracy was 93.5–94.6% whether a fact sat in a table, bullet, first or third sentence. Document position mattered about 3× more (71.9% first vs 39.4% middle) | 5WPR (12 Aug 2026) https://www.5wpr.com/new/do-tables-and-bullets-increase-ai-citations-new-findings-from-2-400-tests/ | [C] small, not peer-reviewed |
| No study found on discontinued-model replacement prompts or industrial "which X for N kW" prompts | — | gap |

### 3.3 Exemplars (what they show for the logic)

- **Eaton 93PM UPS family page.** https://www.eaton.com/us/en-us/catalog/backup-power-ups-surge-it-power-distribution/eaton-93pm-ups.html
  - Strong:
    - definition sentence;
    - specs in HTML (10–200 kW; 97% double conversion / 99% ESS; up to 8 parallel units; THDi ≤ 3.5%);
    - certifications by number (UL 1778, IEC 61000-4-5);
    - applications;
    - legacy-resource link.
  - Weak:
    - specs behind tabs;
    - no variant table or selection guidance;
    - PDF-only brochure;
    - no date;
    - conflicting dimension values.
  - **Implication:** even a competitor family page lacks RNG-1/RNG-2, so these are differentiating opportunities for SE.
- **Sunbird DCIM** (homepage + /pricing). This is the closest DCIM competitor exemplar.
  - Strong:
    - **prices in text** ($5.50/node/month Power IQ; $19.50/cabinet/month dcTrack);
    - licensing unit (per cabinet / per node; subscription or perpetual);
    - **free 30-day trial using the buyer's own data**;
    - **system requirements in text** (2 VMware ESXi instances, 8 GB RAM, 160 GB disk, 4 cores);
    - named integrations (ServiceNow, BMC, Jira, VMware, LDAP/AD);
    - Gartner and Capterra ratings.
  - Weak:
    - no ISO 27001 / SOC 2;
    - no protocol list;
    - no definition sentence.
  - **Implication:** this is the benchmark for SW-2/SW-3/SW-5 and for trial pages.
- **Siemens Desigo CC.**
  - Strong:
    - "open, multi-discipline, integration platform" definition;
    - 6-question FAQ (SaaS, upgrade, cybersecurity, third-party integration);
    - SNMPv3 / Modbus mentioned;
    - SaaS option.
  - Weak:
    - no pricing/licensing, trial, requirements, IEC 62443 or edition comparison.
- **Datadog pricing** (SaaS benchmark).
  - Strong:
    - unit prices in text;
    - free tier defined (5 hosts, 1-day retention);
    - tier comparison tables;
    - billing FAQ ("How do you define a host?");
    - region selector;
    - SOC 2 / PCI / HIPAA;
    - integrations count.
  - **Atlassian Jira pricing returned only its title to the fetcher.** This is a warning that JS-rendered pricing is invisible to some agents (out-of-scope observation type).

**Evidence summary for weighting:**

- Strong:
  - concrete verifiable facts, relevance, freshness and neutral tone (skill evidence-base [C]);
  - for software, the integrations/security/pricing triad (Indig [L]) plus comparison as the #1 AI use (G2 [L]).
- Weak or contested:
  - table/list **format** per se (5WPR [C], skill evidence [C]);
  - FAQ format;
  - schema.
- Gaps:
  - industrial selection and migration prompts. Treat RNG-8 as [O]+[P] inferred.

---

## 4. Proposed logic

Shared conventions (unchanged from the skill):

- U1–U10 are reused with their standard checks c1–c5 and anchors. Below, "range note" / "software note" only clarifies how to read a check for the type.
- Type criteria use checks → level ceiling (`round(5·p/n)`, 5 only if all pass).
- Link-anchor checks are **N/A when the source has no visible link/CTA labels** (corpus markdown strips links).

### 4.1 Product range page — RNG v1.1 (revision of `page-types.md` §2)

**What AI extracts:**

- what the family is and who it is for;
- the members (variants **or, on master ranges, sub-ranges**) and how they differ;
- selection axes with thresholds (rating, voltage, poles, topology, form factor, communication);
- ecosystem and protocols;
- standards;
- **legacy names and successor mapping**.

Prompts: "What is [range]?", "Which [range] for [N kW / A / application]?", "[A] vs [B]", "Is [range] compatible with [protocol]?", "Replacement for [legacy]".

**Master ranges vs ranges (sub-variant decision).** SE master ranges (e.g. PacT) are portfolio hubs above ranges (MasterPact, ComPact…) and sub-ranges (MTZ, NW…). The AI jobs are the same at both levels (define → differentiate → select → migrate); only the *unit of comparison* changes. So there is **one logic and one weight set**:

- On a master range, rows of RNG-1 and members of RNG-9 = sub-ranges.
- On a range page, they are variants.
- A master range is *not* expected to carry PDP-level specs. It must carry **one decision-relevant figure per member** (rating band, voltage) and a "best for".

**Must-haves:**

1. Definition sentence "[Range] is a family of [category] for [application], covering [scope with units]".
2. HTML comparison table of members × decision attributes + "best for".
3. Explicit choice statements, including for overlapping members.
4. One self-contained, unique descriptor per member with rating + application.
5. Standards by number, mapped to members/regions.
6. Compatibility and protocols.
7. Legacy names + successor path + lifecycle status.
8. Visible "last updated".
9. 3–5 FAQ on selection, compatibility and migration.

**Common failures (seen in the corpus):**

- "Discover X" hero with no category noun;
- name-only or tautological cards;
- triplicated card text;
- selection delegated to the Product Selector;
- overlapping members not disambiguated;
- off-topic cross-promotions;
- standards and legacy names missing;
- facts behind tabs or video.

#### Criteria (weights after calibration, sum = 100)

| ID | Criterion | W | Checks (pass definition) | Family | Rationale / evidence |
|---|---|---|---|---|---|
| U1 | Range definition & scope | 10 | Standard c1–c5. *Range notes:* c1 = definition with category noun + application; c2 = H1/title names range **and** category noun (fails on "Discover X" / brand-only); c5 = "range at a glance" (member list + scope) | answer_def | Answer-first: 44% of ChatGPT citations from the first 30% of a page [L]; position about 3× format (5WPR [C]) |
| U2 | What / Who / When / Outcome | 5 | Standard (anchor table) | answer_def | Banner test [SE]; reduced from 6 because RNG-9 carries member-level who/when |
| RNG-1 | Member comparison table with "best for" | **10** (was 16) | c1 HTML-text table exists (not image/PDF/configurator); c2 rows = members, ≥ 3 shared decision attributes; c3 values with units, one per cell, consistent; c4 "best for" / typical-application column; c5 covers all members shown | comparison | Comparisons +55% absorption [L]; Microsoft tables guidance [O]; **format alone ≈ no effect** (5WPR, C-SEO [C]), so it is the *aligned attributes* that matter. Reduced at calibration (§5.3) |
| RNG-2 | Selection guidance in text | 12 | c1 explicit choice statements for ≥ 2 members in conditional/comparative form ("Choose VL for 200–500 kW…; above 500 kW choose…"); card "Ideal for…" lines do **not** count; c2 selection axes named with thresholds + units; c3 selection possible from text alone (not only via Product Selector/configurator); c4 overlapping/adjacent members explicitly disambiguated | comparison | G2: comparison = #1 AI use (41%) [L]; seed prompts are selection prompts |
| RNG-3 | Applications, segments & references | 6 | c1 ≥ 3 named segments/applications; c2 applications attached to specific members; c3 ≥ 1 named reference/case with a metric | proof | Use-case precision decides vendor notice (Semrush) [L] |
| RNG-4 | Quantified differentiators | 5 | c1 ≥ 1 range-level claim with number + unit (scope alone doesn't count); c2 measurement basis/condition stated; c3 differentiator statements free of unanchored superlatives | other | Facts over adjectives [C]; overlaps RNG-9, so reduced from 8 |
| RNG-5 | Ecosystem, compatibility & protocols (*re-scoped*) | 6 | c1 accessories/complementary products named with function; c2 communication protocols / connectivity named (Modbus, SNMP, Ethernet, IEC 61850…); c3 cross-range compatibility stated (e.g. trip units → breakers); c4 monitoring/management software named | **specs** (was none) | Aligns with PDP-3 and Merchant "compatible/accessory" [O]; protocol prompts are standard Evaluation fan-out. Migration moved to RNG-8 |
| RNG-6 | Common standards & certifications | 5 | c1 ≥ 1 product standard by number; c2 standards mapped to members/regions (IEC vs UL variants); c3 certifications/declarations named (listing, PEP/EPD, marine…) | specs | Verifiability; 94% fact-check AI (TrustRadius) [L] |
| RNG-7 | Range FAQ | 4 (was 6) | c1 ≥ 3 Q&A pairs; c2 cover selection, compatibility or migration; c3 direct answer first, range/member named | other | FAQ format evidence contested [C/L]; value comes from matching real questions |
| **RNG-8** | **Lifecycle, legacy names & migration (new)** | 6 | c1 legacy/former names stated ("formerly Vigirex"); c2 successor/replacement path for legacy members; c3 lifecycle status of members (current / end of commercialization / replaced by…); c4 generation identifiers distinguish current from previous generations | commercial | "Replacement for [legacy]" is a core Decision prompt [SE buyer-journey]; Merchant "substitute" relation [O]; no direct citation study (gap) → moderate weight |
| **RNG-9** | **Member descriptors (new)** | **11** (cal.) | Over *product members* (exclude accessory/service cards): c1 every member has a descriptor beyond its name (category noun + function; tautologies fail); c2 ≥ 75% carry a key rating with unit; c3 ≥ 50% state an application / "best for"; c4 descriptors unique (no verbatim double/triple rendering, no copy-paste between members); c5 no off-topic cards inside range content | specs | Cards *are* the content unit of SE master ranges; self-contained, fact-bearing passages (+56% RAG correctness [C]); quotable as is |
| U3 | Extractable structure & self-containment | 5 | Standard | other | Enabler [C] |
| U5 | Evidence & attribution | 3 | Standard | evidence | Low on hubs; standards are scored in RNG-6 |
| U7 | Neutral tone | 4 | Standard (c4 N/A on brand range pages) | tone | Promotion hurts (OR up to 362 against) [C] |
| U8 | Entity clarity & consistency | 5 | Standard; *range note:* c1 also covers brand casing and the explicit master-range ↔ range relationship | other | Consistency OR 1.7–4.1 [C]; G1 |
| U9 | Freshness | 3 | Standard | freshness | Strong evidence, but hubs change slowly; lifecycle is in RNG-8 |

**Changes vs v1.0 (explained):**

| Change | Why |
|---|---|
| RNG-1 16 → 10 | Format alone has a near-null effect [C]. The facts it holds are also rewarded in RNG-9/RNG-2. Still the largest single "standard" gap |
| RNG-2 12 → 12 | No change |
| RNG-3 8 → 6, RNG-4 8 → 5 | Overlap with RNG-9 (member-level applications and ratings) |
| RNG-5 7 → 6, re-scoped and moved to *specs* | Protocols added; migration split out to RNG-8 |
| RNG-7 6 → 4 | Weak FAQ evidence |
| U2 6 → 5, U3 6 → 5, U5 4 → 3 | Free weight for the new criteria |
| + RNG-8 (6) | Separates the migration intent |
| + RNG-9 (11) | Scores the actual content unit of hub pages |

**Natural stages:** Consideration (default for master ranges) · Evaluation (single ranges with specs). Mismatch flag: Awareness.

**Gates and penalties (range):**

- G1, G2, G5 and G6 as standard.
- **New G7 (cap 49):** no rating, capacity or size with a unit for the range or any member in HTML text. A range page that cannot answer "what does it cover?" fails its core job. This is softer than G3 (40) because hubs are not PDPs.
- **New penalty `template_artifact` (−2):** placeholder or test text, or an entire section rendered twice verbatim. Card-title duplication is *not* penalized here; it is scored in RNG-9 c4 so it is not double-counted.
- Existing `fluff_density` and `cta_overload` apply.

**Recommendation templates (range):**

| Failed check | Template |
|---|---|
| U1 c1/c2 | Replace "Discover [Range]" with "[Range] [category noun] range" and add under it: "**[Range] is a family of [category] for [applications], covering [min–max rating with units] across [N] sub-ranges: [A], [B], [C].**" Owner: content owner |
| RNG-1 | Add "Compare [Range] models": rows = members; columns = [rating band] · [voltage] · [topology/form factor] · [communication] · **Best for**. One value per cell, units in the header. Owner: PIM champion |
| RNG-2 c1/c4 | Add "Which [Range] model do I need?": 3–6 conditional lines, e.g. "Below [X kW]: choose [A]. [X–Y kW] in [application]: choose [B]. Above [Y kW], or when [criterion]: choose [C] rather than [D] because [quantified difference]." Values `[VERIFY]` |
| RNG-9 c1–c3 | Rewrite each card to "[Member] – [category noun] for [application], [rating range with units]". Remove tautologies ("Protection devices"). Owner: PIM champion |
| RNG-9 c4/c5 | Template fix: render card text once. Remove off-topic promotions from range templates. Owner: SE Digital / template owner |
| RNG-5 c2 | Add "Connectivity and compatibility": protocols, gateways, compatible software, compatible ranges |
| RNG-6 | Add "Standards and certifications": product standards by number per member/region (`[VERIFY]`) |
| RNG-8 | Add "Replacing an older range?": "[Legacy] → [current member]" lines, lifecycle status, and a link to the substitution tool |
| RNG-7 | 3–5 FAQ items: "Which [Range] for [N kW/A]?", "Is [Range] compatible with [protocol]?", "What replaces [legacy]?" |
| U9 | Visible "Last updated [Month YYYY]" tied to a real review (twice a year for ranges, and on every generation launch) |

**Intake fields (range, extends `intake-sheets.md` B):**

- Range level (master range / range / sub-range)
- Member list (sub-ranges or variants)
- Decision attributes + units
- Overlapping members to disambiguate
- Legacy / former names + successors + lifecycle status per member
- Protocols / compatible software
- Standards per member/region
- Flagship references
- PIM source for card text
- Template type (to separate template from author fixes)

### 4.2 Software page — SW v1.0 (new)

**What AI extracts:**

- what the software is (category definition);
- capabilities mapped to modules;
- **integrations / protocols**;
- **deployment model** and system requirements;
- **security / compliance**;
- **licensing / pricing logic and trial terms**;
- proof;
- which product or edition for which need;
- version and former names.

These are the exact questions in the Indig agent study and the G2 surveys.

**Sub-variants** (classify like datasheet vs document):

- **software_product:** one product or platform (e.g. #45 DCIM). Natural stage **Evaluation** (Consideration acceptable).
- **software_hub:** portfolio or use-case hub listing several products (e.g. #43, #47, #48). Natural stage **Consideration**.
- **software_trial:** trial, download, licensing or conversion page (e.g. #46). Natural stage **Decision**.

**Classifier rule:**

- ≥ 3 software products each with its own card → hub.
- One product's capabilities as the main content → product.
- The main content is a sign-up, download or licensing action → trial.

**Must-haves (product):**

1. "[Product] is a [category] software that [function] for [audience]".
2. Capabilities mapped to modules/editions.
3. Named protocols and integrated systems.
4. Deployment model (cloud / on-prem / hybrid / edge) + requirements.
5. Security controls + certifications by number (IEC 62443-x-x, ISO/IEC 27001, SOC 2) + trust resource.
6. Licensing model, pricing logic or price drivers, trial terms.
7. Named customer with a measured outcome.
8. Edition/module comparison.
9. Version / what's new / former names.
10. Visible update date.

**Common failures:**

- benefit-label tiles with no text;
- "multi-vendor / agnostic" with no specifics;
- deployment phrasing that describes the customer's infrastructure rather than the software;
- logo walls as images;
- KPI counters with no values in HTML;
- name-only portfolio cards;
- trial pages with no terms;
- pricing absent, so third parties answer (45% fallback).

#### SW criteria (checks)

| ID | Criterion | Checks (pass definition) | Family |
|---|---|---|---|
| **SW-1** | Capabilities & use cases in text | c1 ≥ 3 capabilities as concrete functions (verb + object + context), not benefit slogans; c2 capabilities mapped to named modules/editions/products; c3 ≥ 1 capability with a measurable parameter (scale, frequency, granularity in numbers, latency, # devices); c4 jobs-to-be-done / use cases named; c5 no label-only tiles or empty capability headings. *Hub note:* applies to each listed product's descriptor | specs |
| **SW-2** | Integrations, protocols & interoperability | c1 named protocols/standards (BACnet, Modbus, SNMP, OPC UA, MQTT, IEC 61850…); c2 named third-party systems/platforms or device families; c3 integration method (API, connectors, gateways) or SE hardware compatibility named; c4 "agnostic / multi-vendor / open" claims backed by specifics (N/A if no such claim) | specs |
| **SW-3** | Deployment, architecture & requirements | c1 **software** deployment model stated (SaaS / on-prem / hybrid / edge); c2 scale/limits or architecture components; c3 system requirements / supported OS / browsers / mobile stated or linked by name; c4 implementation/onboarding path (time, partner-delivered, services) | specs |
| **SW-4** | Security, privacy & compliance | c1 concrete controls (MFA, encryption, RBAC…); c2 certifications/standards by number (IEC 62443-x-x, ISO/IEC 27001, SOC 2…); c3 privacy/residency (GDPR, hosting region); c4 named security resource (trust center, cybersecurity notifications, vulnerability disclosure) | specs |
| **SW-5** | Licensing, pricing model & trial | c1 licence model (subscription/perpetual; per device/point/site/user; tiers); c2 price, range or an explicit "what drives price / sold via partner" statement; c3 trial/demo with ≥ 2 terms (duration, scope, cost, own-data allowed, hardware needed, expiry); c4 how to acquire/activate (direct, partner, marketplace, licence portal) | commercial |
| **SW-6** | Proof & quantified outcomes | c1 named customer + quantified **achieved** outcome; c2 outcome with baseline/timeframe/method or scope; c3 third-party validation named with year (analyst, review platform, certification); c4 page statistics attributed to a named source **and visible as numbers** | proof |
| **SW-7** | Product / edition map & selection | c1 products/editions listed with one-line differentiation; c2 "which product for which need" guidance (by role, site size, use case); c3 comparison table of editions/products with shared attributes; c4 relationships between products explained (Expert vs Advisor; on-prem vs cloud counterpart; SE vs AVEVA) | comparison |
| **SW-8** | Versions, lifecycle & former names | c1 current version / "what's new" with date; c2 former product names stated; c3 support lifecycle (supported versions, end of support) or release notes named | freshness |

#### Weights per sub-variant (after calibration, sum = 100)

| ID | product | hub | trial | Rationale |
|---|---|---|---|---|
| U1 | 10 | 12 | 12 | Answer-first; hubs must define the portfolio; trial must state the trial offer in sentence 1 |
| U2 | 5 | 6 | 6 | Banner test |
| SW-1 | 12 | 12 | 12 | Use-case precision decides notice (Semrush [L]) |
| SW-2 | 11 | 6 | — | Integrations answered first-party in 93% of agent runs when present (Indig [L]); key OT/BMS fan-out |
| SW-3 | 9 | 4 | 14 | Deployment and requirements are evaluation and trial blockers; Sunbird exemplar |
| SW-4 | 9 | 4 | 6 | Security 92% first-party when present (Indig [L]); IEC 62443 is expected for OT software |
| SW-5 | 11 | 4 | 26 | Pricing = 77% of third-party citations; 45% fallback when hidden (Indig [L]); a trial page's whole job |
| SW-6 | 8 | 8 | — | Evidence-backed claims win (OR 2–46 [C]); 45% trust review citations (G2 [L]) |
| SW-7 | 5 | 16 | — | Comparison = #1 AI use (41%, G2 [L]); a hub's main job is routing to the right product |
| SW-8 | 4 | 6 | — | Former names answer migration prompts; version signals freshness |
| U3 | 4 | 8 | 6 | Enabler; hubs suffer most from tabs and empty components |
| U7 | 4 | 5 | — | Promotion hurts [C] |
| U8 | 4 | 5 | 6 | Consistency; descriptive anchors |
| U9 | 4 | 4 | 6 | Freshness [C]; trial terms change |
| U10 | — | — | 6 | Next step on a conversion page (reduced from 12 at calibration) |

**Stage families for new IDs:**

- SW-1 → specs
- SW-2 → specs
- SW-3 → specs
- SW-4 → specs
- SW-5 → commercial
- SW-6 → proof
- SW-7 → comparison
- SW-8 → freshness
- RNG-5 → specs
- RNG-8 → commercial
- RNG-9 → specs
- RNG-4 and RNG-7 → other

**Gates and penalties (software):**

- G1, G2, G5 and G6 as standard. G6 applies when the core content is only in a gated PDF or video.
- **New G8 (cap 49), software_product / software_trial:** the page states *none* of: deployment model, integrations/protocols, security facts, licensing/pricing/trial terms. Justification: these are the agent tasks, and their absence hands the answer to third parties.
- **Penalties:**
  - `template_artifact` (−2): placeholder text, or a section duplicated verbatim.
  - Standard `cta_overload` (−1) and `fluff_density` (−2).

**Recommendation templates (software):**

| Failed check | Template (facts `[VERIFY]` / `[SME]`) |
|---|---|
| U1 c1 | "**[Product] is a [DCIM / BMS / EMS / SCADA] software that [primary function] for [audience/site type], deployed [on-premises / as SaaS / hybrid].**" |
| SW-1 c2/c5 | Replace label-only tiles with "[Capability] — [module]: [what it does, with a parameter]". Delete tiles that can't be filled |
| SW-2 | Add "Integrations and protocols": protocols list; named third-party systems; API/connector method; "Multi-vendor: tested with [vendors/device classes]". Link to an integration directory |
| SW-3 | Add "Deployment and system requirements": model(s); server/VM/OS/DB minimums; supported browsers/mobile; typical implementation path (partner / services) |
| SW-4 | Add "Security and compliance": controls; certifications by number with scope `[VERIFY]`; data residency; link to cybersecurity notifications / trust center |
| SW-5 | Add "Licensing and pricing": licence model + unit; price or price drivers ("priced per [device/point/site]; available through [channel]"); trial terms; how to buy. Never invent prices |
| SW-6 | Lead the case teaser with "[Customer] [achieved metric] in [timeframe] with [module], measured by [method]". Put KPI values in text with their footnote source |
| SW-7 (hub) | Add "Which [segment] software do I need?": table of products × job × deployment × audience + 3–5 "choose X if…" lines; explain relationships (Expert vs Advisor; SE vs AVEVA) |
| SW-8 | Add "Current version: [x.y] ([Month YYYY]) — what's new" and "(formerly [name])" for renamed tools |
| Trial | Add a 40–60-word answer block: "[Product] offers a free [N]-day trial of [modules], [cloud/on-prem], using [your own devices/demo data]; requires [X]; converts to [licence] at expiry." Plus a 3–5-item trial FAQ |

**Intake fields (software):**

- Sub-variant (product / hub / trial)
- Product name + former names
- Modules / editions
- Deployment options
- Protocols / integrations list
- Security certifications + trust-center URL
- Licensing model and pricing-disclosure policy (public / partner / quote)
- Trial terms
- System-requirements URL
- Current version + release-notes URL
- Approved customer metrics with method
- Review-platform presence (G2 / Capterra / Gartner Peer Insights): advisory, off-page
- Region restrictions

---

## 5. Pilot scores and calibration

### 5.1 Scores (calibrated weights; natural stage stated)

Judge JSONs: `research/type-analysis/pilot/NN_judge.json`. All quotes were verified as substrings (normalized whitespace, case and zero-width characters): **0 quote failures**. Confidence is high on all pages (full server-HTML text).

| Page | Type key | Stage | Score | Band | Gates / penalties | Top 3 gaps (recoverable eff. points) |
|---|---|---|---|---|---|---|
| #13 Smart-UPS | range | Consideration | **19** | Poor | G7 (cap 49, non-binding) | RNG-2 (15.6), RNG-1 (13.0), U1 (6.9) |
| #14 Galaxy | range | Consideration | **32** | Poor | — | RNG-1 (13.0), RNG-2 (9.4), U1 (6.9) |
| #15 PacT Series | range | Consideration | **35** | Poor | — | RNG-1 (13.0), RNG-2 (6.3), U1 (5.2) |
| #16 9 Series | range | Consideration | **23** | Poor | — | RNG-1 (13.0), RNG-9 (10.5), RNG-2 (9.4) |
| #17 Line Series | range | Consideration | **36** | Poor | — | RNG-1 (13.0), RNG-2 (6.3), RNG-5 (5.7) |
| #18 PowerLogic | range | Consideration | **12** | Poor | G7 (non-binding) | RNG-2 (15.6), RNG-1 (13.0), RNG-9 (8.4) |
| #43 Software portfolio hub | software_hub | Consideration | **26** | Poor | cta_overload −1 | SW-7 (16.9), SW-6 (8.4), U1 (8.4) |
| #44 (redirect → #43) | — | — | = #43 | — | duplicate, not re-scored | — |
| #45 EcoStruxure IT DCIM | software_product | Evaluation | **30** | Poor | template_artifact −2 | SW-2 (13.1), SW-5 (9.6), SW-3 (8.6) |
| #46 EcoStruxure IT Trials | software_trial | Decision | **22** | Poor | — | SW-5 (25.0), SW-3 (14.6), SW-1 (12.5) |
| #47 Ops mgmt (large bldgs) | software_hub | Consideration | **27** | Poor | template_artifact −2 | SW-7 (16.9), SW-6 (8.4), U1 (6.3) |
| #48 Energy mgmt (large bldgs) | software_hub | Consideration | **26** | Poor | — | SW-7 (16.9), SW-6 (8.4), U1 (6.3) |

#### Level matrix — range (level, effective weight)

| Criterion | #13 | #14 | #15 | #16 | #17 | #18 |
|---|---|---|---|---|---|---|
| U1 | 1 | 1 | 2 | 2 | 2 | 1 |
| U2 | 3 | 4 | 2 | 2 | 4 | 2 |
| U3 | 2 | 2 | 2 | 2 | 2 | 1 |
| U5 | 0 | 0 | 1 | 0 | 0 | 0 |
| U7 | 0 | 2 | 0 | 0 | 3 | 0 |
| U8 | 2 | 2 | 2 | 4 | 4 | 4 |
| U9 | 1 | 1 | 1 | 1 | 1 | 1 |
| RNG-1 (13.0) | 0 | 0 | 0 | 0 | 0 | 0 |
| RNG-2 (15.6) | 0 | 2 | 3 | 2 | 3 | 0 |
| RNG-3 | 3 | 3 | 2 | 3 | 3 | 0 |
| RNG-4 | 0 | 3 | 0 | 0 | 2 | 0 |
| RNG-5 | 2 | 2 | 2 | 2 | 0 | 1 |
| RNG-6 | 0 | 0 | 3 | 0 | 0 | 0 |
| RNG-7 | 0 | 0 | 0 | 0 | 0 | 0 |
| RNG-8 | 0 | 0 | 2 | 0 | 0 | 0 |
| RNG-9 (10.5) | 2 | 3 | 3 | 0 | 3 | 1 |

#### Level matrix — software

| Criterion | #43 hub | #47 hub | #48 hub | #45 product | #46 trial |
|---|---|---|---|---|---|
| U1 | 1 | 2 | 2 | 3 | 3 |
| U2 | 2 | 1 | 1 | 3 | 2 |
| U3 | 2 | 3 | 3 | 2 | 2 |
| U7 | 0 | 2 | 0 | 3 | — |
| U8 | 4 | 4 | 4 | 4 | 2 |
| U9 | 1 | 1 | 1 | 1 | 1 |
| U10 | — | — | — | — | 3 |
| SW-1 | 2 | 3 | 3 | 2 | 0 |
| SW-2 | 2 | 0 | 0 | 0 | — |
| SW-3 | 0 | 2 | 1 | 1 | 0 |
| SW-4 | 0 | 0 | 0 | 3 | 0 |
| SW-5 | 1 | 0 | 0 | 0 | 1 |
| SW-6 | 0 | 0 | 0 | 2 | — |
| SW-7 (hub 21.1) | 1 | 1 | 1 | 0 | — |
| SW-8 | 3 | 0 | 0 | 2 | — |

### 5.2 Does it discriminate?

- **Range: yes.**
  - Spread 12 → 36 (24 points).
  - Ordering against expert judgement: PowerLogic (name-only cards) < Smart-UPS (no numbers) < 9 Series (mixed descriptors) < Galaxy ≈ PacT ≈ Line (fact-bearing descriptors).
  - **Line (36) vs Galaxy (32)** looks counter-intuitive, because Galaxy has richer decision facts. Galaxy loses on three things, each of them real:
    - inconsistencies (U8 2);
    - promotional lead (U1 1, U7 2);
    - **no tie-breaker at exactly the seed prompt's 500 kW** (VL/VX/VXL overlap; RNG-2 c4).
  - The 4-point gap is within the ±3 band-edge noise the judge protocol flags for triple judging. Both pages are Poor.
- **Software: narrow** (22–30).
  - This reflects systemic gaps: no page passes SW-2 c1, SW-4 c2, SW-5 c1/c2 or SW-8 c1.
  - The logic still separates the product page (30: definition, security facts, named metric) from hubs (26–27) and from the trial page (22).
  - Positive exemplars are needed in the gold set to test the top of the scale (see §7).
- **Headroom test (simulation, not saved as pilot).** Applying the top recommendations to the judge files (scratch `sim14.json`, `sim45.json`):
  - Galaxy (variant table, decision path, standards, FAQ, Symmetra migration, date, definition H1) → **70 (Good)**.
  - DCIM (protocols + vendors, deployment + requirements, licensing model + trial, certifications, module map, date) → **71 (Good)**.
  - Both logics can reward good content, and Good is reachable with realistic edits. 90+ stays rare.
- **Non-discriminating criteria (0 or constant on all pages), and the decision on each:**

| Criterion | Pilot result | Decision |
|---|---|---|
| RNG-1 | 0/6 | **Keep** as the global standard (most-cited must-have; competitor exemplar also lacks it, so it is a differentiator). Weight reduced |
| RNG-7 | 0/6 | Keep at low weight (4). SE-wide FAQ absence is a finding, not a logic flaw |
| U9 | 1 everywhere | Keep. No dates anywhere is a template issue, and freshness is [C]-strong |
| SW-4 / SW-5 | 0 on hubs | Keep at low hub weight (4 each) |
| SW-7 on hubs | 1 everywhere | Keep. Routing is the hub's purpose |
| G7 / G8 | Non-binding in pilot (scores already < 49) | Keep as safety nets for pages that are otherwise well written but fact-free |

### 5.3 Counter-intuitive weight effects found → one recalibration (before/after)

1. **Trial page over-credited for routing.**
   - At Decision, U10 (default 12) × commercial 1.5 gave the country selector 14.3 effective points, about a third of the page's score.
   - Result: a page with no trial terms scored 26, near the DCIM page (30).
   - **Change:** U10 12 → 6; SW-5 24 → 26; SW-3 12 → 14; SW-1 10 → 12.
2. **RNG-1 dominance with a near-null format effect.**
   - At Consideration (comparison × 1.5), RNG-1 took 15.5 effective points and was 0 on every page.
   - **Change:** RNG-1 12 → 10, RNG-9 9 → 11. This rewards decision facts wherever they sit, while keeping the table as the standard.

| Page | v1 (pre-cal) | v1.1 (cal.) |
|---|---|---|
| #13 | 18 | 19 |
| #14 | 31 | 32 |
| #15 | 34 | 35 |
| #16 | 23 | 23 |
| #17 | 35 | 36 |
| #18 | 11 | 12 |
| #43 | 26 | 26 |
| #45 | 30 | 30 |
| #46 | 26 | **22** |
| #47 | 27 | 27 |
| #48 | 26 | 26 |

The judge files did not change between runs; only the weights did. Pre-calibration weights are kept as `weights_range_software_v1.json` in the scratchpad.

### 5.4 Judge observations (for κ calibration)

- **Borderline checks** (expect rater disagreement):
  - U1 c1 on "trust-claim" leads (#13) vs role leads (#16);
  - RNG-2 c1 on card "Ideal for…" lines (resolved: these don't count);
  - SW-6 c1 on a projected figure (#45, passed with c2 failing);
  - SW-3 c1 on infrastructure-vs-software deployment phrasing (#45, failed).
- **Write these rules into the criterion text as exemplars** (critique shadowing, judge-protocol §6.4).
- **N/A use:**
  - U7 c4 (competitors) is N/A on brand range/product pages.
  - U8 c4 is N/A when no link labels are visible.
  - SW-2 c4 is N/A when no openness claim is made.

---

## 6. Proposed weights JSON fragment (merge into `assets/weights.json` after review)

```json
{
  "families": {
    "comparison": ["...existing...", "SW-7"],
    "specs":      ["...existing...", "RNG-5", "RNG-9", "SW-1", "SW-2", "SW-3", "SW-4"],
    "proof":      ["...existing...", "SW-6"],
    "commercial": ["...existing...", "RNG-8", "SW-5"],
    "freshness":  ["...existing...", "SW-8"]
  },
  "page_types": {
    "range":            {"U1": 10, "U2": 5, "RNG-1": 10, "RNG-2": 12, "RNG-3": 6, "RNG-4": 5, "RNG-5": 6, "RNG-6": 5, "RNG-7": 4,
                         "RNG-8": 6, "RNG-9": 11, "U3": 5, "U5": 3, "U7": 4, "U8": 5, "U9": 3},
    "software_product": {"U1": 10, "U2": 5, "SW-1": 12, "SW-2": 11, "SW-3": 9, "SW-4": 9, "SW-5": 11, "SW-6": 8,
                         "SW-7": 5, "SW-8": 4, "U3": 4, "U7": 4, "U8": 4, "U9": 4},
    "software_hub":     {"U1": 12, "U2": 6, "SW-7": 16, "SW-1": 12, "SW-2": 6, "SW-3": 4, "SW-4": 4, "SW-5": 4, "SW-6": 8,
                         "SW-8": 6, "U3": 8, "U7": 5, "U8": 5, "U9": 4},
    "software_trial":   {"U1": 12, "U2": 6, "SW-5": 26, "SW-3": 14, "SW-1": 12, "SW-4": 6, "U10": 6, "U3": 6, "U8": 6, "U9": 6}
  },
  "gates": {
    "G7": {"cap": 49, "desc": "Range page with no rating/capacity/size with a unit for the range or any member in HTML text"},
    "G8": {"cap": 49, "desc": "Software product/trial page that states none of: deployment model, integrations/protocols, security facts, licensing/pricing/trial terms"}
  },
  "penalties": {"template_artifact": 2}
}
```

**Weight sums:** all four types = 100. The selftest passes with the merged file.

**Script and docs follow-ups (for the skill owner):**

- Add aliases to `TYPE_ALIASES` in `geo_score_calc.py`: "software", "software page" → `software_product`; "software hub"; "software trial".
- Update `page-types.md` §2 and add a §2b Software.
- Add the intake rows to `intake-sheets.md`.
- Add the fix-library rows to `recommendations-playbook.md`.

---

## 7. Open questions and risks

1. **Pricing disclosure policy.** SW-5 rewards "what drives price / sold via partner" statements even without prices. Does SE allow public licence models or price drivers for EcoStruxure software? Without them, the Indig data predicts third-party answers (directories, editorial) for pricing prompts.
2. **Certification facts need SME sign-off** (IEC 62443 component/process certifications, ISO/IEC 27001 scope per offer). The agent must never infer them. Use `[VERIFY]`.
3. **Template backlog vs author backlog.** About half of the recoverable points come from template slots that don't exist: comparison table, FAQ, "last updated", standards block, single-render cards, no off-topic promos, KPI values in HTML, no placeholder publishing. Recommend routing these to SE Digital/UX as a **master-range and software template change**, not page-by-page edits.
4. **PIM ownership.** Range member descriptors (RNG-9) and the attributes for RNG-1 live in PIM/OfferDAM. The fix owner is the PIM champion. Confirm attribute availability (rating bands, voltages, lifecycle status, successor refs).
5. **Gold-set imbalance.** All 11 pilot pages are Poor. Calibration needs strong pages (e.g. a well-built SE single-range page, a competitor exemplar such as the Sunbird pricing/requirements pages, or a rewritten Galaxy draft) to test the 70–90 region and κ.
6. **Judge variance.** Galaxy vs Line and several borderline checks (§5.4) need 2–3 human raters and triple LLM runs before locking.
7. **Out-of-scope technical findings to SE Digital** (not scored):
   - card text rendered 2–3× in server HTML;
   - KPI counters without values in HTML (#47, #48);
   - tab panels empty server-side (#18, #43);
   - video heroes without text equivalents;
   - #44 redirect / inventory duplicate;
   - logo walls image-only.
8. **Evidence gaps.**
   - No study on industrial selection or migration prompts, so RNG-8 and the RNG-2 weights are [O]+[P] inferred.
   - Software findings are mostly vendor-run [L] (G2 is a review platform with an interest; Indig is partly paywalled).
   - Re-check quarterly.
9. **Sub-variant boundaries.**
   - #47/#48 are "use-case hubs" sitting between solution page and software hub. If the business wants them to rank for "what is building energy management software", consider scoring them also under `solution` logic and comparing.
   - Similarly, the DCIM page could double as a category explainer ("what is DCIM"). Its opening definition is a strength to keep.
10. **G7/G8 thresholds** were non-binding in the pilot. Confirm the cap value (49) with the business, or drop them if the team prefers no type-specific gates.

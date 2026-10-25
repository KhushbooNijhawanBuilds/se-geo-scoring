# Buyer-Journey Stages, Intents & Stage Multipliers (v1.0)

The Score Agent deck lists 5 stages, with "definition needed". These are the proposed definitions. They reconcile the SE Playbook (Awareness / Consideration / Decision), the Toolkit (+ Purchase, Post-purchase) and the 4 intents (Informational, Comparative/Commercial, Transactional, Navigational).

## 1. Stage definitions

| Stage | Definition (buyer mindset) | Typical AI prompts | Dominant intent | Content most cited at this stage |
|---|---|---|---|---|
| **Awareness** | Recognizes a problem, risk, trend or opportunity. **No solution category or vendor in mind yet.** | "Why does my facility have power quality issues?" · "What is grid congestion and how does it affect factories?" | Informational (problem / definition / why) | Explainers, articles, glossary, trend/thought-leadership, third-party media, problem framing on solution pages |
| **Education** | Understands the problem and is **learning how possible solutions and technologies work**: principles, standards, approaches, terminology. Building the vocabulary and criteria for later. | "How does a Type B RCD work?" · "What standards apply to EV charging installations?" · "What is SF6-free switchgear?" | Informational (how / what standards) | Guides, whitepapers, standards explainers, glossary, technical articles, document gateways, how-it-works videos |
| **Consideration** | Has decided a solution category is needed and is **exploring approaches and shortlisting options/vendors**. | "Best types of energy meters for commercial buildings" · "AC vs DC coupled PV storage" · "Top MV switchgear options for hospitals" | Commercial / comparative (category-level) | Category pages, selection/buying guides, technology comparisons, listicles (often third-party), range pages, solution pages |
| **Evaluation** | Comparing **specific products/vendors against requirements**: specs, compatibility, compliance, proof, TCO/ROI. Builds the business case. | "Galaxy VX vs [competitor] for a 500 kW data center" · "Is [product] compatible with Modbus TCP?" · "ROI of modular UPS" | Comparative / transactional research | PDPs, range pages, datasheets, case studies, comparison pages, calculators, reviews, certification docs |
| **Decision** | Ready to **specify, buy or install**. Needs final justification, availability, pricing logic, where to buy, documents and support. | "Where to buy [ref]?" · "[ref] lead time" · "[ref] installation manual" · "replacement for [legacy ref]" | Transactional / navigational | PDPs, distributor/where-to-buy, support/FAQ, manuals, documents, warranty/lifecycle pages |
| *(Post-purchase, optional)* | Operating, troubleshooting, upgrading, renewing. | "[ref] error code E05" · "how to commission…" | Informational / navigational | Support KB, FAQ, manuals, community, training |

## 2. Stage signals (U10, check c1)

| Stage | The content **should** contain | Red flags (stage mismatch) |
|---|---|---|
| Awareness | Problem definition, why it matters, quantified impact, plain language, neutral tone, link to Education content | Product pitch, specs-first, hard sales CTA ("Buy now", "Request a quote") |
| Education | Mechanisms, principles, standards by number, diagrams explained in text, terminology defined, vendor-neutral framing | Only brand claims; no explanation of how/why |
| Consideration | Selection criteria, option types, comparison tables, "best for" framing, trade-offs, alternatives named fairly | Single-product page with no context; self-ranking lists |
| Evaluation | Specs with units, compatibility, certifications, case studies with metrics, TCO/ROI data, documents accessible | Vague benefits, no numbers, missing proof |
| Decision | Exact identifiers (ref, GTIN), availability/where to buy, lifecycle/substitutes, warranty, installation docs, clear descriptive CTA | Long educational intro before the facts; no next step |

## 3. Stage multipliers (applied to page-type default weights, then renormalized to 100)

| Criterion family (IDs) | Awareness | Education | Consideration | Evaluation | Decision |
|---|---|---|---|---|---|
| Answer-first & definitions (U1, U2, GLO-1) | 1.4 | 1.3 | 1.0 | 0.9 | 0.9 |
| Evidence, authority, original insight (U5, ART-3, DOC-8) | 1.2 | 1.4 | 1.1 | 1.0 | 0.8 |
| Fan-out coverage (U6) | 1.2 | 1.3 | 1.1 | 1.0 | 0.8 |
| Neutral tone (U7) | 1.4 | 1.3 | 1.2 | 1.0 | 0.7 |
| Comparison & selection (CMP-*, CAT-1/2/3, RNG-1/2, PDP-6) | 0.6 | 0.9 | 1.5 | 1.4 | 1.0 |
| Specs, compatibility, standards (PDP-1/3/4, RNG-6, DOC-3, U4) | 0.7 | 0.9 | 1.1 | 1.5 | 1.3 |
| Proof (PDP-7, CS-*, SOL-5, RNG-3) | 0.7 | 0.9 | 1.2 | 1.4 | 1.2 |
| Commercial, lifecycle, next step (PDP-8, U10, BLK-8, FAQ-7) | 0.5 | 0.6 | 0.9 | 1.1 | 1.5 |
| Freshness (U9, DOC-7) | 1.0 | 1.0 | 1.1 | 1.1 | 1.2 |
| All other criteria | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

**Procedure:** effective_w_i = default_w_i × m(stage, family_i). Then scale all effective weights so they sum to 100. The script `scripts/geo_score_calc.py` does this deterministically.

## 4. Page type × stage fit matrix (flag mismatches; do not refuse to score)

| Page type | Natural stages | Mismatch to flag |
|---|---|---|
| Glossary | Awareness, Education | Decision |
| Article / blog | Awareness, Education, (Consideration) | Decision (unless it is a how-to/install article) |
| Solution page | Awareness → Consideration | — |
| Document: whitepaper | Education, Consideration | Decision |
| Document: datasheet / manual | Evaluation, Decision, Post-purchase | Awareness |
| Category | Consideration, (Evaluation) | Awareness |
| Comparison / selection guide | Consideration, Evaluation | Awareness |
| Range | Consideration, Evaluation | Awareness |
| PDP | Evaluation, Decision | Awareness, Education |
| Case study | Evaluation, Decision, (Consideration) | Awareness |
| FAQ / support | Education, Decision, Post-purchase | — |
| CaaS block | any (inherits the host page) | — |

## 5. Persona hints (B2B industrial; tailor the U10 language check)

| Role | What they ask AI for | Emphasis |
|---|---|---|
| Specifier / consultant / design firm | Standards, compliance, BIM/CAD, specification text | U5 standards, DOC-*, PDP-4 |
| Design engineer | Specs, selection, compatibility, sizing | PDP-1/3, CAT-1, CMP-* |
| Panel builder / machine builder | Integration, footprint, wiring, certification, lead time | PDP-1/3/8, DOC-3 |
| Procurement / distributor | Availability, references, lifecycle, substitutes, pricing logic | PDP-8, U9 |
| Facility / plant / data center manager | TCO, uptime, case studies, ROI | CS-3, SOL-4 |
| Contractor / electrician / installer | Installation, wiring, troubleshooting, compatibility | FAQ-*, DOC-2 steps, VID-* |
| C-level | Strategy, risk, ROI, sustainability | SOL-1/4, ART-3 |
| IT channel partner / system integrator | Interoperability, protocols, margins, support | PDP-3, SOL-2 |

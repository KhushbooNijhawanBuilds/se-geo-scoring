# Content Brief Intake Sheets (draft v2.1, 20 Oct 2026, for To-Do 03)

The deck says a pre-designed intake sheet helps the agent understand the content better. Section A is common to every page type. Section B adds page-type fields. Fields marked ★ are mandatory per the Score Agent deck.

## A. Common fields (all page types)

| # | Field | Format / allowed values | Used by |
|---|---|---|---|
| A1 | ★ Page type | PDP · Range · Category · CaaS block · Editorial (common) · Article/blog · News/press release · Solution/industry page · Service (recurring / project) · Software (product / hub / trial) · Case study · Calculator/TradeOff Tool · White paper (gateway) · ESG report / ESG hub · Document (datasheet/catalog/guide/manual) · Comparison/selection guide · FAQ/support · Glossary · Video | Logic selection |
| A2 | ★ Topic | Free text (e.g. "MV switchgear for hospitals") | U1, U6 |
| A3 | ★ Industry | Data centers · Buildings · Healthcare · Industry/machine builders · Utilities/grid · Residential · Infrastructure · F&B · Other | U10, fan-out |
| A4 | ★ Buyer-journey stage | Awareness · Education · Consideration · Evaluation · Decision (definitions in buyer-journey.md) | Multipliers, U10 |
| A5 | Target audience (+ example) | Persona/role, e.g. "Specifier at a design firm (SOFIA)" | U2, U10 |
| A6 | Country / market | ISO country; language | BLK-7, units/standards (IEC vs UL) |
| A7 | Target AI prompts / questions (recommended mandatory — decision for the 22 Oct review) | 1–5 prompts (from Profound if available). If missing, the agent infers them and lowers confidence | U1, U6, ART-2 |
| A8 | Content source | Live URL · file · pasted text · brief | Confidence |
| A9 | Run mode | Score only · Recommendations only · Both | Flow |
| A10 | Last substantive update date | YYYY-MM | U9 |
| A11 | Content owner / editable in | Builder.io · PIM/OfferDAM · DAM · YouTube | Recommendation owner |
| A12 | Template | GEO Power Page · GEO Optimized Template · Power Couple · Other | Recommendation rules |

**Recommendations add:** R1 ★ Primary business objective · R2 Known competitor names/pages · R3 Target customer / job role · R4 Desired CTA / next step.

## B. Page-type-specific fields

| Page type | Extra fields |
|---|---|
| **PDP** | Product reference/SKU · commercial name + plain-language name · range · lifecycle status (active / EOL / successor ref) · category attribute list or link to the spec DB (for completeness checks) · linked datasheet/manual (optional, for the consistency check) · primary applications (owner's view) · key differentiators vs siblings · B2C/B2B/both · where-to-buy model (direct/distributor) |
| **Range** | Range level (master / range / sub-range) · member list · decision attributes + units · overlapping members to disambiguate · legacy/former names + successors + lifecycle status per member · protocols/compatible software · standards per member/region · flagship references · PIM source for card text · template type |
| **Software** | Sub-variant (product / hub / trial) · product name + former names · modules/editions · deployment options · protocols/integrations · security certifications + trust-center URL · licensing model and pricing-disclosure policy · trial terms · system-requirements URL · current version + release-notes URL · approved customer metrics with method |
| **Category** | Category name + synonyms customers use · sub-types · featured ranges · governing standards/regulations · existing selection guides/tools to link |
| **CaaS block** | Block format (definition / benefit / spec snippet / FAQ / stat / quote / CTA / object description short-medium-long) · host pages (list or count) · character limits · canonical claim source + date · localization variants |
| **Editorial** (common logic) | Primary question the page answers · key insight (one sentence) · author / SME reviewer · publish date · related pages to cross-link |
| **Article / blog** | Primary question · key insight (1 sentence) · thesis sentence · author name + role + relevant experience (not "Guest Blogger") · SME reviewer · original data / field evidence (source, conditions) · statistics with source and year · publish date + last substantive update date · next-stage SE asset for the CTA (title + URL) · related articles · syndicated version URL |
| **News / press release** | Release subtype (launch / reference design / partnership / research / corporate-event / financial / award → sets the stage) · canonical offer name + page URL · key facts with basis · "first/only" claims with scope and substantiation · availability (markets + absolute date/quarter) · price/pricing model or how to obtain · maturity (pilot/GA/roadmap; standards by number) · evidence asset (title/ID) · spokespeople + third-party quote approval · partners with descriptor · boilerplate version · publication date (time zone) + dateline city · attachments regenerated with the same date (Y/N) · related releases/posts · wire distribution (reporting only) |
| **Document** | Sub-type · file name · revision/version + date · gated? (Y/N) · HTML gateway URL (if any) · linked PDP(s) · methodology/test standard (whitepapers/datasheets) |
| **Case study** | Customer name + approval to name, industry, size/scale, country · project dates (start, go-live, results period) · primary outcome (metric, unit, baseline value + year, period, scope) · secondary outcomes · measurement method and verifier · offers used with the role of each · partner/integrator · approved quote (speaker, role, Y/N) · video URL + transcript (Y/N) · template (QDS campaign / legacy) · publish/update date · related solution page |
| **Calculator / TradeOff Tool** | Tool name + short name · tool URL + iframe URL · model version and date · owner team · methodology source (white paper number + title) · core formula/logic (SME text) · inputs with units, ranges, defaults · output metrics with definitions · assumptions with value, unit, source, data year · default scenario and outputs · typical result ranges with source · region/currency/price-year basis · known limitations · sibling tools |
| **Comparison / selection guide** | Options compared (incl. non-SE) · decision criteria · data sources for competitor/alternative facts · review date |
| **FAQ / support** | Question sources (support tickets/sales/prompts) · products covered (applies-to) · last review date · related manuals |
| **Glossary** | Term + synonyms/abbreviation · governing standard · related terms |
| **Solution / industry page** | Problem statement + source and year · named offers/components with roles · integration protocols, standards, third-party systems · segments/applications + scale range + new-build/retrofit · quantified outcomes + basis for each · references (customer, site, metric, timeframe, quote approval) · engagement phases + delivery model + typical duration · governing standards · last substantive update · template (hero answer slot Y/N) |
| **Service** | Service name + variant (recurring / project) · plans/tiers and differences · included / excluded / add-ons · eligible equipment (ranges, models, generations, multi-vendor Y/N, prerequisites) · service levels per plan and region + source + legal clearance to publish (Y/N) · process steps + roles + start + typical duration · contract/pricing model · countries · outcome claims + basis/sample/year · references with metrics + quote approval · delivery organization facts · applicable standards · last substantive update |
| **White paper (gateway)** | ★ doc ref / WP number · ★ title · ★ release date + version (+ change note) · ★ gated Y/N · authors + roles · 3–5 key findings with source page · target prompts / questions answered · method/standards · related tools/papers/solutions · supersedes / superseded-by · PDF text supplied Y/N · languages |
| **ESG report / hub** | ★ report type · ★ reporting period · ★ release date + version (+ change note) · ★ canonical report name · headline KPI sheet (metric, value, unit, period, basis, assured Y/N) · targets (baseline, target year, progress, SBTi status) · frameworks · assurance level/provider/scope · restatements · previous/next edition URLs · data annex / GRI-ESRS index / CDP URLs · audience · Legal/claims review status · PDF text supplied Y/N |
| **Video** | YouTube URL · SE page where it's embedded · transcript/SRT available (Y/N) · chapters (Y/N) · video type |

## C. Example (PDP intake, filled)

| Field | Value |
|---|---|
| Page type | PDP |
| Topic | Type B RCCB for EV charging |
| Industry | Buildings / EV charging infrastructure |
| Stage | Evaluation |
| Audience | Electrical contractor specifying EV charger protection |
| Country | FR |
| Target prompts | "Which RCD type is required for EV chargers?" · "Type B vs Type A EV RCCB" |
| Business objective | Increase distributor sell-through of the Type B range |
| Competitors | [competitor pages, if any] |
| CTA | "Find a distributor for [ref]" |

# Content Brief Intake Sheets (draft v1.0, for To-Do 03)

The deck says a pre-designed intake sheet helps the agent understand the content better. Section A is common to every page type. Section B adds page-type fields. Fields marked ★ are mandatory per the Score Agent deck.

## A. Common fields (all page types)

| # | Field | Format / allowed values | Used by |
|---|---|---|---|
| A1 | ★ Page type | PDP · Range · Category · CaaS block · Editorial (common) · Article/blog · Document (datasheet/whitepaper/catalog/guide/manual) · Case study · Comparison/selection guide · FAQ/support · Glossary · Solution/industry page · Video | Logic selection |
| A2 | ★ Topic | Free text (e.g. "MV switchgear for hospitals") | U1, U6 |
| A3 | ★ Industry | Data centers · Buildings · Healthcare · Industry/machine builders · Utilities/grid · Residential · Infrastructure · F&B · Other | U10, fan-out |
| A4 | ★ Buyer-journey stage | Awareness · Education · Consideration · Evaluation · Decision (definitions in buyer-journey.md) | Multipliers, U10 |
| A5 | Target audience (+ example) | Persona/role, e.g. "Specifier at a design firm (SOFIA)" | U2, U10 |
| A6 | Country / market | ISO country; language | BLK-7, units/standards (IEC vs UL) |
| A7 | Target AI prompts / questions | 1–5 prompts (from Profound if available) | U1, U6 |
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
| **Range** | Range name + legacy/predecessor range names · number of variants · decision attributes (e.g. rating, poles, curve, comms) · segments served · flagship references |
| **Category** | Category name + synonyms customers use · sub-types · featured ranges · governing standards/regulations · existing selection guides/tools to link |
| **CaaS block** | Block format (definition / benefit / spec snippet / FAQ / stat / quote / CTA / object description short-medium-long) · host pages (list or count) · character limits · canonical claim source + date · localization variants |
| **Editorial / Article / blog** | Primary question the article answers · key insight (one sentence) · author / SME reviewer · original data or field experience available · publish date · related articles to cross-link |
| **Document** | Sub-type · file name · revision/version + date · gated? (Y/N) · HTML gateway URL (if any) · linked PDP(s) · methodology/test standard (whitepapers/datasheets) |
| **Case study** | Customer (anonymize if needed), industry, size, country · products/modules used · primary quantified result + baseline + timeframe · how it was measured · quote approval (Y/N) |
| **Comparison / selection guide** | Options compared (incl. non-SE) · decision criteria · data sources for competitor/alternative facts · review date |
| **FAQ / support** | Question sources (support tickets/sales/prompts) · products covered (applies-to) · last review date · related manuals |
| **Glossary** | Term + synonyms/abbreviation · governing standard · related terms |
| **Solution / industry page** | Problem statement + data source · architecture components (named offers) · quantified outcomes · references/case studies |
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

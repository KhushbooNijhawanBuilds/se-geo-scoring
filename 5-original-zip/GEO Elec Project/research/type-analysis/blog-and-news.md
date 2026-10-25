# Content GEO Score logic for two page types: blog articles and news / press releases

*Type analysis for the SE Content GEO Score Agent. Prepared 2026-10-19 by the blog_news analysis agent. It builds on skill `geo-research` v1.0 (2026-10-13). This is a proposal: nothing in the skill folder was edited.*

Pilot judge files are in `research/type-analysis/pilot/` as `01–06_judge.json` and `49–54_judge.json` (v2, final). The merged weight files (v1 and v2), the v1 judge backups and the score cards are in the session scratchpad under `agents/blog_news/`.

---

## 1. Executive summary

- **Blog articles.** This keeps the existing §6 Article logic with targeted revisions:
  - ART-1 is now judged on quality, not just presence.
  - ART-2 adds two checks: title consistency and whether the title's promise is delivered.
  - ART-3 is now checkable through 5 binary checks, and its weight rises from 6 to 10.
  - U4 rises from 8 to 10 and U9 falls from 8 to 5.
  - The criteria stay at 12 and sum to 100.
- **News / press releases.** This is a new logic with 12 criteria: 6 new NEWS-* criteria plus U2, U3, U4, U6, U7 and U8.
  - It drops U1, U5, U9 and U10, which are replaced by press-release-shaped criteria:
    - headline and deck (NEWS-1)
    - temporal anchoring (NEWS-2)
    - claim substantiation (NEWS-3)
    - substantive quotes (NEWS-4)
    - offer facts and availability (NEWS-5)
    - About block and canonical bridge (NEWS-6)
  - The default stage is set by release subtype: launch or partnership → Consideration; research → Education; corporate or event → Awareness.
- **Pilot results (v2).**
  - Blogs: 36–71, median 48.5. Ranked 02 (71) > 05 (69) > 04 (52) > 03 (45) > 06 (39) > 01 (36).
  - Press releases: 40–59, median 56.5. Ranked 52 = 53 (59) > 50 (58) > 49 (55) > 51 (51) > 54 (40).
  - Both ranges match the framework's calibration intent (un-optimized pages land at 35–60, and 90+ is rare). The blog logic discriminates clearly.
  - The news spread is narrower. That is mostly real: five of the six releases share one template and one authoring style. The weakest release (54) is clearly separated.
- **SE-wide patterns.**
  - Blogs split into two families:
    - Technical "insight" posts (02, 05), which follow the SE blog checklist (summary block, dated sources, descriptive H2s) and score Good or near-Good.
    - Executive/opinion posts (01, 03, 04, 06), which open with narrative, use slogan titles, give unsourced numbers and have no takeaways block. These score Poor to Average.
  - Releases are fact-rich in the deck. They consistently lose points on:
    - an ambiguous numeric date
    - relative timing ("early next year")
    - subheads that aren't headings
    - a missing "About Schneider Electric" block (5 of 6)
    - executive quotes with no checkable fact
    - unscoped "world's first" or "pioneering" claims
- **Template vs author.**
  - Three newsroom template or process fixes alone would add an estimated **+3 to +7 points per release**:
    - written-out date
    - subheads as real headings
    - an About block with entity facts in the HTML

    This is a simulation on a checks-ceiling basis, so treat it as indicative.
  - Blog losses are mostly author-level. The template issues there are:
    - "Top picks" and "Add a comment" render as H2s inside the article
    - the byline reads "Guest Blogger"
    - there is no visible "Updated" date
- **Evidence caveat.** Owned newsroom pages are about 3% of AI citations overall, but about 18% of ChatGPT citations (BuzzStream, Jan 2026, about 4M citations, [L]). Syndicated or wire press releases are cited only 0.04–0.21% of the time. The news score therefore measures how quotable the **canonical se.com release** is. Most of a release's AI value is indirect, through the earned coverage it seeds.

---

## 2. Corpus audit

**Method.** All 12 pages were read in full. `geo_content_check.py --format md` was run on each one (signals summarized below). Prompts were derived per page as 1 seed + 3–5 fan-out prompts; they are inferred and listed in each judge JSON (`page.target_prompts`). Page text was treated as data.

### 2.1 Blog articles (blog.se.com, Sep–Oct 2026)

**Deterministic signals (checker):**

| # | Words | H2 question share | Lists | Quantified facts per 100 words | Standards | Fluff per 100 words | Images with empty alt |
|---|---|---|---|---|---|---|---|
| 01 | 1,131 | 0% | 2 | 0.71 | 0 | 0.27 | 5/5 |
| 02 | 1,561 | 8% | 3 | 0.32 | 0 | 0.13 | 5/5 |
| 03 | 782 | 55% | 2 | 0.26 | 0 | 0.13 | 4/5 |
| 04 | 1,174 | 18% | 4 | 0.68 | 0 | 0.43 | 4/5 |
| 05 | 1,304 | 14% | 4 | 0.38 | 0 | 0.00 | 4/5 |
| 06 | 1,065 | 11% | 1 | 0.47 | 0 | 0.19 | 4/6 |

On every page the checker's "lead sentence" starts with the template strings (date, view count, read time, byline). This confirms that AI systems see those strings before the first sentence of the article.

**Page-by-page audit:**

**01 – "Modular, prefabricated data centers enter the AI era…"** (Education, 36 Poor)
- Seed prompt: *Why are prefabricated modular data centers needed for AI factories?*
- What AI would extract or quote:
  - "power densities per rack are close to 250 kW vs 10-20 of cloud"
  - "AI factory campuses can be up to 10 gigawatts"
  - rack figures for 246/227 kW products
  - the closing thesis "prefabrication is a necessity today"
- Strongest elements: 30 years of first-hand perspective; concrete density figures; a clear end thesis.
- Weakest elements:
  - opens with a biography
  - Star-Trek pun in the H1
  - "A slow start" history section takes 20% of the article
  - benefits listed as adjectives ("Fewer risks")
  - no sources, no summary, no CTA
- Prompt fit: covers the seed only at the end. Fan-outs on density and pods are good; "how much faster or cheaper" has no numbers.

**02 – "Data center community opposition: How cooling design affects water, noise, and permitting"** (Education, 71 Good)
- Seed prompt: *How does cooling design affect data-center water, noise and permitting?*
- What AI would extract or quote:
  - Summary bullets
  - the March 2026 Gallup figures
  - "White Paper 211 … up to 60% … water use by up to 60%" (with conditions)
  - the trade-off sentence on cooling towers, dry coolers and adiabatic systems
  - the county noise-rule examples
  - the commissioning checklist
- Strongest elements:
  - answer-first summary
  - dated third-party source plus an SE white paper
  - explicit conditions and trade-offs
  - author role stated
  - a reusable heat-path framework
- Weakest elements: the 4-attribute trade-off is in a 5-sentence paragraph rather than a table; no standards cited by number; no expert quote; "Guest Blogger" byline.
- Prompt fit: strong on all 5 fan-outs. This is the closest the set gets to a reference source.

**03 – "AI infrastructure deployment: Demand is easy. Execution is hard."** (Awareness, 45 Average)
- Seed prompt: *What determines successful AI data-center deployment at scale?*
- What AI would extract or quote:
  - the operator typology (fully committed / pragmatists / reactives)
  - "Know the path to power. Know what capacity is secured. Know who will install it."
- Strongest elements: 80% of H2s are question-style; an original typology; first-hand observation ("50 MW a year").
- Weakest elements:
  - the SEO title and meta promise "3 operational priorities — power, capacity, workforce", but the body never enumerates them
  - slogan H1
  - opens with rhetorical questions
  - the only statistic is an unattributed "triple by 2030"
- Prompt fit: the seed is answered only in the last section. Good for "operating model" fan-outs.

**04 – "AI is moving faster than infrastructure. Leaders need a new strategy."** (Awareness, 52 Average)
- Seed prompt: *How should enterprises plan data-center infrastructure for AI?*
- What AI would extract or quote:
  - "10-20 kW … more than 100 kW"
  - "12 to 18 months" to build
  - "liquid cooling removes 80% to 90% of a chip's heat"
  - the three questions for leaders
- Strongest elements:
  - fact-led opening with the thesis within about 70 words
  - fully vendor-neutral
  - practical checklist
  - table of contents
  - the highest view count in the set (9,087)
- Weakest elements: every number is unsourced; thesis-style H1; no question H2s; no summary; the closing CTA names no asset.
- Prompt fit: covers all fan-outs, but without attribution AI engines have no reason to prefer this page over the many similar ones.

**05 – "Using treated and recycled water in Indian data centre cooling"** (Education, 69 Average)
- Seed prompt: *How can Indian data centres use treated/recycled water for cooling?*
- What AI would extract or quote:
  - "India has around 18% of the world's population but only 4% of its freshwater"
  - "recirculate more than 95% of its coolant"
  - the BEE 2023 guidelines
  - the rule for bulk users above 5,000 L/day
  - the 5-step strategy
  - "WUE … does not distinguish between potable and recycled water"
- Strongest elements: summary block; answer-first sections; named, dated policy sources; acronyms defined; neutral, names a competitor example; descriptive CTA.
- Weakest elements: **the 4th summary bullet is truncated ("…thermal architectu")**; the headline statistics are unsourced; no SE data; byline reads "Guest Blogger".
- Prompt fit: strong on all fan-outs.

**06 – "The next decade of AI infrastructure: Why Europe has an opportunity to lead"** (Awareness, 39 Poor)
- Seed prompt: *Opportunities and challenges for AI data-center infrastructure in Europe?*
- What AI would extract or quote: "20 or 30MW … 500MW developments and even gigawatt-scale"; "France and the Nordics" have power available.
- Strongest elements: descriptive H1 that matches the SEO title; first-hand supply-chain view; named next-step guide.
- Weakest elements:
  - personal opening
  - **the "In the AI era, speed wins" heading is merged into body text**
  - no lists
  - "undisputed leader" ambition statement
  - typos ("truly becoming out customers chosen…")
  - no sources
- Prompt fit: touches all fan-outs but gives no quantified European facts. It is a weak citation candidate.

**Cross-page patterns (blogs):**
1. **Two families.** "Insight" posts (02, 05) use the newer house pattern: an "Author:" line, a Summary block, dated sources, descriptive H2s and a descriptive CTA. Executive "perspective" posts (01, 03, 04, 06) open with narrative, use slogan or thesis H1s and carry unsourced numbers. That accounts for 20–35 points between the families.
2. **Evidence is the biggest gap.** U5 is level 1 on 4 of 6 pages. No page cites a standard by number or quotes a second expert. Only 02 cites SE first-party data (WP 211).
3. **Answer-first is weak on executive posts.** U1 is level 1 on 01, 03 and 06. All three would be quoted from their final section, if at all.
4. **Original insight is real but under-packaged.** ART-3 ranges 2–4: there are typologies, field observations and checklists. SE's non-commodity value exists, but it is rarely paired with data or a quotable thesis near the top.
5. **Neutrality is generally good** (U7 at 3–4), except for 06 (2). Product pitches are confined to the closing paragraph, which is the right placement.

### 2.2 News / press releases (se.com newsroom, Jan–Oct 2026)

**Deterministic signals (checker):**

| # | Words | Body H2/H3 | Lists | Quantified facts per 100 words | Fluff per 100 words | Notes |
|---|---|---|---|---|---|---|
| 49 | 1,789 | 0 (only template H2s) | 4 | 0.11 | 0.61 | "seamless" ×5 |
| 50 | 1,039 | 0 | 2 | 0.19 | 0.67 | avg sentence 40 words |
| 51 | 904 | 0 | 3 | 0.66 | **1.22** | "unlock" ×9 (incl. duplicated title) |
| 52 | 1,323 | 0 | 4 | 0.76 | 0.76 | avg sentence 49 words |
| 53 | 1,740 | 0 | 5 | 2.41* | 0.46 | *inflated by repeated "800 VDC" |
| 54 | 1,019 | 0 | 1 | 0.10 | 0.59 | — |

The checker found **no in-body headings on any release**. Its only H2s are template blocks: "Related Spokespeople", "Attached files", "Wiztrust" and "Share this page". The visible subheads ("Availability", "Reference Design Accelerates…") are plain paragraphs in the server HTML.

**Page-by-page audit:**

**49 – Smart Thermostat / Power Mount for Apple Home** (Consideration, 55)
- Seed prompt: *What is the Schneider Home Smart Thermostat for Apple Home; price and availability?*
- What AI would extract or quote:
  - MSRPs ($199.99 / $39.99 / $59.99–$129.99)
  - markets (US/CA; 8 countries for the Power Mount)
  - Matter/Thread, NFC tap-to-pair, works during an internet outage
  - "4 out of 10 U.S. homes"
  - the About block (160,000 employees, 100+ countries)
- Strongest elements: the only release with an About block and entity facts; full availability and pricing; a limitation disclaimer for EnergyKit.
- Weakest elements:
  - "early next year" and "this fall" are never resolved to dates
  - "seamless" used 7 times
  - features packed into a 10-sentence paragraph
  - no HVAC compatibility information
  - "4 out of 10 homes" has no basis
- Prompt fit: strong for price and availability prompts; weak for "will it work with my system".

**50 – "World's first fully Software-Defined MV switchgear"** (Consideration, 58)
- Seed prompt: *What is software-defined MV switchgear and when is it available?*
- What AI would extract or quote:
  - "up to 3× faster ordering and manufacturing, up to 2× faster commissioning"
  - "piloted with Equinix"
  - "Pilot programs continue through 2027 … broader availability … 2028"
  - the ranges named (PremSet, GM/RM/SM AirSeT)
- Strongest elements: quantified deck with a stated basis ("SE studies and estimations"); a named customer pilot plus a customer quote; an explicit roadmap.
- Weakest elements:
  - "world's first" is unscoped
  - the offer is named 4 different ways ("Software-Defined MV switchgear / Software Defined MV Equipment / architecture")
  - no kV or kA ratings and no standards
  - no About block
  - "visit the web or download the white paper" names no destination
- Prompt fit: good for "what/when"; fails engineer prompts about ratings and standards.

**51 – Decarbonization Champion Program with Greenly** (Consideration, 51)
- Seed prompt: *What is the SE Decarbonization Champion Program and what do partners get?*
- What AI would extract or quote:
  - ">34,000 USD (30,000+ EUR) per year per partner"
  - the inclusion list
  - pilot savings (28,500 USD; 178,000 USD)
  - "global carbon accounting and management platform Greenly"
- Strongest elements: program value and pilot results quantified with currency conversion; partner described; basis of savings stated.
- Weakest elements:
  - only one deck bullet
  - no eligibility or how-to-join information
  - "currently being rolled out" with no date
  - attachments dated 23/09 against a release date of 28/09
  - generic quotes that don't name the program
  - fluff 1.22 per 100 words
- Prompt fit: answers "what/value". It can't answer "how do I join", which is the main partner prompt.

**52 – AMD Helios reference design** (Consideration, 59)
- Seed prompt: *What is the Schneider Electric–AMD Helios reference design (density, cooling, PUE)?*
- What AI would extract or quote:
  - "246 kW per rack", "10.4 MW IT", "up to 84% of heat", "PUE as low as ~1.12 at full load", "validated to ANSI standards"
  - "Reference Design 121" by title
- Strongest elements: the best spec list in the set; names the design document; states a scope limit (ANSI now, IEC "in the future").
- Weakest elements: PUE and CDU undefined; IEC timing undated; ETAP and AVEVA undescribed; no About block; "unprecedented / breakthrough" wording.
- Prompt fit: strong for Consideration and Evaluation prompts.

**53 – Arc-flash study on 800 VDC** (Education, 59)
- Seed prompt: *Is arc-flash risk higher in 800 VDC data-center systems?*
- What AI would extract or quote:
  - "arc flash risk in 800 VDC systems can be managed, and in many cases, is comparable to typical AC"
  - "well below the referenced 1.2 cal/cm² PPE threshold"
  - "capacitor discharge dominating the first milliseconds"
  - the white paper title
  - the 5 related resources by title
- Strongest elements: a genuinely informational release with findings in HTML, a method ("conservative methods and assumptions"), a balanced finding (centralized designs show higher energy) and a technical third-party quote.
- Weakest elements:
  - "pioneering", "first-of-its-kind" and "aligning with world's leading hyperscalers" are unscoped
  - the **main finding is not in the headline or deck**
  - "current standards overestimate" without naming the standards
  - date 03/08/2026 is ambiguous (March or August)
- Prompt fit: the best release for informational fan-outs. An AI could answer the seed directly from it.

**54 – Davos / WEF Annual Meeting** (Awareness, 40)
- Seed prompt: *What did Schneider Electric announce at Davos 2026?*
- What AI would extract or quote:
  - "ninth Lighthouse award", Wuhan factory, "one of only three factories … for talent"
  - the products recognized under MINDS
  - EDGE Transition with EDP
- Strongest elements: recognitions from named third-party programs; explicit event dates.
- Weakest elements:
  - abstract headline ("advances energy technology"), no deck
  - four announcements in prose
  - one generic CEO quote
  - two different press e-mails
  - no About block
- Prompt fit: answers "what was announced" only after reading the whole page. Weak for every sub-prompt.

**Cross-page patterns (press releases):**
1. **The deck is the strongest asset.** Releases 50, 51 and 52 put their key number in the deck bullets, which is what an AI quotes. The headline and deck should be treated as the answer layer, as in NEWS-1.
2. **Dates are the weakest.** All six use numeric DD/MM/YYYY. Four leave relative timing unresolved or carry attachment dates that differ from the release date.
3. **Claims outrun substantiation.** Releases 50 and 53 carry several unscoped superlatives between them: "world's first", "pioneering", "first-of-its-kind" and "aligning with world's leading hyperscalers". Performance multipliers usually have a basis, but standards are never cited by number.
4. **Quotes are mostly empty.** Only 53 has a quote with checkable technical content. Third-party voices exist in 5 of 6 releases, which is good.
5. **Entity anchoring is inconsistent.** The About block appears in 1 of 6 releases, and a canonical destination is named in 4 of 6. Partner companies are often undescribed. The offer is named inconsistently in 50.
6. **Structure is template-limited.** No body headings at all, and long multi-claim sentences (averages of 36–49 words in 50–53).

### 2.3 Template-level vs author-level issues

| Level | Blog (blog.se.com) | News (se.com newsroom) |
|---|---|---|
| **Template / CMS (fix once, all pages)** | (T1) "Top picks" related-post titles, often stale or off-topic (2019 posts), and "Add a comment" render as **H2s inside `<article>`**. They pollute section parsing → SE Digital. (T2) The byline and `author` meta read **"Guest Blogger"** while the real author sits in a body line (02, 05). (T3) No visible "Updated" label, although `article:modified_time` differs (all 6 were re-saved 2026-10-02/16). Use it only for substantive updates. (T4) View count and read time are injected ahead of the first sentence. (T5) The Summary and TOC modules are optional; they were used on only 3 of 6 posts. (T6) Empty alt text on most images. (T7) The separate SEO title field allows the H1/title divergence seen in 03, 04 and 06. | (N1) **Numeric DD/MM/YYYY visible date** on all releases, with no `published_time` meta. (N2) **In-body subheads aren't heading elements.** (N3) **No "About Schneider Electric" block in the HTML** for 5 of 6 (it's possibly only in the PDF). (N4) `<title>`/og:title shows the headline duplicated; meta description bullets are concatenated without spaces → SE Digital. (N5) Attached-file dates differ from the release date (51, 52, 54). (N6) "Related Spokespeople" bios (~260 words each) are appended to the body, which dilutes topical focus and repeats across releases. (N7) Wiztrust, share and footer lists sit inside the main content. |
| **Author / editorial (per page)** | Narrative or biographical openings (01, 06). Slogan or thesis H1s (01, 03, 04). Unsourced statistics (01, 03, 04, 06). No standards by number (all). No second-expert quote (all). Promotional ambition lines (06). No CTA (01). Typos (01, 06). Truncated summary (05). Merged heading (06). Title promise not delivered (03). | Abstract headline (54). Unscoped "first/pioneering" (50, 53). Relative timing (49, 51, 52). Quotes without facts (49–52, 54). Standards unnamed (53). Canonical destination unnamed (50, 51). Inconsistent offer naming (50). Main finding missing from headline (53). No eligibility or how-to-join (51). Undefined acronyms (52, 53). |

**Cross-property entity inconsistency (not scored, flag for review).** Blog 01 refers to "AMD Helios 445 racks running at 246 kW", while release 52 describes the Helios rack as "powered by AMD Instinct MI455X GPUs". Use one canonical naming across blog and newsroom.

**Disclosure check (not scored; outside-knowledge note for SE reviewers).** Release 53 presents the ETAP CEO as an external voice. If ETAP is an affiliated company, state the relationship in the text. Undisclosed affiliation weakens the "third-party validation" reading and is a reputational risk. Under judge rule 2 the judge cannot use outside knowledge, so this did not affect the score.

---

## 3. External research and exemplars

**Labels:** [C] controlled · [L] large correlational/observational (usually vendor-run) · [O] official platform · [P] practitioner. All searches used generic terms. Retrieved 2026-10-19.

### 3.1 How AI engines use press releases and newsroom content

| # | Finding | Source (date) | Label | Implication |
|---|---|---|---|---|
| R1 | About 4M citations, 3,600 prompts, 10 industries, ChatGPT plus Google AI Mode, AIO and Gemini. News publications are 14% of citations. Syndicated press releases (Yahoo/MSN) are **0.04%** of all citations; direct newswire citations are **0.21%** (0.37% for informational prompts). **Company-owned newsrooms are 2.98% overall but 18.15% of ChatGPT citations** (about 3% on Google surfaces). Energy is 31% of news citations. | BuzzStream / Citation Labs, data from the week of 27 Jan 2026, updated 8 Apr 2026. https://www.buzzstream.com/blog/news-publications-ai-citations/ · SEJ coverage 16 Mar 2026: https://www.searchenginejournal.com/ai-search-barely-cites-syndicated-news-or-press-releases/569854/ | [L] vendor, 1 week, large brands | The **se.com canonical release** matters, mainly for ChatGPT. Wire syndication is not a direct citation lever. Score the owned release on how quotable it is. |
| R2 | Journalism is about 27% of AI-cited links and earned media about 84% (May 2026, 25M+ links). **More than half of journalism citations are under 12 months old, with a sharp drop after 6 months.** The press-release share is low single digits: it rose about 5× from Jul to Dec 2025, then fell back in May 2026, mainly because ChatGPT cited releases less. GlobeNewswire 61%, PR Newswire 27% and BusinessWire 12% of press-release citations. | Muck Rack *What Is AI Reading?* (Jul 2025; Dec 2025; May 2026). https://muckrack.com/blog/more-stats-from-what-is-ai-reading (updated 17 Nov 2025) · https://aimagazine.com/globenewswire/3198248 · https://www.magazinemanager.com/?p=59107 · https://mediacopilot.ai/claude-cites-journalism-less-muckrack-study/ | [L] vendor | News value decays fast, so absolute dates and recency matter (NEWS-2). Most AI value of a release comes through the earned coverage it seeds. |
| R3 | 8,000+ GlobeNewswire releases (May 2026): 99.3% were cited by ChatGPT or Claude; first citation after an average of 8 h. "Well-structured" releases got 2.6× more citations. Owned content supported by a release was 2× more likely to be cited within 30 days. | Notified (GlobeNewswire owner) via Profound, Jun/Jul 2026. https://finance.yahoo.com/media-advertising/articles/more-99-globenewswire-press-releases-130000200.html | [L] **vendor with direct commercial interest; method unpublished** | Directionally supports structure (NEWS-1, U3) and the canonical bridge (NEWS-6 c3). The magnitudes should not be relied on. |
| R4 | 66% of journalists use PR materials as a story source (1,899 journalists, 19 markets, fieldwork Jan–Feb 2026). They want original research, credible data, expert access and ready-to-use assets. | Cision *2026 State of the Media*, 13 May 2026. https://www.cision.com/about/press-releases/2026-press-releases/pr-emerges-as-the-primary-source-for-journalists-in-high-pressure-newsrooms-302770936/ | [L] survey (vendor) | Releases with substantiated data and substantive quotes earn coverage, and earned coverage dominates AI citations (NEWS-3, NEWS-4). |
| R5 | Google byline-date guidance: show a prominent, **labelled** date ("Published", "Last updated"); keep visible and structured dates consistent; don't use event dates as the publication date; remove confusing extra dates. | Google Search Central, *Byline dates*, page updated 10 Dec 2025. https://developers.google.com/search/docs/appearance/publication-dates | [O] | Supports NEWS-2 c1 (unambiguous labelled date) and the attachment-date consistency in NEWS-2 c4. Applies to blogs (U9) too. |
| R6 | A "Top stories" carousel for developing topics is shown inside AI Overviews (announced May 2026, live in the US by Jul 2026). It surfaces publishers with bylines and dates. | Search Engine Land, Jul 2026. https://searchengineland.com/top-stories-roll-out-in-google-ai-overviews-482615 | [O] via secondary | For news prompts Google surfaces **publishers**, not brand newsrooms, which again points to earned coverage. Out of content scope. |
| R7 | Press-release optimization for AI answer engines is a vendor-led field. No independent, tested template for headline, lede or boilerplate exists. | Everything-PR / ThinkTank commentary, 2025–26 | [P] | NEWS-* criteria transfer the controlled evidence (answer-first, facts, freshness, substantiation, neutrality) to the release format. Label them as inferred. |

### 3.2 How AI engines use blog and thought-leadership content

| # | Finding | Source (date) | Label | Implication |
|---|---|---|---|---|
| B1 | Articles take about 45% of citations for informational queries. ChatGPT is the most article-oriented engine. | KB 04 (Wix study); KB 02 | [L] | Blogs are the right vehicle for Awareness and Education prompts. |
| B2 | About 44% of ChatGPT citations come from the first 30% of a page. Cited titles are more similar to the prompt (0.602 vs 0.484). Cited passages are about 2× more likely to contain a definition. | Ahrefs, 1.4M prompts, 15 Apr 2026 (KB 02) | [L] | U1 at 14 and ART-2 at 7. Narrative openings (01, 06) are the most expensive failure. |
| B3 | "Non-commodity" content is the most influential long-run factor: "don't just recycle what others … already said". First-hand perspectives are sought. | Google Search Central, May 2025 (KB 02) | [O] | ART-3 rises to 10. |
| B4 | Original data is citation-dense, but "most original data never gets cited" unless it is packaged as extractable, quotable findings. Vendor claims of 3.8× uplift are unverified. | Growth Memo, 6 Jul 2026 (paywalled; KB 02) · vendor blogs 2026 | [P]/[L] contested | ART-3 c3 requires first-party data **with conditions or method**. U1 and ART-1 require the finding to sit up top. |
| B5 | Adding statistics, quotes or citations as a *tactic* does not replicate on current models (C-SEO Bench: "add statistics" hurt in 19 of 24 settings). Evidence-backed vs unsupported claims still win pairwise (OR 2–46). | KB 01 (NeurIPS 2025; SIGIR 2026) | [C] | U5 scores substance (named source with year, conditions), never decoration. |
| B6 | Author bylines: vendor studies claim +41–60% for named, credentialed authors. Others find no measurable effect. No peer-reviewed isolation exists. | presenc.ai, authoritytech, Digital Authority Partners (2026) via search | [L]/[P] contested | Expertise is scored only as **visible in content** (U5 c5, ART-3 c1). No separate byline criterion. The "Guest Blogger" byline is flagged as a template issue. |
| B7 | 53% of B2B decision makers say strong thought leadership makes brand recognition matter less (1,934 executives, Mar–Apr 2025). | Edelman–LinkedIn 2025 B2B Thought Leadership Impact Report. https://www.edelman.com/expertise/business-marketing/2025-b2b-thought-leadership-report | [L] survey | The buyer-side reason to invest in ART-3 quality. It is not evidence about AI citation. |
| B8 | Focused pages covering 26–50% of fan-out sub-topics beat exhaustive ones. The sweet spot is 500–2,000 words. | KB 02 | [L] | U6 at 10. The corpus posts (780–1,560 words) sit in range. |

### 3.3 Exemplars from comparable companies (fetched 2026-10-19; structure only, not copied)

| Exemplar | What best-in-class looks like | What it still misses |
|---|---|---|
| **Siemens press release**, 1 Jul 2026 (EUR 300M investment in Germany). https://press.siemens.com/global/en/pressrelease/siemens-invest-eu300-million-germany-build-electrical-backbone-tomorrows-industries | **The headline carries amount, action and place.** Four fact bullets. Dense, specific numbers (investment, jobs by 2030, data-center orders in a named quarter). **Four named quotes including two mayors** (third-party). The About block carries revenue, net income and headcount. The date is written out ("01 July 2026"). Press reference number. | No body subheads. No links to product pages. |
| **ABB "Infinitus" DC portfolio release**, 21 Sep 2026 (via GlobeNewswire). https://www.inderes.se/en/releases/abbs-new-direct-current-portfolio-aims-to-rewire-ai-data-center-energy-infrastructure | **The lede defines the product** (a source-to-rack DC portfolio). Market statistic **attributed to the IEA**; efficiency claim attributed to a named report. Five named building blocks. Dateline with date written out. About block. | Some unsourced figures (1 MW racks, a city-scale analogy). No product-page links. |
| **Vertiv release**, 16 Mar 2026 (Vera Rubin DSX). https://www.vertiv.com/en-in/about/news-and-insights/news-releases/2026/vertiv-brings-converged-physical-infrastructure-to-nvidia-vera-rubin-dsx-ai-factories/ | **Descriptive product anchors** to the canonical product page. One-line subhead deck. Two named quotes (Vertiv plus NVIDIA). About block and forward-looking statements. | Ambiguous numeric date. Product not defined in the lede. No body subheads. |
| **Vertiv educational article**, 9 Jul 2026 ("Cooling Innovation Day 2026"). https://www.vertiv.com/en-us/insights/articles/educational-articles/vertiv-cooling-innovation-day-2026-liquid-cooling-platform-changes-from-design-to-deployment/ | **"Key points in this article" block.** Named product expert with role. Interviewer questions as section heads. **First-party numbers stated with their conditions** (the same CDU rated 800 kW or 2 MW depending on approach-temperature assumptions). Dense links to explainer pages. | Ambiguous numeric date. Question heads are H4 rather than H2. No third-party sources. |
| **Vertiv blog**, 2024 (AI/ML requirements, LATAM). https://www.vertiv.com/en-latam/about/news-and-insights/articles/blog-posts/ai-and-machine-learning-are-redefining-the-technical-and-operational-requirements-of-data-centers/ | Every statistic hyperlinked to its source. Author bio with credentials. Thesis in the first sentence. | One subheading. "Click here" CTA. A two-year-old date with no update. |

**What best-in-class looks like.**

*Press release:*
- headline with action, offer and a number or place
- 2–4 fact bullets
- a lede that defines the offer
- every number sourced or with a stated basis
- a named third-party quote
- the date written out
- an About block with entity facts
- a descriptive link to the canonical product page

*Blog:*
- an answer-first takeaways block
- a named expert with role
- question-shaped sections
- first-party numbers with conditions
- third-party statistics with source and year
- descriptive links to deeper SE assets

No single competitor page does all of this. SE releases 52 and 53 and blogs 02 and 05 already match or beat the exemplars on several elements.

---

## 4. Proposed logic

General rules that apply to both types:
- **Judge protocol.** Binary checks with verbatim quotes, as in judge-protocol.md. When a check isn't met, the evidence is "NOT FOUND" or the offending span.
- **Levels.** Use the calculator's checks-based ceiling, and apply the U-anchors when they are stricter. For U3, c4 and c5 (self-containment and no hidden facts) carry the most weight, as the scoring framework requires.
- **Closing offer paragraph.** U4 c3 (no superlatives) is judged on the informational sections. The closing offer paragraph of a blog or release is judged under U7 c3 instead, so the same sentence isn't penalized twice.

### 4.1 Blog article (revises page-types §6; stays the `article` key)

**What AI extracts:**
- the thesis or answer in the first 30% of the page
- definitions and how-it-works passages
- quantified context (densities, timelines, percentages) with a source
- frameworks and checklists
- named expert perspective
- conditions and trade-offs

It is cited for "why does X matter / how does X work / what's changing in Y". ChatGPT is the most article-oriented engine.

**Must-haves:**
- a takeaways or summary block
- a descriptive, prompt-shaped H1 that is consistent with the SEO title
- the answer in the first 100 words
- every statistic with its source and year
- at least one non-commodity element (field observation, SE data with conditions, original framework)
- a visible date
- a descriptive CTA to a named next-stage SE asset

**Common failures (SE):**
- biographical or narrative openings
- slogan or pun H1s
- unsourced numbers
- no takeaways block
- context-dependent paragraphs
- headings merged into body text
- promotional ambition lines
- a CTA that names no asset
- truncated or untested template modules

| ID | Criterion | W v2 (v1) | Family | Checks (pass = …) | Anchors / notes | Weight rationale |
|---|---|---|---|---|---|---|
| U1 | Insight/answer in paragraph 1 | 14 (14) | answer_def | c1–c5 as in the framework. The Summary block counts as "first 100 words" when it sits directly under the byline. c4 passes if ≥ 80% of H2s open with a direct answer. | Framework anchors | Strong: 44% of citations come from the top third; title–prompt similarity [L] |
| ART-1 | Key-takeaways block: **quality** (was: presence) | 5 (5) | answer_def | c1 a block of 3–5 bullets near the top or bottom · c2 each bullet is a standalone sentence that names its subject · c3 ≥ 1 bullet carries a specific fact, number or concrete recommendation · c4 bullets match the body's claims and are complete (no truncation, no new claims) | Checks-based. 0 if there's no block. | Presence is already U1 c5; this criterion adds fidelity, which caught the truncated bullet in 05. Moderate evidence (summary passages). Weight cut from 6 to 5 to limit double-counting. |
| ART-2 | Title & subheads: descriptive, prompt-aligned, consistent | 7 (6) | other | c1 H1 names the topic in searcher language with no pun, slogan or clickbait · c2 H1, SEO title and meta describe the same topic and angle (one canonical framing) · c3 ≥ 60% of content H2s are descriptive of their section · c4 ≥ 1/3 of H2s are phrased as, or mirror, a buyer question · c5 any explicit promise in the title or meta (e.g. "3 priorities") is delivered as a visible structure | Checks-based | Strong relevance evidence (heading match 41% vs 30%; title similarity) [L]. c2 and c5 added because 03, 04 and 06 diverge. Kept in the stage-neutral "other" family because relevance matters at every stage. |
| U3 | Extractable structure | 8 (10) | other | Framework c1–c5. Template H2s ("Top picks", "Add a comment") are excluded from c1. | c4 and c5 carry the most weight | Formatting has about zero causal effect [C]. The template already supplies most structure. |
| U4 | Factual density & specificity | **10** (8) | specs | Framework c1–c5. c3 is judged on informational sections. | Framework anchors | Strongest content evidence (specs and numbers) [C][L]. Raised in v2 (§5). |
| U5 | Evidence, attribution & expertise | 12 (12) | evidence | Framework c1–c5. c3 (expert quote) passes only for a quote from a named person *other than* the author. c5 passes for a named human author whose role or experience is visible in content ("Guest Blogger" alone fails). | Framework anchors | Evidence-backed claims win (OR 2–46) [C]. Decorative stats don't [C]. |
| ART-3 | Non-commodity insight (now checkable) | **10** (6) | evidence | c1 first-hand observation with a specific detail (number, scale, situation) · c2 an original framework, typology, decision rule or step sequence · c3 SE first-party data or analysis with conditions or method (test, white paper, field data) · c4 a clear, defensible thesis in one quotable sentence that goes beyond consensus · c5 practical, audience-specific implications (what to do, when) | Checks-based. 5 needs c3 plus c1. | Google "non-commodity" [O]. Original data is citation-dense only when packaged [P]. This is SE's main differentiator, and it discriminated 2–4 in the pilot. |
| U6 | Fan-out coverage & focus | 10 (10) | fanout | Framework c1–c4 against the inferred or provided 3–5 fan-outs | Framework anchors | Focused coverage of 26–50% wins [L] |
| U7 | Neutral tone | 7 (7) | tone | Framework. The closing offer paragraph is allowed if it's single and descriptive. | Framework anchors | Promotion hurts (OR up to 362) [C] |
| U8 | Entities & descriptive links | 4 (5) | other | Framework | | Low variance. Links are partly invisible to the judge. |
| U9 | Freshness | **5** (8) | freshness | Framework. c3 is usually N/A. | Level 5 only with a visible "Updated" date plus refreshed statistics. | Strong evidence [C], but the template guarantees the date (all 6 scored 4). Gate G7 protects against undated posts. Cut in v2. |
| U10 | Stage fit & next step | 8 (8) | commercial | Framework. c3/c4 pass when the CTA names a specific SE asset (guide, hub, white paper). | | SE house CTA rule |

**Sum: 100.** No new family IDs except ART-1 joining answer_def.

**Natural stages:** Awareness and Education (Consideration for selection-style posts). Flag Decision unless the post is a how-to or installation article.

**Gates and penalties:** the standard G1–G6 and penalties apply. A new **G7** caps the score at 59 for a dated content type with no visible publication date (it didn't trigger in the pilot). The template's "Top picks" H2s aren't penalized; they are reported as an out-of-scope observation.

**Recommendation templates (most common blog failures):**

| Failed check | Recommendation |
|---|---|
| U1 c1 / ART-1 c1: narrative opening, no summary | Add a 3–5-bullet "Key takeaways" block under the byline, and make sentence 1 the thesis: **"[Topic] matters because [specific fact]; [audience] should [action]."** Move the career story to paragraph 2. |
| ART-2 c1/c2: slogan or pun H1, SEO title diverges | Rewrite the H1 as "[Topic noun phrase]: [angle in plain words]" and align SEO title and meta to the same framing. BEFORE "…boldly go where no data centers have gone before" → AFTER "Why AI data centers need prefabricated, modular power and cooling". |
| ART-2 c5: promise not delivered | If the title says "3 priorities", make 3 H2s named after them, each opening with a one-sentence definition. |
| U5 c1: unsourced statistics | Attribute each number to a named source and year, or to an SE white paper with conditions; delete numbers that can't be sourced ([VERIFY]). |
| U5 c3 / ART-3 c3: no evidence beyond the author | Add one quote from a named SE or customer expert [SME], and one first-party data point with its conditions (white paper or test reference). |
| U3 c2: trade-offs in prose | Turn ≥ 3-attribute comparisons into an HTML table (option × water / energy / noise / footprint). |
| U3 c1: heading merged into text | Restore every section label as an H2 (template or author check before publishing). |
| U7 c3: ambition or "leader" lines | Replace them with what SE actually provides, and state limits ("not every facility needs…"). |
| U10 c3: no CTA, or a vague one | End with one descriptive CTA naming the next-stage asset ("Download the Liquid Cooling System Architecture Guide"). |

**Intake fields (Section B, Article/blog; additions in bold):**
- primary question the article answers
- key insight (1 sentence)
- **author name + role + relevant experience** (for provenance; not "Guest Blogger")
- SME reviewer
- **original data / field evidence available (source, conditions)**
- **statistics list with source and year**
- **thesis sentence**
- publish date and **last substantive update date**
- **next-stage SE asset for the CTA (title + URL)**
- related articles to cross-link
- **syndicated version URL** (e.g. a Forbes version: keep entity facts consistent)

### 4.2 News / press release (new key `news`, prefix NEWS-)

**What AI extracts:**
- who announced what, when and where
- the named offer and its category definition
- headline numbers (performance multipliers, ratings, prices) with their basis
- availability, markets and roadmap
- partner and customer names
- attributed quotes (as attributed claims)
- the company descriptor and size (from the About block)
- findings (for research releases)

ChatGPT cites owned newsrooms most (about 18% of its citations, [L]). Google AI surfaces cite them rarely and prefer publishers. News value decays within months.

**Must-haves:**
- a headline with action, named offer and category
- 2–4 fact bullets
- a lede that defines the offer and who it is for
- an unambiguous written date and dateline
- absolute timing
- every number with a basis
- scoped "first" claims
- ≥ 1 quote with checkable content, plus one third-party voice
- availability and how to obtain
- an About block with entity facts
- the canonical offer page named

**Common failures (SE):**
- numeric dates
- relative timing
- subheads not marked as headings
- missing About block
- unscoped superlatives
- empty quotes
- "visit the web"
- inconsistent offer naming
- the main finding missing from the headline

| ID | Criterion | W v2 (v1) | Family | Checks (pass = …) | Anchors / notes | Weight rationale |
|---|---|---|---|---|---|---|
| NEWS-1 | Headline & summary deck as the answer layer | 12 (12) | answer_def | c1 headline names company + named offer/partner + concrete action (launches / releases / partners), not an abstract verb ("advances") · c2 headline or deck states the single most important specific fact (number, finding, availability, named category) · c3 a deck of 2–4 bullets, **each** a standalone factual sentence naming its subject · c4 (v2) headline uses the category or topic noun phrase a searcher would use ("medium voltage switchgear", "arc flash risk in 800 VDC") | Checks-based | Answer-first and title–prompt match [L]. For releases, the headline plus deck is the inverted pyramid that AI lifts. Replaces U1 (U1 c4 "H2 answers" doesn't fit releases). |
| U2 | Lede context: What / Who / When / Outcome | 12 (12) | answer_def | Framework c1–c4, judged on headline + deck + first paragraph | U2 anchor table | The SE 4-question banner test applied to the lede. Definitions make passages about 2× likelier to be cited [L]. |
| NEWS-2 | Temporal anchoring & dateline | 8 (8) | freshness | c1 visible publication date with the month written out or in ISO format (DD/MM numeric fails) · c2 dateline city · c3 relative time references ("this fall", "early next year", "in the future", "currently being rolled out") resolved to an absolute date or quarter ("today" is resolved by the dateline) · c4 body milestones (availability, pilot end, event dates) stated absolutely **and** consistent with the release date (including attachments) | Checks-based | Recency is the strongest cue (OR 14 to > 10k) [C]. Journalism citations decay after 6 months [L]. Google byline-date guidance [O]. Replaces U9: releases aren't "updated", and their timing must stay interpretable after publication. |
| U4 | Factual density & specificity | **10** (12) | specs | Framework. c2 counts genuine facts only (repeated "800 VDC" doesn't count). | Framework anchors | Concrete facts are the strongest evidence [C]. Trimmed in v2 because c2 never passes for releases. |
| NEWS-3 | Claim substantiation | **12** (10) | evidence | c1 quantified performance or benefit claims state their basis (study, test, pilot, baseline, conditions) · c2 "first / only / leading / pioneering" claims are scoped (category, geography, as-of date) or evidenced · c3 independent validation is named: customer or pilot site, partner test, third-party body, or a standard **by number** · c4 the underlying evidence asset is named by title or ID **and** its key findings appear in the HTML (N/A when no asset exists) | Checks-based | Evidence-backed vs unsupported claims (OR 2–46) [C]. Journalists want credible data [L]. Absorbs U5 c1/c2/c4 for this format. Raised in v2 (§5). |
| NEWS-4 | Substantive attributed quotes | 7 (7) | evidence | c1 ≥ 1 quote with name, title and organization · c2 ≥ 1 quote contains a specific, checkable fact or mechanism (not mission or "excited" language) · c3 a third-party voice (customer, partner, analyst, authority) with name and role · c4 quotes name the offer or topic explicitly (self-contained when lifted) | Checks-based | Quotes are what news answers attribute. Quotation addition is contested as a tactic [C], so only substance is scored (c2). |
| NEWS-5 | Offer facts & availability | 9 (9) | commercial | c1 availability: markets/regions + timing · c2 price, pricing model, or how/where to obtain or join · c3 key specs, capabilities or components listed with units or named elements · c4 maturity explicit (pilot / GA / roadmap / validated to …) | **Applicability:** for research releases c2/c4 are N/A; for corporate, event and financial releases all checks are N/A (criterion dropped). | Price and availability are among the strongest selection cues (OR 6–30+) [C]. The facts a Consideration prompt needs. |
| NEWS-6 | Entity anchoring: About block & canonical bridge | 7 (7) | other | c1 an "About [company]" block in the HTML · c2 entity facts given (size, reach, sector; a one-line slogan alone fails) · c3 the announced offer's canonical destination (product/solution page, white paper, reference design) named by title in text, not "visit the web" or the attached PDF only · c4 partner and third-party entities described at first mention | Checks-based | Entity consistency and a canonical link (SE house: "link by entity to one canonical page") [SE]. Owned content backed by a release is cited more [L vendor]. Replaces U10's next-step role. |
| U3 | Extractable structure | 7 (7) | other | Framework. Template H2s (Spokespeople, Attached files, Wiztrust, Share) are excluded. c1 fails when visible subheads are plain text. | c4 and c5 carry the most weight | Enabler. Structured releases are cited more [L vendor]. Formatting alone has about zero effect [C]. |
| U6 | Fan-out coverage & focus | 6 (6) | fanout | Framework. Roundups of several announcements fail c3. | | Releases mostly answer navigational and news prompts. Fan-out coverage matters most for research and launch releases. |
| U7 | Neutral tone | 6 (6) | tone | Framework. c2 passes on any stated limitation or scope limit. | | Promotion hurts [C]. Releases are inherently promotional, so moderate weight. |
| U8 | Entity clarity & consistency | 4 (4) | other | Framework. One canonical offer name. | G1 hook | Low weight; partly overlaps NEWS-6. |

**Sum: 100.**

**U-criteria not used for news, and why:**
- **U1** → replaced by NEWS-1 + U2 (headline, deck and lede).
- **U5** → split into NEWS-3 (substantiation of the release's own claims, including standards by number) and NEWS-4 (quotes). Provenance is always corporate.
- **U9** → replaced by NEWS-2.
- **U10** → stage fit isn't a goal of a release. The next-step function moves to NEWS-6 c3.

**Buyer-journey stage for news.** A release is primarily an announcement or proof layer. Its default stage comes from its subtype (intake field):

| Release subtype | Default stage | Note |
|---|---|---|
| Product launch / reference design / partnership with an offer | **Consideration** (Evaluation if spec-led, e.g. ratings or validated designs) | 49, 50, 51, 52 |
| Research / study / white-paper release | **Education** | 53 |
| Corporate / event / award / financial | **Awareness** | 54. NEWS-5 is N/A. |

Flag Decision as a mismatch: releases shouldn't be the Decision asset, so route to the PDP or distributor page.

**Gates and penalties:**
- The standard G1–G6 apply, plus **G7** (no visible date → cap 59).
- **G6** covers the case where the announcement facts are only in the attached PDF.
- The fluff-density penalty (> 1.5 per 100 words) applies. 51 came closest at 1.22.
- A cap for unsubstantiated "world's first" claims was considered and rejected. It is already scored in NEWS-3 c2 and U7 c3, and a cap would quadruple-count the defect (see §5).

**Recommendation templates (most common news failures):**

| Failed check | Recommendation | Owner |
|---|---|---|
| NEWS-2 c1: numeric date | Template: render the date as "28 September 2026" (or ISO) with a "Published" label, matching the structured date. | SE Digital (template) |
| NEWS-2 c3/c4: relative timing, mismatched attachment date | Replace "early next year / this fall / in the future" with "Q1 2027 / from 13 November 2026 / [VERIFY quarter]". Regenerate attachments with the release date. | Comms author |
| NEWS-6 c1/c2: no About block | Add the approved "About Schneider Electric" boilerplate as HTML on every release, with entity facts (employees, partners, countries). For joint releases add "About [partner]". | Newsroom template / Comms |
| NEWS-6 c3: "visit the web" | Name and link the canonical destination: "See the [Software-Defined MV switchgear product page] and download the white paper '[exact title]'." | Comms + product marketing |
| NEWS-3 c2: unscoped "first / pioneering" | Scope it ("first … to [criterion], as of [date], according to [basis]") or remove it. Keep it out of the headline unless substantiated. | Comms + Legal |
| NEWS-3 c3: standards unnamed | Name the standards (e.g. "[VERIFY: IEEE 1584 / NFPA 70E edition]") and the validation body or test. | SME |
| NEWS-1 c2: finding missing up top | Put the main finding or number in the headline or first bullet. BEFORE "releases pioneering study assessing arc flash risk…" → AFTER "Study finds arc-flash risk in 800 VDC data centers can be managed to levels comparable with AC [VERIFY wording]". | Comms |
| NEWS-4 c2: empty quotes | Make at least one quote carry a checkable fact or mechanism ("cuts commissioning from X to Y weeks in the Equinix pilot [VERIFY]"). | Comms + spokesperson |
| U3 c1: subheads not headings | Template: render editor subheads as H2. Author: use subheads that answer a question ("When is it available?"). | SE Digital / Comms |
| NEWS-5 c2: no how-to-join or price | Add "Who can join / how to apply / cost" or "Pricing: [model]; contact [named channel]". | Program owner |
| U8 c1: offer named many ways | Choose one canonical name with ™ and use it consistently. Map the synonyms once ("Software-Defined MV switchgear (also: SD MV equipment)"). | Product marketing |

**Intake fields (new Section B row, News / press release):**
- release subtype (launch / reference design / partnership / research / corporate-event / financial / award) → sets the stage
- canonical name of the announced offer + canonical page URL
- key facts with their basis (study / test / pilot / baseline)
- "first/only" claims with scope and substantiation (or none)
- availability: markets + absolute date or quarter
- price or pricing model, or how to obtain or join
- maturity (pilot / GA / roadmap; standards validated against, by number)
- evidence asset (white paper or reference design title / ID)
- spokespeople (name, title, organization) + third-party quote approval
- partners with a one-line descriptor
- boilerplate version
- publication date (with time zone) + dateline city
- attachments regenerated with the same date (Y/N)
- related prior releases or blog posts to link
- wire distribution (Y/N, which wire). Out of scope for the score; used for reporting only.

---

## 5. Pilot scores and calibration

All 12 pages were judged per judge-protocol.md:
- binary checks with verbatim quotes, all **verified as substrings** of the corpus files (whitespace and case normalized; 1 failed quote was corrected before scoring)
- proposed levels, then computed with `geo_score_calc.py --weights <merged>`
- no gates or penalties triggered

Prompts are inferred and listed in each judge JSON. Confidence is "high" overall. Link targets are invisible in the corpus, so U8 c4 and U10 c4 are "medium".

### 5.1 Final pilot scores (v2)

| Page | Type · stage | Score | Band | Top 3 gaps (recoverable points) |
|---|---|---|---|---|
| 02 Cooling design & permitting | Blog · Education | **71** | Good | U1 L3 (+6.3) · U5 L3 (+5.8) · U4 L3 (+3.1) |
| 05 Recycled water, India | Blog · Education | **69** | Average | U5 L2 (+8.7) · ART-3 L3 (+4.9) · U1 L4 (+3.2) |
| 04 AI infrastructure strategy | Blog · Awareness | **52** | Average | U5 L1 (+10.5) · U1 L3 (+7.1) · ART-1 L0 (+6.4) |
| 03 AI deployment execution | Blog · Awareness | **45** | Average | U1 L1 (+14.3) · U5 L1 (+10.5) · ART-1 L0 (+6.4) |
| 06 Europe AI infrastructure | Blog · Awareness | **39** | Poor | U1 L1 (+14.3) · U5 L1 (+10.5) · ART-1 L0 (+6.4) |
| 01 Modular prefab for AI | Blog · Education | **36** | Poor | U1 L1 (+12.6) · U5 L1 (+11.7) · ART-3 L2 (+7.3) |
| 52 AMD Helios reference design | News · Consideration | **59** | Average | NEWS-2 L1 (+6.7) · U4 L2 (+6.3) · NEWS-6 L1 (+5.4) |
| 53 Arc-flash 800 VDC study | News · Education | **59** | Average | NEWS-3 L2 (+8.9) · NEWS-1 L3 (+5.5) · U2 L3 (+5.5) |
| 50 Software-Defined MV switchgear | News · Consideration | **58** | Average | NEWS-3 L2 (+7.6) · NEWS-6 L0 (+6.7) · U4 L3 (+4.2) |
| 49 Apple Home thermostat | News · Consideration | **55** | Average | U2 L2 (+6.9) · NEWS-2 L1 (+6.7) · U4 L2 (+6.3) |
| 51 Greenly decarbonization program | News · Consideration | **51** | Average | NEWS-2 L1 (+6.7) · NEWS-6 L1 (+5.4) · NEWS-3 L3 (+5.1) |
| 54 Davos / WEF | News · Awareness | **40** | Average | NEWS-1 L1 (+12.8) · U2 L2 (+9.6) · NEWS-4 L1 (+6.4) |

**Level matrix (v2 levels):**

*Blog:*

| Criterion | 01 | 02 | 03 | 04 | 05 | 06 |
|---|---|---|---|---|---|---|
| U1 | 1 | 3 | 1 | 3 | 4 | 1 |
| ART-1 | 0 | 4 | 0 | 0 | 3 | 0 |
| ART-2 | 2 | 4 | 2 | 3 | 4 | 3 |
| U3 | 2 | 3 | 3 | 2 | 4 | 1 |
| U4 | 1 | 3 | 2 | 2 | 3 | 1 |
| U5 | 1 | 3 | 1 | 1 | 2 | 1 |
| ART-3 | 2 | 4 | 4 | 3 | 3 | 3 |
| U6 | 3 | 4 | 3 | 4 | 4 | 3 |
| U7 | 3 | 4 | 4 | 4 | 4 | 2 |
| U8 | 2 | 4 | 3 | 3 | 4 | 4 |
| U9 | 4 | 4 | 4 | 4 | 4 | 4 |
| U10 | 2 | 4 | 2 | 2 | 4 | 4 |

*News:*

| Criterion | 49 | 50 | 51 | 52 | 53 | 54 |
|---|---|---|---|---|---|---|
| NEWS-1 | 4 | 4 | 3 | 4 | 3 | 1 |
| U2 | 2 | 4 | 3 | 3 | 3 | 2 |
| NEWS-2 | 1 | 4 | 1 | 1 | 4 | 4 |
| U4 | 2 | 3 | 3 | 2 | 2 | 2 |
| NEWS-3 | 3 | 2 | 3 | 4 | 2 | 3 |
| NEWS-4 | 3 | 3 | 2 | 3 | 4 | 1 |
| NEWS-5 | 4 | 3 | 3 | 3 | 4 | N/A |
| NEWS-6 | 4 | 0 | 1 | 1 | 2 | 1 |
| U3 | 2 | 3 | 3 | 3 | 3 | 2 |
| U6 | 3 | 3 | 3 | 4 | 3 | 2 |
| U7 | 2 | 2 | 2 | 3 | 3 | 2 |
| U8 | 3 | 2 | 3 | 4 | 4 | 3 |

### 5.2 Calibration findings

**Discrimination.**
- **Blog: yes.** There is a 35-point spread. The two checklist-following "insight" posts lead (71/69), the vendor-neutral strategy post is mid-table (52), and the narrative or promotional executive posts trail (36–45). This matches expert intuition.
  - 01 vs 06 (36 vs 39) is the only close call. 01 has better facts but no CTA and a weaker opening; 06 has a named next-step guide.
  - Both are Poor, which is defensible.
- **News: moderate.** The spread is 19 points. The weakest release (54: abstract headline, no deck, empty quote) is clearly last. The four launch and research releases cluster at 55–59, which reflects one shared template and authoring style. The rank order is defensible: the spec-rich reference design and the informational study lead, and the partner program without how-to-join trails.

**Non-discriminating criteria and checks** (kept only where they are a justified standard):

| Item | Behaviour | Decision |
|---|---|---|
| Blog U9 | All 6 at L4. The template guarantees the date. | Kept as a standard (strong evidence; protects against undated or stale posts with G7). **Weight cut from 8 to 5.** |
| U4 c2 (≥ 2 facts per 100 words) | Fails on all 12 pages (max 0.76 genuine). Only 53 passes the script number, and only because "800 VDC" is repeated. | Kept for now, since U4 can't be redefined. **Open question:** set an editorial threshold (e.g. ≥ 1.0 per 100 words) for article and news. With c2 failing everywhere, the effective U4 maximum is 4. |
| NEWS-2 c1 (written-out date) | Fails on all 6 (template). | Kept: a template fix lifts all releases at once (+1 level on NEWS-2). |
| U5 c2 (standards by number) and c3 (second-expert quote) on blogs | Fail on all 6. | Kept as standards. They are the most actionable author-level levers for technical posts. |
| NEWS-6 c1 (About block) | Passes on 1 of 6. | Discriminating today; fixed by process. |

**Counter-intuitive effect found in v1, and the fix (one re-score).** In v1, NEWS-1 c4 ("no unscoped superlative in headline") meant one "pioneering / first" claim was penalized **four times** (NEWS-1 c4, NEWS-3 c2, U4 c3, U7 c3). That pushed the most informative release (53) down to 56, tied with 50 and below 52. In v2:
1. NEWS-1 c4 was redefined as a relevance check (category or topic noun phrase in the headline). Superlatives are now judged only in NEWS-3 c2 (substantiation) and U7 c3 (tone).
2. Weights were rebalanced on the evidence:
   - Blog: U4 8→10, U9 8→5 (stronger content cue up, template-guaranteed cue down).
   - News: U4 12→10, NEWS-3 10→12 (substantiation discriminates; density doesn't).

| Page | v1 | v2 | Δ |
|---|---|---|---|
| 01 | 37 | 36 | −1 |
| 02 | 71 | 71 | 0 |
| 03 | 46 | 45 | −1 |
| 04 | 53 | 52 | −1 |
| 05 | 69 | 69 | 0 |
| 06 | 40 | 39 | −1 |
| 49 | 54 | 55 | +1 |
| 50 | 56 | 58 | +2 |
| 51 | 51 | 51 | 0 |
| 52 | 58 | 59 | +1 |
| 53 | 56 | 59 | +3 |
| 54 | 40 | 40 | 0 |

The blog weight change barely moves scores. That confirms the ranking is driven by levels, not weight choices, which is robust. The news fix removed the double-counting and put 53 level with 52 at the top.

**Effective weights after stage multipliers (v2):**
- **Article.** At Awareness: U1 17.9, U5 13.1, ART-3 10.9, U6 10.9, U7 8.9, …, U10 3.6. At Education: U1 15.8, U5 14.6, ART-3 12.1, U6 11.3.
- **News.** At Consideration: NEWS-3 12.6, NEWS-1 11.5, U2 11.5, U4 10.5, NEWS-2 8.4, NEWS-5 7.7. At Awareness, NEWS-1 and U2 rise to 15.3 each.

None of these effective weights looks counter-intuitive.

**Inflation check.** The blog median is 48.5 and the news median 56.5, both inside the 40–60 gold-set target. No page reaches 90, and one (02) clears 70.

**Next calibration steps:**
1. Have 2–3 human raters (GEO, comms, SME) score the same 12 pages blind. Target κ ≥ 0.6 per criterion. ART-3 c4 ("beyond consensus") and NEWS-4 c2 ("checkable fact") are the most judgement-heavy checks, so add 1–2 exemplars per level.
2. Re-run with 3 judge samples and take the median for pages within ±3 of a band edge (02 at 71, 05 at 69).
3. Expand to ≥ 30 pages per type, including deliberately strong pages (rewrite 01 and 53 per the templates above).

---

## 6. Proposed weights JSON fragment (v2: merge into `assets/weights.json` when approved)

```json
{
  "families": {
    "answer_def": ["U1", "U2", "GLO-1", "ART-1", "NEWS-1"],
    "evidence":   ["U5", "ART-3", "DOC-8", "NEWS-3", "NEWS-4"],
    "freshness":  ["U9", "DOC-7", "NEWS-2"],
    "commercial": ["PDP-8", "U10", "BLK-8", "FAQ-7", "NEWS-5"]
  },
  "page_types": {
    "article": {"U1": 14, "ART-1": 5, "ART-2": 7, "U3": 8, "U4": 10, "U5": 12, "ART-3": 10, "U6": 10, "U7": 7, "U8": 4, "U9": 5, "U10": 8},
    "news":    {"NEWS-1": 12, "U2": 12, "NEWS-2": 8, "U4": 10, "NEWS-3": 12, "NEWS-4": 7, "NEWS-5": 9, "NEWS-6": 7, "U3": 7, "U6": 6, "U7": 6, "U8": 4}
  },
  "gates": {
    "G7": {"cap": 59, "desc": "Dated content type (article/news) with no visible publication date"}
  }
}
```

**Notes:**
- Families not listed above are unchanged. ART-2 and NEWS-6 stay in "other" (multiplier 1.0) on purpose.
- Both page types sum to 100. `geo_score_calc.py --selftest` passes on the merged file (v1 and v2), with no criterion in two families.
- For alias convenience, consider adding `"news": "news", "press release": "news", "news article": "news", "newsroom": "news"` to `TYPE_ALIASES` in the calculator. The `news` key already works without it.
- Add the NEWS-* rows and the revised §6 Article table to `references/page-types.md`, plus a classifier line: "Dated corporate announcement with dateline, spokesperson quotes and media contact → News / press release."

---

## 7. Open questions and risks

1. **Scope of the news score.** Owned newsroom pages are mainly a ChatGPT citation source (about 18% vs about 3% on Google surfaces, one vendor study, one week). Should SE report the news score alongside an **earned-coverage indicator** (pick-up by trade press), which is outside the content score? Recommendation: yes, as a "Beyond this page" note.
2. **U4 c2 threshold for editorial types.** 0 of 12 pages pass the ≥ 2 facts per 100 words threshold. Decide whether article and news use an editorial threshold (≥ 1.0) via a type-level parameter, or accept that U4 is capped at 4.
3. **Template fixes owned by SE Digital** (they lift every page; not scored):
   - newsroom date format
   - subheads as headings
   - About block in HTML
   - attachment dates
   - duplicated `<title>`
   - blog "Top picks" and "Add a comment" H2s inside `<article>`
   - "Guest Blogger" byline
   - a visible "Updated" label used only for substantive updates
4. **Fake-freshness risk.** All six blog posts carry `article:modified_time` values of 2026-10-02 or 2026-10-16, which looks like bulk re-saves. If these are exposed as "Updated" without substantive change, it is a manipulation risk under Google's spam policy. Recommend a policy that the update date changes only with a content change.
5. **Judge limits in this corpus.** Hyperlink targets were stripped during extraction. U8 c4, U10 c4 and NEWS-6 c3 were judged on named destinations in text (medium confidence). Production should pass anchor text plus URL to the judge.
6. **Judgement-heavy checks.**
   - ART-3 c4 (thesis "beyond consensus")
   - NEWS-4 c2 (quote "checkable")
   - U1 c4 (≥ 80% of H2s answer-first)
   - U3 c3 (paragraph length; ≤ 4 sentences rule)

   These need exemplars and inter-rater checks.
7. **Affiliation disclosure in releases.** When an SE-group company or partner is quoted as a third party (e.g. 53), the relationship should be stated. Consider adding NEWS-4 c3 wording: "third-party voice is independent **or** the affiliation is disclosed".
8. **Executive "perspective" posts.** Their purpose is partly brand and leadership visibility. If the business accepts a lower GEO score for some of them, mark them as a separate subtype ("executive perspective") with a lower OK threshold (e.g. 60). Do not lower the standard for technical insight posts.
9. **Cross-property consistency.** The blog and newsroom name the same AMD platform differently (01 vs 52). An SE-wide entity glossary (canonical product and partner names) would make U8 and NEWS-6 checkable across properties.
10. **Evidence quality.** Most press-release citation data is vendor-run, short-window and correlational. One source (R3) comes from a vendor with a direct commercial interest in the result. Re-check at the next quarterly refresh, and validate with a fixed prompt panel (≥ 7 runs per prompt per engine) on rewritten vs control releases.

*Disclaimer: these scores measure the citation-readiness of the content only. Actual AI citation also depends on retrieval, off-site consensus and technical access.*

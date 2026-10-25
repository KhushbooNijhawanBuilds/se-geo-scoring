# GEO Elec Project — review of the Content GEO Scoring work

> **Superseded 20 Oct 2026.** A QA pass corrected 10 findings in this file and added 3. The biggest change is §7.1: judge agreement is weighted κ 0.80, which meets the target. The corrected version is the doc "Content GEO Score — v1 Scoring Logic" (https://claude.ai/code/artifact/cf77ff2f-5b12-4751-8f81-645c9072c7f0), section "QA of the 19 Oct review".

*Reviewed 19 Oct 2026. Covers all 478 files in `GEO Elec Project.zip`, checked against current external research. Before the 21 Oct "1st logic" deadline and the 22 Oct review.*

---

## 1. Bottom line

**Yes. The other chat built a full GEO scoring system for each content type, blogs included.** It is more than a document: it is a working, versioned scoring standard with code, weights, a judge protocol and pilot results on 60 real Schneider pages.

- **25 scoring logics** (type keys) in total.
- **Blog / article logic is at v2.0**, piloted on 6 SE blog posts. Scores were 36–71, and one post reached Good.
- The standard is the **"SE Content GEO Scoring Standard v2.0"** (`weights.json` version `2.0-2026-10-19`).

The system is well grounded and largely sound. It is **not yet ready to be used company-wide**. Three things need to happen first:

1. **Judge reliability.** Two AI judges scored 13 pages. They put **5 of the 13 pages in different bands**, and one judge was stricter on 12 of them. No human calibration has been done.
2. **Coverage gap against the brief.** The Score Agent deck asks for PDP, Range, Category, CaaS, Editorial, Article and Document. **Only Range and Article were piloted on SE pages.** PDP, Category, CaaS, Editorial and Document have logic but were never tested.
3. **A few internal inconsistencies to fix.** Stage-weighting coverage, one gate rule, and some reference docs that disagree with each other (§7).

---

## 2. What is in the zip

| Folder / file | What it is |
|---|---|
| `source-docs/Content GEO Score Agent.pptx` | **The brief.** 8 slides covering inputs, run modes, flow and To-Do. The deadline slide sets 1st logic for Wed 21 Oct and review on Thu 22 Oct. |
| `source-docs/GEO Playbook 1.pdf` | SE house GEO Playbook (Jun 2026): Three Gates, Five-Dimension Content Audit, answer-shaped paragraph, KPIs. **It has no numeric per-type scoring.** |
| `source-docs/GEOI Functional Toolkit…pptx` | SE Toolkit, 14 chapters. Ch. 8 covers blogs. Ch. 13 has the existing **"GEO Strategic Score"**. About 45% of that score is technical (AI interpretability 30%, schema 15%) and 10% is an outcome measure. Bands are <40 / 40–69 / 70–89 / 90+. |
| `schneider_electric_url_inventory.xlsx` | 60 SE URLs: 10 page types × 6. This is the gold-set sample. |
| `research/00–05*.md` | Evidence base: internal synthesis, ~57 academic papers, ~80 industry/platform sources, GitHub/Reddit tools, content-type playbooks, master knowledge base. About 280 KB in total. |
| `research/type-analysis/*.md` | **Per-type logic design**, one file per pair of types, each with an audit of 6 SE pages, competitor exemplars, the proposed logic, pilot scores and open questions. |
| `research/type-analysis/pilot/` | Judge JSONs and score cards from the type-design pilot, plus sensitivity runs. |
| `research/corpus/` + `rendered/` | The 60 pages captured twice: server HTML (what non-JS AI crawlers see) and the rendered page. |
| `research/final-scoring/` | **Final v2.0 scoring of all 60 pages.** Judge A covered every page; blind Judge B covered 13. `consolidate.py` is included, but its output (agreement report and scored-inventory xlsx) is **not** in the zip, so it was apparently never run. |
| `skill/geo-research/` | **The operational Claude skill**: `SKILL.md`, 12 reference files, a deterministic score calculator, a content checker and `weights.json`. The calculator selftest passes. |
| `GEO Content Engine…pptx/pdf`, `Khushboo_Electrifier_Intro.pptx`, `Electrifier_…Contribution_Log.xlsx` | The related Electrifier / Distributor IQ content-engine proposal and your project log. These are context only and contain no scoring logic. |

---

## 3. How the score works

**The score measures citation-readiness.** It estimates how easily an AI engine can understand, trust, extract and quote the content. It cannot promise citations, because retrieval, off-site consensus and technical access also decide those. Technical GEO is out of scope, as the deck requires. Content decisions that hide facts are in scope: facts that exist only in an image, PDF, collapsed tab or gated form.

**Formula**
```
level 0–5 per criterion (from binary checks with verbatim quotes)
effective weight = type weight × stage multiplier, renormalized to 100
raw = Σ level/5 × effective weight
final = raw − penalties (max −10), then gate caps (lowest wins)
Bands: <40 Poor · 40–69 Average · 70–89 Good · 90+ Excellent · "OK" threshold 70
```

**Building blocks**
- **10 universal criteria (U1–U10):**
  - U1 Answer-first & prompt alignment
  - U2 What/Who/When/Outcome
  - U3 Extractable structure & self-containment
  - U4 Factual density
  - U5 Evidence & expertise
  - U6 Fan-out coverage
  - U7 Neutral tone
  - U8 Entity consistency
  - U9 Freshness
  - U10 Stage fit & next step
- **Type-specific criteria:** PDP-, RNG-, CAT-, BLK-, ART-, DOC-, CS-, CMP-, FAQ-, GLO-, SOL-, VID-, NEWS-, SVC-, SW-, CALC-, WP- and ESG-. Each has 3–6 binary checks.
- **Gates G1–G13** cap the score so that averaging can't hide a deal-breaker. Examples:
  - contradiction → max 59
  - question never answered → max 39
  - article/news with no date → max 59
  - case study with no quantified outcome → max 59
- **Penalties:**

  | Penalty | Points |
  |---|---|
  | Keyword stuffing | −3 |
  | Fluff | −2 |
  | Boilerplate | −2 |
  | CTA overload | −1 |
  | Self-ranking | −3 |
  | Template placeholder | −2 |
  | Superseded edition with no notice | −3 |
  | Hidden LLM instructions | −10 |
- **5 buyer-journey stages** (Awareness, Education, Consideration, Evaluation, Decision), each with written definitions and stage multipliers for each criterion family. Example: at Awareness, answer and tone criteria count ×1.4; at Decision, commercial criteria count ×1.5.
- **Judge protocol.** The LLM answers pass/fail per check with a verbatim quote, and missing evidence counts as a fail. **Code, not the LLM, computes the final score.** Code also takes the lower of the judge's proposed level and the level the checks support. Every quote is substring-verified.
- **v2.0 rules:**
  - Score the **rendered** page.
  - Report the "crawler gap" (server text ÷ rendered text < 0.7) separately and route it to SE Digital.
  - Tag every failed check [T] (template) or [A] (author).
  - White papers and ESG reports get two scores, **Gateway** and **Document**, which are never averaged.

This design matches current research. A Sept 2026 audit of ChatGPT, Copilot, Google and Perplexity found that **96.4% of cited URLs appeared in only one engine**. It also found **67% day-to-day URL turnover**, and concluded that engine-free scores measure "page fit", not final visibility ([arXiv 2609.22655](https://arxiv.org/abs/2609.22655)). The project already frames its score exactly this way.

---

## 4. Every content type that has scoring logic

| # | Type key | Version | Piloted on SE pages? | Top-weighted criteria | Type gate |
|---|---|---|---|---|---|
| 1 | **article** (blog) | v2.0 | **Yes, 6** | U1 14, U5 12, U4 10, ART-3 10, U6 10 | G7 (no date) |
| 2 | **news** (press release) | v2.0 new | Yes, 6 | NEWS-1 12, U2 12, NEWS-3 12, U4 10 | G7 |
| 3 | **solution** | v1.1 | Yes, 6 | SOL-2 13, SOL-4 11, SOL-5 10, SOL-7 10 | — |
| 4 | **service** / **service_project** | v1.0 new | Yes, 6 | SVC-1 13/15, SVC-2 12/8, SVC-6 10 | G12 |
| 5 | **range** | v1.1 | Yes, 6 | RNG-2 12, RNG-9 11, RNG-1 10, U1 10 | G10 |
| 6 | **software_product / hub / trial** | v1.0 new | Yes, 5 | SW-5 (trial 26), SW-7 (hub 16), SW-1 12 | G11 |
| 7 | **case_study** | v1.1 | Yes, 6 | CS-3 20, CS-1 14 | G8 |
| 8 | **calculator** (TradeOff Tool) | v1.0 new | Yes, 6 | CALC-1 16, CALC-3 15, CALC-2 13 | G9 |
| 9 | **whitepaper_gateway** + **whitepaper_doc** | v1.0 new | Yes, 6 | WP-2 14, U1 12, WP-1 10, DOC-8 10 | G6 |
| 10 | **esg_hub / esg_report / esg_report_doc** | v1.0 new | Yes, 6 + 2 PDFs | ESG-1 20–22, ESG-2 12–14 | G6 |
| 11 | **pdp** | v1.0 | **No** | PDP-1 specs 16, U1 10 | G3 |
| 12 | **category** | v1.0 | **No** | CAT-1 how-to-choose 16, CAT-2 14 | — |
| 13 | **caas** (reusable block) | v1.0 | **No** | BLK-1 self-containment 22, BLK-3 18, BLK-4 15 | — |
| 14 | **editorial** (common logic) | v1.0 | **No** | U1 16, U5 12, U6 12 | — |
| 15 | **document** / **datasheet** | v1.0 | **No** | DOC-1 HTML gateway 18, DOC-3 12/16 | G3 (datasheet) |
| 16 | **comparison** / selection guide | v1.0 | **No** | CMP-1 neutral table 20, CMP-2 16 | self-ranking penalty |
| 17 | **faq** | v1.0 | **No** | FAQ-2 direct answer 22 | — |
| 18 | **glossary** | v1.0 | **No** | GLO-1 definition 28 | — |
| 19 | **video** | v1.0 | **No** | VID-3 description 16, VID-5 transcript 14 | — |
| + | Image module | rules only | No | Scored inside U3 / PDP-9 / BLK | — |

Counting variants, that is 25 weight sets, and each one sums to 100 (verified).

---

## 5. The blog scoring in detail (`article`, v2.0)

**What AI takes from a blog:**
- the thesis in the first 30% of the page
- definitions
- how-it-works passages
- quantified context with a source
- frameworks and checklists
- named expert view
- trade-offs

Engines cite blogs for "why does X matter", "how does X work" and "what's changing in Y".

| ID | Criterion | Weight | Pass conditions, condensed |
|---|---|---|---|
| U1 | Insight/answer in paragraph 1 | 14 | Answer in the first 100 words (a Summary block under the byline counts). H1 matches the prompt. Key message at the top. ≥ 80% of H2s open with a direct answer. Takeaways present. |
| ART-1 | Key-takeaways block (quality) | 5 | 3–5 bullets. Each bullet stands alone and names its subject. ≥ 1 bullet carries a fact. Bullets match the body, with nothing truncated. |
| ART-2 | Title & subheads | 7 | No pun or slogan H1. H1, SEO title and meta agree. ≥ 60% of H2s are descriptive. ≥ 1/3 of H2s are question-shaped. Any title promise ("3 priorities") is delivered. |
| U3 | Extractable structure | 8 | Descriptive H2s, lists and tables, short paragraphs, self-contained sections. No key fact only in an image or PDF. |
| U4 | Factual density | 10 | Quantified claims. ≥ 1.0 genuine facts per 100 words. No unanchored superlatives. Precise terms. |
| U5 | Evidence & expertise | 12 | Stats with source and year. Standards by number. Quote from a named person *other than the author*. First-party data with method. A named human author with role ("Guest Blogger" fails). |
| ART-3 | Non-commodity insight | 10 | First-hand detail, an original framework, SE data with conditions, a quotable thesis, practical implications. Level 5 needs SE data plus first-hand detail. |
| U6 | Fan-out coverage & focus | 10 | Seed prompt answered, plus 3–5 sub-questions. One intent. |
| U7 | Neutral tone | 7 | Advisor voice, trade-offs, no hype. One descriptive closing offer is allowed. |
| U8 | Entities & links | 4 | Canonical names, IDs, no contradictions, descriptive anchors. |
| U9 | Freshness | 5 | Visible date, current facts. Level 5 needs a visible "Updated" date plus refreshed stats. |
| U10 | Stage fit & next step | 8 | The CTA names a specific SE asset. |

**Pilot results (final v2.0, Judge A / blind Judge B):**

| Post | Stage | A | B | Biggest gaps |
|---|---|---|---|---|
| 02 Cooling design & permitting | Education | **71 Good** | 65 | U1, U5, U4 |
| 05 Recycled water, India | Education | 69 | 59 | U5; truncated summary bullet; unsourced headline stat |
| 04 AI infrastructure strategy | Awareness | 53 | **29** | Every number unsourced; no takeaways |
| 03 AI deployment execution | Awareness | 47 | 36 | Title promises "3 priorities" but they are never delivered |
| 06 Europe AI infrastructure | Awareness | 39 | 34 | Personal opening, no sources, "undisputed leader" |
| 01 Modular prefab DCs | Education | 37 | 29 | Biography opening, Star Trek pun H1, no CTA |

**What it found across SE blogs:**
- Technical "insight" posts that follow the SE checklist (summary block, dated sources) score 20–35 points above executive "perspective" posts.
- **U5 evidence is the biggest gap:** no post cites a standard by number or quotes a second expert.
- Template fixes for SE Digital:
  - "Top picks" and "Add a comment" render as H2s inside the article
  - the "Guest Blogger" byline
  - no visible "Updated" label
- **Fake-freshness risk:** all 6 posts show bulk `modified_time` re-saves. Don't expose an "Updated" date unless the content actually changed.

---

## 6. Results across all 60 pages (Judge A, v2.0, rendered content)

| Page type | n | Min | Median | Max |
|---|---|---|---|---|
| Blog | 6 | 37 | 50 | 71 |
| News | 6 | 38 | 56.5 | 59 |
| Customer story | 6 | 33 | 50.5 | 62 |
| Calculator | 6 | 16 | 51 | 66 |
| Service | 6 | 19 | 43 | 52 |
| White paper (gateway) | 6 | 30 | 35.5 | 45 |
| Solution | 6 | 19 | 33 | 45 |
| Range | 6 | 12 | 27.5 | 37 |
| Software | 5 | 22 | 27 | 33 |
| ESG (gateways) | 6 | 2 | 16 | 20 |
| ESG PDFs (document module) | 2 | 68 | 69 | 70 |

**Only one HTML page reaches 70: blog 02, scored 71 by Judge A** (Judge B: 65). One of the two ESG PDFs also scores 70, but only on its document module (§5.2). The analyses show that most of the shortfall is **template-level, not author-level**. Examples:
- Calculator method lives in an iframe.
- Case-study stories are client-rendered.
- Range pages have no comparison table or date.
- ESG gateways show zero KPIs in HTML.

What-if simulations show single template changes lifting pages from about 33 to about 71–80.

---

## 7. Expert review: issues found, most serious first

### 7.1 Judge reliability is not yet proven (blocker for global use)
- Over the 13 double-scored pages, the mean gap between judges is **7.8 points**. **5 of 13 pages land in different bands:** blog 02 Good vs Average, and blogs 03/04 Average vs Poor.
- **Judge A scored higher on 12 of 13 pages.** That is a systematic leniency gap, not random noise.
- The least stable criteria are **U7 tone** (exact agreement on 5 of 13 pages), **U2** and **U8**. On blog 04, U1 was level 3 from one judge and 0 from the other.
- 47 of the 60 pages had only one judge. `consolidate.py` (κ statistics) was never run, and **no human raters have scored anything** (the protocol targets κ ≥ 0.6).
- **Fix:**
  - Run `consolidate.py`.
  - Get 2–3 human raters (GEO, comms, SME) to score the 13 pages blind.
  - Add 1–2 worked exemplars per level for U7, U2, U1 c1, ART-3 c4 and NEWS-4 c2.
  - Use a 3-run median within ±3 of a band edge (the protocol already specifies this; enforce it in code).

### 7.2 The deck's own To-Do list is only partly piloted
The deck asks for PDP, Page range, Page category, CaaS, Editorial, Article and Document. The 60-URL inventory used a *different* 10 types. As a result, **PDP, Category, CaaS, Editorial and Document/Datasheet have v1.0 logic but no SE-page pilot.** The same applies to Comparison, FAQ, Glossary and Video. PDP and CaaS are the highest-volume types for a global rollout.
- **Fix:** ask Basak, Ayoub and Shaurya for 5–6 examples each of PDP, Category, CaaS block and Datasheet, and pilot them the same way.

### 7.3 Stage multipliers skip 48 criteria
Stage multipliers apply by "family". **48 criteria belong to no family**, so they always count ×1.0. Some of this is deliberate (ART-2 and NEWS-6 are documented as stage-neutral), but several gaps look accidental:
- **SOL-4, SVC-6** (quantified outcomes) are not in *proof*, although SOL-5, SVC-7 and CS-3 are.
- **CS-2, CS-4, CS-6** are not mapped, while CS-3, CS-5 and CS-7 are in *proof*.
- **DOC-1** (HTML gateway), all **FAQ-***, **VID-*** and **GLO-3/4**, and **U3/U8** are unmapped. So for FAQ and video pages the declared stage barely changes the score.
- **Fix:** decide family membership for every ID explicitly, and add a selftest that fails on any unmapped ID that isn't on a "stage-neutral" list.

### 7.4 Gate G1 zeroes the wrong document criterion
G1 (factual contradiction) sets `U8`, `BLK-4` and `DOC-6` to 0. DOC-6 is **"Customer language"**, not consistency, so this looks like an ID mix-up. It affects documents and datasheets only.
- **Fix:** remove DOC-6 from the list. Contradictions are already handled by U8, which those types include.

### 7.5 Reference docs disagree with each other
- `buyer-journey.md` still shows the v1 multiplier table (fewer families).
- `intake-sheets.md` (To-Do 03) has **no sections for news, service, software, calculator, white paper or ESG**. The blog/news analysis proposes richer blog intake fields that were never merged.
- `weights.json` says it "mirrors page-types.md", but it actually mirrors page-types-v2.
- The type-analysis files report **server-HTML** scores that differ from the final **rendered** scores. Case studies are 9–54 there vs 33–62 final; calculators are 11–17 vs 16–66. The white-paper/ESG file still says "scoring uses server HTML". Gate IDs in those files (G7/G8/G-SVC) were renumbered in the v2 registry.
- **Fix:** treat `page-types-v2.md` + `weights.json` + `final-scoring/` as the source of truth, and add a banner to the type-analysis files saying their numbers are pre-v2.

### 7.6 Anchor rules are not all enforced in code
The calculator's ceiling is the share of checks passed, plus the judge's proposed level. Rules such as "U3 ≤ 2 if key facts are hidden", "SOL-1 c3 fail → ≤ 3" and "SOL-5 c2 fail → ≤ 2" depend on the judge remembering them. Python's banker's rounding also makes exactly-half cases round down (2 of 4 checks → level 2, as does 3 of 6).
- **Fix:** encode the per-criterion caps in `weights.json` and apply them in code. Document the rounding.

### 7.7 Upper range untested; threshold of 70 may be unreachable
Only one HTML page reaches 70 (blog 02, from one judge; §6), and only 2 of 60 pages were scored Good. The 70–100 range has never been calibrated, so it is unknown whether "Good" pages really look good to experts.
- **Fix:** add rewritten SE pages and 2–3 competitor pages per type to the gold set. Consider per-type thresholds (the white-paper analysis suggests 60 for gateways until the template ships).

### 7.8 Evidence attribution to verify before global publication
- The "~44% of ChatGPT citations come from the first 30% of a page" figure is credited to Ahrefs (1.4M prompts) in the project. Public secondary sources credit it to **Kevin Indig / Growth Memo (Feb 2026)**, and I could not confirm the Ahrefs attribution. Check the primary source before this goes into company material.
- Many industry numbers are vendor-run (BuzzStream, Notified/GlobeNewswire, Profound). The project already labels them [L] or vendor. Keep that labelling in anything shared.
- The core claims hold up: C-SEO Bench (NeurIPS 2025) confirms that most "conversational SEO" rewrites are ineffective or harmful ([arXiv 2506.11097](https://arxiv.org/html/2506.11097v3)). Google's May 2026 guide confirms that AI features run on core ranking, and that non-commodity content matters most ([Google blog](https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing)).

### 7.9 Make target prompts mandatory, not optional
The deck lists target AI prompts as *optional*. Recent work finds generic page scores weakly predictive, and query-conditioned relevance much more informative ([arXiv 2609.23162](https://arxiv.org/pdf/2609.23162)). U1, U6 and ART-2 all depend on the prompt.
- **Fix:** make at least one target prompt mandatory, or pull prompts from Profound. Show "prompts inferred" prominently and lower confidence when they are.

### 7.10 Naming clash with the existing Toolkit score
The Toolkit's "GEO Strategic Score" uses the same bands but is about 45% technical. The new score excludes technical factors entirely.
- **Fix:** always call the new one the **"Content GEO Score"** and say in the report header that it is not comparable with the Strategic Score.

### Smaller items
- The checker improvements already listed in the type analyses were not applied:
  - footer and "Need help?" text counted in word and fluff counts
  - plain-text CTA labels not detected
  - unresolved footnote markers not flagged
  - HTML comments not stripped
- Link targets were stripped from the corpus, so U8 c4 and U10 c4 are medium confidence. Production should pass the anchor text and URL to the judge.
- Two open policy questions block several criteria and need Legal / BU answers: can SE publish SLAs, pricing models and security certifications (SVC-2, SVC-5, SW-4, SW-5)?
- `scoring-framework.md` §4 still lists only G1–G6. It says v2 takes precedence, but merge the full registry into it.

---

## 8. What is strong (keep it)
- **Evidence-graded design.** Each weight has a rationale and an evidence label (C/L/O/P). Myths are handled explicitly: llms.txt, schema as a lever, "add statistics", bylines.
- **Auditable judging.** Binary checks with verbatim, substring-verified quotes, and code doing the arithmetic. That makes every score defensible to a content owner.
- **Gates plus template/author tagging.** These turn a score into a routing plan for SE Digital, PIM, content owners and SMEs. That matters most for a global rollout.
- **Realistic calibration.** The median un-optimized page lands at 35–60, and 90+ never occurs, so the judge isn't inflating scores. The one double-counting bug found (superlatives counted four times in news) was fixed and re-scored.
- **It fits the deck's flow exactly:** score only, recommendations only, or both; the 70 threshold; the "more recommendations?" loop; bulk mode of up to 10; tech out of scope.

---

## 9. Suggested plan for 21–22 Oct

1. **For the 21 Oct "1st logic" deliverable, present Blog/Article v2.0.** It is the most mature and was double-judged. Bring the logic table (§5), the pilot table, and 2 worked score cards (02 and 01).
2. Before then, **fix 7.3, 7.4 and 7.5** (an hour of edits) and run `consolidate.py`, so the review sees agreement statistics.
3. At the review, **ask for decisions** on:
   - human raters for κ
   - PDP / Category / CaaS / Datasheet examples
   - per-type thresholds
   - mandatory target prompts
   - the 6th "Verification" stage for ESG
   - the SLA / pricing disclosure policy
4. Then pilot the untested v1 types in priority order: PDP → CaaS → Category → Document/Datasheet.
5. Build the intake sheet for each v2 type (To-Do 03), starting with the blog fields already drafted in `blog-and-news.md` §4.1.

*Method note: I read every reference, analysis and research file, the decks (text extracted) and the spreadsheets. I extracted the Playbook PDF as text because it couldn't be rendered; its content matches the synthesis in `00`. I ran the calculator selftest, recomputed every score table from the judge outputs, and checked the key claims against external sources online. Nothing in the original files was changed. The unzipped copy is in the session scratchpad.*

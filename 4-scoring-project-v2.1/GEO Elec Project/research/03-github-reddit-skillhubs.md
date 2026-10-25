# 03 — Open-Source (GitHub), Community (Reddit / HN) and Claude Skill Hubs: GEO / AEO / LLM SEO

*Research date: 2026-10-13. Scope: open-source GEO repos and their scoring rubrics, Claude/agent skills for GEO, and practitioner community insight. No code was downloaded or executed. All rubrics below come from reading README, SKILL.md, docs and script source through raw.githubusercontent.com / the GitHub API.*

> **Method note on Reddit:** reddit.com is blocked to this research agent's fetcher and search tool. Reddit evidence below comes from secondary sources: GummySearch subreddit snapshots, vendor and press write-ups of Reddit experiments, and SEO newsletters quoting threads. Hacker News was read directly through the Algolia HN API. Treat the Reddit section as **community sentiment reported second-hand**, not primary quotes.

---

## 1. Executive summary

1. **The open-source GEO ecosystem has consolidated around a few Claude Code skill packs.** As of Oct 2026 the largest are:
   - `AgriciDaniel/claude-seo`: ~18.8k stars, 26 sub-skills, 19 agents.
   - `zubair-trabzada/geo-seo-claude`: ~11.0k stars, GEO-first, the most explicit published weights.
   - `coreyhaines31/marketingskills`: ~54.5k stars. Its `ai-seo` skill is the best-sourced methodology but has no numeric score.

   Smaller but rubric-rich projects: `aaron-he-zhu` CORE-EEAT (80-item benchmark with content-type weights), `onvoyage-ai/gtm-engineer-skills` (`audit-website-aeo`: 16 deterministic checks plus 6 LLM-judged dimensions), `Auriti-Labs/geo-optimizer-skill` (9-category, 100-point site rubric), `IJONIS/geo-lint` (97 deterministic lint rules, 36 of them GEO), and `houtini-ai/geo-analyzer` (claim density and front-loading; now deprecated).
2. **Every rubric converges on the same five content levers:**
   - **Answer-first extractability:** a direct answer or definition in the first 40–60 words, self-contained passages, question-style headings.
   - **Evidence density:** statistics, named sources, quotations, dates.
   - **Structure:** heading hierarchy, lists, tables.
   - **Authority/E-E-A-T:** author, credentials, entity/sameAs.
   - **Freshness.**

   Off-page "presence" (Wikipedia, Reddit, YouTube, review sites, LinkedIn) is a separate site-level pillar.
3. **The weights are opinion, not evidence.** geo-seo-claude says so explicitly. The peer-reviewed evidence base is small:
   - **Princeton GEO (KDD'24):** quotations +43%, statistics +33%, fluency +29%, citing sources +28%, keyword stuffing −9% in position-adjusted word count. Lower-ranked sources gain the most (+115% at rank 5 for Cite Sources).
   - **AutoGEO (ICLR'26):** learned rules are attribution, comprehensive coverage, accuracy, neutral non-promotional tone, logical structure, clear language, and up-to-date content.
   - **E-GEO (e-commerce):** naive heuristics mostly don't work. Optimized rewrites converge on user intent, competitive differentiation, and external evidence such as reviews.
   - **C-SEO Bench (NeurIPS'25):** most "conversational SEO" rewrites are ineffective or harmful. Classic SEO (being retrieved and ranked into the LLM context) matters more, and gains shrink as more players adopt the same tricks.
4. **Practitioner consensus in 2026, from HN, Reddit-derived write-ups and practitioner newsletters:**
   - Rankings and retrieval are still the floor ("GEO is mostly SEO plus extractability plus off-site consensus").
   - **llms.txt does not move citations.** Ahrefs found 97% of 137K files never requested. Google ignores it. Its only clear value is for developer docs.
   - **Schema alone does not lift citations.** Ahrefs' 1,885-page controlled test found no significant uplift. It is still useful for entities and shopping feeds.
   - **Self-promotional listicles get cited but don't get you recommended.** In Lily Ray's sample, 69% of such citations recommended competitors. ChatGPT 5.6 (Aug 2026) halved listicle citation share.
   - **Reddit seeding is volatile and risky.** Otterly's bot-assisted subreddits were banned under Reddit Rule 2. Reddit's ChatGPT citation share fell about 86–89% around 8–14 Aug 2026.
   - **Google's May 2026 spam-policy update** explicitly covers manipulation of AI responses.
5. **Measurement:** AI answers are non-deterministic. Run each prompt 3–5 times, report rates with sample size, and track the ladder retrieved → cited → mentioned → recommended. Expect AI influence to be under-attributed: about 9% of post-recommendation visits show as AI referrals, and Visibility Labs estimates 70% of AI referrals are invisible in GA4.
6. **What this means for our own GEO skill:**
   - Make the content-level score deterministic where possible, using a citability-block scorer like geo-seo-claude's or lint rules like geo-lint.
   - Make the rest LLM-judged with "rationale before score", as gtm-engineer-skills does.
   - Weight by content type, as CORE-EEAT does. B2B and electrical PDPs, datasheets and how-tos need different weights.
   - Include veto items for trust/consistency, and anti-signals (promotional tone, CTA overload).
   - Keep llms.txt and schema as hygiene with low weight.
   - Separate page-level "citability" from site-level "authority/presence".

---

## 2. GitHub repo catalogue

### 2.1 Summary table

Stars come from the GitHub API where marked †. Other counts come from the deeflect/awesome-geo snapshot and may be stale.

| Repo | Type | Stars / recency | What it does | Scoring rubric? | Reusable for us |
|---|---|---|---|---|---|
| [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | Claude Code plugin (26 sub-skills, 19 agents) | 18.8k† / pushed 2026-10-04 | Full SEO suite incl. `seo-geo`, `seo agentic`, E-E-A-T, schema, CWV, DataForSEO and other MCP extensions | `seo-geo`: 5 weighted dimensions (below). Others qualitative or letter grades | "Google-first, flag conflicts" stance; crawler matrix split by training, search and user fetch; llms.txt evidence file; stats with source and date |
| [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) | Claude Code skill (14 sub-skills, 5 agents, Python scripts) | 11.0k† / pushed 2026-10-13 | `/geo audit`, citability, crawlers, llms.txt, brand mentions, schema, PDF report, prospect CRM | **Most detailed published weights** plus a deterministic `citability_scorer.py` | Block-level citability algorithm; composite weights; schema point table; crawler deductions |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (`skills/ai-seo`) | Skill library (marketing) | 54.5k† / pushed 2026-10-13 | `ai-seo` skill v2.7.6 with 10 reference files (format volatility, citations vs recommendations, platform factors, LinkedIn/YouTube citations, OKF, agent readiness) | 10-item pass/fail extractability checklist; no numeric score | Best-sourced, most up-to-date methodology. Visibility ladder and measurement rigor |
| [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) → [core-eeat-content-benchmark](https://github.com/aaron-he-zhu/core-eeat-content-benchmark) | Skill pack plus benchmark | 220† (signpost repo) / 2026-09 | 16 SEO/GEO skills, now in the `aaron-marketing-skills` bundle; CORE-EEAT 80-item content benchmark; CITE domain rating | **80 items × 8 dimensions, pass/partial/fail, veto items, 9 content-type weight tables** | Item taxonomy; content-type weights; veto concept; GEO vs SEO split |
| [onvoyage-ai/gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills) (`audit-website-aeo`) | Codex/Claude skills (12) plus Node crawler | ~909 / 2026 | Brand research → keywords → Reddit opps → content plan → write → audit → fix | **16 deterministic checks (142 pts) + 6 LLM dimensions (0–5), 50/50, A+–F** | Hybrid deterministic plus LLM-judged design; "rationale before score"; foundational score can't be adjusted by the LLM |
| [Auriti-Labs/geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill) | CLI, Python lib, MCP, GitHub Action | ~430 / 2026 | Site GEO audit 0–100, fix-file generation, `geo citations` checker | **v2 rubric: 9 categories, per-check points**; negative signals −5; separate 47-check citability score | Point table per check; negative-signal concept; informational (unscored) checks |
| [IJONIS/geo-lint](https://github.com/IJONIS/geo-lint) | Node linter plus Claude Code skill | Show HN Mar 2026 | 97 deterministic rules (36 GEO) for Markdown/MDX; agent fix loop until `[]` | Rule-based warnings (e.g., weak lead sentence, low citation density, missing table, too few question headings) | "Lint and auto-fix loop" pattern; restructure, don't rewrite voice |
| [houtini-ai/geo-analyzer](https://github.com/houtini-ai/geo-analyzer) | MCP server (deprecated → seo-audit-console) | ~21 | Claude-based page/text scorer | Claim density ≥4 per 100 words; 800–1,500 words; avg sentence 15–20 words; front-loading in first 100/300 words; semantic triples; entities | Claim-density and front-loading metrics |
| [GEO-optim/GEO](https://github.com/GEO-optim/GEO) | Paper code plus GEO-Bench (HF) | ~246 | Princeton GEO methods and benchmark | PA-WC and Subjective Impression metrics | Method list plus evidence of effect sizes |
| [cxcscmu/AutoGEO](https://github.com/cxcscmu/AutoGEO) | Paper code (ICLR'26) | ~150 | Mines engine preference rules; rule-guided rewriter (API) and RL-trained mini model | GEO (visibility) plus GEU (utility) | Extracted rule list = evidence-based rubric items |
| [psbagga17/E-GEO](https://github.com/psbagga17/E-GEO) | E-commerce GEO testbed | ~33 | 7k+ (paper) / 13.7k (repo) product queries from r/BuyItForLife; 5 LLM judges rank 10 products | Rank-change metric; 15 heuristic plus 14 red-team prompts | PDP rewrite evidence (see §2.3) |
| [parameterlab/c-seo-bench](https://github.com/parameterlab/c-seo-bench) | Benchmark (NeurIPS'25) | ~16 | Tests conversational-SEO methods for QA and product recs | — | Negative result: most rewrite tricks don't work, and gains are zero-sum |
| [Wu-beining/MAGEO](https://github.com/Wu-beining/MAGEO), [AIcling/agentic_geo](https://github.com/AIcling/agentic_geo) | Research frameworks | 26–38 | Multi-agent and self-evolving engine-specific optimization | — | Research only |
| [nowork-studio/toprank](https://github.com/nowork-studio/toprank) | Claude Code plugin (48 skills) | ~2.6k | SEO, ads, GSC, plus a `geo-optimizer` skill | Not published | GSC integration pattern |
| [luka2chat/geo-skills](https://github.com/luka2chat/geo-skills) / [awesome-geo](https://github.com/luka2chat/awesome-geo) | Skill plus awesome list | ~130–208 | `geo-best-practices`: 12 rule files (content, types, brand mentions, technical, schema, crawlers, llms.txt, product feed, E-E-A-T, authority, engines, analytics) | None | Rule-file decomposition; product-feed rule |
| [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt), [firecrawl/llmstxt-generator](https://github.com/firecrawl/llmstxt-generator), [dotenvx/llmstxt](https://github.com/dotenvx/llmstxt), [thedaviddias/llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub) | llms.txt spec and generators | 2.3k / 519 / 143 / 815 | Spec, generators, directory | — | Only if we publish dev docs |
| [ai-robots-txt/ai.robots.txt](https://github.com/ai-robots-txt/ai.robots.txt) | Crawler list | ~1.5k | Community list of AI user agents and configs | — | Crawler reference list |
| [AI2HU/gego](https://github.com/AI2HU/gego), [alexpospekhov/searchstack-aeo](https://github.com/alexpospekhov/searchstack-aeo), [AICMO/ai-cmo](https://github.com/AICMO/ai-cmo), [GetCito](https://github.com/ai-search-guru/getcito-worlds-first-open-source-aio-aeo-or-geo-tool) | Visibility trackers | 62–116 | Scheduled prompts across LLM APIs; logs brand mentions and cited domains | Cited / not-cited counts; brand alias normalization | DIY tracker architecture (but API answers ≠ consumer UI answers) |
| [amplifying-ai/awesome-generative-engine-optimization](https://github.com/amplifying-ai/awesome-generative-engine-optimization), [deeflect/awesome-geo](https://github.com/deeflect/awesome-geo) (site: geo.deeflect.com), [DavidHuji/Awesome-GEO](https://github.com/DavidHuji/Awesome-GEO) | Awesome lists | 367 / — / 96 | Catalogues (deeflect lists 52 OSS tools in 6 categories) | — | Discovery |

### 2.2 Detailed notes and extracted rubrics

#### A. `zubair-trabzada/geo-seo-claude` — composite GEO Score (from `docs/scoring-methodology.md` and `scripts/citability_scorer.py`)

**Structure:**
- `geo/SKILL.md` orchestrator plus `skills/geo-*/SKILL.md` (audit, citability, crawlers, llmstxt, brand-mentions, platform-optimizer, schema, technical, content, report, report-pdf, prospect, proposal, compare, update).
- `agents/` holds 5 parallel subagents: ai-visibility, platform-analysis, technical, content, schema.
- `scripts/` has `fetch_page.py`, `citability_scorer.py`, `brand_scanner.py`, `llmstxt_generator.py`, and a PDF generator.
- `schema/` holds 6 JSON-LD templates: Organization, LocalBusiness, Article+Person, SoftwareApplication, Product, WebSite+SearchAction.
- There is also a white-label kit.

**Composite (0–100):**

| Category | Weight |
|---|---|
| AI Citability & Visibility | 25% |
| Brand Authority Signals | 20% |
| Content Quality & E-E-A-T | 20% |
| Technical Foundations | 15% |
| Structured Data | 10% |
| Platform Optimization | 10% |

Bands: 90+ Excellent, 75–89 Good, 60–74 Fair, 40–59 Poor, <40 Critical.

**AI Citability & Visibility sub-weights:** passage citability 35%, brand mentions 30%, crawler access 25%, llms.txt 10%.

**Deterministic passage citability (per heading-bounded block, max 100).** This is the most reusable artifact.

| Dimension | Max | Signals (points) |
|---|---|---|
| Answer Block Quality | 30 | Definition pattern ("X is a…", "refers to", "means", "defined as") +15; answer-like content (is/are/%, $, million) in first 60 words +15; heading ends with "?" +10; share of sentences of 5–25 words ×10; quotable attribution ("according to", "research shows", "data indicates") +10. Capped at 30 |
| Self-Containment | 25 | Word count 134–167 = 10, 100–200 = 7, 80–250 = 4, 30–79 or 251–400 = 2, otherwise 0; pronoun density <2% = 8, <4% = 5, <6% = 3; ≥3 proper nouns = 7, 1–2 = 4 |
| Structural Readability | 20 | Avg sentence 10–20 words = 8 (8–25 = 5, else 2); sequence words +4; numbered/step items +4; line breaks +4 |
| Statistical Density | 15 | Percentages 3 each (max 6); $ amounts 3 each (max 5); numbers with units 2 each (max 4); year reference +2; named sources 2 each (max 6) |
| Uniqueness | 10 | Original-research phrasing ("our data/we found") +5; example/case-study phrasing +3; tool/product mention +2 |

- Page score = mean of the top 5 blocks.
- Block grades: A ≥80 "Highly Citable", B 65–79, C 50–64, D 35–49, F <35.
- Blocks need ≥20 words. Nav, header, footer, aside and form are stripped.
- Known weaknesses (from reading the source): substring matching (e.g. "second" matches "secondary"); a case-sensitive "according to" check; line-break signal rarely fires; the org list (Gartner, McKinsey, OpenAI…) is US/tech-centric. The 134–167-word "optimal passage" is cited as research-based but unverified. claude-seo labels it a third-party heuristic.

**Crawler access:** starts at 100. −15 per blocked critical crawler (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Googlebot), −5 per secondary crawler, −10 if no sitemap in robots.txt.

**llms.txt:** 0 absent, 30 malformed, 50 minimal, 70 covers main areas, 90–100 comprehensive plus llms-full.txt.

**Brand authority (points):** Wikipedia/Wikidata 30, industry/review sites (G2, Trustpilot, press) 25, Reddit 20, YouTube 15, LinkedIn 10. Cites Ahrefs Dec 2025 (75k brands): YouTube mention correlation about 0.737 vs DR/backlinks about 0.266.

**Content & E-E-A-T:**
- Weights: E-E-A-T 60%, content metrics 15%, AI-pattern / generic-phrasing assessment 10%, topical authority 10%, freshness 5%.
- E-E-A-T is scored 0–25 for each of the four letters. The normalisation method is undocumented.

**Technical:**
- Weights: SSR/JS dependency 25%, meta and indexability 15%, crawlability 15%, security headers 10%, CWV risk 10%, mobile 10%, URL 5%, response headers 5%, other 5%.
- A client-side-only empty body is treated as a critical failure.

**Structured data (100 pts):**

| Component | Points |
|---|---|
| Organization/LocalBusiness | 20 (sameAs ≥3 for full marks) |
| Article | 15 (author as Person, dateModified) |
| Author Person | 15 (sameAs, jobTitle, knowsAbout) |
| sameAs completeness | 15 (5+ incl. Wikipedia for full marks) |
| speakable | 10 |
| BreadcrumbList | 5 |
| WebSite+SearchAction | 5 |
| No deprecated types (HowTo, SpecialAnnouncement) | 5 |
| JSON-LD format | 5 |
| Validates | 5 |

JS-injected schema is flagged.

**Platform:**
- Google AIO: structure 40, authority 30, technical 30.
- ChatGPT: entity recognition 35, content preferences 40, crawler access 25.
- Perplexity, Gemini and Copilot are qualitative.

**Caveats the repo states itself:** "weights are opinion-based". Citability and llms.txt are deterministic; the rest is LLM-judged and varies run to run.

#### B. `AgriciDaniel/claude-seo` → `skills/seo-geo/SKILL.md` (v2.4.2)

**Frontmatter:** `name: seo-geo`, description (AI Overviews and answer engines), user-invocable, `[url]` argument, MIT, metadata (author, version, category).

**Stance:** follows Google's AI optimization guidance ("optimizing for generative AI search is still SEO"). Where community advice conflicts with Google, it defers to Google and flags the conflict in the report.

**GEO readiness weights:**

| Dimension | Weight |
|---|---|
| Citability (self-contained answer blocks, direct answer in first 40–60 words, "X is…" definitions) | 25% |
| Authority & Brand (bylines, credentials, dates, primary-source citations, entity presence, freshness) | 20% |
| Technical Accessibility (SSR, robots by bot purpose, RSL licensing) | 20% |
| Structural Readability (question headings, short paragraphs, tables, lists, FAQs) | 20% |
| Multi-Modal (images, video, infographics, tools plus their structured data) | 15% |

- llms.txt is reported with **0 weight**.
- The 130–170-word passage length is labeled a "third-party heuristic".

**Crawler matrix**, kept strictly separated by purpose:

| Vendor | Training | Search / citability | User-triggered |
|---|---|---|---|
| OpenAI | GPTBot | OAI-SearchBot | ChatGPT-User |
| Anthropic | ClaudeBot | Claude-SearchBot | Claude-User |
| Perplexity | — | PerplexityBot | Perplexity-User |

Also checked: Google-Extended (Gemini/Vertex training and grounding; does not affect Search), Google-CloudVertexBot, Google-Agent, CCBot, Bytespider, cohere-ai, Applebot-Extended. Rule: never merge the training and search-citability findings.

**Myths the skill rejects:** llms.txt as a citation lever, mandatory chunking, AI-specific keyword rewriting.

**Stats the skill carries (with "quote with source and date" caveat):**
- 44% of citations come from the first 30% of a page (SE Ranking).
- 92% of AIO citations come from top-10 pages, but 47% from pages ranked below position 5.
- Content under 3 months old is about 3× more likely to be cited.
- AIO and AI Mode share URLs only about 13.7% of the time (Ahrefs).
- Only 11% of domains are cited by both ChatGPT and AIO for the same query.

**Output:** `GEO-ANALYSIS.md`. Every recommendation carries an observation, dependencies, a "how would we know this failed?" check, and a leading indicator. This is a good pattern.

**Reference file:** `references/llmstxt-evidence.md` (summarized in §4).

**Other:** a `seo agentic` sub-skill scores Lighthouse "Agentic Browsing", llms.txt, markdown delivery, `ai-catalog.json` and WebMCP.

#### C. `aaron-he-zhu/core-eeat-content-benchmark` — CORE-EEAT (80 items)

- **Two systems:**
  - CORE (content body, "GEO" focus): **C**ontextual clarity, **O**rganization, **R**eferenceability, **E**xclusivity.
  - EEAT (source credibility, "SEO" focus): **Exp**erience, **Ept** (Expertise), **A**uthority, **T**rust.
- **10 items per dimension**, each tagged GEO-First, SEO-First or Dual.
- **Scoring:** Pass 10, Partial 5, Fail 0. Dimension = sum (0–100).
  - GEO = (C+O+R+E)/4.
  - SEO = (Exp+Ept+A+T)/4.
  - Total = (GEO+SEO)/2, or a content-type weighted sum.
- **Items:**
  - **C:** Intent alignment, direct answer, query coverage, definition first, topic scope, audience targeting, semantic coherence, use-case mapping, FAQ coverage, semantic closure.
  - **O:** Heading hierarchy, summary box, data tables, list formatting, schema, section chunking, visual hierarchy, anchor navigation, information density, multimedia structure.
  - **R:** Data precision, citation density, source hierarchy, evidence-claim mapping, methodology transparency, timestamp & versioning, entity precision, internal link graph, HTML semantics, content consistency.
  - **E:** Original data, novel framework, primary research, contrarian view, proprietary visuals, gap filling, practical tools, depth advantage, synthesis value, forward insights.
  - **Exp:** First-person narrative, sensory detail, process documentation, tangible proof, usage duration, problems encountered, before/after, quantified metrics, repeated testing, limitations acknowledged.
  - **Ept:** Author identity, credentials, professional vocabulary, technical depth, methodology rigor, edge cases, historical context, reasoning transparency, cross-domain integration, editorial process.
  - **A:** Backlinks, media mentions, awards, publishing record, brand recognition, social proof, knowledge-graph presence, entity consistency, partnerships, community standing.
  - **T:** Legal compliance, contact transparency, security, disclosures, editorial policy, correction/update policy, ad experience, risk disclaimers, review authenticity, customer support.
- **Veto items:**
  - T04: undisclosed affiliate links.
  - C01: clickbait or title/content mismatch.
  - R10: self-contradicting data, which makes citation reliability zero.
- **Content-type weights (%):**

| Dim | Product review | How-to | Comparison | Landing | Blog | FAQ | Alternative | Best-of | Testimonial |
|---|---|---|---|---|---|---|---|---|---|
| C | 10 | 20 | 10 | 20 | 25 | 25 | 10 | 10 | 10 |
| O | 10 | 20 | 20 | 10 | 10 | 25 | 15 | 25 | 5 |
| R | 15 | 10 | 25 | 5 | 10 | 15 | 25 | 20 | 15 |
| E | 20 | 5 | 10 | 5 | 20 | 5 | 5 | 15 | 10 |
| Exp | 20 | 5 | 5 | 5 | 10 | 5 | 15 | 5 | 30 |
| Ept | 5 | 20 | 15 | 5 | 10 | 10 | 5 | 10 | 5 |
| A | 5 | 5 | 5 | 25 | 5 | 5 | 5 | 5 | 5 |
| T | 15 | 15 | 10 | 25 | 10 | 10 | 20 | 10 | 20 |

- Bands: 90+ Excellent, 75–89 Good, 60–74 Medium, 40–59 Low, <40 Poor.
- The skill (`content-quality-auditor`) outputs the 8 dimension scores, the GEO and SEO scores, vetoes, and the top-5 improvements by impact.
- **Assessment:**
  - Strengths: the most comprehensive item taxonomy, and the only rubric with content-type weighting and vetoes.
  - Weakness: 80 LLM-judged items mean high variance and cost. Several items (backlinks, awards) are site-level, not page-level.

#### D. `onvoyage-ai/gtm-engineer-skills` → `audit-website-aeo`

- **Formula:** Final = 0.5 × Foundational + 0.5 × Intelligence.
- **Foundational:** 16 pass/fail checks scored by a Node crawler (`aeo-audit.mjs`), worth 142 points in total. A site-wide check passes if ≥80% of crawled pages pass. Points per check:

| Check | Points |
|---|---|
| title ≥10 chars | 10 |
| meta-description ≥50 chars | 10 |
| canonical | 8 |
| exactly one H1 | 8 |
| JSON-LD present | 8 |
| recognized schema type | 8 |
| OG title + description | 8 |
| ≥5 internal links | 10 |
| ≥80% images with alt | 8 |
| ≥250 words body text | 12 |
| indexable | 10 |
| no AI/snippet-blocking meta | 6 |
| heading hierarchy (no skipped levels) | 6 |
| valid llms.txt | 10 |
| robots doesn't block 9 major AI crawlers | 12 |
| RSS/Atom feed | 8 |

- **Intelligence:** 6 LLM-judged dimensions at 0–5 each (mean ×20). A **rationale must be written before each score**, grounded only in observed excerpts.
  - Answer Readiness
  - Quotability
  - Evidence Density
  - Content Depth
  - Freshness
  - Structural Clarity
- **Grades:** A+ 95+, A 90, A− 85, B+ 80, B 75, B− 70, C+ 65, C 60, C− 55, D 40, F <40.
- **Rules:** no fabricated pages; the foundational score cannot be adjusted by the LLM; the skill only diagnoses (fixes are handed off to `improve-aeo-geo`).
- **Pipeline skills** worth borrowing: `reddit-opportunity-research`, `geo-content-research`, `create-geo-charts`, `build-resource-pages`.

#### E. `Auriti-Labs/geo-optimizer-skill` — Rubric v2 (100 points, from `docs/scoring-rubric.md`)

| Category (max) | Checks (points) |
|---|---|
| google_ai (20) | G-INDEX 5; G-SNIPPET 5 (fails on nosnippet / max-snippet <50; data-nosnippet >50%); G-CANONICAL 3; G-DATES 2 (visible date = schema dates, not future); G-BYLINE 2; G-LINKS 1 (crawlable `<a href>`); G-VIEWPORT 1; G-SITEMAP 1 |
| robots (14) | found 3; citation bots allowed 11 (OAI-SearchBot, ClaudeBot, Claude-SearchBot, PerplexityBot) |
| schema (14) | valid JSON-LD 2; richness 2; FAQPage 2; Article 2; Organization 3; WebSite 1; JSON-LD name visible on page 2 |
| content (14) | H1 2; numbers/stats 1; external links 1; word count 1; heading hierarchy 3; lists/tables 2; front-loading (key info in first 30%) 2; image alt 2 |
| brand_entity (12) | coherence 3; KG readiness (sameAs to authoritative domains) 4; about/contact 3; geo identity 1; topic authority 1 |
| meta (11) | title 5; description 2; OG 4 |
| llms (6) | found 3; sections 1; links 1; llms-full 1 |
| signals (6) | `<html lang>` 3; RSS 1; freshness 2 |
| ai_discovery (3) | ai.txt 1; /ai/summary.json 1; markdown negotiation 1 |

- **Bands:** 86+ Excellent, 68–85 Good, 36–67 Foundation, ≤35 Critical.
- **Negative signals** (up to −5): CTA overload, popups, thin content, keyword stuffing, missing author, boilerplate ratio, and others.
- **Unscored informational checks:** CDN crawler access, JS rendering, prompt-injection detection, RAG chunk readiness, content decay, WebMCP.
- The v1 rubric gave llms.txt 18 points. v2 cut it to 6, which tracks the community's loss of faith in llms.txt.

#### F. `IJONIS/geo-lint` — deterministic lint rules

- 97 rules: SEO 34, content 14, technical 10, i18n 3, **GEO 36 (all warnings)**.
- GEO rules cover E-E-A-T, structure, freshness, RAG optimization and author entity type.
- Examples:
  - `geo-weak-lead-sentences`: the first sentence after a heading is filler. AI often uses that sentence as the snippet.
  - `geo-low-citation-density`
  - `geo-missing-table`: prose comparisons without a table.
  - `geo-no-question-headings`: flags e.g. only 20% of H2/H3 phrased as questions.
- Each violation is JSON with `rule`, `line`, `suggestion` and `fixStrategy`. The agent loops until the output is `[]`.
- Agents are told to restructure, not rewrite voice. This is the right model for a writer-facing tool.

#### G. `houtini-ai/geo-analyzer` (deprecated)

- Metrics: claim density target ≥4 extractable claims per 100 words; 800–1,500 words "optimal"; average sentence 15–20 words; answer front-loading (claims and entities in the first 100/300 words, position of first claim); semantic triples; entity count.
- Outputs four 0–10 scores (Overall, Extractability, Readability, Citability) with undocumented weights.
- Note: it claims "local" analysis, but sends text to the Claude API.

#### H. `coreyhaines31/marketingskills` → `ai-seo` (v2.7.6) — methodology without numbers

- **Three pillars:**
  - **Structure:** direct answers first, 40–60-word key passages, query-matching H2/H3, tables, numbered steps.
  - **Authority:** cited and dated statistics, expert attribution, quarterly refresh.
  - **Presence:** Wikipedia, Reddit, LinkedIn, G2/Capterra, YouTube, podcasts, Quora, with positioning consistent with the About page.
- **Machine-readable layer:** `/pricing.md`, `/llms.txt`, `/okf/` (Google-backed v0.1 format, no confirmed signal), agent readiness (markdown negotiation, WebMCP).
- **10-item extractability checklist (pass/fail):**
  1. Definition in first paragraph
  2. Self-contained answer blocks
  3. Sourced statistics
  4. Comparison tables
  5. Natural-language FAQ
  6. Schema
  7. Expert attribution
  8. Recent update
  9. Query-matching headings
  10. Crawler policy matching goals
- **Audit workflow:** test 10–20 revenue queries across the 4 awareness stages; analyze competitors' citation patterns; check bots by purpose.
- **Reference: `format-volatility.md`.** Peec AI data via Tomek Rudzki and Lily Ray: after ChatGPT 5.6 (Aug 2026), listicle citation share fell 15.77% → 7.80% (−50.5%) and comparison pages 9.08% → 6.17% (−32.1%). Fan-out modifiers shifted from "best/vs/top/reviews" to `site:` and "official". Owned product, docs and pricing pages rose.
  - Format-by-engine matrix: listicles demoted on ChatGPT and ranking-dependent on AIO; original research strong everywhere; product/docs/pricing "dominant on Gemini".
  - DIY fan-out diagnostic: DevTools → conversation payload → `queries`.
- **Reference: `citations-vs-recommendations.md`.**
  - Ladder: retrieved → cited → mentioned → recommended. Recommendation is driven by web-wide consensus (reviews, analysts, communities, PR, video/podcasts).
  - Lily Ray: 69% of self-promotional listicle AIO citations recommended others.
  - SimilarWeb: recommended brands got about 2.5× more new visitors the following week.
  - Only about 9% of post-recommendation visits show as AI referrals.
  - Triad: prompt tracking, "how did you hear about us" with an AI option, sales-call language.
  - Tactic: name the category leader first, then show where you go further.
- **Reference: `platform-ranking-factors.md`:**
  - ChatGPT uses a Bing-based index. SE Ranking (129k domains): authority ~40%, content quality ~35%, platform trust ~25%. Content updated within 30 days was cited about 3.2× more. ZipTie (400k pages): content-answer fit ~55% vs domain authority 12% and on-page structure 14%.
  - Perplexity: own index plus Google, ML quality gate, time decay, likes FAQ JSON-LD and public PDFs.
  - Copilot: Bing only, IndexNow, sub-2s speed, LinkedIn citations about 6.5× Reddit.
  - Claude: Brave Search; very selective; favors precise, well-sourced numbers; in a Sep 2026 test it ignored self-ranked vendor lists in favor of juried awards and practitioner reputation.
- **"Don't" list:** separate AI content, chunking into fragments, mass generation, inauthentic mentions, treating all AI bots as one, JS-hidden content, skipping E-E-A-T.
- **Measurement:** run each query 3–5× in fresh sessions; report rates with n; diagnose failures as technical, comprehension or trust.

### 2.3 Research-code evidence (what the papers behind the repos actually show)

**Princeton GEO (GEO-optim/GEO, KDD'24).** Gains on GEO-Bench vs baseline:

| Method | PA-WC gain | Subjective Impression gain |
|---|---|---|
| Quotation Addition | +42.6% | +28.0% |
| Statistics Addition | +32.8% | +22.8% |
| Fluency Optimization | +28.7% | +13.5% |
| Cite Sources | +27.7% | +13.5% |
| Technical Terms | +18.5% | +10.9% |
| Easy-to-Understand | +13.8% | +6.2% |
| Authoritative | +11.8% | +18.7% |
| Unique Words | +6.2% | +5.7% |
| Keyword Stuffing | −8.7% | +4.7% |

- Lower-ranked sources benefit most: Cite Sources +115% at rank 5, while the rank-1 source fell 30%.
- Effects vary by domain: Statistics works best for Law & Government and Opinion; Quotations for People & Society, Explanation and History; Cite Sources for Facts and Law & Government.
- PA-WC weights citing sentences by e^(−position).

**AutoGEO (cxcscmu, ICLR'26).**
- Mines engine preferences from pairwise "why was A more visible than B" explanations, then turns them into rules.
- Shared rules across engines: attribute claims to credible sources; comprehensive sub-topic coverage; factual accuracy; **neutral, non-promotional tone**; logical structure; concise language that defines jargon; up-to-date information.
- Domain rules:
  - Research: explain how and why, put the conclusion first, give specific evidence and balanced views, keep content self-contained.
  - E-commerce: step-by-step guidance, actionable recommendations, pros and cons, product details, non-exaggerated claims.
- Engine rule sets overlap 79–84% (Jaccard).
- AutoGEO-API improved GEO score by about 36% on average, up to 51% over the best baseline (e.g., Researchy-GEO on Gemini: 20.2 → 43.8), while keeping utility.
- Adversarial hijack and poisoning raised visibility but cut utility.

**E-GEO (e-commerce, arXiv 2511.20867).**
- Setup: 5 LLM judges (GPT-5, Claude Sonnet 4.5, Gemini 3 Flash, DeepSeek V3.2, Llama 4) re-rank 10 products after a description rewrite. Facts are held constant.
- Hand-written heuristics mostly do little or harm. Mean rank change:
  - Competitive "highlight unique advantages" +0.71 (best)
  - Quality +0.65
  - FAQ +0.06
  - Format (headings and bullets) −0.35
  - Technical −0.49
  - Minimalist −1.66
  - Storytelling −4.03
- After prompt optimization, all strategies are positive (+0.68 to +1.61).
- Optimized prompts converge on user-intent alignment, competitive differentiation, external evidence (reviews/ratings), USPs and scannability, while preserving factuality.
- Implication for PDPs: write for the buyer's use case, state differentiators against alternatives, surface review evidence, and never invent facts.

**C-SEO Bench (NeurIPS'25).**
- Most conversational-SEO rewrite methods are "largely ineffective" and often hurt ranking.
- Traditional SEO, which gets the source ranked into the LLM's context, is significantly more effective.
- Benefits shrink as adoption rises (zero-sum congestion).

---

## 3. Existing Claude / LLM skills for GEO — structure, methodology, strengths and gaps

### 3.1 The Agent Skills format (agentskills.io spec, which Anthropic's skills follow)

- **Directory:** `skill-name/SKILL.md` (required) plus optional `scripts/`, `references/` and `assets/`.
- **Frontmatter:**

| Field | Required | Constraint |
|---|---|---|
| `name` | Yes | ≤64 chars, lowercase/digits/hyphens, no leading, trailing or double hyphen, must equal the folder name |
| `description` | Yes | ≤1024 chars; must say **what it does and when to use it**, with trigger keywords |
| `license` | No | — |
| `compatibility` | No | ≤500 chars |
| `metadata` | No | String map, e.g. author and version |
| `allowed-tools` | No | Experimental |

  Claude Code skills also use `argument-hint` and `user-invocable`, as Anthropic's own `seo-audit` and claude-seo do.
- **Progressive disclosure:**
  1. Metadata (~100 tokens) is always loaded.
  2. The SKILL.md body (<5,000 tokens, <500 lines) loads on activation.
  3. references, scripts and assets load on demand.

  Keep references one level deep.
- **Validation:** `skills-ref validate`.
- **Distribution:** Claude Code `/plugin marketplace add <owner/repo>` then `/plugin install`; the cross-agent `npx skills add <repo>` (skills.sh telemetry leaderboard); directories.
- **Directories:** skills.sh, skillsmp, claudeskills.info, skills-hub.ai, skills.cat, playbooks.com, openskillindex, vibeindex, agentskill.work, tessl registry, ClawHub.
- **Tessl's quality review** (useful as our own QA bar): Content 40% (conciseness, actionability, workflow clarity, progressive disclosure), Description 40% (specificity, completeness incl. a "use when" clause, trigger terms, distinctiveness), spec validation, and a Snyk security scan.
  - Its critique of `vudovn/ag-kit/geo-fundamentals` (overall 51): reads as reference material rather than a workflow (workflow clarity 2/5); re-explains what GEO is; lacks copy-paste snippets; no "use when" clause.
- **Anthropic official:**
  - `anthropics/skills` has no SEO/GEO skill.
  - `anthropics/knowledge-work-plugins` → `marketing/skills/seo-audit` (frontmatter `name`, `description`, `argument-hint`) covers keywords, on-page, content gaps, technical and competitor checks. It **contains no AI-search / GEO elements**, only PAA, featured snippets and FAQ/HowTo schema. This is a gap our skill can fill.

### 3.2 Comparison of GEO skills

| Skill | Architecture | Methodology core | Strengths | Gaps |
|---|---|---|---|---|
| geo-seo-claude | Orchestrator + 14 sub-skills + 5 parallel agents + Python scorers + JSON-LD templates + PDF | Weighted composite (25/20/20/15/10/10); deterministic block citability | Transparent weights; deterministic citability; ready templates; delta tracking (`geo-compare`) | Weights unvalidated; agency/sales orientation (prospect CRM, Skool promo); US-tech-centric heuristics; installs a venv via shell script (supply-chain review needed); brand points favor B2C platforms |
| claude-seo `seo-geo` | One skill inside a 26-skill plugin; references incl. llms.txt evidence | Google-first; 5 dimensions (25/20/20/20/15); llms.txt 0 weight | Most evidence-disciplined (labels heuristics, dates stats); strict bot-purpose separation; recommendation format with falsification check | Large footprint; credential tiers for Google APIs; no content-type weighting |
| marketingskills `ai-seo` | Single SKILL.md + 10 focused references | Structure / Authority / Presence; visibility ladder; format volatility | Freshest data (Aug–Sep 2026); excellent measurement guidance; platform-specific format matrix | No numeric score; marketing/SaaS bias |
| CORE-EEAT `content-quality-auditor` | Skill + benchmark reference file | 80 items, pass/partial/fail, content-type weights, vetoes | Most complete taxonomy; content-type weighting; veto logic | Heavy, variable LLM judgement; mixes site- and page-level items |
| gtm-engineer `audit-website-aeo` | Skill + Node crawler + evals (`npm run test:evals`) | 50% deterministic / 50% LLM, rationale-first | Best anti-hallucination design; ships evals | Foundational checks are basic SEO hygiene; llms.txt worth 10/142 |
| geo-lint | npm linter + Claude skill + content-creator pipeline | 36 GEO warnings, auto-fix loop | Deterministic and CI-friendly; writer-friendly fixes | Markdown/MDX focus; thresholds hidden in config |
| luka2chat `geo-best-practices` | 12 rule files | Implementation templates (robots, schema, product feed) | Product-feed rule (relevant to ecommerce) | No scoring |
| Others: toprank `geo-optimizer`, eGEOagents, liangdabiao GEO-Content-Optimizer (compares a URL to the AI Overview summary), tech-leads-club GEO, schwepps `geo-aeo-optimization`, ivzc07 `aeo-skills` | — | — | The AIO comparison idea (liangdabiao) is useful | Low adoption and little documentation |

**Design lessons for our own GEO skill:**
1. Keep the SKILL.md body as a **numbered workflow**: fetch → deterministic checks → LLM-judged dimensions with rationale → score → prioritized fixes → optional rewrite. Put rubrics, crawler lists, schema templates and evidence in `references/`.
2. Write a description with a **"Use when…" clause** and synonyms: GEO, AEO, AI citations, AI Overviews, ChatGPT, Perplexity, Copilot, LLM visibility.
3. Make the scoring **script deterministic where possible**: block extraction, word counts, stats/attribution regexes, heading checks, schema presence. LLM judgement should not override the deterministic part.
4. Add **content-type profiles**: PDP, datasheet/spec page, how-to/installation guide, solution/landing page, blog/thought leadership, FAQ/support article. Each gets its own weights.
5. Use **veto rules**: factual inconsistency (e.g., specs differ between the page and the schema), title/intent mismatch, missing disclosures.
6. Write **evidence-labelled recommendations** with source and date, plus a "how we'd know it failed" check.
7. Avoid the gaps above: sales/CRM bloat, US-only org lists, B2C-only brand platforms, and install scripts that fetch remote content.

---

## 4. Reddit / community practitioner insights

### 4.1 Community landscape

GummySearch snapshots, Sep–Oct 2026:

| Community | Size | Recurring topics |
|---|---|---|
| r/aeo | ~10k | — |
| r/GEO_optimization | ~10k | — |
| r/GenEngineOptimization | ~6k, +192% YoY | "When an AI answer cites a competitor, what do you check first?" (20 posts); where ChatGPT's business recommendations come from; "has ChatGPT/Perplexity ever sent you a customer?"; seeing ChatGPT's background searches; "a crawler policy is not an AI-visibility strategy" |
| r/GEO_chat | ~836 | GEO vs SEO; measuring whether AI evaluates your site; LLM tracking tools; "do LLMs use llms.txt?"; "please stop talking about rankings" |
| r/GenEngineOptimizers | ~433 | White/grey/black-hat GEO thread |
| r/SEO_AEO_GEO | ~190 | Dominant mood: "pain & anger" about decaying blue links |

Pain points across all of them: opaque sourcing, tool overload, unclear ROI, platform volatility.

### 4.2 What practitioners report works

- **Ranking and retrieval first.** A recurring theme from HN, the C-SEO Bench result and the Google-first skills: the eligibility floor is being indexed and ranking for the fan-out sub-queries. Data cited: 92% of AIO citations come from the top 10. Rank–citation correlation is only about 0.35 (Ahrefs), and only about 17% of AIO sources rank in the organic top 10 for the head query. That means **ranking for the fan-out queries**, not the head term.
- **Specific, unique facts.** Real capabilities, real pricing, honest comparisons, original data and stats (Sitefire Launch HN founders, citing the GEO paper).
- **Front-loaded answers.** About 44% of citations come from the first 30% of a page (SE Ranking). geo-lint flags weak lead sentences.
- **Off-site consensus decides recommendations.** HN commenters saw products recommended for a week, then fade unless outside mentions kept being reinforced. Also reported: AI cares less about domain age than Google, and Reddit threads, blogs and docs can surface new products early.
- **Use-case pages and procedural detail.** On HN: being able to map a product to a problem, independent mentions, clear procedural detail.
- **Matching ChatGPT's fan-out queries.** A widely shared Reddit method: inspect the network payload for `queries` and align titles and sub-topics. Since Aug 2026 the fan-outs lean toward `site:` and "official".
- **Freshness.** Many practitioners add the year to titles. Otterly's test was **inconclusive**: citations rose, but an untouched control page rose 63%.
- **Genuine Reddit participation**, per SORN.ai via Otterly:
  - Real people, in subreddits where buyers already are.
  - Roughly 1 branded post per 5–8 non-branded posts; objective, including weaknesses.
  - About 15 hours per month per community.
  - Mirror important content on owned properties.
  - Skip Reddit for engines that rarely cite it (Claude, Gemini).
- **Ecommerce/PDP.**
  - Visibility Labs (94 stores, 12 months): ChatGPT referrals converted at 1.81% vs 1.39% for non-branded organic. About 70% of AI influence is invisible in GA4 (it shows up as branded search).
  - Correlates: Product schema plus clean GTINs; price present in the server HTML (check View Source, not Inspect).
  - Keep the PDP, JSON-LD, Merchant Center feeds and ChatGPT/ACP feeds consistent.
  - Shopify Agentic Storefronts are the main channel.
  - Datma (hundreds of Shopify stores): ChatGPT-tagged sessions grew from 0.0006% to 0.11% of traffic Jan–Aug 2025. Small but fast-growing.
- **B2B.**
  - An HN anecdote reports ChatGPT leads that convert up to about 7× better for some B2B SaaS companies (unverified).
  - Manufacturing guidance: full spec catalogs, material datasheets, certifications, part-number and compatibility data in parseable HTML. There is little rigorous evidence. The FHNW student study of an industrial toolmaker found brand visibility strong for branded prompts, but no GEO process in place.
  - Lily Ray's B2B listicle study (below) is the strongest B2B data point.

### 4.3 What doesn't work, or is unproven

- **llms.txt.** Ahrefs (137K sites): 97% of files never requested, and 77% of fetches came from non-AI bots (mostly SEO tools). Other studies:
  - OtterlyAI logs: 84 of 62,100 AI-bot requests hit llms.txt.
  - Senthor: 104 of 10M+ AI-bot requests, none attributable to a known AI company.
  - Luxeo: pages linked only from llms.txt were never fetched.
  - SE Ranking: 1 of the top 50 AI-cited domains has one.

  Google (Mueller, Illyes) calls it unused, compared it to meta keywords, and in 2026 called it "a dead end". The Reddit sentiment summarized by GummySearch is skeptical, with occasional "spotted in the wild" threads. **Consensus:** low-cost optionality; useful only for developer docs and coding agents.
- **Schema as a citation lever.** Ahrefs (May 2026, 1,885 treated pages vs about 4,000 controls, 30 days) found no significant uplift on any platform. Correlational studies (AirOps; Ahrefs 6M URLs: cited pages about 3× likelier to have JSON-LD) are confounded by site quality. Tests disagree on whether LLM fetchers read JSON-LD at all: Mark Williams-Cook says yes, searchVIU says visible HTML only. **Consensus:** keep schema for entities, Product/Offer feeds and rich results, and make sure the same facts are **visible on the page**.
- **Self-promotional "best X" listicles.**
  - Lily Ray (100 B2B queries, spring 2026): 323 AIO citations; 69% recommended others.
  - Peec (232k citations): about 11% of software citations come from self-promo listicles; ChatGPT lowest at about 4%.
  - Ahrefs: it helps new brands get mentioned, barely moves known brands, and the effect is temporary.
  - ChatGPT 5.6 halved listicle citation share.
  - Google's May 2026 spam update targets "biased best-of listicles".
- **Content-only rewrite tricks** (C-SEO Bench; E-GEO hand-written heuristics). "Format headings and bullets" was negative before optimization. Keyword stuffing is negative in Princeton GEO.
- **Mass-generated pages per fan-out query.** This is the pattern ChatGPT 5.6 demoted and Google classifies as scaled-content abuse.
- **Brand-new single prompts as KPIs.** On HN, an ~800-query study found answers change overnight, and Google AI Mode and ChatGPT agreed on the top recommendation only about 47% of the time. Personalization, location and account history add noise.

### 4.4 Recurring debates

1. **"GEO is just SEO."**
   - The Google-first camp (Hobo-Web's "the GEO grift is over, it's SEO", Position Digital, David Quaid) points to Google's own statement and the C-SEO result.
   - The "separate discipline" camp (James Dooley now runs a separate GEO team; one estimate puts SEO/GEO overlap at about 40%) points to entity authority, off-site consensus, format and platform differences, and only 11% domain overlap between ChatGPT and AIO.
   - **Synthesis:** shared foundations, plus extractability, plus multi-platform presence, plus probabilistic measurement.
2. **llms.txt:** see 4.3. Mostly settled negative for non-dev sites by late 2026.
3. **Schema:** settled as "hygiene, not lever" for citations.
4. **Reddit seeding.**
   - Local SEO Guide: 100 mentions plus 100 comments in a month gave about 3× AIO citations within weeks, which **reverted when the campaign stopped**.
   - Otterly's owned subreddits reached #6 of 126 for citations, then were banned (Reddit Rule 2, content manipulation, bots detected).
   - ChatGPT's Reddit citation share fell from about 3.8–4.0% to about 0.4–0.5% around 8–14 Aug 2026. Promptwatch links this to `site:` fan-outs rising from 0.4% to about 17%; the cause is unproven. AIO and AI Mode declined only gradually, and Perplexity rose.
   - Gemini cites Reddit in about 0.1% of responses. Claude and Copilot showed no Reddit citations in Otterly's data.
5. **Listicles and comparison pages:** still useful for humans and for AIO, Gemini and Perplexity, but no longer a ChatGPT lever. The credible framing is to name the leader first.
6. **White/grey/black-hat GEO:** a Reddit thread exists. Black-hat examples include recommendation poisoning (seeding forums and reviews), fake citations, hidden prompt text and cloaking for AI user agents. An HN post shared a system prompt to defend against a GEO poisoning campaign, which shows engines and users are actively countering it. geo-optimizer-skill even includes prompt-injection detection as a check.

### 4.5 Red flags and spam tactics, to avoid and to detect in audits

- Bot or account-network engagement on Reddit, owned "community" subreddits, account warming.
- Self-ranked "best X" lists that put yourself #1 with no disclosure.
- Scaled AI pages, one per fan-out query.
- Hidden or JS-only content; cloaking for AI user agents; hidden instructions aimed at LLMs (prompt injection).
- Fake statistics or citations. AutoGEO's "poisoning/hijack" raised visibility but destroyed utility.
- Vendors selling guaranteed "AI rankings" or llms.txt as a fix; Shopify apps marketed as "Rank on ChatGPT".
- Over-reliance on a single platform.
- **Policy:** Google's 15 May 2026 spam-policy update explicitly covers manipulating generative AI responses. Penalties can remove a site from Search including AI features.

---

## 5. Synthesis

### 5.1 Consensus best practices, ranked by strength of evidence

| # | Practice | Evidence strength |
|---|---|---|
| 1 | Be retrievable: indexable, server-rendered HTML; search/citation bots allowed by purpose (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Bingbot/Googlebot); WAF/CDN not blocking; Bing indexing and IndexNow for ChatGPT/Copilot | Strong (vendor docs, C-SEO, all skills) |
| 2 | Rank for the fan-out sub-queries: topical cluster coverage, internal links | Strong |
| 3 | Answer-first, self-contained passages: definition or answer in the first 40–60 words of each section; question-matching headings; low pronoun dependency; key info in the first 30% of the page | Moderate–strong (Princeton GEO structure, SE Ranking 44%/30%, AutoGEO "conclusion first / self-contained") |
| 4 | Evidence density: specific numbers with units, named sources, quotations, dates, methodology | Strong (Princeton: +28–43%; AutoGEO "attribution" rule) |
| 5 | Neutral, accurate, non-promotional tone with no exaggeration; acknowledge limitations | Moderate (AutoGEO shared rule; Claude favoring juried sources) |
| 6 | Unique and original information: proprietary data, real specs and pricing, case studies | Moderate |
| 7 | Freshness: visible, accurate dateModified; quarterly refresh of competitive pages | Moderate, correlational (3×/3.2× claims) |
| 8 | Structure for extraction: tables for comparisons/specs, numbered steps, lists, clean heading hierarchy | Moderate (but naive "format" rewriting alone was negative in E-GEO) |
| 9 | Authority and entity clarity: named expert author with credentials, Organization/Person with sameAs, consistent descriptions across the web | Moderate |
| 10 | Off-site consensus: reviews, analysts, trade press, communities, YouTube, LinkedIn. Drives recommendation, not just citation | Moderate (Ahrefs 75k brands; Ray; SimilarWeb) |
| 11 | Schema and llms.txt: hygiene and entity support; no measurable citation lever | Settled negative as a lever |
| 12 | Measure probabilistically: 3–5 runs per prompt, rates with n, the visibility ladder, mention framing, branded-search lift, self-reported attribution | Consensus |

### 5.2 Comparison of existing scoring rubrics (dimension → weight)

| Dimension | geo-seo-claude (site) | claude-seo seo-geo | CORE-EEAT (blog default) | gtm-engineer audit-website-aeo | geo-optimizer v2 | houtini |
|---|---|---|---|---|---|---|
| Answer-first / citability / extractability | 25% (citability 35% of it) | 25% | C 25% | Answer Readiness + Quotability ≈ 17% (2 of 6 LLM dims × 50%) | content front-loading 2 pts | Extractability, Citability |
| Evidence / statistics / sources | inside citability (15/100 per block) | inside citability / authority | R 10% | Evidence Density ≈ 8% | numbers 1 pt | claim density |
| Structure / readability | inside citability (20/100 per block) | 20% | O 10% | Structural Clarity ≈ 8% + heading checks | heading 3 + lists 2 | Readability |
| Uniqueness / original data | inside citability (10/100 per block) | — | E 20% | Content Depth ≈ 8% | — | — |
| E-E-A-T / authority (page) | 20% | 20% (with brand) | Exp/Ept/T 30% | — | byline 2 | — |
| Brand / entity / off-site | 20% | (within 20%) | A 5% | — | brand_entity 12 | — |
| Freshness | 5% of content | in authority | R06, T06 items | Freshness ≈ 8% | dates 2 + freshness 2 | — |
| Technical / crawlability | 15% + crawler 25% of citability | 20% | — | most of 50% foundational | google_ai 20 + robots 14 + meta 11 | — |
| Structured data | 10% | in structure/multimodal | O05 item | schema 16/142 | 14 | — |
| Multimodal | — | 15% | O10, E05 | — | image alt 2 | — |
| llms.txt | 10% of citability (≈2.5% total) | 0% | — | 10/142 (≈3.5%) | 6 | — |
| Platform-specific | 10% | reported separately | — | — | — | — |
| Vetoes / negatives | — | — | 3 vetoes | — | −5 negative signals | — |

**Observations:**
- Rubrics overweight technical hygiene and llms.txt relative to the evidence. They underweight evidence density and neutrality, the two levers with the strongest experimental support.
- Only CORE-EEAT weights by content type. Only CORE-EEAT and geo-optimizer penalize anything.
- None models **consistency of facts across surfaces** (page vs schema vs feed vs datasheet), which matters especially for B2B and ecommerce.
- None separates **page-level content citability** (what a writer controls) from **site and off-site authority** (what SEO and PR control) as cleanly as a content tool should.

### 5.3 Recommended best-in-class content GEO scoring rubric (for our skill)

**Design principles:**
- Score at the page level.
- About 60% deterministic, with the rest LLM-judged; each LLM score needs a rationale and quoted evidence.
- Use content-type weight profiles.
- Apply vetoes and penalties.
- Report site/off-site signals separately as context, not mixed into the page score.
- Label each criterion with its evidence level.

**Page Content GEO Score (0–100):**

| # | Dimension | Default weight | Criteria (D = deterministic, L = LLM-judged) | Evidence |
|---|---|---|---|---|
| 1 | **Answer-first extractability** | 20 | D: definition/answer pattern in the first 40–60 words of the page and each H2 section; key facts in the first 30% of the page; share of question-form or query-matching H2/H3. L: does each section answer one intent completely without relying on surrounding context? | Princeton, SE Ranking, AutoGEO |
| 2 | **Self-contained passages** | 10 | D: passage length distribution (heuristic 75–200 words, not a hard rule); pronoun density <2–4%; explicit entity naming (product, standard and model names repeated, not "it") | geo-seo-claude heuristic (moderate) |
| 3 | **Evidence density and attribution** | 20 | D: numeric facts with units per 100 words (target ≥2–4); named sources/standards (IEC, UL, NEC, ISO…); quotations from named experts; dated facts. L: is every non-obvious claim supported? | Princeton (strongest), AutoGEO |
| 4 | **Specificity and originality** | 10 | L: proprietary data, test results, real specs/pricing/lead times, case outcomes, original diagrams; not generic or AI-pattern text | AutoGEO, Sitefire, marketingskills |
| 5 | **Neutral, accurate tone** | 10 | L: non-promotional, no superlatives without proof, balanced pros/cons, limitations and "when not to use"; names alternatives fairly. Penalty for CTA overload | AutoGEO shared rule; E-GEO factuality; Claude behavior |
| 6 | **Structure for machines** | 10 | D: single H1, no skipped heading levels, tables for specs and comparisons, numbered steps for procedures, lists, descriptive alt text, content present in server HTML | Consensus |
| 7 | **Authority and trust (page)** | 10 | D: visible named author or reviewer with credentials and an author page; Organization/Person schema with sameAs; editorial or "reviewed by engineer" note; disclosures | E-E-A-T (moderate) |
| 8 | **Freshness and versioning** | 5 | D: visible datePublished/dateModified matching schema; current year references; version or standard edition cited | Correlational |
| 9 | **Machine-readable consistency** | 5 | D: JSON-LD valid and matching visible text (name, price, specs, GTIN/MPN); Product/Offer or Article/FAQ as fit; no deprecated types. Hygiene only | Ahrefs (no lift alone) |

- **Content-type weight profiles** (adjust the defaults):
  - **PDP / product page:** ↑ evidence/specs, machine-readable consistency (Product, Offer, GTIN, MPN), neutral tone and use-case fit (E-GEO: intent, differentiation, reviews). ↓ authorship.
  - **Datasheet / technical spec page:** ↑ structure (tables), evidence (units, standards), versioning; HTML version preferred over PDF-only.
  - **How-to / installation guide:** ↑ answer-first, structure (steps), authority (qualified author, safety disclaimers).
  - **Solution / landing page:** ↑ authority/trust, specificity (outcomes), answer-first definition of the solution.
  - **Thought-leadership / blog:** ↑ originality, evidence, authority.
  - **FAQ / support article:** ↑ answer-first, self-containment.
- **Vetoes** (cap the score at 40 and flag):
  - Factual contradiction within the page or between page, schema, feed and datasheet.
  - Title/intent mismatch.
  - Content not present in server-rendered HTML.
  - Page blocked from search/citation bots or noindex.
  - Undisclosed sponsorship or self-ranking.
  - Hidden text or prompt-injection aimed at LLMs.
- **Penalties** (up to −10): keyword stuffing, unsupported superlatives, boilerplate ratio above 40%, CTA/popup overload, AI-pattern filler, scaled near-duplicate pages.
- **Reported separately as context, not in the page score:**
  - Site technical access by bot purpose.
  - Fan-out/topical coverage gaps.
  - Off-site consensus: Wikipedia/Wikidata, trade press, distributors/marketplaces, review sites, LinkedIn, YouTube, relevant communities, analyst coverage.
  - Measured visibility ladder: retrieved, cited, mentioned, recommended, with n and run count.
  - llms.txt presence (0 weight; recommend it only for developer and API docs).
- **Output:** dimension scores with rationale and quoted evidence; top 5 fixes ranked by impact × effort; suggested rewrites of lead sentences, tables and FAQ blocks that **restructure without changing facts**; each fix tagged with its evidence level and a "how we'd know it failed" metric.

---

## 6. Sources

**GitHub repos and files read**
- https://github.com/zubair-trabzada/geo-seo-claude — README, `docs/scoring-methodology.md`, `scripts/citability_scorer.py`, repo tree (GitHub API)
- https://github.com/AgriciDaniel/claude-seo — README, `skills/seo-geo/SKILL.md`, `skills/seo-geo/references/llmstxt-evidence.md`
- https://github.com/coreyhaines31/marketingskills — `skills/ai-seo/SKILL.md`, `references/format-volatility.md`, `references/citations-vs-recommendations.md`, `references/platform-ranking-factors.md`
- https://github.com/aaron-he-zhu/seo-geo-claude-skills ; https://github.com/aaron-he-zhu/core-eeat-content-benchmark (README)
- https://github.com/onvoyage-ai/gtm-engineer-skills — README, `audit-website-aeo/SKILL.md`
- https://github.com/Auriti-Labs/geo-optimizer-skill — README, `docs/scoring-rubric.md`
- https://github.com/IJONIS/geo-lint
- https://github.com/houtini-ai/geo-analyzer
- https://github.com/nowork-studio/toprank
- https://github.com/luka2chat/geo-skills ; https://github.com/luka2chat/awesome-geo
- https://github.com/deeflect/awesome-geo (catalogue at https://geo.deeflect.com) ; https://github.com/amplifying-ai/awesome-generative-engine-optimization ; https://github.com/DavidHuji/Awesome-GEO
- https://github.com/GEO-optim/GEO ; https://github.com/cxcscmu/AutoGEO ; https://github.com/psbagga17/E-GEO ; https://github.com/parameterlab/c-seo-bench
- https://github.com/alexpospekhov/searchstack-aeo ; https://github.com/AI2HU/gego ; https://github.com/AICMO/ai-cmo
- https://github.com/AnswerDotAI/llms-txt ; https://github.com/firecrawl/llmstxt-generator ; https://github.com/ai-robots-txt/ai.robots.txt
- https://github.com/anthropics/skills ; https://github.com/anthropics/knowledge-work-plugins (`marketing/skills/seo-audit/SKILL.md`)

**Papers**
- Princeton GEO: https://arxiv.org/abs/2311.09735 (HTML v3 tables)
- AutoGEO: https://arxiv.org/abs/2510.11438
- E-GEO: https://arxiv.org/abs/2511.20867
- C-SEO Bench: https://arxiv.org/abs/2506.11097 ; https://neurips.cc/virtual/2025/poster/121465

**Skill spec and hubs**
- https://agentskills.io/specification
- https://skills.sh (incl. https://skills.sh/anthropics/knowledge-work-plugins)
- https://tessl.io/registry/skills/github/vudovn/ag-kit/geo-fundamentals/quality
- https://skills-hub.ai/sources/geo-seo ; https://claudeskills.info ; https://playbooks.com/skills/aaron-he-zhu/seo-geo-claude-skills/content-quality-auditor ; https://openskillindex.com ; https://vibeindex.ai ; https://skillselion.com ; https://clawhub.ai/asale-ai/seo-geo-skill
- https://composio.dev/blog/best-marketing-skills ; https://claudefa.st/blog/tools/skills/claude-code-seo-skills

**Hacker News (via Algolia API)**
- https://news.ycombinator.com/item?id=44133279 (a16z GEO thread; ~800-query variability study)
- https://news.ycombinator.com/item?id=46907123 (Ask HN: how ChatGPT decides which sites to recommend)
- https://news.ycombinator.com/item?id=47457472 (Launch HN: Sitefire)
- https://news.ycombinator.com/item?id=41439983 (llms.txt) ; https://news.ycombinator.com/item?id=47274490 (geo-lint) ; https://news.ycombinator.com/item?id=45495087 (GEOfast)

**Reddit (secondary: snapshots and write-ups)**
- https://gummysearch.com/r/GenEngineOptimization ; https://gummysearch.com/r/GEO_chat ; https://gummysearch.com/r/GenEngineOptimizers ; https://gummysearch.com/r/SEO_AEO_GEO/
- https://otterly.ai/blog/reddit-ban-geo-experiment/ ; https://otterly.ai/blog/reddit-geo-ai-search-citations/ ; https://otterly.ai/blog/geo-experiment-year-in-title/
- https://neuronwriter.com/reddit-seo-ai-overview-citations-2026/ (Local SEO Guide Reddit campaign)
- https://promptwatch.com/blog/chatgpt-stop-citing-reddit ; https://promptwatch.com/data/reddit-citations-are-dropping-in-chatgpt
- https://geotoolbox.ai/blog/reddit-seo

**Studies and press on debates**
- llms.txt: https://ahrefs.com/blog?p=198700 ; https://www.senthor.io/en/blog/data-study-llms-txt-vs-reality ; https://redocly.com/blog/llms-txt-still-overhyped
- Schema: https://authoritytech.io/curated/schema-markup-ai-citations-ahrefs-study-2026 ; https://www.danielkcheung.com/musings/schema-ai-citations-evidence-review
- Listicles: https://ahrefs.com/blog/self-promotional-content-ai-seo-experiment/ ; https://peec.ai/blog/self-promotional-listicles-analysis-from-232k-citations ; https://letsdatascience.com/news/self-promotional-listicles-help-competitors-win-ai-search-94bd402d ; https://www.siegemedia.com/conversation/lily-ray-on-ai-slop-geo-and-what-actually-works
- Spam policy: https://ppc.land/google-spam-policies-now-officially-cover-ai-overviews-and-ai-mode-in-search ; https://seosherpa.com/google-just-closed-the-ai-search-loophole-that-gurus-have-been-selling-for-two-years/ ; https://www.hobo-web.co.uk/the-geo-grift-is-over-its-seo/ ; https://blog.on-page.ai/?p=8124 ; https://dejan.ai/blog/ai-spam/
- GEO vs SEO: https://growtika.com/geo-hub/is-geo-just-seo-rebranded ; https://www.searchenginejournal.com/a-little-clarity-on-seo-geo-and-aeo/565522/
- Ecommerce: https://aisearch.similarweb.com/blog/chatgpt-ecommerce/ ; https://community.shopify.com/t/emerging-traffic-source-chatgpt-sessions-across-shopify-stores/574374 ; https://www.zeroclickproject.com/insights/research/chatgpt-shopping-ecommerce-discovery-research ; https://www.aeotable.com/en/blog/chatgpt-shopping-visibility
- B2B/manufacturing: https://studierendenprojekte.wirtschaft.fhnw.ch/view/4922 ; https://www.texta.ai/blog/geo-manufacturing-b2b ; https://thecommerceshop.com/manufacturers/blog/geo-for-b2b-manufacturing-ai-visibility ; https://www.interodigital.com/case-studies/global-industrial/

*Caveat: star counts and many statistics are point-in-time and often come from vendors. Figures attributed to ChatGPT 5.6 and to Aug–Sep 2026 are as reported in the cited repos and articles and were not independently verified.*

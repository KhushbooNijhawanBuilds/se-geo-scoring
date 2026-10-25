# 00 — Internal Source Synthesis (Score Agent deck, GEO Playbook, GEO Functional Toolkit)

Source files: `source-docs/` — *Content GEO Score Agent.pptx* (Oct 2026), *GEO Playbook 1.pdf* (v. 2026-Jun-01), *GEOI Functional Toolkit – Practical Handbook for Partners.pptx* (v1.0, Aug 2026).
Purpose: capture the internal frameworks the Content GEO Score Agent must align with, so external research is layered on top of (not in conflict with) house methodology.

---

## 1. Project scope — Content GEO Score Agent (Stage 1 & 2)

**What it does:** scores content and/or produces recommendations. Three run modes chosen by the user: *GEO score only*, *Recommendations only* (content refresh), *Both*. Recommendations may be generated even when the score is above threshold.

**Inputs it runs on:** content brief file (pre-designed intake sheet), live URL, or bulk review (up to 10 URLs/files at once).

**Recommendation types:** changes to existing content · add/remove suggestions · missing-content gaps.

**Hard scope boundary:** *No technical characteristics reviewed — Tech GEO is not part of this project.* (robots.txt, SSR/CSR, schema code, page speed, canonical, sitemaps = out of scope. The agent may *note* a visible content-level symptom, e.g. "key specs only exist inside an image/PDF", but must not score tech.)

**Score inputs**
| Mandatory | Optional |
|---|---|
| Page type* (predefined list — each launches its own scoring logic) | Target audience (with example) |
| Topic | Specific country |
| Industry | Target AI prompts / questions |
| Buyer-journey stage**: Awareness · Education · Consideration · Evaluation · Decision | |

\*full list to be built · \*\*definitions needed (→ the skill provides draft definitions)

**Additional recommendation inputs:** Mandatory — primary business objective. Optional — known competitor names/pages, target customer/job role, CTA (desired next step).

**Flow:** Owner → score inputs → GEO score → (OK → end) / (needs work → recommendation inputs → recommendations → "more?" loop).

**Page/content types to define (To-Do 01):** PDP · Page range · Page category · CaaS · Editorial page (common logic) · Article-type page (blog or editorial) · Document · … (others TBD).
**To-Do 02:** build logic per page type. **To-Do 03:** content brief intake sheet per page type.

Timeline (from deck): examples of each page type by 16 Oct; 1st logic by 21 Oct; review 22 Oct; remaining logics effort estimate by 27 Oct; weekly status updates.

---

## 2. GEO Playbook — core house frameworks

**Definition.** GEO = making content work for the AI reasoning layer that assembles answers. Parallel to SEO, not a replacement. SEO question: "Can Google find and rank our page?" GEO question: "When AI answers a customer's question, does it mention or recommend us?" Tagline: *AI-ready = accessible, structured, answer-shaped.*

**KPIs.** Visibility Score (foundation; binary present/absent per response) · **Share of Voice** (primary) · **Citation Share** (primary) · Sentiment Score (supporting). North Star = category leadership on SoV + Citation Share vs top competitors across ChatGPT, Gemini, Perplexity, Claude, Copilot.

**Answer engine anatomy.** LLM (generative layer, parametric memory) + Browser (retrieval layer that fetches pages). Pages must be fetchable and content extractable.

**Execution loop.** 1 Setup (topics, prompts, personas, competitors → baseline) → 2 Analyze (visibility, citations, diagnose gaps) → 3 Optimize & Generate (optimize existing, create net-new, measure). Don't skip phases.

**Topic selection — Three-Filter Test:** Commercially significant · Queried · Competitively contested.
**Prompt = Topic × Persona × Stage × Intent.** Stages (playbook): Awareness / Consideration / Decision. Intents: Informational / Comparative / Transactional / Navigational. 15–20 prompts per topic.
Prompt sources: Search Console question queries, predictive text/autosuggest, live AI engine fan-out (e.g. Perplexity sub-queries).

**THE THREE GATES** (diagnostic spine)
| Gate | Question | Checks | In Score-Agent scope? |
|---|---|---|---|
| 1 Fetchable | Can the AI reach & read the page? | robots.txt allows AI bots; no login/form wall; no heavy JS; TTFB <3s; sitemap | **No** (tech) — except content-level gating (key info locked in gated PDF/form) |
| 2 Chosen | Does the page look like the answer before it's opened? | Descriptive URL; title matches query intent (not brand-first); headers align to target prompt; meta description signals utility | **Partially** — title/H1/meta *wording* is content; URL & schema are tech |
| 3 Extractable | Can AI lift a clean, citable chunk? | Key answer in first 100 words; H2/H3 map to fan-out sub-queries; factual density (stats/specs replace adjectives); tables & lists | **Yes — core** |

**Beyond the gates:** map citation supply chain; partner GEO Content Kits; earn third-party coverage; strengthen entity signals (Consensus Principle).

**Query fan-out.** AI expands a seed prompt into sub-queries. Content should (1) answer the seed directly in paragraph 1, (2) cover implied sub-questions via H2/H3, (3) contain specific citable facts. Covering the full fan-out cluster = multiple citation opportunities.

**Generate mindset:** Inverted pyramid · Factual density · Text-first (no key data only in images/video/charts) · Prompt-aligned headers. Against: narrative build-up, marketing fluff ("industry-leading", "innovative"), visual reliance, vague broad coverage.

**FIVE-DIMENSION CONTENT AUDIT** (house rubric)
1. **Relevance** — directly answers the prompt; leads with it.
2. **Factual Density** — concrete stats/specs ("reduces energy consumption by 15%").
3. **Semantic Structure** — headers aligned with fan-out queries.
4. **Recency** — up-to-date info and dates.
5. **Authority** — credible citations: standards (IEC/IEEE), internal whitepapers, verified experts.

**Optimize-existing-page five moves:** Match the prompt in headers · 40–60-word answer paragraph right after heading · Inject factual density · Structural clarity (lists, steps, HTML tables) · Remove the fluff ("if a sentence has no fact, stat or direct answer, consider removing"). *Optimization is often subtraction and restructuring.*

**Answer-shaped paragraph (3 parts):** (1) Subject + primary function, (2) specific citable differentiator, (3) target application/audience.
Example after: "The RM AirSeT is an SF6-free medium voltage switchgear that uses pure air technology, designed for commercial buildings and utilities."

**Citation economy.** ~80% of AI citations from third parties; of that ~50% channel ecosystem (distributors/partners/retailers/integrators), ~30% earned/social/industry media, ~20% owned/competition/other. Consensus Principle: independent corroboration of the same claim.
**Partner GEO Content Kit:** 50–70-word answer-shaped description · HTML spec table (top 8–10 specs) · FAQ pack (3–5 Q&As) · context + canonical link · authority templates.

**Diagnostics.** Visibility-drop protocol (verify drop → check gates → analyze replacement → formulate fix: technical / content / authority). Citation lenses: domain mix, page type & format, competitive rank. Mention-vs-citation gaps: Authority gap (high mention, low citation), Awareness gap (low/low), Positioning gap (cited but framed as secondary). Sentiment root cause: perception / messaging gap / reality gap / hallucination.

**Net-new vs optimize:** format match? density sufficient? gap unanswered anywhere? → "Scalpel Page".
**New Content Brief Template:** Target query · Fan-out cluster (3–5 sub-queries as H2s) · Target audience · Content format · Required facts · Prohibited language · Success criterion (expected AI output). Respect E-E-A-T.

**Technical docs:** HTML-first, PDF-also (HTML gateway page, embed PDF, schema, extract top 5–10 specs to HTML). Stable URLs, descriptive filenames, PDF metadata (title, subject, author, keywords), text-searchable, tagged headings, single column, links back to HTML.

---

## 3. GEO Functional Toolkit — content-type rules & checklists

### Anatomy of a GEO-ready page
Front-loaded quotable answers in top 2–3 components · scannable bullet summaries · authoritative citations/sourcing · conversational human tone · entity & credibility signals (expertise markers, internal cross-links) · (tech GEO in place).

### Universal writing rules (Ch.3)
Answer first · Be extractable (neutral tone, clean headings, structured text, bullets, factual density) · Outcome-led clarity · Clear context & segmentation (who it's for, when used) · Invert the pyramid.
**Banner/hero 4-question test:** if AI reads only the banner, can it explain **What it is · Who it's for · When it applies · What outcome it delivers**? Yes → GEO-ready.
**CTAs:** descriptive & intent-based ("Download the energy management guide"), not "Learn more/Get started"; place after informational sections.
**Short/medium/long object descriptions:** one primary outcome; outcome–solution–timeframe link; scannable bullets for long forms; product & service entities connected.
**Video/image descriptions:** never rely on asset alone; title + 3–4 bullet takeaways; descriptive, not campaign names.
**Gated content:** "Gate the deep dive, not the knowledge" — ungated key findings, definitions, frameworks.
**Dos:** write for answers not campaigns; explicit context; structure for extraction; reuse not persuasion; update every 6–12 months. "Would an AI confidently quote this sentence?"
**Don'ts:** bury meaning in storytelling; assume AI figures it out; hide info in PDFs/gated assets; creative section names; vague value claims.
**GEO Gate before publish:** clear page definition at top · audience & scenario stated · outcomes listed · fact-based & extractable · no critical info behind forms.
**Writing checklist groups:** Answer first · Clear context & segmentation · Outcome-led clarity · Extractable content · Trust & clarity signals (current, verifiable, non-exaggerated, neutral). Final check: 3–4 sentence AI summary must capture what/who/when/outcome.

### Images (Ch.4)
AI reads alt text, surrounding text, captions, filenames. Alt text 80–140 chars, describes purpose in context, no stuffing, unique per variant; explanatory paragraph + caption next to image; descriptive filenames; multimodal (diagrams + comparison tables) helps.

### Videos (Ch.5, Ch.10)
Formats: tutorials, how-to, FAQ, comparisons, case studies, expert insights. Answer within first 30–90 s; chapters (question-style); recap; voice-over; human-reviewed captions (.SRT); fact-based, consistent terminology; no clickbait. Publish on YouTube (descriptive title, 2-paragraph summary + bullets, 300+ word description, link to SE page, chapters starting 00:00, ≥3 timestamps) **and** embed on crawlable SE page (optional HTML transcript). Toolkit's video scoring uses 0–5 per item: video type, title, description, voice-over, subtitles, link to SE page, chapters, publication on SE page.

### FAQ (Ch.6)
Real question as heading; direct answer in first sentence (<25 words), total 40–80 words; lists for steps/specs, tables for comparisons; one entity per answer (no keyword stacking); no hedging ("it depends") when a concrete answer exists; self-contained; one FAQ page per product/topic (no mega-FAQ); reviewed within 90–120 days (3–4-month cycle; immediate on product/policy change). Bad FAQ = marketing filler ending in a CTA.

### Documents (Ch.7)
Lead with the fact (spec first, positioning after) · one topic per heading (descriptive, question-like) · specs in tables (consistent labels/units, one value per cell) · text layer + tagged headings, descriptive filename/title · pair model codes with plain names, define acronyms first use, use customer phrasing ("operating temperature range" not "env. spec") · visible revision date/version, changelog, retire superseded versions · audit twice yearly. 10-point document checklist.

### Blogs (Ch.8)
Core insight in paragraph 1 (intro = summary); context after insight; descriptive, one-idea subheadings mirroring how people ask (not clever); 3–5-bullet key-takeaways block (top or bottom); numbers not superlatives, attributed to named source, cut hedges; name products/standards explicitly, descriptive anchor text, cross-reference posts by title; visible publish + update dates, refresh yearly, retire/redirect stale. 10-point blog checklist.

### Reverse-engineering (Ch.9)
5-step prompt audit: Context (intent, entities, scope, closest page) · Keywords (cited vs our term list) · Tone of voice (formality, perspective, confidence) · Messaging (anchoring facts, structure, proof points, self-containment; extract the single most-quotable sentence) · Sources cited (who, format, authority signals, pattern across 3–5 prompts). E-E-A-T + YMYL awareness (AI answers cite 3–5 sources; weak E-E-A-T = exclusion).

### Social/community (Ch.10), Linking (Ch.11)
Community/social ≈ 25–26% of citation drivers (Profound, Jul 2026); partners/distributors big for B2B. Executive & employee voice > brand voice. Reddit: named, disclosed, helpful participation. Internal links = machine-legible knowledge graph: link by entity to one canonical page, descriptive anchors, hubs open with 40–60-word definition, no orphans. External **mentions** > links; consistent entity naming everywhere.

### UX (Ch.12)
Design for the answer; every page a self-sufficient entry point; modular, independently citable blocks. Query-matched H1–H3 hierarchy (max 3 levels, real semantic tags); paragraphs ≤3–4 sentences; numbered steps; bullets for attributes; tables for comparisons / >2 data dimensions; <strong> key terms; plain language, define jargon, one term per concept; diagrams/tables over narration. Templates: GEO Power Page / GEO Optimized Template / GEO Power Couple. PDP/range/category content often comes from PIM/OfferDAM (not editable in Builder.io) — recommendations must route to the PIM champion.

### Analytics (Ch.13) — existing house scoring
**GEO Strategic Score (prompt prioritization, 0–100):** Competitive Density 25 · Citation Share Potential 25 · Business Impact 25 · Technical Feasibility / E-E-A-T 25.
**GEO Strategic Score — Web Page Assessment (0–5 per component → /5 × 100):** AI Interpretability 30% (tech) · Semantic Richness 25% · Conversational Relevance 20% · Structural Optimization 15% (schema — tech) · Generative Engagement Rate 10% (lagging, observed).
**Bands:** <40 Poor (immediate remediation) · 40–69 Average (backlog) · 70–89 Good (minor tweaks) · 90+ Excellent (internal exemplar).
⚠ Note for the Score Agent: ~45% of this existing page-assessment weight is technical or observational and therefore out of scope → the new content score needs a content-only redistribution. Keep the same 0–100 normalization and the same four bands for continuity.
Prompt-testing log: Mentioned / Cited / Position / Sentiment per prompt × engine × brand.

---

## 4. Implications for the Content GEO Score Agent (from internal sources)

1. Re-use house vocabulary: Three Gates (score Gate 3 fully, Gate 2 wording only), Five-Dimension Audit, answer-shaped paragraph, 4-question hero test, fan-out coverage, Consensus Principle.
2. Re-use house bands (<40 / 40–69 / 70–89 / 90+) and 0–5 component rubric → 0–100 normalization.
3. Page-type-specific checklists already exist for FAQ, Documents, Blogs, Video, Images, object descriptions, CTAs — these become per-type criteria.
4. Missing in internal sources (to fill from external research): PDP / range / category / CaaS-specific logic, buyer-journey stage definitions (5 stages incl. *Education* and *Evaluation*), stage-specific weighting, LLM-as-judge calibration, evidence-backed weights.
5. Recommendations must respect content ownership (PIM/OfferDAM vs Builder.io editorial) and the Optimize-vs-Net-New decision (Scalpel Page + New Content Brief template).

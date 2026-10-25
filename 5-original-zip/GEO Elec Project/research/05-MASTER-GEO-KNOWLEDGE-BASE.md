# 05 — MASTER GEO KNOWLEDGE BASE & Content GEO Score Agent Design Rationale

*Compiled 2026-10-13. This synthesizes reports 00 (SE internal), 01 (academic, about 57 papers), 02 (industry studies and platform docs, about 80 sources), 03 (GitHub/Reddit/Claude skills, 20+ tools) and 04 (content types, scoring tools, LLM-as-judge). The operational version lives in the `geo-research` skill (`skill/geo-research/`).*

---

## Part 1: What we now know about GEO (the 15 truths)

1. **GEO is about the retrieval layer.** Answer engines are an LLM plus a browser. They fan one prompt out into many sub-queries, retrieve pages, score passages and synthesize an answer with citations. Owned content competes at the passage level for sub-questions.
2. **Retrieval gates everything.** In controlled tests, being retrieved and ranked into the model's context beats any content rewrite by roughly 8x (+2.77 vs +0.36 rank). A content score can measure only *citation-readiness given retrieval*. [01, C-SEO Bench]
3. **Relevance is the #1 content factor.** Matching the query's intent and wording has odds ratios above 10,000 in controlled pairwise tests. Headings and titles that mirror the prompt are cited more (41% vs 30%; title similarity 0.60 vs 0.48). [01, 02]
4. **Concrete, verifiable facts win.** Specs, prices, numbers with units, definitions and comparisons are among the strongest selection cues (specs OR 8.6 to over 10,000), and pages with them show 55–62% more absorption. [01]
5. **But "adding statistics or quotes" as a tactic does not replicate.** The famous +30–43% lifts came from GPT-3.5 with the source guaranteed in context. On newer models, 51 of 54 settings were non-significant or negative, and "add statistics" hurt in 19 of 24. *Genuine data helps; decorative data doesn't.* [01]
6. **Freshness is strong and consistent.** A recent visible date has odds ratios of 14 to over 10,000, and a date alone flips up to 25% of reranker preferences. AI-cited content is about 26% fresher than organic results. An old visible date is worse than none. Faking dates is manipulation. [01, 02]
7. **Promotion hurts.** Promotional vs neutral copy has odds ratios up to 362 against promotion. Ad-style rewrites scored −1.82 and storytelling −4.36 on product ranking. Neutral, confident, evidence-backed and internally consistent prose wins. [01]
8. **Self-contained passages are the real meaning of "structure".** Passage independence gives up to +56% factual correctness. Formatting alone, with content held constant, has close to zero causal effect. Structure enables extraction; it isn't a lever by itself. [01]
9. **Answer-first matters.** About 44% of ChatGPT citations come from the first 30% of a page, and cited passages are about 2x more likely to contain a definition. [02]
10. **Focused beats exhaustive in selection.** Pages covering 26–50% of fan-out sub-topics are cited more than "ultimate guides" (sweet spot 500–2,000 words). Depth still beats shallowness, so measure coverage, not length. [01, 02]
11. **Off-site consensus drives recommendation.** Brand mentions correlate with visibility at r = 0.66–0.74, against 0.22 for backlinks. 69–94% of citations come from earned or third-party sources; for SE about 80%, half of it from the channel ecosystem. Being *recommended* needs corroboration elsewhere. [01, 02, 00]
12. **Engines disagree and drift.** 91–96% of citations appear in only one engine, URLs turn over about 67% day to day, and the same brand list repeats under 1% of the time. Measure per engine with 7+ repetitions and control pages. [01, 02]
13. **Myths, as of Oct 2026:**
    - llms.txt as a lever: about 97% of files are never requested.
    - Schema as a citation lever: no lift in a controlled test.
    - Keyword stuffing: −9%.
    - AI-written content penalized: no.
    - Track rank position: no; track visibility rate.
    - Self-promotional "best X" lists: cited, but they recommend others in 69% of cases, and spam updates target them. [02, 03]
14. **Platforms differ.** ChatGPT has the strongest freshness bias, low Google overlap and a Wikipedia lean. AIO is YouTube/Reddit/LinkedIn-heavy, with 38% of citations from the Google top 10. AI Mode favours official category and product pages. Perplexity has the highest Google overlap and a Reddit lean. Copilot follows Bing and the most prescriptive structure guidance. Claude is selective, prefers precise sourced numbers and has a low Reddit share. Gemini favours first-party sites. [02]
15. **B2B industrial is underserved but specific.** 94% of B2B buyers use GenAI, and use-case precision decides whether a vendor gets noticed. 69% of technical buyers use AI, yet only 6% trust the summaries, and datasheets are the most valued content. So: verifiable HTML specs, standards by number, compatibility, lifecycle and documents with HTML summaries. No rigorous manufacturing-specific GEO study exists, so this is inferred. [02, 04]

## Part 2: Where the sources conflict, and how the skill resolves it

| Conflict | Positions | Resolution in the skill |
|---|---|---|
| Is GEO just SEO? | Google: "still SEO", no chunking or special schema. Microsoft: section-level scoring, Q&A, tables, schema. | Shared foundation. Write self-contained sections under descriptive headings, don't fragment pages, and score extractability through self-containment. |
| Statistics, quotes, citations | +28–43% (KDD'24) vs null or negative (C-SEO, NeurIPS'25) | Score the *substance* of evidence (real, relevant, sourced), never decoration. Weight U5 moderately. |
| Structure | Correlational: heavily over-represented in citations. Causal: about null. | U3 rewards self-containment and no-hidden-facts most; formatting alone can't reach level 4. |
| Length | Exhaustive pages win at retrieval vs focused pages win at selection | U6 "coverage and focus": core + 3–5 fan-out questions, without sprawl. |
| Earned vs owned | 84% earned (Muck Rack) vs 86% brand-managed (Yext, local/brand queries) | Owned content wins branded and factual queries; earned wins "best/compare". The content score covers owned content, and off-site advice is given separately. |
| Author bylines | E-E-A-T +31% (correlational) vs "noise" (listicle study) | Score expertise *visible in the content*; a byline counts only as provenance. |
| Q&A/FAQ format | +25% (Semrush) vs about 0 (E-GEO) | Keep FAQ as a format with its own rules, at moderate weight. FAQs are valuable mainly because they match real questions. |

## Part 3: Content GEO Score Agent design decisions (Stage 1 & 2)

| Decision | Choice | Why |
|---|---|---|
| What the score means | Citation-readiness of content (necessary, not sufficient) | Retrieval and off-site factors dominate (C-SEO, Tannenbaum 2026: engine-agnostic scores don't predict discovery). |
| Scope | Content only; technical items become out-of-scope observations | Project rule: "Tech GEO is not part of this project". |
| Scale & bands | 0–5 per criterion → 0–100; <40 Poor · 40–69 Average · 70–89 Good · 90+ Excellent; OK threshold 70 | Continuity with the SE Toolkit GEO Strategic Score. |
| Structure of logic | 10 universal criteria (U1–U10) + type-specific criteria; 13 page types (+ datasheet variant, image module) | Covers every type in the deck's To-Do list plus likely additions (case study, comparison, FAQ, glossary, solution, video). |
| Stage handling | 5 defined stages; multipliers per criterion family, then renormalized | The deck asks for stage definitions. Research shows each stage needs different formats and signals. |
| Judging | LLM judge answers binary checks with verbatim quotes; code computes levels, weights, caps | CheckEval, RULERS, Prometheus; consistency and auditability. |
| Gates & penalties | Contradictions, unanswered primary question, PDP with no specs, unsafe info, clickbait, info only in gated assets/images; penalties for stuffing, fluff, boilerplate, CTA overload, self-ranking, hidden instructions | Stops averaging from hiding deal-breakers. Integrity. |
| Recommendations | Impact points × objective fit ÷ effort; owner tagging (content / PIM / SME); BEFORE→AFTER rewrites; no invented facts; restructure before rewriting | Deck's 3 recommendation types plus the loop. SAGEO shows over-rewriting can hurt retrieval. |
| Calibration | The 5–6 example pages per type (due 16 Oct) become the first gold set; κ ≥ 0.6 target; quarterly outcome validation (≥ 7 runs/prompt, control pages) | Weights are evidence-informed priors and must be calibrated on SE pages. |

## Part 4: Open questions for the team (decide before locking v1)

1. **Threshold:** keep 70 for "Score is OK" for all types, or set it per type (e.g. CaaS blocks 75, documents 65)?
2. **Stage list:** confirm the 5 stages. Should post-purchase/support be a 6th stage for FAQ and manual content?
3. **Page-type list:** confirm the additions (case study, comparison/selection guide, FAQ, glossary, solution page, video). Is "Supercharge Experience Page" a separate type?
4. **Spec completeness:** can the agent access PIM category attribute lists to compute PDP-1 completeness? If not, use the top 8–10 spec heuristic.
5. **Consistency check:** will datasheets or PIM exports be supplied alongside PDPs so the agent can check for contradictions (gate G1)?
6. **Ownership routing:** confirm the owner tags (content owner / PIM champion / SME / SE Digital).
7. **Validation:** can Profound prompt panels be used for before/after validation of scored pages?

## Part 5: File map

| File | Contents |
|---|---|
| `source-docs/` | The 3 source documents |
| `research/00-internal-source-synthesis.md` | SE Playbook, Toolkit and Score Agent deck, distilled |
| `research/01-academic-research.md` | ~57 papers, evidence table, rubric implications |
| `research/02-industry-studies-and-platforms.md` | 30 data-backed findings, platform-by-platform guidance, myths, KPIs |
| `research/03-github-reddit-skillhubs.md` | Open-source rubrics extracted, Claude skill landscape, community insight |
| `research/04-content-types-and-scoring-tools.md` | Per-page-type playbooks, stage × intent, scoring tools, LLM-judge design |
| `research/05-MASTER-GEO-KNOWLEDGE-BASE.md` | This synthesis |
| `skill/geo-research/` | The operational skill (SKILL.md, references, scripts, weights) |

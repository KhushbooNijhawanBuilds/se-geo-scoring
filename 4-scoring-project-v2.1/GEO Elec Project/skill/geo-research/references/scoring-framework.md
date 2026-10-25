# Content GEO Score — Scoring Framework (v2.1, 20 Oct 2026)

**What the score means:** *citation-readiness* of the **content**: how easily an AI answer engine can understand it, trust it, extract it and quote it for the target prompts. It does **not** promise citations. Retrieval rank, off-site consensus and technical access also drive citation, and they are outside this score. Always say this in the report.

**Scope:** content only. Technical GEO is out of scope for the Score Agent: robots.txt, SSR/CSR, schema code, speed, canonicals, sitemaps, llms.txt. Content decisions that block extraction (key facts only in an image, PDF, collapsed tab or gated form) **are** in scope. Score them under U3. Flag anything technical as *"Out-of-scope observation → route to SE Digital"* and never score it.


**v2.0 rules (SE Content GEO Scoring Standard):**
- **What is scored: the rendered page content.** That means what a visitor sees after load, including web-component (shadow DOM) text, same-origin iframes and collapsed tabs, marked `[hidden]`. Key facts that exist *only* in hidden tabs, carousels, tool panels or video still fail U3 c5.
- **Crawler gap.** If server-HTML words ÷ rendered words < 0.7, or the H1, primary outcome or key facts are missing from the server HTML, report "Crawler gap → SE Digital". Show the server-HTML score alongside. This is not part of the score.
- **v2.1 level rules:** the anchors in §2 (e.g. "3 = c1+c2") and the caps written into criterion text are applied **in code** from the binary checks; halves round up. See `judge-protocol.md` §3.
- **Score name:** report this as the **Content GEO Score**. It is not comparable with the Toolkit's GEO Strategic Score, which is about 45% technical.
- **Gate registry G1–G13, penalties (incl. `template_artifact`, `superseded_no_notice`), U4 c2 thresholds per type and template-vs-author tagging** are defined in `page-types-v2.md` §0 and `assets/weights.json`. These take precedence over §4 below where they differ.

---

## 1. Scale and formula (aligned with the SE Toolkit's "GEO Strategic Score")

Each criterion is graded **0–5** with anchored descriptors:

| Level | Label | Meaning |
|---|---|---|
| 0 | Absent | Not present at all, or contradicts the requirement |
| 1 | Very weak | Token presence; would not be extracted |
| 2 | Weak | Present but buried, vague or incomplete |
| 3 | Adequate | Meets the basic requirement; extractable with effort |
| 4 | Strong | Clear, specific, well placed; likely to be lifted as-is |
| 5 | Exemplary | Best-in-class; needs exceptional evidence (original data, complete specs, named experts) |

```
Raw score   = Σ (level_i / 5 × effective_weight_i)          # effective weights sum to 100
Final score = Raw score − penalties, then caps applied        # 0–100
```

**Effective weights** = page-type default weight × stage multiplier (see `buyer-journey.md`), **renormalized to 100**.

**Bands** (same as the SE Toolkit, for continuity):

| Score | Band | Action |
|---|---|---|
| < 40 | Poor | High priority, immediate remediation |
| 40–69 | Average | Needs improvement; add to optimization backlog |
| 70–89 | Good | Well optimized; minor tweaks |
| 90+ | Excellent | Best-in-class; use as internal exemplar |

**Calibration intent:** a typical un-optimized page should land at 35–60, and 90+ should be rare. If most pages score above 70, the judge is too lenient. Tighten the evidence requirements.

**Threshold for "Score is OK"** (Score Agent flow): default **70**. The business can set it per page type.

---

## 2. Universal criteria (U1–U10)

Every page type uses a subset of these, with its own weights. Each criterion is decided by **binary sub-checks**: the judge answers pass/fail with a verbatim quote, then maps the checks to a level using the anchors.

### U1 — Answer-first & prompt alignment
*Does the page lead with the answer, and does its wording signal the target prompt?* Covers the house Gate 2 at content level (title/H1/meta **wording** only) and the inverted pyramid.
- c1 First 1–2 sentences under the H1 (or the first 100 words) directly answer the primary question or define the subject.
- c2 Title/H1 wording matches the intent of the target prompt (descriptive, not brand-first or clever).
- c3 The key message sits in the top 2–3 components (hero/banner/intro), not below the fold.
- c4 Each major H2 section opens with a 1–2 sentence direct answer (40–60-word answer paragraph).
- c5 A summary / key-takeaways block exists where the format allows.
- Anchors: 0 the question is never answered · 1 answered only deep in the page · 2 answered within ~150 words but vague or hedged · 3 c1+c2 · 4 c1–c4 · 5 all five, and the opening could be quoted verbatim as the answer.
- Evidence: ~44% of ChatGPT citations come from the first 30% of a page. Cited titles are more similar to the prompt (0.60 vs 0.48). Heading–query match gives a 41% vs 30% citation rate.

### U2 — Context clarity: What / Who / When / Outcome
*SE Toolkit 4-question test: if an AI reads only the top block, can it explain what this is, who it is for, when it applies and what outcome it delivers?*
- c1 What it is: explicit definition or category ("X is a …").
- c2 Who it is for: role, segment or industry named.
- c3 When it applies: scenario, trigger or application named.
- c4 Outcome: concrete result stated, owned by the solution (not "helps you…").
- Anchors: number of checks passed (0→0, 1→1, 2→2, 3→3, 4→4). Give 5 only if all four are in the first block **and** the outcome is quantified.

### U3 — Extractable structure & self-containment
*Can an engine lift a clean chunk? Includes content-level blockers.*
- c1 Descriptive H2/H3s, one idea per heading, ideally phrased as the question a buyer asks. No "Overview", "The Power of Change" style labels.
- c2 Lists for features and attributes, numbered steps for procedures, HTML-text tables for specs and comparisons (>2 data dimensions).
- c3 Paragraphs ≤ 3–4 sentences. No walls of text.
- c4 Sections stand alone: subjects named, no "as mentioned above", "this product", or "our solution" without the name.
- c5 No critical info only in an image, video, PDF, carousel, collapsed tab or gated form (content decision → content scope).
- Anchors: 0 wall of text or image-only · 1 headings exist but are generic · 2 some descriptive headings, few lists · 3 c1+c2+c3 · 4 + c4 · 5 all five, and every section is quotable on its own.
- Rule: if c5 fails for **key** facts, U3 ≤ 2.
- Evidence: *self-containment* is the part with causal support: passage independence gave up to +56% factual correctness in RAG (HOPE 2025). Formatting alone (structured vs dense text, same content) has about zero causal effect in controlled tests. So weight c4/c5 most, and treat c2/c3 as enablers. Never give level 4+ for formatting without self-contained, fact-bearing sections.

### U4 — Factual density & specificity
*Facts instead of adjectives.*
- c1 Key claims are quantified (numbers with units, ranges, timeframes, conditions).
- c2 Density: ≥ 2.0 quantified facts per 100 words for product/technical types; ≥ 1.0 for editorial types (article, news, solution, service, case study, hubs, glossary). Count genuine facts only; a repeated number counts once.
- c3 No unanchored superlatives or marketing abstractions ("innovative", "industry-leading", "next-gen", "seamless", "designed to help").
- c4 Precise terminology plus the customer-facing synonym (model code + plain name; acronyms defined at first use).
- c5 Outcomes are specific ("reduces peak demand charges by 10–15%"), not generic ("significant savings").
- Anchors: 0 generic claims only · 1 few numbers, no units · 2 some key claims quantified · 3 c1+c3 · 4 c1–c4 · 5 all five, dense and verifiable.
- Evidence: concrete specs and prices are among the strongest selection cues (odds ratios 8.6 to over 10,000; SIGIR 2026). Pages with numbers, definitions and comparisons show 55–62% more absorption into answers. **But** decorative or injected statistics hurt: "add statistics" lowered rank in 19 of 24 C-SEO Bench settings. Score **genuine, relevant, verifiable** facts only. A number that is generic, off-topic or unsourced is not a pass. Microsoft: "42 dB, not 'quiet'".

### U5 — Evidence, attribution & expertise (E-E-A-T in the content)
- c1 Statistics attributed to a named source with a year.
- c2 Standards and regulations cited by number (IEC 60947-2, UL 489, IEC 61850, IEC 62443…).
- c3 ≥ 1 attributed expert or customer quotation (where the format allows).
- c4 First-party or original evidence: test results, field data, deployments, case metrics, with method or conditions.
- c5 Provenance: named author, reviewer or owner, or clear organizational accountability for technical/safety content (YMYL-adjacent). Expertise is *visible in the content*.
- Anchors: 0 no sources · 1 vague ("studies show") · 2 ≥ 1 source · 3 c1+c2 · 4 c1–c4 (any 4) · 5 all five.
- Evidence: quotation addition +43% and cite sources +28% in the original GEO paper (GPT-3.5, source guaranteed in context; biggest gains for lower-ranked sources). These are **contested** on newer models (about 0 in C-SEO Bench), and LLMs largely ignore credibility *style* cues (ACL 2024). Evidence-backed vs unsupported claims still win pairwise (odds ratios 2–46). Semrush links E-E-A-T signals to +31%. Score **substance**: is the claim actually backed? Decoration does not count. A byline alone is unproven; score expertise shown in the content.

### U6 — Fan-out coverage & focus
*Does the page answer the seed prompt AND its 3–5 most likely sub-questions, without sprawl?*
- c1 The seed/target prompt is answered (take it from the input; otherwise infer it from topic + stage).
- c2 Most of the 3–5 predicted fan-out sub-questions have a dedicated section or answer.
- c3 One primary intent. Adjacent intents are linked out, not crammed in.
- c4 Covers the facts a buyer at this stage needs (an expected-facts checklist for the page type).
- Anchors: 0 off-topic · 1 < 50% of core facts · 2 core facts but misses key sub-questions · 3 c1+c2 · 4 c1–c4 · 5 c1–c4 plus anticipates the follow-on prompt (next step in the conversation chain).
- Evidence: pages covering 26–50% of fan-out sub-topics are cited more than exhaustive ones. Sweet spot is about 500–2,000 words for most editorial pages.

### U7 — Neutral, non-promotional tone
- c1 Informational, expert voice (an advisor, not a brand talking about itself).
- c2 Balanced: trade-offs, limitations or "when not to use / when to choose another option" are present.
- c3 No hype, no clickbait, and no stacked CTAs inside informational sections.
- c4 Competitors and alternatives are named fairly where relevant (comparison or selection content).
- Anchors: 0 pure sales copy · 1 mostly promotional · 2 mixed · 3 c1+c3 · 4 + c2 · 5 all four (or c4 N/A) and reads like a reference source.
- Evidence: AutoGEO's cross-engine rule set includes "neutral, non-promotional tone". Self-promotional "best-of" lists get cited but recommend others (69%). Stage matters: promotion hurts most at Awareness/Consideration.

### U8 — Entity clarity & consistency
- c1 Products, ranges, standards and the brand are named explicitly and consistently (one canonical name per entity, ™ usage consistent).
- c2 Identifiers present where relevant (reference/SKU, model code, standard numbers).
- c3 No internal contradictions (prose vs spec table, block vs page, page vs linked datasheet if provided).
- c4 Descriptive anchor text names the destination entity ("See the guide to sizing a commercial microgrid", not "click here").
- Anchors: 0 ambiguous or contradictory · 1 inconsistent naming · 2 consistent naming · 3 c1+c2 · 4 c1–c3 · 5 all four.
- **Gate:** any factual contradiction → U8 = 0 and the overall score is capped at 59.

### U9 — Freshness & currency
- c1 Visible publish/update date or revision/version (documents: Rev. X, date, changelog).
- c2 Facts, statistics and standard editions are current (no superseded editions or discontinued products presented as current).
- c3 Lifecycle status stated where relevant (active / end-of-life / replaced by a named successor).
- c4 Content updated within the cadence for its type (FAQ 90–120 days, blogs ≥ yearly, docs twice a year, competitive pages quarterly).
- Anchors: 0 visibly outdated · 1 undated with stale references · 2 dated but stale · 3 c1+c2 · 4 c1–c3 · 5 all four.
- Note: never recommend changing a date without a substantive update. Fake freshness is manipulation.
- Evidence: recency is one of the strongest, most consistent cues. A recent vs old timestamp has odds ratios of 14 to over 10,000 across 6 LLMs, and a date alone reversed up to 25% of reranker preferences. An **old visible date is worse than no date**, so only show dates you maintain.

### U10 — Journey-stage fit & next step
- c1 Content type and depth match the declared stage (see `buyer-journey.md`, stage signals).
- c2 Language matches the declared audience/job role.
- c3 Next step (CTA) is descriptive and intent-based ("Download the RM AirSeT selection guide"), placed after informational sections, and fits the stage and business objective.
- c4 Links to the logical next-stage content (e.g. guide → range → PDP).
- Anchors: 0 wrong content for the stage · 1 largely mismatched · 2 fits the stage · 3 c1+c2 · 4 c1–c3 · 5 all four.

---

## 3. Type-specific criteria

These are defined in `page-types.md` (PDP-x, RNG-x, CAT-x, BLK-x, ART-x, DOC-x, CS-x, CMP-x, FAQ-x, GLO-x, SOL-x, VID-x). Each has 3–6 binary checks and the same 0–5 anchoring logic: checks passed → level, with 5 reserved for exceptional evidence.

---

## 4. Gates (caps) and penalties

**Caps.** These are applied after the weighted sum, and the lowest cap wins.

| ID | Trigger | Effect |
|---|---|---|
| G1 | Factual contradiction inside the content, or between content and a provided spec/datasheet | U8 (or BLK-4 for CaaS) = 0; overall ≤ 59 |
| G2 | Primary question/subject never answered or defined anywhere (U1 = 0 **and** U2 ≤ 1) | overall ≤ 39 |
| G3 | PDP / datasheet with no quantified specs in text | overall ≤ 40 |
| G4 | Misleading or unsafe technical/safety statement | overall ≤ 39; escalate to human SME |
| G5 | Title/H1 promises something the content does not deliver (clickbait / intent mismatch) | overall ≤ 49 |
| G6 | Core content only in a gated asset / image / PDF with no HTML text equivalent | U3 ≤ 2 and overall ≤ 59 |

**Penalties** (deduct from the raw score, max −10 total):

| Signal | Deduction |
|---|---|
| Keyword or question stuffing (repeated phrasings, unnatural repetition) | −3 |
| Superlative/fluff density high (script: > 1.5 per 100 words) | −2 |
| Boilerplate repeated across pages > 40% of the text (CaaS/PDP families, when known) | −2 |
| Vague CTA overload (≥ 3 "Learn more / Read more / Get started" style CTAs) | −1 |
| Self-ranking "best X" with own brand #1 and no transparent criteria | −3 |
| Hidden or LLM-directed instructions in the text | −10 + flag |

---

## 5. Confidence and N/A handling

- Mark a check **N/A** only when the format makes it impossible (e.g. quotes in a 40-word CaaS block). N/A checks are removed from the denominator of that criterion's mapping. They are **not** counted as passes.
- If a criterion has > 50% N/A checks, drop the criterion and redistribute its weight proportionally.
- **Missing evidence = fail.** Never infer from brand reputation, "likely" content, or what the page "probably" has elsewhere.
- Confidence per criterion: *high* (clear quotes), *medium* (partial content, e.g. a brief rather than a live page), *low* (content truncated or unrenderable). Report the overall confidence. If more than a third of the weight is at low confidence, say the score is indicative only.

---

## 6. Score-only output (what the agent returns)

1. Header: page, page type, stage, topic, industry, target prompt(s), date, input mode (URL / brief / file).
2. **Content GEO Score: NN/100: Band**, and confidence.
3. Criterion table: ID · criterion · weight (effective) · level 0–5 · points · one-line rationale · key evidence quote.
4. Gates triggered and penalties applied.
5. Top 3 strengths, top 5 gaps (ordered by points lost).
6. Out-of-scope observations (tech), not scored.
7. Disclaimer: "Citation-readiness of content only; actual AI citation also depends on retrieval, off-site consensus and technical access."

For the full judge protocol and JSON schema see `judge-protocol.md`.

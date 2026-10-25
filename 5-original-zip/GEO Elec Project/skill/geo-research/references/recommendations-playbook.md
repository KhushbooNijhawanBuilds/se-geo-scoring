# Recommendations Playbook (v1.0)

Recommendations are produced in **Recommendations-only** or **Both** mode. They are allowed even when the score is above the threshold. Three types (Score Agent deck): **(A) changes to existing content · (B) add/remove · (C) missing content (gaps)**.

## 1. Extra inputs used
- **Mandatory:** primary business objective (e.g. awareness on a topic, leads, distributor sell-through, support deflection).
- **Optional:** competitor names/pages · target customer / job role · CTA (desired next step).
- If competitor pages are provided, run the **5-step reverse-engineering audit** (§5) on them and turn the differences into recommendations.

## 2. Prioritization (deterministic)

```
impact_points = (5 − level) / 5 × effective_weight       # points recoverable for that criterion
priority      = impact_points × objective_fit / effort
  objective_fit: 1.5 if the fix directly serves the stated business objective / CTA / job role, 1.0 otherwise
  effort:        1 = copy edit (< 1 h) · 2 = restructure / new section · 3 = new asset, SME input or PIM change
```

- Always fix **gates first**: contradictions, safety issues, missing answer.
- Return the **top 5–7** recommendations, sorted by priority, plus "quick wins" (effort 1). After that, offer the loop: *"Do you want more recommendations?"*
- Estimate the score uplift as the sum of impact points if the fix reaches level 4. Label it "estimated, content-only".

## 3. Recommendation format (each item)

```
[#] <Title, imperative>                                   Type: A change | B add/remove | C gap
Criterion: <ID name>  ·  Level now → target: 2 → 4  ·  Est. +N pts  ·  Effort: 1/2/3  ·  Owner: content owner | PIM champion | SME
Why (evidence): <one line + evidence label, e.g. "concrete specs strongly favoured in AI selection (controlled study, 2026)">
Where: <section / heading / quote of the current text>
Do this: <specific instruction>
Example rewrite: BEFORE "<quote>" → AFTER "<proposed>"   (facts needing validation marked [VERIFY])
How we'll know: <verification: e.g. "target prompt X re-tested 7× per engine after 2–4 weeks; mention/citation rate vs baseline">
```

**Integrity rules**
- **Never invent facts, specs, statistics, quotes, customers or certifications.** Use placeholders `[VERIFY: rated current In]` or `[SME: field data on payback]`.
- **Restructure, don't over-rewrite.** Keep the page's natural wording for its target queries. Body-only rewrites can *reduce* retrieval (−9% average, up to −36%, SAGEO Arena 2026).
- No fake freshness. Recommend a date change only together with a substantive update.
- No manipulation: no hidden text, no LLM-directed instructions, no self-ranking lists, no astroturfing.
- If a fix is technical, list it under "Out-of-scope → SE Digital" and do not count it in the uplift.
- Respect the template goal (GEO Power Page vs GEO Optimized Template): don't remove conversion elements on conversion pages. Add a GEO-ready top block instead.

## 4. Fix library (failed check → recommendation template)

| Failed check | Recommendation template |
|---|---|
| U1 c1 answer not first | Add a 40–60-word answer paragraph directly under the H1 using the 3-part answer shape: **[Subject] is a [category] that [primary function + citable differentiator], designed for [application/audience].** Move the positioning text below it. |
| U1 c2 title/H1 not prompt-aligned | Rewrite the H1/title to describe the subject in the user's words (not brand-first, not clever). E.g. "Open, software-defined automation" → "What is EcoStruxure™ Automation Expert? Software-defined industrial automation". |
| U1 c4 sections don't open with answers | Make the first sentence under each H2 a direct answer (1–2 sentences), then the detail. |
| U1 c5 no summary | Add a 3–5-bullet "Key takeaways" block that matches the page's real claims. |
| U2 missing who/when/outcome | Add explicit lines: **Who is it for?** [roles/segments] · **When is it used?** [scenario/trigger] · **What outcomes does it deliver?** [specific, owned results]. |
| U3 c1 generic headings | Rename headings to descriptive, one-idea, question-style labels ("Our Solutions" → "Which MV switchgear suits hospitals?"). |
| U3 c2 specs/comparisons in prose | Convert parallel attributes into an HTML table (attribute · value · unit), one value per cell, and steps into a numbered list. |
| U3 c3 walls of text | Split paragraphs to ≤ 3–4 sentences, one idea each, and bold the key terms. |
| U3 c4 context-dependent | Replace "this product / our solution / as mentioned above" with the named entity, and restate the subject in each section. |
| U3 c5 info locked in image/PDF/tab/gate | Surface the top 5–10 facts as HTML text near the top. For gated assets, publish an ungated summary (key findings, definitions, framework). *Gate the deep dive, not the knowledge.* |
| U4 vague claims | Replace each adjective claim with a measurable fact and its condition. "highly efficient" → "reduces energy loss by [VERIFY]% under [condition]". Delete sentences that contain no fact, stat or direct answer. |
| U4 codes without names | Pair codes with plain names and define acronyms at first use. |
| U5 unsourced stats | Attribute each statistic to a named source and year, and cite standards by number. Remove stats that can't be sourced. |
| U5 no expert/first-party evidence | Add one attributed quote from a named SE expert or customer [SME] and one first-party data point (test, deployment, field data) with its method. |
| U6 fan-out gaps | Add H2 sections for the missing sub-questions: [list derived from target prompt]. Each gets a direct answer + facts. If a sub-question needs its own depth, recommend a **Scalpel Page** (Type C) and link to it. |
| U6 sprawl / multiple intents | Split secondary intents into linked pages. Keep one primary intent. |
| U7 promotional tone | Rewrite in an advisor voice. Remove hype ("innovative, cutting-edge, world-class"). Add trade-offs and "when to choose another option". Keep CTAs out of informational sections. |
| U8 inconsistent names / contradictions | Standardize on the canonical entity name. Align prose values with the spec table and datasheet. Replace "click here" with descriptive anchors that name the destination. |
| U9 undated / stale | Add a visible "Published / Last updated" date (documents: Rev. N, date, changelog). Refresh stats, standard editions and product status. Mark or retire superseded content. Set the review cadence for the type. |
| U10 stage mismatch / weak CTA | Align depth to the stage (see buyer-journey §2). Replace vague CTAs with descriptive, intent-based ones placed after the informational sections, aligned to the stated CTA/business objective. Link to the next-stage content. |
| PDP-1 spec gaps | Complete the spec table to the category's attribute set (list of missing attributes). Owner: PIM champion. |
| PDP-2 no applications | Add ≥ 3 application noun phrases with environment/conditions, plus "not suitable for…". |
| PDP-3 no compatibility | Add a "Compatible with" section: accessories, complementary products, protocols, successor/predecessor refs, each linked. |
| PDP-5 no Q&A | Add 3–5 product Q&As from support/sales/prompt research. Answer first (< 25 words), 40–80 words total, product named. |
| PDP-8 lifecycle missing | State the lifecycle status and the named substitute. Add where-to-buy/availability. |
| RNG-1 / CAT-2 no comparison table | Add a variant/type comparison table with decision attributes and a "best for" column. |
| CAT-1 no selection criteria | Add a "How to choose a [category]" block with 4–8 criteria, each with thresholds and units. |
| BLK-1 not self-contained | Name the subject inside the block and apply the banner test (what / who / when / outcome). |
| BLK-3 / BLK-9 vague object description | Rewrite as one primary outcome + solution + timeframe ("By implementing [named module], [customer] reduced energy costs by 15% in six months"). |
| BLK-8 / CTA vague | "Learn more" → "Read the [named] case study" / "Download the [named] guide". |
| DOC-1 no gateway | Create an HTML gateway page: title, 100–200-word abstract, top 5–10 specs/findings as table/bullets, questions answered, version/date, download link. |
| DOC-7 no version | Put "Rev. N – updated Month YYYY" on the cover and footer, add a changelog, retire superseded editions. |
| FAQ-2 answer not first / filler | Rewrite: direct answer in the first sentence, then the supporting detail and the next step. Never end with a CTA instead of an answer. |
| CS-3 results not quantified | Lead with one primary quantified outcome, its baseline and timeframe, and state how it was measured. |
| CMP-3 one-sided comparison | Add honest trade-offs and "choose [alternative] if…", and source competitor data. |
| VID-5/6 no transcript/chapters | Upload a human-reviewed .SRT and add question-style chapters (00:00 start, ≥ 3). Write a 300+-word description with a link to the SE page. |

## 5. Competitor reverse-engineering (SE Toolkit Ch. 9: 5-step prompt audit)

For each competitor or cited page vs the SE page, fill in:

| Dimension | Observed in cited content | Gap on our page | Optimization action |
|---|---|---|---|
| Context: intent, entities, scope | | | |
| Keywords: their terms vs ours (two-column term list) | | | |
| Tone of voice: formality, perspective, confidence | | | |
| Messaging: anchoring facts, structure, proof; *the single most-quotable sentence* | | | |
| Sources: who is cited, format, authority signals, pattern across 3–5 prompts | | | |

Then turn each gap into a recommendation using the format in §3. Do not copy competitor text. Benchmark the approach only.

## 6. Optimize vs net-new (Playbook "Scalpel Page")

Recommend **net-new content (Type C)** when the answer to any of these is no:
1. **Format match?** The winning format for the prompt (listicle, comparison, guide, FAQ) differs from this page's type.
2. **Density sufficient?** The facts can't be added here without hurting UX or the page's goal.
3. **Gap answered anywhere?** A high-value sub-query is unaddressed on the domain.

Deliver a **New Content Brief** (target query · fan-out cluster 3–5 H2s · target audience · format · required facts · prohibited language · success criterion = expected AI output · E-E-A-T requirements · stage · CTA).

## 7. Off-page context (advise, never score)

If relevant to the objective, add a short "Beyond this page" note:
- Partner GEO Content Kit: 50–70-word answer-shaped description, HTML spec table of the top 8–10 specs, 3–5 FAQ pairs, canonical link.
- Earned/third-party corroboration (trade press, analysts, standards bodies, distributors, reviews).
- Consistent entity naming across se.com, partner pages, LinkedIn and Wikidata.
- YouTube with transcript and chapters.

About 80% of AI citations come from third-party sources (SE Playbook), so content-only fixes have a ceiling.

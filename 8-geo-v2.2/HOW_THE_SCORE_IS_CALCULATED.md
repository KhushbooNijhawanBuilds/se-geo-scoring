# How the Content GEO Score is calculated (v2.2)

The score answers one question: how easy is it for an AI assistant (ChatGPT, Copilot, Google AI, Perplexity, Gemini, Claude) to understand, trust and quote this page for a buyer's question? It runs from 0 to 100.

The AI judge never produces the number. It only answers yes/no checks and quotes the page as proof. The calculator (`engine/geo_score_calc.py`) does all the maths, so the same answers always give the same score.

## The five steps

| Step | What happens | Who does it |
|---|---|---|
| 1. Checks | Each criterion has 3–6 yes/no checks. Every "pass" needs a verbatim quote from the page. A few absence or layout checks (e.g. "no contradictions") accept a judge note instead. Missing evidence counts as fail. | AI judge |
| 2. Level 0–5 | The calculator turns ticks into a level (below). | Calculator |
| 3. Weights | Each page type has its own criteria and base weights (sum 100). Each criterion belongs to a family; the buyer's stage multiplies each family; the weights are then rescaled to sum to 100. | Calculator |
| 4. Raw score | points = level ÷ 5 × weight, summed over all criteria. | Calculator |
| 5. Final score | raw − penalties (max −10), then capped by the lowest deal-breaker (gate) that fired. | Calculator |

```
raw   = Σ (level_i ÷ 5 × weight_i)
final = round( min( lowest gate cap , raw − penalties ) )
```

Bands: **90+ Excellent · 70–89 Good ("Score is OK") · 40–69 Average · below 40 Poor.** A score within 3 points of 40, 70 or 90 is borderline: run 3 independent judgements and take the median.

## Step 2 in detail: from ticks to a level (changed in v2.2)

For each criterion, n = number of pass + fail checks (na is ignored), p = number of passes.

1. **Drop rule:** if more than half the checks are na, the criterion is dropped and the other weights are rescaled to 100.
2. **Ceiling:** 5 if p = n, otherwise min(4, round-half-up(5 × p ÷ n)).
3. **Anchor floor:** for most shared criteria, passing the core checks guarantees at least level 3 or 4 (e.g. U1 is at least 3 when c1 and c2 pass).
4. **Caps:** written limits, e.g. key facts only in an image → structure (U3) max 2; no visible date → freshness (U9) max 1; no takeaways block → ART-1 = 0.
5. **Gate effects** on levels are applied last (e.g. a contradiction sets entity clarity U8 to 0).
6. **v2.2 level rule:** the level is the ceiling after floors and caps. The judge may only propose a lower level with a `downgrade_reason` that names a weak check of that criterion; otherwise its proposal is ignored. (v2.1 let the judge pick freely below the ceiling, which was the biggest source of drift between runs.)
7. **Missing block = fail (v2.2):** when a block is absent (no takeaways, no comparison table, no sections), its dependent checks count as fail, not na, so a missing block can't drop its own criterion.

Example: "Answer up front" on a blog has 5 checks; 4 pass. Ceiling = min(4, round(5 × 4/5)) = 4. At the Education stage the criterion weighs 15.77, so it earns 4 ÷ 5 × 15.77 = 12.6 points; 3.2 points are left to win.

## Step 3 in detail: weights by page type and buyer stage

There are 26 page-type keys (blog `article`, `news`, `solution`, `service`, `service_project`, `range`, `software_product`, `software_hub`, `software_trial`, `case_study`, `calculator`, `whitepaper_gateway`, `whitepaper_doc`, `esg_hub`, `esg_report`, `esg_report_doc`, `pdp`, `category`, `caas`, `editorial`, `document`, `datasheet`, `comparison`, `faq`, `glossary`, `video`). Each has its own criteria and base weights in `engine/weights.json`, documented in `GEO_Scoring_Standard_All_Types_v2.2.md`.

Every criterion belongs to one family. The stage multiplies the family:

| Family | Awareness | Education | Consideration | Evaluation | Decision |
|---|---|---|---|---|---|
| Answer and definition | 1.4 | 1.3 | 1.0 | 0.9 | 0.9 |
| Evidence | 1.2 | 1.4 | 1.1 | 1.0 | 0.8 |
| Follow-up coverage | 1.2 | 1.3 | 1.1 | 1.0 | 0.8 |
| Tone | 1.4 | 1.3 | 1.2 | 1.0 | 0.7 |
| Comparison | 0.6 | 0.9 | 1.5 | 1.4 | 1.0 |
| Specs | 0.7 | 0.9 | 1.1 | 1.5 | 1.3 |
| Proof | 0.7 | 0.9 | 1.2 | 1.4 | 1.2 |
| Commercial / next step | 0.5 | 0.6 | 0.9 | 1.1 | 1.5 |
| Freshness | 1.0 | 1.0 | 1.1 | 1.1 | 1.2 |

effective weight_i = base_i × multiplier(family_i, stage) ÷ Σ(base × multiplier) × 100

Blog example: answer-first (U1) base 14 → 17.85 at Awareness, 12.07 at Evaluation; facts (U4) base 10 → 6.38 at Awareness, 14.37 at Evaluation.

The stage is chosen by a written test for each page type (v2.2), or supplied by the user.

## Step 5 in detail: penalties and deal-breakers

**Penalties** (subtracted from the raw score, total capped at −10; hidden instructions can exceed the cap and raise a flag):

| Penalty | Points |
|---|---|
| Hidden or AI-directed instructions in the text | −10 + flag |
| Keyword or question stuffing | −3 |
| Self-ranking "best X" list with own brand first, no criteria | −3 |
| Outdated edition with no notice or link to the current one | −3 |
| Fluff: more than 1.5 superlatives per 100 words | −2 |
| Boilerplate shared with sibling pages (over 40%) | −2 |
| Template artifact: placeholder text, widget errors, a section rendered twice | −2 |
| 3 or more vague CTAs ("Learn more") | −1 |

**Gates (deal-breakers)** cap the final score; the lowest cap wins:

| Gate | Cap | Applies to |
|---|---|---|
| G1 Material factual contradiction (also zeroes U8) | 59 | all |
| G2 Main question never answered or subject never defined | 39 | all |
| G3 Product/datasheet with no quantified specs in text | 40 | pdp, datasheet |
| G4 Misleading or unsafe technical/safety statement (expert review) | 39 | all |
| G5 Title/H1 promise not delivered | 49 | all |
| G6 Core content only in an image, video, PDF, gated asset or widget (U3 max 2) | 59 | all |
| G7 Dated content with no visible date | 59 | article, news |
| G8 Case study with no quantified customer outcome | 59 | case_study |
| G9 Calculator with no method, assumptions or example in text | 39 | calculator |
| G10 Range page with no rating, capacity or size with a unit | 49 | range |
| G11 Software page with no deployment, integration, security or licensing facts | 49 | software |
| G12 Service page with no deliverable and no service-level fact | 40 | service |
| G13 Thin page: fewer than 3 substantive facts (tone and consistency max 2) | — | all |

## Worked example: an SE blog that scores 81

"Data center community opposition: how cooling design affects water, noise and permitting" (blog.se.com, October 2026), blog `article`, Consideration stage, judged under v2.2.

| Criterion | Ticks | Level | Weight | Points | Left to win |
|---|---|---|---|---|---|
| U5 Proof and expertise | 3/5 | 3 | 12.54 | 7.52 | 5.02 |
| U3 Easy to scan | 3/5 | 3 | 7.60 | 4.56 | 3.04 |
| U1 Answer up front | 4/5 | 4 | 13.30 | 10.64 | 2.66 |
| U4 Facts, not hype | 4/5 | 4 | 10.45 | 8.36 | 2.09 |
| ART-3 Original insight | 4/5 | 4 | 10.45 | 8.36 | 2.09 |
| ART-2 Title and headings | 4/5 | 4 | 6.65 | 5.32 | 1.33 |
| U9 Up to date | 3/3 | 4* | 5.22 | 4.18 | 1.04 |
| ART-1 Key takeaways | 4/4 | 4* | 4.75 | 3.80 | 0.95 |
| U8 Consistent names | 3/3 | 4* | 3.80 | 3.04 | 0.76 |
| U6 Follow-up questions | 4/4 | 5 | 10.45 | 10.45 | 0 |
| U7 Neutral tone | 3/3 | 5 | 7.98 | 7.98 | 0 |
| U10 Right depth, next step | 3/3 | 5 | 6.84 | 6.84 | 0 |
| **Total** | | | **100** | **81.1** | |

\* All checks passed but the judge lowered the level to 4 with a named reason: U9 "only a publication date, no visible 'Updated' date"; ART-1 "no takeaway carries a number"; U8 "no product codes".

Raw 81.1 − penalties 0, no gates → **81, Good**.

## Run it yourself

```bash
python3 engine/geo_score_calc.py --judge test-run/judge/02.json
```

`--rules v2.1` reproduces the v2.1 level logic exactly (all 60 pilot scores).

## Validation

- All 26 prompts' weight tables match the calculator at all 5 stages.
- 60 SE inventory pages (10 types) scored three times: v2.1 pilot, v2.1 per-type prompts, v2.2. v2.2 vs the previous run: 55 of 62 within 10 points, average +3.7. Results: `test-run/GEO_v2.2_vs_previous_vs_v2.1.xlsx`.
- Two independent AI judges agreed at criterion level with weighted κ 0.80 (v2.1 pilot; target 0.6).
- Not yet validated: 11 page types without SE test pages, human raters, and correlation with real AI citations.

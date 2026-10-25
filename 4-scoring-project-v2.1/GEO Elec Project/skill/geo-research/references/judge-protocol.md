# LLM-as-Judge Protocol for the Content GEO Score (v1.0)

Research basis: CheckEval (EMNLP 2025, checklist decomposition gave +0.45 inter-model agreement), Prometheus (ICLR 2024, anchored rubrics plus a reference answer gave r ≈ 0.90 with humans), G-Eval (evaluation steps before the score), RULERS (2026, evidence-anchored scoring), Zheng et al. (position, verbosity and self-preference biases), 2026 anchoring-bias work. Production pattern: deterministic signals + LLM-judged binary checks with verbatim evidence. Code computes levels, weights, caps and the final score.

## 1. Pipeline

```
0 Intake    → validate mandatory inputs (page type, topic, industry, stage); note optional ones
1 Acquire   → content text (URL fetch / brief / file). Keep the headings, lists, tables, alt text and CTA labels
2 Signals   → run scripts/geo_content_check.py → deterministic metrics (JSON)
3 Prompts   → if no target prompts were given, derive 1 seed prompt + 3–5 fan-out sub-questions from
              topic × stage × persona × intent (state that they are inferred)
4 Judge     → per criterion of the page-type logic: answer binary checks with verbatim quotes → propose a level
5 Verify    → every quote must be a substring of the content (normalize whitespace and case). Failed quote → check = fail
6 Compute   → scripts/geo_score_calc.py: stage multipliers, renormalize, levels × weights, penalties, caps → score + band
7 Report    → score card (scoring-framework §6), then recommendations if the mode requires them
```

## 2. Judge rules (put these verbatim in any judge prompt)

1. You evaluate **citation-readiness of content** for AI answer engines (ChatGPT, Perplexity, Google AI Overviews/AI Mode, Gemini, Copilot, Claude). Ignore technical SEO: crawlability, schema code, speed, rendering.
2. Judge **only the content provided**. Do not use outside knowledge about the brand, product reputation or what the site "probably" has elsewhere.
3. **Missing evidence = fail.** If you cannot quote it, it fails.
4. For every pass, quote the shortest verbatim span that proves it (≤ 40 words). For a fail, write `NOT FOUND` or quote the offending span.
5. Write the evidence and a ≤ 50-word rationale **before** the level.
6. Length is not quality. Formatting without facts is not a pass for factual checks. Promotional adjectives are never evidence.
7. Numbers count only if they are relevant, specific and verifiable (unit, condition or source). Generic or decorative numbers fail.
8. Use the anchors exactly. Level 5 needs exceptional evidence. When torn between two levels, pick the lower.
9. Never see or use a previous score for the same page.
10. Output JSON only, valid against the schema in §3.

## 3. Output schema (per page)

```json
{
  "page": {"id": "...", "type": "PDP", "stage": "Evaluation", "topic": "...", "industry": "...",
           "target_prompts": ["..."], "prompts_inferred": true},
  "criteria": [
    {
      "id": "PDP-1",
      "checks": [
        {"id": "c1", "result": "pass|fail|na", "evidence": "<verbatim or NOT FOUND>", "location": "<heading/section>"}
      ],
      "rationale": "<= 50 words",
      "proposed_level": 0,
      "confidence": "high|medium|low"
    }
  ],
  "gates": [{"id": "G1", "triggered": false, "evidence": "..."}],
  "penalties": [{"id": "fluff_density", "applied": false, "evidence": "..."}],
  "out_of_scope_observations": ["Key specs appear to be loaded inside an image carousel → route to SE Digital"],
  "stage_fit": {"fits": true, "note": "..."}
}
```

Pass this JSON to `geo_score_calc.py`. It maps checks to levels where the judge's level is inconsistent with the checks (it takes the **lower** of the proposed level and the checks-based ceiling), applies weights, multipliers, penalties and caps, and returns the final score.

**Checks → level (v2.1, 20 Oct 2026):**
1. *Ceiling:* with n applicable checks and p passes, ceiling = round-half-up(5 × p / n), capped at 4 unless p = n; level 5 also needs the judge to propose 5. The level is the lower of the judge's proposal and this ceiling. U2 follows its own anchor table.
2. *Anchors:* for U1 and U3–U10, the rubric's level-3 and level-4 definitions (e.g. "U10: 3 = c1+c2") are applied in code from the checks (`level_anchors` in `weights.json`). When the checks meet a definition, the level is at least that level, even if the judge proposed lower. The judge still decides the checks.
3. *Caps:* rubric caps written in the criterion text (e.g. "U3 ≤ 2 if c5 fails", "SOL-5 c2 fail → ≤ 2", "U9 undated → ≤ 1") are enforced in code (`level_caps`), then gate caps apply.
v2.0 used Python banker's rounding (2 of 4 checks → 2) and did not apply anchors, so pages meeting a written level-3 rule could score 2. `--legacy-levels` reproduces v2.0 for comparison.

## 4. Bias and variance controls

- **Temperature 0** (or the lowest available). Structured output with schema validation; retry on invalid JSON.
- **Batch criteria in small groups** (3–5 per call) for long pages, so that later criteria do not get less attention.
- **High-stakes or borderline scores** (within ±3 of a band edge or the 70 threshold): run 3 independent judgements and take the median level per criterion. Report the spread and flag criteria with a spread ≥ 2 levels for human review.
- **Competitor comparisons:** present the pages in randomized order. For pairwise questions, run both orders and accept only consistent verdicts.
- **Self-preference:** when the agent has rewritten content, the re-score must use a fresh context and must not include the agent's own rewrite rationale.
- **Inflation watch:** the gold-set median should land at 40–60. If production medians drift above 70, tighten the anchors.

## 5. Bulk mode (up to 10 URLs/files)

- Score each item independently (fresh judge context per item).
- Output: one summary table (item · type · stage · score · band · top gap) + individual score cards.
- Cross-item checks when items share a family: duplicated boilerplate (BLK-5 / penalty), naming inconsistencies (U8), conflicting specs (G1).

## 6. Calibration plan (before production)

1. **Gold set:** 5–6 example pages per page type (the examples requested by 16 Oct). Expand to ≥ 30 per major type over time. Include deliberately weak and strong pages.
2. **Human labels:** 2–3 raters (SEO/GEO, content, product SME) score independently with this rubric.
3. **Agreement:** Cohen's/Fleiss' κ per criterion. Human–human first, then judge–human. Target κ ≥ 0.6. Rewrite any criterion below 0.4.
4. **Critique shadowing:** take expert critiques of disagreements and add 1–2 short exemplars per level to the criterion text.
5. **Lock & version:** freeze the prompt, rubric and weights as `vX.Y`. Re-calibrate when the judge model changes.
6. **Outcome validation (quarterly):**
   - Pick 20–50 pages per type with a fixed prompt panel.
   - Run ≥ 7 repetitions per prompt per engine, on multiple dates, with untreated control pages.
   - Correlate score changes with changes in citation/mention rate (Profound + manual panel).
   - Down-weight any criterion that shows no relationship.

## 7. Prompt skeleton (per criterion group)

```
SYSTEM: You are a strict GEO content evaluator. [Judge rules §2]
CONTEXT: page_type={…}; stage={…} (definition: …); topic={…}; industry={…}; audience={…}; country={…};
         target_prompts={…}; fan_out={…}
CRITERIA: for each: id, definition, checks (pass/fail definitions), anchors 0–5, 1 exemplar for levels 1/3/5
CONTENT: <<< full extracted text with heading markers [H1]/[H2]/[H3], [TABLE], [LIST], [IMG alt="…"], [CTA "…"] >>>
SIGNALS: <<< JSON from geo_content_check.py >>>
TASK: Return JSON per schema §3 for these criteria only.
```

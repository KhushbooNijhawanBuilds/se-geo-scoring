# Batch test: Blog article (01–06) and News / press release (49–54), per-type prompts v2.1

Judge: blind, strict, single run per page. Each page was judged on its corpus text (`corpus/<file>`; the `rendered/` copies were shorter and had no extra content), following `prompts/copilot_prompt_article_v2.1.txt` and `copilot_prompt_news_v2.1.txt`. The type key comes from Appendix A (Blog article → `article`, News / press release → `news`). Target prompt and stage were inferred as each prompt instructs, before looking at the v2.1 scores. Judge JSON is in `judge/NN.json`, and the official calculator output (`geo_score_calc.py --judge`) is in `result/NN_result.json`.

**Level convention used:** the proposed level = the check ceiling (`min(4, round-half-up(5p/n))`), and 4 when every check passed. The one exception is 50 U2, proposed at 5 because all four checks pass in the first block and the outcome is quantified. The calculator then applied the anchors and caps. It lowered U2 on 49 and 52, because my helper used the generic ceiling rather than the U2 "ceiling = passes" rule.

## Results

| ID | type key | stage used | new score | band | v2.1 score | diff | gates | top 3 gaps (impact pts) |
|---|---|---|---|---|---|---|---|---|
| 01 | article | Awareness (v2.1: Education) | 39 | Poor | 37 | +2 | none | U1 (+17.9); U5 (+10.5); ART-1 (+6.4) |
| 02 | article | Education (v2.1: Education) | 76 | Good | 71 | +5 | none | U5 (+5.8); U1 (+3.1); U3 (+2.8) |
| 03 | article | Education (v2.1: Awareness) | 45 | Average | 47 | -2 | none | U5 (+14.6); U1 (+12.6); ART-1 (+5.6) |
| 04 | article | Education (v2.1: Awareness) | 40 | Average | 53 | -13 | none | U5 (+14.6); U1 (+12.6); U4 (+6.2) |
| 05 | article | Education (v2.1: Education) | 66 | Average | 69 | -3 | none | U5 (+11.7); ART-3 (+4.8); U4 (+4.7) |
| 06 | article | Awareness (v2.1: Awareness) | 42 | Average | 39 | +3 | none | U1 (+14.3); U5 (+10.5); ART-1 (+6.4) |
| 49 | news | Consideration (v2.1: Consideration) | 48 | Average | 55 | -7 | none | NEWS-3 (+12.6); U4 (+8.4); U2 (+6.9) |
| 50 | news | Consideration (v2.1: Consideration) | 65 | Average | 58 | +7 | none | NEWS-6 (+6.7); NEWS-3 (+5.0); U4 (+4.2) |
| 51 | news | Consideration (v2.1: Consideration) | 64 | Average | 52 | +12 | none | NEWS-2 (+6.7); NEWS-6 (+5.3); U4 (+4.2) |
| 52 | news | Evaluation (v2.1: Consideration) | 62 | Average | 59 | +3 | none | NEWS-2 (+6.8); U4 (+5.8); NEWS-6 (+5.4) |
| 53 | news | Education (v2.1: Education) | 65 | Average | 59 | +6 | none | NEWS-3 (+5.9); NEWS-1 (+5.5); NEWS-6 (+4.9) |
| 54 | news | Awareness (v2.1: Awareness) | 43 | Average | 40 | +3 | none | NEWS-1 (+12.8); U2 (+12.8); U7 (+8.0) |

- **article** median: new 43.5 vs v2.1 50.0; mean |diff| 4.7
- **news** median: new 63.0 vs v2.1 56.5; mean |diff| 6.3
No gates or penalties fired on any of the 12 pages. Band agreement with v2.1: 11/12. The only change is 06, Poor (39) → Average (42), across the 40 line. 04 drops 53→40 but stays Average. Borderline (within 3 of 40/70/90): 01 (39), 04 (40), 06 (42), 54 (43). These need 3 runs and the median.

## Big differences (>10 pts)

**04 (−13: 40 vs 53).**
- *Check interpretation, U1 (−6.3 pts).* v2.1 passed U1 c1 ("But they’re not the biggest challenge…"), c2 (the slogan H1) and c3. I failed c1 and c2. The first 100 words are a rack-density anecdote that does not answer the planning question, and "AI is moving faster than infrastructure. Leaders need a new strategy." is a slogan, not searcher wording. Rule 9 (torn → fail) decides it.
- *Check interpretation, U5 c5.* v2.1 passed "Aaron Dudley" alone. The new prompt explicitly needs "role or experience visible", so it fails. U5 drops 1→0 at a weight of 14.6.
- *Stage choice.* v2.1 used Awareness and I used Education. The page gives "three questions… ask this week" and a "start with a facility assessment" step, which reads as "how to approach it". The Education weights put more on U5 (14.6) and ART-3, where the page is weak.
- The remaining gap is small level calls on U4 c4 (undefined GPU/HVAC/ROI), U7 c3 and U8 c2.

**51 (+12: 64 vs 52).**
- *Level choice inside the allowed range, not check results.* Pass counts are nearly identical to v2.1 (NEWS-1 3/4, U3 4/5 and U6 3/4 are the same in both runs). v2.1's judge proposed level 3 where the ceiling allowed 4 on NEWS-1, U3 and U6. I proposed the ceiling. That alone is worth about 5 pts.
- *Real check differences.* NEWS-3 c3: I passed "Pilot deployments in the Pacific region" as a pilot site, while v2.1 failed it (the customer is unnamed). U2 c4: I passed "over 34,000 USD of annual value". U7 c2: I passed the "Scopes 1 and 2" scope limit under the news rule "c2 passes on any stated limitation or scope limit".

**Smaller but systematic (5–7 pts):**
- *News 50 and 53 are higher.* Same reason as 51: ceiling-level proposals, plus 50 U2 = 5.
- *News 49 is lower (−7).* I failed NEWS-3 c2 ("its first…" is scoped, but "global energy technology leader" and "among the world’s most sustainable companies" are not) and NEWS-3 c3 (Matter/Thread compliance has no standard number). NEWS-3 = 0 at a weight of 12.6.

## Per-type observations
- **Article** median is 43.5 (v2.1: 50). Every blog except 02 and 05 has no takeaways block (ART-1 = 0) and an anecdote opening (U1 ≤ 1). U5 is the biggest gap across the set: no sourced stats, no standards and no third-party quotes. Template fixes would help every page: a required Summary block, a visible author role, and a stat-source field.
- **News** median is 63 (v2.1: 56.5). Every release fails NEWS-2 c1, because the template prints numeric `DD/MM/YYYY` dates. Five of six have no About block in the HTML (only 49 has one), so NEWS-6 is ≤1. Template subheads are plain text, so U3 c1 fails. All three are [T] fixes that would add about 8–12 pts per release.

## Prompt wording that was ambiguous or broken
1. **The level inside [anchor, ceiling] is undefined (both prompts).** Step 2b says only "may not exceed the ceiling". It gives no rule for when to propose the ceiling and when to go lower. This was the largest source of drift: 51 gained 12 pts with almost the same checks. Suggested fix: "propose the ceiling unless a passed check is weak; state why if lower". Alternatively, let the calculator set level = ceiling.
2. **News U2 ceiling rule vs the generic rule.** "U2 is special: ceiling = number of passes" sits inside 2b and is easy to miss. The calculator silently corrects it, with a warning. It would be clearer as its own line.
3. **Absence checks vs "every PASS needs a verbatim quote".** Checks such as U3 c5 (nothing only in an image), U8 c3 (no contradictions), U6 c3 (one intent) and U10 c1/c2 (stage/language fit) cannot be proven with a quote. I wrote judge notes for them. The prompt should allow "verified absent" notes for these check ids.
4. **The article ART-2 c2 "SEO title" is not the H1.** On 03 the `<title>` is "3 operational priorities…" while the H1 is "Demand is easy. Execution is hard." It is unclear whether the unfulfilled "3 priorities" promise in the `<title>`/meta should trigger **G5** ("Title/H1 promise") or only ART-2 c5. I failed c2 and c5 and did not fire G5. The wording should say which title G5 refers to.
5. **ART-1 c2–c4 when there is no block.** Without a block these are untestable, so it is unclear whether they are fail or na. I used fail. The cap makes it moot, but if they are marked na the criterion is dropped (>50% na), and its weight goes to the other criteria instead of scoring 0. That is a real scoring loophole. The prompt should state "fail".
6. **The news stage text is duplicated and garbled.** "Set the stage from the release subtype: … Natural stages for this type: By release subtype: launch / …" repeats the same sentence twice. "Evaluation if spec-led" has no test. On 52 (reference design with full specs) I used Evaluation and v2.1 used Consideration.
7. **The news header line "U1, U5, U9 and U10 are replaced by NEWS-1/U2, NEWS-3/NEWS-4, NEWS-2 and NEWS-6 c3"** is unclear to a non-author judge and adds nothing a judge can act on.
8. **News U5 / author.** No check covers a byline. That is fine for releases, but the "Related Spokespeople" bio block (template) contains claims ("world-class", "Most Sustainable Corporation") that are easy to count wrongly toward fluff, NEWS-3 c2 or U4. Rule 7 should list "spokesperson bios, attached-files lists, Wiztrust block" as excluded.
9. **Minor:** the U4 c2 density count ("count each distinct fact once") does not say whether the About block counts. It changed 49's density from about 1.0 to about 0.8.

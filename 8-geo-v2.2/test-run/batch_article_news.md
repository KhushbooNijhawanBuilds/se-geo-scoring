# GEO v2.2 test run: article + news batch (IDs 01-06, 49-54)

Judge: blind, strict, single run per page; prompts `copilot_prompt_article_v2.2.txt` / `copilot_prompt_news_v2.2.txt` followed as written, page text from `research/corpus/<file>` (base corpus was richer than `rendered/` for all 12; URL headers matched). Key per Appendix A: blog posts -> `article` (rule 17), press releases -> `news` (rule 12). All 158 "pass/quote" evidence spans were script-checked as verbatim substrings of the page text (0 missing). Earlier results were opened only after all 12 were judged.

| ID | key | stage (v2.2) | v2.2 score | band | prev run (stage) | v2.1 (stage) | diff vs prev | level diffs vs prev | gates | top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | article | Consideration | 41 | Average* | 39 (Awareness) | 37 (Education) | +2 | ART-3 3→2; U3 2→3 | none | U1 13.3, U5 10.0, U4 8.4 |
| 02 | article | Consideration | 81 | Good | 76 (Education) | 71 (Education) | +5 | U6 4→5; U7 4→5; U10 4→5 | none | U5 5.0, U3 3.0, U1 2.7 |
| 03 | article | Education | 52 | Average | 45 (Education) | 47 (Awareness) | +7 | U1 1→3; U4 2→1; U6 3→4 | none | U5 14.6, U1 6.3, U4 6.2 |
| 04 | article | Education | 46 | Average | 40 (Education) | 53 (Awareness) | +6 | U1 1→2; U3 2→4 | none | U5 14.6, U1 9.5, U4 6.2 |
| 05 | article | Education | 72 | Good* | 66 (Education) | 69 (Education) | +6 | U4 2→3; U6 4→5; U7 4→5; U10 4→5 | none | U5 11.7, ART-3 4.8, U1 3.1 |
| 06 | article | Awareness | 44 | Average | 42 (Awareness) | 39 (Awareness) | +2 | U3 1→2; ART-3 4→3; U6 3→4; U8 4→3; U10 4→5 | none | U1 14.3, U5 10.5, ART-1 6.4 |
| 49 | news | Evaluation | 58 | Average | 48 (Consideration) | 55 (Consideration) | +10 | U4 1→2; NEWS-3 0→2; NEWS-5 4→5; U6 4→5 | none | U4 8.6, NEWS-3 6.9, NEWS-2 6.8 |
| 50 | news | Evaluation | 64 | Average | 65 (Consideration) | 58 (Consideration) | -1 | U3 2→3; U7 2→3; U2 5→4 | none | NEWS-6 6.7, U4 5.8, NEWS-3 4.6 |
| 51 | news | Evaluation | 60 | Average | 64 (Consideration) | 52 (Consideration) | -4 | NEWS-3 4→3; U7 3→2 | none | NEWS-2 6.8, U4 5.8, NEWS-6 5.4 |
| 52 | news | Evaluation | 63 | Average | 62 (Evaluation) | 59 (Consideration) | +1 | U6 4→5 | none | NEWS-2 6.8, U4 5.8, NEWS-6 5.4 |
| 53 | news | Education | 66 | Average | 65 (Education) | 59 (Education) | +1 | U2 4→3; NEWS-5 3→4; NEWS-4 4→5; U6 4→5 | none | NEWS-3 5.9, NEWS-1 5.5, U2 5.5 |
| 54 | news | Awareness | 43 | Average* | 43 (Awareness) | 40 (Awareness) | 0 | U2 1→2; U4 2→1; NEWS-2 4→3; U8 4→3 | none (NEWS-5 dropped, all na) | NEWS-1 12.8, U2 9.6, U7 8.0 |

\* Borderline (within 3 of a band edge): 01 (41), 05 (72), 54 (43). Standard says confirm with 3 independent runs and use the median; only one run was done here.

No penalties applied on any page. No gates triggered (G4 considered for 53 - "Current standards are shown to overestimate arc flash risk" and "well below ... even without protection devices" - not triggered, but worth an expert look).

## Medians

| | v2.2 (this run) | prev run (7-geo-all-types) | v2.1 CSV |
|---|---|---|---|
| article (6) | 49 | 43.5 | 50 |
| news (6) | 61.5 | 63 | 56.5 |
| all 12 | 59 | 55 | 54 |

Mean absolute difference vs prev run: 3.75 points; vs v2.1: 5.9.

## Differences > 10 vs prev run

None. The largest is 49 (+10, exactly at the threshold). Causes: (1) stage — the v2.2 news stage test (rule 1: launch + 3 specs with units/named elements) gives Evaluation, not Consideration, so U4/NEWS-5 weigh more; (2) NEWS-3 0→2: I passed c2 ("introduces its first Smart Thermostat designed in collaboration with Apple" is self-scoped to Schneider Home) and marked c4 na (no evidence asset); (3) NEWS-5 and U6 reach 5 because price, markets, dates and configurations are all in the text.

Systematic small drifts: articles are +2 to +7 above the previous run, mostly because U6/U7/U10 reach 5 when every check passes (I downgraded only where a passed check was clearly weak) and because U1 c2 / ART-2 judgments on slogan-style H1s went the other way on 03/04.

## Remaining prompt ambiguity

1. **Article stage test, rule 2 vs 3.** "Compares approaches or solution types" catches almost any post that contrasts old vs new (stick-built vs prefab in 01; evaporative vs closed-loop in 05; cooling towers vs dry coolers in 02). I took 01 and 02 as Consideration and 05 as Education; three runs have now put 01 in three different stages. Proposed fix: rule 2 only when the post compares options the reader picks between, as its main structure.
2. **Article stage test, typology posts.** A "which group are you" typology (03) can be read as a comparison of approaches (rule 2) or as a framework (rule 3).
3. **News stage test, the "3+ specs" count.** It does not say whether prices, configurations or program inclusions (49, 51) count as "specs/capabilities with named elements"; that one call moves 49 and 51 between Consideration and Evaluation.
4. **When to downgrade a 5.** b3 says "use it for level 5 too when the evidence is not exceptional", but gives no test for "exceptional". Judges differ on U6/U7/U10 (02, 05) and NEWS-4/U6 (52, 53). Suggest a fixed rule (e.g. 5 only when every passed check has a quote, not a note).
5. **ART-2 c5 / NEWS-2 c3 with no promise or relative date.** Pass or na is not specified; a pass needs a quote, so judges quote the title or a sentence. Suggest na.
6. **NEWS-2 c1 numeric dateline + spelled-out event date in body** (50 "September 28–30", 54 "January 20, 2026"). Not clear whether a body date counts as the visible date. I failed it.
7. **Third-party voice for a co-developer/partner** (Apple 49, AMD 52, ETAP 53). NEWS-4 c3 passes them; NEWS-3 c3 "independent validation" doesn't say whether a co-developer counts. I passed NEWS-3 c3 for 52 and then downgraded it.
8. **Byline "Guest Blogger" with an "Author: name, role" line** (02, 05). U5 c5 fails "Guest Blogger" but the named line below it should pass; the prompt should say so explicitly.
9. **Absence/layout note list.** ART-2 c3 ("60% of H2s are descriptive") is a counting check like U3 c3, but notes aren't allowed for it, so the calculator turned three of my note passes into fails until I swapped in a quoted H2. Suggest adding ART-2 c3/c4 and U1 c4 to the note-allowed list.

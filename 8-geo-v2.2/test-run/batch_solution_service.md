# Batch: Solution + Service pages (IDs 07-12, 37-42) - GEO v2.2 judge run

Judge: blind, independent; prompts `8-geo-v2.2/prompts/copilot_prompt_<key>_v2.2.txt` followed as written, with each prompt's stage test. Text source: `corpus/rendered/<file>` where richer and URL header matched (07-12, 37, 39, 40, 41); `corpus/<file>` for 38 and 42 (plain text richer). Every pass quote was checked by script against the source text (normalised for NFKC and zero-width spaces): 0 missing.

Judge JSON: `8-geo-v2.2/test-run/judge/<NN>.json`; calculator output: `8-geo-v2.2/test-run/result/<NN>_result.json` (`geo_score_calc.py`, rules v2.2).

| ID | key | stage | v2.2 score | band | prev run | v2.1 | Δ prev | Δ v2.1 | gates / penalties | top 3 gaps (recoverable pts) |
|---|---|---|---|---|---|---|---|---|---|---|
| 07 | solution | Consideration | 33 | Poor | 33 | 22 (v2.1: solution/Evaluation) | +0 | +11 | - | SOL-7 (+13.6); SOL-5 (+10.8); SOL-4 (+9.9) |
| 08 | solution | Consideration | 22 | Poor | 15 | 19 | +7 | +3 | - | SOL-2 (+12.9); SOL-7 (+10.8); SOL-4 (+8.0) |
| 09 | solution | Consideration | 47 | Average | 29 | 39 | +18 | +8 | cta_overload | SOL-2 (+7.8); U1 (+7.2); U7 (+6.5) |
| 10 | solution | Consideration | 40 | Average | 37 | 45 (v2.1: solution/Awareness) | +3 | -5 | - | SOL-7 (+10.8); SOL-2 (+10.3); U7 (+6.5) |
| 11 | solution | Consideration | 50 | Average | 46 | 41 | +4 | +9 | template_artifact | SOL-5 (+10.8); SOL-7 (+5.4); SOL-2 (+5.2) |
| 12 | solution | Consideration | 25 | Poor | 25 | 26 | +0 | -1 | template_artifact | SOL-7 (+13.6); SOL-5 (+10.8); SOL-2 (+10.3) |
| 37 | service | Evaluation | 49 | Average | 48 | 51 | +1 | -2 | - | SVC-2 (+9.0); SVC-3 (+8.9); SVC-7 (+6.3) |
| 38 | service_project | Consideration | 44 | Average | 39 | 45 | +5 | -1 | cta_overload | SVC-7 (+10.3); SVC-2 (+8.4); SVC-4 (+7.6) |
| 39 | service_project | Consideration | 53 | Average | 51 | 45 | +2 | +8 | template_artifact | SVC-2 (+8.4); SVC-7 (+8.2); SVC-5 (+5.5) |
| 40 | service_project | Consideration | 25 | Poor | 17 | 19 (v2.1: service/Consideration) | +8 | +6 | G13, cta_overload | SVC-7 (+10.3); SVC-6 (+9.5); SVC-1 (+9.4) |
| 41 | service | Evaluation | 48 | Average | 41 | 43 | +7 | +5 | - | SVC-2 (+9.0); SVC-3 (+8.9); SVC-7 (+8.4) |
| 42 | service_project | Consideration | 36 | Poor | 31 | 25 (v2.1: service_project/Decision) | +5 | +11 | G12, G13 | SVC-1 (+12.5); SVC-4 (+9.5); SVC-2 (+8.4) |

**Medians** - v2.2: all 42.0, solution 36.5, service 46.0 | previous run: all 35.0, solution 31.0, service 40.0 | v2.1: all 40.0, solution 32.5, service 44.0.
Mean absolute difference: vs previous run 5.0; vs v2.1 5.8. Bands: 4 Poor / 8 Average / 0 Good. Borderline (within 3 of 40/70/90): only 10 (40). It needs 3 independent runs and the median.

## Level differences vs previous run (criterion prev -> v2.2)
- 07: none. 12: U5 0->1, U10 4->5. 37: SVC-2 1->2, U1 4->3, U7 3->2, U10 3->4. 39: SVC-1 2->4, SVC-6 5->4.
- 08: U10 1->3, U7 0->2, SOL-1/SOL-4/U6/U9 0->1, SOL-8 1->0. The previous run's G6 (cap 59) did not fire here: the text is thin, but the core content is not locked in media.
- 10: SOL-4 5->3 (the basis-cap now applies), U1 3->2, U2 2->3, U6 1->3, SOL-2/SOL-7 0->1.
- 11: SOL-4 1->3, U2/U6 3->4, U10 5->4.
- 38: U3 2->4, SVC-1 3->4, U2/U10 3->4, SVC-2 1->0. 40: SVC-1 1->2, U7 0->2, SVC-2/SVC-3/U9 0->1. 41: SVC-6 1->3, SVC-1/U10 3->4, U7 2->0, SVC-5/U9 0->1.
- 42: SVC-5/SVC-6 1->3, U2/U3 2->3, SVC-2 2->0, SVC-4 1->0, U7 2->0, SVC-1 0->1. Its G12 and G13 caps did not bind (raw 36.1 is under 40).
- Across the batch: U9 0->1 on almost every page. v2.2 lets U9 c2 pass on a note ("nothing superseded shown"), so an undated page now gets 1 instead of 0, and the U9 cap then holds it at 1.

## Reasons for the one diff over 10 points vs the previous run
**09 Water and Wastewater (29 -> 47, +18).** The main reason: v2.2 judge rule 7 says text in hidden tabs and carousels counts for every check. On this page about half the words (1,026 of 2,152) sit in hidden tab panels, and they hold the subsegment applications (treatment, desalination, networks) and most of the offer detail. The previous run apparently did not credit that text.
- SOL-7 1->3: c1 (applications with context, in hidden tabs) and c3 ("Microgrids are a reliable alternative wherever a stable power supply is needed") now pass.
- SOL-1 1->3: c4 passes, because the climate/demand problem paragraph starts about 100 words after the H1.
- U6 1->3: c2 passes, because products, customer stories and energy savings answer most of the fan-out questions.
- SOL-4 3->4: c3 passes, because the City of Conroe result names its basis. A strict judge could fail this: it is a customer name, not a baseline or method.
- U3 1->2, SOL-2 1->2, U9 0->1: smaller changes.

The hidden text no longer costs points under these criteria. It is now penalised once, under U3 c5 (U3 max 2). This is how v2.2 is meant to work, not judge drift. Still, three of these calls (SOL-1 c4, SOL-7 c3, SOL-4 c3) are judgement calls a stricter judge could fail, which would give about 38-40.

## Remaining prompt ambiguity
1. **template_artifact vs duplicated card titles.** The rendered text often repeats a card's title ("APC NetShelter Power Shelf APC NetShelter Power Shelf", "EcoCare for 3-Phase UPS EcoCare for 3-Phase UPS"). It sometimes repeats the whole card body too (SpaceLogic in 11, MSS cards in 12, EcoConsult cards in 39). I applied the penalty only when the body text repeats. The prompt says "a whole section or card rendered twice" but does not say whether a duplicated title or alt label counts. Because this comes from the template, it changes 2 points on many pages.
2. **SOL-1 c4 "within about 150 words after the H1".** When the hero is a customer teaser (09, 10), it is unclear whether a generic benefit line ("reduce stranded asset risk") counts as stating the problem. A word-count rule with an example would help.
3. **SVC-1 c2 / G12 on thin modernization pages (42).** "Modernize and extend the life of aging Altivar 61 and 71 drives" names the assets but no work done and no artifact received. Whether that passes c2 decides whether G12 fires. I failed it, but the cap did not bind here.
4. **G13 counting.** The threshold of 3 statements is easy to argue either way on 40 and 42. It is unclear whether "named service + what it does" counts when the description is generic ("Delivering design, configuration and implementation services"). One more example of a generic offer line that does not count would settle it.
5. **SVC-5 c1 "one plan stated" on a single-offer service (41).** Naming the service itself ("managed security services (MSS)") passes c1 if read literally, which gives every single-offer page a free pass. Clarify that c1 needs a named plan or tier, not the service name.
6. **SOL-4/SVC-6 c3 "basis".** It is unclear whether a customer name next to a figure (Conroe "up to 70%"), or a generic disclaimer ("based on Schneider Electric's data, benchmark and estimation", 39), counts as a basis. I passed both and then downgraded them to 4. The caps depend on this check, so the threshold should be spelled out.
7. **Mixed service type (40).** The H1 is just "Cybersecurity services", so I classified by the intro under Appendix A, which matches its own example: `service_project`. v2.1 used `service`. This works as written. I note it only because it explains part of the gap with v2.1.
8. **Stage: v2.1 used Evaluation for 07, Awareness for 10 and Decision for 42.** The v2.2 stage tests give Consideration for all three: 07 has no quantified parameter, 10 names offers, 42 has no order form. The tests were unambiguous here, and these stage changes explain most of the +11 gaps vs v2.1 on 07 and 42.

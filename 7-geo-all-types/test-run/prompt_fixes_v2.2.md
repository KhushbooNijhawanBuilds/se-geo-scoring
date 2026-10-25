# Prompt and rubric fixes found in the 60-page test run (for v2.2)

Source: the five batch reports in this folder (batch_*.md). Grouped by impact.

## Affects scores across many types
1. **Level between anchor and ceiling is undefined.** Judges choose differently (biggest source of drift, ~5 pts on news). Fix: the calculator sets the level = ceiling, with the judge only allowed to go lower if a named check is weak, stated in the rationale.
2. **Stage choice moves scores ~10 pts** and the tie-break rules are vague: solution "product-solution page", news "spec-led", calculator comparison vs TCO, case study "approach showcase". 15 of 61 pages got a different stage from v2.1. Fix: a concrete stage test per type, or require the business to supply the stage.
3. **"Every pass needs a verbatim quote" can't work for absence/layout checks** (no contradictions, paragraph length, facts not only in images). Fix: allow a judge note for those checks.
4. **na loophole:** when a block is missing (e.g. no takeaways), marking its checks na drops the criterion instead of scoring 0. Fix: say "fail" explicitly. Similar: U1 c4 na on pages with no sections.
5. **G1 contradiction has no materiality threshold**, and widget errors (#VALUE!, "reduce 80% to 100%") are unclear: G1 or placeholder penalty. Fix: define material contradiction; widget errors = template_artifact.
6. **Hidden duplicate / hidden-tab content is penalised 2–3 times** (U3 c5 + type checks + duplicate penalty). Fix: count once.
7. **G13 thin-page is applied inconsistently** on abstract-only pages; G2 vs G6 unclear on download pages without KPIs.

## Broken references (fix now)
8. esg_report / esg_report_doc: G6 says "U3 max 2" but these types have no U3.
9. esg_report_doc: "bookmarks/outline" counted twice (ESG-5 c2 and DOC-4 c5).
10. case_study: U9 rule refers to a non-existent c3.
11. esg_report DOC-5 c3 still uses the "White paper 126" example.
12. range U7 c4 text conflicts with its own "c4 is na" rule.
13. service_project SVC-2 c5 still has recurring-service wording.
14. News: U2 ceiling rule buried in step 2b; duplicate stage sentence; header "U1, U5, U9 and U10 are replaced by…" not actionable.

## Unjudgeable from pasted text
15. DERIVED DOC-4 / ESG-5 checks (tagged PDF, bookmarks, text layer on every page, cross-references accurate). Fix: mark na unless extraction metadata is supplied.
16. "Current edition" checks need outside knowledge, which judge rule 1 forbids. Fix: judge only what the page itself says (superseded notice, dates).

## Type-boundary rules to clarify
17. service vs service_project for mixed offers; "3+ product cards" rule for software hubs; whether accessory/app cards are range "members"; whether HTML `<title>` counts as "Title/H1" (CS-1, ART-2, G5); whether a bare "free" counts as a trial term (G11); whether software types should have U5.

## Data notes
- #44 is the same page as #43 (duplicate URL in the inventory).
- Rendered captures for 55–58 belong to other pages; server text was used.
- No white-paper PDF text in the corpus, so whitepaper_doc is still untested.

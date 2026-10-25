
## Appendix C. Gaps and contradictions found in the source (to resolve; the engine was not changed)

**Checks not specified in the source.** Here the checks were derived, and they are marked "DERIVED" or "v1 split" in the criteria tables:
- **v1 types (pdp, category, caas, document, datasheet, comparison, faq, video).** `page-types.md` gives checks as phrase lists, not numbered c1..cN, so they were split into binary checks.
- **Criteria with no checks at all.** Checks were written from the criterion name for:
  - CAT-2, CAT-4
  - BLK-6
  - CMP-2 (and the CMP-3 trade-off check)
  - FAQ-4, FAQ-7
  - GLO-1 to GLO-5 (no glossary checks exist)
  - VID-8
  - PDP-7 (second check)
- **ESG and white-paper document modules.** No checks are written in `page-types-v2.md` for:
  - DOC-1 in esg_report_doc (mirrors the whitepaper_doc DOC-1)
  - DOC-4 in esg_report_doc (from "tagged PDF, real tables, reading order, bookmarks")
  - the ESG variant of DOC-7
  - DOC-5 in esg_report (white-paper DOC-5 reused)
  - DOC-7, DOC-8 and DOC-5 in whitepaper_doc (gateway versions reused)
- **DOC-9 checks** come from `research/type-analysis/whitepaper-and-esg.md`, not from page-types-v2.
- **The pilot judges' check wording for the ESG document criteria was never written down.** Only their evidence is stored. The derived checks may differ from what the judge used on #59_doc and #60_doc, even though the calculator reproduces those scores.

**Rubric caps that are not in code.** These work only through the judge's proposed level:
- CS-6: "card grids alone reach at most 2"
- BLK-1 and BLK-9: banner test, at most 3
- PDP-1: level 5 needs at least 95% of the attributes
- PDP-5: level 5 needs at least 5 Q&As
- ART U9: level 5 needs an "Updated" date
- WP-2: at level 1 or below, trigger G6 (a judge-set gate)

**Gate G2 differs between documents.** `scoring-framework.md` §4 defines it as "U1 = 0 and U2 ≤ 1". The gate registry and the code have it as a judge-set flag, and the code does not derive it.

**Gate applicability is not enforced.** The calculator applies any gate the judge triggers, even one meant for another type (e.g. G7 on a solution page). Applicability exists only as a judging rule.

**G1 and G13 do nothing for some types.**
- G1 zeroes U8 and BLK-4, so for types without either criterion (glossary, faq, comparison, category, video, solution, service, software_trial) it only caps the score.
- G13 has no effect on types without U7 or U8 (video, and partly others).

**Weights in `page-types.md` v1 disagree with `weights.json`.** `weights.json` was used (it is the source of truth). Examples:
- solution and case_study: v1 tables are superseded by v2
- range: v1 RNG-1 16 vs 10
- v1 CaaS and editorial tables do match

**Undocumented engine behaviour:**
- A criterion is dropped when **more than** 50% of its checks are na; exactly 50% stays.
- Anchors need at least one listed check to pass.
- Level 5 requires the judge to propose 5, even when every check passes.
- Effective weights are rounded to 2 decimals per criterion, so a stage column can sum to 99.97-100.03.

**Stages:**
- There is no "Post-purchase" stage in the engine, though `buyer-journey.md` and the service type mention it.
- The proposed ESG "Verification" stage is not implemented.
- No default stage is defined for editorial, video, faq, caas or service. The defaults used here are this document's choice: editorial Education, video Education, faq Education, caas = host page or Consideration, service Evaluation, service_project Consideration.

**Validation gaps:**
- Not piloted on SE pages: pdp, category, caas, editorial, document, datasheet, comparison, faq, glossary, video and whitepaper_doc.
- Fewer than 3 pilots: software_product (1), software_trial (1), esg_hub (1), esg_report_doc (2).
- Inventory #44 (software) is absent from the CSV and the judge files.
- Blind Judge B covered only 13 pages: articles, solutions and #37.

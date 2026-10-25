## Appendix A. How to choose the page type (decision tree)

Work down the list and take the first match. If the declared type conflicts with the content, score with the declared logic, then flag the mismatch and give the score under the better-fitting type.

1. **Is it a PDF or the text of a PDF?** White paper -> `whitepaper_doc` (and score its HTML page with `whitepaper_gateway`). Sustainability/ESG report -> `esg_report_doc` (and `esg_report` for the gateway; a bare PDF URL gets the gateway logic with every HTML check failing). Datasheet -> `datasheet`. Catalog, guide, manual -> `document`.
2. **Document download / landing page?** White paper or technical guide -> `whitepaper_gateway`. One ESG report -> `esg_report`. Report library / sustainability hub -> `esg_hub`.
3. **Video asset** (YouTube + embed) -> `video`.
4. **Reusable module under ~150 words** (object description, banner, benefit block) -> `caas`.
5. **SKU/reference + spec table** -> `pdp`.
6. **Several variants of one named family** -> `range` (master ranges included). Members are the variants or sub-ranges of the named family; accessory, battery, software/app and service cards on the page are **not** members (judge them under RNG-5; they fail RNG-9 c5 only if unrelated to the range).
7. **Several families/types under a generic noun** -> `category`.
8. **Software?** 3+ cards for **distinct, separately named software products** -> `software_hub` (capability tiles or modules of one platform are not products: one platform with module tiles -> `software_product`); sign-up/download/licence action is the main content -> `software_trial`; otherwise -> `software_product`. Software types have no U5 by design: the U5 evidence checks are scored inside SW-6 (proof, attributed statistics, third-party validation with year), SW-4 c2 and SW-2 c1 (standards and certifications by number); adding U5 would double-count them and require re-weighting.
9. **Service offer?** Recurring (maintenance, monitoring, managed) -> `service`; one-off (modernization, retrofit, consulting) -> `service_project`. **Mixed offers:** classify by the offer named in the H1; if the H1 names both, by the first deliverable listed in the H1/intro (e.g. "design, configuration and implementation services with maintenance" -> `service_project`). Cross-sells ("Combine with EcoCare membership") are ignored.
10. **Primary element is an interactive tool computing outputs from inputs** -> `calculator`.
11. **Named customer + results** -> `case_study`.
12. **Dated corporate announcement with dateline, spokesperson quotes, media contact** -> `news`.
13. **Two or more options side by side, or "how to choose"** -> `comparison`.
14. **Q&A pairs are the main content** -> `faq`.
15. **Defines one term** -> `glossary`.
16. **Industry/segment problem + architecture of offers** -> `solution`.
17. **Dated narrative, opinion or explainer** -> `article`.
18. **Otherwise** -> `editorial`.

**Boundary rules that apply inside the types (v2.2):**
- **"Title/H1"** in CS-1 c1/c2 means the visible H1 **or** the HTML `<title>`; either passes. ART-2 c2/c5 judge the `<title>` and meta explicitly. **G5** concerns the visible H1 (and deck) only; an unfulfilled promise that is only in the `<title>`/meta fails ART-2 c5 (or U1 c2), not G5.
- **A bare "free"** ("free trial", "free download") counts as a trial term (cost) for **G11**, so G11 does not fire; SW-5 c3 still needs at least 2 trial terms.
- **SW-3 c1** counts only statements about where the software itself runs, not the customer's infrastructure.
- **Software hubs (SW-1):** a check passes when at least half of the product cards meet it.



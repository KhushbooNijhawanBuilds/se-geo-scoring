# SE URL inventory corpus (captured 2026-10-19)

- Source: `source-docs/schneider_electric_url_inventory.xlsx` (60 URLs, 10 page types × 6).
- `NN_<type>.md`: main content converted from server HTML (what non-JS AI crawlers receive). Header comment = title/meta/JSON-LD types.
- Extraction: body content minus header/nav/footer/aside/forms; blog.se.com scoped to `<article>`; screen-reader-only (`sr-only`) text kept, because crawlers read it.
- Validated against the rendered page in a browser (calculator page 33): text matched. The calculator UI itself is an iframe and is not in page text.
- Not captured: #59 and #60 (2023/2022 sustainability reports) are direct PDF links; they were not downloaded.
- #44 redirects to #43 (same page).
- `build_corpus.py` regenerates the corpus (`--rebuild` re-parses saved HTML).

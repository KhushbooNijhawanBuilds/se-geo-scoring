# Round 2: Title tag, meta description, URL/slug (as of Oct 2026)

Scope: fills gaps left by official_guidance.md and ranking_evidence.md. Labels: [OFFICIAL] = search-engine doc; [EXPERIMENT] = controlled split test; [OBSERVATIONAL] = vendor SERP scrape or correlation. Primary pages were fetched on 2026-10-23 unless noted. About 20 distinct sources were read in full, short of the 25+ target. Gaps are listed honestly.

## Title tag

### Takeaway
Google gives no length limit. It truncates "to fit the device width" and rewrites titles that are half-empty, obsolete, inaccurate, boilerplate, unclear or in the wrong language. Observational data shows rewrite rates rising, from 61.6% (2022) to 76% (Q1 2025, secondary). Rewrites are least likely for titles of about 51-60 characters that match the H1. Split tests show title wording can move organic traffic by about 10-24%.

### Cited Findings
- [OFFICIAL] Google best practices, quoted verbatim:
  - "Make sure every page on your site has a title specified in the `<title>` element"
  - "Write descriptive and concise text for your `<title>` elements"
  - "Avoid keyword stuffing"
  - "Avoid repeated or boilerplate text in `<title>` elements"
  - "Brand your titles concisely"
  - "Make it clear which text is the main title"
  - "Use the same language and writing system"
  - "Avoid including flight price information"
  - Source: [Influencing title links](https://developers.google.com/search/docs/appearance/title-link), last updated 2025-12-10.
- [OFFICIAL] Sources Google uses for title links, verbatim:
  - "Content in `<title>` elements"
  - "Main visual title shown on the page"
  - "Heading elements, such as `<h1>` elements"
  - "Content in `og:title` `meta` tags"
  - "Other content that's large and prominent through the use of style treatments"
  - "Other text contained in the page"
  - "Anchor text on the page"
  - "Text within links that point to the page"
  - "`WebSite` structured data"
  - Source: [same](https://developers.google.com/search/docs/appearance/title-link)
- [OFFICIAL] Named rewrite issues, with Google's examples:
  - Half-empty: "| Site Name" is rewritten to "Product Name | Site Name".
  - Obsolete: "2020 admissions criteria" is shown as 2021 when the visible heading says 2021.
  - Inaccurate: a stuffed list becomes "Stuffed animals - Site Name".
  - Micro-boilerplate: identical titles across seasons get "Season 1 - ..." added.
  - No clear main title: Google may use the first of several equally prominent headings.
  - Writing-system or language mismatch.
  - Duplication of the site name: Google may omit it.
  - Source: [same](https://developers.google.com/search/docs/appearance/title-link)
- [OFFICIAL] On length: "While there's no limit on how long a `<title>` element can be, the title link is truncated in Google Search results as needed", typically "to fit the device width." Site name guidance: "just your site name at the beginning or end of each `<title>` element", with a hyphen, colon or pipe as the delimiter. — [same](https://developers.google.com/search/docs/appearance/title-link)
- [OFFICIAL] Good titles are "unique to the page, clear and concise, and accurately describes the contents of the page." — [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), last updated 2025-12-10.
- [OBSERVATIONAL] Zyppy, Q1 2022 (80,959 titles across 2,370 sites, desktop, collected with site: searches):
  - Overall: 61.6% of titles were rewritten.
  - By length: titles of 1-5 characters were rewritten 96.6% of the time, those of 20 characters or fewer over 50%, over 60 characters over 76%, and over 70 characters 99.9%. Titles of 51-60 characters had the lowest rate, 39-42%.
  - Brackets: 77.6% rewritten, with the bracketed text removed 32.9% of the time. Parentheses: 61.9% rewritten, with the text removed 19.7% of the time.
  - Separators: pipes were removed or replaced 41.0% of the time, dashes 19.7%.
  - Numbers: when the title had a number but the H1 didn't, Google dropped the number 25.8% of the time. When both had one, Google kept a number 97.3% of the time.
  - Source: [Zyppy](https://zyppy.com/seo/google-title-rewrites/). The page shows an Oct 2026 update stamp, but the data is still Q1 2022.
- [OBSERVATIONAL] John McAlpin's Q1 2025 study for Search Engine Land reported that Google changed 76% of title tags, up from about 61%. Brand-name removal was reportedly the most common change, at about 63% of modified titles. — [Search Engine Land, May 2025](https://searchengineland.com/google-changed-76-of-title-tags-in-q1-2025-heres-what-that-means-454847)
  - The page returned 403 on fetch. Figures come from search snippets and secondary summaries ([blckalpaca](https://blckalpaca.at/en/knowledge-base/seo-geo/on-page-seo/title-tags-2026-google-rewrites-76-how-to-prevent-it)), so treat them as unverified.
- [EXPERIMENT] SearchPilot split tests:
  - Removing "Compare" from ecommerce title templates (which also shortened them) gave an estimated +24% organic sessions at 95% confidence, July 11, 2024 — [SearchPilot](https://www.searchpilot.com/resources/case-studies/removing-compare-from-title-tags).
  - Adding "best" to ecommerce titles gave about +11% at 95% confidence — [SearchPilot](https://www.searchpilot.com/resources/case-studies/adding-best-to-title-tags).
  - "The Best" on an editorial site gave about +10% — [SearchPilot](https://www.searchpilot.com/resources/case-studies/the-best-title-tag-experiment).
  - All-caps titles gave +14% on mobile and no significant change on desktop — [SearchPilot](https://www.searchpilot.com/resources/case-studies/14-percent-increase-on-mobile-with-all-caps).
  - Exact numbers vs approximations: inconclusive — [SearchPilot](https://www.searchpilot.com/resources/case-studies/title-tag-exact-numbers-vs-approximations-seo).
  - Natural-language brand phrasing (Feb 2026): outcome not retrieved — [SearchPilot](https://www.searchpilot.com/resources/case-studies/do-title-tags-perform-better-when-they-sound-more-natural).
  - The non-"best" results above came from search snippets only.
- [OBSERVATIONAL] Backlinko CTR study (about 4M results; 1,312,881 pages and 12,166,560 queries from GSC data; charts appear to date from about 2022; page updated 2025-04-16):
  - Position 1 averages 27.6% CTR, and the top 3 get 54.4% of clicks.
  - Titles of 40-60 characters had the highest CTR. The page itself gives inconsistent uplift figures, 33.3% vs 8.9%.
  - Titles of 6-9 words performed best.
  - Question titles were not significantly different (15.5% vs 16.3%).
  - Positive sentiment was about 4.1% higher than negative.
  - The page contains no power-word or brackets analysis.
  - Source: [Backlinko](https://backlinko.com/google-ctr-stats). The bracket-title CTR claim often attributed to Backlinko is not on the current page.
- [OBSERVATIONAL, superseded detail] Screaming Frog's 2014 reverse-engineering, last modified 2025-03-12, found an 18px Arial title, about 512px desktop truncation, and about 920px (923px in its emulator) for descriptions. Later reports of a 600px title width are not verified on that page. — [Screaming Frog](https://www.screamingfrog.co.uk/page-title-meta-description-lengths-by-pixel-width/)
- [OBSERVATIONAL] Current SERP tools commonly use about 580-600px for desktop titles. Mobile title figures conflict (480px, 540px, and a dubious 920px). — [search summary of tool pages, e.g. spotibo](https://spotibo.com/meta-description-length/); [dev.to](https://dev.to/frontendtoolstech/pixel-accurate-serp-preview-tools-for-google-url-metadata-combined-57aa)
- [SECONDARY, about Bing] Bing reportedly suggests titles of about 65 characters with the keyword near the beginning. The official Bing page could not be fetched; this comes from a third-party excerpt. — [Labnol](https://Labnol.org/tech/bing-seo/20015/)

### Inferences
- Pass/fail checks:
  - (1) Exactly one non-empty `<title>`.
  - (2) Title is unique across the site.
  - (3) Main text (excluding the brand) is at least 20 characters.
  - (4) Title is 70 characters or fewer, and 600px or less at 18px Arial if measured. Target 50-60.
  - (5) Brand appears at most once, at the start or end, after a delimiter.
  - (6) No word token repeated 3 or more times (stuffing proxy).
  - (7) Any year in the title is not older than the visible H1 or dateModified year.
  - (8) Title and H1 share their core terms, and any number in one appears in the other.
  - (9) Title language matches body language.
  - (10) Prefer a dash or colon over a pipe, and parentheses over brackets. This is a soft check based only on observational data.
- Front-loading the primary topic is supported only by truncation logic and the second-hand Bing advice. No experiment was found.

### Gaps
- The McAlpin 2025 methodology and sample size could not be verified (403).
- No 2026 rewrite study was found.
- No Google statement gives pixel numbers, so every pixel threshold is vendor-derived.

## Meta description

### Takeaway
Google says snippets come mainly from page content and the meta description is used "occasionally". It sets no length limit. Observational studies find Google rewrites 63-71% of descriptions. It is not a ranking factor. Even so, a unique, accurate description is a cheap hygiene item. Lighthouse checks only that one exists and is not empty.

### Cited Findings
- [OFFICIAL] Snippets doc, verbatim:
  - "Snippets are automatically created from page content."
  - Google may use the meta description when it gives a more accurate picture of the page.
  - "Wherever possible, create descriptions that accurately describe the specific page."
  - "meta descriptions comprised of long strings of keywords don't give users a clear idea of the page's content."
  - "There's no limit on how long a meta description can be ... the snippet is truncated in Google Search results as needed, typically to fit the device width."
  - Controls: `nosnippet`, `max-snippet:[number]`, and the `data-nosnippet` attribute for parts of a page.
  - Source: [Control your snippets](https://developers.google.com/search/docs/appearance/snippet), last updated 2026-04-20.
- [OFFICIAL] "Occasionally the snippet may be sourced from the contents of the meta description tag", and "A good meta description is short, unique to one particular page, and includes the most relevant points of the page." — [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide), 2025-12-10.
- [OFFICIAL / tool] The Lighthouse audit fails if the page has no `<meta name=description>` or its `content` is empty. It does not judge quality. It recommends unique, concise descriptions with no keyword stuffing. — [Lighthouse](https://developer.chrome.com/docs/lighthouse/seo/meta-description), last updated 2019-05-02.
- [OBSERVATIONAL] Ahrefs, 2020:
  - Sample: 20,000 keywords for rewrites; 192,656 descriptions for truncation.
  - Rewrite rate: 62.78% overall, 59.65% for fat-head and 65.62% for long-tail keywords.
  - Length: 40.61% of descriptions were too long, but long ones were rewritten no more often (61.46% vs 63.69%).
  - Presence: 25.02% of top pages had no description, with a weak correlation to ranking (0.28).
  - Source: [Ahrefs](https://ahrefs.com/blog/meta-description-study/), updated Oct 9, 2020.
- [OBSERVATIONAL] Portent, Sept 10, 2020 (about 30,000 non-brand keywords):
  - First-page rewrite rate: 71% on mobile, 68% on desktop.
  - Rewrites bump at positions 4-6.
  - Rewrites are less common for high-volume queries and more common for longer queries.
  - Recommendations: put the key message in the first ~120 characters for mobile, and use about 138-148 characters when the result shows a date.
  - Source: [Portent](https://portent.com/blog/seo/how-often-google-ignores-our-meta-descriptions.htm)
- [OBSERVATIONAL] Pixel truncation: about 920px desktop (Screaming Frog's 923px emulator); mobile about 120 characters / about 680px (tool consensus, unofficial). — [Screaming Frog](https://www.screamingfrog.co.uk/page-title-meta-description-lengths-by-pixel-width/); [spotibo](https://spotibo.com/meta-description-length/)
- [OBSERVATIONAL] Backlinko's CTR page does not measure the effect of having a meta description. Older claims of a 5.8% uplift are not on the current page. — [Backlinko](https://backlinko.com/google-ctr-stats)
- [OBSERVATIONAL] Semrush/ranking_evidence (round 1) rated meta description importance at 1%.

### Inferences
- Pass/fail checks:
  - (1) Exactly one meta description, not empty.
  - (2) Unique across the site.
  - (3) Not identical to the title.
  - (4) Roughly 70-160 characters. Flag anything over about 920px or 160 characters as truncation risk.
  - (5) Key message within the first 120 characters.
  - (6) No keyword repeated 3 or more times.
  - (7) No `nosnippet` or `max-snippet:0` unless intended.
- Weight it low. It is a CTR and snippet-eligibility hygiene item, not a ranking factor.
- AI Overviews: the round-1 notes show lower CTR on informational queries, so the description's CTR value is shrinking further. Bing's NOSNIPPET and data-nosnippet controls also limit citations (round 1).

### Gaps
- No post-2020 large-scale study of meta description rewrite rates was found.
- No study of the meta description's effect on AI Overview citations was found.

## URL / slug

### Takeaway
Google recommends readable words, hyphens, consistent lowercase, few parameters, no session IDs and no fragment-driven content. It says keywords in the URL have "hardly any effect" beyond breadcrumbs. Do not change existing URLs for SEO. If a change is necessary, use 301/308 redirects kept for at least a year.

### Cited Findings
- [OFFICIAL] URL structure doc, verbatim:
  - "When possible, use readable words rather than long ID numbers in your URLs"
  - "we recommend using hyphens (-) instead of underscores (_)"
  - "Google Search's URL handling is case sensitive" … "convert all text to the same case"
  - "shorten URLs by trimming unnecessary parameters"
  - "avoid the use of session IDs in URLs"
  - "Use words in your audience's language in the URL"
  - "Don't use fragments to change the content of a page"
  - non-ASCII characters "should be percent encoded"
  - Source: [URL structure](https://developers.google.com/search/docs/crawling-indexing/url-structure), last updated 2026-10-21.
- [OFFICIAL] SEO Starter Guide, verbatim:
  - "Parts of the URL can be displayed in search results as breadcrumbs"
  - "Try to include words in the URL that may be useful for users"
  - Random identifiers are "less helpful for users"
  - "the keywords in the name of the domain (or URL path) alone have hardly any effect" beyond breadcrumbs
  - Source: [Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [OFFICIAL] On changing URLs:
  - "we recommend that you use HTTP permanent redirects if possible, such as 301 and 308"
  - "Keep the redirects for as long as possible ... generally at least 1 year"
  - Visibility "may fluctuate temporarily"
  - Source: [Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes), last updated 2026-08-20.
- [GOOGLER STATEMENT] Mueller has called URL words a "very lightweight" factor, mainly used before Google sees the content, and said they are not worth restructuring for. In 2017 he said keywords in URLs are "overrated" and to make URLs for users. — Quoted second-hand by [Search Laboratory](https://www.searchlaboratory.com/?p=2862) and [Ahrefs glossary](https://ahrefs.com/seo/glossary/url-slug); the original tweet and Hangout were not opened.
- [OBSERVATIONAL] Backlinko: URLs that fully or partly match the query had higher CTR. Only 6.3% of URLs had more than 80% similarity to their query. This is correlational. — [Backlinko](https://backlinko.com/google-ctr-stats)

### Inferences
- Pass/fail checks:
  - (1) Slug contains readable words, not just IDs or hashes.
  - (2) Hyphen separators, no underscores or spaces.
  - (3) All lowercase.
  - (4) No query parameters or session IDs on the canonical URL.
  - (5) No `#!` or fragment routing.
  - (6) Slug is 5 words or fewer, or about 60 characters or fewer. This is a convention, not an official limit.
  - (7) No stop-word or keyword stuffing; no word repeated in the slug.
  - (8) Slug is in the page's language.
  - (9) The URL is stable: changed URLs return a single 301/308 hop.
  - (10) Dates in the slug are discouraged for evergreen posts. This is best practice inferred from the "obsolete" title-rewrite trigger and redirect costs. No Google statement was found.
- Breadcrumbs often replace the URL path in SERPs, which further shrinks the URL's CTR role.

### Gaps
- No primary Google or Mueller quote on dates in blog URLs was found (the search returned nothing relevant).
- No experiment isolating a keyword-in-slug ranking effect was found.
- The official Bing guidelines page could not be fetched.

## Open Graph / social titles

### Takeaway
`og:title` is one of the sources Google uses for title links. Open Graph requires og:title, og:type, og:image and og:url, and og:description is optional. Keep og:title consistent with, though it may be shorter than, the `<title>` and H1.

### Cited Findings
- [SPEC] Required properties: `og:title` ("The title of your object as it should appear within the graph"), `og:type`, `og:image`, and `og:url` ("The canonical URL of your object"). Optional: `og:description` ("A one to two sentence description of your object"). — [ogp.me](https://ogp.me/)
- [OFFICIAL] `og:title` is listed among Google's title-link sources. — [Google title links](https://developers.google.com/search/docs/appearance/title-link)
- [OBSERVATIONAL] Ahrefs notes that social platforms may fall back to the meta description when OG tags are missing. — [Ahrefs](https://ahrefs.com/blog/meta-description-study/)

### Inferences
- Pass/fail checks:
  - (1) All four required OG properties are present.
  - (2) og:url equals the canonical URL.
  - (3) og:title does not contradict the title or H1 (shares core terms).
  - (4) og:description is present.

### Gaps
- No study was found that measures og:title's effect on Google rewrites.

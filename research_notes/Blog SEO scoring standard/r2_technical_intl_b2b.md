# Technical and international SEO eligibility, B2B intent and cannibalisation for blog articles (blog.se.com / se.com), as of 23 Oct 2026

This round adds to official_guidance.md section 4. That section listed several Google pages as "known, not re-fetched". The canonicalization, mobile-first, page-experience and pagination pages were fetched and verified this round. All Google docs were fetched on 2026-10-23; each one's "last updated" date is given.

## (a) Page-level technical eligibility checklist (checkable from HTML and HTTP response)

### Takeaway
Most eligibility gates can be checked from a single fetch and are binary:
- the URL returns 200, with no redirect chain;
- there is no noindex in the meta robots tag or the X-Robots-Tag header;
- robots.txt does not block it;
- there is one absolute, self-referencing canonical in `<head>`;
- hreflang tags (if any) are valid and reciprocal;
- it is served over HTTPS with a viewport tag;
- content and links are in `<a href>` HTML.

Core Web Vitals are a weak tiebreaker, not a gate.

### Cited Findings
- **HTTP status** — [Google HTTP/network errors, updated 2026-02-04](https://developers.google.com/search/docs/crawling-indexing/http-network-errors):
  - "an HTTP 2xx (success) status code doesn't guarantee indexing."
  - Google follows "up to 10 redirect hops".
  - 301/308 are a "strong" canonical signal; 302/307 are "weak".
  - Newly found 404 pages "aren't processed". Indexed 4xx URLs are dropped over time.
  - 5xx and 429 errors slow crawling. A persistent 5xx gets the URL removed.
  - A soft 404 is a 2xx page whose "content suggests an error ... an empty page or an error message".
- **Robots meta / X-Robots-Tag** — [Robots meta doc, updated 2026-03-24](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag):
  - Valid rules: all, noindex, nofollow, none, nosnippet, indexifembedded, max-snippet, max-image-preview, max-video-preview, notranslate, noimageindex, unavailable_after.
  - "In the case of conflicting robots rules, the more restrictive rule applies."
  - If robots.txt disallows a URL, Google never reads its meta or header rules.
- **Canonicalization** — [Canonicalization doc, updated 2026-07-10](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls):
  - Signal strength: redirects are "strong", rel=canonical is "strong", sitemap inclusion is "weak".
  - Use absolute URLs. The tag "is only accepted if it appears in the `<head>`".
  - Include a self-referential canonical.
  - "Don't use the robots.txt file for canonicalization purposes". Don't use noindex to choose a canonical.
  - Don't name different canonicals through different methods, e.g. a sitemap URL that differs from the rel=canonical URL.
  - Google prefers HTTPS unless there are conflicting signals.
  - rel=canonical with an hreflang attribute is "not used for canonicalization".
  - Google prefers URLs that belong to hreflang clusters. Canonicalize to a page in the same language.
- **Duplicate content across locales** — [Localized versions doc, updated 2026-09-21](https://developers.google.com/search/docs/specialty/international/localized-versions): localized pages "are only considered duplicates if the main content of the page remains untranslated."
- **Hreflang** — [same doc](https://developers.google.com/search/docs/specialty/international/localized-versions):
  - HTML link tags, HTTP headers and sitemaps "are equivalent".
  - "Each language version must list itself".
  - "If two pages don't both point to each other, the tags will be ignored."
  - x-default is the fallback "when no other language/region matches".
  - Use ISO 639-1 language codes and ISO 3166-1 Alpha-2 region codes. A region alone is invalid. `UK` and `EU` have no effect (use `en-GB`).
- **Mobile-first parity** — [Mobile-first doc, updated 2025-12-10](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing):
  - same content, same structured data, equivalent title and meta description;
  - "Don't lazy-load primary content upon user interaction";
  - same robots meta tags and the same alt text.
- **Page experience / CWV** — [Page experience doc, updated 2026-09-22](https://developers.google.com/search/docs/appearance/page-experience):
  - "Core Web Vitals are used by our ranking systems".
  - "other page experience aspects don't directly help your website rank higher".
  - "There is no single signal".
  - "Google Search always seeks to show the most relevant content, even if the page experience is sub-par."
  - The self-assessment covers HTTPS and "avoid using intrusive interstitials".
- **CWV thresholds** — [web.dev Vitals, updated 2024-10-31](https://web.dev/articles/vitals): LCP ≤2.5s, INP ≤200ms, CLS ≤0.1, measured at the "75th percentile of page loads, segmented across mobile and desktop".
- **JavaScript SEO** — [JS SEO basics, updated 2026-03-04](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics):
  - Processing runs in three phases: crawl, render, index.
  - Links must be `<a>` elements with an href.
  - On a noindex, Google "may skip rendering", so JS cannot reliably remove a noindex.
  - "The best way to set the canonical URL is to use HTML". A JS-set canonical should match the HTML one.
- **Pagination** — [Pagination doc, updated 2025-12-10](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading):
  - "Google no longer uses" rel next/prev.
  - Each page in a series gets its own canonical. Don't canonicalize the series to page 1.
  - Link the pages with `<a href>`.
- **Lighthouse SEO audits (technical baseline)** — [Lighthouse SEO docs](https://developer.chrome.com/docs/lighthouse/seo/meta-description):
  - meta description present;
  - descriptive link text;
  - valid hreflang;
  - valid rel=canonical;
  - successful HTTP status;
  - valid robots.txt;
  - no plugins;
  - tap targets sized;
  - manual check: structured data valid.
  - Lighthouse "doesn't evaluate the quality of your description" (it checks presence only).

### Pass/fail definitions (inferred from the above)

| Check | Pass | Fail |
|---|---|---|
| Final status | 200 after at most 1 hop (301/308) | 4xx, 5xx or soft 404. Warn on 302 or more than 1 hop |
| Indexability | No noindex/none in meta or X-Robots-Tag, and the URL is not disallowed in robots.txt | Any of these present |
| Canonical | Exactly one, in `<head>`, absolute, HTTPS, self-referencing (or pointing to a 200 indexable URL), and the same in raw HTML and rendered DOM | Missing, relative, multiple, pointing to a non-200/noindex URL, or conflicting with the sitemap |
| Hreflang (if used) | Self-reference present, valid ISO codes, return links present, x-default present, targets return 200 and are canonical | Invalid code (e.g. `en-UK`), no return link, or a target that is non-canonical |
| HTTPS | Served over HTTPS, and HTTP 301-redirects to HTTPS | Mixed content, or HTTP served |
| Mobile | `meta viewport width=device-width`, same primary content (no click-to-load body) | Missing |
| CWV (field data) | p75 LCP ≤2.5s, INP ≤200ms, CLS ≤0.1 | Poor. Treat as low weight |
| Links/rendering | Body text and internal links present in HTML as `<a href>` | Content only after JS interaction |

### Inferences
- In a scoring rubric, the indexability gates (status, noindex, robots, canonical) should be pass/fail multipliers, not weighted points. Google treats CWV as a minor factor that relevance overrides.

### Gaps
- I did not re-fetch the Google intrusive-interstitials page. Its wording is only confirmed through the page-experience self-assessment.
- I found no Google-published "poor" thresholds on the pages I fetched. The commonly cited values (LCP >4s, INP >500ms, CLS >0.25) are from memory and need verification.

## (b) Site-level items that need other data, and how to get it

### Takeaway
Several items can't be judged from one page:
- index coverage;
- the canonical Google actually chose;
- CWV field data;
- sitemap accuracy;
- hreflang cluster integrity;
- cannibalisation.

They need Search Console, CrUX or PageSpeed Insights, crawls, or IndexNow logs.

### Cited Findings
- Sitemaps — [Build sitemap, updated 2026-07-08](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap):
  - Google uses lastmod only "if it's consistently and verifiably" accurate.
  - "Google ignores `<priority>` and `<changefreq>`".
  - The limit is 50MB / 50,000 URLs per sitemap.
  - List canonical URLs only.
  - Add a `Sitemap:` line to robots.txt.
- IndexNow — [indexnow.org docs](https://www.indexnow.org/documentation):
  - Ownership is proven with a key file (8 to 128 characters) at the site root.
  - A POST can carry up to 10,000 URLs.
  - Submitted URLs are shared with all participating engines.
  - Responses: 200/202 OK, 400, 403 (bad key), 422, 429.
- IndexNow — [Bing IndexNow](https://www.bing.com/indexnow/getstarted): "Using IndexNow does not guarantee that web pages will be crawled or indexed". Cloudflare Crawler Hints is supported. Google is not named as a participant on either page.
- Multi-regional — [Managing multi-regional sites, updated 2025-12-10](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites):
  - Use different URLs per language.
  - "Don't use IP analysis to adapt your content". Googlebot crawls mostly from the US.
  - ccTLD, subdomain or subdirectory are all OK. URL parameters are not recommended.
  - "Google ignores locational meta tags".
  - Translating only the boilerplate is a poor experience.

### Inferences
Data sources for each item:

| Item | Source |
|---|---|
| Indexed status and Google-selected canonical | Search Console URL Inspection (API: urlInspection.index.inspect) |
| Field CWV | CrUX API / PageSpeed Insights (p75 by URL or origin) |
| Sitemap accuracy | Compare sitemap lastmod with `article:modified_time` / `dateModified` |
| Hreflang reciprocity | Crawl every alternate and confirm its return link |
| Cannibalisation | Search Console Performance, query + page dimensions |
| Bing freshness | Bing Webmaster Tools IndexNow report |

### Gaps
- I couldn't access Search Console or CrUX for se.com. No field data was gathered.

## (c) B2B/industrial intent, keyword targeting and cannibalisation (rubric checks)

### Takeaway
Use the four-type intent model (informational, navigational, commercial, transactional) and allow for mixed intent. Blog articles for engineers mostly serve informational and commercial-investigation intent.

Google downplays "cannibalisation" as a label. Duplication that matters is near-duplicate pages splitting the same intent, and Search Console query→page data is the detection method.

Topic clusters are a practitioner framework that Google has not endorsed.

### Cited Findings
- Semrush intent types — [Semrush, 2024-11-21](https://www.semrush.com/blog/search-intent/):
  - The four types are informational ("The user wants to learn about something"), navigational, commercial (comparing options, e.g. "best running shoes") and transactional ("buy ... size 10").
  - A query can carry mixed intent.
  - Google's rater guidelines use a different set: Know / Do / Website / Visit-in-person.
- Mueller on cannibalisation — [SEJ, 2025-09-22](https://www.searchenginejournal.com/google-answers-seo-question-about-keyword-cannibalization/556472/):
  - "If you have 3 different pages appearing in the same search result, that doesn't seem problematic to me".
  - "Reduce unnecessary duplication and spend your energy on a fantastic page, sure."
  - "pages aren't duplicates just because they happen to appear in the same search results page."
  - Search Console "shows data for when pages were actually shown".
- 2018 AMA (secondary source): Mueller said cannibalisation doesn't directly hurt rankings but can narrow the range of queries a site ranks for — [cognitiveSEO](https://cognitiveseo.com/blog/?p=20390) (secondary, unverified).
- Practitioner guidance: it matters only when the split has a cost, such as the wrong URL ranking or links diluted across near-duplicates — [Relevant Audience](https://www.relevantaudience.com/seo/keyword-cannibalization/).
- Topic clusters — [Ahrefs, 2022-02-24](https://ahrefs.com/blog/topic-clusters/):
  - A cluster is "interlinked pages about a particular subject": one broad pillar plus subtopic pages, with internal links between them.
  - Group subtopics that share intent, using "Traffic share by page" to avoid cannibalisation.
  - Google has never endorsed clusters. They "may help".
- Engineer buyer research — [TREW Marketing archives](https://www.trewmarketing.com/resources/research-archives): the annual State of Marketing to Engineers survey (2020 to 2025, with GlobalSpec and Elektor) covers where engineers search and which content they favour. The figures sit inside downloadable reports I did not access.
- Vendor statistics, low reliability:
  - 62% of the buying process is completed online before contacting sales, and search figures trace to a 2019 Thomas survey — [Webtonic](https://www.webtonic.io/blog/manufacturing-and-industrial-enterprise-seo-statistics).
  - An older Enquiro study put most technical buyers in the research stage (56.3%) — [SEJ](https://searchenginejournal.com/vertical-search-tapping-the-b2b-tech-buyer-market/5952).
- International localisation — [Google multi-regional](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites) and [localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions): main content must actually be translated. Translating only the template leaves the pages as duplicates.

### Inferences (rubric checks)
- Intent:
  - The article declares one primary query/intent, and its title, H1 and opening answer that intent.
  - Informational intent: a definition or how-to answered early.
  - Commercial investigation: comparisons, selection criteria, specifications, standards (IEC/UL/NEC), and total-cost-of-ownership (TCO) content.
- Technical long-tail: names specific standards, ratings (kVA, kW per rack, IP class) and part or product families. Searches by engineers are typically specific.
- Funnel: a relevant next step, such as a link to a se.com product, solution, whitepaper or tool page.
- Cluster: links to the category pillar page and 2 or more sibling articles, and is linked back from the pillar.
- Cannibalisation (site-level): in Search Console, flag queries where 2 or more blog/se.com URLs swap impressions for the same intent. Flag only near-duplicate intent, not mere co-ranking.
- Localisation: local-market keyword research (local terms such as "switchboard" vs "switchgear", local standards and units), not literal translation.
- My reasoning, not sourced: the localisation check is a recommendation and no data supports it.

### Gaps
- I did not get the Ahrefs intent guide or primary B2B engineer search statistics (the TREW reports are gated).
- I found no Google doc on keyword localisation. The localisation guidance above is practitioner consensus and wasn't sourced in this round.

## (d) Observations: how blog.se.com implements these (fetched with curl on 2026-10-23)

### Takeaway
blog.se.com is WordPress with Yoast SEO Premium v27.8, on Akamai CDN. The example article passes all indexability gates: 200, index/follow, self-canonical, HTTPS, viewport, BlogPosting-equivalent Article JSON-LD.

Weaknesses:
- no hreflang, and the blog is English only (en-US);
- the author schema lacks url/sameAs;
- all 5 images have empty alt;
- robots.txt has no Sitemap line, and it disallows `/category/` while the category sitemap lists archives at other paths;
- internal links to se.com carry UTM parameters.

www.se.com returned HTTP 403 to my plain curl (bot protection). I did not bypass it, so se.com country-site hreflang was not inspected.

### Cited Findings (all from direct fetches of [the example article](https://blog.se.com/datacenter/2026/10/13/modular-prefabricated-data-centers-enter-the-ai-era-and-boldly-go-where-no-data-centers-have-gone-before/), [robots.txt](https://blog.se.com/robots.txt) and [sitemap_index.xml](https://blog.se.com/sitemap_index.xml))
- **HTTP and response:**
  - 200, text/html UTF-8, served via Apache with an Akamai CDN cache HIT.
  - There is no X-Robots-Tag. There is a `Link: <https://blog.se.com/?p=167413>; rel=shortlink` header.
  - http:// returns 301 to https.
  - The URL without a trailing slash returns 301 to the slashed URL (one hop).
- **Robots meta:** `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1`.
- **Title vs H1:**
  - The title is "Modular, prefabricated data centers enter the AI era - Schneider Electric Blog". The format is shortened SEO title + " - Schneider Electric Blog".
  - The H1 (`h1.post-title`) and og:title carry the full long headline. The title is a shortened, consistent version of the H1.
- **Meta description:** present, about 420 characters (long, so it will be truncated). og:description is identical.
- **Canonical:** absolute, self-referencing, HTTPS, in `<head>`.
- **Hreflang:** none. `<html lang="en-US">`, og:locale en_US.
- **Schema (Yoast graph):**
  - Types: Article (not BlogPosting), WebPage, WebSite with SearchAction, BreadcrumbList (3 items), Person, ImageObject.
  - Article fields: datePublished 2026-10-13T12:00:00+00:00, dateModified 2026-10-16T04:29:27+00:00, articleSection ["Data Centers"], wordCount 943, inLanguage en-US.
  - The Person ("Steven Carlini") has a name and image but no url or sameAs.
- **Byline and date:**
  - The byline links to /author/steven-carlini/.
  - The visible date is `<time class="published" datetime="2026-10-13T08:00:00-0400">October 13, 2026`. It is consistent with the schema (the same instant).
  - No visible "updated" date was found.
- **Images:** 5 `<img>` tags, all with `alt=""`. 4 use `loading="lazy"`. og:image is 1200×630.
- **URL pattern:** `/{category}/{yyyy}/{mm}/{dd}/{slug}/`. Some use a subcategory, e.g. `/infrastructure-and-grid/power-management-metering-monitoring-power-quality/2020/03/03/slug/`. The slugs are long, full headlines.
- **Category structure:**
  - Top-level categories: datacenter, buildings, industry, infrastructure-and-grid, sustainability, digital-transformation, services.
  - Subcategory archives sit at e.g. /datacenter/architecture/.
  - /category/datacenter/ also returns 200.
- **robots.txt:**
  - Disallows /wp-admin/, /wp-includes/, plugin and theme folders, /comments/, /category/, /tag/, `/*?*` and /search/.
  - Allows /wp-content/uploads/20*.
  - Has **no Sitemap: directive**.
- **Sitemaps:**
  - The Yoast sitemap index lists post-sitemap1 to 7, page, podcast-transcript, category and post_tag sitemaps.
  - lastmod values are present.
  - The post_tag sitemap is listed even though /tag/ is disallowed in robots.txt.
- **Internal links:** cross-links to se.com country homepages (ww, us, ca, uk, ie...) use `?utm_source=blog.se.com...` parameters.
- **se.com:** `https://www.se.com/ww/en/` returned 403 to a non-browser request. I did not bypass the protection.

### Inferences
- Concrete fixes for the rubric:
  - add Sitemap lines to robots.txt;
  - stop listing the tag sitemap while /tag/ is disallowed, or allow /tag/ (blocked-but-in-sitemap is a conflicting signal);
  - add author url/sameAs;
  - write descriptive alt text;
  - trim meta descriptions to about 155 characters;
  - consider shorter slugs;
  - consider removing UTMs from internal links (my inference; internal UTMs can create parameter URL variants).
- There is no hreflang because the blog is single-language. That is correct as long as there are no translated equivalents. If country se.com sites republish translated versions, they need reciprocal hreflang, or canonicals to the original if they are untranslated.
- Article vs BlogPosting: Google's Article docs accept Article, NewsArticle and BlogPosting, so Article is not a failure.

### Gaps
- I checked only one article in depth. Other articles and category pages were not checked for consistency.
- No CWV or field data was gathered.
- I couldn't inspect se.com country blogs or their hreflang because of the 403.

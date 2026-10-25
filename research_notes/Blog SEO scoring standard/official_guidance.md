# Official Search-Engine Guidance on Blog/Content SEO (as of Oct 2026)

Classification tags: [C] content/on-page (judgeable from text + HTML), [T] technical, [O] off-page.
Verification tags: "fetched" = the page was read for these notes (Oct 23, 2026). "known, not re-fetched" = long-standing doc content I did not re-read this session. Check those before relying on them.

## 1. Google Search Essentials and spam policies

### Takeaway
The spam policies page (last updated 2026-08-28) lists 16 spam policies and 4 other demotion grounds. For a content rubric, the relevant ones are keyword stuffing, hidden text/links, scaled content abuse, scraping, thin affiliation, doorway abuse, site reputation abuse, expired domain abuse, cloaking, sneaky redirects, and link spam. Breaking a spam policy is a hard fail, not a matter of degree.

### Cited Findings
- Policy list, page last updated 2026-08-28 (fetched) — [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies):
  - Cloaking [T]: showing search engines different content than users, to manipulate rankings.
  - Doorway abuse [C/T]: pages or sites built to rank for similar queries that funnel users to less useful pages.
  - Expired domain abuse [O]: buying a lapsed domain and reusing it mainly to rank low-value content.
  - Hacked content [T].
  - Hidden text and link abuse [C]: text or links that search engines can see but people can't easily view.
  - Keyword stuffing [C]: overloading a page with keywords or numbers, often unnaturally.
  - Link spam [O/C]: links built mainly to manipulate rankings (buying, selling, excessive exchanges).
  - Machine-generated traffic; malicious practices, including back-button hijacking [T].
  - Misleading functionality [C]: promising a tool or service that isn't delivered.
  - Scaled content abuse [C]: mass-producing low-value pages "regardless of method" (AI, human, or both).
  - Scraping [C]: republishing other sites' content.
  - Site reputation abuse [O]: third-party content hosted mainly to exploit the host's ranking signals.
  - Sneaky redirects [T].
  - Thin affiliation [C]: affiliate pages with copied merchant descriptions and no added value.
  - User-generated spam [C]: spam in comments, forums, etc.
  - Other demotion grounds: legal removals, personal-information removals, policy circumvention, scam and fraud.
- Search Essentials has three parts: technical requirements (Googlebot isn't blocked, the page returns HTTP 200, indexable content), spam policies, and key best practices (helpful content, words people search for in prominent places such as titles, headings, alt text and link text, crawlable links, structured data). Known, not re-fetched — [Search Essentials](https://developers.google.com/search/docs/essentials).

### Inferences
- In a rubric, spam-policy violations work best as gates or penalties: keyword stuffing, hidden text, scraped or unedited mass-produced text, and thin affiliate content. They shouldn't be weighted positives.

### Gaps
- I did not re-fetch the exact wording of the Search Essentials technical requirements this session.

## 2. Helpful, people-first content; helpful content system folded into core; 2024-2026 updates

### Takeaway
Google's self-assessment questions (Content/Quality, Expertise, Who/How/Why) are the best official basis for scoring content. The helpful content system became part of core ranking in March 2024. Since then Google has run core updates roughly quarterly and spam updates frequently, and most recent ones came without a stated target.

### Cited Findings
- Self-assessment questions (fetched, paraphrased) — [Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content):
  - Content and quality [C]: original information, reporting, research or analysis; thorough coverage beyond the obvious; real added value over the sources it uses; a title or H1 that summarizes accurately and isn't exaggerated or shocking; worth bookmarking or sharing; magazine or book quality; more valuable than competing results; no spelling or style problems and no rushed feel; not mass-produced or spread thin across many creators or sites.
  - Expertise [C]: clear sourcing, evidence of expertise, information about the author or publisher; written or reviewed by someone who knows the topic; no easily checked factual errors.
  - Who [C]: bylines where readers expect them, linked to author background. Fabricated profiles (made-up names, AI-generated headshots, false credentials) are treated as deception.
  - How [C]: explain how the content was produced (for reviews: what was tested, how, with what evidence). Disclose automation or AI use where readers would wonder.
  - Why [C]: the content exists primarily to help people, not to attract search traffic.
  - Warning signs [C]: writing to a target word count ("no preferred word count"); changing dates without substantial updates; large volumes of unreviewed AI text.
- Ranking updates, 2024-2026 (fetched) — [Search Status Dashboard ranking history](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history):
  - Core updates: Mar 5 2024; Aug 15 2024; Nov 11 2024; Dec 12 2024; Mar 13 2025; Jun 30 2025; Dec 11 2025; Mar 27 2026; May 21 2026.
  - Spam updates: Mar 5 2024; Jun 20 2024; Dec 19 2024; Aug 26 2025; Mar 24 2026; Jun 24 2026; Aug 18 2026; Sep 24 2026.
- The February 2026 Discover core update started Feb 5 for US English users, with expansion planned — [Search Central blog](https://developers.google.com/search/blog/2026/02/discover-core-update).
- The March and May 2026 core updates had no companion blog post or stated goals. The May update finished June 2, 2026 — [SERoundtable](https://www.seroundtable.com/google-may-2026-core-update-done-41435.html), [SEJ](https://www.searchenginejournal.com/google-confirms-may-2026-core-update-is-now-rolling-out/575589/).
- March 2024: the helpful content system was absorbed into core ranking, and the scaled content abuse, site reputation abuse and expired domain abuse policies were introduced. Site reputation enforcement began May 5, 2024. Known, not re-fetched — [Search Central blog, Mar 2024](https://developers.google.com/search/blog/2024/03/core-update-spam-policies).

### Inferences
- The self-assessment questions turn directly into rubric items: originality, depth, an accurate title, a byline linking to a bio, method disclosure, sourcing, factual accuracy, and editing quality.

### Gaps
- I found no official descriptions of what the 2025-2026 core and spam updates specifically targeted. Google gave none for most of them.

## 3. E-E-A-T and YMYL in the Quality Rater Guidelines

### Takeaway
The QRG was revised on Jan 23 2025 and again on Sep 11 2025 (182 pages). The 2025 changes added scaled and low-effort AI content to the Lowest ratings and updated the YMYL definitions. Raters' scores train and evaluate ranking systems; they do not rank pages directly.

### Cited Findings
- The Sep 11 2025 revision added AI Overview rating examples and updated YMYL definitions, with civics broadened to cover elections and trust in public institutions. The previous revision was Jan 23 2025 — [SERoundtable](https://www.seroundtable.com/google-ads-related-searches-based-on-your-browsing-40092.html), [Marie Haynes](https://www.mariehaynes.com/google-quality-raters-now-rate-ai-overviews/).
- Google's AI-content doc points to QRG sections 4.6.5 (scaled content abuse) and 4.6.6 (low-effort, low-originality main content) and notes that rater ratings "don't directly affect rankings" (fetched) — [Using gen-AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content).
- Known, not re-fetched — [QRG PDF](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf):
  - Raters judge page purpose first, then main content quality, E-E-A-T, reputation and other factors.
  - The Jan 2025 revision added Lowest ratings for main content that is mostly auto- or AI-generated with little originality or added value, and for filler or paraphrased content.
  - Trust is the most important member of E-E-A-T.
  - YMYL topics (health, finance, safety, civics) are held to higher standards.

### Inferences
- The scoring signals here are page purpose clarity, main content effort and originality, visible author or creator information, and stricter rules on YMYL topics.

### Gaps
- I did not read the QRG PDF directly this session. Exact section numbers other than 4.6.5 and 4.6.6 are unverified.

## 4. Google on-page and technical documentation

### Takeaway
On-page guidance is consistent across Google's docs: a unique, descriptive, branded `<title>` that matches the H1; descriptive anchors and alt text; readable URLs; Article markup with author and dates. Core Web Vitals thresholds are LCP ≤2.5s, INP <200ms and CLS <0.1, and Google describes them only as "aligned with" what ranking rewards.

### Cited Findings
- Title links [C] (fetched) — [Title links doc](https://developers.google.com/search/docs/appearance/title-link):
  - Every page needs a `<title>`, descriptive and concise, unique per page, with no keyword stuffing and a brief site-name brand separated by a delimiter.
  - The main visual title (the H1) should be clear, and the title should be in the page's language and script.
  - Google builds title links from: `<title>`, the main visual title, `<h1>`, `og:title`, prominent styled text, other page text, anchors on the page, inbound link text, and WebSite structured data.
  - Rewrite triggers: half-empty, obsolete (e.g. an old year), or inaccurate titles; micro-boilerplate; no clear main title; language mismatch; a duplicated site name.
- SEO Starter Guide [C] (fetched) — [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide):
  - URLs: use descriptive words, since random identifiers are "less helpful".
  - Links: descriptive anchor text; `nofollow` for links you don't trust and for user-generated links.
  - Images: sharp images placed near relevant text, with short, descriptive alt text.
  - Headings: break long content into sections.
- Article structured data [C] (fetched) — [Article markup](https://developers.google.com/search/docs/appearance/structured-data/article):
  - "There are no required properties."
  - Recommended: `author` (Person or Organization), `author.name` (name only), `author.url` or `sameAs`, `datePublished` and `dateModified` (ISO 8601 with timezone), `headline` (concise), `image` (multiple high-resolution images, 16x9, 4x3 and 1x1).
  - Mark up every author on the page, each in a separate entry.
- Core Web Vitals [T] (fetched) — [CWV doc](https://developers.google.com/search/docs/appearance/core-web-vitals):
  - Good thresholds: LCP within 2.5s, INP under 200ms, CLS below 0.1. (The 75th percentile comes from web.dev and was not stated on the fetched page.)
  - Google "highly recommend[s]" good CWV, which it says "aligns with what our core ranking systems seek to reward".
- Generative AI content [C] (fetched, last updated 2026-10-01) — [Using gen-AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content):
  - AI is acceptable for research and structure. Mass-produced, no-value pages risk scaled content abuse.
  - Manually fact-check all AI output, including titles, meta descriptions, structured data and alt text.
  - Giving readers context on how content was made is suggested. Merchant Center requires the IPTC `TrainedAlgorithmicMedia` label on AI-generated images.
- AI Overviews and AI Mode (fetched, last updated 2025-12-10) — [AI features doc](https://developers.google.com/search/docs/appearance/ai-features):
  - "There are no additional requirements": the page must be indexed and eligible for a snippet.
  - "You don't need to create new machine readable files, AI text files, or markup", so llms.txt and special schema aren't needed.
  - Usual fundamentals apply: crawlability, internal links, page experience, content in text form, structured data that matches visible text.
  - Controls: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`, and Google-Extended (for training and grounding in other Google systems).
- Known, not re-fetched (verify before citing):
  - Meta descriptions [C]: Google often generates snippets from page text. Write unique, specific descriptions per page and don't fill them with keywords — [Snippets doc](https://developers.google.com/search/docs/appearance/snippet).
  - Images [C/T]: descriptive file names, alt text, captions and nearby text; image sitemaps are optional — [Image SEO](https://developers.google.com/search/docs/appearance/google-images).
  - Links [C/T]: crawlable `<a href>` links; `rel` values `sponsored`, `ugc` and `nofollow`; internal links to important pages — [Link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable).
  - Canonicalization [T]: `rel=canonical`, redirects and sitemaps are canonical signals — [Canonicalization](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).
  - Bylines and dates [C]: show a visible date with clear "published" or "updated" labels, consistent with the structured data — [Publication dates](https://developers.google.com/search/docs/appearance/publication-dates).
  - Mobile-first indexing [T]: the mobile version should carry the same content, structured data and metadata as desktop — [Mobile-first indexing](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing).
  - HTTPS [T] — [Page experience](https://developers.google.com/search/docs/appearance/page-experience).
  - Intrusive interstitials [T/C]: avoid interstitials that block content — [Interstitials](https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials).

### Inferences
- High-confidence rubric checks: a unique title that matches the H1 and includes the brand, no stale year in the title, a meta description present and unique, one clear H1, sectioned headings, descriptive anchors, alt text on content images, a readable slug, Article JSON-LD with author.url, datePublished and dateModified, and visible dates and byline consistent with the markup.

### Gaps
- Pages marked "known, not re-fetched" were not verified this session.
- I could not confirm the exact current wording of the page-experience doc.

## 5. 2024 Content Warehouse API leak

### Takeaway
The leaked documentation is authentic: 2,596 modules and 14,014 attributes, confirmed by Google on May 29 2024. It shows that attributes exist, but not their weights or whether they are currently used. Treat it as directional evidence only.

### Cited Findings
- What the leak was (fetched) — [Wikipedia](https://en.wikipedia.org/wiki/2024_Google_Search_documentation_leak):
  - Posted to GitHub around Mar 13 2024; became public in May 2024.
  - Analyzed by Rand Fishkin (SparkToro, May 27) and Mike King (iPullRank, May 28).
  - Google warned against conclusions drawn from "out-of-context, outdated, or incomplete information".
  - It contains no source code and no weights.
- Attributes it revealed (fetched) — [Wikipedia](https://en.wikipedia.org/wiki/2024_Google_Search_documentation_leak):
  - NavBoost (click-based re-ranking, also confirmed in US v. Google) [O].
  - Chrome attributes such as `chrome_trans_clicks` [O].
  - `siteAuthority` [O], which Google had publicly denied.
  - `hostAge` and sandbox-like signals [O].
- Practitioner readings of content attributes (secondary sources, interpretive) — [SE Ranking](https://seranking.com/blog/seo-news-google-api-data-leak/), [Searchable](https://www.searchable.com/blog/effort-attribute-google-content-warehouse-leak), [Hobo Web](https://www.hobo-web.co.uk/the-contenteffort-attribute-the-helpful-content-system-and-e-e-a-t-is-gemini-behind-the-hcu/):
  - `OriginalContentScore` [C]: a score for short content.
  - `titlematchScore` [C]: how well the title matches queries.
  - `contentEffort` [C]: read as an LLM-based estimate of effort, which would counter low-effort or AI-scaled content.
- Known from the King and Fishkin analyses, not re-fetched:
  - `lastSignificantUpdate` [C], date-related fields, and author fields (an `isAuthor`-type attribute and author entity data).
  - `siteFocusScore` and `siteRadius` [C/site-level]: topical focus.
  - [iPullRank](https://ipullrank.com/google-algo-leak) and [SparkToro](https://sparktoro.com/blog/an-anonymous-source-shared-thousands-of-leaked-google-search-api-documents-with-me-everything-you-need-to-know/). The iPullRank fetch failed with a DNS error.

### Inferences
- Responsible use: the leak can back rubric items that Google's own docs already support (title-query match, original or effortful content, real dated updates, authorship, topical focus). It shouldn't introduce new weights. Click and Chrome signals are off-page and can't be scored from a page.

### Gaps
- I could not fetch iPullRank's primary analysis. The exact attribute descriptions are unverified here.

## 6. Bing Webmaster Guidelines

### Takeaway
Bing rewrote its guidelines on Feb 27 2026 to cover Copilot and grounding. It names GEO, adds AI-specific abuse categories ("artificially engineered language", prompt injection), and recommends direct facts, consistent entity names, one topic per URL, and key information near the top. Bing documents per-directive controls over AI use, which Google has not done in the same way.

### Cited Findings
- Rewrite details, Feb 27 2026 — [SEJ](https://www.searchenginejournal.com/bing-adds-geo-to-official-guidelines-expands-ai-abuse-definitions/568442):
  - Grounding and citations are treated as eligibility outcomes. Advice for grounding [C]: state facts directly, use clear and consistent entity names, one topic per URL, essential information near the top.
  - Abuse definitions: "Keyword Stuffing and Artificially Engineered Language" (now covers content engineered to trigger citations); "Prompt Injection and AI Manipulation"; "Large-scale content generated without oversight, quality control, or editorial review" may be excluded from the index.
  - Copilot directives [T]: NOARCHIVE excludes content from Copilot answers and grounding; NOCACHE limits Copilot to URL, title and snippet; NOSNIPPET and data-nosnippet may limit citations; a data-snippet attribute controls which text can be cited.
- The AI Performance report (public preview, Feb 2026) shows how often a site is cited in Copilot and Bing AI answers. It advises clear headings and tables — [Bing blog](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview).
- Missing, duplicate or too-short titles and descriptions can hurt indexing and grounding eligibility. Secondary source quoting Bing, unverified — [geotoolbox](https://geotoolbox.ai/blog/meta-tags-for-seo.md).
- IndexNow [T]: a push protocol for added, changed or deleted URLs, supported by Bing, Yandex and Seznam — [gracker.ai (secondary)](https://gracker.ai/seo-101/indexnow-seo-guide). Official source: [indexnow.org](https://www.indexnow.org).
- Known, not re-fetched: Bing has long listed relevance, quality and credibility, user engagement, freshness, location and page load time as ranking parameters, and still reads meta keywords as a spam signal only — [Bing guidelines](https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a).

### Inferences
- Rubric items specific to Bing and AI: answer-first or lead-with-facts structure, consistent entity naming, a single-topic page, no prompt-injection or engineered text, and no NOCACHE or NOARCHIVE if AI citation is wanted.

### Gaps
- Bing's guidelines page renders client-side and could not be fetched. The current wording on titles, meta and headings is unverified.

## 7. What Google says are NOT ranking factors

### Takeaway
Google explicitly calls these myths or non-factors: meta keywords, content length or word count, keywords in the domain or URL (beyond minor effect), heading count and order, a duplicate content "penalty", subdomain vs. subdirectory, and E-E-A-T as a direct factor. Core Web Vitals are "aligned with" ranking, not described as a major factor.

### Cited Findings
- From the SEO Starter Guide (fetched) — [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide):
  - "Google Search doesn't use the keywords meta tag."
  - "The length of the content alone doesn't matter for ranking purposes."
  - Keywords in the domain or URL have "hardly any effect beyond appearing in breadcrumbs".
  - Heading order doesn't matter for Search, and there is no ideal number of headings.
  - Duplicate content is "not something that will cause a manual action".
  - Subdomains vs. subdirectories: use whatever suits the business.
  - PageRank is one of many signals.
  - Is E-E-A-T a ranking factor? "No, it's not."
- Google has "no preferred word count" (fetched) — [Creating helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
- Rater ratings "don't directly affect rankings" (fetched) — [Using gen-AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content).
- No special AI files or markup are needed for AI features (fetched) — [AI features doc](https://developers.google.com/search/docs/appearance/ai-features).

### Inferences
- A rubric shouldn't reward word count, keyword density, meta keywords, keyword-exact domains, H-tag hierarchy as a ranking factor (it can still count for accessibility), or llms.txt. Author bios should be scored as trust or E-E-A-T evidence, not as a direct ranking signal.

### Gaps
- I did not retrieve verbatim, dated John Mueller or Danny Sullivan quotes (for example on keyword density, author bios, or CWV as a "tie-breaker"). Primary links for these weren't found this session.

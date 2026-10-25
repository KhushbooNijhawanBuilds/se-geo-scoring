# Round 2: on-page SEO elements of blog articles beyond titles (as of 23 Oct 2026)

Scope note: this round fetched 7 Google primary docs in full: Link best practices, Image SEO, Publication dates, SEO Starter Guide, Spam policies, Article structured data and Creating helpful content. The other items came from search summaries of secondary coverage, marked [secondary]. That gives about 20 distinct sources, short of the 25 asked for.

Fetch caveats:
- Google pages were read through a summarising fetcher. Text in quotation marks was returned as verbatim. Items marked "paraphrase" were not.
- The Bing guidelines page returned no content when fetched, so Bing is not covered here.
- Zyppy's study page was not opened (the URL tried returned 404). Its figures come from search summaries.

Evidence labels: [G] = official Google wording; [EXP] = controlled experiment; [CORR] = correlation study; [VENDOR] = study by a company that sells SEO tools or services.

## 1. Headings (H1 count, order, passage ranking)

### Takeaway
Google says heading order and heading count don't matter for ranking. Mueller has said one, several or no H1s all work. Headings matter for structure and accessibility, not as a ranking boost. I found no SearchPilot heading test.

### Cited Findings
- [G] SEO Starter Guide (last updated 2025-12-10): semantic order is "fantastic for screen readers", but "from Google Search perspective, it doesn't matter if you're using them out of order." The guide also says there is no ideal number of headings per page. — https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- [G, secondary] Mueller: "Our systems aren't too picky and we'll try to work with the HTML as we find it, be it one H1 heading, multiple H1 headings or just styled pieces of text without semantic HTML at all." — https://www.searchenginejournal.com/h1-headings-for-google/406720/
- [G, secondary] Mueller on H1s: "It's not a secret ranking push." He described H1s as giving structure "so that users and search engines can understand which parts of a page are kind of under different headings". — https://searchengineland.com/?p=322909 ; https://searchengineland.com/if-google-says-h1s-dont-matter-for-rankings-why-should-you-use-them-heres-why-323056
- [G, secondary] Passage ranking went live in February 2021 for US English queries. Sullivan: "We're still indexing pages and considering info about entire pages for ranking." Splitt said no specific changes are needed. No Google statement found ties passage ranking to headings. — https://www.seroundtable.com/google-passage-ranking-live-30920.html ; https://www.searchenginejournal.com/google-passage-ranking-martin-splitt/388206/
- [G] Title links doc (round 1): the main visual title or H1 is one of the sources Google uses to build title links. A clear H1 that matches the `<title>` reduces rewrites. — official_guidance.md §4
- Evidence gap: no SearchPilot test on H1 or H2 changes surfaced in search.

### Rubric checks
- PASS if there is exactly one visually dominant main title, marked as an H1 or equivalent, and it matches the `<title>` topic. Basis: title-link doc. Don't fail a page for having several H1s (Mueller).
- PASS if pages over about 300 words have H2 or H3 subheads that describe their sections. Basis: Starter Guide on breaking long content into sections. The 300-word threshold is a heuristic, not Google's.
- Heading order: informational only (accessibility), never a fail for SEO.

## 2. Keyword/topic placement and stuffing

### Takeaway
Google has no "keyword in first paragraph" rule. The current Starter Guide says to think about the words users search for and notes that Google's language matching is sophisticated. Older Google advice to put words "in prominent places" no longer appears in the 2025 Starter Guide; treat it as superseded. Keyword stuffing is defined in the spam policy.

### Cited Findings
- [G] Starter Guide: "Think about the words that a user might search for to find a piece of your content". Google's "language matching systems are sophisticated", so exact terms aren't always required. — Starter Guide URL above
- [G] Starter Guide: "Excessively repeating the same words over and over (even in variations) is tiring for users" and "keyword stuffing is against Google's spam policies." — same
- [G] Spam policies (last updated 2026-08-28): "Keyword stuffing refers to the practice of filling a web page with keywords or numbers in an attempt to manipulate rankings in Google Search results." Examples include "Repeating the same words or phrases so often that it sounds unnatural" and "Blocks of text that list cities and regions that a web page is trying to rank for". — https://developers.google.com/search/docs/essentials/spam-policies
- [G] Starter Guide: "Google Search doesn't use the keywords meta tag."
- SUPERSEDED: older Starter Guide versions told sites to include words people would look for in prominent places. The fetched 2025-12-10 Starter Guide does not contain that wording. The older text was not re-fetched to confirm it.
- Evidence: round 1 found no sourced data on keyword-in-first-paragraph. No new evidence was found this round.

### Rubric checks
- PASS if the primary topic phrase or a close variant appears in the H1 and in the first 100–150 words. This is a clarity heuristic, not a Google rule, so weight it low.
- FAIL if any non-stopword phrase is repeated unnaturally, or if the page has lists of cities or keywords. Suggested trigger: the exact primary phrase makes up more than about 3% of words, or appears in more than half of the subheads. The thresholds are heuristic; the basis is the spam-policy definition.
- No density target, and no meta keywords check.

## 3. Internal links and anchor text

### Takeaway
Google wants crawlable `<a href>` links, with descriptive, concise anchors that make sense out of context. Every important page should be linked from at least one other page. There is no ideal link count. The evidence is correlational (Zyppy) plus a few vendor A/B tests (SearchPilot).

### Cited Findings
- [G] Link best practices (last updated 2025-12-10): "Generally, Google can only crawl your link if it's an `<a>` HTML element" with an `href`. — https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- [G] Same doc: "Good anchor text is descriptive, reasonably concise, and relevant to the page that it's on." It gives "Click here" as the example to avoid. Self-test: "Try reading only the anchor text (out of context) and check if it's specific enough to make sense by itself." It also says not to cram keywords into anchors.
- [G, paraphrase] Same doc: every page you care about should have a link from at least one other page on the site. There is no ideal number of links per page.
- [CORR, VENDOR-adjacent] Zyppy (Cyrus Shepard) studied 23M internal links across about 1,800 sites and about 520K URLs. URLs with more distinct internal anchor variations correlated with more Google traffic. — https://zyppy.com/seo/internal-links-study/
- [secondary, Zyppy page not opened] Pages with 40–44 internal links drew about 4× the clicks of pages with 0–4 links, and the curve plateaued after about 45 links. — https://www.nearmedia.co/internal-links-drive-clicks-google-support-decline-social-vs-search-growth/
- [secondary, unconfirmed] Pages with at least one exact-match internal anchor had about 5× the traffic. — https://seojuice.com/blog/internal-linking-statistics-2026/
- Note: "23 billion" figures attributed to Ahrefs appear to be an error. Use 23 million.
- [EXP, VENDOR] SearchPilot tests:
  - Adding nearby-region links to about 8,000 regional pages gave a +7% organic uplift on the pages receiving the links (Jan 2021).
  - Adding related-article links lifted the donor pages, with no conclusive effect on recipient pages.
  - Fixing internal links that pointed to 301 redirects gave -1% to +4%, not significant.
  — https://www.searchpilot.com/resources/case-studies/seo-split-test-lessons-nearby-location-links ; https://searchpilot.com/resources/case-studies/impact-of-internal-linking-seo ; https://www.searchpilot.com/resources/case-studies/change-internal-redirect-links-for-seo

### Rubric checks
- FAIL if any in-content link is not an `<a href>` (JS-only onclick, a span). Basis: [G].
- FAIL if any anchor is generic ("click here", "read more", "this", a bare URL used as the only anchor). Basis: [G] out-of-context test.
- PASS if the post has at least 3 contextual internal links to relevant pages, and at least 1 to a pillar or hub page. The threshold is a heuristic; Google gives no number.
- PASS if the post itself is linked from at least one other page (not an orphan). Basis: [G].
- PASS if every anchor is 2–8 words. This is a heuristic for "reasonably concise".

## 4. Outbound links

### Takeaway
Google says citing trusted sources can build trust, and that nofollow should be used only for untrusted, paid or user-generated links. Reboot's small experiment suggested authoritative outbound links help rankings, but it was 10 sites ranking for a made-up word.

### Cited Findings
- [G] Link best practices: "Use nofollow only when you don't trust the source, and not for every external link on your site." "If you were paid in some way for the link, qualify these links with sponsored or nofollow." For links users can insert, "add ugc or nofollow to these links too." — links doc URL above
- [G] Starter Guide: if you can't trust a page you link to, add "a nofollow or similar annotation to the link".
- [EXP] Reboot Online: 10 new domains with articles on the invented term "Phylandocic".
  - 5 sites linked to Oxford, Cambridge and the Genome Research Institute; 5 had the same mentions as plain text.
  - The 5 linking sites took the top 5 positions, and rankings stabilised after 8–10 weeks.
  - Reboot says it reran the test in April 2020 with the same result.
  - Caveats: tiny sample, a non-competitive term, and dofollow vs nofollow was not tested.
  — https://rebootonline.com/blog/long-term-outgoing-link-experiment/ ; https://www.searchenginejournal.com/study-shows-outgoing-links-have-positive-effects-on-seo/157431/
- SEJ's ranking-factor review calls the evidence "not exactly convincing". — https://www.searchenginejournal.com/ranking-factors/outbound-links/

### Rubric checks
- PASS if factual claims or statistics link to their primary or authoritative source (at least 1 outbound citation per post that has stats). Basis: [G] trust, plus Reboot [EXP].
- FAIL if affiliate or paid links lack `rel="sponsored"` or `rel="nofollow"`. Basis: [G].
- FAIL if every external link is nofollowed. Basis: [G] "not for every external link".

## 5. Images and alt text

### Takeaway
Google's image doc (last updated 2026-03-02) calls alt text "the most important attribute" for image metadata. It also asks for descriptive filenames, images near relevant text, responsive images with a `src` fallback, and supported formats including WebP and AVIF. Lazy loading is not covered in that doc.

### Cited Findings
- [G] "The most important attribute when it comes to providing more metadata for an image is the alt text". Write "useful, information-rich content that uses keywords appropriately". Avoid keyword stuffing in `alt` attributes. Best example: `alt="Dalmatian puppy playing fetch"`. — https://developers.google.com/search/docs/appearance/google-images
- [G] "use filenames that are short, but descriptive". Example: `my-new-black-kitten.jpg`, not `IMG00023.JPG`.
- [G] "Google extracts information about the subject matter of the image from the content of the page"; "make sure images are placed near relevant text".
- [G] Responsive images: use `<picture>` or `srcset`, and "always specify a fallback URL using the `src` attribute".
- [G] Supported formats: "BMP, GIF, JPEG, PNG, WebP, SVG, and AVIF". The file extension should match the actual file type.
- [G] Image sitemaps can list CDN URLs in `<image:loc>`. They are optional.
- [G] Starter Guide: alt text is "a short, but descriptive piece of text that explains the relationship between the image and your content".
- Evidence: I found no controlled test showing alt text affects web (non-image) rankings.

### Rubric checks
- FAIL if a content image (not decorative) has missing or empty alt. FAIL if alt text is stuffed (more than about 125 characters, or a list of keywords). Basis: [G]. The 125-character figure is a screen-reader convention, not Google's.
- PASS if image filenames are descriptive words, not camera or CMS IDs.
- PASS if every `<img>` has a `src` (including when `srcset` is used), and uses a supported format with the right extension.
- PASS if at least 1 relevant image sits near the text it illustrates (optional for text-only posts).
- Lazy loading: don't lazy-load the LCP or hero image. This comes from web.dev and Core Web Vitals practice, not the image doc.

## 6. Structured data

### Takeaway
Article/BlogPosting markup has no required properties. Google recommends author (with url or sameAs), datePublished, dateModified, headline and image. Google says structured data does not improve rankings; it makes pages eligible for rich results. FAQ rich results were restricted in August 2023 and HowTo rich results were later dropped. Google says no special markup is needed for AI features.

### Cited Findings
- [G] Article structured data (last updated 2026-09-08):
  - `author.url` is "A link to a web page that uniquely identifies the author of the article" (or use `sameAs`).
  - `datePublished` and `dateModified` use ISO 8601 and should include a timezone.
  - `headline`: "Consider using a concise title, as long titles may be truncated on some devices."
  - Images: multiple high-resolution images, each at least 50K pixels (width × height), in 16x9, 4x3 and 1x1.
  - Author best practices: mark up every author, each in a separate entry; put only the name in `author.name`; use Person or Organization correctly and never Thing.
  — https://developers.google.com/search/docs/appearance/structured-data/article
- [G, secondary] Mueller, April 2025: "Structured data won't make your site rank better." He said it is "used for displaying the search features listed in" the search gallery. — https://www.seroundtable.com/google-structured-data-ranking-39232.html ; https://www.searchenginejournal.com/google-confirms-that-structured-data-wont-make-a-site-rank-better/544433/
- [G] August 8, 2023: FAQ rich results are shown only for "well-known, authoritative government and health websites", and HowTo was limited to desktop. Unused markup "does not cause problems for Search". — https://developers.google.com/search/blog/2023/08/howto-faq-changes
- SUPERSEDED: Google's earlier FAQ and HowTo rich-result eligibility for all sites. HowTo was reportedly removed fully in September 2023; this was not verified from the primary doc.
- [G] AI features doc (round 1): "You don't need to create new machine readable files, AI text files, or markup". Structured data should match visible text.
- [EXP, VENDOR] SearchPilot ran schema tests (FAQ markup removal; JSON-LD vs Microdata). Outcomes were not retrieved (see ranking_evidence.md).

### Rubric checks
- PASS if valid Article or BlogPosting JSON-LD is present with: headline, at least one image, datePublished, dateModified, author with @type Person and a name, and author.url or sameAs. Basis: [G] recommended properties.
- FAIL if the marked-up dates or author differ from the visible ones. Basis: [G].
- PASS if BreadcrumbList is present (optional, low weight).
- PASS if Organization or publisher markup exists somewhere on the site (optional, low weight).
- Do not award points for FAQPage or HowTo expecting rich results (rich-result value is low).
- Score schema as a clarity and eligibility check, not as a ranking factor.

## 7. Dates and bylines

### Takeaway
Google asks for a prominent visible date with a clear label, matching dates in structured data, and no future dates. The helpful-content doc flags changing dates without substantial change, and encourages accurate bylines.

### Cited Findings
- [G] Publication dates (last updated 2025-12-10):
  - "Add a user-visible date to the page and feature it prominently", with labels such as "Published" or "Last updated".
  - "The date is required; the time is not."
  - "Ensure that the date (and optional time and timezone) match between the equivalent user-visible and structured values."
  - "Don't specify future dates".
  - If Google picks the wrong date, "consider removing some or all other dates that appear on the page."
  — https://developers.google.com/search/docs/appearance/publication-dates
- [G] Creating helpful content (last updated 2026-10-05):
  - "Are you changing the date of pages to make them seem fresh when the content has not substantially changed?"
  - Google "strongly encourage[s] adding accurate authorship information, such as bylines to content where readers might expect it".
  - Fabricated author profiles are deceptive.
  — https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Anecdote, outdated: a 2016 blog post said a fake "Updated" line moved a page up 11 places. This is a single anecdote, not evidence. — https://www.brandignity.com/2016/12/google-freshness-factor/

### Rubric checks
- PASS if a visible, labelled published date or updated date is shown near the title.
- PASS if the visible date matches the JSON-LD date (same day).
- FAIL if the date is in the future, or if dateModified is newer than the last substantive edit (check against the diff when available).
- PASS if a visible byline links to an author page with a bio or credentials, and the same URL is used as author.url.

## 8. Readability

### Takeaway
No Google statement or study supports readability scores as a ranking factor. Mueller (2018) said he knew of no algorithms using basic readability scores. Ahrefs and Portent found little or no correlation. Readability is a user and indirect factor only.

### Cited Findings
- [G, secondary] Mueller (2018) was not aware of algorithms that use simple readability scores. — https://www.searchenginejournal.com/ranking-factors/reading-level-ranking-factor/
- [CORR, VENDOR] Ahrefs: across about 15K keywords, there was virtually no correlation between Flesch Reading Ease and position. — https://ahrefs.com/blog/flesch-reading-ease/
- [CORR, VENDOR] Portent: reading level was about the same at position 1 as at position 100. Reported sample sizes conflict (750K vs 5.8M pages). — https://portent.com/?p=56359 ; https://www.tryanalyze.ai/blog/flesch-reading-ease
- Plain language for non-native readers: no Google-specific guidance was found this round. Use this as a user-focused heuristic.

### Rubric checks
- Informational or low weight only: Flesch-Kincaid grade at or below about 9–10 for general B2B audiences, sentence length about 20 words on average, and paragraphs of 4 sentences or fewer. Basis: plain-language convention, not ranking evidence.

## 9. Content length and depth

### Takeaway
Google says plainly that length alone doesn't matter and that it has no preferred word count. Correlation studies show length is evenly distributed across the top 10 (see round 1). Score topic coverage instead of length.

### Cited Findings
- [G] Starter Guide: "The length of the content alone doesn't matter for ranking purposes." There is no minimum or maximum word count.
- [G] Creating helpful content: "Google has a preferred word count? (No, we don't.)"
- [CORR, VENDOR] Backlinko: the average first-page result has 1,447 words, and word count is evenly distributed across the top 10 (ranking_evidence.md).

### Rubric checks
- No word-count pass or fail.
- PASS if the post covers the subtopics and questions searchers expect (judged against the SERP or a topic list), and adds original detail such as data, examples or first-hand experience.

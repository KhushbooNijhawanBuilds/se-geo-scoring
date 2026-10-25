# SEO scoring and audit tools: rubrics and known flaws (as of Oct 2026)

## Yoast SEO / Yoast readability, Rank Math, AIOSEO TruSEO

### Takeaway
Yoast and Rank Math are keyphrase-centric, pass/fail traffic-light checklists. Rank Math publishes concrete thresholds. Yoast's marketing pages omit thresholds; numbers come from its open-source `yoastseo` package docs and secondary guides. Both still keep keyword density and length checks.

### Cited Findings
- Yoast SEO analysis has 18 checks: keyphrase in introduction, keyphrase length, keyphrase density, keyphrase in meta description, keyphrase in subheadings, keyphrase in link text, keyphrase in image alt, keyphrase in title, keyphrase in slug, previously used keyphrase, keyphrase distribution (Premium), text length, outbound links (present and followed), internal links (present and followed), SEO title width, meta description length, taxonomy text length, and stale cornerstone content (Premium). The features page gives no numeric thresholds. — [Yoast SEO analysis features](https://yoast.com/features/seo-analysis/)
- Yoast readability checks: subheading distribution, paragraph length, sentence length, consecutive sentences, passive voice, transition words. Premium adds word complexity and text alignment. Some checks are language-specific (passive voice, transition words). Default sentence-length upper limit is 20 words. — [Yoast readability](https://yoast.com/features/readability-analysis/); [yoastseo package readability scoring doc](https://unpkg.com/yoastseo@3.6.0/build/scoring/assessments/SCORING%20READABILITY%20PRODUCT.md)
- Paragraph length scoring in the yoastseo package (v3.6.0 doc): green (score 9) at 70 words or fewer, orange (score 6) at 70-100 words, red (score 3) above 100 words. Assessments are scored on a 3/6/9 scale. — [yoastseo readability scoring doc](https://unpkg.com/yoastseo@3.6.0/build/scoring/assessments/SCORING%20READABILITY%20PRODUCT.md)
- Keyphrase density is green between 0.5% and 3% in the free plugin (secondary guide, possibly dated). — [InMotion Hosting](https://www.inmotionhosting.com/support/?p=97666)
- A 300-word minimum text length is generally advised. — [Yoast Academy PDF](https://academy.yoast.com/app/uploads/sites/4/2021/08/3_3_content_analysis_factors_be.pdf)
- Meta description check expects 120-156 characters. Yoast briefly allowed 320, then reverted to 156 in v7.6 (2018). — [Yoast Shopify editor help](https://yoast.com/help/yoast-seo-for-shopify-editor/); [travis.media](https://travis.media/yoast-meta-description-length-reduced-7-6-update)
- Rank Math's tests, with thresholds:
  - **Basic SEO:** keyword in SEO title (ideally in the first 50 chars), in meta description, in URL, and in the first 10% of content (first 300 words for short posts). Keyword in content. Content length: >2,500 words = 100%, 2,000-2,500 = 70%, 1,500-2,000 = 60%, 1,000-1,500 = 40%, 600-1,000 = 20%, <600 = 0%.
  - **Additional:** keyword in a subheading and in image alt. Keyword density 1-1.5% for full marks, warning above 2.5%. URL of 75 characters or fewer, including domain. External links, at least one of them followed. Internal links. Focus keyword unique across posts. "Use Content AI".
  - **Title readability:** keyword in the first 50% of the title, sentiment word, power word, number.
  - **Content readability:** table of contents, no paragraph over 120 words, media (1 to pass, 4 for full marks).
  - **Score bands:** 81+ green, 51-80 yellow, <50 red.

  — [Rank Math KB: score 100 in tests](https://rankmath.com/kb/score-100-in-tests/)

### Inferences
- Rank Math's length ladder (2,500+ words for full marks) and its sentiment, power-word and number title tests reward padding and clickbait, not usefulness. Reuse the structural checks (keyword in title, H1, intro and slug; alt text; links; paragraph length). Drop or soften density, raw length, and the power-word heuristics.
- Exact-match keyphrase checks penalise synonyms. Yoast partly addresses this with synonyms and keyphrase forms (Premium).

### Gaps
- I could not retrieve a current (2026) official page with Yoast thresholds for passive voice (commonly cited as 10%), transition words (commonly 30%), subheading distribution (commonly 300 words), Flesch bands, or title pixel width. These are unverified here. Check the current `yoastseo` package source.
- I did not research the AIOSEO TruSEO check list.

## Google Lighthouse SEO audit

### Takeaway
Lighthouse SEO is a small technical checklist, not a content-quality score. Every automated audit is weighted equally. The structured-data audit is manual and does not count toward the score.

### Cited Findings
- Audits:
  - Understanding content: meta description present, descriptive link text, valid hreflang, valid rel=canonical.
  - Crawl and index: successful HTTP status, valid robots.txt, no plugins.
  - Mobile: tap target sizing.
  - Manual: structured data is valid.

  "Each SEO audit is weighted equally... except for the manual" structured-data audit. — [Lighthouse SEO docs](https://developer.chrome.com/docs/lighthouse/seo/meta-description)

### Inferences
- Most of these can be checked from HTML alone. Robots.txt, HTTP status and the indexability effect of robots directives need a fetch.

### Gaps
- I did not check whether "page is blocked from indexing", "image alt", or "crawlable links" are still in the 2026 list. Older versions had them. Verify against the current Lighthouse release.

## Semrush, Ahrefs, Screaming Frog, Sitebulb, Moz

### Takeaway
Site-audit "health" scores are crawl-level aggregates of technical errors, not page-content scores. Ahrefs' formula is fully transparent. Semrush's uses unpublished weights.

### Cited Findings
- Ahrefs Health Score = internal URLs with no Error-level issues ÷ total internal URLs crawled × 100. Warnings and notices don't count. — [Ahrefs help](https://help.ahrefs.com/en/articles/1424673-what-is-health-score-in-ahrefs-site-audit)
- Semrush Site Health (0-100%) is based on errors and warnings relative to the number of checks performed. Errors weigh more than warnings, and a given warning may have a 10-fold weaker effect than an error. Notices do not affect the score. There are over 140 checks. — [Semrush KB site audit overview](https://www.semrush.com/kb/540-site-audit-overview); [Semrush blog](https://www.semrush.com/blog/website-health/)

### Inferences
- Ahrefs' approach has a weakness: one error, whatever its severity, makes a whole page "unhealthy". A blog score should weight issues by severity instead.

### Gaps
- I did not retrieve rubrics for Semrush SEO Writing Assistant, Semrush On Page SEO Checker, Screaming Frog checks, Sitebulb hints (priority levels), or the Moz On-Page Grader. Research time ran out.

## Content optimisation scores (Surfer, Clearscope, MarketMuse, Frase, NeuronWriter)

### Takeaway
These tools score a draft against the top SERP results (term and NLP-entity coverage, length, structure). Independent and vendor studies both find only weak correlations with rankings, roughly 0.17-0.30.

### Cited Findings
- Surfer Content Score:
  - It is a 0-100 score that compares a draft against the top 20 ranking pages. It now combines an SEO Score with an AI Search Score.
  - The AI Search Score has two parts: Facts Coverage, and Upfront Intent Alignment (how early the page answers the question).
  - Factors include main, partial and NLP terms, "True Density" (where terms appear), title, H1, headers, paragraphs, length relative to the SERP, images and alt text, OG/meta, internal links, and E-E-A-T.
  - Surfer says natural use of terms is weighted above structure. It publishes no weights.
  - Bands: 0-33 poor, 34-66 partial, 67-100 optimum.
  - Audit scores the whole `<body>`, including navigation and footer, so its score differs from the Editor's.

  — [Surfer docs: What is Content Score](https://docs.surferseo.com/en/articles/5700317-what-is-content-score)
- Ahrefs study (2025):
  - Method: 20 keywords; Surfer, Frase, NeuronWriter, Clearscope and Ahrefs AI Content Helper; per-keyword Spearman and Kendall correlations, averaged. Clearscope letter grades were converted to numbers using ChatGPT.
  - Result: "weak correlations everywhere". NeuronWriter and Ahrefs' tool did best. Surfer, Frase and Clearscope were very weak.
  - Advice: use scores to measure topic coverage, match the range of top pages instead of chasing 100, note that some tools can be gamed by pasting in terms, and check intent first.
  - Ahrefs sells a competing tool.

  — [Ahrefs content score study](https://ahrefs.com/blog/seo-content-score-study/)
- Surfer claims a 0.28 correlation across 10,000 queries (vendor study). Clearscope disputes Surfer's method and cites Ahrefs data showing Clearscope ahead, .30 vs .27. An Originality.ai figure, cited by Surfer, puts Surfer at 26% and Clearscope at 17.5%. — [Surfer study](https://surferseo.com/blog/surfer-content-score-study); [Clearscope vs Surfer](https://www.clearscope.io/blog/clearscope-vs-surferseo)

### Inferences
- The studies conflict, all are small or vendor-run, and correlation is not causation: top pages share terms because they rank, not the reverse. SERP-mirroring scores also push content toward sameness. A blog score should use topic and entity coverage as one moderate component, not the headline number.

### Gaps
- I did not retrieve the formulas for Clearscope grades, MarketMuse Content Score and Topic Authority, Frase, or NeuronWriter. I found no rigorous independent peer-reviewed test.

## Criticisms and Google statements

### Takeaway
Google repeatedly says it does not use third-party tool scores. As of June 2026 it has a formal Search Central page on third-party SEO tools.

### Cited Findings
- John Mueller (#AskGooglebot): Google does not use third-party SEO tool scores, whether for authority or spamminess. Transparently calculated scores can still help point out actual issues. — [Search Engine Journal](https://www.searchenginejournal.com/google-we-dont-use-third-party-seo-tool-scores-for-rankings/493956); [Search Engine Land](https://searchengineland.com/?p=430771)
- Danny Sullivan (2020): Google does not use third-party scores, such as BBB ratings, in ranking. — [SERoundtable](https://seroundtable.com/google-bbb-ratings-seo-29040.html)
- June 5, 2026: Google published "third-party SEO tools" guidance. Google does not evaluate or endorse tools, and tools have no access to Google's ranking data. Readers should be wary of "Google-approved" claims and should treat AEO/GEO advice the same way. This is a secondary paraphrase; verify the wording. — [Google page](https://developers.google.com/search/docs/fundamentals/third-party-seo); [webiano.digital summary](https://webiano.digital/google-draws-a-sharper-line-around-third-party-seo-tools/)

### Inferences
- A defensible blog score should be transparent: published checks and weights, each tied to a Google guideline or a user-facing benefit. It should not claim to predict rankings.

### Gaps
- I found no Google statement specifically about keyword density in 2026 sources.

## Open-source and Claude SEO audit skills

### Takeaway
Community Claude skills exist. At least one keeps its scores separate (never blended) and flags checks that need an API. I did not verify their full rubrics.

### Cited Findings
- hainrixz/claude-seo-ai: a `score` command recomputes two separate 0-100 scores from the audit findings JSON (`scripts/score.mjs`). It shows bands, a per-category breakdown, a severity-gating cap, and a "needs_api" count. It describes the scores as "Two scores, never blended." — [skills.sh](https://www.skills.sh/hainrixz/claude-seo-ai/score)
- AgriciDaniel/claude-seo: a third-party review cautions that its reports are the output of instructions, scripts and model reasoning, and that audits contact the target URLs. — [Towards AI review](https://pub.towardsai.net/claude-seo-review-what-to-verify-before-using-the-claude-code-skill-c28fd9e12a26)

### Inferences
- Severity gating, meaning a critical issue caps the score, and an explicit "needs external data" flag are both worth reusing.

### Gaps
- I did not read the full rubric of claude-seo or any ClawHub skill.

## What page text and HTML can check versus external data

### Takeaway
Most on-page checks need only the HTML. Health, indexing, link equity and ranking signals need a crawl, Search Console or backlink data.

### Cited Findings
- From HTML alone: title, meta description, H1/H2, slug, alt text, link text, internal and external links, canonical, hreflang, structured data, paragraph and sentence length, and keyphrase placement. These are the Yoast, Rank Math and Lighthouse content checks. — [Lighthouse](https://developer.chrome.com/docs/lighthouse/seo/meta-description); [Rank Math](https://rankmath.com/kb/score-100-in-tests/)
- Needs a fetch or crawl: HTTP status and robots.txt (Lighthouse), site-wide duplicate keyphrase use (Yoast and Rank Math check this across posts), and health scores over all internal URLs (Ahrefs). — [Ahrefs help](https://help.ahrefs.com/en/articles/1424673-what-is-health-score-in-ahrefs-site-audit)
- Needs SERP data: Surfer, Clearscope and similar competitor-relative scores (Surfer uses the top 20 pages). — [Surfer docs](https://docs.surferseo.com/en/articles/5700317-what-is-content-score)

### Inferences
- Search Console data (impressions, indexing) and backlink data (authority) cannot come from the page. A blog score should label those checks "needs data" rather than guess.

### Gaps
- None beyond those noted above.

# Empirical Evidence on Google Ranking Factors for Content Pages and Blog Articles (as of Oct 2026)

Scope note: these notes come from about 12 searches. Most figures come from search-result summaries of primary pages; the primary pages were not fetched in full. Vendor conflicts of interest are flagged: Ahrefs, Semrush, Backlinko (owned by Semrush), Clearscope, Surfer and SearchPilot all sell SEO tools or services, and First Page Sage is an agency.

## 1. What the large ranking-factor and correlation studies find

### Takeaway
Across correlation studies, two factors stand out: link authority (referring domains and Domain Rating) and topical relevance or comprehensiveness. Page speed, word count and exact-match keyword placement show weak or no correlation. None of these studies proves causation, and First Page Sage's "weights" are opinion, not measurement.

### Cited Findings
- **Backlinko 11.8M results study** (Brian Dean, with Ahrefs data, published about 2020):
  - Domain Rating "strongly correlates" with rankings, and the #1 result has 3.8x more backlinks than positions 2-10.
  - About 95% of pages have zero backlinks, so those pages were excluded from the link analysis.
  - Content with a high Clearscope "Content Grade" significantly outperformed thinner content.
  - There was no correlation between page speed (Alexa) and first-page rankings.
  - Source: [Backlinko](https://backlinko.com/search-engine-ranking)
- **Backlinko, title keyword and word count:**
  - The average first-page result has 1,447 words, and word count is evenly distributed across the top 10.
  - Using the keyword in the title tag showed close to zero correlation with higher first-page rank, even though 65-85% of top-10 pages include it. That means prevalence is high but discrimination within the top 10 is low.
  - Sources: [Backlinko](https://backlinko.com/search-engine-ranking); [Newswire summary](https://www.newswire.com/view/content/backlinks-and-content-quality-correlate-with-higher-google-rankings-21110817)
- **Semrush Ranking Factors 2024:**
  - Sample: 16,298 English keywords with more than 100 monthly searches, top 20 positions each.
  - "Text relevance" ranked #1. URL-level referring domains ranked #14 and backlinks #17; Semrush's own write-up puts referring-domain diversity at #12.
  - Semrush itself says isolating any single factor's impact is "difficult, if not impossible."
  - Sources: [Semrush study](https://semrush.com/blog/ranking-factors-semrush-study); [Semrush ranking factors](https://semrush.com/blog/google-ranking-factors)
- **Ahrefs "also rank for" study (3M searches):** longer content ranks for more keywords. This measures how many keywords a page ranks for, not its position. — [Ahrefs](https://ahrefs.com/blog/fr/also-rank-for-study/)
- **Unverified word-count figure:** a 2026 benchmark site credits Ahrefs with a 2,450-word average for position 1. This could not be confirmed in any Ahrefs source. — [Averi](https://resources.averi.ai/benchmarks/blog-post-length-performance)
- **First Page Sage, Q1 2025 weights** (agency estimate, not an empirical measurement):

  | Factor | Weight |
  |---|---|
  | Consistent publication of helpful content | 23% |
  | Keyword in meta title | 14% (down from 15%) |
  | Backlinks | 13% (down from 15% in 2023) |
  | Niche expertise | 13% |
  | Searcher engagement | 12% |
  | Freshness | 6% |
  | Mobile-friendliness | 5% |
  | Trustworthiness | 4% |
  | Link diversity | 3% |
  | Page speed | 3% |
  | SSL | 2% |
  | Internal links | 1% |
  | Meta description | 1% |

  Source: [First Page Sage](https://firstpagesage.com/seo-blog/the-google-algorithm-ranking-factors/)
- **Zyppy title rewrite study** (early 2022; 80,959 titles across 2,370 sites):
  - Google rewrote 61.6% of titles.
  - Titles over 70 characters were rewritten 99.9% of the time, and titles of 20 characters or fewer were rewritten more than 50% of the time. The best range was 51-60 characters.
  - Rewrite triggers: a repeated keyword, separators, brackets, boilerplate, and a missing or superfluous brand name.
  - These results are consistent with studies by Dr. Pete Meyers (Moz) and Alexis Rylko.
  - Sources: [Zyppy](https://zyppy.com/seo/google-title-rewrites/); [SEJ](https://www.searchenginejournal.com/google-changes-more-than-61-percent-of-title-tags/435618/)
- **SearchPilot A/B tests:** published tests include all-caps title tags (+14% on mobile), adding keywords to titles, removing FAQ markup, and schema markup / JSON-LD vs Microdata. Outcome details beyond the all-caps result were not retrieved. — [SearchPilot case studies](https://searchpilot.com/resources/case-studies/tag/seo-a-b-testing)

### Inferences
- **Weighting:** put the most weight on topical relevance and coverage. Treat links as an off-page factor, outside a content score but the strongest correlate. Treat keyword-in-title as a hygiene check, a binary pass/fail, rather than something to score on a gradient.
- **Title length:** aim for about 50-60 characters with no keyword repetition. This rests on observed Google behaviour (rewrites), which is stronger evidence than correlation.

### Gaps
- Not retrieved: Moz, Surfer and Clearscope correlation coefficients; Portent and Backlinko CTR-by-position curves; specific SearchPilot outcomes for meta descriptions, H1, internal links and FAQ.
- No sourced data was found on keyword-in-URL, keyword-in-first-paragraph, Flesch readability, alt text, outbound links or URL length. These remain unscored by evidence.

## 2. Evidence on specific factors

### Takeaway
| Factor | Evidence strength | Basis |
|---|---|---|
| User engagement (NavBoost) | Strong as a system | Sworn testimony, but no weights known |
| Topical relevance / comprehensiveness | Moderate to strong | Correlation only |
| Core Web Vitals | Weak (tiebreaker) | Correlation studies |
| Word count | Weak or myth as a direct factor | Correlation studies |
| Exact-match title keyword | Weak within the top 10 | Correlation studies |
| Page speed | Weak | Correlation studies |

### Cited Findings
- **NavBoost (click-based ranking system):**
  - Google VP Pandu Nayak described NavBoost as a key ranking system in the October 2023 DOJ trial, mentioning it about 54 times.
  - The May 2024 API leak references goodClicks, badClicks and lastLongestClicks, and roughly 13 months of interaction data.
  - The leak does not reveal signal weights.
  - Sources: [Hobo Web](https://www.hobo-web.co.uk/navboost-how-google-uses-large-scale-user-interaction-data-to-rank-websites/); [AIOSEO](https://aioseo.com/google-search-algorithm-leak/)
- **Core Web Vitals:**
  - Perficient (2021): a "not a large factor at all"; correlation did not shift after the Page Experience rollout. — [Perficient](https://www.perficient.com/insights/research-hub/impact-of-core-web-vitals-on-ranking)
  - Screaming Frog: position-1 URLs are 10% more likely to pass CWV than position-9 URLs. — [corewebvitals.io](https://www.corewebvitals.io/core-web-vitals/seo)
  - Advanced Web Ranking (2022; 3M pages): CWV is a ranking factor, but less important than links, content or intent. — [AWR](https://advancedwebranking.com/blog/core-web-vitals-study)
  - Caveat: most CWV studies predate INP replacing FID, and good CWV may simply proxy for good engineering overall. — [corewebvitals.io](https://www.corewebvitals.io/core-web-vitals/seo)
- **Page speed:** no correlation in Backlinko's study, and 3% in First Page Sage's estimate. — [Backlinko](https://backlinko.com/search-engine-ranking); [First Page Sage](https://firstpagesage.com/seo-blog/the-google-algorithm-ranking-factors/)
- **Freshness:** 6%, and SSL / HTTPS 2%, in First Page Sage's estimate. Both are opinion, not measurement. — [First Page Sage](https://firstpagesage.com/seo-blog/the-google-algorithm-ranking-factors/)

### Inferences
- **Word count:** score coverage of subtopics and entities instead of length. Length correlates with coverage but is not itself a factor.
- **Engagement:** satisfying the query (rewarded by NavBoost via long clicks) is the most plausible causal content lever, but a static content score can only proxy for it.
- **HTTPS and CWV:** treat both as minor technical gates, not as content-score weight.

### Gaps
- No sourced evidence was retrieved for:
  - keyword density (widely considered a myth, but unverified here)
  - Flesch readability
  - author bylines and E-E-A-T markup
  - internal anchor text
  - outbound links
  - alt text
  - schema-driven CTR lift
  - meta description CTR
  - information gain
- The Google API leak confirms some attributes exist, but not that they are weighted.

## 3. Value shift with AI Overviews (2024-2026)

### Takeaway
AI Overviews (AIOs) are associated with roughly 35-61% lower organic CTR on affected queries. Overlap between top-10 rankings and AIO citations fell from about 76% (mid-2025) to about 17-38% (early 2026, with method changes). Ranking well is still a necessary condition for traffic, but it is no longer sufficient.

### Cited Findings
- **Ahrefs CTR studies:**
  - April 2025 (300k keywords, March 2024 vs March 2025): AIOs cut position-1 CTR by 34.5%. Informational position-1 CTR fell from 0.056 to 0.031.
  - February 4, 2026 update (December 2023 vs December 2025): AIO presence correlates with 58% lower CTR for the top page. Position-1 CTR fell from 0.073 to 0.016 on AIO keywords and from 0.076 to 0.039 on informational keywords.
  - Source: [Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/)
- **Seer Interactive (September 2025 update):**
  - Organic CTR on AIO queries fell from 1.76% (June 2024) to 0.61% (September 2025), a 61% decline.
  - Paid CTR on AIO queries fell 68%. Paid CTR on non-AIO queries fell 32%, which points to a broader behaviour shift.
  - Caveat: AIOs tend to appear on queries that already had low CTR.
  - Source: [Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update)
- **Pew Research (July 22, 2025; 900 US adults, 68,879 searches, March 2025):**
  - Users clicked a traditional result in 8% of visits when an AI summary appeared, versus 15% without one.
  - Only 1% of visits included a click on a link cited inside the summary.
  - Sessions ended on 26% of pages with a summary, versus 16% without.
  - Sources: [Infodocket summary](https://www.infodocket.com/2025/07/22/pew-research-google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results); [TheWrap](https://www.thewrap.com/ai-summaries-google-article-clicks-half/)
- **Ahrefs, AIO citations vs rankings:**
  - July 2025 (1.9M citations from 1M AIOs): 76.1% of cited pages ranked in the top 10.
  - Update (863k keywords, 4M URLs): only 38% top-10 overlap (37% for organic listings only); 31.2% came from positions 11-100 and 31.0% from beyond 100.
  - Ahrefs says the two datasets are not directly comparable. It suggests query fan-out as a possible explanation, which Google has not confirmed.
  - YouTube is the most-cited domain.
  - Sources: [Ahrefs](https://ahrefs.com/blog/search-rankings-ai-citations); [SEJ](https://www.searchenginejournal.com/google-ai-overview/515286/); [SEJ](https://www.searchenginejournal.com/google-ai-overview/518427/)
- **BrightEdge:** about 17% top-10 overlap, using a different method. — [SEJ](https://www.searchenginejournal.com/google-ai-overview/518427/)

### Inferences
- **CTR-dependent factors:** title and meta-description CTR optimisation is now worth less on informational queries.
- **Passage-level answerability:** content that answers sub-questions (fan-out) may earn citations even without a top-10 rank, which argues for scoring coverage of related sub-questions.

### Gaps
- No Similarweb zero-click figure was retrieved.
- Pew's data collection window is reported inconsistently across sources (March vs April 7-17, 2025).

## 4. Myths and overweighted factors to exclude

### Takeaway
Exclude or down-weight:
- raw word count
- exact keyword density
- page speed or CWV as content-score weight
- the notion that a keyword in the title is a strong differentiator
- First Page Sage-style percentage weights presented as empirical

### Cited Findings
- **Word count** is evenly distributed in the top 10, so it is not a factor in itself. — [Backlinko](https://backlinko.com/search-engine-ranking)
- **Page speed** shows no ranking correlation. — [Backlinko](https://backlinko.com/search-engine-ranking)
- **CWV** is "not a large factor at all." — [Perficient](https://www.perficient.com/insights/research-hub/impact-of-core-web-vitals-on-ranking)
- **Title keyword** shows near-zero correlation with position within page 1. — [Newswire / Backlinko](https://www.newswire.com/view/content/backlinks-and-content-quality-correlate-with-higher-google-rankings-21110817)
- **Single-factor weights** cannot be measured reliably, per Semrush's own caveat. — [Semrush](https://semrush.com/blog/ranking-factors-semrush-study)

### Inferences
- **Keyword density:** likely a myth. No study here supports it, and Zyppy's finding that repeated keywords trigger title rewrites argues against stuffing.
- **Overly long titles:** penalise titles over 70 characters, since Google rewrites them almost every time (99.9%).

### Gaps
- No primary source was retrieved that tests keyword density, LSI keywords, Flesch scores or meta keywords. Their myth status rests on consensus, not on studies cited here.

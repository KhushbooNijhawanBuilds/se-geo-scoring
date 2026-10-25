# Round 2: page-level check rubrics of SEO tools, and a merged check library (Oct 2026)

Scope: this adds to tools_rubrics.md and does not repeat it. Yoast numbers below come from the source code on the `trunk` branch of github.com/Yoast/wordpress-seo (`packages/yoastseo`, package.json version 3.6.0), fetched 2026-10-23. YS = `https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/`.

## Yoast SEO and readability: verified thresholds from source

### Takeaway
Each Yoast check returns a score from 1 to 9: 9 is green, 6 orange, 3 red. A few checks return negative scores as penalties. The overall score is the sum of the check scores divided by (number of checks × 9), times 100. Several first-round numbers are wrong or out of date. Paragraph length in trunk is 150/200 words, not 70/100. The Flesch reading-ease check is no longer in the readability folder.

### Cited Findings

**Scoring mechanics**

- **Overall score:** `Math.round(totalScore / (results.length * 9) * 100)`. — [assessor.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessors/assessor.js)
- **Per-check ratings:** -1 means feedback only and 0 means no score. A score of 4 or less is bad, 5-7 is ok, and above 7 is good. — [scoreToRating.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/interpreters/scoreToRating.js)

**SEO checks**

- **Keyphrase density:**
  - Green (9) from 0.5% up to 3%. With morphological word forms (Premium) the top of the green band is 3.5%.
  - Above the maximum scores -10. Above 4% scores -50. Below 0.5% scores 4.
  - Density is multiplied by a keyphrase-length factor.
  - Texts under 100 words use counts instead: 1 occurrence, or at most 2 when the text is over 50 words.

  — [YS seo/KeywordDensityAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/KeywordDensityAssessment.js)
- **Text length:** 300+ words scores 9, 250-299 scores 6, 200-249 scores 3. Below 200 the score goes to -10, and below 100 words to -20. — [YS seo/TextLengthAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/TextLengthAssessment.js)
- **Meta description length:**
  - Missing scores 1.
  - 120 characters or fewer scores 6 ("too short").
  - 121-156 scores 9.
  - Over 156 scores 6.
  - Japanese has its own configuration.

  — [YS seo/MetaDescriptionLengthAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/MetaDescriptionLengthAssessment.js)
- **SEO title width:** measured in pixels. 400-600px scores 9, under 400px scores 6, over 600px scores 3, and no title scores 1. — [YS seo/PageTitleWidthAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/PageTitleWidthAssessment.js)
- **Keyphrase in SEO title:** an exact match at the beginning of the title scores 9 (recommendedPosition 0). Other matches score 6, and none scores 2. — [YS seo/KeyphraseInSEOTitleAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/KeyphraseInSEOTitleAssessment.js)
- **Keyphrase length:**
  - 1-4 content words scores 9. Up to 8 is acceptable.
  - For languages without function-word support the limits are 6 and 9.
  - No keyphrase scores -999.

  — [YS seo/KeyphraseLengthAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/KeyphraseLengthAssessment.js)
- **Keyphrase in introduction:** found in one sentence of the first paragraph scores 9, otherwise 6 or 3. — [YS seo/IntroductionKeywordAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/IntroductionKeywordAssessment.js)
- **Keyphrase in subheadings (H2/H3):**
  - Good (9) when 30-75% of subheadings contain the keyphrase or a synonym.
  - Fewer or more scores 3.
  - A long text with no subheadings scores 2. A short text (300 words or fewer) with none scores 9.

  — [YS seo/SubHeadingsKeywordAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/SubHeadingsKeywordAssessment.js)
- **Keyphrase in meta description:** 1-2 occurrences scores 9. Zero, or 3 or more, scores 3. — [YS seo/MetaDescriptionKeywordAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/MetaDescriptionKeywordAssessment.js)
- **Keyphrase in image alt:**
  - With fewer than 5 images, at least one alt containing the keyphrase scores 9.
  - With 5 or more images, 30-75% of alts containing it scores 9.
  - Too few, too many, alts without the keyphrase, or no alt at all score 6.
  - No images or no keyphrase scores 3.

  — [YS seo/KeyphraseInImageTextAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/KeyphraseInImageTextAssessment.js)
- **Image count:** 0 images scores 3, at least 1 scores 9. — [YS seo/ImageCountAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/ImageCountAssessment.js)
- **Keyphrase in slug:**
  - For a keyphrase under 3 words, a 100% word match scores 9.
  - Otherwise, more than 50% of words matching scores 9. Partial matches score 6, none scores 3.

  — [YS seo/UrlKeywordAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/UrlKeywordAssessment.js)
- **Internal links** (minimum 1): all followed scores 9, some followed 8, all nofollowed 7, none 3. — [YS seo/InternalLinksAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/InternalLinksAssessment.js)
- **Outbound links:** same pattern: 9 / 8 / 7, and none scores 3. — [YS seo/OutboundLinksAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/OutboundLinksAssessment.js)
- **Single H1:** 0 or 1 H1 in the body scores 8, more than one scores 1. The code says it flags only multiple H1s, because some themes put the title H1 inside the body. — [YS seo/SingleH1Assessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/SingleH1Assessment.js)
- **Competing links** (anchor text equal to the keyphrase): the recommended maximum is 0. None scores 8, any scores 2. — [YS seo/TextCompetingLinksAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/TextCompetingLinksAssessment.js)
- **Keyphrase distribution** (Premium): the "distraction" percentage is the largest share of text with no keyphrase. Up to 30% scores 9, up to 50% scores 6, more scores 1. — [YS seo/KeyphraseDistributionAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/seo/KeyphraseDistributionAssessment.js)
- **Other SEO files in the folder:** FunctionWordsInKeyphrase, TextTitle (title present), and the product checks ProductIdentifiers and ProductSKU. — [GitHub dir listing](https://github.com/Yoast/wordpress-seo/tree/trunk/packages/yoastseo/src/scoring/assessments/seo)
- **"Previously used keyphrase":** not in this folder. It is a site-level check done in the plugin's PHP/JS layer, not in yoastseo. Its thresholds were not verified.

**Readability checks**

- **Subheading distribution:**
  - Every section of 300 words or fewer scores 9.
  - Sections of 300-350 words score 6. Over 350 scores 3.
  - A long text with no subheadings scores 2. A short text with none scores 9.

  — [YS readability/SubheadingDistributionTooLongAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/readability/SubheadingDistributionTooLongAssessment.js)
- **Passive voice:** passive sentences up to 10% score 9, 10-15% score 6, over 15% score 3. — [YS readability/PassiveVoiceAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/readability/PassiveVoiceAssessment.js)
- **Transition words:** sentences with transitions under 20% score 3, 20-30% score 6, 30% or more score 9. The check applies only to texts over 200 words. — [YS readability/TransitionWordsAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/readability/TransitionWordsAssessment.js)
- **Sentence length:** a sentence is "too long" above 20 words. Up to 25% too-long sentences scores 9, 25-30% scores 6, over 30% scores 3. — [YS readability/SentenceLengthInTextAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/readability/SentenceLengthInTextAssessment.js)
- **Paragraph length** (trunk default): the longest paragraph at 150 words or fewer scores 9, 150-200 scores 6, over 200 scores 3. The v3.6.0 product doc cited in round 1 gives 70/100, a product-page or older configuration, so the two sources conflict. — [YS readability/ParagraphTooLongAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/readability/ParagraphTooLongAssessment.js)
- **Consecutive sentence beginnings:** more than 2 consecutive sentences starting with the same word scores 3, otherwise 9. — [YS readability/SentenceBeginningsAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/readability/SentenceBeginningsAssessment.js)
- **Word complexity** (Premium): complex words under 10% score 9, otherwise 6. — [YS readability/WordComplexityAssessment.js](https://github.com/Yoast/wordpress-seo/blob/trunk/packages/yoastseo/src/scoring/assessments/readability/WordComplexityAssessment.js)
- **Full readability folder:** List, ParagraphTooLong, PassiveVoice, SentenceBeginnings, SentenceLengthInText, SubheadingDistributionTooLong, TextAlignment, TextPresence, TransitionWords, WordComplexity. There is no Flesch file. — [dir listing](https://github.com/Yoast/wordpress-seo/tree/trunk/packages/yoastseo/src/scoring/assessments/readability)
- claude-seo's docs say "Yoast deprioritized Flesch scores in v19.3". That is a secondary claim and I did not check it against the Yoast changelog. — [claude-seo seo-content SKILL.md](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-content/SKILL.md)

### Inferences
- **Density penalties dominate.** Yoast's negative scores (-10, -50, -999) mean density and keyphrase checks swing the averaged total far more than any readability check. This is a design flaw: it over-rewards exact-match repetition.
- **Inconsistent link scores.** Linking out with nofollow still scores 7 or 8, which is green, so the follow/nofollow split barely matters. SingleH1 and competing links score at most 8, not 9, so a "perfect" 100 is impossible whenever they are active. That is a minor quirk.

### Gaps
- I did not read the PHP/JS code for "previously used keyphrase", cornerstone content, or taxonomy text length.
- The exact keyphraseLengthFactor formula was not extracted.

## Screaming Frog, Sitebulb, Semrush Site Audit, Ahrefs

### Takeaway
The crawlers agree on title, meta, H1, canonical, directive, hreflang and structured-data checks. Their length cutoffs differ:

| Tool | Title | Meta description |
|---|---|---|
| Screaming Frog | 30-60 chars or 200-561 px | 70-155 chars or 400-985 px |
| Semrush | over 70 chars, or 10 chars or fewer, is flagged | — |
| Yoast | 400-600 px | 120-156 chars |

### Cited Findings

**Screaming Frog** (issue type and priority). Priorities come from page icons; the fetch read only the first ~100k characters. — [Screaming Frog SEO Spider issues](https://www.screamingfrog.co.uk/seo-spider/issues/)

- **Titles:**
  - Missing, multiple, or outside `<head>`: Issue, High.
  - Duplicate; over 60 characters; below 30 characters; over 561 px; below 200 px: Opportunity, Medium.
  - Same as H1: Opportunity, Low.
- **Meta description:**
  - Multiple, or outside `<head>`: Issue, Medium.
  - Missing; duplicate; over 155 characters; below 70 characters; over 985 px; below 400 px: Opportunity, Low.
- **H1:**
  - Missing: Issue, Medium. Multiple: Warning, Medium.
  - Alt text in H1, and non-sequential: Warning, Low.
  - Duplicate, and over 70 characters: Opportunity, Low.
- **H2:** missing, multiple and non-sequential are Low warnings. Duplicate and over 70 characters are Opportunities.
- **Content:**
  - Exact duplicates: Issue, High. Spelling and grammar errors: Issue, Medium.
  - Soft 404 and Lorem Ipsum: Warning, High.
  - Near duplicates, semantically similar: Warning, Medium. Low relevance: Warning, Low.
  - Low content pages: Opportunity, Medium. Readability difficult / very difficult: Opportunity, Low.
- **Images:**
  - Missing alt text and missing alt attribute: Issue, Low.
  - Over 100 KB: Opportunity, Medium.
  - Alt over 100 characters, incorrectly sized, missing size attributes: Opportunity, Low.
  - Background images: Warning.
- **Canonicals:**
  - Multiple conflicting, non-indexable canonical, invalid attribute, fragment URL, outside head: Issue, High.
  - Canonicalised: Warning, High.
  - Missing and unlinked: Warning, Medium. Multiple and relative: Warning, Low.
- **Directives:**
  - Outside head: Issue, High.
  - Noindex, nofollow and none: Warning, High.
  - NoImageIndex: Issue, Low. Nosnippet: Warning, Low.
- **Hreflang:**
  - High issues: non-200 URLs, missing return links, inconsistent confirmation links, non-canonical return links, noindex return links, incorrect codes, multiple entries, not using canonical, outside head.
  - Unlinked: Medium.
  - Missing self-reference and missing x-default: Warning, Low.
- **Structured data:**
  - Validation errors, rich-result validation errors, parse errors: Issue, High.
  - Missing, and validation warnings: Opportunity, Low.

**Sitebulb**

- **Priorities:** Critical, High, Medium, Low, plus Insight. Types: Issue, Potential Issue, Opportunity. — [Sitebulb hints](https://sitebulb.com/hints/)
- **On-page hints:**
  - Critical: title missing, HTML missing or empty, title empty, title outside head, broken or invalid HTML.
  - High: multiple titles, meta description outside head.
  - Medium: H1 missing, H1 empty, images missing alt, Lorem Ipsum.
  - Low: H1 too short or too long, title too short or too long, meta description too short or too long, meta description empty or missing, multiple meta descriptions, multiple H1, title equals meta description.
  - The page states no numeric thresholds.

  — [Sitebulb on-page hints](https://sitebulb.com/hints/on-page/)

**Semrush Site Audit** (from the KB issues list)

| Check | Severity | Trigger |
|---|---|---|
| Missing or empty title | Error | — |
| Duplicate titles | Error | Exact match |
| Duplicate meta descriptions | Error | — |
| Duplicate content | Error | 85% or more identical |
| Broken internal links | Error | — |
| Too many on-page links | Error | Over 3,000 |
| Internal nofollow | Error | — |
| Invalid structured data | Error | — |
| Title too long | Warning | Over 70 chars |
| Title too short | Warning | 10 chars or fewer |
| Missing meta description | Warning | — |
| Missing H1 | Warning | — |
| Title = H1 | Warning | — |
| Low word count | Warning | Under 200 words |
| Low text/HTML ratio | Warning | 10% or less |
| Missing alt attribute | Warning | — |
| Broken external links | Warning | — |
| Multiple H1 | Notice | — |
| URL too long | Notice | Over 200 chars |
| Non-descriptive anchors | Notice | — |
| Only one incoming internal link | Notice | — |
| Too deep | Notice | More than 3 clicks |

— [Semrush KB 542](https://www.semrush.com/kb/542-site-audit-issues-list)

**Ahrefs Site Audit:** I could not retrieve the official Ahrefs per-issue list. The help URL I tried returned an unrelated meta-refresh article, and the Ahrefs blog's audit guide lists no thresholds. — [Ahrefs SEO audit guide](https://ahrefs.com/blog/seo-audit/)

### Inferences
- **Weak consensus on length.** Character cutoffs vary by roughly 2x across tools: title upper limits run 60-70 characters, meta lower limits 70-120. The truncation point is set by pixel width, not a hard rule.
- **Same-as-H1 rule is contested.** Semrush flags "title equals H1" as a Warning. Screaming Frog rates it only a Low opportunity. This is a convention without evidence.

### Gaps
- Ahrefs' issue list with Error/Warning/Notice levels and its thresholds was not verified.
- Sitebulb's numeric thresholds were not found.

## Semrush SEO Writing Assistant and On Page SEO Checker; AIOSEO; Moz

### Takeaway
SWA and On Page SEO Checker benchmark a page against the top 10 competitors and publish no weights. AIOSEO TruSEO (rebuilt in 5.0) mirrors Yoast's checks but documents few numbers. Moz On-Page Grader's factor weights are undocumented in what I could reach; moz.com blocked fetching.

### Cited Findings

**Semrush SEO Writing Assistant**

- The overall 0-10 score combines Readability, SEO, Originality and Tone of Voice. No formula is given. — [Semrush KB 814](https://www.semrush.com/kb/814-seo-writing-assistant)
- **Readability:** Flesch target set to the average of the top 10 competitors; word count against a target; title over about 60 characters; long paragraphs, hard sentences, passive voice and complex words (no numbers).
- **SEO:** target and recommended keywords; keyword stuffing; alt attributes; broken links or too many links; keyword in title.
- **Tone of voice:** a 5-level formality scale, filler words.
- **Originality:** share of copied text.

**Semrush On Page SEO Checker**

- Idea categories: Strategy, Backlinks, Technical SEO (pulled from Site Audit), User Experience (needs GA), Semantics, Content, SERP features. Ideas are based on the top 10 competitors per keyword. — [Semrush On Page SEO Checker](https://www.semrush.com/features/on-page-seo-checker); [Semrush KB SEO ideas](https://semrush.com/kb/semrush-reports-tools/projects/seo-ideas)

**AIOSEO TruSEO**

- Numbers it states:
  - meta description over 160 characters may be truncated
  - paragraphs over 150 words are flagged
  - readability target 60-80
  - headline score 70+ good, 40-69 ok, under 40 poor
  - at least 1 internal link
  - at least 1 image or video
- Checks with no number given:
  - Basics: title pixel width, single title, text length, outbound links.
  - Keyword checks: keyword length, function words, keyword in SEO title/slug/meta/intro/subheading, density, distribution, competing links, cannibalization.
  - Readability: sentence length, sentence beginnings, missing subheadings, passive voice, transition words, word complexity.
  - Spelling.
  - Headline: sentiment, type, word balance.

  — [AIOSEO TruSEO recommendations](https://aioseo.com/docs/understanding-the-truseo-page-analysis-recommendations/)
- AIOSEO 5.0.0 rebuilt TruSEO with tabs for Keywords, Basics, Spelling, Readability and Headline. The Flesch, passive-voice and transition checks are English only. — [AIOSEO TruSEO content analysis](https://aioseo.com/docs/using-truseo-content-analysis/)

**Moz On-Page Grader**

- Only community forum sources were found. Keyword in title is said to carry heavy weight (a page moved from F to A after adding it). There is no stuffing threshold, and users report keyword counts that don't match the source. — [Moz Q&A](https://mozdev.nodebb.com/community/q/post/45080)

### Gaps
- No official Moz On-Page Grader factor list was reachable; moz.com blocks fetching.
- AIOSEO's numeric density and sentence thresholds would need the plugin source.

## Content optimisers: how the scores are computed

### Takeaway
All four score coverage of terms or entities mined from the SERP. Only MarketMuse publishes per-topic point mechanics. None publishes a full formula.

### Cited Findings
- **MarketMuse Content Score:** 0-100. A topic earns 1 point per mention, capped at 2 points per topic. The score is judged relative to competitors, "there is no perfect score", and the Target Content Score is a recommended minimum. — [MarketMuse docs: Content Score](https://docs.marketmuse.com/marketmuse-terminology/what-is-content-score/)
- **Clearscope:**
  - It grades using terms scraped from the top results. Term importance runs from 1 to 10, and the top grade is A++.
  - Including more terms raises the grade. No cutoffs are published.
  - A separate readability score exists.

  — [Clearscope support: grading](https://www.clearscope.io/support/how-does-clearscope-grade-your-content); [Clearscope readability](https://www.clearscope.io/support/articles/how-does-the-readability-score-work)
- **Frase Topic Score:** topics come from NER over the top results. Each topic shows your mention count against the competitor average. The overall score is compared with the competitor average score. — [Frase help: Topic Score](https://help.frase.io/article/343-frase-topic-score-for-on-page-optimization); [Frase crash course](https://crashcourse.frase.io/frase-crash-course/optimizing/what-is-my-topic-score)
- **NeuronWriter Content Score:** based on semantic term recommendations used in the text and headings. Bands run from red to green near 100. It also has a separate "AI Score" for LLM optimisation. — [NeuronWriter FAQ](https://neuronwriter.com/faqs/what-is-content-score-and-what-the-main-text-parameters-are-displayed-in-the-editor/); [NeuronWriter AI Score](https://neuronwriter.com/faqs/ai-optimisation-in-neuronwriter/)

### Inferences
- Capped per-topic counting, as in MarketMuse, resists stuffing better than raw frequency. It is the best model to borrow for a coverage component.

## Open-source skill: AgriciDaniel/claude-seo (latest commit 2026-10-22)

### Takeaway
claude-seo weights categories into a 0-100 health score with Critical/High/Medium/Low priorities. Its threshold files contradict each other, and much of it is convention.

### Cited Findings
- **Category weights:** Technical 22%, Content Quality 23%, On-Page 20%, Schema 10%, Performance (CWV) 10%, AI Search Readiness 10%, Images 5%. — [skills/seo-audit/SKILL.md](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-audit/SKILL.md)
- **E-E-A-T sub-weights:** Experience 20%, Expertise 25%, Authoritativeness 25%, Trust 30%. Bands: 90-100, 70-89, 50-69, 30-49, 0-29. — [eeat-framework.md](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo/references/eeat-framework.md); [eeat-scoring-guide.md](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo/references/eeat-scoring-guide.md)
- **Quality gates:**
  - Title 30-60 characters, meta description 120-160, alt text 10-125 characters.
  - Minimum words: blog post 1,500, service page 800, product page 400, homepage 500.
  - Location pages: warning at 30+ pages, hard stop at 50+.

  — [quality-gates.md](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo/references/quality-gates.md)
- **Contradiction:** seo-page asks for a title of 50-60 characters and a meta description of 150-160, with exactly one H1 and no skipped heading levels. — [skills/seo-page/SKILL.md](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-page/SKILL.md)
- **seo-content:**
  - Flesch 60-70, sentences averaging 15-20 words, paragraphs of 2-4 sentences.
  - Keyword in title, H1 and the first 100 words. No density target, "Google publishes none".
  - 3-5 internal links per 1,000 words.
  - Word counts are "floors, not targets".

  — [skills/seo-content/SKILL.md](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-content/SKILL.md)
- **llms.txt** is reported but given no weight. — [skills/seo-geo/SKILL.md](https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-geo/SKILL.md)

### Inferences
- **Self-contradiction.** It calls word counts floors while the blog gate requires 1,500 words. Title and meta ranges also differ between files.

## Google's stance and independent evidence

### Cited Findings
- Google Search Central, "Guidance on third-party SEO tools and advice", last updated 2026-06-05:
  - Google "doesn't evaluate third-party services".
  - "Third-party tools don't have access to our internal ranking data. They can't guarantee performance."
  - Predictions "may not happen".
  - The page does not mention scores specifically.

  — [Google](https://developers.google.com/search/docs/fundamentals/third-party-seo)
- Mueller (early 2018) said readability is not a ranking factor to his knowledge, and Portent and Ahrefs found no readability-to-ranking correlation. This is a secondary source; I found no primary transcript. — [Practical Ecommerce](https://www.practicalecommerce.com/readability-for-seo-myths-and-reality)
- Agency write-ups note that all-green Yoast pages can still rank poorly. This is anecdotal. — [lockedownseo](https://lockedownseo.com/yoast-green-dots-ranking)

### Gaps
- I found no rigorous independent test of Yoast, Semrush, Screaming Frog or Sitebulb scores against rankings. Correlation studies of content scores are covered in tools_rubrics.md.

## Merged page-level check library

Labels:
- **E** = evidence-backed: grounded in Google documentation or a clear user, indexing or rendering mechanism.
- **C** = convention: a tool consensus with no ranking evidence.
- **M** = myth or anti-pattern.

Sources are the tools above. Y = Yoast, SF = Screaming Frog, SB = Sitebulb, SR = Semrush, AIO = AIOSEO, CS = claude-seo, RM = Rank Math (round 1).

### Indexing and head

| Check | Tools | Thresholds seen | Label |
|---|---|---|---|
| Title present, single, in `<head>` | SF High, SB Critical, SR Error | — | E |
| Title length/width | Y, SF, SR, SB, CS, AIO | Y 400-600 px; SF 30-60 chars / 200-561 px; SR >70 or ≤10 chars; CS 30-60 or 50-60 | C (truncation only) |
| Title unique across site | SF, SR, CS | exact duplicate | E (Google advises distinct titles) |
| Title = H1 | SF Low, SR Warning | — | C/M |
| Meta description present/unique | SF, SB, SR | — | C (Google may rewrite it; not a ranking factor) |
| Meta description length | Y, SF, CS, AIO | Y 121-156; SF 70-155 / 400-985 px; CS 120-160 / 150-160; AIO ≤160 | C |
| Canonical valid, single, absolute, indexable | SF, Lighthouse | — | E |
| Robots directives (noindex/nofollow), in `<head>` | SF High, SB | — | E |
| Hreflang valid, return links, x-default | SF, Lighthouse | — | E (x-default C) |
| Structured data parses/validates | SF High, SR Error | — | E (for rich results) |

### Structure and links

| Check | Tools | Thresholds seen | Label |
|---|---|---|---|
| H1 present | SF Medium, SB Medium, SR Warning | — | C/E (aids accessibility) |
| Single H1 | Y (score 1 if >1), SF Medium, SR Notice, SB Low | — | C (Google has said multiple H1s are fine) |
| Heading hierarchy sequential | SF Low, CS | — | C (accessibility) |
| Subheading distribution | Y | ≤300 words per section | C |
| Images: alt present | SF, SB, SR, Y | — | E (accessibility and image search) |
| Alt length | SF, CS | SF >100 chars; CS 10-125 | C |
| Image file size | SF | >100 KB | E (performance) |
| Image count ≥1 | Y, AIO, RM | — | C |
| Internal links ≥1 | Y, AIO, CS | CS 3-5 per 1,000 words | E (discovery) / C (counts) |
| Outbound links ≥1 | Y, AIO | — | C |
| Broken links | SR, SWA | — | E |
| Descriptive anchor text | SR Notice, Lighthouse | — | E |
| Competing links (anchor = keyphrase) | Y, AIO | 0 | C |

### Content

| Check | Tools | Thresholds seen | Label |
|---|---|---|---|
| Duplicate / near-duplicate content | SF High, SR | SR 85% identical | E |
| Thin / low word count | Y, SR, SF, CS, RM | Y 300; SR 200; CS blog 1,500; RM 2,500 for full marks | M as a target / C as a floor (Google: word count is not a factor) |
| Text-to-HTML ratio | SR | ≤10% | M |
| Lorem ipsum / placeholder | SF High, SB Medium | — | E (quality) |
| Spelling/grammar | SF, AIO | — | C/E (quality raters) |

### Keyphrase

| Check | Tools | Thresholds seen | Label |
|---|---|---|---|
| Keyword in title (at start) | Y, AIO, RM, SWA, Moz | — | C (relevance; position is myth-adjacent) |
| Keyword in intro | Y, AIO, RM, CS | first paragraph, first 10%, or first 100 words | C |
| Keyword in slug | Y, AIO, RM | >50% word match | C |
| Keyword in subheadings | Y, AIO, RM | Y 30-75% of H2/H3 | C |
| Keyword in alt | Y, AIO, RM | Y 30-75% when 5+ images | M (alt should describe the image) |
| Keyword in meta description | Y, AIO, RM | Y 1-2 times | C (bolding in snippets) |
| Keyword density | Y, AIO, RM, Moz | Y 0.5-3%; RM 1-1.5% | M (no Google target; stuffing violates spam policy) |
| Keyphrase distribution | Y Premium, AIO | Y gap ≤30% | C |
| Keyphrase length | Y, AIO | 1-4 content words | C |
| Previously used keyphrase / cannibalization | Y, AIO, RM | — | C (needs site data) |

### Readability

| Check | Tools | Thresholds seen | Label |
|---|---|---|---|
| Sentence length | Y, AIO, CS | Y: ≤25% of sentences over 20 words; CS average 15-20 | C (usability) |
| Paragraph length | Y, AIO, RM, CS | Y ≤150/200 words; AIO 150; RM 120; CS 2-4 sentences | C |
| Passive voice | Y, AIO, SWA | Y ≤10% | C |
| Transition words | Y, AIO | Y ≥30% of sentences | C/M |
| Sentence beginnings | Y, AIO | ≤2 in a row | C |
| Word complexity | Y Premium, AIO | <10% | C |
| Flesch reading ease | AIO 60-80, SWA vs competitors, CS 60-70; Y no longer has the file | — | C (not a ranking factor per Mueller) |

### Title copy, SERP coverage and E-E-A-T

| Check | Tools | Label |
|---|---|---|
| Power, sentiment and number words in title | RM, AIO headline | M |
| Tone/formality | SWA | C |
| SERP term/entity coverage | Surfer, Clearscope, MarketMuse, Frase, NeuronWriter, SWA | C (weak correlation, ~0.2-0.3) |
| Originality/plagiarism | SWA | E (helpful-content guidance) |
| Author/E-E-A-T signals | CS | C/E (quality rater guidelines; not a direct algorithmic score) |

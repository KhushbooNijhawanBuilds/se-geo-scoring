# Google and Bing content quality standards for scoring blog articles (round 2, verbatim; as of 2026-10-23)

Source tags used below:
- **[P]** a primary document opened this session, quoted verbatim.
- **[S]** a secondary source.
- **[P-ext]** the verbatim text of the QRG PDF, which was downloaded and text-extracted locally.

What this round verifies from round 1 (official_guidance.md):
- **QRG edition:** confirmed as the September 11, 2025 edition, 182 pages.
- **QRG section numbers:** all confirmed.
- **Helpful content page:** now dated 2026-10-05. Round 1 did not record a date.
- **Spam policies:** still dated 2026-08-28.
- **Gen-AI guidance:** still dated 2026-10-01.
- **March 2024 blog post:** the wording is now verified.
- **Site reputation policy:** an August 2026 change was found (new).

## 1. Google "Creating helpful, reliable, people-first content": self-assessment questions

### Takeaway
The page was last updated **2026-10-05 UTC**. It contains 12 content/quality questions, 4 expertise questions, 5 people-first questions and 11 search-engine-first warning signs. It then covers Who (3 questions), How (3 questions on automation and AI disclosure) and Why (no questions, a statement). The fetch tool truncates long questions at 125 characters, so questions marked "…" below are cut off. Paste the full wording from the page before encoding a question verbatim.

### Cited Findings
All quotes in this section are [P] from [developers.google.com/search/docs/fundamentals/creating-helpful-content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content), "Last updated 2026-10-05 UTC".

**Content and quality.** Each question is paired with a candidate binary check.

| # | Question (verbatim) | Candidate check |
|---|---|---|
| C1 | "Does the content provide original information, reporting, research, or analysis?" | Has at least one original data point, test, case, or analysis not found in the cited sources |
| C2 | "Does the content provide a substantial, complete, or comprehensive description of the topic?" | Covers all the subtopics a reader needs for the stated intent |
| C3 | "Does the content provide insightful analysis or interesting information that is beyond the obvious?" | Contains at least one non-obvious insight |
| C4 | "If the content draws on other sources, does it avoid simply copying or rewriting those sources…" (continues: substantial added value and originality) | Not a paraphrase of a single source |
| C5 | "Does the main heading or page title provide a descriptive, helpful summary of the content?" | Title or H1 accurately summarizes the body |
| C6 | "Does the main heading or page title avoid exaggerating or being shocking in nature?" | No clickbait or superlatives that the body doesn't back up |
| C7 | "Is this the sort of page you'd want to bookmark, share with a friend, or recommend?" | Judge's yes/no |
| C8 | "Would you expect to see this content in or referenced by a printed magazine, encyclopedia, or book?" | Judge's yes/no |
| C9 | "Does the content provide substantial value when compared to other pages in search results?" | Adds something absent from the current top results |
| C10 | "Does the content have any spelling or stylistic issues?" | Zero spelling or grammar errors |
| C11 | "Is the content produced well, or does it appear sloppy or hastily produced?" | No broken formatting, placeholder text or leftover prompt text |
| C12 | "Is the content mass-produced by or outsourced to a large number of creators, or spread across a large network of sites…" | Not templated or near-duplicate across the site |

**Expertise:**
- E1: "Does the content present information in a way that makes you want to trust it…". It continues with clear sourcing, evidence of expertise, and background on the author or site. Check: sources are cited, and an author or site background is linked.
- E2: "If someone researched the site producing the content, would they come away with an impression that it is well-trusted…". Off-page; can't be checked from the page.
- E3: "Is this content written or reviewed by an expert or enthusiast who demonstrably knows the topic well?" Check: the author or reviewer credential is stated and relevant.
- E4: "Does the content have any easily-verified factual errors?" Check: zero verifiable factual errors. Make this a **gate on YMYL pages**.

**People-first:**
- P1: "Do you have an existing or intended audience for your business or site that would find the content useful…"
- P2: "Does your content clearly demonstrate first-hand expertise and a depth of knowledge…". The examples given are using a product or visiting a place. Check: first-hand evidence is present (own photos, test results, "we installed…").
- P3: "Does your site have a primary purpose or focus?" Check: the topic is within the site's focus.
- P4: "After reading your content, will someone leave feeling they've learned enough about a topic to help achieve their goal?"
- P5: "Will someone reading your content leave feeling like they've had a satisfying experience?"

**Search-engine-first warning signs.** Each is a negative check.
- W1: "Is the content primarily made to attract visits from search engines?"
- W2: "Are you producing lots of content on many different topics in hopes that some of it might perform well in search results?"
- W3: "Are you using extensive automation to produce content on many topics?"
- W4: "Are you mainly summarizing what others have to say without adding much value?"
- W5: "Are you writing about things simply because they seem trending…"
- W6: "Does your content leave readers feeling like they need to search again to get better information from other sources?"
- W7: "Are you writing to a particular word count because you've heard or read that Google has a preferred word count?" The page answers: "(No, we don't.)"
- W8: "Did you decide to enter some niche topic area without any real expertise…"
- W9: "Does your content promise to answer a question that actually has no answer…"
- W10: "Are you changing the date of pages to make them seem fresh when the content has not substantially changed?" Check: dateModified changes only with a substantive diff.
- W11: "Are you adding a lot of new content or removing a lot of older content primarily because you believe…" (it will help rankings; the page says it won't).

**Who:**
- "Is it self-evident to your visitors who authored your content?"
- "Do pages carry a byline, where one might be expected?"
- "Do bylines lead to further information about the author or authors involved…"

Checks: a byline is present; the byline links to a bio page; the bio states relevant background.

**How (automation and AI):**
- "Is the use of automation, including AI-generation, self-evident to visitors through disclosures or in other ways?"
- "Are you providing background about how automation or AI-generation was used to create content?"
- "Are you explaining why automation or AI was seen as useful to produce content?"

**Why:** there are no questions in this section. It states that the primary reason for creating content should be to help people who visit the site directly.

**Feb 8 2023 Search Central blog post** [P], [Google Search's guidance about AI-generated content](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content), posted by Danny Sullivan and Chris Nelson:
- "Appropriate use of AI or automation is not against our guidelines."
- "Using AI doesn't give content any special gains. It's just content."
- "You should consider having accurate author bylines when readers would reasonably expect it, such as to any content where someone might think, 'Who wrote this?'"
- "AI or automation disclosures are useful for content where someone might think 'How was this created?'"
- "Giving AI an author byline is probably not the best way to follow our recommendation…"
- On topics "like health, civic, or financial information—our systems place an even greater emphasis on signals of reliability."

### Inferences
- In Google's own text, AI disclosure and bylines apply "where reasonably expected". Score them as conditional checks, not as universal hard requirements.
- Valid gates from this page:
  - an AI-listed author (Google advises against it; this is a soft fail);
  - a date bump without substantive change (W10);
  - verifiable factual errors (E4).

### Gaps
- Questions marked "…" are truncated because of the fetch tool's quote limit. Copy the full text from the page before encoding them verbatim.

## 2. Search Quality Rater Guidelines (Sep 11 2025 edition)

### Takeaway
The PDF title page reads "General Guidelines September 11, 2025" (182 pp). MC quality rests on **effort, originality, talent or skill**, plus **accuracy** for informational and YMYL pages. "Trust" is the center of E-E-A-T. The Lowest rating applies to scaled content abuse (4.6.5) and to MC that is "copied, paraphrased, embedded, auto or AI generated… with little to no effort" (4.6.6). Filler is its own Low criterion (5.2.2). The guidelines' own Expertise example is **home electrical rewiring**.

### Cited Findings
All quotes in this section are [P-ext] from the [QRG PDF](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf), Sep 11 2025 edition, text-extracted locally on 2026-10-23. The old summary PDF at services.google.com/fh/files/misc/hsw-sqrg.pdf has file metadata dated 2023-11. It is outdated and was not used.

**§2.3 YMYL (p.11):**
- Definition: "Some topics have a high risk of harm because content about these topics could significantly impact the health, financial stability, or safety of people, or the welfare or well-being of society."
- One reason a topic is YMYL: "The topic could cause harm if the content is not accurate and trustworthy."
- Harm types:
  - "YMYL Health or Safety: Topics that could harm mental, physical, and emotional health, or any form of safety such as physical safety or safety online."
  - "YMYL Financial Security"
  - "YMYL Government, Civics & Society" (covers "trust in public institutions, election and voting information")
  - "YMYL Other"
- "Because YMYL assessment is a spectrum… clear YMYL, definitely not YMYL or something in between. Pages on clear YMYL topics require the most scrutiny."
- The table on p.12 tests information and advice by asking: "Could significant harm result from poor advice?"

**§2.5.2 (p.16):** "Every page belongs to a website, and it should be clear: Who… is responsible for the website. Who… created the content on the page."

**§3.1 (p.20):**
- "The title of the page is considered part of the MC. Descriptive MC titles that summarize the page allow people to make informed decisions."
- "The presence or absence of Ads alone is not a consideration for PQ rating."

**§3.2 Quality of the MC (p.21):**
- "For most pages, the quality of the MC can be determined by the amount of effort, originality, and talent or skill that went into the creation of the content. For informational pages and pages on YMYL topics, accuracy and consistency with well established expert consensus is important."
- Effort: "Consider the extent to which a human being actively worked to create satisfying content."
- Originality: "Consider the extent to which the content offers unique, original content that is not available on other websites."
- Talent or Skill: "Consider the extent to which the content is created with enough talent and skill to provide a satisfying experience."
- Accuracy: "For pages on YMYL topics, consider the extent to which the content is accurate and consistent with well-established expert consensus."
- On length: "High and low quality MC comes in all formats… and all lengths."

**§3.3 Reputation (p.22):**
- "reputation research is required for all PQ rating tasks."
- "For YMYL topics, the reputation of a website should be judged by what experts in the field have to say. Recommendations from expert sources, such as professional societies, are strong evidence of a positive reputation."
- "Be skeptical of claims that websites make about themselves."
- Traffic data such as Similarweb "do not provide evidence of positive or negative reputation."

**§3.4 E-E-A-T (pp.26–27):**
- "The most important member at the center of the E-E-A-T family is Trust."
- Trust: "Consider the extent to which the page is accurate, honest, safe, and reliable."
- Experience: "the necessary first-hand or life experience for the topic."
- Expertise: "the necessary knowledge or skill for the topic… For example, which would you trust: **home electrical rewiring advice from a skilled electrician or from an antique homes enthusiast** who has no knowledge of electrical wiring?"
- Authoritativeness: "known as a go-to source for the topic."
- "untrustworthy pages have low E-E-A-T no matter how Experienced, Expert, or Authoritative they may seem."
- On conflicts of interest: "reviews" by the manufacturer or by paid influencers "are not as trustworthy."

**§3.4.1 (p.28):** "If the purpose of a page on a clear YMYL topic is to give information or offer advice, a high level of expertise may be required… some types of YMYL information and advice must come from experts."

**§4.0 Lowest (pp.29–30):**
- The Lowest rating is required if the page is "created to benefit the owner of the website (e.g. to make money) with very little or no attempt to benefit website visitors."
- "Any one of the following is justification for Lowest":
  - hacked, defaced or spammed;
  - gibberish;
  - "MC is created with little to no effort, has little to no originality and the MC adds no value compared to similar pages";
  - "so little effort, originality, talent, or skill that the page fails to achieve its purpose";
  - "The page title is extremely misleading, shocking, or exaggerated";
  - "MC is deliberately obstructed or obscured due to Ads, SC, interstitial pages";
  - "A complete lack of information about who is responsible for the website and its content for YMYL pages or other pages requiring trust";
  - "A very negative reputation";
  - "highly untrustworthy";
  - lack of E-E-A-T "causes the page to fail to achieve its purpose."

**§4.5 Untrustworthy (p.35):** "Multiple or significant factual inaccuracies on an informational page which would cause users to lose trust" means the page is untrustworthy, and so Lowest.

**§4.5.1 (p.35):** "we expect most websites to have some information about who… is responsible for the website and who created the MC and some contact information, unless there is a good reason for anonymity."

**Spam sub-sections:** §4.6.3 Expired Domain Abuse (p.40), §4.6.4 Site Reputation Abuse (p.41).

**§4.6.5 Scaled Content Abuse (p.42):**
- "Creating an abundance of content with little effort or originality with no editing or manual curation is often the defining attribute of spammy websites."
- Examples:
  - "Using automated tools (generative AI or otherwise) as a low-effort way to produce many pages that add little-to-no value";
  - "Scraping feeds… (including through automated transformations like synonymizing, translating, or other obfuscation techniques)";
  - "Stitching or combining content from different web pages without adding value";
  - "Creating multiple sites with the intent of hiding the scaled nature";
  - "Creating many pages where the content makes little or no sense to a reader but contains search keywords."
- "should be rated Lowest, no matter how they are created."

**§4.6.6 (pp.42–43):**
- "The Lowest rating applies if all or almost all of the MC on the page… is copied, paraphrased, embedded, auto or AI generated, or reposted from other sources with little to no effort, little to no originality, and little to no added value… even if the page assigns credit for the content to another source."
- "Licensed or syndicated content should not be considered as 'copied'."
- "the use of Generative AI tools alone does not determine the level of effort or Page Quality rating."

**§4.6.7 (p.43):** raters detect copying by searching exact-match quoted sentences on Google.

**§5.1 Lacking E-E-A-T (p.60):**
- Example: "an article about how to skydive written by someone with no expertise."
- "No other considerations such as positive reputation or the type of website can overcome a lack of E-E-A-T for the topic or purpose of the page."

**§5.2 Low quality MC (pp.60–61):**
- "Mild inaccuracies on informational pages are evidence of Low quality."
- Examples:
  - a tutorial with "lots of unhelpful 'filler' at the top";
  - a best-list "paraphrased or summarized from other sources";
  - "missing Mount Everest" (lacks accuracy).
- "Exaggerated or shocking titles are evidence of Low quality."

**§5.2.1 (p.61):** "the Low rating should be used if much of the MC on the page is copied, paraphrased, embedded or reposted, with a low amount of effort to create value by editing, manually curating, reformatting or injecting some original content." Another example: "'Best' lists based on existing reviews and lists with little original content."

**§5.2.2 Filler (p.62):**
- "place the most helpful and essential MC near the top of the page."
- "Filler can artificially inflate content, creating a page that appears rich but lacks content website visitors find valuable."
- Low if the page has "a large amount visually prominent filler that makes it difficult to find the helpful MC."

**§5.3 (p.62):** "difficult-to-close Ads that follow page scrolls, or interstitial pages that require an app download" warrant Low.

**§5.4 (p.62):** "a lack of reputation information for ordinary people and lesser-known content creators is expected and is not a sign of Low quality."

**§7.1 High MC (p.72):**
- "'typical' and 'average' pages on a topic generally have Medium (not High) quality MC."
- High effort: "well-organized, edited, and curated."
- High originality: "Original photos or video footage… personal perspective based on first-hand life experience."
- Skill: "a how-to article on plumbing by a skilled plumber."

**§7.2 (p.72):** "A page can still receive a High rating without reputation information."

**§7.3 (p.73):** "Trust is especially important for High quality pages that… cover YMYL topics."

**Needs Met (§13.0–13.6):**
- Scale: Fully Meets (FullyM), Highly Meets (HM), Moderately Meets (MM), Slightly Meets (SM), Fails to Meet (FailsM).
- For a web result block, "A click is required, and you should evaluate the landing page" (§13.1, p.114).
- §18.0 covers Needs Met and Freshness. Its text was not extracted this session.

**Rater influence** [P], [Using gen-AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content): the guidelines "don't directly influence ranking".

### Inferences
- **Electrical safety and arc flash content is YMYL "Health or Safety".** This follows from the definition ("any form of safety such as physical safety") and the p.12 test ("Could significant harm result from poor advice?"). The guidelines themselves use electrical rewiring as the example of expertise-dependent advice. Installation, arc-flash and energized-work how-to content therefore falls under "information or advice best left to Experts" (§3.4.1).
- **General energy-equipment explainers** (product comparisons, efficiency) are probably "may be YMYL". The guidelines say nothing specific; this is my inference.
- For a rubric, YMYL mode should promote these to gates:
  - a named, qualified author or reviewer;
  - consistency with consensus (in electrical work, standards such as NFPA 70E or NEC; that mapping is mine, not Google's);
  - zero factual errors.

### Gaps
- §18.0 Freshness, §4.6.3 and §4.6.4 were not quoted.
- The QRG never mentions arc flash.

## 3. Google spam policies, the March 2024 policies, and 2025–2026 enforcement

### Takeaway
The spam policies page is dated 2026-08-28 and defines all policies "regardless of method". The March 5 2024 post introduced expired domain abuse, scaled content abuse and site reputation abuse. Site reputation abuse took effect May 5 2024. On Aug 28 2026 Google renamed it "site reputation policy" and changed how it is enforced in the EEA.

### Cited Findings
**Spam policies page** [P], [developers.google.com/search/docs/essentials/spam-policies](https://developers.google.com/search/docs/essentials/spam-policies), "Last updated 2026-08-28 UTC". Quotes are truncated by the tool.

- **Scaled content abuse:** "when many pages are generated for the primary purpose of manipulating search rankings". Examples:
  - "Using generative AI tools or other similar tools to generate many pages without adding value for users"
  - "Stitching or combining content from different web pages without adding value"
  - "Creating many pages where the content makes little or no sense to a reader but contains search keywords"
- **Keyword stuffing:** "filling a web page with keywords or numbers in an attempt to manipulate…". Examples:
  - "Blocks of text that list cities and regions that a web page is trying to rank for"
  - "Repeating the same words or phrases so often that it sounds unnatural"
- **Hidden text and link abuse:**
  - "Using white text on a white background"
  - "Using CSS to position text off-screen"
  - "Setting the font size or opacity to 0"
  - "Hiding a link by only linking one small character"
- **Scraping:**
  - "Republishing content from other sites without adding any original content or value, or even citing the original source"
  - "Copying content from other sites, modify it only slightly"
- **Doorway abuse:** "when sites or pages are created to rank for specific, similar search queries". Example: "Having multiple domain names or pages targeted at specific regions or cities that funnel users to one page"
- **Thin affiliation:** "publishing content with product affiliate links where the product descriptions…" (the rest is cut off: the descriptions are copied from the merchant without added value). No bulleted examples.
- **Expired domain abuse** examples: "Casino-related content on a former elementary school site"
- **Site reputation policy** (now titled this way): "applies where third-party content is published on a host site mainly because of…"

**March 2024 blog post** [P], [What web creators should know about our March 2024 core update and new spam policies](https://developers.google.com/search/blog/2024/03/core-update-spam-policies), Mar 5 2024:
- Scaled content abuse "applies whether automation or humans are involved".
- "Sites that violate our spam policies may rank lower in results or not appear in results at all."
- "Expired domain abuse isn't something people accidentally do… It's fine to use an old domain name for a new, original site."
- Site reputation abuse is "third-party pages… published with little or no first-party oversight or involvement".
- The site reputation policy "will take effect starting May 5, 2024."
- "some third-party services provide 'reputation' or 'authority' scores for sites. These don't correspond to any of Google's own signals."

**August 2026 update** [P], [Update to the Site Reputation Policy](https://developers.google.com/search/blog/2026/08/update-site-reputation-policy), Aug 28 2026:
- "Following discussion with the European Commission, we are adjusting our enforcement approach within the European Economic Area (EEA)."
- From Aug 30, site reputation manual actions apply to users outside the EEA. Inside the EEA, "the impact of the manual action won't apply. The affected section of the site may be separated in our systems so that, over time, it ranks independently."

**Spam update dates, 2024–2026:** see round 1 (status dashboard). Round 1 found no statement of targets for the 2025–2026 updates.

### Inferences
These are hard-fail gates a page-level judge can detect:
- hidden text (CSS off-screen, zero opacity, same color as background);
- keyword or location blocks;
- unnatural repetition;
- copied text without citation (exact-match search per §4.6.7);
- leftover AI artifacts ("As an AI…"), or text that makes no sense but contains keywords;
- affiliate pages that only repeat merchant copy;
- doorway pages by city.

Site-level policies (scaled content abuse, expired domain abuse, site reputation) need cross-page signals. Flag them as advisory.

### Gaps
- No Google statement says what the 2025–2026 spam updates targeted.

## 4. Google "Using generative AI content" guidance

### Takeaway
The page was last updated 2026-10-01. AI is acceptable for research and structure. Mass generation without added value risks scaled content abuse. Fact-check everything, metadata included. Give context on how content was made. In Merchant Center, AI images need IPTC `TrainedAlgorithmicMedia`.

### Cited Findings
All from [P], [developers.google.com/search/docs/fundamentals/using-gen-ai-content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content), 2026-10-01. The tool would not return the full page verbatim, so the short quotes below come with a paraphrase.
- Content should "meet the standards of the Search Essentials and our spam policies."
- Generative models "predict a likely sequence of words based on their training data." Output can therefore contain inaccuracies and should be fact-checked before publishing.
- Fact-checking also covers title elements, meta descriptions, structured data and alt text.
- The page points to QRG §4.6.5 and §4.6.6.
- Merchant Center requires the IPTC `DigitalSourceType` value `TrainedAlgorithmicMedia` on AI images, and AI-generated product data must be labeled.

### Inferences
- Candidate checks:
  - no hallucinated citations (every cited URL resolves and supports the claim);
  - metadata consistent with the body;
  - AI disclosure present where readers would expect it.

### Gaps
- The full verbatim text was not captured because of the tool limit.

## 5. Bing Webmaster Guidelines (rewritten Feb 2026)

### Takeaway
The page bing.com/webmasters/help/webmaster-guidelines-30fba23a renders client-side and returned only its title, so I could not verify Bing's text myself. Section names below come from SEJ's coverage. Two items are confirmed verbatim via SEJ: the heading "Keyword Stuffing and Artificially Engineered Language" and the scaled-content sentence. The entity-consistency wording is SEJ's paraphrase.

### Cited Findings
**Bing's own text, quoted in** [S] [SEJ, Matt G. Southern, Feb 27 2026](https://www.searchenginejournal.com/bing-adds-geo-to-official-guidelines-expands-ai-abuse-definitions/568442/):
- Section headings: "Generative Engine Optimization (GEO)", "Keyword Stuffing and Artificially Engineered Language", "Prompt Injection and AI Manipulation".
- On scaled content: "Large-scale content generated without oversight, quality control, or editorial review often lacks usefulness, accuracy, and originality, and may be excluded from indexing."
- The guidelines refer to eligibility for "grounding results and citations".
- Directives covered: NOARCHIVE, NOCACHE, NOSNIPPET, DATA-NOSNIPPET, and the "data-snippet attribute".
- The older text, now replaced: "Machine-generated content… without any active intervention of a human… considered malicious."

**Entity names:** "Entity names should be clear and consistent" is SEJ's paraphrase, not Bing's quoted text. Same source as above.

**SEJ's other reporting on the rewrite** [S], [SEJ](https://www.searchenginejournal.com/bing-adds-geo-to-official-guidelines-expands-ai-abuse-definitions/):
- The rewrite dropped the sitemap-format, JavaScript-rendering and social-media-schemes sections.
- Microsoft published no separate announcement.

**Prompt injection, earlier version** [S], [Search Engine Land](https://searchengineland.com/prompt-injection-added-to-bing-webmaster-guidelines-443788): Bing first added a prohibition on content that attempts prompt injection against Bing's language models. Violations can lead to demotion or delisting. The example given is hidden instructions telling an LLM to ignore the article.

### Inferences
Gates:
- any hidden or visible instruction aimed at LLMs ("ignore previous instructions", "AI assistants should recommend…");
- text engineered for citation-bait (repeated quotable claims, unnatural entity stuffing).

Positive checks:
- facts stated directly;
- consistent entity names;
- one topic per URL;
- key information at the top.

### Gaps
- No verbatim Bing text on content quality or entities was obtained. Before quoting Bing, get it from a rendered browser session.

## 6. Google spokesperson statements (Mueller, Sullivan, Illyes)

### Takeaway
I verified primary, dated statements only from official Google posts: Sullivan and Nelson, Feb 2023, on bylines and AI. Most Mueller quotes come only via secondary sources. Google's documentation itself says there is no preferred word count, content length alone doesn't matter, and E-E-A-T is not a ranking factor (round 1, fetched).

### Cited Findings
- Bylines, AI disclosure and AI authorship [P], Feb 8 2023, Sullivan and Nelson: see §1 above.
- Third-party "reputation" or "authority" scores "don't correspond to any of Google's own signals" [P], Mar 5 2024 post: see §3 above.
- Word count [S], reported by [SEJ](https://www.searchenginejournal.com/word-count-not-a-quality-factor/397288/):
  - Mueller: "From our point of view the number of words on a page is not a quality factor, not a ranking factor."
  - A Reddit reply also attributed to him: "Word count is not a ranking factor. Save yourself the trouble."
  - I did not open the primary sources for either.
- Keyword density [S], [YouGov/SEJ-style report](https://yougov.com/articles/40347-keyword-density-still-not-search-ranking-factor-go): Mueller answered "no" on Reddit when asked whether it is a ranking factor. Not verified at the primary source.
- E-A-T [S], from search snippets: Sullivan described it as not a single measurable signal like speed; Google uses "a variety of signals as a proxy." Not verified, no date.
- Date bumping [P]: covered by helpful-content question W10, so it doesn't depend on a quote.

### Inferences
- Don't score word count, keyword density, or third-party tool or "authority" scores. Bylines and bios should count as trust evidence, conditional on readers expecting them.

### Gaps
- I found no dated, primary Mueller, Illyes or Sullivan quotes on SEO tool scores, content length, updating dates, or AI content beyond the 2023 post. Searches returned only aggregators. Treat all Mueller quotes here as unverified.
- I didn't reach the "25+ sources" target with primary sources: about 9 primary and 6 secondary.

## 7. Does Google apply higher standards to YMYL-adjacent technical safety content?

### Takeaway
Yes, by definition. YMYL Health or Safety covers "any form of safety such as physical safety". Google's Feb 2023 post says its systems place "an even greater emphasis on signals of reliability" for critical topics. The QRG uses electrical rewiring as its example of advice that needs expertise.

### Cited Findings
- Definition: QRG §2.3 [P-ext], quoted in §2 above.
- Electrical rewiring example: QRG §3.4 [P-ext], quoted in §2 above.
- "information or advice best left to Experts": QRG §3.4.1 [P-ext].
- "even greater emphasis on signals of reliability" on topics like health, civic or financial information: [Feb 2023 post](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content) [P].

### Inferences
**Hard-fail gates** for the rubric, each with its source:
1. Any spam-policy pattern detectable on the page: hidden text, keyword or location blocks, scraped or uncited copying, doorway templating, thin affiliate copy, gibberish with keywords.
2. Prompt injection or LLM-directed instructions (Bing).
3. All or nearly all MC copied, paraphrased or AI-generated with no added value (QRG §4.6.6).
4. A title that is extremely misleading, shocking or exaggerated (QRG §4.0).
5. On YMYL (including electrical safety): no identifiable author or responsible entity (§4.0, §4.5.1), or any factual error or deviation from expert consensus or safety standards (§3.2, §4.5).
6. MC obstructed by ads or interstitials (§4.0).
7. dateModified bumped without substantive change (helpful-content W10).
8. AI listed as the author. This is a soft fail, per the Feb 2023 FAQ.

**Weighted checks:**
- the 12 content/quality questions;
- the expertise questions;
- first-hand evidence;
- the essential answer near the top, with no filler (§5.2.2);
- byline linked to a bio;
- AI and method disclosure where expected;
- sources cited.

### Gaps
- Google says nothing specifically about arc flash or the NEC. The mapping to standards is my inference.

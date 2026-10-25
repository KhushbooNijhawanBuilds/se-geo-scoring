# Academic and B2B perspectives on SEO content quality, and the SEO–GEO overlap (as of Oct 2026)

## Q1. What does academic work say about content-quality measurement in search?

### Takeaway
Academic evidence links surface quality signals such as readability only weakly and inconsistently to rank. Longitudinal work shows SEO-optimised affiliate content dominating some query classes. LLM judges are now accepted as a way to produce relevance labels at scale.

### Cited Findings
- Bevendorff, Wiegmann, Potthast and Stein, "Is Google Getting Worse? A Longitudinal Investigation of SEO Spam in Search Engines", ECIR 2024, pp. 56–71:
  - Method: Google, Bing and DuckDuckGo were monitored for one year on 7,392 product-review queries.
  - Affiliate content: all three engines carried more affiliate content than a ClueWeb22 baseline. Only a small share of reviews on the web use affiliate links, but most results did.
  - Google trend: affiliate spam fell somewhat on Google, but text quality trended downward on all three engines.
  - Outlook: the authors expect the line between benign content and spam to blur further with generative AI.
  - Sources: [PDF](https://gwern.net/doc/technology/google/2024-bevendorff.pdf); [dblp](https://dblp.org/pid/195/5852)
- Thomas, Spielman, Craswell and Mitra, "Large Language Models Can Accurately Predict Searcher Preferences", SIGIR 2024:
  - Bing has used LLM labelling for most offline metrics since late 2022.
  - Prompts are tuned against real searcher feedback, and the LLM labels are claimed to be as accurate as human labellers.
  - Sources: [arXiv](https://arxiv.org/html/2309.10621v3); [Microsoft Research](https://microsoft.com/en-us/research/publication/large-language-models-can-accurately-predict-searcher-preferences)
- Follow-up and critique of LLM judging:
  - UMBRELA reproduced the approach with GPT-4o and found high correlation with system rankings. The LLMJudge challenge at SIGIR 2024 benchmarked LLM labels on TREC DL 2023. — [arXiv 2406.06519](https://web3.arxiv.org/pdf/2406.06519); [arXiv 2502.13908](https://arxiv.org/html/2502.13908v1)
  - Critics note the validation was "backported" onto an old TREC collection. — [arXiv 2411.08275](https://arxiv.org/html/2411.08275v1)
- Quality and readability against rank, mostly health-domain studies, with mixed results:
  - JMIR 2013: a website-quality tool and Flesch readability scores correlated moderately to strongly with Google rank. — [JMIR](https://doaj.org/article/ed49d61aaff8494bb4776ce3e2673261)
  - Clinical Gastroenterology and Hepatology 2017: accuracy was not correlated with rank (rs = −0.31, p = .18), and mean reading grade was 11. — [NTU repository](https://nanyangtechnologicaluniv.demo.elsevierpure.com/en/publications/variable-quality-and-readability-of-patient-oriented-websites-on-)
  - A non-peer-reviewed vendor analysis found no significant correlation between readability and rank. — [Originality.ai](https://originality.ai/pt/blog/best-readability-score-to-rank-in-google)

### Inferences
- Readability is best scored as a usability and extractability factor, not as a ranking factor.
- An LLM-as-judge rubric for content quality is defensible if it is calibrated against human judgements, following the Thomas et al. approach.
- Homogenised "SEO-shaped" content is a documented quality risk. That supports penalties for fluff, boilerplate and self-ranking lists.

### Gaps
- I did not retrieve specific learning-to-rank feature-importance studies from 2023–26 (for example LETOR or MSLR feature ablations).
- I did not find a peer-reviewed study that measures SEO content homogenisation directly, beyond Bevendorff et al.
- No web-credibility research from 2023–26 was verified.

## Q2. How much do ranking pages overlap with pages cited by AI engines, and do SEO tactics help or hurt AI citation?

### Takeaway
Overlap between Google's top 10 and AI citations is partial, and the figures vary widely by method and engine:
- Google AI Overviews: roughly 17–76% of citations come from top-10 pages, depending on the study.
- ChatGPT, Gemini and Copilot: about 8–12%.
- Perplexity: about 30–65%.

Academic GEO studies agree that keyword stuffing does not help. Adding evidence (quotations, statistics, cited sources) does help. Ranking within the retrieved context still matters most. Google says AI features need no optimisation beyond normal SEO.

### Cited Findings
- **Ahrefs on AI Overviews** (863k keywords): 76% of cited URLs ranked in the top 10 in July 2025, falling to about 38% in a later snapshot. The rest split between positions 11–100 and outside the top 100. Ahrefs attributes the drop to query fan-out. — [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)
- **seoClarity on AI Overviews** (362k keywords, Oct 2025): about 32% overlap with the top 10. 94% of keywords had at least one overlapping URL in the top 20. — [seoClarity](https://www.seoclarity.net/research/aio-rankings-overlap)
- **BrightEdge on AI Overviews:**
  - Top-10 overlap ran from about 9% to 24% by vertical, highest in healthcare. — [BrightEdge](https://brightedge.com/resources/weekly-ai-search-insights/ai-overviews-one-year-presence-size-citing)
  - About 16.7% of citations came from the top 10 over 16 months, as reported second-hand. — [Radiant Elephant](https://www.radiantelephant.com/?p=51541)
- **Surfer on AI Overviews** (10k keywords): 67.82% of cited pages did not rank in the top 10 for the query or any of its fan-out queries. This is second-hand, via [Radiant Elephant](https://www.radiantelephant.com/?p=51541).
- **Ahrefs on assistants** (Aug 2025, 15k prompts):
  - Only 12% of URLs cited by ChatGPT, Gemini and Copilot were in Google's top 10 for the prompt.
  - Perplexity was close to 1 in 3.
  - Over 80% of the other assistants' citations do not rank for the query at all.
  - Short-tail queries: ChatGPT overlapped 10% with the top 10, Perplexity 65%.
  - Source: [Ahrefs](https://ahrefs.com/blog/ai-search-overlap/)
- **Search Atlas** (domain-level overlap): Perplexity median about 25–30%, ChatGPT about 10–15%. — [SEJ](https://www.searchenginejournal.com/new-data-finds-gap-between-google-rankings-and-llm-citations/561492/)
- **Data-quality caveat:** SEJ warns that these datasets are not comparable. Some of the change may be better citation detection rather than a real shift in selection. — [SEJ](https://www.searchenginejournal.com/google-ai-overview-citations-from-top-ranking-pages-drop-sharply/568637/)
- **GEO paper** (Aggarwal et al., KDD 2024), measured on GEO-bench with GPT-3.5. Relative gains below are my calculations from Table 1. Sources: [arXiv abs](https://arxiv.org/abs/2311.09735v3); [HTML](https://arxiv.org/html/2311.09735v3)

  | Method | Position-adjusted word count | Subjective impression |
  |---|---|---|
  | Quotation Addition | +43% | +28% |
  | Statistics Addition | +33% | +23% |
  | Fluency | +29% | not recorded in my notes |
  | Cite Sources | +28% | not recorded in my notes |
  | Technical Terms | +18% | not recorded in my notes |
  | Easy-to-Understand | +14% | not recorded in my notes |
  | Keyword Stuffing | −9% | about +5% |

  - On Perplexity, keyword stuffing scored about 10% below baseline.
  - Fluency plus Statistics was the best combination.
  - Effects vary by domain. Cite Sources worked best for facts and law; Statistics for law and government and for opinion.
- **C-SEO Bench** (Puerto et al., NeurIPS 2025, arXiv 2506.11097):
  - Most conversational-SEO methods were ineffective, contradicting earlier reports.
  - Traditional SEO, meaning a higher position in the LLM's context, worked better.
  - Gains shrink as more actors adopt the methods, a zero-sum dynamic.
  - Sources: [arXiv](https://arxiv.org/abs/2506.11097); [NeurIPS](https://neurips.cc/virtual/2025/loc/san-diego/poster/121465)
- **Google's position:**
  - Pages need to be indexed and eligible for a snippet. There are no extra technical requirements for AI Overviews or AI Mode, and normal SEO fundamentals apply. — [Google Search Central](https://developers.google.com/search/docs/appearance/ai-features)
  - Secondary coverage reports a May 2026 Google guide that frames optimising for AI features as part of SEO. I could not fetch it (HTTP 403). — [Search Engine Land](https://searchengineland.com/google-publishes-guide-on-optimizing-for-generative-ai-features-477671); [letsdatascience](https://letsdatascience.com/news/google-defines-ai-search-optimization-as-seo-8cf32e65)
- **FAQ and HowTo markup** (Aug 2023):
  - FAQ rich results are now limited to well-known government and health sites. HowTo rich results were cut back; Google's post says desktop only.
  - Unused markup causes no harm and has no visible effect.
  - Source: [Google](https://developers.google.com/search/blog/2023/08/howto-faq-changes)

### Inferences
- Being indexable and ranking well (Google's own guidance) appears necessary but not sufficient for AI citation.
- Fan-out coverage (U6) partly explains why cited pages often rank for sub-queries rather than for the head term.
- Keyword stuffing is the clearest point where old SEO tactics hurt GEO. Evidence density (U4/U5) is the clearest place where GEO adds to SEO.
- Gains from GEO tactics may fade as competitors adopt them (C-SEO Bench). Durable signals such as original insight (ART-3) and authority are safer to weight.
- FAQ schema no longer earns a rich result for most B2B sites. Question-style H2s with visible answers carry the value instead.

### Gaps
- I found no Semrush or Authoritas overlap figures in this pass.
- There is no peer-reviewed study of AI-citation overlap; all the numbers above are vendor studies.
- No study isolated schema markup as a cause of AI citation.

## Q3. B2B and industrial blog SEO specifics

### Takeaway
Industrial buyers search with technical, specification-led, long-tail questions and do most of their research before contacting a vendor. The standard architecture is pillar and cluster pages, with one page per keyword cluster. International sites need hreflang with an x-default fallback.

### Cited Findings
- B2B buyers complete about 70% of their research before contacting a vendor (agency claim; primary source not given). — [Nopio](https://www.nopio.com/blog/manufacturing-seo/)
- Industrial buyers are technical and work through long, specification-driven sales cycles. LLMs increasingly cite manufacturer primary sources when the content is well structured and credentialed. — [Marketing Signals 2026](https://marketingsignals.com/playbooks/the-visibility-playbook-for-manufacturing-and-industrial-b2b/)
- Hub-and-spoke model: a pillar page links to spoke pages on specifications, tolerances and applications. — [Lform](https://lform.com/?p=4174); [IRPR](https://irpr.agency/industrial-b2b-website-keywords)
- Give each keyword cluster a distinct page to avoid cannibalisation. Cover capabilities, industries, certifications and case studies. — [WeAreTG](https://www.wearetg.com/?p=16031)
- Hreflang, per Google's documentation:
  - The three methods (HTML link tags, HTTP headers, sitemap) are equivalent.
  - Each page lists every variant, including itself.
  - Use x-default as the fallback.
  - For one language across several regions, provide a generic language URL.
  - Google does not use hreflang to detect a page's language.
  - Source: [Google](https://developers.google.com/search/docs/specialty/international/localized-versions)
- A ccTLD is a strong implicit country signal, and IP-based redirects are discouraged. This is third-party commentary, not Google policy. — [LinkGraph](https://www.linkgraph.com/blog/hreflang-implementation-guide)

### Inferences
- se.com is organised by country path (for example se.com/uk/en/), so hreflang and canonical consistency matter at the page level for blogs. This is my observation, not verified in this pass.
- Glossary pages suit definitional question queries, which are also the queries AI answers take. U1 and U3 are therefore likely to matter more for B2B than for e-commerce.

### Gaps
- I did not verify how Siemens, ABB, Eaton or Schneider structure their blogs and hreflang. No page inspection was done.
- No dedicated industrial glossary SEO study was found.
- The agency guides are opinion and not empirical.

## Q4. Factor-by-factor map of SEO factors against the GEO rubric

### Takeaway
The GEO rubric already covers most on-page content factors. It is missing the technical and off-page SEO factors: indexability, canonical, hreflang, Core Web Vitals and page experience, mobile, backlinks, URL slug, alt text, structured data and the internal-link graph. Its only real conflicts with SEO are mild ones, around keyword placement and length.

### Cited Findings
Status values:
- **Covered** means a rubric item scores the factor.
- **Partly** means it is scored only in part.
- **Missing** means no rubric item scores it.

Relation values:
- **Agree** means SEO and GEO push the same way.
- **Differ** means they weigh it differently.
- **Conflict** means optimising for one can hurt the other.

| SEO factor | GEO rubric item | Status | Relation |
|---|---|---|---|
| Primary keyword in title, H1 and intro | ART-2 (searcher language), U1 | Partly. No exact-keyword check. | Differ. Stuffing hurts GEO (−9%, [GEO paper](https://arxiv.org/html/2311.09735v3)). Keyword use should be natural. |
| Keyword in URL slug | None | Missing | Neutral for GEO |
| Title length and truncation | ART-2 | Partly. No length check. | Agree |
| Meta description | ART-2 (H1, SEO title and meta consistent) | Partly | Agree |
| Heading hierarchy, single H1 | U3, ART-2 | Covered | Agree |
| Internal links | U8 (descriptive link text) | Partly. No link-graph or cluster check. | Agree. Google cites internal linking ([Google](https://developers.google.com/search/docs/appearance/ai-features)). |
| External authoritative links | U5 | Covered | Agree. Cite Sources gave +28% ([GEO](https://arxiv.org/html/2311.09735v3)). |
| Image alt text | Gate: facts only in image or PDF | Partly | Agree |
| URL structure | None | Missing | Neutral |
| Canonical | None. The penalty for superseded content is related. | Missing | Agree |
| Structured data (Article, author, dates, breadcrumbs) | U5, U9 (visible versions only) | Partly. Markup itself is not checked. | Differ. FAQ markup gives little SERP benefit ([Google](https://developers.google.com/search/blog/2023/08/howto-faq-changes)). |
| Search-intent match | U10 (stage fit), gate: question never answered | Covered | Agree |
| Content depth against competitors | U6, gate: thin page | Partly. No competitor benchmark. | Differ. SEO rewards length; GEO rewards focus. Penalties for fluff and boilerplate. |
| E-E-A-T | U5, U7, ART-3 | Covered | Agree |
| Freshness | U9, penalty for superseded content | Covered | Agree |
| Duplicate content and cannibalisation | Boilerplate penalty (>40%) | Partly. No cross-page check. | Agree |
| Readability | U3, U1, fluff penalty | Partly | Agree. Fluency gave +29% (GEO), but the link to rank is mixed. |
| Core Web Vitals and page experience | None | Missing | Neutral for GEO; SEO tiebreaker |
| Mobile | None | Missing | Neutral |
| Indexability (robots, noindex) | None | Missing | Agree. A prerequisite for AI features ([Google](https://developers.google.com/search/docs/appearance/ai-features)). |
| Hreflang | None | Missing | Neutral. Entity consistency (U8) across locales is related. |
| Backlinks | None | Missing | Partly agree. Off-page authority shapes retrieval rank, which C-SEO Bench finds dominant. |

Rubric items with no direct SEO counterpart:
- U4 factual density
- ART-1 key takeaways
- U1 answer-first
- Penalties for hidden instructions and self-ranking lists

### Inferences
- Answer-first (U1) can conflict mildly with keyword-led intros and with long, scroll-depth content. A one-to-two-sentence answer that contains the topic term satisfies both.
- Hidden-instruction and self-ranking-list penalties suit GEO specifically. The self-ranking-list penalty also matches Bevendorff-style review spam.
- A combined SEO and GEO blog standard should add a technical-eligibility gate covering indexable, canonical and hreflang, and keep CWV and backlinks as site-level context rather than page scores.

### Gaps
- No empirical study tests answer-first against keyword-placement conflicts.
- Conflict ratings for length are inferred from the penalties and are not directly measured.

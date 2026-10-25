# 02 — Industry Data Studies, Platform Documentation & Expert Practitioners (GEO / AEO / LLMO)

**Compiled:** 2026-10-13. **Scope:** 2024 to Oct 2026, weighted toward the most recent work.
**Evidence legend**
- **[D-P]**: data-backed, read in the primary source (study page, official doc, or PDF).
- **[D-S]**: data-backed, but known only from secondary coverage. Treat as directional and confirm before quoting externally.
- **[O]**: opinion, practitioner framework, or vendor claim with no published method.
- **[OFFICIAL]**: platform documentation or an official platform statement.

> Caveat on the evidence base. Nearly all large-scale citation data comes from vendors who sell AI-visibility tools (Ahrefs, Semrush, Profound, BrightEdge, SE Ranking, Yext, Muck Rack, AirOps, and others). Most of it is correlational. Only a handful of studies are quasi-experimental: Ahrefs' schema difference-in-differences test, the arXiv date-injection reranking test, and the Princeton GEO benchmark. AI answers are also highly non-deterministic (see §2.8), so any single-run measurement is noise.

---

## 1. Executive summary: top 30 data-backed findings

| # | Finding | Numbers | Date | Source | Evidence |
|---|---|---|---|---|---|
| 1 | **Google says GEO/AEO "is still SEO."** It lists llms.txt, chunking, rewriting for AI, inauthentic mentions, and special schema as unnecessary for Google Search. | Mythbusting list. "No third-party tool has access to our internal ranking or AI systems." | Guide published 15 May 2026, last updated 10 Jul 2026 | Google Search Central, *AI optimization guide* | [OFFICIAL] |
| 2 | **Google: no special optimization, schema, or AI text files are needed** for AI Overviews or AI Mode. Pages must be indexed and snippet-eligible. Both features use **query fan-out**. | — | Doc last updated 10 Dec 2025 | Google, *AI features and your website* | [OFFICIAL] |
| 3 | **Microsoft (Bing/Copilot) says the opposite on structure.** AI breaks pages into sections and scores each one for clarity and how directly it answers. Microsoft recommends Q&A pairs, lists, tables, schema, measurable facts, and 1–2-sentence "snippable" answers. It advises against hidden tabs, PDFs for core information, and text locked in images. | AI referrals to top sites rose 357% YoY (June 2025) | 8 Oct 2025 | Microsoft Advertising blog | [OFFICIAL] |
| 4 | **Ranking no longer guarantees citation in AI Overviews.** The share of AIO citations that also rank in the top 10 fell from about 76% to about 38%. Of the rest, 31.2% rank 11–100 and 31.0% rank beyond 100. Ahrefs attributes the shift to fan-out under Gemini 3. | 863K SERPs, 4M AIO URLs | 2 Mar 2026 | Ahrefs | [D-P] |
| 5 | **Only about 12% of AI-assistant citations rank in Google's top 10 for the same prompt.** About 80% don't rank for the prompt at all. Perplexity is the exception at 28.6%. ChatGPT is about 8% on both Google and Bing. | 15K long-tail prompts | 11 Aug 2025 | Ahrefs | [D-P] |
| 6 | **In ChatGPT, retrieval rank still drives citation.** A page in retrieval position 1 is cited 58% of the time, falling to 14% at position 10. Pages whose heading closely matches the query (0.90+ similarity) are cited 41% of the time versus 30% below 0.50. Covering 100% of fan-out subtopics adds only 4.6 points, and pages covering 26–50% of subtopics do best. Word count, heading count, and DA were the same (about 2,200 words, about 20 headings, DA about 54) for always-cited and never-cited pages. | 815K query-page pairs, 16,851 queries, 353,799 pages | 13–14 Apr 2026 | Kevin Indig / AirOps (Growth Memo, SEJ) | [D-P] |
| 7 | **About 50% of URLs ChatGPT retrieves end up cited.** The "search" channel converts at 88.5%, Reddit at 1.9%, YouTube at 0.5%. Cited titles are more semantically similar to the prompt (0.602 vs 0.484). Natural-language URL slugs are cited 89.8% of the time versus 81.1% for other slugs. | 1.4M ChatGPT-5.2 prompts | 15 Apr 2026 | Ahrefs | [D-P] |
| 8 | **Citations cluster at the top of the page ("ski ramp").** About 44% of ChatGPT citations come from the first 30% of a page, 31% from the middle, and 25% from the final third. Cited passages are about 2x more likely to contain a clear definition, and direct subject-verb-object statements beat vague framing. | 18,012 verified citations, sampled from about 1.2M answers | ~Feb 2026 | Kevin Indig / Growth Memo (via SEL) | [D-S] |
| 9 | **Brand web mentions, and especially YouTube mentions, correlate more strongly with AI visibility than links do.** In May 2025, branded web mentions correlated at 0.664 with AIO visibility, versus 0.218 for backlinks and 0.326 for DR. In December 2025, YouTube mentions correlated at about 0.737 across ChatGPT, AI Mode, and AIO. | 75K brands, Spearman correlation | 26 May 2025; 12 Dec 2025 | Ahrefs | [D-P] |
| 10 | **Adding schema did not increase AI citations.** Pages that added JSON-LD saw −4.6% in AIO (significant), +2.4% in AI Mode, and +2.2% in ChatGPT (neither significant). In the searchVIU retrieval test, none of ChatGPT, Claude, Perplexity, Gemini, or AI Mode read JSON-LD at fetch time. | 1,885 treated pages vs 4,000 controls, difference-in-differences | 11 May 2026 | Ahrefs | [D-P] |
| 11 | **llms.txt is effectively unused.** About 97% of llms.txt files received zero requests in a month. Otterly logged about 84 llms.txt hits out of 62K AI-bot visits. Google says Search doesn't use the file. | 137K domains (Ahrefs) | 2025–2026 | Ahrefs, Otterly (secondary); Google (official) | [D-S] / [OFFICIAL] |
| 12 | **Cross-engine overlap is tiny.** 91% of citations appear in only one engine, and only about 2.4% of URLs are cited by ChatGPT, Perplexity, and AIO for the same prompt. | 3.7M citations (Omnia data) | 11 May 2026 | Kevin Indig, *The Consensus Gap* | [D-S] |
| 13 | **AI brand lists are non-deterministic.** The odds of getting the same brand list twice are under 1 in 100, and the same list in the same order under about 1 in 1,000. Average visibility of the top-3 brands was 73% on Claude, 68% on Google AI, and 64% on ChatGPT. | 2,961 runs across ChatGPT, Claude, and Google AI | Jan 2026 | SparkToro / Gumshoe | [D-S] |
| 14 | **AI Overviews change constantly.** There is a 70% chance an AIO differs between consecutive observations. Only 54.5% of cited URLs persist between captures, and content shifts roughly every 2.15 days. | 43K keywords | 11 Nov 2025 | Ahrefs | [D-S] |
| 15 | **AI Mode is volatile even within a day.** Across three same-day runs, average URL overlap was 9.2%. AI Mode and AIO URL overlap was 10.7%. AI Mode URL overlap with the organic top 10 was 14%. AI Mode averages 12.6 links per answer. | 10K keywords | 29 Aug 2025 | SE Ranking | [D-P] |
| 16 | **AI Overviews cut the CTR of position 1 by about 58%.** The April 2025 estimate was 34.5%. The drop is about 51% at position 2 and about 19% at position 10. | Dec 2025 vs Dec 2023 | Early 2026 | Ahrefs | [D-S] |
| 17 | **Being cited inside an AIO recovers part of the lost clicks.** Cited brands get about 120% more organic clicks per impression than uncited brands, but about 38% fewer than when no AIO appears. Informational queries: 2.07% CTR cited, 0.94% not cited, 3.35% with no AIO. CTR rebounded in Jan–Feb 2026. | 53 brands, 5.47M queries, 2.43B impressions | 24 Apr 2026 | Seer Interactive v3 | [D-P] |
| 18 | **AIO prevalence depends on query type.** Comparison queries trigger an AIO 95.4% of the time and question-format queries 85.9%. By intent: informational 36%, commercial 8%, transactional 5%. | Same Seer dataset | 24 Apr 2026 | Seer Interactive | [D-P] |
| 19 | **Users click less when an AI summary appears.** Users clicked a result in 8% of visits with an AI summary versus 15% without. Only 1% clicked a link inside the summary, and 26% ended their session (versus 16%). | 900 US adults, March 2025 browsing | 22 Jul 2025 | Pew Research | [D-S] |
| 20 | **Zero-click rates.** 68.01% of US Google searches ended without a click (Jan–Apr 2026, Similarweb panel), up from 58.5–60% in 2024 (Datos panel). AI Mode sessions are about 93% zero-click. | — | 2026; mid-2025 | SparkToro; Semrush (69M sessions) | [D-S] |
| 21 | **AI Mode users accept the AI's shortlist.** 88% accepted the shortlist as-is, 74% picked the item ranked first, and 64% clicked nothing. AIO users behave differently: they compare and re-scroll (47.5% reverse scrolling vs 27% without an AIO). | 185 purchase tasks; 846K sessions | Apr–May 2026 | Kevin Indig / Growth Memo | [D-P] |
| 22 | **AI-cited content is fresher than organic results.** AI-cited URLs average 1,064 days old versus 1,432 for organic SERP results (25.7% fresher). ChatGPT has the strongest freshness bias; AIO has the weakest. Of ChatGPT's top 1,000 cited pages that showed an update date, 89.7% were updated in 2025. | 17M citations | Jul 2025; 28 Oct 2025 | Ahrefs | [D-P] |
| 23 | **LLM rerankers are biased toward recent dates.** Adding a fake recent date to a passage, with no other change, moved the top-10 mean publication year forward by up to 4.78 years and flipped up to 25% of pairwise preferences. | TREC DL21/22, 7 LLMs | 14 Sep 2025 | arXiv 2509.11353 | [D-P] |
| 24 | **Platforms favor different sources.** ChatGPT: Wikipedia 47.9% of its top-10 source share. Perplexity: Reddit 46.7%. AIO: Reddit 21%, YouTube 18.8%, Quora 14.3%, LinkedIn 13%. | 680M citations, Aug 2024–Jun 2025 | Jun/Aug 2025 | Profound | [D-P] |
| 25 | **ChatGPT's source mix can change overnight.** Reddit's share of ChatGPT responses fell from about 60% to about 10% between August and mid-September 2025, and Wikipedia's from about 55% to under 20%. In August 2026, Reddit fell another 86% (from 3.83% to 0.52% of citations). | 230K prompts (Semrush); Promptwatch tracking | 10 Nov 2025; Aug 2026 | Semrush; Promptwatch via SEJ | [D-P] / [D-S] |
| 26 | **YouTube is the most-cited domain in AIO and is growing.** It accounts for 5.6% of all AIO-cited URLs, up 34% in six months. BrightEdge puts YouTube at 29.5% of AIO citations, 16.6% of AI Mode, 9.7% of Perplexity, and 0.2% of ChatGPT. | — | Mar 2026; 2025 | Ahrefs; BrightEdge | [D-P] / [D-S] |
| 27 | **Whether earned or owned media dominates depends on the query set.** Muck Rack finds earned media at about 84% of citations (journalism about 27%; paid 0.3%) across 25M+ links. Yext finds 86% of citations come from brand-managed sources (websites 44%, listings 42%) on local and brand-intent queries. Both are right for their own query mix. | 25M links; 6.8M citations | May 2026; Oct 2025 | Muck Rack; Yext | [D-P] / [D-S] |
| 28 | **AI-assisted content is not penalized in AIO.** 87.8% of AIO-cited pages contain some AI-generated text; only 8.6% are purely human and 3.6% purely AI. The correlation between AI-content share and citation order is 0.017. Google's October 2026 guidance makes manual fact-checking of all AI content "critical." | 500K URLs | 14 Jul 2025; 1 Oct 2026 | Ahrefs; Google | [D-P] / [OFFICIAL] |
| 29 | **Valuation and value of AI traffic.** AI visitors are worth about 4.4x an organic visitor on conversion (Semrush, June 2025). AI referrals to US retail grew 693% YoY in the 2025 holiday season and converted 31% better (Adobe). Only 8.8% of AI-influenced visits arrive as direct referrals; about 56% arrive via branded search (Similarweb via PPC Land). | — | 2025–2026 | Semrush; Adobe; Similarweb | [D-S] |
| 30 | **B2B buyers now research vendors in AI.** 94% of B2B buyers used generative AI in a recent purchase (Forrester 2026, about 18K buyers, reported secondhand). 92% say AI shaped their shortlist and only 7% say brand recognition decides whether they notice a vendor; use-case match does (Semrush, 519 respondents, July 2026). When a vendor hides pricing, AI agents fall back to third-party sources in 45% of runs. | — | 2026 | Forrester; Semrush; Growth Memo | [D-S] / [D-P] |

**Platform scale context.** These figures are mostly secondary; confirm them against company releases. ChatGPT has about 900M weekly users (early 2026). The Gemini app has 950M+ monthly users (July 2026). AI Overviews have 2.5B+ monthly users (Google I/O, May 2026). Similarweb puts ChatGPT's share of generative-AI web visits at about 76% in June 2025, falling to about 53% in May 2026, while Gemini rose to about 27–28% and Claude to about 9%. The share of US ChatGPT answers containing external citations rose from about 1.6% to 6.8% over the same period. About 26% of ChatGPT responses now contain an ad (Similarweb, 2026).

---

## 2. Platform-by-platform behaviour and official guidance

### 2.1 Google: AI Overviews, AI Mode, and Gemini

**Official guidance [OFFICIAL]**
- *Top ways to ensure your content performs well in Google's AI experiences* (Search Central blog, 21 May 2025) lists eight practices:
  1. Unique, non-commodity content.
  2. Good page experience.
  3. Crawl, index, and HTTP-200 basics.
  4. Preview controls (nosnippet, data-nosnippet, max-snippet, noindex).
  5. Structured data that matches visible content.
  6. Multimodal support (images, video, Merchant Center, Business Profile).
  7. Measuring the full value of visits, not just clicks.
  8. Evolving with users.
- *AI features and your website* (updated 10 Dec 2025):
  - "No additional requirements… nor other special optimizations necessary."
  - "No special schema.org structured data that you need to add."
  - No AI text files are needed.
  - AI feature traffic is counted in the Search Console Performance report under "Web."
  - Google-Extended controls Gemini training and grounding, not Search.
  - AIO and AI Mode may use different models, so their links differ.
- *Optimizing your website for generative AI features* (`/search/docs/fundamentals/ai-optimization-guide`, published 15 May 2026, updated 10 Jul 2026):
  - Describes the pipeline as RAG/grounding plus **query fan-out**.
  - States: "optimizing for generative AI search is optimizing for the search experience, and thus still SEO."
  - Calls non-commodity content the most influential long-run factor: "Don't just recycle what others on the internet have already said."
  - Scaled pages built to manipulate AI answers violate the scaled-content-abuse policy.
  - Semantic HTML is recommended but not required.
  - Mythbusting: you don't need llms.txt, chunking, rewriting for AI, long-tail variants, inauthentic mentions, or AI-specific schema.
  - On chunking specifically: "There's no requirement to break your content into tiny pieces," and page length should suit the audience.
  - Warns against third-party tools that claim access to internal metrics.
  - Points agentic readiness to web.dev's *Build agent-friendly websites* guide and the **Universal Commerce Protocol (UCP)**.
  - Notes that a site "must be included in Search generative AI features in Search Console."
- *2026 Marketer's Non-Technical Guide to SEO in AI Search* (Google PDF):
  - Repeats the eight practices.
  - Claims total organic click volume is "relatively stable year-over-year" and that clicks from AIO pages are "higher quality."
  - Says AIO drives more than 10% usage growth for the query types where they appear.
  - **Agentic section:** use Product and MerchantListing markup for commerce, LocalBusiness, Event, JobPosting, and MathSolver.
  - Retailers should feed Google Merchant Center with rich attributes (color, size, special features). Checkout agents also require GPay API integration, guest checkout, and bots not being blocked.
  - Notes that users increasingly seek "forums, videos, podcasts… authentic voices and first-hand perspectives."
- **Search Console Generative AI performance report** (announced 3 Jun 2026):
  - Reports **impressions only**, with no clicks, CTR, or position.
  - Breaks down by page, country, device, and date.
  - Combines AIO and AI Mode in one view, plus a separate Discover view.
  - Rolled out gradually and was not on every property as of Aug 2026. Reportedly not available in the API. [D-S]
- **AI content guidance** (updated 1 Oct 2026): "It is critical to manually factcheck and review all AI-generated content." The review explicitly covers titles, meta descriptions, structured data, and alt text. No new penalty was announced. [OFFICIAL via secondary]

**Observed behaviour [D-P / D-S]**
- **AIO citation sources are decoupling from rankings:**
  - 76% of AIO citations ranked in the top 10 in July 2025, versus 38% in March 2026 (Ahrefs).
  - BrightEdge reports only about 17% from the top 10 in February 2026. This conflicts with its own earlier figure of 54% overlap, so methods differ. [D-S]
  - In AI Mode, about 88% of citations are not in the organic top 10 (Moz, about 40K queries, Feb 2026). [D-S] SE Ranking finds 14% URL overlap.
  - Moz's Tom Capper describes AI Mode as running about 20 sub-searches. [O / D-S]
- **AIO top sources** (Profound): Reddit, YouTube, Quora, LinkedIn, Gartner, NerdWallet, Forbes, Wikipedia.
- **AI Mode top sources** (Semrush, Jul–Oct 2025): LinkedIn (about 15% of responses), YouTube, Reddit, and Google-owned properties. Google Maps business profiles account for 5.7% of all AI Mode links (SE Ranking). AI Mode favors Google-owned properties.
- **Ahrefs cross-feature comparison** [D-S]: AIO and AI Mode reach the same conclusion 86% of the time but have only 13.7% citation overlap.
- **Freshness:** AIO is the least freshness-biased AI surface; it cites content about as old as organic results (Ahrefs).
- **AIO trigger rates** (BrightEdge via secondary sources) [D-S]: rising sharply in B2B tech (36% to 82%) and education (18% to 83%) from February 2025 to February 2026. Ecommerce stays low (about 3%).
- **Shopping in AI Mode** [D-S, vendor]: AI Mode surfaces about 95% fewer product listings than standard search (Productrise, 100K queries, Jul 2026). Only 0.8% of products overlap between the two.

### 2.2 OpenAI: ChatGPT search and shopping

**Official [OFFICIAL]**
- **Crawlers:**
  - `OAI-SearchBot` governs inclusion in ChatGPT search. Sites that opt out are not shown in answers but may still appear as navigational links.
  - `GPTBot` is for training.
  - `ChatGPT-User` handles user-initiated fetches and is not used to decide search inclusion.
  - `noindex` only works if the crawler is allowed to fetch the page.
  - Referral traffic carries `utm_source=chatgpt.com`, trackable in GA.
  - Sources: OpenAI developer docs on bots; publishers FAQ.
- **Shopping (help center):**
  - Product results are "selected independently… not ads."
  - Selection is based on relevance to intent, the user's context (Memory, Custom Instructions), price, reviews, availability, and ease of use.
  - Merchant ranking considers availability, price, quality, and **whether the seller is the maker or primary seller**.
  - Merchants can submit a direct **Product Feed**. Shopify merchants are integrated via Shopify Catalog.
- **Product Feed Spec** (developers.openai.com/commerce):
  - Required fields include a stable ID, title, plain-text description, link, image, price with ISO-4217 currency, and availability.
  - Optional fields include GTIN, MPN, condition, seller, and returns.
  - Flags control discoverability and purchasability.
  - Format, cadence, and transport details differ across secondary sources (CSV/TSV/XML/JSON; refresh as often as 15 minutes). Check the live spec.
- **Agentic Commerce Protocol (ACP)**:
  - Open (Apache 2.0) and co-developed with Stripe, launched September 2025 with Instant Checkout.
  - Components: Checkout API, Delegated Payment spec, webhooks.
  - **Status change [D-S]:** In-chat Instant Checkout was scaled back around 24 March 2026, and the shopping experience was refocused on discovery, with merchants using their own checkout. Reported reasons include Walmart's in-chat conversion at about one-third of its own site's.
  - Product-feed ad format launched 12 May 2026 [D-S].

**Observed behaviour**
- ChatGPT cites pages that often don't rank:
  - 8% of its citations rank in Google's top 10 (Ahrefs).
  - Semrush (June 2025) found ChatGPT-cited pages rank 21+ for related queries about 90% of the time.
  - Profound reports 26% overlap with Bing [D-S].
- **ChatGPT may draw on Google results.** The Information (August 2025) reported that OpenAI used SerpApi-scraped Google results for real-time topics. This is disputed. [D-S]
- **ChatGPT's top 1,000 cited pages** (September 2025, Ahrefs) [D-P]:
  - By type: Wikipedia 29.7%, homepages 23.8%, educational pages 19.4%, app stores 6.6%, reviews 5.8%, news 5.2%.
  - Only 32.3% are content types marketers can influence.
  - 28.3% have zero organic keywords.
  - Among pages that rank, the median domain DR is 90, but 67% have page-level UR 0–10. Domain authority matters; page-level links don't.
- **Source mix:** Wikipedia is the top source (7.8% of all citations; 47.9% of the top-10 share), followed by Reddit, Forbes, G2, TechRadar, and NerdWallet (Profound). Brand-owned content is roughly 1% of ChatGPT citations versus about 7% on Perplexity [D-S]. Yext finds OpenAI leans on **listings** (48.7%) for local and brand queries.
- **Freshness:** ChatGPT has the strongest freshness bias. Cited content is 393–458 days newer than organic results (Ahrefs).
- **Reasoning mode changes the sources** [D-S]:
  - High-reasoning ChatGPT runs about 4.6x more searches.
  - Domain overlap between minimal and high reasoning is about 25.6%.
  - Citation rate rises from 50% to 68%.
  - Reddit share falls from 15% to 7%, while official documentation and academic sources rise from 12.4% to 17.5%.
  - Source: Indig / Semrush, 18 May 2026.
- **Feed-based picks** [D-S, vendor]: ChatGPT Shopping product picks from integrated feeds jumped from 8.26% to 61.54% on 10 July 2026 (Profound). Shopify accounts for about 35% of feed-integrated retrieval.
- **Referral landing** [D-S]: after a May 2026 link update, the share of ChatGPT referrals landing on homepages rose from about 25% to about 60% (Similarweb).

### 2.3 Microsoft: Bing and Copilot

**Official [OFFICIAL]**
- *Optimizing your content for inclusion in AI search answers* (Microsoft Advertising blog, 8 Oct 2025). This is the most prescriptive structural guidance from any platform.
  - **Do:**
    - Align the title, H1, and description.
    - Write descriptive H2/H3 headings that act as "chapter titles."
    - Use Q&A pairs, lists, and tables.
    - Add JSON-LD for Product, Review, FAQ, and Event.
    - Write concrete measurable facts (their example: "42 dB dishwasher" rather than "quiet").
    - Use synonyms.
    - Write self-contained 1–2-sentence answers.
    - Provide alt text.
    - Keep content "fresh, authoritative, structured, and semantically clear."
  - **Don't:**
    - Write walls of text.
    - Hide answers in tabs or accordions.
    - Put core information only in PDFs or images.
    - Overload sentences.
    - Use decorative symbols.
    - Make vague claims ("next-gen," "innovative," "eco").
    - Keyword-stuff.
- *From Discovery to Influence: A Guide to AEO and GEO* (Microsoft Advertising, January 2026, retail-focused, about 15 pages) [D-S on contents]:
  - SEO and catalog investment are the foundation.
  - Copilot uses **web data** for category and brand positioning, and **feed data** for price, availability, and specs.
  - Claims should be "factual, consistent, verifiable."
- Fabrice Canel (Bing), SMX Munich 2025: "schema markup helps Microsoft's LLMs understand your content." [OFFICIAL via secondary]
- **Bing Webmaster Tools AI Performance report** (public preview February 2026):
  - Reports total citations, unique cited URLs, and sample **grounding queries** across Copilot, Bing AI summaries, and partners.
  - No click data, and no per-surface filter. [D-S]
  - Early single-site analyses show heavy concentration. In one, 19,717 citations spread over 86 pages, with one page receiving 69%. [D-S]

**Observed:** Copilot aligns most closely with Bing rankings, with the highest Bing top-10 overlap in the Ahrefs study. IndexNow is logically relevant for freshness on Bing, but no Copilot-specific study was found. [O]

### 2.4 Perplexity
- **Official [OFFICIAL]:**
  - Allow `PerplexityBot` (the index crawler) for search inclusion. IP ranges are published.
  - `Perplexity-User` handles user-initiated fetches and is not used for training.
  - Robots.txt changes take up to 24 hours to apply.
  - The Publishers Program (July 2024) shares revenue. Comet Plus extends payouts to visits, citations, and agent actions [D-S].
  - Perplexity has not disclosed its ranking architecture.
- **Observed:**
  - Perplexity has the highest overlap with Google rankings: 28.6% top-10 overlap (Ahrefs), and 65% for short-tail queries.
  - Reddit is its top source (6.6% of all citations; 46.7% of the top-10 share), then YouTube, Gartner, Yelp, LinkedIn (Profound).
  - It favors vertical specialists such as Zocdoc and TripAdvisor (Yext).
  - Only about 11% domain overlap with ChatGPT [D-S].
- [O] Practitioners recommend direct factual answers, freshness, and topical match. Perplexity is generally seen as the engine most influenced by classic rankings plus recency.

### 2.5 Anthropic: Claude
- **Official [OFFICIAL]** (Anthropic support article on its bots):
  - `ClaudeBot` is for training.
  - `Claude-User` handles user-initiated fetches.
  - `Claude-SearchBot` builds the search index. Blocking it reduces visibility in Claude's search answers.
  - Crawl-delay is honored. IP ranges are not published.
- **Search backend [D-S]:** Brave Search was added to Anthropic's subprocessor list on 19 March 2025. Scrunch found Claude's results closely match Brave's top organic results. Brave follows Googlebot robots rules, so being crawlable by Googlebot matters for Claude too.
- **Observed [D-S]:**
  - Claude includes citations in 55% of responses, averaging 13 sources when it does cite (Muck Rack). It is selective about *whether* to cite, but generous once it does.
  - Claude names fewer brands overall, and near-zero Reddit share is reported.
  - ChatGPT and Claude share only about 17.6% of cited domains per prompt.
  - Claude was the most consistent engine on brand lists (SparkToro): 73% average visibility for the top-3 brands.
  - Claude's share of generative-AI web visits grew from about 2% to about 9% (Similarweb, June 2025 to May 2026).

### 2.6 Gemini (app)
- Gemini uses Google Search grounding. Google-Extended controls Gemini training and grounding outside Search [OFFICIAL].
- Yext finds Gemini favors **first-party websites** (52.1% of citations) [D-S].
- Gemini app usage: 950M+ monthly users (July 2026) [D-S].
- Gemini 3 in AIO is credited with broader fan-out (Ahrefs) [O / D-S].

### 2.7 Cross-platform comparison

| Dimension | ChatGPT | Google AIO | Google AI Mode | Perplexity | Copilot | Claude | Gemini app |
|---|---|---|---|---|---|---|---|
| Retrieval backbone | Own index plus Bing; possibly Google via SerpApi (disputed) | Google index plus fan-out | Google index, about 20 sub-queries | Own index (PerplexityBot) | Bing index | Brave (inferred) plus Claude-SearchBot | Google Search grounding |
| Overlap with Google top 10 | Low, about 8% | 38% (Mar 2026) | 12–14% | Highest, about 29% | Highest with Bing | Unknown | Similar to Google |
| Signature sources | Wikipedia, Forbes, G2, listings | Reddit, YouTube, Quora, LinkedIn | LinkedIn, YouTube, Reddit, Google Maps/properties | Reddit, YouTube, Gartner, Yelp | Bing-ranked pages | Earned media, docs; low Reddit | Brand websites |
| Freshness bias | Strongest | Weakest | Medium | Strong (reported) | n/a | n/a | n/a |
| Volatility | High; source-mix shocks (Sep 2025, Aug 2026) | 70% change rate between captures | About 9% URL overlap across 3 same-day runs | High | n/a | Most consistent on lists | n/a |
| Official first-party guidance | Bot docs, feed spec | "Just SEO"; anti-hacks | Same as AIO | Bot docs | Detailed structure guide | Bot docs | Google-Extended |
| First-party measurement | utm_source=chatgpt.com | GSC Gen-AI report (impressions only) | Same | Referrer | BWT AI Performance (citations, grounding queries) | Referrer | n/a |

### 2.8 Consistency and volatility (cross-cutting)
- Brand lists repeat less than 1% of the time (SparkToro, Jan 2026). **Track visibility percentage across many runs, not rank.**
- AIO changes about 70% of the time between captures (Ahrefs, Nov 2025). AI Mode has about 9% URL overlap across three same-day runs (SE Ranking).
- **Category ownership is durable** [D-P]: clear category owners kept the #1 spot in 90.4% of month-over-month comparisons. Leaders who were replaced had a median lead of 1.3 points versus 2.9 points for those who held. Only 15.2% of categories had a clear owner (Indig, 1,094 categories, Jan–Jun 2026, ChatGPT).
- **Mentions are not citations** [D-P]: the correlation between how often a brand's domain is cited and how often it is mentioned is −0.229. The most-mentioned brand was cited at least once in 69.9% of cases (same study). Measure mentions and citations separately.

---

## 3. Content format and structure findings

### 3.1 Page types most cited
- **Comparative listicles and "best X" pages** [D-S]:
  - Profound (Blyskal deck): comparative listicles are 32.5% of AI citations.
  - Secondary summaries of Ahrefs data put "best X" lists at 40–44% of ChatGPT page types. **This conflicts with the Ahrefs top-1,000 table**, where blogs and articles are only 1.9%; the samples differ.
  - Prismic: 51% of non-homepage citations go to comparison listicles.
  - The Hoth: 85.6% of "best"-intent citations land on roundup or "vs/alternatives/review" URLs.
  - Seer: comparison queries trigger an AIO 95.4% of the time.
- **Risk** [D-S / O]:
  - Lily Ray documents 30–50% visibility losses on sites with mass-produced self-promotional "best X" and "alternatives" pages.
  - In her test of 100 business-software queries, brands that ranked themselves #1 were left out of the recommendation in 83% of the Google AI answers that cited those pages. Citation is being decoupled from recommendation.
  - Indig's listicle study (31 Aug 2026): **freshness was the only factor** that predicted top-3 listicle placement. Author bios, schema, and word count were "noise."
- **Product and service landing pages** were the most-cited identifiable page type in Indig's category study. Homepages were cited only 4% of the time (that sample). In ChatGPT's top 1,000, homepages and landing pages were 23.8%. [D-P]
- **Educational and how-to pages:** 19.4% of ChatGPT's top 1,000 [D-P]. YouTube "how-to" citations are growing fastest [D-S].
- **Original data and primary research** "is much more citation-dense than ordinary pages" (Indig, 6 Jul 2026; detail paywalled) [D-S]. Princeton GEO benchmark (KDD 2024): adding statistics, quotations, and cited sources raised attributed visibility by up to about 40% [D-P (paper) / D-S (per-method figures)].
- **Wikipedia-style reference pages** are the outlier. They have the highest citation rate when retrieved (59%) despite a poor median retrieval rank (24), averaging 4,383 words, 31 lists, and 6.6 tables (Indig/AirOps). [D-P]

### 3.2 Position on page and answer-first writing
- About 44% of ChatGPT citations come from the first 30% of the page [D-S]. Put the answer, definition, and key facts high on the page.
- Cited passages are about 2x more likely to contain definitions, and direct subject-verb-object statements win [D-S].
- Microsoft recommends self-contained 1–2-sentence answers and Q&A pairs [OFFICIAL]. AirOps recommends 40–60-word definition blocks [O].

### 3.3 Headings and query match
- Heading-to-query similarity matters: 41% citation rate at 0.90+ similarity versus 30% below 0.50. Among top-ranked pages, a better match adds 19 points (Indig/AirOps) [D-P].
- Title-to-prompt cosine similarity is 0.602 for cited pages versus 0.484 for uncited (Ahrefs) [D-P].
- Natural-language URL slugs: 89.8% versus 81.1% citation rate [D-P].
- Question-format headings: practitioners recommend them [O]. Microsoft endorses Q&A pairs [OFFICIAL]. Google says you don't need to include every question phrasing, and overdoing it may be spam [OFFICIAL]. No controlled study isolates the effect of question-style headings.

### 3.4 Length and chunking
- **Focused beats exhaustive in ChatGPT.** Pages covering 26–50% of fan-out subtopics beat pages covering everything. The suggested sweet spot is 500–2,000 words and 7–20 subheadings (Indig/AirOps, Apr 2026) [D-P].
- **Conflicting evidence:** ConvertMate's 2026 benchmark found pages over 20K characters got 4.3x more citations than pages under 500 characters. This likely measures *retrieval* rather than *selection* among retrieved pages [D-S].
- **Chunking:**
  - Google says it isn't needed [OFFICIAL].
  - Microsoft says its systems evaluate sections individually and that walls of text hurt [OFFICIAL].
  - Aleyda Solis (June 2025) and iPullRank / Mike King ("relevance engineering," passage-level extractability, semantic triples) advocate self-contained passages [O].
  - **Reconciliation:** write sections that stand on their own under descriptive headings. Don't fragment content into tiny pages.

### 3.5 Lists and tables
- Microsoft recommends lists and comparison tables [OFFICIAL]. Wikipedia's high citation rate co-occurs with heavy use of lists and tables [D-P, correlational]. No isolated causal study was found.

### 3.6 Freshness and dates
- AI-cited content is 25.7% fresher by publication date and 13.1% by last update (Ahrefs) [D-P].
- 89.7% of ChatGPT's top cited pages that showed an update date were updated in 2025, and 76.4% of 564 dated URLs fall in the most-recent bucket [D-P].
- **Counterpoint** [D-P]: within ChatGPT's search channel, the median cited page is about 500 days old (Ahrefs, Apr 2026). Freshness helps most in news and time-sensitive categories.
- LLM rerankers can be swayed by injected dates (arXiv 2509.11353) [D-P]. **Faking dates is a manipulation risk.** Update content substantively and show a visible "last updated" date.
- Freshness is the only factor that predicted top-3 listicle placement (Indig, Aug 2026) [D-S].
- AirOps reports that 40% of pages that lost AI visibility resurfaced after structure and freshness updates [O / no published method].

### 3.7 Statistics, specificity, and original data
- Princeton GEO: statistics, quotation, and source-citation addition gave the largest visibility lifts on GEO-bench [D-P].
- Microsoft: "measurable facts" (42 dB, not "quiet") [OFFICIAL].
- Google: "non-commodity" content with first-hand experience [OFFICIAL].

### 3.8 Multimodal
- YouTube mentions are the top-correlating factor for AI visibility (0.737) [D-P].
- YouTube is the most-cited domain in AIO (5.6% of AIO URLs, +34% in six months). 18.2% of AIO-cited pages outside the top 100 are YouTube URLs [D-P].
- BrightEdge: YouTube holds about 29.5% of AIO citations but only 0.2% on ChatGPT [D-S].
- Video citations concentrate in long-form, transcript-anchored videos and may decay about 43% within a month (Scrunch via Digiday) [D-S].
- Google advises high-quality images and video, VideoObject markup, and key-moment segments [OFFICIAL].
- Microsoft: don't put critical facts only in images; provide alt text [OFFICIAL].

### 3.9 AI-written content
- 87.8% of AIO-cited pages are AI-assisted, and AI share doesn't correlate with citation order (0.017) [D-P].
- Google: the use of AI is fine, but manual fact-checking is "critical," and scaled content abuse is a violation [OFFICIAL].
- Wil Reynolds warns against mass AI content production for visibility [O].

---

## 4. Authority, off-site signals, and entity findings
- **Brand mentions beat links** [D-P]:
  - Branded web mentions 0.664, branded anchors 0.527, branded search 0.392, DR 0.326, backlinks 0.218 (Ahrefs, May 2025).
  - December 2025 update: YouTube mentions about 0.737, branded web mentions 0.66–0.71.
  - Visibility compounds: the top quartile of brands by mentions averaged 169 AIO mentions versus 0 for the bottom quartile.
- **Rankings and brand search also correlate** [D-P via Ahrefs citing Seer]: Seer (2025, about 10K GPT-4o answers) found Google rankings correlated at about 0.65 with ChatGPT brand mentions, Bing rankings at about 0.50, DR at 0.25, and backlinks at 0.10.
- **Profound** [D-S]: 97.2% of AI citations "cannot be explained by backlinks."
- **Domain trust, not page links** [D-P]: among ChatGPT's top cited pages that rank, the median domain DR is 90, while 67% have UR 0–10.
- **Third-party consensus and earned media** [D-P / D-S]:
  - Muck Rack: earned media is 82–89% of citations across editions, journalism 25–27%. Journalism reaches 49% for recent-news queries, and industry-trend queries cite journalism at more than 2x the rate of how-to queries.
  - BrightEdge (via secondary): earned media generates about 325% more citations than owned content.
  - McKinsey (via secondary): brand sites supply only 5–10% of the sources AI consults, and only 16% of brands track AI search.
  - **Counter-evidence:** Yext finds 86% of citations come from brand-managed sources (websites 44%, listings 42%) for local and brand-intent queries.
  - **Implication:** owned content wins branded, factual, and local queries. Earned and third-party content wins unbranded "best/compare" queries.
- **Community and UGC:**
  - UGC out-cites review sites at every buyer-journey stage (Indig, Aug 2026) [D-S].
  - But the Reddit share is unstable in ChatGPT (−83% in Sep 2025, −86% in Aug 2026). Reddit converts to a citation only 1.93% of the time when retrieved (Ahrefs) [D-P].
  - **Don't build a strategy on one platform's share.**
- **Topical authority** [D-S]:
  - Indig, Jun 2026: "Generic off-site authority leaks budget; the sources AI trusts are topic-specific."
  - Indig, Jul 2026: category owners had higher branded search volume in 55.7% of head-to-head comparisons. Treated as clues, not causes.
- **Inauthentic mentions:** Google says they are "less helpful than they seem," and spam systems block manipulation [OFFICIAL].
- **Author and E-E-A-T:**
  - No AI-specific study shows that author bios lift citations. Indig's listicle study found author bios to be noise [D-S].
  - Google's guidance stresses first-hand experience and expertise, which maps to E-E-A-T rather than author markup [OFFICIAL].
  - In the scoring rubric, treat expertise *in the content* (specific, experienced, verifiable) as the signal, not the byline itself.
- **Wikipedia and entity presence:** Wikipedia is ChatGPT's top source (7.8% of all citations; 29.7% of its top 1,000 pages). Wikimedia reported human pageviews down about 8% (Mar–Aug 2025 YoY), which it attributes to AI answers [D-S]. An accurate entity presence (Wikipedia/Wikidata, where notability allows) is a likely lever [O].

---

## 5. E-commerce/PDP and B2B/industrial findings

### 5.1 E-commerce and PDPs
- **Feeds are the primary channel** [OFFICIAL]:
  - Google: Merchant Center plus Product and MerchantListing markup for agentic shopping. Richer attributes (color, size, special features) mean better matching. Checkout needs GPay, guest checkout, and bot access.
  - OpenAI: Product Feed Spec, with the maker or primary seller ranked favorably.
  - Microsoft: feeds supply price, availability, and specs; web content supplies positioning.
- **Protocols** [OFFICIAL / D-S]:
  - Google **UCP** (11 Jan 2026, NRF): an open standard with Shopify, Etsy, Wayfair, Target, and Walmart, endorsed by Visa, Mastercard, Stripe, Adyen, and others. Checkout runs inside AI Mode and Gemini. Requires Merchant Center.
  - OpenAI **ACP** (Sep 2025): in-chat checkout was scaled back in March 2026, and the focus moved to discovery.
- **Selection factors** (OpenAI) [OFFICIAL]: relevance to intent, price, reviews, availability, ease of use, and user context.
- **Microsoft's example** [OFFICIAL]: write measurable attributes ("42 dB"), not adjectives.
- **Observed** [D-S, vendor]:
  - AI Mode shows about 95% fewer product listings than standard search.
  - Retailers took only 2.9% of citations on non-branded shopping questions, and Reddit and YouTube out-cite big-box stores (LLM Pulse, 391K citations, Jul 2026).
  - Adobe: AI referrals to US retail grew 693% YoY in the 2025 holiday season, with 31% higher conversion and a 33% lower bounce rate.
  - Bazaarvoice suggests review *volume* may matter more than star rating (study not yet public).
- **Gap:** no published controlled study isolates the effect of PDP attribute completeness, specs, or reviews on AI recommendations. Treat attribute completeness as an official-guidance lever, not a measured one.

### 5.2 B2B
- **Adoption** [D-S]:
  - Forrester 2026: 94% of B2B buyers used generative AI in their latest purchase (about 18K buyers).
  - G2 (Mar 2026): about 51% start software research in an AI chatbot more often than in Google.
  - Responsive (Oct 2025): generative AI has overtaken search for a quarter of B2B buyers.
  - Semrush (Jul 2026, 519 AI users): 97% say AI helped them discover vendors, 92% say it shaped their shortlist, 83% say it influenced the final decision. Only 7% say brand recognition determines whether they notice a vendor; **use-case precision** does.
- **AI agents on B2B sites** [D-P] (Indig, 13 Jul 2026, 100 B2B products):
  - First-party answer rates were 79% for pricing, 93% for integrations, and 92% for security.
  - With hidden pricing, agents cited a third-party source in 45% of runs. With public pricing, still 18%.
  - Access errors pushed pricing fallback to third parties to 77%.
  - Third-party pricing citations: 52% editorial, 46% directories (G2, Capterra, Vendr).
  - Adding Product and Offer schema raised one page's readiness score from 73 to 93.
  - **Implication:** publish machine-readable pricing, specs, integrations, and compliance facts in HTML.
- **Directories and reviews:** G2 is #4 in ChatGPT's top sources and Gartner is top-5 in Perplexity and AIO (Profound) [D-P]. For B2B, analyst and review platforms are core third-party consensus sources.
- **Category trigger rates** [D-S]: B2B tech AIO trigger rate rose from 36% to 82% (Feb 2025 to Feb 2026, BrightEdge via ALM).

### 5.3 Industrial and manufacturing
- No independent, rigorous GEO study specific to industrial or manufacturing was found. Available sources are agency blogs. [O]
- **Directional points:**
  - Engineers search by spec, application, and compatibility. Procurement searches by part number and certification.
  - Datasheets, application guides, compatibility matrices, and CAD/calculators are the cite-worthy assets.
  - Content authored by applications engineers is said to beat marketing copy [O].
  - Survey figures [D-S, small samples]: 85% of industrial buyers used AI for supplier research in the past 90 days (Kula, n=263). TREW: 75% of engineers have noticed AI summaries, but only 6% find them usually sufficient.
- **Evidence-based inferences for industrial** [O, grounded in the data above]:
  1. Put specs and ratings in HTML tables, not only in PDFs (Microsoft).
  2. Use precise, measurable attributes (Microsoft; Princeton).
  3. Maintain consistent product facts across distributors and marketplaces. Third-party sources fill in when first-party facts are missing or unreadable (Indig agent study).
  4. Publish focused application and how-to pages matched to specific engineering questions (Indig/AirOps query match).
  5. Use YouTube for demonstrations, with transcripts (Ahrefs, BrightEdge).
  6. Keep pages fresh and visibly dated.

---

## 6. Myths vs evidence

| Claim | Verdict | Evidence |
|---|---|---|
| "Add llms.txt to get cited." | **Myth for now.** | Google: Search doesn't use it, and it neither helps nor harms [OFFICIAL]. Mueller (Jun 2025, 2026): "purely speculative" [OFFICIAL]. About 97% of files received zero requests (Ahrefs, 137K domains) [D-S]. Otterly: about 0.1% of AI-bot hits touched llms.txt [D-S]. Chrome Lighthouse added an experimental llms.txt audit to its Agentic Browsing category (mid-2026) [D-S], so it may matter for agents later. Low cost, near-zero proven benefit. |
| "Schema gets you into AI answers." | **Mostly myth for citations of already-visible pages. Useful elsewhere.** | Ahrefs difference-in-differences shows no lift. AI fetchers ignore JSON-LD at retrieval (searchVIU) [D-P]. Correlational studies show 3x co-occurrence (Ahrefs) and +6.5 points (AirOps), likely confounded by site quality [D-P / D-S]. Google says schema isn't required [OFFICIAL]. Bing says it helps its LLMs [OFFICIAL]. Merchant and Product markup matters for shopping and agentic flows [OFFICIAL]. **Keep schema for rich results, entity clarity, Bing, commerce, and agents. Don't sell it as a citation hack. It must match visible content.** |
| "You must chunk content into small passages." | **Partly myth.** | Google says no [OFFICIAL]. Microsoft says sections are evaluated individually [OFFICIAL]. Focused pages beat sprawling guides in ChatGPT [D-P]. **Write self-contained sections, not fragmented pages.** |
| "Longer, ultimate guides win." | **Myth for ChatGPT selection.** | 500–2,000 words performs best; 100% subtopic coverage adds only 4.6 points (Indig/AirOps) [D-P]. Long pages may win at *retrieval* (ConvertMate) [D-S]. |
| "Keyword stuffing and question-variant stuffing help." | **Myth.** | Google says it's unnecessary and potentially spam [OFFICIAL]. Microsoft lists it as a "don't" [OFFICIAL]. Semantic match (embeddings) is what correlates [D-P]. |
| "AI-written content is penalized." | **Myth.** | 87.8% of AIO citations are AI-assisted, with no correlation to citation order [D-P]. Quality and fact-checking requirements still apply [OFFICIAL]. |
| "Rank #1 on Google, so you'll be cited." | **Weakening.** | 38% of AIO citations come from the top 10 [D-P]; 8% for ChatGPT [D-P]. But in ChatGPT's own retrieval ranking, position still dominates (58% citation rate at #1) [D-P]. **Ranking for fan-out sub-queries matters.** |
| "Backlinks drive AI visibility." | **Weak.** | Correlations of 0.10–0.22 for backlinks versus 0.66–0.74 for mentions [D-P]. |
| "Reddit is the #1 lever." | **Unstable.** | Large, sudden share swings in ChatGPT [D-P / D-S]. Yext: 2% of citations once local and intent context is applied [D-S]. It still matters on Perplexity and AIO. |
| "Self-promotional 'best X' lists are a reliable shortcut." | **Risky.** | Lily Ray: 30–50% visibility losses after 2026 spam updates. Own-brand-first lists were left out of 83% of the AI recommendations that cited them [D-S]. |
| "Track your AI rank position." | **Myth.** | Same brand list repeats less than 1% of the time [D-S]. Use visibility percentage across repeated runs [D-S]. |
| "Fake 'updated' dates boost you." | **Works on rerankers in the lab, but it's manipulation.** | arXiv date-injection effect [D-P]. Google's spam policies apply [OFFICIAL]. |
| "Author bios are an AI ranking factor." | **Unproven.** | No AI-specific lift found. Bios were noise in the listicle study [D-S]. |
| "AI clicks don't matter, it's all zero-click." | **Partly true.** | AIO cuts position-1 CTR about 58% [D-S], and AI Mode is about 93% zero-click [D-S]. But being cited recovers CTR (+120% vs not cited, Seer) [D-P]. AI referrals convert better (Semrush 4.4x; Adobe +31%) [D-S]. Google says click quality is higher [OFFICIAL, self-interested]. |

---

## 7. Measurement: KPIs and tools landscape

### 7.1 KPIs (recommended, with rationale)
1. **AI visibility rate (mention rate):** the percentage of runs in which the brand appears for a fixed prompt set, per engine, measured across multiple runs and days. SparkToro shows visibility percentage is far more stable than rank.
2. **Citation rate:** the percentage of runs that cite your domain. Track this separately from mentions; the two are only weakly related (r = −0.229).
3. **Share of voice / citation share** against competitors, per engine. 91% of citations are engine-exclusive, so **never aggregate across engines without a per-engine view.**
4. **Category ownership margin:** your lead over the #2 brand. Leads of at least about 5 points are durable; leads around 1.3 points flip (Indig).
5. **Sentiment and accuracy of brand facts:** whether AI states prices, specs, and claims correctly.
6. **Prompt and fan-out coverage:** which prompts and sub-queries cite you.
7. **First-party platform data:**
   - GSC Gen-AI report (impressions only).
   - Bing Webmaster Tools AI Performance (citations and grounding queries).
   - utm_source=chatgpt.com and other AI referrers in GA4.
   - AI bot crawl logs (OAI-SearchBot, Claude-SearchBot, PerplexityBot).
8. **Business outcomes** (Wil Reynolds; Growth Memo on attribution): branded search lift, direct traffic, assisted conversions, and lead quality. Only 8.8% of AI-influenced visits arrive as direct referrals and about 56% arrive via branded search (Similarweb via PPC Land) [D-S].

**Method hygiene:**
- Fix the prompt set, location, and logged-in state.
- Run each prompt at least 3 times across days.
- Record one row per prompt × engine × date × run.
- Separate mention, citation, and sentiment.
- Note reasoning mode in ChatGPT; only about 25.6% of domains overlap between minimal and high reasoning.

### 7.2 Tool vendors (snapshot, Jul–Sep 2026) [D-S; prices change often, so verify]

| Tool | Positioning | Notes |
|---|---|---|
| **Profound** | Enterprise; real-user conversation data; publishes large citation studies | Self-serve plans ($99 and $399) reportedly pulled from the pricing page by Sep 2026. G2 AEO leader in Winter 2026. |
| **Peec AI** (Berlin) | Mid-market; prompt-level competitive analysis | About €89–$100/month entry. Unlimited seats. SOC 2 and GDPR. |
| **Otterly.AI** | Low-cost entry | $29/month for 15 prompts, up to $489/month for 400. Covers ChatGPT, AIO, Perplexity, Copilot. Brand Visibility Index. |
| **Scrunch AI** | Brands and agencies; crawler/agent analytics | About $250–300/month. |
| **AthenaHQ** | Broad engine coverage (8–11 engines) | About $295/month. No technical audit. |
| **Semrush AI Visibility Toolkit / Enterprise AIO** | Add-on to the SEO suite | About $99–199/month. 25 daily prompts. AI site audit. Powers Indig's reasoning study. |
| **Ahrefs Brand Radar** | Large indexed prompt database plus YouTube, TikTok, and Reddit mention indexes | API and Looker Studio connector. Underpins most Ahrefs studies. |
| **Goodie AI, Bluefish, Conductor, BrightEdge (AI Catalyst), seoClarity, Gauge, HubSpot AEO** | Various | HubSpot connects visibility to CRM data. |

**Caution:** tools measure different things (licensed prompt panels, clickstream, scraped UIs, crawler logs), so numbers won't match across vendors. Google says no tool has access to its internal systems [OFFICIAL]. Fan-out "query" tools generate *plausible* sub-queries; they don't observe Google's actual ones.

---

## 8. Implications for a content GEO scoring rubric

Weights are suggestions based on the strength of evidence. Items marked **(E)** are evidence-backed; items marked **(G)** rest on official guidance only.

| Dimension | What to score | Evidence basis | Suggested weight |
|---|---|---|---|
| **1. Query and intent match** | Title and H1/H2s semantically match the target prompt and its likely fan-out sub-questions. Descriptive natural-language URL slug. | (E) 41% vs 30% citation by heading match; 0.602 vs 0.484 title similarity; 89.8% vs 81.1% for natural slugs | **High (15%)** |
| **2. Answer-first and extractability** | Direct answer or definition in the first 30% of the page and the first sentence of each section. Self-contained 1–3-sentence answers. Subject-verb-object phrasing. No answers hidden in tabs, images, or PDFs. | (E) 44% of citations from the top third; definitions about 2x. (G) Microsoft. | **High (15%)** |
| **3. Focus and appropriate length** | One primary question per page. 500–2,000 words for most pages. 7–20 descriptive subheadings. Covers the core sub-questions without sprawl. | (E) Indig/AirOps | **Medium (10%)** |
| **4. Specificity and evidence** | Measurable attributes (units, ratings, standards), statistics with sources, quotations, original data, first-hand or engineering insight ("non-commodity"). No vague marketing claims. | (E) Princeton GEO; original data is citation-dense. (G) Google, Microsoft. | **High (15%)** |
| **5. Structure** | Logical H1 to H3 hierarchy. Lists for steps. Tables for specs and comparisons. Short paragraphs. Semantic HTML. | (G) Microsoft, Google semantic HTML. (E, correlational) Wikipedia pattern. | **Medium (10%)** |
| **6. Freshness** | Visible, truthful "last updated" date. Substantive refresh cadence by topic volatility. Current facts and prices. | (E) Ahrefs freshness studies; listicle freshness. (Caution) date-manipulation risk. | **Medium (10%)** |
| **7. Technical accessibility** | Crawlable by Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot, and PerplexityBot. HTTP 200. Indexable. Snippet-eligible (no nosnippet on key content). Key content in server-rendered HTML. Canonical set. Fast. | (G) all platforms. (E) access errors raise third-party fallback to 77%. | **Gate (pass/fail)** plus 5% |
| **8. Structured data and feeds** | Valid schema matching visible content (Product/Offer, Organization, Article, FAQ where genuine, VideoObject). Merchant Center, OpenAI, and Bing feeds complete with attributes. | (E) no citation lift for already-cited pages. (G) required for shopping and agents; Bing says helpful. | **Low–Medium (5%)**; higher for PDPs |
| **9. Entity and third-party consensus (off-page, site level)** | Brand and product facts consistent across distributors, marketplaces, review sites, Wikipedia/Wikidata, YouTube, LinkedIn, and trade press. Earned mentions on topic-relevant sources. | (E) mentions 0.66–0.74 correlation; earned media 84%. | Score separately as a **site/brand index**, not per page |
| **10. Multimodal** | Relevant images with descriptive alt text. Video, especially YouTube with transcript and chapters. Captions. Facts not locked in images. | (E) YouTube correlation and AIO share. (G) Google, Microsoft. | **Low–Medium (5%)** |
| **11. Trust and quality (E-E-A-T)** | Accurate, fact-checked (especially AI-assisted drafts, including metadata). Clear authorship and expertise evident *in the content*. No self-serving "we're #1" comparisons without real testing. | (G) Google Oct 2026. (E / D-S) Lily Ray self-ranking risk. | **Medium (10%)**; red flags subtract |
| **Penalties / red flags** | Keyword or question stuffing. Scaled near-duplicate pages. Fake dates. Self-ranking listicles. Schema not matching the content. Hidden key content. Commodity rewrites. | (G) Google spam policies; Microsoft "don'ts." | Deduct |

**Page-type modifiers:**
- **PDP:** raise the weight of attribute completeness, spec tables, units and standards, price and availability, reviews (volume), feed parity, and the maker/primary-seller signal.
- **Comparison / "best for X":** require transparent criteria and evidence of testing, include competitors fairly, add a comparison table, and keep it fresh.
- **How-to / application note:** steps as an ordered list, prerequisites, safety and standards references, video.
- **FAQ / support:** real customer questions, concise answers, FAQ markup optional.
- **B2B solution pages:** public pricing or pricing logic, integration and compatibility lists, certifications and compliance in HTML.

**Measurement loop:** for each scored page, track the prompt set's visibility rate and citation rate per engine (at least 3 runs per prompt), GSC Gen-AI impressions, Bing grounding queries, and AI referrals. Re-score after updates and compare the rubric score with visibility deltas to recalibrate the weights.

---

## 9. Source list (with publish dates)

### Platform documentation (primary)
- Google Search Central, *Top ways to ensure your content performs well in Google's AI experiences on Search* (21 May 2025): https://developers.google.com/search/blog/2025/05/succeeding-in-ai-search
- Google Search Central, *AI features and your website* (updated 10 Dec 2025): https://developers.google.com/search/docs/appearance/ai-features
- Google Search Central, *Optimizing your website for generative AI features on Google Search* (published 15 May 2026, updated 10 Jul 2026): https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google, *2026 Marketer's Non-Technical Guide to SEO in AI Search* (PDF, 2026): https://services.google.com/fh/files/misc/2026_seo_in_ai_search_guide_for_marketers.pdf
- Google Search Central blog, *Introducing Search Generative AI performance reports in Search Console* (3 Jun 2026): https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- Google AI-generated content guidance update (1 Oct 2026), coverage: https://seroundtable.com/google-updates-ai-content-guidelines-factcheck-review-42217.html
- Chrome for Developers, *Agent-ready toolkit / Lighthouse Agentic browsing* (Jun 2026): https://developer.chrome.com/blog/agent-ready-toolkit
- Google UCP launch coverage (11 Jan 2026): https://itbrief.com.au/story/google-unveils-open-ucp-standard-for-ai-driven-shopping
- Microsoft Advertising, *Optimizing Your Content for Inclusion in AI Search Answers* (8 Oct 2025): https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers
- Microsoft, *From Discovery to Influence: A Guide to AEO and GEO* (Jan 2026), breakdown: https://www.searchenginejournal.com/a-breakdown-of-microsofts-guide-to-aeo-geo/565651/
- Bing Webmaster Tools AI Performance report (Feb 2026), coverage: https://www.searchinfluence.com/blog/bing-ai-performance-report-copilot-citations/
- OpenAI, *Overview of OpenAI Crawlers*: https://developers.openai.com/api/docs/bots
- OpenAI, *Publishers and developers FAQ*: https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- OpenAI, *Shopping in ChatGPT* (help): https://help.openai.com/en/articles/11128490
- OpenAI Commerce, *Product Feed Spec*: https://developers.openai.com/commerce/specs/feed
- OpenAI Commerce, *Key concepts* (ACP): https://developers.openai.com/commerce/guides/key-concepts
- Perplexity, *Perplexity crawlers*: https://docs.perplexity.ai/docs/resources/perplexity-crawlers.md
- Anthropic, *Does Anthropic crawl data from the web…* (ClaudeBot, Claude-User, Claude-SearchBot): https://support.claude.com/en/articles/8896518
- Simon Willison on Claude web search and Brave (20 Mar 2025): https://simonwillison.net/2025/Mar/20/claude-can-now-search-the-web/
- Google's Mueller on llms.txt (SER, Jun 2025): https://seroundtable.com/google-ai-llms-txt-39607.html

### Large-scale studies
- Ahrefs, *AI Overview brand visibility factors (75K brands)* (26 May 2025): https://ahrefs.com/blog/ai-overview-brand-correlation/
- Ahrefs, *Top brand visibility factors in ChatGPT, AI Mode, AIO* (12 Dec 2025): https://ahrefs.com/blog/ai-brand-visibility-correlations
- Ahrefs, *Only 12% of AI cited URLs rank in Google's top 10* (11 Aug 2025): https://ahrefs.com/blog/ai-search-overlap/
- Ahrefs, *AI Overview citations from top 10 (38%)* (2 Mar 2026): https://ahrefs.com/blog/ai-overview-citations-top-10
- Ahrefs, *AI assistants prefer fresher content (17M citations)* (Jul 2025): https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/
- Ahrefs, *ChatGPT's most cited pages* (28 Oct 2025): https://ahrefs.com/blog/chatgpts-most-cited-pages/
- Ahrefs, *Why ChatGPT cites one page over another (1.4M prompts)* (15 Apr 2026): https://ahrefs.com/blog/why-chatgpt-cites-pages/
- Ahrefs, *We tracked 1,885 pages adding schema* (11 May 2026): https://ahrefs.com/blog/schema-ai-citations/
- Ahrefs, *AI Overviews cite AI-generated content* (14 Jul 2025): https://ahrefs.com/blog/ai-overviews-cite-ai-generated-content-more-than-human-writing/
- Ahrefs, *AI Overviews reduce clicks by 58%* (early 2026): https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/
- Ahrefs, *AI Overviews change every 2 days* (11 Nov 2025): https://ahrefs.com/blog/ai-overview-change
- Profound, *AI platform citation patterns (680M citations)* (5 Jun 2025, updated Aug 2025): https://www.tryprofound.com/blog/ai-platform-citation-patterns
- Profound / Josh Blyskal deck (content types): https://speakerdeck.com/joshbly/josh-blyskal-profound-we-analyed-10000-000-ai-search-results-dot-dot-dot
- Semrush, *AI search and SEO traffic study (4.4x)* (9 Jun 2025): https://www.semrush.com/blog/ai-search-seo-traffic-study/
- Semrush, *Most cited domains in AI (230K prompts)* (10 Nov 2025): https://www.semrush.com/blog/most-cited-domains-ai/
- Semrush, *Google AI Mode SEO impact (zero-click)* (2025): https://www.semrush.com/blog/google-ai-mode-seo-impact/
- Semrush, *AI Mode comparison study* (2025): https://semrush.com/blog/ai-mode-comparison-study
- Semrush, *How AI tools shape B2B buying* (Jul 2026): https://www.semrush.com/blog/how-ai-shapes-b2b-buying/
- SE Ranking, *AI Mode research: volatility, sources* (29 Aug 2025): https://seranking.com/blog/ai-mode-research/
- Seer Interactive, *AIO impact on Google CTR, Sep 2025 update*: https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update
- Seer Interactive, *AIO impact on Google CTR, 2026 update* (24 Apr 2026): https://seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update
- Seer Interactive, *What drives brand mentions in AI answers* (2025): https://www.seerinteractive.com/insights/what-drives-brand-mentions-in-ai-answers
- BrightEdge, *YouTube presence in AI search*: https://brightedge.com/resources/weekly-ai-search-insights/youtube-presence-ai-search
- BrightEdge, *One year of AI Overviews* (May 2025): https://brightedge.com/news/press-releases/one-year-google-ai-overviews-brightedge-data-reveals-google-search-usage
- BrightEdge, *AIO citations now 54% from organic*: https://www.brightedge.com/resources/weekly-ai-search-insights/rank-overlap-after-16-months-of-aio
- Pew Research Center, *Google users are less likely to click on links when an AI summary appears* (22 Jul 2025): https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/
- Bain & Company, *Goodbye clicks, hello AI: zero-click search* (Feb 2025): https://www.bain.com/insights/goodbye-clicks-hello-ai-zero-click-search-redefines-marketing/
- SparkToro zero-click 2026, coverage (2026): https://searchengineland.com/google-zero-click-searches-2026-study-479717
- SparkToro / Gumshoe, AI recommendation consistency (Jan 2026), coverage: https://searchengineland.com/ai-recommendation-lists-rarely-repeat-study-468076
- Similarweb, *AI search stats 2026*: https://aisearch.similarweb.com/blog/gen-ai-stats/
- Adobe holiday 2025 AI traffic, coverage (Jan 2026): https://www.digitalcommerce360.com/2026/01/13/generative-ai-online-holiday-shopping-traffic-2025/amp/
- Yext, *86% of AI citations come from brand-managed sources* (9 Oct 2025): https://www.yext.com/blog/ai-citations-86-percent-of-sources-are-brand-managed
- Muck Rack, *What Is AI Reading?* (May 2026 PDF): https://media.muckrack.com/documents/What_Is_AI_Reading__May_2026.pdf
- Moz AI Mode citations study (Feb 2026), coverage: https://www.seo.com/blog/ai-mode-citations/
- Wikimedia traffic decline (Oct 2025), coverage: https://www.computing.co.uk/news/2025/ai/wikipedia-reports-traffic-drop
- McKinsey AI search consumer research (≈Oct 2025), coverage: https://letsdatascience.com/news/brands-face-discovery-risk-as-ai-search-grows-3d32c646
- Gartner, 25% search volume drop by 2026 prediction (Feb 2024), coverage: https://searchengineland.com/?p=437650
- The Information / SEL, ChatGPT and SerpApi (Aug 2025): https://searchengineland.com/openai-chatgpt-serpapi-google-search-results-461226
- Reddit ChatGPT citation drop, Aug 2026 (SEJ): https://www.searchenginejournal.com/why-reddits-chatgpt-citation-drop-isnt-fully-explained/534572/
- Productrise AI Mode shopping study (Jul 2026), coverage: https://ppc.land/ai-mode-cuts-google-shopping-listings-95-productrise-finds/
- ChatGPT Shopping feed shift (Profound, Jul 2026), coverage: https://www.relevantaudience.com/ecommerce-marketing/chatgpt-shopping-product-feeds-profound-research/
- ChatGPT Instant Checkout status 2026: https://www.eesel.ai/blog/chatgpt-instant-checkout-2026

### Practitioners and research
- Kevin Indig / Growth Memo:
  - *Shorter, focused content wins in ChatGPT* (13 Apr 2026): https://www.growth-memo.com/p/shorter-focused-content-wins-in-chatgpt; SEJ version (14 Apr 2026): https://www.searchenginejournal.com/shorter-focused-content-wins-in-chatgpt/571857/
  - *The Consensus Gap* (11 May 2026): https://www.growth-memo.com/p/the-consensus-gap
  - *Reasoning lift* (18 May 2026): https://www.growth-memo.com/p/reasoning-lift-what-happens-to-ai
  - *Users behave differently in AI Overviews vs. AI Mode* (25 May 2026): https://www.growth-memo.com/p/users-behave-differently-in-ai-overviews
  - *Topics matter for third-party authority signals* (15 Jun 2026): https://www.growth-memo.com/p/topics-matter-for-third-party-authority
  - *Why most original data never gets cited* (6 Jul 2026): https://www.growth-memo.com/p/why-most-original-data-never-gets
  - *Where AI agents get stuck on your site* (13 Jul 2026): https://www.growth-memo.com/p/where-ai-agents-get-stuck-on-your
  - *Does topical authority matter in AI Search?* (20 Jul 2026): https://www.growth-memo.com/p/does-topical-authority-matter-in
  - *Community signals* (10 Aug 2026): https://www.growth-memo.com/p/community-signals-are-ais-largest
  - *What makes a good listicle?* (31 Aug 2026): https://www.growth-memo.com/p/what-makes-a-good-listicle
  - ChatGPT "first third" citation study (≈Feb 2026, coverage): https://searchengineland.com/chatgpt-citations-content-study-469483
- Lily Ray: self-promotional listicles and AI search (2026), coverage: https://ppc.land/google-ai-overviews-cut-self-ranking-listicle-citations-38-lily-ray-finds/ and https://www.siegemedia.com/conversation/lily-ray-on-ai-slop-geo-and-what-actually-works
- Aleyda Solis, *AI Search Content Optimization Checklist* (16 Jun 2025): https://www.aleydasolis.com/en/ai-search/ai-search-optimization-checklist
- iPullRank (Mike King), AI Mode and query fan-out webinars and recaps (2025): https://ipullrank.com/ai-mode-webinar-recap and https://ipullrank.com/resources/webinars/query-fan-out-webinar
- Wil Reynolds on AI visibility as a vanity metric (Feb 2026), commentary: https://somethinginc.com/blog/is-ai-visibility-tracking-a-vanity-metric/
- AirOps, *AEO content structure best practices* (25 Jan 2026): https://airops.com/blog/improve-article-structure-increase-llm-citations
- Aggarwal et al., *GEO: Generative Engine Optimization* (arXiv 2311.09735, KDD 2024): https://arxiv.org/abs/2311.09735
- Fang et al., *Do LLMs favor recent content? Recency bias in LLM reranking* (arXiv 2509.11353, 14 Sep 2025): https://arxiv.org/abs/2509.11353v1
- AI visibility tools comparison (Sep 2026, prices): https://www.eclincher.com/articles/profound-alternatives-8-ai-visibility-tools-after-profounds-pricing-change

### Notes on verification gaps
- Paywalled Growth Memo sections (listicle factors, original data, community signals): only headlines and teasers were visible.
- The "best X listicles = 40–44% of ChatGPT citations" figure comes from secondary summaries and conflicts with Ahrefs' own top-1,000 table.
- BrightEdge's 2026 "17% from top 10" figure is secondary and conflicts with its own earlier 54% figure.
- The Microsoft AEO/GEO PDF and OpenAI help pages could not be fetched directly (403 errors); their contents here come from search snippets and secondary breakdowns.
- Forrester, G2, and 6sense B2B survey figures are secondary.
- Ahrefs' 1.4M-prompt ChatGPT study lists its data as "February 2025," but it uses ChatGPT 5.2, so the collection date is likely February 2026.
- No rigorous industrial or manufacturing GEO study exists. The industrial recommendations in §5.3 are inferences from cross-industry evidence.

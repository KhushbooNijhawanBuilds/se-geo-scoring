# Answer-Engine Platform Notes (snapshot Oct 2026; volatile, so re-verify quarterly)

| Dimension | ChatGPT | Google AI Overviews | Google AI Mode | Perplexity | Copilot | Claude | Gemini app |
|---|---|---|---|---|---|---|---|
| Retrieval backbone | Own index + Bing (Google via SerpApi reported, disputed) | Google index + fan-out | Google index, ~20 sub-queries | Own index (PerplexityBot) | Bing | Brave (inferred) + Claude-SearchBot | Google Search grounding |
| Overlap with Google top 10 | ~8% | 38% (Mar 2026; was 76%) | 12–14% | ~29% (highest) | Highest with Bing | n/a | Similar to Google |
| Signature sources | Wikipedia, Forbes, G2, listings; Reddit share collapsed Aug 2026 | Reddit, YouTube, Quora, LinkedIn | LinkedIn, YouTube, Reddit, Google properties/Maps; official brand category/product pages | Reddit, YouTube, Gartner, Yelp | Bing-ranked pages; LinkedIn | Earned media, docs; near-zero Reddit | First-party sites (52%) |
| Freshness bias | Strongest | Weakest | Medium | Strong | n/a | n/a | n/a |
| Volatility | High; overnight source-mix shocks | 70% change between captures | ~9% URL overlap across 3 same-day runs | High | n/a | Most consistent on brand lists | n/a |
| Official content guidance | Bot docs, product feed spec | "Still SEO"; non-commodity content; no special schema, chunking or llms.txt | Same as AIO | Bot docs | **Most prescriptive**: Q&A, lists, tables, measurable facts, no hidden tabs/PDF-only/image-only info, snippable 1–2-sentence answers | Bot docs | Google-Extended |
| First-party measurement | utm_source=chatgpt.com | GSC Gen-AI report (impressions) | Same | Referrer | Bing WMT AI Performance (citations, grounding queries) | Referrer | n/a |

**Implications for content scoring:** the Score Agent stays engine-agnostic, but the recommendations can note:
- Copilot/Bing reward explicit structure and measurable facts the most.
- ChatGPT rewards freshness and focused pages.
- AI Mode rewards official category/product pages with guide layers.
- Claude rewards precise, sourced numbers and neutral tone.
- Perplexity rewards classic ranking plus recency.

Reasoning modes change the sources. High-reasoning ChatGPT runs about 4.6x more searches and cites more official documentation (12.4% to 17.5%), which favours rich technical HTML.

**Crawlers (tech, out of scope; reference only):** OpenAI GPTBot (training) / OAI-SearchBot (search) / ChatGPT-User (user fetch) · Anthropic ClaudeBot / Claude-SearchBot / Claude-User · Perplexity PerplexityBot / Perplexity-User · Google-Extended (Gemini training and grounding; does not affect Search).

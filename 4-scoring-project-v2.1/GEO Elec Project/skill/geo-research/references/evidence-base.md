# GEO Evidence Base: What Actually Moves AI Citations (state of knowledge, Oct 2026)

Synthesized from about 57 academic papers (2023–Oct 2026), about 80 dated industry studies and platform docs, more than 20 open-source GEO tools/skills, practitioner communities, and SE internal sources. Full reports are in the project folder `GEO Elec Project/research/01–04`.

**Evidence labels:** **[C]** controlled/causal study · **[L]** large-sample correlational (usually vendor-run) · **[O]** official platform statement · **[P]** practitioner consensus/opinion · **[SE]** SE house guidance.

Quote numbers with their source and date. Most large studies are vendor-run and correlational, and AI answers are non-deterministic.

---

## 1. The core model: how an answer engine picks sources

1. **Two layers** [SE][O]: parametric memory (what the model knows) + retrieval layer (live search, then fetch, then passages, then synthesis with citations). GEO for owned content targets the retrieval layer.
2. **Query fan-out** [O]: Google AI Overviews and AI Mode expand one prompt into many sub-queries (AI Mode runs about 20 sub-searches) and retrieve sources for each one. Pages are cited for *sub-questions*, not only the head query.
3. **Passages, not pages** [O]: Microsoft says assistants parse pages into sections and score each one for clarity and directness. Google says no special chunking is needed. **Reconciliation:** write self-contained sections under descriptive headings, and don't fragment the content into tiny pages.
4. **The funnel is retrieved → cited → mentioned → recommended** [P][L]. These stages are separate. Mention and citation rates are only weakly related (r = −0.23). Self-promotional listicles get cited but recommend competitors (69%).
5. **Retrieval gates everything** [C]: being retrieved and ranked into the model's context beats any content tactic. Moving a page to context position 1 gave +2.77 ranks, against +0.36 for the best content tactic (C-SEO Bench, NeurIPS 2025). In ChatGPT, retrieval position 1 is cited 58% of the time and position 10 only 14% [L]. **A content score measures citation-readiness given retrieval. It is necessary, not sufficient.**

## 2. Content factors ranked by evidence strength

| # | Factor | Evidence | Strength | Score Agent criterion |
|---|---|---|---|---|
| 1 | **Query/intent relevance**: the page directly answers the prompt; query terms and synonyms used naturally | On-topic vs off-topic odds ratio > 10,000; query terms present OR 6–40 (SIGIR 2026) [C]; relevance edits win, style edits don't (ACL 2024) [C]; heading–query match 41% vs 30% citation, title similarity 0.60 vs 0.48 [L] | **Strong** | U1, U6 |
| 2 | **Concrete, verifiable facts**: specs, prices, numbers with units, definitions, comparisons | Specs OR 8.6 to > 10k; price OR 6–30+ [C]; numbers +62%, definitions +57%, comparisons +55% absorption [L]; Microsoft "42 dB not quiet" [O] | **Strong** | U4, PDP-1 |
| 3 | **Freshness with a visible date** | Recent vs old timestamp OR 14 to > 10k [C]; a date alone flips up to 25% of reranker preferences [C]; AI-cited URLs are 25.7% fresher than organic results [L]; ChatGPT has the strongest freshness bias [L]. An old date is worse than no date | **Strong** | U9 |
| 4 | **Neutral, non-promotional tone** | Promotional vs neutral OR up to 362 against promotion [C]; ad-style rewrite −1.82, storytelling −4.36 rank (E-GEO) [C]; AutoGEO cross-engine rule [C] | **Strong** (promotion hurts) | U7 |
| 5 | **Depth / completeness** (coverage, not word count) | Deep vs shallow OR 4 to > 10k [C]; top-influence pages about 11x longer [L]. But in ChatGPT, *focused* pages covering 26–50% of fan-out sub-topics beat exhaustive ones; sweet spot 500–2,000 words [L] | Moderate–strong | U6 |
| 6 | **Answer-first / top of page** | 44% of ChatGPT citations come from the first 30% of the page [L]; cited passages about 2x more likely to contain a definition [L]; AutoGEO rule "conclusion first" [C] | Moderate–strong | U1 |
| 7 | **Self-contained passages** | Passage independence up to +56% factual correctness in RAG [C]; segments cut mid-thought are under-used [C] | Moderate | U3 c4, BLK-1 |
| 8 | **Confident, evidence-backed, consistent claims** | Confident vs hedged OR 2.7–754; evidence-backed OR 2–46; consistent vs contradictory OR 1.7–4.1 [C] | Moderate–strong | U5, U8, FAQ-2 |
| 9 | **Original / non-commodity information** | Google: non-commodity content is the most influential long-run factor [O]; original data is citation-dense [L] | Moderate | ART-3, U5 c4 |
| 10 | **Statistics, quotations, cited sources** (added as tactics) | +33% / +43% / +28% in the original GEO paper (KDD 2024, GPT-3.5) [C]. **Did not replicate**: only 3 of 54 C-SEO settings were positive, and "add statistics" hurt in 19 of 24 [C]. Credibility style cues are ignored (ACL 2024) [C] | **Contested**: real, relevant evidence helps; decorative additions don't | U5 (substance only) |
| 11 | **Structure** (headings, lists, tables) | Formatting alone, with content held constant: about zero effect (OR ≈ 1) [C]. Structured pages are over-represented among citations [L] (likely a depth confound). Microsoft recommends lists, tables and Q&A [O] | Contested: an enabler, not a lever | U3 |
| 12 | **Q&A / FAQ format** | Semrush Q&A +25% [L]; E-GEO FAQ ≈ +0.05 [C]; absorption −5.7% [L] | Weak/contested | FAQ-*, PDP-5 |
| 13 | **Author bylines / E-E-A-T markup** | No AI-specific lift; bios were "noise" in a listicle study [L]; E-E-A-T signals +31% (Semrush) [L] | Unproven as a byline; expertise in the content matters | U5 c5 |
| 14 | **Keyword stuffing** | −8.7% (GEO paper), about −10% on Perplexity, null or negative everywhere [C] | **Strong: doesn't work** | Penalty |

## 3. Off-page and site factors (flag; outside the content score)

- **Brand mentions beat backlinks**: branded web mentions r = 0.66, YouTube mentions r = 0.74, backlinks r = 0.22 vs AI visibility [L].
- **Earned/third-party media dominates**: 69–94% of AI citations [C-observational]. SE: ~80% third-party, of which ~50% is the channel ecosystem (distributors/partners) [SE]. Exception: owned/listing sources win branded and local queries (Yext 86%) [L].
- **Own-domain retrieval gates brand mention**: about 3% mention rate when the own domain is not retrieved, 91–100% when it is retrieved with a branded fan-out [C-observational].
- **Recognition ≠ discovery**: 99% name recognition vs 3% discovery for generic prompts [C-observational].
- **Schema/JSON-LD**: no citation lift in a controlled difference-in-differences test, and AI fetchers ignore JSON-LD at retrieval [L]. Still useful for Bing, shopping feeds, agents and rich results. Must match the visible content. *(Tech, out of Score Agent scope.)*
- **llms.txt**: about 97% of files are never requested; Google doesn't use it [L][O]. Near-zero proven benefit except for developer docs.
- **Crawler access**: blocking Google's AI crawler reduces AIO retrieval [C]. Each vendor separates training, search and user-fetch bots (GPTBot / OAI-SearchBot / ChatGPT-User; ClaudeBot / Claude-SearchBot / Claude-User; PerplexityBot / Perplexity-User). *(Tech.)*
- **Video**: YouTube is the most-cited domain in AIO (5.6% of cited URLs, +34% in 6 months). View count has close to zero correlation with citation; transcripts and chapters matter [L].

## 4. Platform differences (summary; see platforms.md)

ChatGPT: low Google overlap (about 8%), strongest freshness bias, Wikipedia-heavy, volatile source mix (Reddit share fell about 86% in Aug 2026). AI Overviews: 38% of citations from the Google top 10 (Mar 2026), YouTube/Reddit/LinkedIn heavy, weakest freshness bias. AI Mode: about 9% URL overlap across same-day runs, favours official brand category/product pages and Google properties. Perplexity: highest Google overlap (about 29%), Reddit-heavy. Copilot: Bing-aligned; Microsoft gives the most prescriptive structure guidance. Claude: Brave-backed (inferred), selective about whether to cite, low Reddit share, favours precise, well-sourced numbers and juried sources. Gemini app: favours first-party sites (52%). **91% of citations appear in only one engine**, so optimize and measure per engine.

## 5. E-commerce, PDP and B2B industrial

- AI shopping surfaces consume **feeds + page data**: Google Merchant Center (2026 conversational attributes: Q&A, document links, parts & accessories, variant axes), the OpenAI Product Feed (factual description, category path, dimensions, GTIN/MPN; maker or primary seller favoured), Microsoft (feeds for price, availability and specs; web for positioning). **Consistency between page, feed and datasheet** is the content implication.
- E-GEO: winning PDP rewrites align with user intent, state competitive differentiation and surface review evidence. Storytelling and minimalist copy hurt.
- B2B: 94% of buyers used GenAI in a recent purchase; use-case precision, not brand recognition, decides whether a vendor gets noticed (only 7% say brand recognition). With pricing hidden, AI agents cite a third party 45% of the time.
- Industrial: 69% of technical buyers use AI, but only about 6% find AI summaries sufficient, and datasheets are the most valued content (77–86%). So **verifiable specs in HTML + an HTML summary layer for every PDF**. No rigorous manufacturing-specific GEO study exists, so these industrial recommendations are inferred from cross-industry evidence.

## 6. Myths vs evidence

| Claim | Verdict |
|---|---|
| "Add statistics/quotes and get +40%" | Lab result on GPT-3.5; doesn't replicate. Real, relevant data helps; decoration doesn't. |
| "llms.txt gets you cited" | Myth (for now). |
| "Schema gets you into AI answers" | Mostly myth for citations; hygiene for Bing, commerce and agents. |
| "Chunk everything into tiny passages" | Partly myth. Write self-contained sections, not fragments. |
| "Longer ultimate guides win" | Myth for ChatGPT selection; focused wins. |
| "AI-written content is penalized" | Myth (87.8% of AIO-cited pages are AI-assisted). Fact-checking is mandatory, and scaled abuse is spam. |
| "Rank #1 on Google, so you'll be cited" | Weakening (38% AIO, 8% ChatGPT). Rank for the fan-out sub-queries. |
| "Backlinks drive AI visibility" | Weak (r ≈ 0.1–0.2). Mentions matter more. |
| "Self-promotional best-X lists are a shortcut" | Risky. Cited but not recommended; targeted by spam updates. |
| "Track AI rank position" | Myth. The same list repeats < 1% of the time. Track visibility rate over repeated runs. |
| "Fake 'updated' dates boost you" | Works on rerankers in the lab; it's manipulation and a spam risk. |
| "Formatting = GEO" | Formatting alone ≈ no effect. Self-contained, fact-bearing structure is what matters. |

## 7. Risks and integrity

- Body-only LLM rewriting can **reduce** retrieval (−9% on average, −36% for AutoGEO) and citation (−6% to −22%) (SAGEO Arena 2026). Preserve lexical match to the target queries.
- Gains are zero-sum and shrink as competitors adopt the same tactics (C-SEO Bench).
- Adversarial methods (strategic text sequences, prompt injection, RAG poisoning) work in the lab, but defences cut success from about 50% to about 6%, and Google's May 2026 spam policy explicitly covers manipulation of AI responses. Hard negative.

## 8. Measurement (for validating content changes)

- KPIs [SE]: Visibility score, **Share of Voice** and **Citation Share** (primary), Sentiment. Add accuracy of brand facts and category ownership margin.
- Method: fixed prompt panel (20–50 prompts) × each engine separately × **≥ 7 repetitions** (minimum 3–5) × multiple dates, logged out, with **untreated control pages**. Track the retrieved → cited → mentioned → recommended ladder separately.
- First-party data: GA4 "AI Assistant" channel (from Jun 2026), GSC Generative AI report (impressions only), Bing Webmaster Tools AI Performance (citations + grounding queries), utm_source=chatgpt.com, Profound.
- Expect under-attribution: about 9% of post-recommendation visits show as AI referrals, and about 56% arrive through branded search.

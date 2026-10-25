# 01 — Academic and Research Literature on Generative Engine Optimization (GEO)

Compiled: 2026-10-13. Scope: peer-reviewed papers and arXiv preprints (2023 to Oct 2026) on how content gets retrieved, cited, and used by AI answer engines (ChatGPT, Perplexity, Google AI Overviews/AI Mode, Gemini, Claude, Copilot), plus adjacent IR/NLP work (RAG poisoning, LLM source bias, position bias, chunking).

**How to read this document**
- **[V]** = verified by reading the paper's arXiv abstract/HTML page during this research.
- **[V-survey]** = number taken from the July 2026 critical survey (Martinez, arXiv:2607.14035), which summarizes the primary paper; the primary paper itself was not opened.
- **[I]** = my inference or synthesis, not a claim made by the paper.
- Percent changes in the Aggarwal et al. table were computed from the paper's Table 1 values; the paper's own text rounds slightly differently (noted where relevant).

---

## 1. Executive summary: the 22 most evidence-backed findings

| # | Finding | Effect size | Source | Strength |
|---|---|---|---|---|
| 1 | **Relevance to the query is the dominant driver of being cited**, ahead of any style/content tactic. | Wan et al.: relevance edits (question prefix, rewrite for relevance) substantially raised "win rate"; style edits (adding scientific references, neutral tone) were neutral-to-negative. Vishwakarma et al.: on-topic vs off-topic OR >>10,000 in 5 of 6 LLMs; query terms present vs missing OR 6-40. Zhang/He/Yao: LLM relevance score is the strongest correlate of absorption (r=0.43). | Wan et al. ACL 2024 [V]; Vishwakarma et al. SIGIR 2026 [V]; Zhang et al. 2026 [V] | Strong |
| 2 | **Position in the retrieved context (i.e., classical retrieval rank) matters more than content edits.** | C-SEO Bench: moving a doc to context position 1 = +2.77 rank (Retail) vs best content method +0.36. Vishwakarma: position 1 vs 2 OR 1,795 to >10k. Lost in the Middle: 75.8% accuracy at pos. 1 vs 53.8% at pos. 10 (20 docs). | Puerto et al. NeurIPS 2025 [V]; Vishwakarma 2026 [V]; Liu et al. TACL 2024 [V] | Strong |
| 3 | **Original GEO result: adding quotations, statistics, and citations raised visibility ~28-43% in a controlled 5-source setup.** | PAWC: Quotation +42.6%, Statistics +32.8%, Fluency +28.7%, Cite Sources +27.7% (baseline 19.5). | Aggarwal et al. KDD 2024 [V] | Strong *within its setup*; contested in replication (see #4) |
| 4 | **Those same heuristics largely fail to replicate on newer models / other domains.** | C-SEO Bench: only 3 of 54 method-domain cells significantly positive (none in QA); "Statistics" *decreased* rank in 19 of 24 settings. E-GEO: 11 of 15 heuristic prompts hurt; "authoritative" -0.64, "advertisement" -1.82. | Puerto et al. 2025 [V]; Bagga et al. E-GEO v2 2026 [V] | Strong (that fixed heuristics are unreliable) |
| 5 | **GEO gains are biggest for lower-ranked sources; top-ranked sources can lose.** | Cite Sources: rank-5 source +115.1% visibility, rank-1 source -30.3%. Quotation: rank-5 +99.7%, rank-1 -22.9%. | Aggarwal et al. Table 2 [V] | Moderate (single setup) |
| 6 | **Keyword stuffing does not work** in generative engines. | PAWC -8.7% vs baseline (GPT-3.5); ~-10% on Perplexity; survey: null or negative across benchmarks. | Aggarwal et al. [V]; Martinez survey [V] | Strong |
| 7 | **Freshness / a recent date is a strong, consistent selection cue**, and LLM rerankers have a measurable recency bias. | Vishwakarma: recent vs old timestamp OR 14 to >10k across 6 LLMs; recent vs no timestamp OR 1.15-13. Fang et al.: date injection alone shifted top-10 mean publication year by up to 4.78 years, moved items up to 95 ranks, and reversed up to 25% of pairwise preferences. Chinese GSE study: citation half-life ~39 days (time-sensitive queries) / ~68 days (others). | Vishwakarma 2026 [V]; Fang et al. 2025 [V]; Zhen et al. 2026 [V] | Strong |
| 8 | **Concrete facts (prices, specs, numbers, definitions, comparisons) increase citation and "absorption".** | Vishwakarma: specs vs none OR 8.6 to >10k; price vs none OR 6-30+. Zhang/He/Yao: pages with numbers/statistics +61.6% mean influence, definitions +57.3%, comparisons +55.3%, how-to +41.2%. | Vishwakarma 2026 [V]; Zhang et al. 2026 [V] (correlational) | Strong / moderate |
| 9 | **Depth / completeness beats shallow coverage.** | Vishwakarma: deep vs shallow OR 4 to >10k (all 6 models). Zhang/He/Yao: top-quartile-influence pages average 1,943 words vs 170 (11.4x) and 10.6 headings vs 0.85. | Vishwakarma [V]; Zhang [V] (correlational) | Moderate-strong |
| 10 | **Formatting alone (structure vs dense text) has little causal effect once content is fixed.** | Vishwakarma: structured vs dense OR 0.78-1.68 (mostly n.s.); "organized vs scattered" weak (1.1-3.9). E-GEO "format" prompt +0.02. Survey: "authoritative tone and formatting alone: weak or unstable." | Vishwakarma [V]; E-GEO [V]; Martinez [V] | Moderate (contested by correlational studies that find structured pages over-represented) |
| 11 | **Confident, evidence-backed, internally consistent, non-promotional prose wins pairwise.** | Confident vs hedged OR 2.7-754; evidence vs none OR 2-46+; consistent vs contradictory OR 1.7-4.1; neutral vs promotional OR 1.3-362. | Vishwakarma 2026 [V] | Moderate-strong |
| 12 | **AI engines heavily favor earned (third-party) media over brand-owned pages.** | GPT cited 69-92% earned media across verticals vs Google ~32-54%; Claude 81.6-93.7% earned; big brands 62.2% of cola mentions vs niche 9.0%. | Chen et al. 2025 [V] | Moderate (observational, Aug-2025 snapshot) |
| 13 | **Own-domain retrieval is the gate for brand mention.** | Brand mention rate 2.8% (GPT) / 3.8% (Gemini) with no own-domain exposure vs 49-58% with own-domain citation vs 91-100% with own-domain + branded fan-out. | Tannenbaum 2026b [V] | Moderate (observational, predictive not causal) |
| 14 | **Recognition is not discovery**: LLMs know brands by name but rarely surface them for generic queries. | 99.4% name recognition vs 3.32% discovery (ChatGPT); Perplexity 94.3% vs 8.29%. GEO scores did **not** correlate with discovery; referring domains (r=+0.32) and Reddit presence (r=+0.40) did on Perplexity. | Sharma 2026 [V] | Moderate |
| 15 | **AI Overviews pick sources partly outside organic rankings.** | ~30% of AIO-cited domains absent from page-1 results; AIO-cited domains more credible than first-page results; AIO shown on 13.7% of trending queries but 64.7% of question-form queries. Grossman: AIO on 51.5% of real-user queries; Jaccard to SERP <0.2. Kirsten: 53% of AIO-cited domains outside organic top-10. | Xu et al. IMC 2026 [V]; Grossman et al. SIGIR 2026 [V]; Kirsten et al. ACL Findings 2026 [V-survey] | Strong (direction) |
| 16 | **Blocking Google's AI crawler reduces AIO retrieval.** | Sites blocking Google's AI crawler "significantly less likely" to be retrieved by AIOs. | Grossman et al. 2026 [V] | Moderate |
| 17 | **Engines barely agree with each other and are unstable over time** — single measurements are unreliable. | Cross-engine URL Jaccard 0.0079; 96.4% of URLs cited by only one engine; 67% day-to-day URL turnover. Schulte: daily Jaccard ~0.34-0.42, recommend 7-8 repetitions. Kirsten: 9-28% of decisions change on repeated temperature-0 runs. | Tannenbaum 2026a [V]; Schulte et al. 2026 [V-survey]; Kirsten [V-survey] | Strong |
| 18 | **Body-only rewriting can hurt upstream retrieval; structural fields (title, meta description, schema) help retrieval.** | SAGEO Arena: body-only optimization H@20 -9%, rerank H@10 -16%, citation -6%; structural-only H@20 +22%, citation +2%; AutoGEO body rewrite: retrieval -36%, citation -22%. | Kim et al. 2026 [V] | Moderate (one simulated pipeline, BM25-based) |
| 19 | **Learned / optimized rewriting beats fixed heuristics in controlled setups, and converges on "quality" features.** | AutoGEO-API +35.99% avg (up to +50.99%) over best GEO baseline; rules: cite credible sources, comprehensive, accurate/verifiable, neutral, logically organized, current, conclusion first, self-contained. E-GEO optimized prompts converge on intent alignment, structured sections/bullets, use cases, FAQ answers, no keyword stuffing, factuality. | Wu et al. ICLR 2026 [V]; Bagga et al. 2026 [V] | Moderate |
| 20 | **Gains are zero-sum and erode as adoption rises.** | C-SEO Bench: gains approach zero at 100% adoption; early adopters gain most. | Puerto et al. [V]; Hu 2025 (prisoner's dilemma) [V-survey] | Moderate |
| 21 | **Self-contained passages are retrieved/used better (extractability).** | HOPE: passage semantic independence gives up to +56.2% factual correctness, +21.1% answer correctness; concept unity has minimal impact. Dense X: proposition-level units beat passages under fixed budgets (largest gap at ~100-200 words). Tan et al.: retrieved segments that are cut mid-thought are under-used. | Brådland et al. 2025 [V]; Chen et al. EMNLP 2024 [V]; Tan et al. 2024 [V] | Moderate |
| 22 | **Adversarial manipulation works but is detectable/defendable; it's a reputational and policy risk.** | STS/CORE: CORE 80.3% Top-1 promotion success on 4 commercial APIs; Nestaas: fictitious camera recommendation 34.0% to 59.4%; PoisonedRAG: 5 texts = 90% ASR; GEO Defender cuts malicious-GEO ASR 50.3% to 6.2%. | Jin et al. 2026 [V]; Nestaas et al. ICLR 2025 [V-survey]; Zou et al. USENIX Sec 2025 [V]; Li et al. 2026 [V] | Strong (that it works in lab); risk of penalties is [I] |

**One-paragraph bottom line [I]:** The literature has moved from "a few rewrite tricks give +40%" (2023-24) to "being retrieved and being relevant dominate; content-level edits help only conditional on retrieval, are model-dependent, and erode under competition" (2025-26). The content features that survive replication are the ones that look like genuine quality: tight query/intent match, concrete verifiable facts (numbers, specs, prices, definitions, comparisons), completeness, freshness with visible dates, non-promotional confident tone, internal consistency, and self-contained, extractable passages. Third-party (earned) presence and retrievability (crawl access, classic SEO rank, titles/meta) gate everything else.

---

## 2. Paper-by-paper notes

### 2.1 Foundational GEO

#### Aggarwal et al. — "GEO: Generative Engine Optimization" (KDD 2024) [V]
- **Authors:** Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande (IIT Delhi, Princeton, independent).
- **Link:** https://arxiv.org/abs/2311.09735 (HTML: https://arxiv.org/html/2311.09735). Code: GEO-optim GitHub repo (linked from paper).
- **GEO-bench:** 10K queries (8K train / 1K val / 1K test) from 9 sources (MS MARCO, ORCAS-1, Natural Questions, AllSouls, LIMA, Davinci-Debate, Perplexity Discover, ELI5, GPT-4-generated); 25 domains, 9 query types, 7 tag categories; ~80% informational, 10% transactional, 10% navigational. Each query gets the cleaned text of the top-5 Google results.
- **Engine:** GPT-3.5-turbo, 5 samples at temperature 0.7, top-5 sources in context. Rewrites by GPT-3.5-turbo; one random source per query modified; 5 seeds.
- **Metrics:**
  - *Position-Adjusted Word Count (PAWC):* share of response words in sentences citing the source, weighted by e^(-pos/|S|) so earlier citations count more.
  - *Subjective Impression (SI):* 7 G-Eval-style sub-scores (relevance, influence, uniqueness, subjective position, subjective count, click likelihood, diversity) judged by GPT-3.5, normalized to PAWC scale.
- **Results (Table 1, test set; baseline PAWC 19.5, SI 19.3):**

| Method | PAWC | Δ PAWC | SI | Δ SI |
|---|---|---|---|---|
| Quotation Addition | 27.8 | +42.6% | 24.7 | +28.0% |
| Statistics Addition | 25.9 | +32.8% | 23.7 | +22.8% |
| Fluency Optimization | 25.1 | +28.7% | 21.9 | +13.5% |
| Cite Sources | 24.9 | +27.7% | 21.9 | +13.5% |
| Technical Terms | 23.1 | +18.5% | 21.4 | +10.9% |
| Easy-to-Understand | 22.2 | +13.8% | 20.5 | +6.2% |
| Authoritative | 21.8 | +11.8% | 22.9 | +18.7% |
| Unique Words | 20.7 | +6.2% | 20.4 | +5.7% |
| Keyword Stuffing | 17.8 | **-8.7%** | 20.2 | +4.7% |

  - Paper text reports best methods as +41% PAWC / +28% SI; headline "up to 40%". Fluency/readability changes alone gave "15-30%".
- **Perplexity.ai (200 queries; baseline PAWC 24.0, SI 24.7):** Quotation 29.1 PAWC (~+21%); Statistics SI 33.9 (~+37%); Cite Sources PAWC 26.6 but SI fell to 19.0; Keyword Stuffing PAWC 21.9 (~-9%).
- **Combinations:** Fluency + Statistics best pair, >5.5% better than any single method. Cite Sources averages +31.4% when combined with others.
- **By source rank (Table 2, relative visibility change):** Cite Sources rank-1 -30.3% / rank-5 +115.1%; Quotation -22.9% / +99.7%; Statistics -20.6% / +97.9%; Authoritative -6.0% / +6.1%; Fluency -2.0% / +2.2%.
- **Domain fit (Table 3):** Authoritative → Debate, History, Science; Fluency → Business, Science, Health; Cite Sources → Statement, Facts, Law & Government; Quotation → People & Society, Explanation, History; Statistics → Law & Government, Debate, Opinion.
- **Limitations (stated):** only 2 engines (one public); query drift; search-ranking effects not evaluated; GPT-4 tagging noisy; LLM-judged SI.
- **Limitations [I]:** the edited source is guaranteed to be in context (no retrieval stage); GPT-3.5 era; the "cite sources/quotes/stats" rewrites by an LLM may add fabricated content; PAWC rewards *length of cited sentences*, not traffic.

#### Chen, Wang, Chen, Koudas — "Generative Engine Optimization: How to Dominate AI Search" (arXiv 2509.08919, Sep 2025) [V]
- **Link:** https://arxiv.org/abs/2509.08919
- **Method:** Observational audit (Aug 2025) of ChatGPT/GPT, Claude, Gemini, Perplexity vs Google. 1,000 ranking-style prompts (10 categories x 100) in Canada and US; 100 queries x 5 languages; 100 queries x 7 paraphrases. Domains classified Brand (owned) / Earned / Social by GPT-4o.
- **Key numbers:**
  - GPT earned share: Automotive 69.1% (CA) / 81.9% (US); Electronics 77.6% / 92.1%; Software 74.2% / 72.7%. Google: 40.6-54.1% earned with 10-23% social.
  - Claude: 87.3% earned (well-known brands), 86.3% (niche), ~93.7% (consumer electronics), ~81.6% (automotive). Gemini 63-66% earned, 21-25% brand (most brand-leaning). Perplexity 53-73% earned, more social (15-24%).
  - Big-brand bias (cola): ChatGPT 56.3% major / 12.3% niche; Perplexity 67.9% / 5.8%.
  - Freshness (Claude): consumer electronics median cited-page age 62 days (mean ~117); automotive median 148 days (mean ~331). Perplexity "somewhat newer".
  - Domain overlap Google vs GPT: 15-33% at top-5; local services 0.1-20.6%.
  - Cross-language: GPT near-zero overlap between languages (switches ecosystems); Gemini/Claude more stable.
  - Paraphrase: AI engines 0.3-0.7 overlap across paraphrases.
- **Recommendations (not tested):** machine-scannable + justification content, dominate earned media, engine/language-specific strategies, overcome big-brand bias.
- **Limitations:** single snapshot; subjective taxonomy (authors say read relative trends, not absolute shares); no causal tests.

### 2.2 Replication / benchmark papers (the "does it actually work?" wave)

#### Puerto, Gubri, Green, Oh, Yun — "C-SEO Bench: Does Conversational SEO Work?" (NeurIPS 2025 D&B) [V]
- **Link:** https://arxiv.org/abs/2506.11097 (v3)
- **Design:** 6 domains — product recommendation (Retail 500 q, Games 436, Books 249) and QA (Web 300, News 294, Debate 142); ~1.9k queries, ~16k docs. Models: GPT-4o-mini, Claude 3.5 Haiku, o3, o4-mini. Metric: change in citation rank of the edited document. Tested 8 Aggarwal methods + "Content Improvement" (all combined) + "LLM Guidance" (llms.txt-style markdown summary prepended).
- **Key results (GPT-4o-mini, mean rank improvement):** LLM Guidance Retail +0.36, Games +0.24; Content Improvement Retail +0.18; most others within ±0.1; **Statistics -0.53 (Web), -0.80 (Debate)**. Only 3/54 cells significant (all positive cells in product rec). "Best SEO" (move to position 1): +2.77 Retail, +1.89 Games, +1.60 Books, +0.87 Web, +0.70 News, +1.54 Debate. Position 10: -0.78 to -1.02.
  - Haiku 3.5: no significant gains; 26/30 product-rec cells significantly *negative*. o4-mini: 19/30 QA cells significantly negative.
  - Multi-actor: gains shrink toward zero as adoption goes from 10% to 100%; LLM Guidance most robust.
- **Limitations:** white-hat only, proprietary models, English, no long docs, SEO-C-SEO interplay not studied.
- **Takeaway [I]:** the clearest causal evidence that retrieval position >> rewrite tricks; also the only academic test of an llms.txt-like summary (modest positive in product domains, within the context window — says nothing about whether engines fetch llms.txt files).

#### Bagga, Farias, Korkotashvili, Peng, Wu — "E-GEO: A Testbed for GEO in E-Commerce" (arXiv 2511.20867, v2 Jul 2026) [V]
- **Link:** https://arxiv.org/abs/2511.20867 ; code: github psbagga17/E-GEO
- **Design (v2):** 13,747 multi-sentence product queries x 10 Amazon listings; 5 re-rankers (GPT-5, Claude Sonnet 4.5, Gemini 3 Flash Preview, DeepSeek V3.2, Llama 4 Maverick); 7 rewriters; 15 heuristic prompts; prompt meta-optimization.
- **Heuristics (GPT-4.1 rewriter, avg rank change):** helped/neutral — "trick" +0.14, FAQ +0.05, competitive +0.03, format +0.02; hurt — advertisement -1.82, language -1.66, minimalist -1.49, authoritative -0.64, clickable -0.62, unique -0.27, fluent -0.19, diverse -0.19, technical -0.16, quality -0.13; storytelling (negative control) -4.36.
- **Meta-optimization:** improved 63 of 75 prompt x re-ranker cells; transfers to held-out Claude (13/15 improved). Optimized prompts converge on: explicit ranking goal, user-intent alignment, keyword/synonym integration (without stuffing), structured sections and bullets, use cases, FAQ-style answers, factuality clause.
- **Rewriter matters:** simple-prompt rewrites by Claude (+0.57) and GPT-5 (+0.56) helped; GPT-4o-mini (-0.36) hurt.
- **Red-teaming:** with an in-prompt "questionable content" clause, superlative/emotional attacks were flagged (100% → but optimized attacks drifted toward neutral, fact-grounded prose to evade). Authors conclude gains reflect real content improvement under the defense.
- **Takeaway [I]:** "Write like an ad" is strongly penalized by modern LLM rankers; FAQ/use-case/structure help a little; quality of the rewriting model matters.

#### Kim, Jeong, Kim, Lee, Lee — "SAGEO Arena" (arXiv 2602.12187, 2026) [V]
- **Link:** https://arxiv.org/abs/2602.12187
- **Design:** full pipeline (BM25 top-100 → Qwen3-Reranker-4B → GPT-5-mini generator on top-10) over 171,003 real web docs that keep structural info (title, meta description, schema/JSON-LD, headings); 2,700 queries, 9 domains. Robustness with dense/hybrid retrieval and Claude Sonnet 4.6.
- **Results (avg over 10 strategies):** body-only rewrites → retrieval H@20 -9%, rerank H@10 -16%, citation -6%. Structural-only → retrieval +22%, citation +2%. Both → retrieval +15%, citation -5%. AutoGEO body rewrite: retrieval -36%, citation -22%. Best structural-only strategies: Fluency +30% H@20, Statistics +29%, Cite Sources +28%, Quotation +27%. Their stage-aware method: citation 0.58 vs 0.50 baseline (+16%).
- **Caveats:** structural fields not ablated individually (schema not isolated); equal field weights; shopping domain all strategies reduced citation; visibility drops under query variation.
- **Takeaway [I]:** rewriting a page to "sound GEO-optimized" can dilute its lexical match and lose retrieval. Titles/meta/structured fields are a lower-risk lever.

#### Martinez — "Optimizing Visibility in Generative Engines: A Critical Survey of GEO (2023-2026)" (arXiv 2607.14035, Jul 2026) [V]
- **Link:** https://arxiv.org/abs/2607.14035
- Reviews 45 studies. Models GEO as a pipeline: activation → crawl/index → retrieval → rerank/context allocation → citation → prominence → absorption → fidelity → user behavior.
- **Robust (high confidence):** retrieval-conditional causal effects; relevance and context position dominate; engines differ and drift; retrieved content is an attack surface. **Moderate:** extractable evidence (figures, definitions, dated attributed evidence) and suitable structure; learned methods beat fixed heuristics.
- **Fail/do not generalize:** keyword stuffing; fixed heuristics across domains; authoritative tone and formatting alone; body-only rewrites (can hurt retrieval); the "40%" claim as a general promise.
- **Evidence grading A-E** (A = randomized field trials with logs; E = fixed contexts / LLM judges). Almost all GEO lab work is grade D-E.
- **Bottom line:** "No reviewed technique shows a stable, longitudinal, cross-platform causal effect on organic discoverability or downstream clicks and conversions."

#### Nimase, Chen, Qi, Zhao, Hu — "GEO-Bench: Benchmarking Ranking Manipulation in GEO" (arXiv 2605.29107, 2026) [V]
- Unified benchmark of 5 attacks (TAP, Zero-Shot, STS, RAF, StealthRank) + 10 white-hat C-SEO strategies on Llama-3.1-8B ranker; finds effectiveness-stealth trade-off; black-box rewriting matches or exceeds gradient attacks; most attacks detectable by at least one proxy. (Different from Aggarwal's GEO-bench.)

### 2.3 Learned / agentic optimization methods

#### Wu, Zhong, Kim, Xiong — "What Generative Search Engines Like and How to Optimize Web Content Cooperatively" (AutoGEO; ICLR 2026) [V]
- **Link:** https://arxiv.org/abs/2510.11438 ; code + rules: github cxcscmu/AutoGEO
- **Method:** LLMs explain why one doc beat another → extract → merge → filter into preference rules; AutoGEO-API (rules as prompt) and AutoGEO-Mini (Qwen3-1.7B trained with RL on rule-based rewards; ~0.7% of API cost).
- **Benchmarks:** GEO-Bench, Researchy-GEO (10k/1k), E-commerce (LMSYS commercial queries, 1,667/416); 5 ClueWeb22 docs per query. Engines: gemini-2.5-flash-lite, gpt-4o-mini, claude-3-haiku.
- **Results:** AutoGEO-API +35.99% average over best baseline (Fluency), up to +50.99%; AutoGEO-Mini +20.99%. Overall score e.g. Researchy-GEO (Gemini) 20.18 → 43.76 (API) / 38.53 (Mini). Utility (faithfulness, relevance, clarity) preserved; attack baselines raised visibility but lowered utility.
- **Learned rules (Gemini, Researchy-GEO; paraphrased):** cite credible sources for factual claims; comprehensive coverage; accurate, verifiable info; neutral tone; logical organization; clear language; current information; concise; balanced views; explain causes/mechanisms; **state the main conclusion first**; stay on topic; back claims with specific data/examples; **make the document self-contained**. E-commerce adds: actionable step-by-step guidance; concrete product details (model numbers, specs).
- **Rule overlap:** across engines 79-84% (Jaccard); across informational datasets 88%; informational vs e-commerce only 35-40% → rules are **query-type-specific more than engine-specific**.
- **Caveat:** SAGEO Arena found AutoGEO-style body rewriting cuts retrieval 36% in a full pipeline.

#### Other method papers (2025-2026)
- **RAID G-SEO** — Chen et al., "Role-Augmented Intent-Driven Generative Search Engine Optimization" (arXiv 2508.11158) [V abstract]: 4-step pipeline (summarize, infer and refine latent intent via multi-role "4W" reflection, plan, rewrite); G-Eval 2.0 6-level rubric; reports gains over single-aspect baselines (no public code at time of check). https://arxiv.org/abs/2508.11158
- **IF-GEO** — Zhou et al. (Findings ACL 2026; arXiv 2601.13938) [V abstract]: one document must serve many queries; mines per-query revision preferences and fuses them with conflict-aware "Global Revision Blueprint"; adds risk-aware stability metrics. https://arxiv.org/abs/2601.13938
- **Mind Reader** — Chen et al. (ACL 2026 long, pp. 40832-40848) [V abstract]: decompose/recombine queries to infer latent user demands; optimize content for "reasoning coverage". Survey notes gains are largely LLM-generated and LLM-evaluated. https://aclanthology.org/2026.acl-long.1894/
- **AgenticGEO** — Yuan et al. (arXiv 2603.20213) [V abstract]: MAP-Elites archive of strategies + co-evolving critic; beats 14 baselines on 3 datasets, 2 engines. https://arxiv.org/abs/2603.20213
- **AgentGEO / citation-failure repair** — Tian et al. (arXiv 2603.09296) [V abstract]: taxonomy of why a document is *not* cited across pipeline stages; targeted repairs; >40% relative citation-rate improvement while modifying ~5% of text (vs 25% for baselines); generic optimization can hurt long-tail content. https://arxiv.org/abs/2603.09296
- **Beyond the Vacuum** — Sourirajan et al. (arXiv 2608.27631) [V abstract]: competitor-aware strategy selection via Bayesian optimization over strategy combinations; argues best strategy depends on what competitors already do. https://arxiv.org/abs/2608.27631
- **GEO-SFE (structural feature engineering)** — Yu et al. (arXiv 2603.29979) [V abstract]: three structure levels (document architecture, information chunking, visual emphasis); +17.3% citation rate, +18.5% subjective quality across 6 engines (no per-element breakdown; survey: "limited validation"). https://arxiv.org/abs/2603.29979
- **CC-GSEO-Bench** — Chen et al. (arXiv 2509.05607) [V]: 1,000+ articles, 5,000+ query-article pairs; scores Exposure, Faithful Credit, Causal Impact + Readability/Structure, Trustworthiness/Safety. Useful *metric design* reference. https://arxiv.org/abs/2509.05607
- **Beyond SEO (BART fine-tune)** — Lüttgenau et al. (arXiv 2507.03169) [V]: travel content; +15.63% word count, +30.96% PAWC with Llama-3.3-70B. Small, synthetic. https://arxiv.org/abs/2507.03169
- **Rewrite-to-Rank** — Ho et al. (ICML 2025 workshop; arXiv 2507.21099) [V]: ad rewriting; best ΔMRR@5 only 0.0073 → tiny absolute gains. https://arxiv.org/abs/2507.21099
- **Pinterest GEO** — Zhang et al. (arXiv 2602.02961) [V via search abstract]: VLMs predict queries users would type for images → generate interlinked collection pages; ~20% organic traffic lift in production (survey: design under-described). Notable as one of very few production results. https://arxiv.org/abs/2602.02961
- **Multi-agent GEO via reusable strategy learning** — arXiv 2604.19516 (not read in depth). https://arxiv.org/abs/2604.19516

### 2.4 Controlled factor studies

#### Vishwakarma, Kumar, Jamidar — "What Gets Cited: Competitive GEO in AI Answer Engines" (SIGIR 2026; arXiv 2605.25517) [V]
- **Link:** https://arxiv.org/abs/2605.25517
- **Design:** 252,000 paired trials; 2 sources injected in context; 6 LLMs (Gemini 2.5 Flash, Claude 3.5 Sonnet, Kimi K2 Thinking, GPT-5 Nano, GPT-5 Mini, GPT-5.2); 18 single-factor manipulations; source order counterbalanced; outcome = which source gets first citation. Corpus: 100 anonymized B2C product-review blogs (GPT-4o generated).
- **Odds ratios (A beats B; range across 6 models):**
  - Gatekeepers: on-topic (221 to >>10k); position 1 vs 2 (1,795 to >>10k); recent vs old timestamp (14 to >>10k); price present (6 to >>10k); query terms present (6-40).
  - Strong/moderate: specs (8.6 to >>10k); deep vs shallow (4 to >>10k); evidence (2-46+, >>10k Claude); social proof (2-25, >>10k Claude); confident vs hedged (2.7-754); strong value prop (1.5-7); comparisons (1.6-7.5); consistent vs contradictory (1.7-4.1); neutral vs promotional (1.3-362).
  - Weak/null: organized vs scattered (1.1-3.9); **structured vs dense (0.78-1.68, mostly n.s.)**; no timestamp vs old timestamp (1.3-2.3, i.e., an old date is worse than no date); recent vs no timestamp (1.15-13).
- **Checklist (authors):** fix gatekeepers (topical match, prices, recent dates, retrieval rank) → editorial quick wins → differentiators (spec tables, comparisons, value prop, social proof, evidence, remove contradictions, reduce promotional tone) → deprioritize formatting.
- **Limitations:** 2-doc pairwise; anonymized (no brand trust); synthetic content; first citation only; B2C product reviews only; some ORs quasi-separated; author affiliation with a vendor (Sprinklr).

#### Wan, Wallace, Klein — "What Evidence Do Language Models Find Convincing?" (ACL 2024) [V]
- **Link:** https://arxiv.org/abs/2402.11782
- ConflictingQA: 238 contested questions, 2,208 paragraphs; models LLaMA-2, Vicuna, WizardLM, GPT-4, Claude Instant.
- Models "overindex on relevancy": relevance edits (question prefix, rewrite for relevance, even keyword stuffing) raised win-rate; stylistic credibility edits (adding scientific references, objective tone) were neutral-to-negative. Exact win-rates only in figures.
- **Takeaway [I]:** Credibility signals humans value are not what the model reads; topical alignment is. Note: keyword stuffing *raised* persuasiveness here (pairwise, in-context) but *lowered* visibility in Aggarwal et al. — the measures differ.

#### Fang et al. — "Do Large Language Models Favor Recent Content? A Study on Recency Bias in LLM-Based Reranking" (arXiv 2509.11353, 2025) [V via search summary]
- Injected artificial publication dates on TREC DL21/22 passages; 7 LLMs. All models promoted "fresh" passages; top-10 mean publication year shifted up to 4.78 years; individual items moved up to 95 ranks; up to 25% of equal-relevance pairwise preferences reversed. Bigger models attenuate but do not eliminate. https://arxiv.org/abs/2509.11353

### 2.5 Observational audits of live engines

#### Zhang, He, Yao — "From Citation Selection to Citation Absorption" (arXiv 2604.25707, 2026) [V]
- **Link:** https://arxiv.org/abs/2604.25707
- 602 controlled prompts on ChatGPT, Google AIO/Gemini, Perplexity; 21,143 citations; 18,151 fetched pages; 72 features. Defines *selection* (cited?) vs *absorption* (did the page's words/facts end up in the answer?).
- Mean citations per answer: ChatGPT 6.88, Google AIO 12.06, Perplexity 16.35. ChatGPT cites fewer but each citation is used far more (mean influence 0.27 vs 0.06).
- Feature/influence associations: code +76.9%, numbers/statistics +61.6%, definitions +57.3%, comparisons +55.3%, how-to +41.2%, Q&A format **-5.7%**. Top vs bottom quartile: words 1,943 vs 170; headings 10.6 vs 0.85; list density 0.43 vs 0.05. Correlations: LLM relevance r=0.43, answer-page embedding similarity r=0.36, LLM quality r=0.29.
- Domain type influence: encyclopedia 0.214 highest; commercial 0.103; government 0.077; news 0.073.
- **Limitations:** descriptive only, no causal claims; composite influence score; designed prompt set.

#### Xu, Iqbal, Montgomery — "Measuring Google AI Overviews" (IMC 2026; arXiv 2605.14021) [V]
- 55,393 trending queries, 19 categories, 40 days (spring 2026). AIO activation 13.7% overall, 64.7% for question-form queries; lower for politically sensitive topics. Nearly 30% of cited domains not in page-1 results; cited domains more credible than page-1 results. 11.0% of 98,020 atomic claims unsupported by cited pages (omission most common). Well over half of cited pages carried display ads. https://arxiv.org/abs/2605.14021

#### Grossman et al. — "How Generative AI Disrupts Search: Google Search, Gemini, and AI Overviews" (SIGIR 2026; arXiv 2604.27790) [V]
- 11,500 real-user queries; AIO on 51.5%; cross-engine source Jaccard <0.2 (secondary report: 0.17, ~18% shared); traditional Search favours gov/edu/institutional, generative engines more likely to retrieve Google-owned content; **sites blocking Google's AI crawler significantly less likely to be retrieved by AIO**; AIO less consistent across repeated runs and minor edits. https://arxiv.org/abs/2604.27790

#### Kirsten et al. — "Characterizing Web Search in the Age of Generative AI" (Findings ACL 2026) [V-survey]
- 4,706 queries; AIO page overlap with organic 18% (vs 45% baseline comparison per survey); 9-28% of decisions change on repeated temperature-0 runs; 53% of AIO-cited domains outside organic top-10.

#### Tannenbaum — "Scoring With the Engine: Retrieval Exposure, Cross-Engine Divergence, and the Limits of Engine-Agnostic GEO Scores" (arXiv 2609.22655, Sep 2026) [V]
- 15 commercial prompts; ChatGPT, Copilot, Google, Perplexity; 589 citations. Mean pairwise URL Jaccard 0.0079 (5.7% of chance expectation); 84.9% of engine pairs share zero URLs; 96.4% of URLs in one engine only; 67% day-over-day turnover. **Argues engine-free page scores measure "page quality or query-page fit" only; recommends reporting page fit, exposure, conditional selection, and final visibility separately.** Directly relevant to any GEO scoring rubric. https://arxiv.org/abs/2609.22655

#### Tannenbaum — "From Prompt to Recommendation: A Fitted Stage Model of Brand Visibility in AI Search" (arXiv 2609.23162) [V]
- 34,960 prompt-engine observations, 75 projects, Jun-Sep 2026, GPT and Gemini. Mention rate 2.8%/3.8% without own-domain exposure; 49.0%/58.4% with own-domain citation; 91.4%/100% with own-domain + branded fan-out query. Prior mention strongly predicts next mention (persistence). Prompt-page match predicts Gemini exposure better (AUC 0.64) than GPT (0.55). https://arxiv.org/abs/2609.23162

#### Zhen et al. — "What Do Chinese-Language Generative Search Engines Cite and Surface?" (arXiv 2607.15771) [V]
- 614 queries, 8 interfaces, 160,860 citation records. Only 8.3% of brands in the citation pool surfaced in answers; top predictors = content fit, **cross-source occurrence count** (being mentioned on many sources), semantic role; a commercial SEO quality score was not a leading predictor. Freshness half-life ~39 days (high-timeliness) / ~68 days (low). App vs Web interfaces cite different sources. https://arxiv.org/abs/2607.15771

#### Sharma — "The Discovery Gap" (arXiv 2601.00912) [V]
- 112 Product Hunt startups, 2,240 queries. Recognition 99.4% vs discovery 3.32% (ChatGPT gpt-4o-mini); Perplexity 94.3% vs 8.29%. GEO scores did not correlate with discovery; on Perplexity referring domains r=+0.319, Reddit presence r=+0.395. https://arxiv.org/abs/2601.00912

#### Watanabe & Nakayashiki — "Disentangling AEO from Platform Growth" (arXiv 2606.04362) [V]
- One domain, hundreds of thousands of Q&A pages treated Jan 2026. Raw ChatGPT referrals x5.7, but untreated pages x3.5; ITS estimate x1.82 (95% CI 1.31-2.54); placebo-in-time p=0.16 → "suggestive, not conclusive". Google organic not harmed. The closest thing to a quasi-experimental field test of AEO. https://arxiv.org/abs/2606.04362

#### Allaham & Diakopoulos — "Synthetic Sources?" (AIES 2026; arXiv 2605.23684) [V]
- 712 real queries (politics, health, environment), 4 engines; ~16% of cited sources were AI-generated; engines cite a narrow set of domains repeatedly. https://arxiv.org/abs/2605.23684

#### Schulte, Bleeker, Kaufmann — "Don't Measure Once: Measuring Visibility in AI Search" (arXiv 2604.07585) [V abstract; numbers V-survey]
- Visibility is a distribution; daily Jaccard ~0.34-0.42; suggests 7-8 repetitions; 57.8% of ChatGPT repetitions triggered no web search. https://arxiv.org/abs/2604.07585

#### Sielinski — "From Stochastic to Stable: Rank Stability and Structural Sufficiency in AI Visibility Measurement" (arXiv 2607.10341) [V]
- Sequential stopping rule for citation-share measurement across 30 platform-topic combos (Gemini, SearchGPT, Perplexity); no single fixed query budget is justified. https://arxiv.org/abs/2607.10341

#### Earlier audits
- **Liu, Zhang, Liang — "Evaluating Verifiability in Generative Search Engines"** (Findings EMNLP 2023) [V]: Bing Chat, NeevaAI, Perplexity, YouChat; only 51.5% of sentences fully supported by citations; 74.5% citation precision; fluent answers mask unsupported claims (paper also reports citation quality inversely correlated with perceived fluency/utility). https://arxiv.org/abs/2304.09848
- **Li & Sinnamon — "Generative AI Search Engines as Arbiters of Public Knowledge"** (2024) [V abstract]: 48 queries x 4 topics x 7 days (June 2023) on ChatGPT, Bing Chat, Perplexity; commercial and geographic source bias; heavy reliance on news/media, business, digital media sites. https://arxiv.org/abs/2405.14034
- **Narayanan Venkit et al. — "Search Engines in an AI Era: The False Promise of Factual and Verifiable Source-Cited Responses"** (FAccT 2025) [V abstract]: 21-participant usability study; 16 findings, 16 design recommendations. https://arxiv.org/abs/2410.22349
- **Vykopal et al. — "Assessing web search credibility and response groundedness in chat assistants"** (EACL 2026) [V-survey]: credible-source shares 71.4-86.3%.

### 2.6 Manipulation, ranking attacks, and RAG poisoning

- **Kumar & Lakkaraju — "Manipulating Large Language Models to Increase Product Visibility"** (arXiv 2404.07981) [V]: GCG-optimized "strategic text sequence" (STS) in a product's JSON entry; Llama-2; fictitious catalog of 10 coffee machines. A $199 product "almost never" recommended became top recommendation within ~100 iterations; with random product order and order-robust optimization, advantage rose and disadvantage became negligible (exact rates only in figures). Code: github aounon/llm-rank-optimizer. https://arxiv.org/abs/2404.07981
- **Pfrommer et al. — "Ranking Manipulation for Conversational Search Engines"** (EMNLP 2024) [V abstract; number V-survey]: LLMs weigh product name, document content, and context position differently; tree-of-attacks prompt injections promote low-ranked products and transfer to Perplexity (~3 rank gain). https://arxiv.org/abs/2406.03589
- **Nestaas, Debenedetti, Tramèr — "Adversarial Search Engine Optimization for LLMs"** (ICLR 2025) [V abstract; numbers V-survey]: "Preference Manipulation Attacks" on Bing Copilot, Perplexity, GPT-4/Claude plugins; fictitious camera recommendation 34.0% → 59.4%; plugin selection up to 7.2x; prisoner's-dilemma dynamics. https://arxiv.org/abs/2406.18382
- **Jin et al. — "CORE: Controlling Output Rankings in Generative Engines"** (arXiv 2602.03608) [V via search]: appends string-, reasoning-, or review-based optimization content; ProductBench 15 categories x 200 products; GPT-4o, Gemini-2.5, Claude-4, Grok-3 APIs; promotion success 91.4% Top-5, 86.6% Top-3, 80.3% Top-1. Finds LLM recommendations largely follow initial search order. https://arxiv.org/abs/2602.03608
- **StealthRank** (Tang et al. 2025, workshop) and **Xing et al. 2026 "Are LLMs reliable rankers?"** (ACL 2026) [V-survey]: rank-fluency trade-offs; short suffixes promote targets.
- **Zou et al. — "PoisonedRAG"** (USENIX Security 2025) [V]: 5 malicious texts per target question in a database of millions → 90% attack success. https://arxiv.org/abs/2402.07867
- **Li et al. — "When Optimization Becomes Manipulation: Defending Generative Search against Malicious GEO"** (arXiv 2609.02964, Sep 2026) [V]: GEO Defender (Shield Reranker + training-free shield generation) lowers attack success 50.32% → 6.20% across 7 GEO attacks and 5 LLMs, retaining 94.12% of benign evidence use; generalizes to unseen attacks. **Implication [I]: engines are actively building demotion of "GEO-rewritten" documents.** https://arxiv.org/abs/2609.02964
- **GRADA** (Zheng et al. 2025) [V-survey]: defense reducing attack success up to ~80%.
- **Hu 2025** (arXiv 2501.00745) [V-survey]: models GEO attack choice as an infinitely repeated prisoner's dilemma.

### 2.7 LLM source-preference biases

- **Dai et al. — "Neural Retrievers are Biased Towards LLM-Generated Content"** (KDD 2024) [V via search]: "source bias" — neural retrievers and rerankers rank LLM-generated text higher than equivalent human text; linked to lower perplexity / more focused semantics; BM25 tends the other way. Challenged by Xion & Nejdl 2026 (arXiv 2602.10833): bias is training-induced, dataset-dependent, not inherent. https://arxiv.org/abs/2310.20501
- **Laurito et al. — "AI-AI Bias"** (PNAS 2025) [V abstract]: GPT-3.5, GPT-4 and open models consistently prefer items (products, papers, films) described by LLMs over human-written descriptions. https://arxiv.org/abs/2407.12856
- **Ma, Qin, Xu, Tan — "When Content is Goliath and Algorithm is David"** (arXiv 2509.14436) [V]: ~10k sites from Google generative vs conventional search; generative engines prefer citing content with higher LLM predictability (lower perplexity) and higher semantic similarity among selected sources; LLM polishing of sites increased diversity of AI summaries. https://arxiv.org/abs/2509.14436
- **Tan et al. — "Blinded by Generated Contexts"** (ACL 2024) [V via search]: LLMs favour generated contexts over retrieved ones even when wrong; causes: higher query similarity and the incompleteness of segmented retrieved passages. https://arxiv.org/abs/2401.11911
- **Kamruzzaman, Nguyen, Kim — "Global is Good, Local is Bad?: Understanding Brand Bias in LLMs"** (EMNLP 2024) [V via search]: LLMs associate global brands with positive attributes; country-of-origin effects; GPT-4o largest effect sizes. https://arxiv.org/abs/2406.13997
- **Liu et al. — "Lost in the Middle"** (TACL 2024) [V]: GPT-3.5-Turbo, 20 docs: 75.8% accuracy when answer doc is first, 53.8% when 10th (below 56.1% closed-book), 63.2% when last. U-shaped position bias. https://arxiv.org/abs/2307.03172

### 2.8 Chunking, granularity, and extractability

- **Chen et al. — "Dense X Retrieval: What Retrieval Granularity Should We Use?"** (EMNLP 2024) [V via search]: proposition-level indexing (atomic, self-contained factual statements) beats sentence/passage for dense retrieval and downstream QA under fixed budgets; largest gap at ~100-200 retrieved words. https://arxiv.org/abs/2312.06648
- **Brådland et al. — "A New HOPE: Domain-agnostic Automatic Evaluation of Text Chunking"** (arXiv 2505.02171) [V]: across 7 domains, passage semantic independence gives up to +56.2% factual correctness and +21.1% answer correctness; keeping a concept unified within one passage had minimal impact. https://arxiv.org/abs/2505.02171
- **Merola & Singh** (arXiv 2504.19754) and **Kreileder et al.** (arXiv 2607.01852) [V via search]: no chunking method dominates; contextual retrieval keeps coherence at higher cost; semantic chunking did not beat simple strategies on theses.
- **Implication [I]:** you cannot control how an engine chunks your page, so write sections that stand alone (restate the subject/entity, avoid "as mentioned above", put the answer in the first sentence under each heading, keep key facts within ~100-200 words of their context).

---

## 3. Evidence table: tactic → measured effect → confidence → sources

| Tactic / factor | Measured effect | Confidence | Sources |
|---|---|---|---|
| **Query/intent relevance (topical match, query terms present)** | OR >>10k on-topic; query terms OR 6-40; relevance edits raise LLM "win rate"; r=0.43 with absorption | **Strong** | Vishwakarma 2026; Wan 2024; Zhang 2026; Martinez 2026 |
| **Being retrieved / high retrieval rank (classic SEO)** | Position 1 = +2.77 rank vs +0.36 best content tactic; OR >1,795; 75.8% vs 53.8% accuracy by position; own-domain exposure +40-49 pp mention rate | **Strong** | Puerto 2025; Vishwakarma 2026; Liu 2024; Tannenbaum 2026b; Sharma 2026 |
| **Allow AI crawlers** | Blocking Google's AI crawler → significantly less AIO retrieval | Moderate | Grossman 2026 |
| **Freshness / recent visible date** | OR 14 to >>10k (recent vs old); up to 25% pairwise preference reversal from date alone; half-life 39-68 days; old date worse than no date (OR 1.3-2.3) | **Strong** | Vishwakarma 2026; Fang 2025; Zhen 2026; Chen 2025 |
| **Statistics / numbers** | +32.8% PAWC (GPT-3.5); +61.6% absorption (correlational); **but** -0.53 to -0.80 rank in C-SEO QA, negative in 19/24 settings | **Contested** (helps when numbers are real and relevant; LLM-injected stats can hurt) | Aggarwal 2024; Zhang 2026; Puerto 2025; SAGEO (+7% citation, structural) |
| **Quotations from experts** | +42.6% PAWC; ~+21% on Perplexity; C-SEO ~0 to -0.19 | **Contested** | Aggarwal 2024; Puerto 2025 |
| **Cite sources / references** | +27.7% PAWC; C-SEO ~0; Wan: adding scientific references neutral-negative; AutoGEO rule "cite credible sources" | **Contested / moderate** | Aggarwal; Puerto; Wan; Wu 2026 |
| **Concrete specs, prices, model numbers** | Specs OR 8.6 to >>10k; price OR 6 to >>10k; AutoGEO e-commerce rule | **Strong** (product content) | Vishwakarma 2026; Wu 2026 |
| **Definitions, comparisons, how-to steps** | +55-57% (definitions, comparisons) / +41% (how-to) absorption; comparisons OR 1.6-7.5 | Moderate | Zhang 2026; Vishwakarma 2026 |
| **Depth / comprehensiveness / length** | Deep vs shallow OR 4 to >>10k; top-influence pages ~11x longer | Moderate-strong (length is a proxy for coverage, not causal by itself) | Vishwakarma; Zhang; AutoGEO rules |
| **Evidence-backed, confident (not hedged) claims** | Evidence OR 2-46+; confident OR 2.7-754 | Moderate-strong | Vishwakarma 2026 |
| **Internal consistency (no contradictions)** | OR 1.7-4.1 | Moderate | Vishwakarma 2026 |
| **Neutral, non-promotional tone** | Neutral vs promotional OR 1.3-362; "advertisement" rewrite -1.82, storytelling -4.36 | **Strong** (that promo hurts) | Vishwakarma; E-GEO |
| **"Authoritative" tone rewrite** | +11.8% PAWC (GPT-3.5); -0.64 (E-GEO); ~0 (C-SEO) | **Contested / weak** | Aggarwal; E-GEO; Puerto |
| **Fluency / readability / easy-to-understand** | +13.8 to +28.7% PAWC; fluency +0.32 Debate (C-SEO) but ~0 elsewhere; "fluent" -0.19 E-GEO; SAGEO structural fluency +30% retrieval | Weak-moderate (baseline hygiene, not a differentiator) | Aggarwal; Puerto; E-GEO; Kim 2026 |
| **Technical terms / unique words** | +18.5% / +6.2% PAWC; ~0 or negative elsewhere | Weak | Aggarwal; Puerto; E-GEO |
| **Structure: headings, lists, sections** | Correlational: top-influence pages 12.5x more headings, 9x list density; GEO-SFE +17.3% citation; **causal pairwise: structured vs dense OR ~1 (n.s.)** | **Contested** (likely helps extraction/coverage, little effect when content held constant) | Zhang 2026; Yu 2026; Vishwakarma 2026; E-GEO "format" +0.02 |
| **Answer-first / conclusion first** | AutoGEO learned rule; supported indirectly by position-weighted metrics | Moderate (learned rule, not isolated) | Wu 2026 |
| **Self-contained passages** | +56.2% factual correctness (passage independence); AutoGEO rule "self-contained"; segmented passages under-used | Moderate | Brådland 2025; Wu 2026; Tan 2024 |
| **FAQ / Q&A format** | E-GEO FAQ +0.05 and emerges in optimized prompts; Zhang: Q&A format -5.7% absorption | **Weak / contested** | Bagga 2026; Zhang 2026 |
| **Schema / structured data (JSON-LD)** | SAGEO: structural fields together (incl. schema) +22% retrieval, +2% citation; not isolated. No academic study isolates schema's effect on LLM citation (industry tests mostly null) | **Weak / unproven** | Kim 2026; (industry: not in this slice) |
| **llms.txt-style summary in document** | LLM Guidance +0.36 Retail, +0.24 Games (significant), ~0 in QA | Weak-moderate (in-context only) | Puerto 2025 |
| **Social proof / reviews** | OR 2-25 (>>10k Claude) | Moderate | Vishwakarma 2026 |
| **Earned media / third-party mentions** | 69-94% of AI citations are earned media; cross-source occurrence a top predictor; referring domains & Reddit correlate with discovery | Moderate-strong (observational) | Chen 2025; Zhen 2026; Sharma 2026 |
| **Brand size / global brands** | Major brands 62% vs niche 9% of mentions; global-brand positivity bias | Moderate | Chen 2025; Kamruzzaman 2024 |
| **LLM-like writing style (low perplexity)** | Neural retrievers & generative engines prefer LLM-predictable text; LLM agents prefer LLM-written descriptions | Moderate (mechanism contested) | Dai 2024; Ma 2025; Laurito 2025; Xion & Nejdl 2026 |
| **Keyword stuffing** | -8.7% PAWC; ~-10% Perplexity; null/negative across benchmarks | **Strong (doesn't work)** | Aggarwal; Martinez |
| **Body-only LLM rewriting for GEO** | -9% retrieval, -6% citation; AutoGEO body: -36% retrieval | Moderate (harmful) | Kim 2026 |
| **Learned/optimized rewriting** | +21-51% in fixed-context benchmarks | Moderate (lab only) | Wu 2026; Bagga 2026; Tian 2026 |
| **Adversarial text sequences / injections** | 80-91% promotion success (CORE); 34→59% recommendation (Nestaas) | Strong in lab; **harmful** (detectable, defended) | Kumar 2024; Jin 2026; Nestaas 2025; Li 2026 |

---

## 4. What does NOT work, is contested, or is harmful

1. **Keyword stuffing** — the one tactic negative even in the original GEO paper (-8.7% PAWC; ~-10% on Perplexity). Survey: null or negative across all benchmarks. (Nuance: Wan et al. found query-term insertion increases *persuasiveness* in a pairwise in-context test — relevance helps, stuffing beyond natural relevance does not.)
2. **The "+40% visibility" headline as a general promise** — it is a relative maximum on one metric (PAWC), one engine (GPT-3.5), with the source guaranteed in context. C-SEO Bench (newer models) found 51 of 54 method-domain cells non-significant or negative.
3. **Mechanically "adding statistics"** — negative in 19/24 C-SEO settings, likely because LLM-inserted numbers are generic, off-topic, or unverifiable. Real, relevant numbers correlate with absorption (Zhang et al.). [I] The distinction is *genuine data* vs *decorative data*.
4. **"Authoritative" or persuasive tone rewrites** — +11.8% on GPT-3.5, -0.64 in E-GEO, ~0 in C-SEO. Wan et al.: models ignore credibility style cues.
5. **Promotional / ad-copy / storytelling style** — strongly penalized: E-GEO advertisement -1.82, storytelling -4.36; promotional vs neutral OR up to 362 against.
6. **Formatting-only changes** — Vishwakarma: negligible. Correlational studies showing structured pages cited more do not separate structure from depth. [I] Treat structure as an enabler of extractability and coverage, not as a standalone lever.
7. **Body-only LLM rewrites of existing pages** — SAGEO Arena: can reduce retrieval (-9% avg, -36% for AutoGEO) and final citation (-6% to -22%). Preserve the page's lexical match to target queries when editing.
8. **Fixed one-size-fits-all heuristics** — rule overlap across query types only 35-40% (AutoGEO); best strategy depends on competitors (Beyond the Vacuum); generic optimization can hurt long-tail docs (Tian et al.).
9. **Zero-sum erosion** — gains shrink toward zero as more competitors adopt the same tactic (C-SEO Bench).
10. **Adversarial manipulation (STS, CORE, prompt injection, preference manipulation, RAG poisoning)** — works in lab conditions, but: (a) detectable by proxies (GEO-Bench 2026), (b) dedicated defenses cut success from ~50% to ~6% (GEO Defender), (c) E-GEO's in-prompt defense flags superlatives/emotional manipulation at up to 100%, (d) collective prisoner's-dilemma degradation. [I] For a reputable brand this is a reputational, legal, and platform-policy risk, and should score as a hard negative in any rubric.
11. **Schema markup as a citation lever** — no academic study isolates it; SAGEO only tests structural fields bundled together. Unproven, not disproven.
12. **Single-run measurement** — 67% day-to-day URL turnover, 9-28% decision flips at temperature 0, cross-engine overlap ~1%. Any "before/after" GEO claim from single runs is unreliable; use 7+ repetitions.
13. **Assuming engine-agnostic content scores predict visibility** — Tannenbaum 2026 and Sharma 2026 (GEO scores did not correlate with discovery) show page-level scores capture only page fit, not exposure.

---

## 5. Implications for a content GEO scoring rubric

**Framing principle [I, grounded in Tannenbaum 2026a and Martinez 2026]:** A page-level rubric can only measure *page fit and extractability* — the conditional probability of being selected and absorbed **given** retrieval. It cannot measure exposure. Be explicit in the rubric that it is a necessary-not-sufficient score, and pair it with (a) retrievability checks and (b) repeated live-engine measurement.

### Suggested weighting (relative importance, based on strength and consistency of evidence)

| Rubric dimension | Suggested weight | Why (evidence) |
|---|---|---|
| **1. Query/intent fit** — the page directly answers the target questions; key query terms and synonyms used naturally; covers the sub-questions a fan-out would generate | **Very high (~20-25%)** | Strongest factor in every causal study (Wan; Vishwakarma OR >>10k; C-SEO; Zhang r=0.43; Zhen "content fit"). Mind Reader / IF-GEO / RAID: latent intent & multi-query coverage drive gains. |
| **2. Concrete, verifiable facts** — specs, numbers with units, prices/ratings where relevant, standards references, definitions, comparisons, procedures; facts sourced and dated | **High (~15-20%)** | Specs/price ORs very large; definitions/comparisons/numbers +55-62% absorption; AutoGEO rule "specific data/examples". Penalize generic or unsupported numbers (C-SEO negative stats result). |
| **3. Completeness / depth** — covers the topic end-to-end (mechanisms, use cases, limits, alternatives) | **High (~10-15%)** | Deep vs shallow OR 4 to >>10k; top-influence pages far longer with more sections; AutoGEO "comprehensive". Measure coverage, not raw word count. |
| **4. Extractability** — answer-first paragraphs; each section self-contained (restates entity); one idea per passage; descriptive headings; lists/tables for specs and steps | **Medium-high (~10-15%)** | HOPE +56% factual correctness from passage independence; Dense X propositions; AutoGEO "conclusion first", "self-contained"; correlational heading/list density. Weight on *self-containment*, not on formatting per se (formatting alone ~null). |
| **5. Freshness signals** — visible, accurate "last updated" date; current figures/versions; no stale dates | **Medium-high (~10%)** | Recent timestamp OR 14 to >>10k; recency bias in all LLM rerankers; half-life 39-68 days. Old visible date is worse than no date — only show dates you maintain. |
| **6. Tone & integrity** — neutral, non-promotional, confident (not hedged) where evidence supports, no internal contradictions, balanced (mentions trade-offs/alternatives) | **Medium (~10%)** | Promotional penalty (E-GEO -1.82; OR up to 362); confident OR up to 754; consistency OR 1.7-4.1; AutoGEO "neutral", "balanced". Hard penalty for superlatives and ad-speak. |
| **7. Trust / evidence cues** — citations to credible primary sources, named expert quotes, certifications, social proof, author/organization identity | **Medium-low (~5-10%)** | Mixed: big gains on GPT-3.5 (Aggarwal), null on newer models (C-SEO), style cues ignored (Wan), but evidence and social proof matter pairwise (Vishwakarma) and AutoGEO keeps "cite credible sources". Score substance (is the claim actually backed?) over decoration. |
| **8. Retrievability hygiene (page-level)** — descriptive title & meta description aligned to queries, structured data present and consistent with visible text, crawlable by AI crawlers, fast/clean HTML | **Medium (~5-10%), or a gate** | SAGEO structural fields +22% retrieval; Grossman: blocking AI crawler cuts AIO retrieval; position/retrieval dominates. Treat crawler blocking as a hard fail. Schema: include for consistency, don't over-weight. |
| **9. Readability / fluency** | **Low (~5%)** | +14-29% on GPT-3.5 only; null or slightly negative on newer models. Hygiene factor. |
| **Negative modifiers (penalties)** | — | Keyword stuffing; promotional superlatives; hidden or injected instructions/text aimed at LLMs; unverifiable statistics; contradictory claims; stale dates. Evidence: Aggarwal, E-GEO, Vishwakarma, GEO Defender. |

### Off-page factors the rubric should flag but not score at page level [I]
- **Earned-media footprint** (third-party reviews, trade press, standards bodies, forums): 69-94% of AI citations are earned media (Chen 2025); cross-source occurrence is a top predictor (Zhen 2026); referring domains and community presence predict discovery (Sharma 2026).
- **Classic search ranking** for the target and fan-out queries: retrieval position dominates (C-SEO, CORE, Lost in the Middle).
- **Own-domain exposure + branded fan-out**: brand mention rate jumps from ~3% to ~50-100% when the brand's own domain is retrieved (Tannenbaum 2026b).

### Measurement design recommendations [from Martinez 2026, Schulte 2026, Tannenbaum 2026a, Sielinski 2026]
- Measure visibility as a distribution: 7+ repetitions per prompt, multiple dates, multiple paraphrases, per engine separately.
- Separate stages: exposure (retrieved/cited at all) → selection → prominence (position, share of answer) → absorption (facts actually used) → fidelity (cited correctly).
- Use control pages (untreated) when claiming uplift; raw referral growth is confounded by platform growth (Watanabe 2026: x5.7 raw vs x1.82 estimated causal).
- Validate rubric scores against observed visibility before trusting weights; engine-agnostic scores showed no correlation with discovery in Sharma 2026.

### Domain-specific notes for technical/B2B content [I]
- Vishwakarma's gatekeeper findings (specs, price, recency) and AutoGEO's e-commerce rules (model numbers, specifications, step-by-step guidance) map closely to technical product content: spec tables, part numbers, standards compliance, selection guides, and installation steps are the strongest candidates for "extractable evidence".
- Aggarwal's domain table: Cite Sources helped most on "Facts" and "Law & Government" (relevant to standards/regulation content); Fluency helped on Business/Science/Health.
- Comparison content had the highest absorption among question types (Zhang 2026) — "X vs Y" and selection-guide pages are well supported.

---

## 6. Full source list

### Core GEO and benchmarks
1. Aggarwal et al. (2024). GEO: Generative Engine Optimization. KDD '24. https://arxiv.org/abs/2311.09735
2. Chen, Wang, Chen, Koudas (2025). Generative Engine Optimization: How to Dominate AI Search. https://arxiv.org/abs/2509.08919
3. Puerto, Gubri, Green, Oh, Yun (2025). C-SEO Bench: Does Conversational SEO Work? NeurIPS 2025 D&B. https://arxiv.org/abs/2506.11097
4. Bagga, Farias, Korkotashvili, Peng, Wu (2025/2026). E-GEO: A Testbed for GEO in E-Commerce. https://arxiv.org/abs/2511.20867
5. Kim, Jeong, Kim, Lee, Lee (2026). SAGEO Arena. https://arxiv.org/abs/2602.12187
6. Martinez (2026). Optimizing Visibility in Generative Engines: A Critical Survey of GEO (2023-2026). https://arxiv.org/abs/2607.14035
7. Nimase et al. (2026). GEO-Bench: Benchmarking Ranking Manipulation in GEO. https://arxiv.org/abs/2605.29107
8. Chen et al. (2025). CC-GSEO-Bench. https://arxiv.org/abs/2509.05607

### Optimization methods
9. Wu, Zhong, Kim, Xiong (2025/ICLR 2026). What Generative Search Engines Like and How to Optimize Web Content Cooperatively (AutoGEO). https://arxiv.org/abs/2510.11438 ; https://github.com/cxcscmu/AutoGEO
10. Chen et al. (2025). Role-Augmented Intent-Driven Generative Search Engine Optimization (RAID G-SEO). https://arxiv.org/abs/2508.11158
11. Zhou et al. (2026). IF-GEO. Findings ACL 2026. https://arxiv.org/abs/2601.13938
12. Chen et al. (2026). Mind Reader. ACL 2026. https://aclanthology.org/2026.acl-long.1894/
13. Yuan et al. (2026). AgenticGEO. https://arxiv.org/abs/2603.20213
14. Tian et al. (2026). Diagnosing and Repairing Citation Failures in GEO. https://arxiv.org/abs/2603.09296
15. Sourirajan et al. (2026). Beyond the Vacuum: Competitor-Aware GEO. https://arxiv.org/abs/2608.27631
16. Yu et al. (2026). Structural Feature Engineering for GEO (GEO-SFE). https://arxiv.org/abs/2603.29979
17. Lüttgenau, Colic, Ramirez (2025). Beyond SEO: A Transformer-Based Approach. https://arxiv.org/abs/2507.03169
18. Ho et al. (2025). Rewrite-to-Rank. https://arxiv.org/abs/2507.21099
19. Zhang et al. (2026). GEO: A VLM and Agent Framework for Pinterest Acquisition Growth. https://arxiv.org/abs/2602.02961
20. Multi-Agent GEO via Reusable Strategy Learning (2026). https://arxiv.org/abs/2604.19516

### Controlled factor studies and biases
21. Vishwakarma, Kumar, Jamidar (2026). What Gets Cited: Competitive GEO in AI Answer Engines. SIGIR 2026. https://arxiv.org/abs/2605.25517
22. Wan, Wallace, Klein (2024). What Evidence Do Language Models Find Convincing? ACL 2024. https://arxiv.org/abs/2402.11782
23. Fang et al. (2025). Do LLMs Favor Recent Content? Recency Bias in LLM-Based Reranking. https://arxiv.org/abs/2509.11353
24. Liu et al. (2023/2024). Lost in the Middle. TACL. https://arxiv.org/abs/2307.03172
25. Dai et al. (2024). Neural Retrievers are Biased Towards LLM-Generated Content. KDD 2024. https://arxiv.org/abs/2310.20501
26. Xion & Nejdl (2026). Revisiting source bias. https://arxiv.org/abs/2602.10833
27. Laurito et al. (2025). AI-AI Bias. PNAS 122(31). https://arxiv.org/abs/2407.12856
28. Ma, Qin, Xu, Tan (2025). When Content is Goliath and Algorithm is David. https://arxiv.org/abs/2509.14436
29. Tan et al. (2024). Blinded by Generated Contexts. https://arxiv.org/abs/2401.11911
30. Kamruzzaman, Nguyen, Kim (2024). Global is Good, Local is Bad? Brand Bias in LLMs. EMNLP 2024. https://arxiv.org/abs/2406.13997

### Observational audits of live engines
31. Zhang, He, Yao (2026). From Citation Selection to Citation Absorption. https://arxiv.org/abs/2604.25707
32. Xu, Iqbal, Montgomery (2026). Measuring Google AI Overviews. IMC 2026. https://arxiv.org/abs/2605.14021
33. Grossman et al. (2026). How Generative AI Disrupts Search. SIGIR 2026. https://arxiv.org/abs/2604.27790
34. Kirsten et al. (2026). Characterizing Web Search in the Age of Generative AI. Findings ACL 2026 (pp. 10827-10848).
35. Tannenbaum (2026a). Scoring With the Engine. https://arxiv.org/abs/2609.22655
36. Tannenbaum (2026b). From Prompt to Recommendation. https://arxiv.org/abs/2609.23162
37. Zhen et al. (2026). What Do Chinese-Language Generative Search Engines Cite and Surface? https://arxiv.org/abs/2607.15771
38. Sharma (2026). The Discovery Gap. https://arxiv.org/abs/2601.00912
39. Watanabe & Nakayashiki (2026). Disentangling AEO from Platform Growth. https://arxiv.org/abs/2606.04362
40. Allaham & Diakopoulos (2026). Synthetic Sources? AIES 2026. https://arxiv.org/abs/2605.23684
41. Schulte, Bleeker, Kaufmann (2026). Don't Measure Once. https://arxiv.org/abs/2604.07585
42. Sielinski (2026). From Stochastic to Stable. https://arxiv.org/abs/2607.10341
43. Liu, Zhang, Liang (2023). Evaluating Verifiability in Generative Search Engines. Findings EMNLP 2023. https://arxiv.org/abs/2304.09848
44. Li & Sinnamon (2024). Generative AI Search Engines as Arbiters of Public Knowledge. https://arxiv.org/abs/2405.14034
45. Narayanan Venkit et al. (2024/FAccT 2025). Search Engines in an AI Era. https://arxiv.org/abs/2410.22349
46. Vykopal et al. (2026). Assessing web search credibility and response groundedness in chat assistants. EACL 2026.

### Manipulation and defenses
47. Kumar & Lakkaraju (2024). Manipulating LLMs to Increase Product Visibility. https://arxiv.org/abs/2404.07981 ; https://github.com/aounon/llm-rank-optimizer
48. Pfrommer et al. (2024). Ranking Manipulation for Conversational Search Engines. EMNLP 2024. https://arxiv.org/abs/2406.03589
49. Nestaas, Debenedetti, Tramèr (2025). Adversarial SEO for LLMs. ICLR 2025. https://arxiv.org/abs/2406.18382
50. Jin et al. (2026). CORE: Controlling Output Rankings in Generative Engines. https://arxiv.org/abs/2602.03608
51. Zou et al. (2025). PoisonedRAG. USENIX Security 2025. https://arxiv.org/abs/2402.07867
52. Li et al. (2026). When Optimization Becomes Manipulation (GEO Defender). https://arxiv.org/abs/2609.02964
53. Hu (2025). GEO attack game theory. https://arxiv.org/abs/2501.00745

### Chunking and extractability
54. Chen et al. (2024). Dense X Retrieval. EMNLP 2024. https://arxiv.org/abs/2312.06648
55. Brådland et al. (2025). A New HOPE: Evaluation of Text Chunking. https://arxiv.org/abs/2505.02171
56. Merola & Singh (2025). Reconstructing Context: late chunking vs contextual retrieval. https://arxiv.org/abs/2504.19754
57. Kreileder et al. (2026). Evaluating Chunking Strategies for RAG on Academic Texts. https://arxiv.org/abs/2607.01852

### Gaps in the academic literature (as of Oct 2026)
- No peer-reviewed study isolates **schema/JSON-LD** effects on LLM citation.
- No academic study of **Google AI Mode query fan-out** mechanics; closest are multi-query GEO (IF-GEO, Mind Reader) and the branded fan-out finding in Tannenbaum 2026b. Industry fan-out data is outside this slice.
- No isolated causal test of **E-E-A-T-style author signals** (bylines, credentials) on LLM citation; Vishwakarma anonymized brands by design.
- Few **field experiments** with control groups (Watanabe 2026 and Pinterest 2026 are the only production-scale results found).
- Most lab work uses small/older models (GPT-3.5, GPT-4o-mini, Claude 3 Haiku); results drift with model versions.

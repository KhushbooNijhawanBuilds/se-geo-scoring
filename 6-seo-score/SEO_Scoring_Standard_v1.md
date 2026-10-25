# SE Blog SEO Scoring Standard v1 (23 Oct 2026)

## 1. Purpose and what the score means (business summary)

The **Blog SEO Score** rates how well one Schneider Electric blog article is built to be found, understood and chosen in classic web search (Google, Bing). The scale is 0–100. It is a standalone score. It is **never combined** with the Content GEO Score: GEO measures whether AI answer engines can cite a page, SEO measures whether search engines can rank it and show it well. The two now diverge (only about 38% of AI Overview citations come from top-10 pages, per Ahrefs), so a page that is Good on one and Average on the other is useful information.

The score covers only what can be seen on the page: the URL, the `<head>` metadata (title, meta description, canonical, robots, hreflang, Open Graph, JSON-LD) and the visible content. It measures **on-page quality and hygiene**. It does **not** predict rankings. The strongest measured ranking correlate, link authority, is off-page. Click behaviour (NavBoost) and Core Web Vitals are not visible on the page either. Those items sit beside the score as **Needs data**. Indexability problems sit beside it as a pass/fail **Technical eligibility** block. Neither adds or removes points.

How it works, in one line: 14 criteria, each decided by 3–6 yes/no checks. Every "yes" must quote the page or give the literal metadata value. The checks set a level from 0 to 5, and the level times the weight gives the points. Gates then cap the score for serious faults, and penalties subtract for bad practice.

| Band | Score | Action |
|---|---|---|
| Excellent | 90+ | Internal exemplar |
| Good | 70–89 | Minor tweaks ("Score is OK", threshold 70) |
| Average | 40–69 | Optimisation backlog |
| Poor | <40 | Fix first |

**What differs from GEO.** GEO already judges answer-first writing, evidence, neutrality and freshness. SEO adds a hygiene layer that GEO does not score: the title tag length and brand pattern, the meta description, the URL slug, the H1 and heading outline, topic placement without stuffing, internal-link architecture and tracking parameters, outbound link `rel`, image alt text and filenames, Article/BreadcrumbList markup and Open Graph. It also adds the technical eligibility block. Where SEO and GEO judge the same thing (intent, coverage, E-E-A-T, originality), the SEO checks are worded for searchers and search engines, not for AI extraction.

## 2. Scope

**In scope (scored):** URL/slug; `<title>`; meta description; H1/H2/H3; primary topic placement; search-intent match; topical coverage; E-E-A-T signals visible on the page; originality; visible versus markup dates; in-body internal and outbound links (anchors, parameters, `rel`); in-body images (alt, filename); JSON-LD Article/BlogPosting and BreadcrumbList; Open Graph; spam patterns visible on the page.

**Reported beside the score, not in points:** Technical eligibility (§7) and Needs data (§8).

**Out of scope:** site navigation, header, footer, cookie banners, newsletter boxes and related-post widgets (except where they inject markup into the article, as in S5 c4); off-page signals; anything that needs a site crawl.

**Inputs:** the page URL, plus, where available, the raw HTML (`seo_extract.py --html`) or the corpus markdown (`--md`), and optionally a target keyword or question. If the head tags cannot be seen (for example, a Copilot reading rendered text only), those checks are marked **na** and the report says so. The judge never guesses them.

## 3. Criteria, weights and why

### 3.1 Criteria table

| ID | Criterion | Weight | Evidence strength | Why this weight |
|---|---|---|---|---|
| S1 | Search intent match | 14 | Strong as a mechanism (Google helpful-content questions; NavBoost confirmed in trial testimony, weights unknown); Semrush ranks "text relevance" #1 | Satisfying the query is the core of ranking; official guidance and correlation evidence agree |
| S7 | Topical coverage and depth | 14 | Moderate–strong (correlation; Google "substantial, complete description of the topic") | Same evidence family as S1; replaces word-count targets |
| S8 | E-E-A-T: author, expertise, sourcing | 12 | Official as trust evidence (Google: E-E-A-T "is not a ranking factor" itself, but bylines and sources are what raters look for; QRG Sep 2025) | High for SE because electrical and energy topics can be YMYL-adjacent |
| S9 | Originality and first-hand value | 11 | Official (Google "original information, reporting, research or analysis"); leak attribute `contentEffort` (practitioner reading only) | Commodity text is what the 2024–26 core updates demote; weight just below S8 because the evidence is partly inferred |
| S2 | SEO title tag | 10 | Official best practice (Google title-link doc, updated 2025-12-10); observational rewrite data (Zyppy, 81k titles); split tests that move traffic 10–24% (SearchPilot) | The best-evidenced hygiene item, and the only one with controlled experiments |
| S5 | H1 and heading structure | 6 | Official for clarity ("make it clear which text is the main title"); Google: heading order and count do not matter for ranking | Medium: structure helps comprehension and passage understanding, not as a ranking boost |
| S11 | Internal links | 6 | Official (crawlable `<a href>`, descriptive anchors, every page linked); correlational (Zyppy) and a few SearchPilot tests | Discovery and topical context; counts are heuristics |
| S6 | Primary topic placement (no stuffing) | 5 | Weak: Google has no "keyword in first paragraph" rule and says its language matching is sophisticated; stuffing is spam policy | Kept low: a clarity heuristic plus a stuffing tripwire |
| S10 | Freshness and date integrity | 5 | Official (visible date, matching structured data, no date bumps without change) | Low: hygiene and trust, not a ranking lever for evergreen posts |
| S3 | Meta description | 4 | Official: snippets come "mainly from page content", the meta description is used "occasionally", not a ranking factor; Google rewrites 63–71% (Ahrefs 2020, Portent 2020) | Low: CTR and snippet hygiene only, and CTR is falling under AI Overviews |
| S14 | Structured data and Open Graph | 4 | Official: Article markup has "no required properties", does not improve ranking, enables rich-result eligibility; og:title is a title-link source | Low: eligibility and clarity, not ranking |
| S4 | URL / slug | 3 | Official: keywords in the URL have "hardly any effect" beyond breadcrumbs; Mueller "very lightweight" | Very low: user-facing hygiene; never change a live URL for SEO alone |
| S12 | Outbound links | 3 | Official ("citing trusted sources can build trust", nofollow only for untrusted/paid/UGC); one small experiment (Reboot, 10 sites) | Very low: the evidence is weak |
| S13 | Images and alt text | 3 | Official: alt is "the most important attribute" for image metadata (image SEO doc, 2026-03-02); no ranking study | Very low for blog text ranking; also an accessibility duty |
| | **Total** | **100** | | About 61% on S1, S7, S8, S9 and S2, where the evidence is strongest |

### 3.2 Why no stage multipliers

GEO reweights criteria by buyer stage because its evidence shows that answer engines favour different content at different stages. The SEO notes contain **no evidence** that title, meta, URL, heading or markup hygiene matters more or less by funnel stage. The SEO effects of intent are handled **inside** S1 (c3: the format fits the dominant intent, informational or commercial investigation) and S7 (the facts that intent needs). Weights are therefore fixed. This can be revisited if Search Console data shows stage-specific gaps.

## 4. Checks and exact pass rules

Legend: **[C]** computed by `seo_extract.py` (the AI must not override it without a written reason); **[J]** judged by the AI with a verbatim quote; **[H]** computed when inputs allow (for example, a keyword was given), otherwise judged. "Basis" gives the source type: G = Google/Bing documentation; E = controlled experiment; O = observational or vendor study; V = vendor tool convention; H = heuristic (ours).

### S1 Search intent match (14)
- c1 [J] The primary query can be identified from the title or H1, worded as a searcher would type it (no pun, slogan or clever tail). Basis G (title-link "descriptive"), helpful-content "descriptive, helpful summary" question.
- c2 [J] Within the first 150 words of the body, a sentence directly answers the query or defines the subject. A Summary block counts. Basis G QRG §5.2.2 (main content up top); H for the 150 words.
- c3 [J] The format fits the dominant intent: informational means a definition, explanation or how-to; commercial investigation means criteria, comparisons, standards or total cost of ownership. Basis G (four-type intent model; r2_technical_intl_b2b).
- c4 [J] Every explicit promise in the title, H1 or meta (a number of items, "how X affects Y") is delivered as visible structure. Basis G (title-link "inaccurate"; QRG "misleading titles").
- c5 [J] The page stays on intent: no section switches to an unrelated product pitch, and product mentions serve the query. Basis G (helpful-content "people-first").
- Anchor: c1 + c2 + c4 pass → at least level 3.

### S2 SEO title tag (10)
- c1 [C] Exactly one non-empty `<title>`, with at least 10 characters of main text (excluding the brand), and not generic ("Home", "Blog"). Basis G ("every page ... has a title"); Lighthouse/SF/Semrush "missing title" = error.
- c2 [C] Length band: **30–60 characters including the brand, or ≤65 characters when the estimated width is ≤600px** (18px Arial estimate). Basis O: Zyppy (Q1 2022) found the lowest rewrite rate at 51–60 characters (39–42%), above 76% beyond 60 and 99.9% beyond 70. V: Yoast 400–600px (verified from source), Screaming Frog 30–60 characters / 200–561px, Semrush warning above 70. Google sets **no** limit and truncates "to fit the device width", so this is a truncation/rewrite risk band, not a rule.
- c3 [C] The brand appears at most once, concisely, at the start or end after a delimiter (- : |). Basis G ("brand your titles concisely"; "site name at the beginning or end"). Note: SEJ/blckalpaca report brand removal as the most common rewrite in 2025 (unverified, 403).
- c4 [H] The primary topic appears near the front: within the first ~45 characters of the main title text. Basis H (truncation logic) plus second-hand Bing advice (keyword near the beginning). No experiment.
- c5 [C] No stuffing or staleness: no content word 3 or more times, and no year older than the dateModified year. Basis G ("avoid keyword stuffing"; "obsolete" rewrite example).
- c6 [C] The title matches the H1: at least 50% of the title's main content words appear in the H1, and every number in the title also appears in the H1. Basis G (the H1 is a title-link source; mismatches cause rewrites); O (Zyppy: numbers dropped 25.8% of the time when absent from the H1).
- Caps: c1 fail → S2 = 0. **c2 fail → S2 max 3** (calibration v1; basis O Zyppy).

### S3 Meta description (4)
- c1 [C] Exactly one non-empty `<meta name="description">`. Basis G Lighthouse audit.
- c2 [C] **120–160 characters.** Basis V/O: Yoast 121–156 (verified from source), Screaming Frog 70–155 / 400–985px, common checkers 120–160; Portent advises putting the key message in the first ~120 characters on mobile. Google sets no limit. Pages at 70–119 characters fail here; this is a convention, which is why the weight is low.
- c3 [J] It summarises **this** page accurately (no boilerplate, not identical to the title, no promise the page does not keep), with the key message in the first ~120 characters. Basis G ("accurately describe the specific page"; "unique to one particular page"). The extractor auto-fails it if the description is identical to the title.
- c4 [H] It includes the primary topic or a close variant. Basis V (Yoast/AIOSEO; bolding in snippets); weak.
- c5 [C] No content word 3 or more times. Basis G ("long strings of keywords").
- Cap: c1 fail → S3 = 0. Uniqueness across the site is Needs data (N6).

### S4 URL / slug (3)
- c1 [C] Readable words; no ID-like tokens (5 or more digits, or hex of 8 or more characters). Basis G URL-structure doc ("readable words rather than long ID numbers").
- c2 [C] Hyphens, lowercase, no underscores, spaces or percent-encoding. Basis G ("hyphens instead of underscores"; case sensitive).
- c3 [C] No query parameters, session IDs or fragments on the canonical URL. Basis G ("trim unnecessary parameters"; "avoid session IDs"; "don't use fragments").
- c4 [C] Slug ≤60 characters. Basis V/H (convention; Google gives no limit).
- c5 [J] The slug is correctly spelt, in the page's language, matches the topic, and has no repeated content word or slogan. Basis G ("words in your audience's language").
- Note: date folders (`/2026/10/13/`) are not scored; no Google statement was found. **Never change a live URL for this criterion alone.** If a URL must change, use a single 301/308 hop kept for at least a year (Google site-move doc).

### S5 H1 and heading structure (6)
- c1 [C] Exactly one H1 (the visually dominant main title). Basis G ("make it clear which text is the main title"). Mueller says several H1s are fine, so a fail here costs little; this is clarity hygiene.
- c2 [C] Pages over 300 words have H2/H3 subheads at least every ~350 words. Basis V (Yoast ≤300 words per section) plus G Starter Guide ("break long content into sections"); 350 gives a little tolerance.
- c3 [J] At least 60% of H2/H3s describe their section, and no major section lacks a heading. Generic labels ("Overview", "A slow start", "Looking ahead") fail. Basis G passage understanding / accessibility.
- c4 [C] No non-content headings inside the article's heading outline (comment form, "Top picks", related-post titles as `<h2>` inside `<article>`). Basis H/accessibility. Usually a **[T]** template fix.
- Heading order is informational only and never fails (Google: order does not matter for ranking).

### S6 Primary topic placement, no stuffing (5)
Requires a primary topic phrase: supplied by the user, otherwise inferred by the judge as the query a searcher would type, and flagged "inferred". Matching ignores stop words and light suffixes (recycled ≈ recycling).
- c1 [H] Topic in the title. c2 [H] in the H1. c3 [H] in the first 150 words. c4 [H] in at least one H2/H3. Basis V/H (Yoast, AIOSEO, Rank Math keyphrase checks; Google: no placement rule). Low weight for that reason.
- c5 [C] No stuffing: the exact phrase is ≤3% of words and appears in ≤50% of subheads (when there are 4 or more); no keyword or location lists. Basis G spam policy (keyword stuffing); the thresholds are a **tripwire, not a target**.
- Limitation: when the keyword is inferred from the H1, c1 and c2 are close to circular. Supply the keyword when one exists.

### S7 Topical coverage and depth (14)
- c1 [J] Most of the 3–5 follow-up questions a searcher would ask next have a section or a direct answer. Basis G ("substantial, complete or comprehensive description"); O (Semrush relevance; SERP-coverage tools correlate only ~0.2–0.3, so the judge uses questions, not a tool score).
- c2 [J] Key terms and acronyms are defined at first use. Basis G (clarity); H.
- c3 [J] Specifics: values with units, standards, conditions or named examples (at least 3 distinct ones). Basis G ("insightful analysis or interesting information beyond the obvious").
- c4 [J] One topic per URL; no off-topic sections. Basis Bing guidelines (Feb 2026, "one topic per URL"); G cannibalisation guidance.
- c5 [J] Depth matches the question: no padding, repetition or filler aimed at a length target. Basis G ("no preferred word count").
- Anchor: c1 + c3 pass → at least level 3. **No word-count check exists.**

### S8 E-E-A-T: author, expertise, sourcing (12)
- c1 [J] A named human author is visible (a byline or an in-text "Author:" line). "Guest Blogger", "Admin" or a team name alone fails. Basis G ("who created the content"; bylines "where reasonably expected").
- c2 [C] The byline links to **that named author's own** bio page (not `/author/guest-blogger/`). Basis G (bylines that lead to more information about the author).
- c3 [J] The author's role, credential or relevant experience is visible on the article. Basis G/QRG (expertise questions).
- c4 [J] Statistics and factual claims cite a named source (linked, or named with a year). Basis G trust questions; QRG.
- c5 [J] No easily checked factual error or internal contradiction. Basis QRG §3.2/§4.5 (YMYL accuracy).
- Caps: c1 fail → S8 max 2. **c2 fail → S8 max 3** (calibration v1).

### S9 Originality and first-hand value (11)
- c1 [J] A first-hand observation with a specific detail (scale, situation, number). A bare years-of-experience claim fails. Basis G ("first-hand expertise"; the "Experience" in E-E-A-T).
- c2 [J] Schneider first-party data, test, white paper result or deployment, with conditions. Basis G ("original information, reporting, research").
- c3 [J] Analysis beyond paraphrase: a framework, typology, decision rule or quotable thesis. Basis G ("original analysis").
- c4 [J] An original visual, table or diagram (not a stock photo; `GettyImages`/`AdobeStock` filenames count as stock). Basis G image guidance; H.
- c5 [J] Not mass-produced, unedited or republished without added value; syndication disclosed. Basis G spam policy (scaled content); QRG §4.6.6.
- **Cap: c1 and c2 both fail → S9 max 3** (calibration v1).

### S10 Freshness and date integrity (5)
- c1 [C] A visible, labelled publication date near the title. Basis G (publication-date guidance; cited from memory in round 1, consistent with r2).
- c2 [C] The visible date equals JSON-LD `datePublished` (or `article:published_time`) to the day. Basis G (matching dates in structured data).
- c3 [C] `dateModified` ≥ `datePublished` and not in the future. Basis G.
- c4 [H] If `dateModified` is 7 or more days after publication, a visible "Updated" date is shown (na if under 7 days). Basis G (show the update date prominently); 7 days is H.
- c5 [J] No stale years, superseded standards or old statistics presented as current. Basis G ("obsolete" title example; helpful content).
- Cap: c1 fail → S10 max 1. Date bumps without substantive change are gate SG7 when evidenced.

### S11 Internal links (6)
- c1 [C] At least 3 contextual in-body links to SE pages (blog.se.com, se.com, schneider-electric.com). Basis H; V (content tools 3–5 per 1,000 words). Google gives no number.
- c2 [J] At least one goes to a relevant hub, pillar, solution page or sibling article on the same topic. Basis G (important pages linked); topic clusters are practitioner convention.
- c3 [C] Anchors are descriptive: no generic anchors ("click here", "read more", "here", a bare URL), and the same anchor text never points to two different URLs. Basis G link best practice; Lighthouse "link text".
- c4 [C] No tracking or ID parameters on internal links (`utm_*`, `gclid`, `fbclid`, `sourceId`). Basis G ("trim unnecessary parameters"); parameter variants also hit the blog's robots.txt `Disallow: /*?*`. The internal-UTM harm is our inference.
- c5 [C] All in-body links are crawlable `<a href>` (no `javascript:` or onclick-only). Basis G.
- Inbound links and orphan status are Needs data (N7).

### S12 Outbound links (3)
- c1 [J] At least one outbound link to an authoritative primary source for a statistic or third-party claim (na if the page has none). Basis G; E (Reboot, small).
- c2 [C] `rel` is correct: paid/affiliate links are `sponsored`/`nofollow`, and not every editorial external link is nofollowed (na if there are no external links). Basis G.
- c3 [J] Outbound links are relevant and reputable (na if there are none). Basis G trust.

### S13 Images and alt text (3)
- c1 [C] Every in-body content image has non-empty alt. A decorative `role="none"` hero still fails if it is the article's lead image. Basis G image SEO doc; accessibility (WCAG 1.1.1).
- c2 [J] Alt text describes the image, is ≤125 characters and is not stuffed (na if there is no alt). Basis G; V (125 characters is a screen-reader convention; Screaming Frog flags over 100).
- c3 [C] Filenames are descriptive words, not camera, CMS or stock IDs. Basis G ("descriptive filenames").
- c4 [J] At least one relevant image or diagram sits near the text it illustrates. Basis G.

### S14 Structured data and Open Graph (4)
- c1 [C] Article/BlogPosting/NewsArticle JSON-LD with `headline`, `datePublished`, `dateModified` and `image`. Basis G Article doc (recommended properties; "no required properties").
- c2 [C] `author` is a Person with a real name (not "Guest Blogger"/"Admin") and `url` or `sameAs`. Basis G.
- c3 [C] Markup matches the visible page: the headline equals the H1 or title, the author equals the visible author, and the dates match. Basis G (markup must reflect visible content).
- c4 [C] BreadcrumbList is present. Basis G (breadcrumb rich result); low.
- c5 [C] `og:title`, `og:type`, `og:image` and `og:url` are present, and `og:url` equals the canonical. Basis ogp.me spec; G (og:title is a title-link source).
- Cap: c1 fail → S14 max 1. No points for FAQPage/HowTo (FAQ rich results restricted Aug 2023; HowTo dropped). No llms.txt or "AI markup" (Google: not needed).

## 5. Level, weight and score rules (same as GEO v2.1)

1. For each criterion, n = pass + fail checks (na ignored) and p = passes. If **more than half** the checks are na, the criterion is **dropped** and the remaining weights are renormalised to 100.
2. **Ceiling = 5 if p = n, otherwise min(4, round-half-up(5p/n)).** The judge proposes a level; the final level = min(proposed, ceiling). Level 5 needs every applicable check to pass, and the judge should propose 5 only for exemplary evidence.
3. Anchors raise the level to at least the anchor level when the listed checks pass (na counts as met). Caps then lower it. Both are applied in code from `seo_weights.json`.
4. Gate effects on levels (zeroing) are applied last.
5. points_i = level_i / 5 × eff_weight_i; raw = Σ points; final = min(lowest gate cap, raw − penalties), floored at 0 and rounded half-up. recoverable_i = (5 − level_i) / 5 × eff_weight_i.
6. A score within 3 points of 40, 70 or 90 is **Borderline**: confirm with 3 independent judge runs and use the median.
7. Confidence = low if criteria judged with low confidence carry more than 33 points of weight, medium if more than 10.

## 6. Computed versus judged

| Computed by `seo_extract.py` [C] | Judged by the AI [J] |
|---|---|
| S2 c1, c2, c3, c5, c6 (c4 with keyword) | S1 all |
| S3 c1, c2, c5 (c4 with keyword; c3 auto-fails if meta = title) | S3 c3 |
| S4 c1–c4 | S4 c5 |
| S5 c1, c2, c4 | S5 c3 |
| S6 c1–c5 (with keyword) | S6 when no keyword (judge infers and flags it) |
| S8 c2 (from the byline link) | S7 all; S8 c1, c3–c5; S9 all |
| S10 c1–c3 (c4 when under 7 days) | S10 c4 (≥7 days), c5 |
| S11 c1, c3, c4, c5; S12 c2 | S11 c2; S12 c1, c3 |
| S13 c1, c3 (alt >125 auto-fails c2) | S13 c2, c4 |
| S14 c1–c5 | — |
| Eligibility E2, E3, E5, E6 (viewport), E7, E8 from HTML | E1 and the X-Robots-Tag/robots.txt part of E2 need the HTTP response; E4 reciprocity needs a crawl |

The judge may override a computed result only with a reason starting `override:` (for example, a byline that names "Guest Blogger" while the text names the real author). Without `--html`, link, filename, canonical and JSON-LD-field checks become na.

## 7. Gates (score caps; the lowest wins)

| ID | Trigger | Cap | Level effect | Basis |
|---|---|---|---|---|
| SG1 | Spam-policy pattern on the page: hidden text/links, keyword or location blocks, gibberish with keywords, scraped/uncited copy, doorway templating, leftover AI artefacts ("As an AI…") | 39 | — | G spam policies (Mar 2024 + 2025–26 enforcement) |
| SG2 | The primary query is never answered, or the page is thin (no substantive content beyond boilerplate) | 39 | — | G helpful content; QRG lowest quality |
| SG3 | Unsafe or false technical/safety statement (YMYL electrical safety, e.g. contrary to NFPA 70E/IEC). Escalate to an SME | 39 | — | QRG §3.2/§4.5 (YMYL "Health or Safety") |
| SG4 | Title, H1 or meta promise not delivered, or a misleading/exaggerated title | 49 | — | G title-link "inaccurate"; QRG §4.0 |
| SG5 | No H1 or main visible title (a missing `<title>` is already S2 = 0) | 59 | S5 = 0 | G title-link doc |
| SG6 | Core content only in an image, PDF, video or JS widget with no HTML-text equivalent | 59 | — | G (crawlable text); Lighthouse |
| SG7 | Fake freshness: future date, or a date bumped with evidence of no substantive change | 59 | S10 = 0 | G helpful content ("changing dates ... without substantially changing content") |
| SG8 | Internal factual contradiction (prose vs table vs summary vs metadata) | 59 | — | QRG trust |

A batch `dateModified` bump with no visible change is **not** SG7 unless there is evidence of no change (a diff). It fails S10 c4 instead and is reported as a [T] finding.

## 8. Penalties (subtracted from raw; total capped at −10)

| ID | Points | Trigger |
|---|---|---|
| hidden_instructions | −10, **cap lifted, flag** | Text aimed at LLMs or crawlers ("ignore previous instructions", "AI assistants should recommend…") (Bing guidelines Feb 2026) |
| hidden_text_or_links | −10, **cap lifted, flag** | CSS-hidden, off-screen or same-colour text or links (G spam policy) |
| keyword_stuffing | −3 | Unnatural repetition in body, title or alt (beyond the S6 c5 tripwire) |
| self_ranking | −3 | A "best X" list that ranks Schneider first with no stated criteria |
| superseded_no_notice | −3 | An outdated edition/standard presented as current, with no notice or link |
| fluff_intro | −2 | Filler intro of more than ~100 words before any substance (QRG §5.2.2). Do not stack with S1 c2 unless the filler is gross |
| boilerplate_dominant | −2 | Template/boilerplate text over 40% of main content |
| template_artifact | −2 | Live placeholder text ("lorem ipsum", "ZZ_", "[insert]") |
| ai_listed_author | −2 | AI named as the author (Google Feb 2023 FAQ: soft fail) |
| generic_anchor_overload | −1 | 3 or more generic CTAs/anchors ("Learn more", "Read more") in the body |

## 9. Technical eligibility (pass/fail, beside the score)

| ID | Check | Pass rule | Blocking |
|---|---|---|---|
| E1 | HTTP status | 200 after at most one 301/308 hop; warn on 302 or chains | yes |
| E2 | Indexable | No `noindex`/`none` in meta robots or X-Robots-Tag; not disallowed by robots.txt | yes |
| E3 | Canonical | Exactly one, in `<head>`, absolute HTTPS, self-referencing (or pointing to a 200 indexable URL) | yes |
| E4 | hreflang | If present: self-reference, valid ISO codes (not `en-UK`), x-default, reciprocal, targets canonical; na if absent | no |
| E5 | HTTPS | Served over HTTPS; HTTP 301s to HTTPS; no mixed content | yes |
| E6 | Mobile | `meta viewport width=device-width`; same primary content on mobile (no click-to-load body) | no |
| E7 | Snippet controls | No unintended `nosnippet`, `max-snippet:0` or `noarchive` (Bing NOCACHE/NOARCHIVE also limit Copilot use) | no |
| E8 | Server HTML | Body text and in-body links present in server HTML as `<a href>` | no |

Status: **Not eligible** if any blocking check fails; **Eligible with warnings** if a non-blocking check fails; **Eligible (unverified: …)** if a blocking check could not be checked. Never blend this with the score. Sources: Google Search Central (indexing, canonical, localized versions); Lighthouse SEO audits; r2_technical_intl_b2b (a).

## 10. Needs data (site level, reported, never scored)

| ID | Item | Data source |
|---|---|---|
| N1 | Core Web Vitals field data (p75 LCP ≤2.5s, INP ≤200ms, CLS ≤0.1); a weak tiebreaker | CrUX API / PageSpeed Insights |
| N2 | Backlinks and referring domains (the strongest correlate) | Ahrefs / Semrush / Majestic |
| N3 | Clicks, impressions, CTR, queries | Google Search Console Performance; Bing Webmaster Tools |
| N4 | Cannibalisation: 2 or more URLs swapping impressions for the same query/intent | Search Console query + page dimensions |
| N5 | Index status and the Google-selected canonical | Search Console URL Inspection API |
| N6 | Title and meta uniqueness across the site | Site crawl (Screaming Frog / Sitebulb) |
| N7 | Inbound internal links, orphan status, links from the pillar/hub | Site crawl |
| N8 | hreflang cluster reciprocity; robots.txt and sitemap consistency (sitemap lastmod vs dateModified) | Crawl of alternates; robots.txt; sitemaps |

## 11. Excluded myths and non-signals (never scored)

| Excluded item | Why |
|---|---|
| Keyword density targets (Yoast 0.5–3%, Rank Math 1–1.5%) | No supporting study; Google has no density target. Only kept as a stuffing tripwire (S6 c5) |
| Word-count targets (Rank Math 2,500 for full marks, "1,500 for blogs") | Google: "no preferred word count", length "alone doesn't matter"; word count is spread evenly across the top 10 (Backlinko) |
| Readability scores (Flesch, grade level, passive voice, transition words) | Mueller: no algorithms use basic readability scores; Ahrefs/Portent found little or no correlation; Yoast removed its Flesch file |
| Power, sentiment and emotional words in titles | Plugin heuristic only (Rank Math/AIOSEO); no test |
| Meta keywords tag | Google: not used |
| Third-party tool content scores (Surfer, Clearscope, MarketMuse, Yoast "green") | Google does not use them; correlation with rank only ~0.17–0.30 (Ahrefs) |
| Keyword in domain or exact-match slug as a ranking boost | Google: "hardly any effect" (only the readable-slug hygiene in S4 is scored) |
| Heading order or count as a ranking factor | Google: neither matters for ranking (S5 scores clarity only) |
| Text-to-HTML ratio | No evidence; Semrush-only metric |
| FAQPage/HowTo markup for rich results | FAQ rich results restricted (Aug 2023); HowTo dropped |
| llms.txt or special "AI" markup | Google: not needed for AI features |
| Keyword in image alt | Alt should describe the image; Yoast's 30–75% rule is a myth for ranking |
| "Previously used keyphrase" plugin warnings | Real cannibalisation needs Search Console (N4) |

## 12. Evidence table (main sources)

| Source | Type | Used for |
|---|---|---|
| Google, Influencing title links (updated 2025-12-10) | Official | S2 c1, c3, c5, c6; title-link sources incl. og:title; SG4 |
| Google, SEO Starter Guide (2025-12-10) | Official | S3, S4, S5, myths (meta keywords, URL keywords, heading order, length) |
| Google, Control your snippets (2026-04-20) | Official | S3; E7 |
| Google, URL structure (2026-10-21); Site moves (2026-08-20) | Official | S4 |
| Google, Creating helpful, reliable, people-first content | Official | S1, S7, S8, S9, S10, SG2, SG7 |
| Google, Search Quality Rater Guidelines (Sep 2025) | Official (rater) | S8, S9, SG3, SG4, fluff_intro |
| Google, Spam policies (2024; 2025–26 enforcement) | Official | SG1, keyword_stuffing, hidden_text_or_links |
| Google, Article structured data; Image SEO (2026-03-02) | Official | S14, S13 |
| Google, Localized versions / canonical / Core Web Vitals | Official | §9, N1 |
| Bing Webmaster Guidelines (rewritten Feb 2026) | Official | S7 c4, hidden_instructions, E7 |
| Lighthouse SEO audits | Official tool | S3 c1, S11 c3, E-checks |
| Zyppy title rewrite study (Q1 2022, 80,959 titles) | Observational | S2 c2 and its cap, S2 c6 |
| SearchPilot title split tests (2024–26) | Experiment | S2 weight (title wording moves traffic 10–24%) |
| Ahrefs meta study (2020); Portent (2020) | Observational | S3 weight and c2 |
| Backlinko ranking factors and CTR studies | Observational | Weights (links strongest; word count flat; 40–60-character titles best CTR) |
| Semrush ranking factors | Observational | S1/S7 weight ("text relevance") |
| Yoast source code; Screaming Frog; Semrush Site Audit; Sitebulb (r2_tool_check_library) | Vendor convention | Thresholds: title 30–60 chars / 600px, meta 120–160, ~300 words per section, alt ≤125 |
| Ahrefs SEO content-score study | Observational | Excluding tool scores |
| Mueller / Sullivan / Illyes statements | Googler statements | Multiple H1s OK, readability, URL keywords lightweight |
| Hobo Web, 2024 leak write-ups | Practitioner reading | S9 (contentEffort), NavBoost context only; never used to set a threshold |

## 13. Known limitations

- **It does not predict rankings.** Off-page authority and click data dominate and sit outside the score. Validate the score against Search Console clicks and impressions before using it for targets.
- **Many thresholds are conventions.** Title and meta lengths, slug ≤60, ≥3 internal links, 150-word intro, 350 words per subhead, alt ≤125 and the 7-day update rule are vendor or heuristic numbers. Each is labelled, and the weights stay low where that is all there is.
- **Pixel width is an estimate** (an 18px Arial approximation). Google publishes no pixel numbers.
- **Inferred keywords make S6 partly circular.** Supply the target keyword when one exists.
- **The judged criteria (S1, S7, S8, S9; 51 points) depend on the LLM judge.** Use 3 runs for borderline scores and calibrate against editor labels (Bing's labelling work shows LLM judges can match humans when calibrated).
- **Several Google pages were cited from memory in round 1** (publication dates, link best practices). The Bing guidelines page could not be fetched directly in round 2, and the McAlpin 2025 rewrite study returned 403. Re-verify these before freezing v1.1.
- **The calibration sample is 6 recent, templated posts**, not a random sample. Mean 67.5, range 49–75. Recalibrate on 30 or more posts, including old and thin ones.
- **Site-level checks are not covered:** uniqueness, cannibalisation, orphans and hreflang reciprocity need a crawl or Search Console (§10).
- The extractor's content scope is tuned to blog.se.com (WordPress `wp-block-*`). On other templates it falls back to `<article>`/`<main>`/`<body>` and may include widgets; check the heading list.

## 14. Change log

- v1 (2026-10-23): first release. Calibration caps were added after the test run: S2 max 3 when the title fails the length band; S8 max 3 when the byline is not the named author's bio; S9 max 3 with no first-hand experience and no first-party data. Scores moved from a mean of 69 to 67.5.

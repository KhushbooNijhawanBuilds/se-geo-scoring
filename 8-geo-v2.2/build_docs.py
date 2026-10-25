#!/usr/bin/env python3
"""Generate GEO_Scoring_Standard_All_Types_v2.2.md. All tables (weights, effective weights, gates,
penalties, anchors, caps, families, pilot statistics) are generated from weights.json, the engine and the
pilot CSV; the explanatory prose is hand-written below."""
import csv, json, os, statistics
from collections import Counter, defaultdict
from common import W, C, KEYS, STAGES, ROOT, FINAL, eff_weights, criteria_for, gates_for, fact_density, calc, anchors_for, block_fail_for, note_checks_for

SRC_NAMES = {"FW": "framework", "V2": "page-types-v2", "V1-split": "page-types v1 (phrase list split into checks)",
             "V1-split+DER": "v1 split + derived", "DER": "DERIVED (no checks in source)", "TA": "type-analysis", "BLOG": "blog prompt"}

FAM_LABEL = {"answer_def": "Answer-first & definitions", "evidence": "Evidence & insight", "fanout": "Fan-out coverage",
             "tone": "Neutral tone", "comparison": "Comparison & selection", "specs": "Specs, compatibility, standards",
             "proof": "Proof", "commercial": "Commercial, lifecycle, next step", "freshness": "Freshness", "other": "Stage-neutral (1.0)"}


def pilots():
    rows = list(csv.DictReader(open(os.path.join(FINAL, "SE_GEO_scored_inventory_v2.1.csv"), encoding="utf-8-sig")))
    by = defaultdict(list)
    for r in rows:
        by[r["Scoring logic"]].append(r)
    return by


def kappa():
    try:
        a = json.load(open(os.path.join(FINAL, "agreement.json")))["summary"]
        return a
    except Exception:
        return {}


def esc(s):
    return s.replace("|", "\\|")


OVERVIEW = """
## 1. Overview

### 1.1 What the score measures, and what it does not
The **Content GEO Score** (0-100) measures the *citation-readiness of a page's content*: how easily an AI answer engine (ChatGPT, Perplexity, Google AI Overviews / AI Mode, Gemini, Copilot, Claude) can understand, trust, extract and quote the page for the buyer question it targets.

It does **not** predict or promise citations. Actual citation also depends on retrieval rank, off-site consensus (about 80% of AI citations are third-party) and technical access. Technical GEO - robots.txt, server vs client rendering, schema code, speed, canonicals, sitemaps, llms.txt - is **out of scope**: it is reported as "Out-of-scope observations -> SE Digital" and never scored. Content decisions that block extraction (key facts only in an image, PDF, collapsed tab, widget or gated form) **are** in scope and are scored under U3 and gate G6.

The score is computed on the **rendered page content** (what a visitor sees after load, including collapsed tabs, marked hidden). Header, navigation, footer, cookie banner and breadcrumbs are excluded. A *crawler gap* (server-HTML words / rendered words < 0.7, or H1/key facts missing server-side) is reported beside the score, not inside it. The score is not comparable with the SE Toolkit's "GEO Strategic Score", which is about 45% technical.

### 1.2 Method in one line
**binary checks -> levels (0-5) -> weights x stage multiplier (renormalised to 100) -> raw score -> minus penalties -> gate caps -> final score and band.**

1. **Checks.** Each criterion has 1-7 binary checks. The judge (an LLM or a person) answers each check *pass / fail / na* and quotes the verbatim evidence (max 40 words). Missing evidence = fail. Absence/layout checks may pass on a judge note instead of a quote (section 1.4).
2. **Levels.** The calculator (`geo_score_calc.py`) turns the checks into a level 0-5 deterministically (section 1.4). In v2.2 the judge does not pick levels: the level is the check ceiling, and the judge can only lower it with a `downgrade_reason` that names the weak passed check.
3. **Weights.** Every page type has default weights that sum to 100. Each criterion belongs to a *family*; the buyer-journey stage multiplies each family's weights; the result is renormalised to 100 (the *effective weights*, tabulated for all 5 stages in every type section).
4. **Raw score** = sum over criteria of level / 5 x effective weight.
5. **Penalties** are subtracted (max -10 in total, except hidden instructions).
6. **Gates** cap the final score (the lowest triggered cap wins) and can force some criterion levels down.
7. **Final score** is rounded to a whole number and mapped to a band. Each criterion also gets *recoverable points* = (5 - level) / 5 x effective weight, which ranks the gaps.

### 1.3 Bands
{bands}

The default "Score is OK" threshold is **{ok}**. Calibration intent: a typical un-optimised page lands at 35-60; 90+ should be rare. If a final score is within 3 points of 40, 70 or 90, run 3 independent judgements and use the median.

### 1.4 Levels explained (how the calculator sets them)
| Level | Label | Meaning |
|---|---|---|
| 0 | Absent | Not present at all, or contradicts the requirement |
| 1 | Very weak | Token presence; would not be extracted |
| 2 | Weak | Present but buried, vague or incomplete |
| 3 | Adequate | Meets the basic requirement; extractable with effort |
| 4 | Strong | Clear, specific, well placed; likely to be lifted as-is |
| 5 | Exemplary | Best in class; needs exceptional evidence (original data, complete specs, named experts) |

Exact code rules (`level_from_checks`, v2.2; `--rules v2.1` reproduces v2.1 exactly):
- **Check preprocessing (v2.2).** (a) A pass whose `evidence_type` is `"note"` is accepted only on the absence/layout checks in `note_allowed_checks` (below); on any other check it is scored as fail - presence checks still need a verbatim quote. (b) `block_dependent_checks`: when a block check fails, na on its dependent checks is scored as fail (ART-1 c2-c4 when c1 fails; CS-1 c4-c5 when c3 fails; RNG-1 c2-c5 when c1 fails). (c) `na_is_fail`: U1 c4 is never na (a page with no sections fails it). A missing block therefore scores 0 instead of being dropped.
- n = pass + fail checks, p = passes. If n = 0 **or** more than 50% of the checks are na, the criterion is **dropped** and its weight is redistributed proportionally (exactly 50% na is not dropped).
- **Ceiling** = 5 if p = n, else min(4, round-half-up(5 x p / n)).
- **U2** uses its own table: ceiling = min(p, 4), plus 1 when p = n and n >= 4.
- **Level rule (v2.2).** Level = max(ceiling, anchor floor). The judge's `proposed_level` is used only when it is lower **and** `downgrade_reason` names a check id of that criterion whose result is pass (the weak check, e.g. "c3: the only figure has no unit"); it never goes below the anchor floor. Otherwise `proposed_level` is ignored (a warning is logged). So all checks passing gives 5 unless the judge downgrades it, naming the weakest check, because the evidence is not exceptional. (v2.1: level = min(proposed, ceiling), which let judges choose freely between the anchor and the ceiling - the largest source of judge drift in the 60-page test run.)
- **Anchors** (U1, U3-U10, from `level_anchors`, with per-type `level_anchor_overrides`, e.g. case_study U9 has only c1-c2 so it has no level-4 anchor): if the listed checks are all pass-or-na and at least one of them passes, the level is at least 3 or 4. 4 is tested before 3. A listed check the criterion does not have is never met.
- **Caps** (`level_caps`), applied after anchors: `unless_pass` = if any listed check *fails* (na does not), cap at max; `if_all_fail` = if every listed check fails, cap at max.
- **Gate level effects** are applied last: G1 sets U8 and BLK-4 to 0; G6 and G9 cap U3 at 2; G13 caps U7 and U8 at 2.
- Judge-applied caps that are written in the rubric but not encoded (e.g. CS-6 "card grids alone reach at most 2", BLK-1/BLK-9 banner test, PDP-1 level-5 completeness) work through a downgrade (`proposed_level` + `downgrade_reason` naming the passed check the cap rests on).
- Gate level effects are logged as gate actions ("gate sets level 3 -> 0"), not as anchor overrides.

Checks where a judge note may replace a quote (`note_allowed_checks`):
{notes}

Anchors in code:
{anchors}

Caps in code:
{caps}

### 1.5 Buyer-journey stages
| Stage | Buyer mindset | Typical prompt |
|---|---|---|
| Awareness | Recognises a problem, risk or trend; no solution category or vendor in mind | "Why does my facility have power quality issues?" |
| Education | Learns how solutions and technologies work: principles, standards, terminology | "How does a Type B RCD work?" |
| Consideration | Has decided a category is needed; explores approaches and shortlists | "AC vs DC coupled PV storage" |
| Evaluation | Compares specific products/vendors against requirements: specs, compliance, proof, TCO | "Is [product] compatible with Modbus TCP?" |
| Decision | Ready to specify, buy or install: availability, pricing logic, documents, support | "[ref] lead time", "replacement for [legacy ref]" |

The user's declared stage is always used (override). Otherwise the judge applies the type's **stage test** (given in each type section: decision rules in order, first match wins, with examples) and labels the stage *inferred*; the default is used only when no rule matches. ESG pages always use Evaluation (rule R10). The engine accepts only these 5 stages (Post-purchase is scored as Decision).

Stage multipliers by criterion family (from `weights.json`):
{mult}

Family membership:
{fams}

Effective weight = default weight x multiplier(stage, family), then all weights of the type are rescaled to sum to 100 (rounded to 2 decimals per criterion, so a column can sum to about 99.97-100.03).

### 1.6 Universal criteria U1-U10 (framework wording)
Each type uses a subset with its own weights; type sections add type-specific rules. U4 c2 thresholds per type: {fd}. U9 c4 cadence: FAQ 90-120 days, blogs at least yearly, documents twice a year, competitive pages quarterly, general content every 6-12 months.
{ucrit}

### 1.7 Gates G1-G13
G1 needs a *material* contradiction and G13 a count of substantive factual statements (judge rules 12-13). Gates are triggered by the judge in the JSON; the calculator applies the cap and level effects of **any** triggered gate in `weights.json` (it does not check which types a gate is meant for, so the "applies to" column is a judging rule).
{gates}

### 1.8 Penalties
Subtracted from the raw score; total capped at {pcap} points, except `hidden_instructions`, which always takes at least 10.
{pens}

### 1.9 Judge rules
1. Evaluate citation-readiness of content only; ignore technical SEO.
2. Judge only the content provided; no outside knowledge about the brand or what the site "probably" has elsewhere.
3. Missing evidence = fail. If you cannot quote it, it fails.
4. For every pass of a presence check quote the shortest verbatim span (max 40 words, `evidence_type: "quote"`); for a fail write NOT FOUND or quote the offending span. Quotes are verified as substrings of the content; a quote that is not found turns the check into a fail. Absence/layout checks (section 1.4 list: e.g. U3 c3 paragraph length, U3 c5 nothing only in images, U8 c3 no contradictions, U10 c1/c2 stage and language fit) may pass on a judge note (`evidence_type: "note"`).
5. Write the evidence and rationale first. The calculator sets the level; the judge only downgrades, naming the weak passed check.
6. Length is not quality; formatting without facts does not pass factual checks; promotional adjectives are never evidence.
7. Numbers count only if relevant, specific and verifiable (unit, condition or source).
8. Use the anchors exactly; level 5 needs exceptional evidence; when torn, pick the lower level / fail.
9. Never see or use a previous score for the same page; temperature 0; borderline scores get 3 runs and the median.
10. Mark na only when the format makes a check impossible; na is never a pass. **A missing block is not an impossible format: its checks fail** (ART-1 c2-c4 with no takeaways; CS-1 c4-c5 with no summary; RNG-1 c2-c5 with no table; U1 c4 with no sections). Tag every failed check [T] (template/CMS) or [A] (author).
11. **Hidden or duplicated content is counted once.** Key facts that exist only in a collapsed tab/accordion/carousel/hidden panel fail U3 c5 and nothing else (tab text counts as page text for every other check, including the type criteria, and is a text equivalent for G6). The same section or card rendered twice (visible or hidden, e.g. the second truncated abstract on SE white-paper pages, cloned carousel slides, double-rendered range cards) is the `template_artifact` penalty only - not WP-1 c1, RNG-9 c4 or U3 c4.
12. **G1 needs a material contradiction**: conflicting values for a figure, spec/rating, date, scope or claim a buyer would rely on. Wording or naming variation, rounding, a mislabelled card whose facts are right and page-vs-file version mismatches are not G1 (judge them under U8 c3 / DOC-7). Widget or runtime output errors ("#VALUE!", "reduce 80% to 100%") are `template_artifact`, never G1.
13. **G13, G2 and G6 on thin and download pages.** A substantive factual statement is specific and checkable (number with unit or date, named standard, named customer/product with what it does, named finding); general assertions, slogans and metadata do not count. Fewer than 3 in the abstract plus findings of an abstract-only gateway -> G13. A download/gateway page that names the document and subject but gives no findings or KPIs -> G6 (not G2); G2 only when the page never says what the document is about.
14. **Unjudgeable checks are na unless metadata is supplied**: tagged PDF, bookmarks/outline, text layer on every page, accurate cross-references (DOC-4 c1/c2 and ESG-5 c2/c5 in esg_report_doc).
15. **Currency is judged from the page only**: "current edition", superseded standards/editions and `superseded_no_notice` use only what the supplied content states (superseded notice, later edition listed on the page or supplied hub text, dates); never outside knowledge.
"""

APPENDIX = """
## Appendix A. How to choose the page type (decision tree)

Work down the list and take the first match. If the declared type conflicts with the content, score with the declared logic, then flag the mismatch and give the score under the better-fitting type.

1. **Is it a PDF or the text of a PDF?** White paper -> `whitepaper_doc` (and score its HTML page with `whitepaper_gateway`). Sustainability/ESG report -> `esg_report_doc` (and `esg_report` for the gateway; a bare PDF URL gets the gateway logic with every HTML check failing). Datasheet -> `datasheet`. Catalog, guide, manual -> `document`.
2. **Document download / landing page?** White paper or technical guide -> `whitepaper_gateway`. One ESG report -> `esg_report`. Report library / sustainability hub -> `esg_hub`.
3. **Video asset** (YouTube + embed) -> `video`.
4. **Reusable module under ~150 words** (object description, banner, benefit block) -> `caas`.
5. **SKU/reference + spec table** -> `pdp`.
6. **Several variants of one named family** -> `range` (master ranges included). Members are the variants or sub-ranges of the named family; accessory, battery, software/app and service cards on the page are **not** members (judge them under RNG-5; they fail RNG-9 c5 only if unrelated to the range).
7. **Several families/types under a generic noun** -> `category`.
8. **Software?** 3+ cards for **distinct, separately named software products** -> `software_hub` (capability tiles or modules of one platform are not products: one platform with module tiles -> `software_product`); sign-up/download/licence action is the main content -> `software_trial`; otherwise -> `software_product`. Software types have no U5 by design: the U5 evidence checks are scored inside SW-6 (proof, attributed statistics, third-party validation with year), SW-4 c2 and SW-2 c1 (standards and certifications by number); adding U5 would double-count them and require re-weighting.
9. **Service offer?** Recurring (maintenance, monitoring, managed) -> `service`; one-off (modernization, retrofit, consulting) -> `service_project`. **Mixed offers:** classify by the offer named in the H1; if the H1 names both, by the first deliverable listed in the H1/intro (e.g. "design, configuration and implementation services with maintenance" -> `service_project`). Cross-sells ("Combine with EcoCare membership") are ignored.
10. **Primary element is an interactive tool computing outputs from inputs** -> `calculator`.
11. **Named customer + results** -> `case_study`.
12. **Dated corporate announcement with dateline, spokesperson quotes, media contact** -> `news`.
13. **Two or more options side by side, or "how to choose"** -> `comparison`.
14. **Q&A pairs are the main content** -> `faq`.
15. **Defines one term** -> `glossary`.
16. **Industry/segment problem + architecture of offers** -> `solution`.
17. **Dated narrative, opinion or explainer** -> `article`.
18. **Otherwise** -> `editorial`.

**Boundary rules that apply inside the types (v2.2):**
- **"Title/H1"** in CS-1 c1/c2 means the visible H1 **or** the HTML `<title>`; either passes. ART-2 c2/c5 judge the `<title>` and meta explicitly. **G5** concerns the visible H1 (and deck) only; an unfulfilled promise that is only in the `<title>`/meta fails ART-2 c5 (or U1 c2), not G5.
- **A bare "free"** ("free trial", "free download") counts as a trial term (cost) for **G11**, so G11 does not fire; SW-5 c3 still needs at least 2 trial terms.
- **SW-3 c1** counts only statements about where the software itself runs, not the customer's infrastructure.
- **Software hubs (SW-1):** a check passes when at least half of the product cards meet it.
"""


def table(rows, head):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def ucrit_md():
    out = []
    for cid, (name, checks) in C.U.items():
        out.append(f"\n**{cid} - {name}**")
        for i, c in enumerate(checks, 1):
            c = c.replace("{fd}", "the type's threshold (1.0 or 2.0)").replace("{cadence}", "cadence below").replace("{expected}", "per type")
            out.append(f"- c{i} {c}")
    return "\n".join(out)


def gates_md():
    rows = []
    for g, d in W["gates"].items():
        applies = ", ".join(C.GATE_TYPES[g]) if g in C.GATE_TYPES else "all types"
        eff = []
        if d.get("zero"): eff.append(" and ".join(f"{z} = 0" for z in d["zero"]))
        if d.get("max_level"): eff.append(", ".join(f"{k} max {v}" for k, v in d["max_level"].items()))
        eff.append("no cap" if d["cap"] >= 100 else f"score max {d['cap']}")
        rows.append((g, esc(d["desc"]), "; ".join(eff), applies))
    return table(rows, ["Gate", "Trigger", "Effect (in code)", "Applies to"])


PEN_DESC = {"keyword_stuffing": "Keyword or question stuffing", "fluff_density": "Superlative/fluff density > 1.5 per 100 words of body text",
            "boilerplate": "> 40% of text shared with sibling pages", "cta_overload": ">= 3 vague CTAs (\"Learn more\", \"Read more\")",
            "self_ranking": "Self-ranking \"best X\" with own brand #1 and no transparent criteria", "hidden_instructions": "Hidden or LLM-directed instructions (and flag)",
            "template_artifact": "Live placeholder text (\"ZZ_\", lorem ipsum), a whole section or card rendered twice (visible or hidden; the single place duplicates are penalised), or a widget/runtime output error (\"#VALUE!\")",
            "superseded_no_notice": "Older edition with no link to or label for the newer one, judged only from what the supplied content shows"}


def type_section(key, pil, kap):
    m = C.META[key]
    crit = criteria_for(key)
    ew = eff_weights(key)
    L = [f"\n### `{key}` - {m['label']}\n", f"*Source logic: {m['src']}. Prompt: `prompts/copilot_prompt_{key}_v2.2.txt`.*\n"]
    L.append(f"**When to use this key:** {m['when']}\n")
    L.append(f"**What AI extracts from such pages:** {m['extracts']}\n")
    L.append(f"**Stage:** natural stages - {m['natural']} A stage supplied by the business/user always overrides. **Stage test (first match wins):** {m['stage_rule']} Default when no rule matches: **{m['default']}**.\n")
    if m.get("extra"):
        L.append(f"**Type rules:** {m['extra']}\n")
    L.append(f"**U4 c2 fact-density threshold:** {fact_density(key):.1f} per 100 words. **U9 c4 cadence:** {C.CADENCE.get(key, C.DEFAULT_CADENCE)}.\n")
    L.append("**Criteria (base weights sum to 100; checks as used in the prompt):**\n")
    rows = []
    for cid, name, checks, src, rule, w, fam in crit:
        ch = "<br>".join(f"c{i} {esc(c)}" for i, c in enumerate(checks, 1))
        if rule:
            ch += f"<br>*Rule: {esc(rule)}*"
        rows.append((cid, esc(name), w, FAM_LABEL[fam], ch, SRC_NAMES.get(src, src)))
    L.append(table(rows, ["ID", "Criterion", "Base W", "Family", "Checks", "Check source"]))
    L.append(f"\n\n**Effective weights by stage** (computed with `geo_score_calc.compute()`; all criteria present):\n")
    order = sorted([c[0] for c in crit], key=lambda c: -ew[m["default"]][c])
    rows = [(cid, *[f"{ew[s][cid]:.2f}" for s in STAGES]) for cid in order]
    rows.append(("**Sum**", *[f"{sum(ew[s].values()):.2f}" for s in STAGES]))
    L.append(table(rows, ["Criterion"] + STAGES))
    gs = gates_for(key)
    L.append(f"\n\n**Gates that apply:** " + "; ".join(f"{g} ({'no cap' if W['gates'][g]['cap'] >= 100 else 'max ' + str(W['gates'][g]['cap'])})" for g in gs) + ".")
    caps = [f"{cid}: {', '.join(('cap ' + str(c['max']) + ' unless ' + '+'.join(c['unless_pass']) + ' pass') if 'unless_pass' in c else ('cap ' + str(c['max']) + ' if ' + '+'.join(c['if_all_fail']) + ' all fail') for c in W['level_caps'][cid])}"
            for cid in W["page_types"][key] if cid in W["level_caps"]]
    anch = [cid for cid in W["page_types"][key] if cid in W["level_anchors"]]
    bf = block_fail_for(key)
    nc = note_checks_for(key)
    L.append(f"\n\n**Anchors in code for this type:** {'; '.join(anchors_for(key)) if anch else 'none'}. **Caps in code:** {'; '.join(caps) if caps else 'none'}.")
    L.append(f" **Missing block = fail:** {'; '.join(bf) if bf else 'general rule only (a missing block fails its checks)'}. **Judge note allowed on:** {'; '.join(f'{c} {chr(44).join(cs)}' for c, cs in nc) if nc else 'none'}.")
    jr = [f"{cid}: {r}" for cid, _, _, _, r, _, _ in crit if r and cid not in W["level_caps"] and ("<=" in r or "at most level" in r or "Level 5" in r or "level 5" in r)]
    if jr:
        L.append(f" **Judge-applied caps (not in code):** {' | '.join(esc(x) for x in jr)}.")
    L.append(f"\n\n**Common SE failures:** {m['failures']}\n")
    p = pil.get(key, [])
    if p:
        sc = [int(r["GEO score (final, v2.1)"]) for r in p]
        gaps = Counter(g.split(" (")[0].strip() for r in p for g in r["Top 3 gaps (recoverable pts)"].split(";") if g.strip())
        gates = Counter(g.strip() for r in p for g in r["Gates"].split(",") if g.strip())
        pairs = [(int(r["Judge A"]), int(r["Judge B (blind)"])) for r in p if r["Judge B (blind)"].strip()]
        agree = f"{len(pairs)} pages double-judged, mean |A-B| = {statistics.mean(abs(a - b) for a, b in pairs):.1f} points" if pairs else "not double-judged"
        if key in (kap.get("wkappa_by_type") or {}):
            agree += f", criterion-level weighted kappa {kap['wkappa_by_type'][key]}"
        L.append(f"**Pilot results (SE inventory, Oct 2026, Judge A final):** n = {len(sc)}, median {statistics.median(sc):g}, range {min(sc)}-{max(sc)}; "
                 f"pages: {', '.join(r['ID'] + '=' + r['GEO score (final, v2.1)'] for r in p)}. Stages used: {', '.join(sorted(set(r['Stage'] for r in p)))}. "
                 f"Most frequent top gaps: {', '.join(f'{k} ({v}x)' for k, v in gaps.most_common(4))}. Gates triggered: {', '.join(f'{k} ({v}x)' for k, v in gates.most_common()) or 'none'}. Judge agreement: {agree}.\n")
    else:
        L.append("**Pilot results: UNTESTED** - no SE page of this type was scored in the Oct 2026 pilot. Weights and checks are evidence-informed starting points; calibrate before relying on the score.\n")
    return "\n".join(L)


def main():
    pil, kap = pilots(), kappa()
    fams = "\n".join(f"- **{FAM_LABEL[f]}** (`{f}`): {', '.join(ids)}" for f, ids in W["families"].items()) + "\n- **Stage-neutral** (multiplier 1.0): every other criterion (e.g. U3, U8, ART-2, NEWS-6, SOL-4, SVC-6, CS-2/4/6, DOC-1/2/4/5/6/9, BLK-1..5/7/9, FAQ-*, VID-*, ESG-5)."
    mult = table([(FAM_LABEL[f], *[W["stage_multipliers"][s][f] for s in STAGES]) for f in W["families"]] + [("Stage-neutral (other)", *["1.0"] * 5)], ["Family"] + STAGES)
    bands = table([(f">= {lo}", name) for lo, name in W["bands"]], ["Final score", "Band"])
    anchors = table([(cid, "+".join(a["3"]) if isinstance(a["3"], list) else f"any {a['3']['any']}", "+".join(a["4"]) if isinstance(a["4"], list) else f"any {a['4']['any']} passing checks")
                     for cid, a in W["level_anchors"].items() if not cid.startswith("_")], ["Criterion", "Level >= 3 when", "Level >= 4 when"])
    caps = table([(cid, c["max"], ("any of " + ", ".join(c["unless_pass"]) + " fails") if "unless_pass" in c else ("all of " + ", ".join(c["if_all_fail"]) + " fail"), esc(c["why"]))
                  for cid, cl in W["level_caps"].items() if not cid.startswith("_") for c in cl], ["Criterion", "Max level", "When", "Why"])
    fd = ", ".join(f"{k} {v}" for k, v in W["fact_density_threshold_per_100w"].items())
    notes = table([(cid, ", ".join(cs)) for cid, cs in W["note_allowed_checks"].items() if not cid.startswith("_")], ["Criterion", "Checks (absence/layout)"])
    pens = table([(p, esc(PEN_DESC[p]), f"-{v}") for p, v in W["penalties"].items()], ["Penalty id", "Signal", "Deduction"])
    doc = [f"# SE Content GEO Scoring Standard v2.2 - All Page Types\n",
           f"*Generated by `build_docs.py` from `engine/weights.json` {W['version']} and `engine/geo_score_calc.py` (v2.2); do not edit tables by hand. {len(KEYS)} page-type keys documented. Changes from v2.1: see `CHANGELOG-v2.2.md`. Pilot statistics below are the v2.1 pilot (Oct 2026) as published.*\n",
           "Contents: 1 Overview (method, bands, levels, stages, U1-U10, gates, penalties, judge rules) - 2 Page types (10 inventory types, then the other types) - Appendix A decision tree - Appendix B validation status - Appendix C source gaps.\n",
           OVERVIEW.format(bands=bands, ok=W["ok_threshold"], notes=notes, anchors=anchors, caps=caps, mult=mult, fams=fams, fd=fd, ucrit=ucrit_md(), gates=gates_md(), pcap=W["penalty_cap"], pens=pens),
           "\n## 2. Page types\n"]
    for title, ks in C.GROUPS:
        doc.append(f"\n## 2.{C.GROUPS.index((title, ks)) + 1} {title}\n")
        for k in ks:
            doc.append(type_section(k, pil, kap))
    doc.append(APPENDIX)
    rows = []
    for k in KEYS:
        p = pil.get(k, [])
        pairs = [r for r in p if r["Judge B (blind)"].strip()]
        der = sum(1 for c in criteria_for(k) if "DER" in c[3])
        rows.append((f"`{k}`", "yes" if p else "**no**", len(p), f"{len(pairs)} paired" + (f", wkappa {kap['wkappa_by_type'][k]}" if k in (kap.get('wkappa_by_type') or {}) else "") if pairs else "none",
                     "yes" if p else "n/a", der))
    doc.append("\n## Appendix B. Validation status\n")
    doc.append(table(rows, ["Key", "Tested on SE pages", "Pilot n", "Judge agreement (A vs blind B)", "Calculator reproduces pilot scores", "Criteria with derived checks"]))
    s = kap
    doc.append(f"\n\nOverall (13 paired pages): mean |A-B| {s.get('mean_abs_diff')} points (Judge A stricter... A minus B = +{s.get('mean_signed_diff_A_minus_B')}), Pearson r {s.get('pearson_r')}, band agreement {s.get('band_agreement')}, check-level agreement {s.get('check_level_agreement')}, criterion-level weighted kappa {s.get('criterion_level_wkappa_overall')}. Low-kappa criteria: U2 0.18, U8 0.32, U10 0.49, U7 0.52, U1 0.57. Calculator reproduction: see `verification_report.md` (all 60 pilot judge files reproduce the CSV score).\n".replace("(Judge A stricter... A minus B", "(A minus B"))
    doc.append(open(os.path.join(ROOT, "source_gaps.md"), encoding="utf-8").read())
    open(os.path.join(ROOT, "GEO_Scoring_Standard_All_Types_v2.2.md"), "w", encoding="utf-8").write("\n".join(doc))
    print("wrote GEO_Scoring_Standard_All_Types_v2.2.md")


if __name__ == "__main__":
    main()

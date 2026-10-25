#!/usr/bin/env python3
"""Builds tests/0N_seo_judge.json from (a) seo_extract.py computed checks and (b) the human/AI
judge's verdicts on the judged checks, written below with verbatim quotes.

Judge: Claude (strict mode), 2026-10-23. Inputs: corpus .md + live HTML fetched 2026-10-23 (tests/html).
A judged entry may OVERRIDE a computed one only with a written reason (marked 'override:').
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
P, F, NA = "pass", "fail", "na"

ELIG = [
    {"id": "E1", "result": P, "evidence": "curl 2026-10-23: HTTP/2 200, 0 redirects"},
    {"id": "E2", "result": P, "evidence": "meta robots 'index, follow, max-image-preview:large, max-snippet:-1'; no X-Robots-Tag header; robots.txt has no Disallow matching the post path"},
    {"id": "E3", "result": None, "evidence": None},  # from extractor
    {"id": "E4", "result": NA, "evidence": "no hreflang tags (blog is single-language en)"},
    {"id": "E5", "result": P, "evidence": "https; http://blog.se.com/ returns 301 to https"},
    {"id": "E6", "result": P, "evidence": "viewport 'width=device-width, initial-scale=1'; mobile content parity not rendered (unverified)"},
    {"id": "E7", "result": P, "evidence": "max-snippet:-1, no nosnippet/noarchive"},
    {"id": "E8", "result": None, "evidence": None},
]

# Judged checks per page: {criterion: {check: (result, evidence)}}, plus proposed levels, gates, penalties.
J = {
 1: {"keyword": "modular data center",
   "S1": {"c1": (F, "H1 'Modular, prefabricated data centers enter the AI era and boldly go where no data centers have gone before' - second half is a slogan, not searcher language"),
          "c2": (F, "First 150 words defer the answer: 'But why the need for prefabrication in AI data centers? Let’s take a look.'"),
          "c3": (P, "Explainer format with sections 'Challenges of the AI era', 'Power Capacity and Scale', 'High Density Liquid Cooling'"),
          "c4": (P, "Title promise (prefab in the AI era) delivered: 'prefabrication is a necessity today'"),
          "c5": (P, "No product pitch section; product links are contextual ('AI factory modular IT Pod')")},
   "S3": {"c3": (P, "Meta summarises the page thesis: 'prefabrication is a necessity today' (but is the closing paragraph copied, 414 chars)")},
   "S4": {"c5": (F, "Slug carries the slogan and repeats 'data-centers': '...-boldly-go-where-no-data-centers-have-gone-before'")},
   "S5": {"c3": (P, "4 of 5 H2s descriptive ('Power Capacity and Scale', 'High Density Liquid Cooling'); 'A slow start' is not")},
   "S7": {"c1": (P, "Covers why AI needs prefab, which systems (UPS/switchgear skids, IT Pod), how it is deployed; costs/limits not covered"),
          "c2": (F, "'CDUs' used without expansion: 'manifolds, hot and cold liquid plumbing to the servers, and the CDUs'"),
          "c3": (P, "'AMD Helios 445 racks running at 246 kW per rack and the NVIDIA Vera Rubin running at 227 kW per rack'"),
          "c4": (P, "Single topic: prefabrication for AI data centers"),
          "c5": (P, "No padding to a length target; 895 words")},
   "S8": {"c1": (P, "Byline 'Steven Carlini'"),
          "c2": (None, None),
          "c3": (P, "'I have been strategically involved in the modular data center industry for over 30 years'"),
          "c4": (F, "Statistics unsourced: 'AI factory campuses can be up to 10 gigawatts'; 'close to 250 kW vs 10-20' - no source named or linked"),
          "c5": (P, "No checkable error or internal contradiction found")},
   "S9": {"c1": (F, "Experience is asserted ('over 30 years') but no first-hand observation with a specific detail"),
          "c2": (F, "NOT FOUND: no Schneider first-party data, test or deployment"),
          "c3": (P, "Specific analysis: 'the power and cooling components sit above the AI racks in an overhead metal superstructure'"),
          "c4": (F, "Only image is stock: GettyImages-1337227407_resized-1024x538.jpg"),
          "c5": (P, "Original column; 'A condensed version of this article appeared in Forbes.' (syndication disclosed)")},
   "S10": {"c5": (P, "Racks cited are current (AMD Helios, NVIDIA Vera Rubin); no stale year")},
   "S11": {"c2": (P, "Links to the AI factory solution page and AI factory ebook: 'AI factory data centers' -> se.com/ww/en/work/solutions/ai-factory/")},
   "S12": {"c1": (F, "Page has statistics but the only outbound link is the author's own Forbes column, not a primary source"),
           "c3": (P, "Forbes link is relevant (condensed version of this article)")},
   "S13": {"c2": (NA, "no non-empty alt to judge"), "c4": (F, "Single stock hero; the IT Pod architecture described in text has no diagram")},
   "levels": {"S1": 2, "S2": 4, "S3": 4, "S4": 3, "S5": 4, "S6": 4, "S7": 4, "S8": 4, "S9": 2, "S10": 4, "S11": 3, "S12": 3, "S13": 0, "S14": 5},
   "gates": {}, "penalties": {}},
 2: {"keyword": "data center community opposition",
   "S1": {"c1": (P, "H1 'Data center community opposition: How cooling design affects water, noise, and permitting'"),
          "c2": (P, "Summary bullet 1: 'cooling is one of the technical decisions that directly affects water and acoustic impacts'"),
          "c3": (P, "Explainer with question H2 'Why are communities so opposed to data centers?'"),
          "c4": (P, "Water ('Water use depends on the full heat-rejection path'), noise ('Mitigating ... with cooling architecture') and permitting sections all present"),
          "c5": (P, "Product mention confined to the close: 'Schneider Electric’s comprehensive, end-to-end liquid cooling portfolio'")},
   "S3": {"c3": (P, "'Data center community opposition is putting water use, noise, and permitting under greater scrutiny across the US.'")},
   "S4": {"c5": (P, "Slug mirrors the title wording, correctly spelt")},
   "S5": {"c3": (P, "All 6 H2s descriptive, e.g. 'Carry permitting assumptions into specifications and commissioning'")},
   "S7": {"c1": (P, "Covers why opposition arises, permitting pathways, water, noise, commissioning handoff"),
          "c2": (P, "'Coolant Distribution Unit (CDU)', 'Heat Dissipation Units (HDUs)', 'Rear-door heat exchangers (RDHx)'"),
          "c3": (P, "'reduce cooling energy use by up to 60% and water use by up to 60%'; 'added C-weighted limits for steady tonal equipment sound'"),
          "c4": (P, "One topic: cooling design and local approval"),
          "c5": (P, "Dense, no filler; 1,418 words matched to a multi-part question")},
   "S8": {"c1": (P, "'Author: Andrew Whitmore, VP of Sales of Motivair, Motivair by Schneider Electric'"),
          "c2": (F, "override: byline link is 'Guest Blogger' -> /author/guest-blogger/, not the named author's bio"),
          "c3": (P, "'VP of Sales of Motivair'"),
          "c4": (P, "'In a March 2026 Gallup survey' (linked news.gallup.com); 'Schneider Electric White Paper 211'"),
          "c5": (P, "Claims hedged and consistent: 'These are local examples, rather than national requirements.'")},
   "S9": {"c1": (F, "NOT FOUND: no first-hand project experience"),
          "c2": (P, "'Schneider Electric White Paper 211 reports that direct-to-chip liquid cooling can reduce cooling energy use by up to 60%'"),
          "c3": (P, "Framework: 'follow the complete heat path from the CPU or GPU and cold plate, through the Coolant Distribution Unit (CDU) and facility loop'"),
          "c4": (F, "Only image is stock: GettyImages-2247595118_SDL-1920x1080-1-1024x576.jpg"),
          "c5": (P, "Original synthesis with local examples (Prince William County, Fairfax County)")},
   "S10": {"c4": (F, "dateModified 2026-10-16 is 8 days after publication; no visible 'Updated' label"),
           "c5": (P, "'March 2026 Gallup survey' is current")},
   "S11": {"c2": (P, "'Liquid Cooling solutions' -> se.com/us/en/work/solutions/data-centers-and-networks/liquid-cooling hub")},
   "S12": {"c1": (P, "'March 2026 Gallup survey' -> news.gallup.com; 'added C-weighted limits' -> pwcva.gov/noise"),
           "c3": (P, "Government and polling sources relevant to each claim")},
   "S13": {"c2": (NA, "no non-empty alt"), "c4": (F, "Single stock image; no heat-path diagram")},
   "S14": {"c3": (F, "override: markup author 'Guest Blogger' does not match the named author 'Andrew Whitmore' shown in the text")},
   "levels": {"S1": 4, "S2": 4, "S3": 4, "S4": 4, "S5": 4, "S6": 4, "S7": 4, "S8": 4, "S9": 3, "S10": 4, "S11": 4, "S12": 5, "S13": 0, "S14": 3},
   "gates": {}, "penalties": {}},
 3: {"keyword": "AI infrastructure deployment",
   "S1": {"c1": (P, "Title '3 operational priorities for successful AI infrastructure deployment' names the topic"),
          "c2": (P, "'meeting AI demand comes down to turning opportunity into operational capacity. Is there a credible path to power?'"),
          "c3": (P, "Question H2s, e.g. 'How does prefab help operators build at scale?'"),
          "c4": (F, "Title promises '3 operational priorities' and meta 'power, infrastructure capacity, and workforce'; body has no 3-priority structure and no workforce section"),
          "c5": (P, "One closing SE section: 'How does Schneider Electric support repeatable AI infrastructure deployment?'")},
   "S3": {"c3": (F, "Meta promises 'three operational priorities—power, infrastructure capacity, and workforce' which the page does not deliver as structure")},
   "S4": {"c5": (P, "Slug matches the title, correctly spelt")},
   "S5": {"c3": (P, "All 5 H2s descriptive questions, e.g. 'How do fungible designs keep AI projects moving?'")},
   "S7": {"c1": (F, "Power path, workforce and schedule risk are raised as questions but not answered in sections"),
          "c2": (F, "'fungible designs' and 'e-house' used without definition"),
          "c3": (F, "Only one specific: 'I see customers building 50 MW a year'"),
          "c4": (P, "One topic: executing AI infrastructure deployment"),
          "c5": (P, "649 words; no padding")},
   "S8": {"c1": (P, "Byline 'Gary Lamora'"), "c2": (None, None),
          "c3": (F, "NOT FOUND: no role or credential visible on the article"),
          "c4": (P, "'expected to triple by 2030' linked to mckinsey.com"),
          "c5": (P, "No checkable error found")},
   "S9": {"c1": (P, "'I see customers building 50 MW a year and others building ten or twenty times that.'"),
          "c2": (F, "NOT FOUND: no first-party data"),
          "c3": (P, "Typology: 'The fully committed', 'The pragmatists', 'The reactives'"),
          "c4": (F, "Photo only (Background-1024x443.png); no original diagram"),
          "c5": (P, "Original opinion piece")},
   "S10": {"c4": (F, "dateModified 2026-10-16 is 10 days after publication; no visible 'Updated' label"),
           "c5": (P, "No stale facts")},
   "S11": {"c2": (P, "'prefabricated modular data center' -> se.com/ww/en/work/solutions/ai-factory/prefab/")},
   "S12": {"c1": (P, "'expected to triple by 2030' -> mckinsey.com"), "c3": (P, "McKinsey research is relevant and reputable")},
   "S13": {"c2": (P, "alt 'Technician working on electrical equipment in a data center infrastructure room'"),
           "c4": (P, "Image sits after the intro and illustrates data center electrical work")},
   "levels": {"S1": 3, "S2": 3, "S3": 3, "S4": 4, "S5": 4, "S6": 5, "S7": 2, "S8": 4, "S9": 3, "S10": 4, "S11": 4, "S12": 5, "S13": 4, "S14": 5},
   "gates": {"SG4": "Title '3 operational priorities...' and meta 'power, infrastructure capacity, and workforce' not delivered; H1 is a different headline 'Demand is easy. Execution is hard.'"},
   "penalties": {}},
 4: {"keyword": "AI infrastructure planning",
   "S1": {"c1": (P, "Title 'Leaders need a new strategy for AI infrastructure planning' (H1 is a slogan: 'AI is moving faster than infrastructure.')"),
          "c2": (P, "'Today, AI-enabled racks can exceed 100 kilowatts... The bigger issue is time.'"),
          "c3": (P, "Opinion/explainer with an action list 'Three questions every infrastructure leader should ask this week'"),
          "c4": (P, "'new strategy' delivered: 'Designing for a multi-generation AI future'"),
          "c5": (P, "No product pitch; soft close only")},
   "S3": {"c3": (P, "'Learn how power, cooling, and facility strategies can adapt to support changing enterprise AI demands.'")},
   "S4": {"c5": (F, "Slug misspelt: 'ai-infrastucture-planning' (missing r)")},
   "S5": {"c3": (P, "All 5 H2s descriptive; Table of Contents present")},
   "S7": {"c1": (P, "Covers why planning breaks, physical constraints (density, cooling, weight), multi-generation strategy, what to ask"),
          "c2": (P, "Terms explained in context ('liquid cooling ... plumbing, leak detection')"),
          "c3": (P, "'Building a new data center typically takes 12 to 18 months'; 'removes 80% to 90% of a chip’s heat'"),
          "c4": (P, "One topic"), "c5": (P, "No padding")},
   "S8": {"c1": (P, "Byline 'Aaron Dudley'"), "c2": (None, None),
          "c3": (F, "NOT FOUND: no role or credential on the article"),
          "c4": (P, "'exceed 100 kilowatts' linked to iaeimagazine.org; '12 to 18 months' linked"),
          "c5": (P, "No checkable error found")},
   "S9": {"c1": (F, "NOT FOUND: no first-hand observation"),
          "c2": (F, "NOT FOUND: no first-party data"),
          "c3": (P, "Decision aid: 'What is your actual rack density ceiling today?'"),
          "c4": (F, "Stock image AdobeStock_1725140750-copy.jpeg"),
          "c5": (P, "Original editorial")},
   "S10": {"c4": (F, "dateModified 2026-10-16 is 14 days after publication; no visible 'Updated' label"),
           "c5": (P, "No stale facts")},
   "S11": {"c2": (P, "'AI infrastructure investment' -> se.com/ww/en/work/solutions/data-centers-and-networks/")},
   "S12": {"c1": (P, "Claims linked: iaeimagazine.org, datacenterknowledge.com, nvidianews.nvidia.com"),
           "c3": (P, "Sources relevant; some are vendor/trade blogs (ingenious.build) rather than primary")},
   "S13": {"c2": (F, "alt 'AI Infrastructure' does not describe the image"), "c4": (F, "Generic stock image, not explanatory")},
   "levels": {"S1": 4, "S2": 3, "S3": 4, "S4": 4, "S5": 4, "S6": 4, "S7": 4, "S8": 4, "S9": 2, "S10": 4, "S11": 4, "S12": 5, "S13": 1, "S14": 5},
   "gates": {}, "penalties": {}},
 5: {"keyword": "data centre water recycling",
   "S1": {"c1": (P, "H1 'Using treated and recycled water in Indian data centre cooling'"),
          "c2": (P, "'A stronger approach is to reduce consumptive water demand first, then use appropriately treated and recycled water'"),
          "c3": (P, "How-to/explainer with a step list 'Reduce consumptive water demand ... Measure both water consumption and water source'"),
          "c4": (P, "Treated/recycled water sources and Indian context both delivered"),
          "c5": (P, "Product mention confined to 'Design the complete cooling and water path'")},
   "S3": {"c3": (P, "'Discover how data centre water recycling and closed-loop liquid cooling can help Indian data centres reduce freshwater use'")},
   "S4": {"c5": (P, "Slug matches title, en-IN spelling consistent ('centre')")},
   "S5": {"c3": (P, "All H2/H3 descriptive, e.g. 'Recycled water has to be engineered for the cooling system'")},
   "S7": {"c1": (P, "Why water constrains, liquid vs consumption, sources, treatment, policy, metrics, design path"),
          "c2": (P, "'Water Usage Effectiveness (WUE) measures...'; 'zero liquid discharge (ZLD)'"),
          "c3": (P, "'recirculate more than 95% of its coolant'; 'more than 5,000 litres per day'"),
          "c4": (P, "One topic"), "c5": (P, "No padding")},
   "S8": {"c1": (P, "'Author: Anuj Kudesia, Managing Director SEPSL & Direct BD'"),
          "c2": (F, "override: byline link is 'Guest Blogger' -> /author/guest-blogger/"),
          "c3": (P, "'Managing Director SEPSL & Direct BD'"),
          "c4": (P, "'only 4% of its freshwater resources' -> worldbank.org; 'The Bureau of Energy Efficiency’s 2023 District Cooling Guidelines'"),
          "c5": (P, "No checkable error found")},
   "S9": {"c1": (F, "NOT FOUND: no first-hand project detail"),
          "c2": (F, "NOT FOUND: no SE first-party data"),
          "c3": (P, "Decision rule: 'Reduce consumptive demand first, then determine how much of the remaining requirement can be supplied'"),
          "c4": (F, "Stock image AdobeStock_428397714_resized-1024x538.jpg"),
          "c5": (P, "Original synthesis for India")},
   "S10": {"c5": (P, "2025 rules and 2023 guidelines cited as current with dates")},
   "S11": {"c2": (P, "'Liquid Cooling Hub' -> se.com/in/en/work/solutions/.../liquid-cooling")},
   "S12": {"c1": (P, "worldbank.org, aeee.in, rajasthan.gov.in sources"), "c3": (P, "Relevant; some news sources (etvbharat) are secondary")},
   "S13": {"c2": (P, "alt 'Waste water treatment plant.'"), "c4": (P, "Placed beside 'Treated municipal wastewater is one increasingly relevant alternative'")},
   "S14": {"c3": (F, "override: markup author 'Guest Blogger' does not match the named author 'Anuj Kudesia'")},
   "levels": {"S1": 4, "S2": 3, "S3": 5, "S4": 4, "S5": 4, "S6": 5, "S7": 4, "S8": 4, "S9": 2, "S10": 4, "S11": 4, "S12": 5, "S13": 4, "S14": 3},
   "gates": {}, "penalties": {}},
 6: {"keyword": "AI infrastructure Europe",
   "S1": {"c1": (P, "Title 'AI infrastructure in Europe: Why the next decade offers a leadership opportunity'"),
          "c2": (F, "First 150 words are personal context ('After 30 years at Schneider Electric...'); the 'why' is deferred to 'three areas stand out to me'"),
          "c3": (P, "Thought-leadership format fits an awareness query"),
          "c4": (P, "Speed, power and people sections deliver the 'why'"),
          "c5": (P, "Close offers a guide only")},
   "S3": {"c3": (P, "'how speed, power availability, talent, and innovation can position Europe as a leader'")},
   "S4": {"c5": (P, "Slug matches the H1 wording")},
   "S5": {"c3": (F, "First section has no heading: its label is run into a paragraph, 'In the AI era, speed wins I spent 20 years of my career in supply chain'; 'Looking ahead' is generic")},
   "S7": {"c1": (P, "Covers supply chain speed, power availability by market, skills"),
          "c2": (P, "Few technical terms; 'Edge computing' used plainly"),
          "c3": (F, "Few specifics: '20 or 30MW ... 500MW'; market claims ('France and the Nordics') unquantified"),
          "c4": (P, "One topic"), "c5": (P, "No padding")},
   "S8": {"c1": (P, "Byline 'Damien Dhellemmes'"), "c2": (None, None),
          "c3": (P, "'After 30 years at Schneider Electric'; image alt 'Senior Vice President, Secure Power and Data Centers, Europe'"),
          "c4": (F, "Market claims uncited: 'Markets with available and competitive power, including France and the Nordics, are attracting significant attention'"),
          "c5": (P, "No checkable error found")},
   "S9": {"c1": (P, "'I spent 20 years of my career in supply chain.'"),
          "c2": (F, "NOT FOUND: no first-party data"),
          "c3": (P, "Thesis: 'supply chain has become one of the most important competitive differentiators in the data center industry'"),
          "c4": (P, "SE graphic 'End to End AI Infrastructure Digital Twin'"),
          "c5": (P, "Original first-person piece")},
   "S10": {"c5": (P, "No stale facts")},
   "S11": {"c2": (P, "'to support AI at scale' -> se.com/ww/en/work/solutions/ai-factory/")},
   "S12": {"c1": (NA, "No third-party statistics; all links are SE"), "c3": (NA, "No outbound third-party links")},
   "S13": {"c2": (P, "alt 'End to End AI Infrastructure Digital Twin'"), "c4": (P, "Digital-twin graphic placed after the powertrain paragraph")},
   "levels": {"S1": 3, "S2": 4, "S3": 4, "S4": 4, "S5": 3, "S6": 4, "S7": 4, "S8": 4, "S9": 4, "S10": 4, "S11": 4, "S12": 5, "S13": 4, "S14": 5},
   "gates": {}, "penalties": {}},
}

CHECKS = {"S1": 5, "S2": 6, "S3": 5, "S4": 5, "S5": 4, "S6": 5, "S7": 5, "S8": 5, "S9": 5,
          "S10": 5, "S11": 5, "S12": 3, "S13": 4, "S14": 5}
GATES = ["SG1", "SG2", "SG3", "SG4", "SG5", "SG6", "SG7", "SG8"]
PENS = ["hidden_instructions", "hidden_text_or_links", "keyword_stuffing", "self_ranking", "superseded_no_notice",
        "fluff_intro", "boilerplate_dominant", "template_artifact", "ai_listed_author", "generic_anchor_overload"]
# Computed check that the extractor cannot fully decide: S8.c2 is taken from byline_links.

for i, j in J.items():
    ex = json.load(open(os.path.join(HERE, "extract", f"0{i}_extract.json"), encoding="utf-8"))
    cc, facts = ex["computed_checks"], ex["facts"]
    crit = []
    for cid, n in CHECKS.items():
        checks = []
        for k in range(1, n + 1):
            key = f"{cid}.c{k}"
            judged = j.get(cid, {}).get(f"c{k}")
            if judged and judged[0] is not None:
                res, ev = judged
                src = "judged" if key not in cc else "judged (override)"
            elif key in cc:
                res, ev, src = cc[key]["result"], cc[key]["evidence"], "computed"
            elif cid == "S8" and k == 2:
                bl = (facts.get("byline_links") or [{}])[0]
                ok = bl.get("href", "").rstrip("/").split("/")[-1] not in ("", "guest-blogger", "admin")
                res, ev, src = (P if ok else F), f"byline '{bl.get('text')}' -> {bl.get('href')}", "computed"
            elif cid == "S3" and k == 3:
                raise SystemExit(f"page {i}: S3.c3 must be judged")
            else:
                raise SystemExit(f"page {i}: no verdict for {key}")
            checks.append({"id": f"c{k}", "result": res, "evidence": ev, "source": src})
        crit.append({"id": cid, "proposed_level": j["levels"][cid], "rationale": "; ".join(
            f"{c['id']} {c['result']}" for c in checks if c["result"] == F) or "all applicable checks pass",
            "confidence": "high", "checks": checks})
    elig = []
    for e in ELIG:
        if e["result"] is None:
            ce = ex["computed_eligibility"][e["id"]]
            elig.append({"id": e["id"], "result": ce["result"], "evidence": ce["evidence"]})
        else:
            elig.append(dict(e))
    out = {"page": {"url": facts["url"]["url"], "title": facts["title"]["text"], "h1": facts["title"]["h1"],
                    "keyword": j["keyword"], "keyword_inferred": True, "judge": "Claude strict, 2026-10-23",
                    "inputs": "corpus .md + live HTML (tests/html)"},
           "criteria": crit,
           "gates": [{"id": g, "triggered": g in j["gates"], "evidence": j["gates"].get(g, "")} for g in GATES],
           "penalties": [{"id": p, "applied": p in j["penalties"], "evidence": j["penalties"].get(p, "")} for p in PENS],
           "eligibility": elig}
    with open(os.path.join(HERE, f"0{i}_seo_judge.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("wrote", f"0{i}_seo_judge.json")

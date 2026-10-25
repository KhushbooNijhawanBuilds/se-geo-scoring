"""Page types, stages, gates, penalties and criterion names for the Content GEO Score (standard v2.2, all 26 types).

Names, checks, stage tests and type metadata come from geoscore/standard_v22.py (a verbatim copy of
8-geo-v2.2/catalog.py). Weights, gates, anchors, caps and the v2.2 check rules come from engine/weights.json.
"""
import json
from pathlib import Path

from . import standard_v22 as C

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT / "engine"
STANDARD = ROOT / "standard"
PROMPTS = STANDARD / "prompts"
WEIGHTS_PATH = ENGINE / "weights.json"

STAGES = ["Awareness", "Education", "Consideration", "Evaluation", "Decision"]

# Types not yet tested on SE pages (8-geo-v2.2 README / Appendix B).
UNTESTED = {"pdp", "category", "caas", "editorial", "document", "datasheet", "comparison", "faq", "glossary", "video",
            "whitepaper_doc"}

GROUPS = C.GROUPS  # [(group label, [keys])] in the standard's order
ORDERED_KEYS = [k for _, ks in GROUPS for k in ks]

# key: (label, default stage, tested on SE pages, group label)
PAGE_TYPES = {k: (C.META[k]["label"], C.META[k].get("default", "Education"), k not in UNTESTED, g)
              for g, ks in GROUPS for k in ks}

UNIVERSAL_GATES = list(C.UNIVERSAL_GATES)
TYPE_GATES = dict(C.GATE_TYPES)

GATE_WHY = {
    "G1": "A material contradiction makes every fact on the page untrustworthy.",
    "G2": "If the main question is never answered, nothing on the page can be quoted as the answer.",
    "G3": "A product page or datasheet without specs in text gives engines nothing to cite.",
    "G4": "Unsafe technical advice is a safety and reputation risk; an expert must review it.",
    "G5": "A visible H1 that promises what the body doesn't deliver is clickbait.",
    "G6": "Engines quote text; facts locked in images, video, PDFs or gated assets are invisible to them.",
    "G7": "Dated content without a date can't be judged current; recency is a strong citation cue.",
    "G8": "A customer story without a measured result has no proof to quote.",
    "G9": "A calculator page that hides its method, assumptions and results has nothing to cite.",
    "G10": "A range page without a single rating or unit can't answer any selection question.",
    "G11": "Software pages must state at least deployment, integrations, security or licensing.",
    "G12": "A service page needs a concrete deliverable or a service level.",
    "G13": "On a page with almost no facts, 'neutral' and 'consistent' pass by default, so they are capped.",
}

PENALTY_INFO = {
    "hidden_instructions": ("Hidden AI instructions", "Text aimed at AI engines and hidden from readers. Always -10 and flagged."),
    "keyword_stuffing": ("Keyword stuffing", "The same phrases or questions repeated unnaturally."),
    "self_ranking": ("Self-ranking list", "A 'best X' list with our own brand first and no transparent criteria."),
    "superseded_no_notice": ("Superseded, no notice", "An older edition with no notice or link to the current one (judged from the supplied content only)."),
    "fluff_density": ("Fluff", "More than 1.5 superlatives per 100 words of body text."),
    "boilerplate": ("Boilerplate", "More than 40% of the text shared with sibling pages."),
    "template_artifact": ("Template artifact", "Live placeholder text, a section rendered twice, or a widget/runtime output error ('#VALUE!')."),
    "cta_overload": ("CTA overload", "3 or more vague calls to action ('Learn more', 'Read more')."),
}

UNIVERSAL_NAMES = {k: v[0] for k, v in C.U.items()}


def load_weights():
    return json.loads(WEIGHTS_PATH.read_text(encoding="utf-8"))


def type_label(key, mark_untested=True):
    label, _, tested, _ = PAGE_TYPES.get(key, (key, "", True, ""))
    return label + ("" if tested or not mark_untested else " (not yet tested)")


def criterion_names(type_key):
    """{criterion id: name} for this type, with the type's v2.2 overrides."""
    ovr = C.OVR.get(type_key, {})
    names = {}
    for cid in load_weights()["page_types"][type_key]:
        base = C.U[cid][0] if cid in C.U else (C.T[cid][0] if cid in C.T else cid)
        names[cid] = ovr.get(cid, {}).get("name", base)
    return names


def gates_for(type_key):
    """All gates that can fire on this page type, in numeric order."""
    scoped = [g for g, types in TYPE_GATES.items() if type_key in types]
    return sorted(UNIVERSAL_GATES + scoped, key=lambda g: int(g[1:]))


def prompt_path(type_key):
    return PROMPTS / f"copilot_prompt_{type_key}_v2.2.txt"


def appendix_a():
    return (STANDARD / "appendix_a_page_type_decision_tree.md").read_text(encoding="utf-8")

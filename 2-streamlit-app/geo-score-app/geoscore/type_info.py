"""'How this page type is scored': plain-language explanation per page type, generated from the v2.2 sources
(geoscore/standard_v22.py = 8-geo-v2.2/catalog.py, engine/weights.json, standard/GEO_Scoring_Standard_All_Types_v2.2.md)
so it cannot drift from the scoring logic."""
import re
import sys

from . import standard_v22 as C
from .catalog import ENGINE, GATE_WHY, PAGE_TYPES, STANDARD, criterion_names, gates_for, load_weights

if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))
import geo_score_calc as calc  # noqa: E402

FAMILY_PLAIN = {
    "answer_def": "answering the question", "evidence": "evidence and insight", "fanout": "follow-up coverage",
    "tone": "neutral tone", "comparison": "comparison and selection", "specs": "specs and facts", "proof": "proof",
    "commercial": "next step / commercial", "freshness": "freshness", None: "stage-neutral",
}


def _pilot_lines():
    """{key: pilot results sentence} from the standard's type sections."""
    text = (STANDARD / "GEO_Scoring_Standard_All_Types_v2.2.md").read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^### `([a-z_]+)` - .*?(?=^### `|^## |\Z)", text, flags=re.M | re.S):
        p = re.search(r"\*\*Pilot results[^*]*\*\*:?\s*(.*)", m.group(0))
        if p:
            out[m.group(1)] = p.group(1).strip()
    return out


_PILOT = None


def pilot(key):
    """(sentence or '', median or None)."""
    global _PILOT
    if _PILOT is None:
        _PILOT = _pilot_lines()
    s = _PILOT.get(key, "")
    m = re.search(r"median ([\d.]+)", s)
    return s, (float(m.group(1)) if m else None)


def _gate_effect(W, key, g):
    gd = W["gates"][g]
    eff = []
    if gd.get("cap", 100) < 100:
        eff.append(f"score max {gd['cap']}")
    names = criterion_names(key)
    for k, v in (gd.get("max_level") or {}).items():
        if k in W["page_types"][key]:
            eff.append(f"'{names.get(k, k)}' max level {v}")
    for k in gd.get("zero", []):
        if k in W["page_types"][key]:
            eff.append(f"'{names.get(k, k)}' set to 0")
    return ", ".join(eff)


def describe(key, stage=None):
    """Dict with everything the panel shows for this type."""
    W = load_weights()
    meta = C.META[key]
    label, default_stage, tested, group = PAGE_TYPES[key]
    names = criterion_names(key)
    st = stage or default_stage
    j = {"page": {"type": key, "stage": st},
         "criteria": [{"id": c, "checks": [{"id": "c1", "result": "pass"}]} for c in W["page_types"][key]]}
    eff = {r["id"]: r["eff_w"] for r in calc.compute(j, W)["criteria"]}
    crit = [{"Criterion": names.get(cid, cid), "ID": cid,
             "Kind": "Universal" if cid in C.U else "Specific to this type",
             "Default weight": w, f"Weight at {st}": eff.get(cid),
             "Counts more/less by stage as": FAMILY_PLAIN.get(calc.family_of(cid, W["families"]))}
            for cid, w in W["page_types"][key].items()]
    crit.sort(key=lambda r: -r["Default weight"])
    gates = [{"Gate": g, "Fires when": W["gates"][g]["desc"], "Effect": _gate_effect(W, key, g), "Why": GATE_WHY.get(g, "")}
             for g in gates_for(key)]
    pil, med = pilot(key)
    return {"key": key, "label": label, "group": group, "tested": tested, "when": meta.get("when", ""),
            "extracts": meta.get("extracts", ""), "natural": meta.get("natural", ""), "default_stage": default_stage,
            "stage_test": C.STAGE_TEST.get(key, ""), "failures": meta.get("failures", ""), "criteria": crit,
            "stage_shown": st, "gates": gates, "pilot": pil, "pilot_median": med}


def render(st, key, stage=None):
    """Render the panel with Streamlit module `st`."""
    d = describe(key, stage)
    st.markdown(f"**{d['label']}** (`{d['key']}`) · {d['group']}")
    if d["tested"]:
        st.success("Tested on SE pages." + (f" Pilot median score: **{d['pilot_median']:g}**." if d["pilot_median"] is not None else ""))
    else:
        st.warning("Not yet tested on SE pages: the logic comes from the standard, so treat scores as indicative.")
    st.markdown(f"**Use it for:** {d['when']}")
    st.markdown(f"**What AI engines extract from this page type:** {d['extracts']}")
    st.markdown(f"**Stage:** default {d['default_stage']}. Natural stages: {d['natural']}  \n"
                f"**How the stage is detected (v2.2 stage test, first match wins):** {d['stage_test']}")
    st.markdown(f"**What is scored and how much it counts** (weights sum to 100; the stage shifts them; shown at {d['stage_shown']}):")
    st.dataframe(d["criteria"], hide_index=True, width="stretch")
    st.markdown("**Gates (deal-breakers that cap the score) for this type:**")
    st.dataframe(d["gates"], hide_index=True, width="stretch")
    st.markdown(f"**Common SE failures** ([A] = author fix on the page, [T] = template/CMS fix): {d['failures']}")
    if d["pilot"]:
        st.caption("Pilot results (Oct 2026): " + d["pilot"])

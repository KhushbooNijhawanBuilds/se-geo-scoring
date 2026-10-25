"""Shared helpers (v2.2): load engine/weights.json, import the v2.2 engine copy, merge the catalogue per page type."""
import json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(ROOT)
ENGINE = os.path.join(ROOT, "engine")  # v2.2 copy of geo_score_calc.py + weights.json (v2.1 is untouched)
FINAL = os.path.join(PROJ, "4-scoring-project-v2.1", "GEO Elec Project", "research", "final-scoring")  # pilot data (read-only)
TESTRUN = os.path.join(PROJ, "7-geo-all-types", "test-run")  # 62 test-run judge JSONs (read-only)
WEIGHTS_PATH = os.path.join(ENGINE, "weights.json")
VERSION = "v2.2"
sys.path.insert(0, ENGINE)
import geo_score_calc as calc  # noqa: E402
import catalog as C  # noqa: E402

W = calc.load(WEIGHTS_PATH)
STAGES = calc.STAGES
KEYS = [k for _, ks in C.GROUPS for k in ks]
assert sorted(KEYS) == sorted(W["page_types"]), set(W["page_types"]) ^ set(KEYS)


def eff_weights(key):
    """Effective weights per stage, computed by the engine's own compute() with every criterion present."""
    out = {}
    for st in STAGES:
        j = {"page": {"type": key, "stage": st},
             "criteria": [{"id": c, "checks": [{"id": "c1", "result": "pass"}], "proposed_level": 5} for c in W["page_types"][key]]}
        r = calc.compute(j, W)
        out[st] = {row["id"]: row["eff_w"] for row in r["criteria"]}
    return out


def fact_density(key):
    t = W["fact_density_threshold_per_100w"]
    return t.get(key, t["default"])


def gates_for(key):
    gs = list(C.UNIVERSAL_GATES) + [g for g, ts in C.GATE_TYPES.items() if key in ts]
    return sorted(gs, key=lambda g: int(g[1:]))


def criteria_for(key):
    """[(cid, name, checks, src, rule, weight, family)] in weights.json order."""
    ovr = C.OVR.get(key, {})
    meta = C.META[key]
    out = []
    for cid, w in W["page_types"][key].items():
        if cid in C.U:
            name, checks = C.U[cid]; src = "FW"; rule = ""
        else:
            name, checks, src, rule = C.T[cid]
        o = ovr.get(cid, {})
        name = o.get("name", name); checks = list(o.get("checks", checks)); src = o.get("src", src)
        rule = " ".join(x for x in [rule, o.get("rule", "")] if x)
        checks = [c.replace("{fd}", f"{fact_density(key):.1f}")
                    .replace("{cadence}", C.CADENCE.get(key, C.DEFAULT_CADENCE))
                    .replace("{expected}", meta.get("expected", "the facts listed under 'What AI extracts'")) for c in checks]
        out.append((cid, name, checks, src, rule, w, calc.family_of(cid, W["families"]) or "other"))
    return out


def gate_text(key, g):
    t = C.GATE_PROMPT[g]
    if g == "G1":
        z = [c for c in W["gates"]["G1"].get("zero", []) if c in W["page_types"][key]]
        t = t.replace("{zero}", (" -> " + " and ".join(f"{c} = 0" for c in z)) if z else " ->")
        t = t.replace("->; ", "-> ")
    if g == "G6":
        t = t.replace("{g6}", C.G6_EXTRA.get(key, ""))
        # v2.2 fix 8: only name U3 when the type has it
        t = t.replace("{g6u3}", " -> U3 max 2" if "U3" in W["page_types"][key] else " (this type has no U3, so only the score cap applies)")
    if g == "G13":
        lv = [c for c in W["gates"]["G13"]["max_level"] if c in W["page_types"][key]]
        t = (f"Thin page (fewer than 3 substantive factual statements) -> {' and '.join(lv)} max 2." if lv
             else "Thin page (fewer than 3 substantive factual statements) -> no effect for this type (it has no U7/U8); still report it.")
        t += " " + C.G13_RULE
    return t


def caps_for(key):
    """Encoded level caps for criteria in this type, as prompt text."""
    out = []
    for cid in W["page_types"][key]:
        for cap in W["level_caps"].get(cid, []):
            if "unless_pass" in cap:
                cs = cap["unless_pass"]
                cond = f"{cid} {' or '.join(cs)} fails" if len(cs) > 1 else f"{cid} {cs[0]} fails"
            else:
                cond = f"{cid} {' and '.join(cap['if_all_fail'])} both fail"
            out.append(f"{cond} -> {cid} max {cap['max']} ({cap['why']})")
    return out


def n_checks(key, cid):
    return next(len(c[2]) for c in criteria_for(key) if c[0] == cid)


def anchors_for(key):
    """Anchor text per criterion; v2.2 fix 10: per-type overrides, and no anchor that names a check the type does not have."""
    out = []
    for cid in W["page_types"][key]:
        a = (W.get("level_anchor_overrides", {}).get(key) or {}).get(cid) or W["level_anchors"].get(cid)
        if not a:
            continue
        nc = n_checks(key, cid)
        parts = []
        for L in ("3", "4"):
            r = a.get(L)
            if r is None or (isinstance(r, list) and any(int(c[1:]) > nc for c in r)):
                continue
            parts.append(f"{L} = any {r['any']}" if isinstance(r, dict) else f"{L} = " + "+".join(r))
        out.append(f"{cid}: " + "; ".join(parts))
    return out


def note_checks_for(key):
    """[(cid, [check ids])] where a judge note may replace a quote (v2.2 fix 3)."""
    na = W.get("note_allowed_checks", {})
    return [(cid, na[cid]) for cid in W["page_types"][key] if cid in na]


def block_fail_for(key):
    """Text lines: checks that are fail (never na) when their block is missing (v2.2 fix 4)."""
    out = []
    for cid in W["page_types"][key]:
        bd = W.get("block_dependent_checks", {}).get(cid)
        if bd:
            out.append(f"{cid} {'/'.join(bd['then_fail'])} fail when {bd['block']} fails (no block)")
        for c in W.get("na_is_fail", {}).get(cid, []):
            out.append(f"{cid} {c} fails when the page has no sections (never na)")
    return out

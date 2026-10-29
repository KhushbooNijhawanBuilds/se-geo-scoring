"""Content GEO Score: score a page against the SE Content GEO Scoring Standard v2.2 (all 26 page types).

Run:  streamlit run app.py
"""
import json
import os
from pathlib import Path

import pandas as pd
import streamlit as st

from geoscore.capture import CaptureError, capture
from geoscore.catalog import GROUPS, PAGE_TYPES, STAGES, appendix_a, load_weights, type_label
from geoscore.type_info import render as render_type_info
from geoscore.explain import explain, normalise
from geoscore.judge import GEMINI_MODEL, GEMINI_MODEL_ALT, JudgeError, classify_type, resolve_model, run_judge, to_calc_judge, verify_quotes

HERE = Path(__file__).resolve().parent
EXAMPLES = {
    "SE blog: cooling design, water, noise and permitting": "blog_cooling_design_se.json",
    "SE calculator: data center power sizing (gate + penalties)": "calculator_power_sizing_se.json",
    "Medium blog: building agents in Copilot Studio": "medium_copilot_studio_blog.json",
    "Test run 07, solution: EcoStruxure rack solutions for AI": "v22_testrun_07_solution.json",
    "Test run 19, case study: technology at McLaren Racing": "v22_testrun_19_case_study.json",
    "Test run 44, software hub: industrial software portfolio": "v22_testrun_44_software_hub.json",
    "Test run 56, ESG report download page: 2025 Sustainability Report": "v22_testrun_56_esg_report.json",
}
SE_INVENTORY = HERE / "examples" / "se_inventory"
AUTO_TYPE = "auto"
DETECT = "Detect automatically (v2.2 stage test for the page type)"
BAND_COLORS = {"Excellent": "#0F766E", "Good": "#15803D", "Average": "#B45309", "Poor": "#B91C1C"}


def _fmt(v):
    if isinstance(v, float) and v.is_integer():
        return str(int(v))
    return str(v)


def saved_api_key():
    """Key from .streamlit/secrets.toml, else the GEMINI_API_KEY environment variable. Never shown."""
    try:
        key = st.secrets.get("GEMINI_API_KEY", "")
        if key:
            return key, "the secrets file on this computer"
    except Exception:
        pass
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"], "the GEMINI_API_KEY environment variable"
    return "", ""


@st.cache_data(show_spinner=False)
def se_inventory():
    """The bundled Schneider scorings, grouped by content type. Empty if the folder isn't bundled."""
    path = SE_INVENTORY / "index.json"
    if not path.exists():
        return [], {}
    entries = json.loads(path.read_text(encoding="utf-8"))
    groups = {}
    for e in entries:
        groups.setdefault(e["inventory_type"], []).append(e)
    return entries, groups


def se_page_label(e):
    return f"{e['id']} · {e['title']} · score {e['expected_final_score']} {e['expected_band']}"


def type_options():
    """Picker options: auto-detect, then tested types grouped, then not-yet-tested types grouped."""
    opts, labels = [AUTO_TYPE], {AUTO_TYPE: "Auto-detect the page type (the AI classifies it with the standard's decision tree)"}
    for tested in (True, False):
        for group, keys in GROUPS:
            for k in keys:
                if PAGE_TYPES[k][2] == tested:
                    opts.append(k)
                    head = "Tested" if tested else "Not yet tested"
                    labels[k] = f"{head} · {group.split(' - ', 1)[-1]} · {type_label(k)}"
    return opts, labels


st.set_page_config(page_title="Content GEO Score", page_icon=":bar_chart:", layout="wide")


# ---------- sidebar ----------
with st.sidebar:
    st.header("Setup")
    saved_key, key_source = saved_api_key()
    if saved_key:
        st.success(f"Using your saved Gemini API key (from {key_source}).")
        override = st.text_input("Use a different key for this session (optional)", type="password", value="")
        api_key = override or saved_key
    else:
        st.warning("No saved API key found. Add it to .streamlit/secrets.toml (see README), or paste it below for this session only.")
        api_key = st.text_input("Gemini API key", type="password", value="",
                                help="A Google AI Studio API key. Get one at https://aistudio.google.com/apikey")
    default_model = resolve_model()
    model_choices = list(dict.fromkeys([default_model, GEMINI_MODEL, GEMINI_MODEL_ALT]))
    model = st.selectbox("Judge model", model_choices, index=0,
                         help="Google Gemini model. Gemini 2.5 Pro is recommended for judging. "
                              "Set GEMINI_MODEL in secrets.toml or the environment to change the default.")
    effort = st.selectbox("Judge effort", ["high", "medium", "xhigh"], index=0,
                          help="Mapped to the Gemini thinking budget. Higher effort = more careful checks, slower and costlier.")
    rules = st.radio("Scoring rules", ["v2.2", "v2.1"], index=0, horizontal=True,
                     help="v2.2 (default): the level is set by the calculator from the checks; the judge can only lower it with a reason. "
                          "v2.1: the older level logic, for comparison only (same weights).")
    st.caption(f"Standard: SE Content GEO Scoring Standard v2.2, weights {load_weights().get('version')}")
    st.caption("The AI judge only answers pass/fail checks with evidence. Levels and the score are calculated by code.")

st.title("Content GEO Score")
st.write("Score how ready a page's content is to be understood, trusted and quoted by AI answer engines, "
         "and see exactly how the score was calculated. All 26 page types of standard v2.2.")

tab_score, tab_replay = st.tabs(["Score a page", "Replay a saved judgement or Copilot JSON (no API call)"])

# ---------- intake ----------
with tab_score:
    opts, opt_labels = type_options()
    st.caption("Fields marked * are required. A target question is strongly recommended: the score checks whether the page answers it.")
    type_key = st.selectbox("Content type *", opts, format_func=lambda k: opt_labels[k],
                            help="Types marked 'Not yet tested' use the v2.2 logic but have not been validated on SE pages yet.")
    with st.expander("How this page type is scored", expanded=False):
        if type_key == AUTO_TYPE:
            st.write("The page type will be detected from the page with the standard's decision tree (below). "
                     "Pick a type above to see how it is scored; after scoring, the result has a tab for the detected type.")
            st.markdown(appendix_a())
        else:
            render_type_info(st, type_key)
    with st.form("intake"):
        url = st.text_input("Page URL *", placeholder="https://www.se.com/...  (or paste the page text below)")
        c1, c2 = st.columns(2)
        with c1:
            stage_choice = st.selectbox("Buyer-journey stage *", [DETECT] + STAGES,
                                        help="Awareness: sees a problem. Education: learning how solutions work. Consideration: comparing options. "
                                             "Evaluation: checking specific products. Decision: ready to buy. "
                                             "'Detect automatically' applies the page type's v2.2 stage test.")
            topic = st.text_input("Topic *", placeholder="e.g. liquid cooling for AI data centers")
        with c2:
            ind = st.selectbox("Industry *", ["Data Centers & Networks", "Buildings (commercial)", "Homes (residential)", "Industrial Automation & Machine Builders",
                                              "Power Systems & Distribution", "Grid & Utilities", "Healthcare", "Infrastructure (water, transport)",
                                              "Energy Management & Sustainability", "Software (EcoStruxure, AVEVA)", "Services", "Other (type below)"])
            other_ind = st.text_input("Other industry (only if you chose Other)")
            industry = other_ind if ind.startswith("Other") else ind
            prompts = st.text_area("Target question(s) a buyer asks AI (recommended, one per line)", height=96,
                                   placeholder="How does direct liquid cooling work?\nLiquid vs air cooling for AI racks")
            c3, c4 = st.columns(2)
            audience = c3.text_input("Audience (optional)")
            country = c4.text_input("Country (optional)")
        with st.expander("Paste the page text instead (for pages that block automated requests, load content with JavaScript, or PDFs)"):
            pasted = st.text_area("Page text (mark headings with # if you can)", height=200)
        submitted = st.form_submit_button("Score page", type="primary")

    if submitted:
        detect = stage_choice == DETECT
        intake = {"url": url.strip(), "topic": topic.strip(), "industry": industry.strip(),
                  "stage": stage_choice if not detect else "", "detect_stage": detect,
                  "target_prompts": [p.strip() for p in prompts.splitlines() if p.strip()],
                  "audience": audience.strip(), "country": country.strip()}
        missing = [name for name, ok in (("Page URL or pasted page text", intake["url"] or (pasted or "").strip()),
                                         ("Topic", intake["topic"]), ("Industry", intake["industry"])) if not ok]
        if missing:
            st.error("Please fill in the required fields: " + ", ".join(missing) + ".")
        elif not api_key:
            st.error("Add your Gemini API key (see the sidebar) to score a page. You can try the Replay tab without a key.")
        else:
            if not intake["target_prompts"]:
                st.warning("No target question given: the judge will infer one, and the result will say so.")
            with st.status("Scoring the page...", expanded=True) as status:
                try:
                    st.write("Capturing the page content...")
                    captured = capture(url=intake["url"] or None, pasted_text=pasted)
                    st.write(f"Captured {captured['signals'].get('word_count', 0):,} words from {captured['source']}.")
                    type_info, usage_c = None, None
                    key = type_key
                    if type_key == AUTO_TYPE:
                        st.write("Classifying the page type with the standard's decision tree (Appendix A)...")
                        type_info, usage_c = classify_type(api_key or None, model, "medium", intake, captured)
                        key = type_info["type_key"]
                        st.write(f"Detected page type: **{type_label(key)}** (`{key}`). {type_info.get('reason', '')}")
                    if detect:
                        intake["stage"] = PAGE_TYPES[key][1]  # fallback only; the judge's stage test decides
                    st.write(f"Judging every {type_label(key, False)} check with {model} (this can take 1-3 minutes)...")
                    judgement, usage = run_judge(api_key or None, model, effort, key, intake, captured)
                    st.write("Verifying every quote against the page...")
                    qv = verify_quotes(judgement, captured["text"])
                    judge_json = to_calc_judge(judgement, key, intake, type_info)
                    judge_json["capture"] = {"source": captured["source"], "notes": captured["notes"],
                                             "signals": captured["signals"], "title": captured["title"]}
                    judge_json["quote_check"] = qv
                    if usage_c:
                        usage["classify_input_tokens"] = usage_c["input_tokens"]
                        usage["classify_output_tokens"] = usage_c["output_tokens"]
                    judge_json["usage"] = usage
                    st.session_state["judge"] = judge_json
                    st.session_state["page_text"] = captured["text"]
                    st.session_state["expected"] = None
                    status.update(label="Scored.", state="complete", expanded=False)
                except (CaptureError, JudgeError) as e:
                    status.update(label="Could not score the page.", state="error")
                    st.error(str(e))

with tab_replay:
    st.write("Load a judgement saved earlier (or one of the examples) to see the full calculation without calling the API.")

    entries, se_groups = se_inventory()
    if entries:
        st.subheader("Load a Schneider page we have already scored")
        st.caption(f"{len(entries)} pages from the Schneider content inventory, scored with standard v2.2. "
                   "Pick a content type, then the page. No API key needed.")
        s1, s2 = st.columns([1, 2])
        with s1:
            se_type = st.selectbox("Content type", list(se_groups),
                                   format_func=lambda t: f"{t} ({len(se_groups[t])})",
                                   key="se_type")
        with s2:
            pages = {e["id"]: e for e in se_groups[se_type]}
            se_id = st.selectbox(f"Page ({len(pages)} of this type)", list(pages),
                                 format_func=lambda i: se_page_label(pages[i]), key=f"se_page_{se_type}")
            se_page = pages[se_id]
        st.markdown(f"**Stage:** {se_page['stage']} · **Page type:** {type_label(se_page['page_type_key'])} "
                    f"(`{se_page['page_type_key']}`)")
        st.markdown(f"[{se_page['url']}]({se_page['url']})")
        if se_page["note"]:
            st.info(se_page["note"])
        if st.button("Show this page's calculation", type="primary", key="se_show"):
            data = json.loads((SE_INVENTORY / f"{se_page['id']}.json").read_text(encoding="utf-8"))
            st.session_state["judge"] = normalise(data)
            st.session_state["page_text"] = None
            st.session_state["expected"] = se_page
        st.divider()
        st.markdown("**Or replay your own judgement**")

    choice = st.selectbox("Example", ["(choose)"] + list(EXAMPLES))
    upload = st.file_uploader("...or upload a judge JSON", type=["json"])
    pasted_json = st.text_area("...or paste the JSON block from any of the 26 v2.2 Copilot prompts here. No API key needed.", height=150,
                               help="Run the Copilot prompt for the page type (standard/prompts/copilot_prompt_<type>_v2.2.txt). "
                                    "Copy the JSON block it returns at the end and paste it here.")
    if st.button("Show calculation"):
        data = None
        if pasted_json.strip():
            raw = pasted_json.strip()
            try:
                data = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
            except ValueError:
                st.error("That isn't valid JSON. Copy only the block between { and } from the AI tool's answer.")
        elif upload is not None:
            try:
                data = json.load(upload)
            except ValueError:
                st.error("That file isn't valid JSON.")
        elif choice in EXAMPLES:
            data = json.loads((HERE / "examples" / EXAMPLES[choice]).read_text(encoding="utf-8"))
        else:
            st.warning("Choose an example, upload a file or paste a JSON block.")
        if data is not None:
            st.session_state["judge"] = normalise(data)
            st.session_state["page_text"] = None
            st.session_state["expected"] = None


# ---------- results ----------
judge = st.session_state.get("judge")
if judge:
    try:
        ex = explain(judge, rules=rules)
    except SystemExit as e:  # the engine exits on unknown type/stage
        st.error(f"This judgement can't be scored: {e}")
        st.stop()
    r = ex["result"]
    page = judge.get("page", {})
    tkey = r["page_type_key"]
    st.divider()
    exp = st.session_state.get("expected")
    if exp:
        if r["final_score"] == exp["expected_final_score"] and r["band"] == exp["expected_band"]:
            st.success(f"Bundled Schneider page {exp['id']}: recomputed score {r['final_score']} ({r['band']}) "
                       "matches the recorded result for this page.")
        else:
            st.warning(f"Bundled Schneider page {exp['id']}: the recomputed score is {r['final_score']} ({r['band']}) "
                       f"but the recorded result is {exp['expected_final_score']} ({exp['expected_band']}). "
                       "The engine or weights may have changed since this page was scored.")
        if exp["note"]:
            st.caption(exp["note"])
        st.caption(f"Page: [{exp['url']}]({exp['url']})")
    st.subheader(f"Result: {page.get('topic') or type_label(tkey, False)}")
    if page.get("url"):
        st.caption(page["url"])
    st.caption(f"{type_label(tkey)} (`{tkey}`) · target question(s): {'; '.join(page.get('target_prompts') or []) or '(inferred)'}")
    if page.get("type_source") == "detected":
        st.markdown(f"**Page type: {type_label(tkey)}** (auto-detected, {page.get('type_rule', '')}): {page.get('type_reason', '')}")
    if not PAGE_TYPES.get(tkey, ("", "", True))[2]:
        st.warning("This page type's logic has not yet been tested on SE pages: treat the score as indicative.")
    how = {"detected": "from the v2.2 stage test", "chosen": "chosen in the intake"}.get(page.get("stage_source"), "as recorded in the judgement")
    reason = page.get("stage_reason") or page.get("stage_signal") or ""
    st.markdown(f"**Buyer-journey stage: {r['stage']}** ({how})" + (f": {reason}" if reason and page.get("stage_source") != "chosen" else ""))
    if page.get("stage_source") == "chosen" and page.get("detected_stage") and page["detected_stage"] != r["stage"]:
        st.caption(f"Note: the v2.2 stage test would place this page at {page['detected_stage']} ({reason}). "
                   "Re-run with that stage if it fits your intent better.")

    m1, m2, m3, m4, m5 = st.columns(5)
    m1.metric("Content GEO Score", f"{r['final_score']} / 100")
    m2.markdown(f"<div style='padding-top:6px'><span style='font-size:14px;color:#6B7480'>Band</span><br>"
                f"<span style='font-size:30px;font-weight:700;color:{BAND_COLORS.get(r['band'], '#1B2430')}'>{r['band']}</span></div>",
                unsafe_allow_html=True)
    m3.metric("Raw score", r["raw_score"])
    m4.metric("Penalties", f"-{r['penalty_points']}")
    m5.metric("Gate cap", r["cap"] if r["cap"] else "none", help=", ".join(r["gates_triggered"]) or None)
    ok = "meets" if r["meets_threshold"] else "is below"
    st.info(f"This page {ok} the 70 'Score is OK' bar. Confidence: {r['confidence']}. Rules: {r['level_rules']}. "
            f"{'Borderline: within 3 points of a band edge, so confirm with 3 independent runs and use the median. ' if any(abs(r['final_score'] - b) <= 3 for b in (40, 70, 90)) else ''}"
            "The score measures citation-readiness of the content only; actual AI citation also depends on retrieval, off-site consensus and technical access.")

    t1, t2, t3, t4, t5, t6, t7 = st.tabs(["How the score was calculated", "Gates", "Penalties", "Top gaps",
                                           "Evidence for every check", "Content & notes", "How this page type is scored"])

    with t7:
        render_type_info(st, tkey, r["stage"])

    with t1:
        with st.expander("What are levels? (plain-language explanation)", expanded=False):
            st.markdown(
                "Each criterion gets a **level from 0 to 5**, like a star rating: "
                "**0** missing · **1** barely there · **2** weak · **3** good enough · **4** strong · **5** best in class.  \n"
                "**In v2.2 the calculator sets the level, not the AI.** Level = the check ceiling: 5 if every check passes, "
                "otherwise share of checks passed x 5, rounded half up (max 4). It is raised to the rubric's anchor floor when the "
                "anchor checks pass, then the rubric caps apply (e.g. 'no takeaways block' keeps it at 0).  \n"
                "The AI judge can only **lower** a level, and only with a downgrade reason that names a check it passed but found weak "
                "(never below the anchor floor). Without such a reason, its proposed level is ignored.  \n"
                "**Points = level / 5 x the criterion's weight.** The 'Lost' points are what a fix can win back.")
        st.markdown("**Step by step**")
        st.table(pd.DataFrame([(s, _fmt(v)) for s, v in ex["steps"]], columns=["Step", "Value"]).set_index("Step"))
        st.markdown(
            "1. **Checks:** each criterion has pass/fail/na checks, answered with a quote (or a judge note for absence/layout checks).  \n"
            "2. **v2.2 check rules:** a note on a check that needs a quote becomes a fail; when a block is missing its checks fail instead of being na.  \n"
            "3. **Level 0-5:** set by the calculator (ceiling, anchor floor, caps; judge downgrade only with a reason).  \n"
            "4. **Weights:** content-type weight x stage multiplier, rescaled to sum to 100 (= Effective weight).  \n"
            "5. **Points** = level / 5 x effective weight. **Lost** = what is still recoverable.  \n"
            "6. **Final** = raw - penalties (max -10), then the lowest triggered gate cap.")
        df = pd.DataFrame(ex["rows"])
        st.dataframe(df, hide_index=True, width="stretch",
                     column_config={"Points": st.column_config.NumberColumn(format="%.2f"),
                                    "Lost": st.column_config.NumberColumn(format="%.2f"),
                                    "Effective weight": st.column_config.NumberColumn(format="%.2f")})
        tot = df["Points"].sum()
        st.caption(f"Sum of points = {tot:.1f} (raw score). Universal criteria carry "
                   f"{df.loc[df['Kind'] == 'Universal', 'Effective weight'].sum():.0f}% of the weight on this page type; "
                   f"type-specific criteria {df.loc[df['Kind'] == 'Type-specific', 'Effective weight'].sum():.0f}%.")
        if ex["downgrades"]:
            st.markdown("**Judge downgrades accepted** (a passed check named as weak)")
            st.table(pd.DataFrame(ex["downgrades"]).set_index("Criterion"))
        elif rules == "v2.2":
            st.caption("No judge downgrade: every level is the calculator's level.")
        if r.get("warnings"):
            with st.expander(f"Calculator notes ({len(r['warnings'])})"):
                for w in r["warnings"]:
                    st.markdown(f"- {w}")

    with t2:
        trig = [g for g in ex["gates"] if g["Status"] == "TRIGGERED"]
        if trig:
            st.error(f"{len(trig)} gate(s) triggered: " + ", ".join(f"{g['Gate']} ({g['Effect if triggered']})" for g in trig))
        else:
            st.success("No gate triggered.")
        st.write("Gates are deal-breakers. If one fires, the final score can't go above its cap, however good the rest is. "
                 "These are all the gates that apply to this content type:")
        st.table(pd.DataFrame(ex["gates"]).set_index("Gate"))

    with t3:
        appl = [p for p in ex["penalties"] if p["Status"] == "APPLIED"]
        st.write(f"Penalties are subtracted from the raw score, capped at -10 in total. Hidden AI instructions are always -10 and flagged. "
                 f"Applied here: **-{r['penalty_points']}**" + (f" ({', '.join(p['Penalty'] for p in appl)})." if appl else "."))
        st.table(pd.DataFrame(ex["penalties"]).set_index("Penalty"))

    with t4:
        st.write("Gaps ranked by the points you would recover. [Template / CMS] fixes are made once for every page; [Author] fixes are on this page.")
        for i, s in enumerate(ex["shortfalls"][:8]):
            with st.expander(f"{s['id']} {s['name']}: +{s['lost']:.1f} points available (now level {s['level']})", expanded=i == 0):
                if s["rationale"]:
                    st.write(s["rationale"])
                if s["adjustments"]:
                    st.caption(s["adjustments"])
                for f in s["failed_checks"]:
                    st.markdown(f"- **{f['check']}** {f['description']}  \n  _{f['owner']}_ · {f['evidence']}")

    with t5:
        st.table(pd.DataFrame(ex["evidence"]))
        qc = judge.get("quote_check")
        if qc:
            st.caption(f"{qc['checked']} quotes checked against the page; {qc['failed']} not found and turned into fails. "
                       "Judge notes are not quotes; the calculator accepts them only on the absence/layout checks the standard allows.")

    with t6:
        cap = judge.get("capture") or {}
        for n in cap.get("notes", []):
            st.warning(n)
        obs = judge.get("out_of_scope_observations") or []
        if obs:
            st.markdown("**Out-of-scope observations (technical, not scored)**")
            for o in obs:
                st.markdown(f"- {o}")
        if (judge.get("stage_fit") or {}).get("note"):
            st.markdown("**Stage fit:** " + judge["stage_fit"]["note"])
        if page.get("inferred_fields"):
            st.markdown("**Inferred by the judge:** " + ", ".join(page["inferred_fields"]))
        if page.get("fan_outs"):
            st.markdown("**Follow-up questions judged:** " + " · ".join(page["fan_outs"]))
        if judge.get("usage"):
            u = judge["usage"]
            st.caption(f"Judge: {u.get('model')} · {u.get('input_tokens', 0):,} input tokens · {u.get('output_tokens', 0):,} output tokens")
        if st.session_state.get("page_text"):
            with st.expander("Captured page text"):
                st.text(st.session_state["page_text"][:20000])

    d1, d2 = st.columns(2)
    d1.download_button("Download judgement (JSON)", json.dumps(judge, ensure_ascii=False, indent=2), file_name="geo_judgement.json")
    d2.download_button("Download score result (JSON)", json.dumps(r, ensure_ascii=False, indent=2), file_name="geo_score_result.json")

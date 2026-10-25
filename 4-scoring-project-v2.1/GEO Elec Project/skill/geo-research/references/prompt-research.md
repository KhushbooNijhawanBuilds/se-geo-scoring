# Prompt Research, Fan-Out Prediction & Reverse Engineering

## 1. Deriving target prompts when none are provided (Score Agent step 3)

Build the seed prompt from **Topic × Persona × Stage × Intent**. Then predict 3–5 fan-out sub-questions.

| Stage | Seed template | Typical fan-out sub-questions |
|---|---|---|
| Awareness | "Why does/What causes [problem] in [industry/site type]?" · "What is [concept]?" | impact/cost of the problem · causes · who is affected · early warning signs · what options exist |
| Education | "How does [technology] work?" · "What standards apply to [application]?" | mechanism · key components · standards/regulations · pros/cons vs alternatives · typical use cases |
| Consideration | "What are the best [category] for [application]?" · "[Tech A] vs [Tech B] for [use]?" | selection criteria · types compared · cost ranges · maintenance · compliance · leading options |
| Evaluation | "[Product] vs [competitor] for [requirement]" · "Is [product] compatible with [X]?" · "ROI of [solution]" | specs/ratings · compatibility · certifications · TCO/payback · references/case studies · lead time |
| Decision | "Where to buy [ref]?" · "[ref] installation / datasheet / price" · "replacement for [legacy ref]" | availability · distributors · documents · warranty · substitutes · installation steps |

Example (Playbook): the seed "What is the best SF6-free switchgear?" fans out to: how does pure-air technology work · cost vs traditional · maintenance differences · regulatory compliance benefits.

Always label inferred prompts as *inferred*. The content owner should confirm them or replace them with Profound or real-user prompts.

## 2. Prompt sources (when doing research for a topic)

- **Free/manual:**
  - Google Search Console question queries (what/why/how/where).
  - People Also Ask and autosuggest.
  - Perplexity sub-queries.
  - The ChatGPT network payload `queries` field (DevTools).
  - Reddit and technical forums (r/electrical, r/HVAC, r/PLC, r/manufacturing, r/sysadmin), searching "vs", "worth it" and "how to".
  - YouTube/LinkedIn comments.
  - Competitor FAQs.
  - Support and sales logs.
- **LLM extrapolation:**
  - Give the model the audience, offer and stage.
  - Ask 5 engines (ChatGPT, Perplexity, Gemini, Copilot, Claude) the same prompts in logged-out sessions.
  - Prompts that overlap across engines are the "hot" ones.
  - **Never paste confidential data into public AI tools.**
- **Paid:** Profound (SE standard), Semrush AI Toolkit, Ahrefs Brand Radar, Peec, Otterly.

## 3. Topical map & prompt chains (Toolkit grounding methodology)

1. Extract intent from PAA and related queries.
2. Ground it in community signals (real friction points).
3. Build the topical map: core category → subtopics → specific prompts.
4. Sequence the prompts: Lead-up context → **Pivot Prompt** → Follow-on the brand guides the user towards.

Prioritize with the **GEO Strategic Score**: Competitive Density + Citation Share Potential + Business Impact + Technical Feasibility/E-E-A-T, each 0–25.

## 4. Prompt analysis matrix

| Intent | Example prompt | Funnel stage | Mapped asset (owned/gap) | Action (optimize/build) | Opportunity (H/M/L + why) |

## 5. Reverse-engineering a cited competitor (5-step audit)

1. **Context:** real intent, entities the AI attaches (incl. competitors), scope, our closest page.
2. **Keywords:** two-column term list (cited answer vs our page); flag internal jargon.
3. **Tone of voice:** formality, perspective, confidence. Rate theirs and ours side by side.
4. **Messaging:** anchoring facts, structure, proof points, self-containment. Extract the single sentence most likely to be quoted, then check whether we have an equivalent.
5. **Sources:** who is cited (competitor, publisher, distributor, forum, institution), format, authority signals, pattern across 3–5 related prompts.

Interpretation (Playbook citation lenses):
- If competitor pages dominate, owned content can win.
- If institutions dominate, go through earned and institutional coverage.
- If publishers dominate, go through those outlets.
- If the winning format is a list or table and ours is narrative, restructure.
- If no page answers the prompt, there is a creation gap.
- If the topic exists only as a subsection, build a dedicated page.

## 6. Manual visibility testing (for before/after validation)

Fixed panel of 20–50 prompts, run monthly on ChatGPT, Perplexity, Gemini/AI Mode, Copilot and Claude. Use logged-out sessions and ≥ 3 runs (ideally 7) per prompt. Log **Mentioned · Cited (URL) · Position · Sentiment** per prompt × engine × brand, plus a competitor row. Track the cited URL, not just the mention.

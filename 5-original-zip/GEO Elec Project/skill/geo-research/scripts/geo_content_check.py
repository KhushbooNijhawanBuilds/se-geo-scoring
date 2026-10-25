#!/usr/bin/env python3
"""Deterministic GEO content signals for the Content GEO Score.

Stdlib only. Reads an HTML, Markdown or plain-text file (or fetches a URL's raw HTML)
and emits JSON metrics that the LLM judge uses as evidence. These signals inform the
judge; they are NOT the score.

Usage:
  python geo_content_check.py --file page.html [--pretty]
  python geo_content_check.py --file brief.md --format md
  python geo_content_check.py --url https://www.example.com/page --pretty
"""
import argparse
import html
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

SKIP_TAGS = {"script", "style", "noscript", "nav", "footer", "header", "aside", "form", "svg", "template"}
BLOCK_TAGS = {"p", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6", "dt", "dd", "blockquote", "figcaption", "caption", "div", "section", "article"}

UNITS = (r"%|percent|VAC|VDC|Vac|Vdc|kVAC|kVDC|Vrms|°C|°F|mm|cm|m|km|kg|g|t|V|kV|mV|A|kA|mA|W|kW|MW|GW|Wh|kWh|MWh|VA|kVA|MVA|var|kvar|Hz|kHz|ms|s|min|h|hours?|days?|"
         r"weeks?|months?|years?|dB|lux|lm|bar|Pa|kPa|psi|Nm|rpm|IP\d{2}|IK\d{2}|AWG|mm²|m²|m³|ft|in|lbs?|USD|EUR|\$|€|£|x")
NUM_UNIT_RE = re.compile(r"(?<![\w.])(\d{1,3}(?:[ ,.]\d{3})*(?:[.,]\d+)?|\d+(?:[.,]\d+)?)\s?(?:-|–|to)?\s?(?:\d+(?:[.,]\d+)?)?\s?(" + UNITS + r")(?![a-zA-Z])")
PCT_RE = re.compile(r"\d+(?:[.,]\d+)?\s?%")
STANDARD_RE = re.compile(r"\b(?:IEC|EN|UL|ISO|IEEE|NEC|NFPA|CSA|BS|DIN|ANSI|NEMA|ASHRAE|IEC/EN|EN/IEC)\s?-?\s?\d{2,6}(?:[-.]\d+)*(?::\d{4})?\b")
CERT_RE = re.compile(r"\b(?:CE|UKCA|RoHS|REACH|cULus|UL[- ]listed|PEP|EPD|ENERGY STAR|ATEX|IECEx|SIL\s?\d|ISO\s?9001|ISO\s?14001|ISO\s?50001)\b")
YEAR_RE = re.compile(r"\b(20[0-3]\d|19[89]\d)\b")
DATE_LABEL_RE = re.compile(r"\b(last updated|updated|published|revised|revision|rev\.?\s?\d+|version\s?\d|v\d+\.\d+)\b", re.I)
DEFINITION_RE = re.compile(r"\b(is|are)\s+(an?|the)\b|\brefers to\b|\bmeans\b|\bis defined as\b|\bdefined as\b|\bconsists of\b", re.I)
QUESTION_START_RE = re.compile(r"^(what|how|why|which|when|where|who|can|does|do|is|are|should|will|could)\b", re.I)
SENT_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"“(])")
QUOTE_RE = re.compile(r"[“\"]([^”\"]{25,400})[”\"]")
ATTRIBUTION_RE = re.compile(r"\b(according to|source:|sources:|study|survey|report|research by|data from|as reported by|cited by|measured)\b", re.I)

FLUFF = ["innovative", "innovation", "cutting-edge", "cutting edge", "industry-leading", "industry leading", "world-class", "world class",
         "revolutionary", "next-gen", "next-generation", "next generation", "best-in-class", "best in class", "state-of-the-art",
         "state of the art", "seamless", "seamlessly", "robust", "unparalleled", "unmatched", "game-changing", "game changer",
         "leverage", "leveraging", "empower", "empowering", "transform the way", "future-ready", "future-proof", "smarter",
         "unlock", "unleash", "holistic", "synergy", "best-of-breed", "market-leading", "leading provider", "global leader",
         "peace of mind", "unrivaled", "superior", "exceptional", "designed to help", "helps you"]
HEDGES = ["it depends", "in general", "generally speaking", "many experts", "studies show", "some say", "may help", "can help",
          "might", "arguably", "it is believed", "various factors", "a range of", "a variety of"]
VAGUE_CTAS = ["learn more", "read more", "know more", "find out more", "discover more", "discover", "get started", "click here",
              "download now", "unlock insights", "see more", "more info", "explore now", "contact us today"]
CONTEXT_DEP = ["as mentioned above", "as mentioned earlier", "as seen before", "see above", "as described above", "the above",
               "this product", "our solution", "our solutions", "our platform", "our product", "this solution", "the following below"]
GENERIC_HEADINGS = {"overview", "introduction", "intro", "features", "benefits", "learn more", "more", "details", "description",
                    "about", "summary", "conclusion", "our solutions", "solutions", "products", "resources", "highlights",
                    "key features", "why us", "why choose us", "what's next", "what's next?", "the power of change", "a new era begins"}


class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.blocks = []          # list of (kind, text) kinds: h1..h6, p, li, cell, other
        self.cur_tag = None
        self.buf = []
        self.tables = 0
        self.table_rows = 0
        self.lists = 0
        self.images = []          # alt texts (None = missing)
        self.links = []           # anchor texts
        self.buttons = []
        self._in_a = False
        self._a_buf = []
        self._in_button = False
        self._b_buf = []
        self.title = ""
        self._in_title = False
        self.meta_desc = ""

    def _flush(self):
        text = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        if text:
            kind = self.cur_tag if self.cur_tag and re.fullmatch(r"h[1-6]", self.cur_tag) else (
                "li" if self.cur_tag == "li" else "cell" if self.cur_tag in ("td", "th") else "p")
            self.blocks.append((kind, text))
        self.buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "meta" and (a.get("name") or "").lower() == "description":
            self.meta_desc = a.get("content") or ""
        if tag in SKIP_TAGS:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "img":
            self.images.append(a.get("alt"))
        if tag == "table":
            self.tables += 1
        if tag == "tr":
            self.table_rows += 1
        if tag in ("ul", "ol"):
            self.lists += 1
        if tag == "a":
            self._in_a, self._a_buf = True, []
        if tag == "button":
            self._in_button, self._b_buf = True, []
        if tag in BLOCK_TAGS or tag == "br":
            self._flush()
            if tag != "br":
                self.cur_tag = tag

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == "a" and self._in_a:
            self.links.append(re.sub(r"\s+", " ", "".join(self._a_buf)).strip())
            self._in_a = False
        if tag == "button" and self._in_button:
            self.buttons.append(re.sub(r"\s+", " ", "".join(self._b_buf)).strip())
            self._in_button = False
        if tag in BLOCK_TAGS:
            self._flush()
            self.cur_tag = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self.skip:
            return
        self.buf.append(data)
        if self._in_a:
            self._a_buf.append(data)
        if self._in_button:
            self._b_buf.append(data)


def parse_html(raw):
    ex = Extractor()
    ex.feed(raw)
    ex._flush()
    return {"blocks": ex.blocks, "tables": ex.tables, "table_rows": ex.table_rows, "lists": ex.lists,
            "images": ex.images, "links": ex.links + ex.buttons, "title": ex.title.strip(), "meta_description": ex.meta_desc}


def parse_markdown(raw):
    blocks, tables, rows, lists, links, images = [], 0, 0, 0, [], []
    in_table = in_list = False
    para = []

    def flush():
        if para:
            blocks.append(("p", " ".join(para).strip()))
            para.clear()

    for line in raw.splitlines():
        s = line.strip()
        for alt, _ in re.findall(r"!\[([^\]]*)\]\(([^)]*)\)", s):
            images.append(alt or None)
        links += [t for t in re.findall(r"(?<!!)\[([^\]]+)\]\([^)]*\)", s)]
        s_clean = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
        s_clean = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s_clean)
        m = re.match(r"^(#{1,6})\s+(.*)", s_clean)
        if not s_clean:
            flush(); in_table = in_list = False
            continue
        if m:
            flush(); blocks.append((f"h{len(m.group(1))}", m.group(2).strip("# ").strip()))
            continue
        if s_clean.startswith("|"):
            flush()
            if not in_table:
                tables += 1; in_table = True
            if not re.fullmatch(r"\|?[\s:\-|]+\|?", s_clean):
                rows += 1
                for c in [c.strip() for c in s_clean.strip("|").split("|") if c.strip()]:
                    blocks.append(("cell", c))
            continue
        lm = re.match(r"^([-*+]|\d+[.)])\s+(.*)", s_clean)
        if lm:
            flush()
            if not in_list:
                lists += 1; in_list = True
            blocks.append(("li", lm.group(2)))
            continue
        para.append(s_clean)
    flush()
    title = next((t for k, t in blocks if k == "h1"), "")
    return {"blocks": blocks, "tables": tables, "table_rows": rows, "lists": lists, "images": images,
            "links": links, "title": title, "meta_description": ""}


def parse_text(raw):
    blocks = [("p", re.sub(r"\s+", " ", b).strip()) for b in re.split(r"\n\s*\n", raw) if b.strip()]
    return {"blocks": blocks, "tables": 0, "table_rows": 0, "lists": 0, "images": [], "links": [], "title": "", "meta_description": ""}


def words(text):
    return re.findall(r"[A-Za-zÀ-ÿ0-9][\w'’\-/.]*", text)


def sentences(text):
    return [s.strip() for s in SENT_SPLIT_RE.split(text) if s.strip()]


def find_terms(text_l, terms):
    found = {}
    for t in terms:
        n = len(re.findall(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])", text_l))
        if n:
            found[t] = n
    return found


def analyse(doc, source_kind):
    blocks = doc["blocks"]
    body_blocks = [(k, t) for k, t in blocks if not re.fullmatch(r"h[1-6]", k)]
    full_text = " ".join(t for _, t in blocks)
    body_text = " ".join(t for _, t in body_blocks)
    text_l = full_text.lower()
    wc = len(words(body_text))
    per100 = (lambda n: round(n * 100 / wc, 2) if wc else 0.0)

    headings = [(int(k[1]), t) for k, t in blocks if re.fullmatch(r"h[1-6]", k)]
    h1s = [t for lvl, t in headings if lvl == 1]
    sub = [t for lvl, t in headings if lvl in (2, 3)]
    q_heads = [t for t in sub if t.strip().endswith("?") or QUESTION_START_RE.match(t.strip())]
    generic = [t for t in sub if t.strip().lower().rstrip(":") in GENERIC_HEADINGS]
    skipped_levels = any(b - a > 1 for (a, _), (b, _) in zip(headings, headings[1:]))

    # Lead: first body text after the first H1 (or start of doc)
    start = 0
    for i, (k, _) in enumerate(blocks):
        if k == "h1":
            start = i + 1
            break
    lead_text = " ".join(t for k, t in blocks[start:] if not re.fullmatch(r"h[1-6]", k))
    lead_words = words(lead_text)[:100]
    first100 = " ".join(lead_words)
    lead_sents = sentences(lead_text)
    lead_sentence = lead_sents[0] if lead_sents else ""

    # Sections (H2/H3)
    sections, cur = [], None
    for k, t in blocks:
        if k in ("h2", "h3"):
            if cur:
                sections.append(cur)
            cur = {"heading": t, "level": int(k[1]), "text": []}
        elif cur is not None and not re.fullmatch(r"h[1-6]", k):
            cur["text"].append(t)
    if cur:
        sections.append(cur)
    sec_out = []
    for s in sections:
        txt = " ".join(s["text"])
        ss = sentences(txt)
        first = ss[0] if ss else ""
        sec_out.append({
            "heading": s["heading"][:120], "level": s["level"], "words": len(words(txt)),
            "first_sentence": first[:240], "first_sentence_words": len(words(first)),
            "first_sentence_has_fact": bool(NUM_UNIT_RE.search(first) or STANDARD_RE.search(first)),
            "first_sentence_context_dependent": bool(re.match(r"^(it|this|these|they|that)\b", first.strip(), re.I)),
        })

    paras = [t for k, t in blocks if k == "p"]
    long_paras = [p[:80] + "…" for p in paras if len(sentences(p)) > 4 or len(words(p)) > 100]
    all_sents = sentences(body_text)
    avg_sent = round(sum(len(words(s)) for s in all_sents) / len(all_sents), 1) if all_sents else 0
    pron_start = sum(1 for s in all_sents if re.match(r"^(it|this|these|they|that)\b", s, re.I))

    num_units = NUM_UNIT_RE.findall(body_text)
    years = [int(y) for y in YEAR_RE.findall(full_text)]
    fluff = find_terms(text_l, FLUFF)
    hedges = find_terms(text_l, HEDGES)
    ctx = find_terms(text_l, CONTEXT_DEP)
    link_texts = [l for l in doc["links"] if l]
    vague_cta = [l for l in link_texts if l.strip().lower().rstrip(" >→.!") in VAGUE_CTAS]
    imgs = doc["images"]
    alt_missing = sum(1 for a in imgs if a is None or not a.strip())
    alt_lens = [len(a.strip()) for a in imgs if a and a.strip()]

    flags = []
    if source_kind == "url" and wc < 150:
        flags.append("OUT-OF-SCOPE OBSERVATION: very little text in raw HTML; content may be client-side rendered or in images. Route to SE Digital; score only the content you can see.")
    if not lead_sentence:
        flags.append("No body text found after H1.")
    if len(h1s) != 1 and headings:
        flags.append(f"H1 count = {len(h1s)} (expected 1).")
    if per100(sum(fluff.values())) > 1.5:
        flags.append("Fluff density > 1.5 per 100 words → candidate penalty 'fluff_density'.")
    if len(vague_cta) >= 3:
        flags.append("≥3 vague CTAs → candidate penalty 'cta_overload'.")

    return {
        "source_kind": source_kind,
        "title": doc["title"][:200], "meta_description": doc["meta_description"][:300],
        "word_count": wc,
        "lead": {"first_sentence": lead_sentence[:300], "first_sentence_words": len(words(lead_sentence)),
                 "definition_pattern_in_first_2_sentences": bool(DEFINITION_RE.search(" ".join(lead_sents[:2]))),
                 "facts_in_first_100_words": len(NUM_UNIT_RE.findall(first100)), "first_100_words": first100},
        "headings": {"h1": h1s[:3], "count_by_level": {f"h{l}": sum(1 for x, _ in headings if x == l) for l in range(1, 7)},
                     "h2_h3_count": len(sub), "question_style_ratio": round(len(q_heads) / len(sub), 2) if sub else 0.0,
                     "generic_headings": generic, "skipped_levels": skipped_levels, "outline": [f"H{l}: {t[:90]}" for l, t in headings[:60]]},
        "sections": sec_out[:40],
        "structure": {"paragraphs": len(paras), "long_paragraphs": len(long_paras), "long_paragraph_samples": long_paras[:5],
                      "lists": doc["lists"], "list_items": sum(1 for k, _ in blocks if k == "li"),
                      "tables": doc["tables"], "table_rows": doc["table_rows"], "avg_sentence_words": avg_sent,
                      "pronoun_start_sentence_ratio": round(pron_start / len(all_sents), 2) if all_sents else 0.0},
        "facts": {"numbers_with_units": len(num_units), "numbers_with_units_per_100w": per100(len(num_units)),
                  "percentages": len(PCT_RE.findall(body_text)),
                  "standards_refs": sorted(set(m.strip() for m in STANDARD_RE.findall(full_text)))[:30],
                  "certifications": sorted(set(CERT_RE.findall(full_text)))[:20]},
        "evidence": {"quotations": len(QUOTE_RE.findall(full_text)), "attribution_phrases": len(ATTRIBUTION_RE.findall(full_text))},
        "freshness": {"years_mentioned": sorted(set(years))[-10:], "latest_year": max(years) if years else None,
                      "date_labels": sorted(set(m.lower() for m in DATE_LABEL_RE.findall(full_text)))[:10]},
        "tone": {"fluff_terms": fluff, "fluff_per_100w": per100(sum(fluff.values())), "hedges": hedges},
        "self_containment": {"context_dependent_phrases": ctx},
        "links_ctas": {"links_and_buttons": len(link_texts), "vague_ctas": vague_cta[:15],
                       "descriptive_samples": [l for l in link_texts if len(words(l)) >= 4][:10]},
        "images": {"count": len(imgs), "missing_alt": alt_missing,
                   "alt_outside_80_140_chars": sum(1 for n in alt_lens if n < 80 or n > 140)},
        "flags": flags,
        "note": "Deterministic signals only; use as evidence for the judge. Not a score.",
    }


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (GEO content check)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        ctype = r.headers.get("Content-Type", "")
        if "html" not in ctype:
            sys.exit(f"Not an HTML page (Content-Type: {ctype}). Download the file and use --file.")
        charset = r.headers.get_content_charset() or "utf-8"
        return r.read().decode(charset, errors="replace")


def pretty(m):
    L = [f"Title: {m['title']}", f"Words: {m['word_count']}",
         f"Lead sentence ({m['lead']['first_sentence_words']} w): {m['lead']['first_sentence']}",
         f"Definition pattern in lead: {m['lead']['definition_pattern_in_first_2_sentences']} | facts in first 100 words: {m['lead']['facts_in_first_100_words']}",
         f"H1: {m['headings']['h1']} | H2/H3: {m['headings']['h2_h3_count']} | question-style: {m['headings']['question_style_ratio']} | generic: {m['headings']['generic_headings']}",
         f"Lists: {m['structure']['lists']} ({m['structure']['list_items']} items) | tables: {m['structure']['tables']} | long paragraphs: {m['structure']['long_paragraphs']} | avg sentence: {m['structure']['avg_sentence_words']} w",
         f"Numbers with units: {m['facts']['numbers_with_units']} ({m['facts']['numbers_with_units_per_100w']}/100w) | standards: {m['facts']['standards_refs']}",
         f"Quotes: {m['evidence']['quotations']} | attribution phrases: {m['evidence']['attribution_phrases']}",
         f"Latest year: {m['freshness']['latest_year']} | date labels: {m['freshness']['date_labels']}",
         f"Fluff ({m['tone']['fluff_per_100w']}/100w): {m['tone']['fluff_terms']}",
         f"Hedges: {m['tone']['hedges']} | context-dependent: {m['self_containment']['context_dependent_phrases']}",
         f"Vague CTAs: {m['links_ctas']['vague_ctas']}",
         f"Images: {m['images']['count']} (missing alt {m['images']['missing_alt']})", "Sections:"]
    for s in m["sections"]:
        L.append(f"  [H{s['level']}] {s['heading']} — {s['words']} w; first sentence {s['first_sentence_words']} w; fact={s['first_sentence_has_fact']}")
    L += ["Flags:"] + [f"  - {f}" for f in m["flags"]]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--file")
    g.add_argument("--url")
    ap.add_argument("--format", choices=["auto", "html", "md", "text"], default="auto")
    ap.add_argument("--pretty", action="store_true", help="human-readable summary instead of JSON")
    a = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    if a.url:
        raw, kind, fmt = fetch(a.url), "url", "html"
    else:
        with open(a.file, encoding="utf-8", errors="replace") as f:
            raw = f.read()
        kind = "file"
        fmt = a.format
        if fmt == "auto":
            low = a.file.lower()
            fmt = "html" if low.endswith((".html", ".htm")) or re.search(r"<(html|body|div|p|h1)\b", raw[:5000], re.I) else (
                "md" if low.endswith((".md", ".markdown")) or re.search(r"^#{1,6}\s", raw, re.M) else "text")
    doc = parse_html(raw) if fmt == "html" else parse_markdown(raw) if fmt == "md" else parse_text(html.unescape(raw))
    m = analyse(doc, kind)
    print(pretty(m) if a.pretty else json.dumps(m, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

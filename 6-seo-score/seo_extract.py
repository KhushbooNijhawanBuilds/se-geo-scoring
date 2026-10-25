#!/usr/bin/env python3
"""Deterministic fact extractor for the Blog SEO Score v1 (stdlib only, Python 3.9+).

Pulls the objectively measurable facts from a blog page so mechanical checks are
COMPUTED, not left to the AI judge. It never judges meaning (intent, coverage, E-E-A-T).

Inputs (either or both):
  --md   corpus markdown file (header HTML comments with URL, html_title, meta JSON, jsonld types)
  --html raw HTML of the page (preferred: gives canonical, robots, hreflang, JSON-LD, links, img src)
  --keyword "primary topic phrase"  (optional; enables the S6 placement checks)

Output: JSON with  facts{...}  and  computed_checks{"S2.c1": {"result","evidence"}, ...}
Checks not computable from the input are returned as "na" with the reason; the judge must
not invent them. See SEO_Scoring_Standard_v1.md section 6 for which checks are computed vs judged.

Usage:
  python3 seo_extract.py --html page.html [--md corpus.md] [--keyword "data center cooling"] [--brand "Schneider Electric Blog"]
  python3 seo_extract.py --md corpus.md
"""
import argparse
import json
import re
import sys
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urlsplit, parse_qs

STOP = set("""a an the and or of to in on for with by at from as is are be was were it its this that these those
how why what when where which who your you we our us can will not no vs via into over than about up out new""".split())
GENERIC_ANCHORS = {"click here", "here", "read more", "learn more", "more", "this", "link", "this page",
                   "find out more", "see more", "download", "continue reading"}
SOCIAL_HOSTS = ("facebook.com", "linkedin.com", "twitter.com", "x.com", "instagram.com", "youtube.com", "pinterest.")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

# Approximate Arial 16-18px glyph widths (px at 18px) for a title-width ESTIMATE only.
# Basis: Screaming Frog 2014 reverse-engineering (18px Arial) and current tool limits ~561-600px.
# Not Google data. Report as an estimate.
NARROW, WIDE = set("ilj.,;:'!|tfI ()[]-/"), set("mwMWOQGDHNU@%")


def est_px(text):
    w = 0.0
    for ch in text:
        if ch in NARROW:
            w += 5.0
        elif ch in WIDE:
            w += 15.0
        elif ch.isupper() or ch.isdigit():
            w += 11.5
        else:
            w += 9.0
    return round(w)


def words(text):
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", text or "")


def content_tokens(text):
    return [w.lower().strip("'’-") for w in words(text) if w.lower() not in STOP and len(w) > 1]


def stem(w):
    """Light suffix stripping so close variants match (recycled/recycling, centers/center). Not a full stemmer."""
    for suf in ("ing", "ed", "es", "s"):
        if len(w) > 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


# ---------------------------------------------------------------- HTML parsing
class Node:
    __slots__ = ("tag", "attrs", "children", "parent", "text")

    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.parent, self.children, self.text = tag, dict(attrs), parent, [], []


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", [], None)
        self.cur = self.root
        self.scripts = []  # (type, text)
        self._script = None

    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur)
        self.cur.children.append(n)
        if tag == "script":
            self._script = [dict(attrs).get("type", ""), ""]
        if tag not in VOID:
            self.cur = n

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))

    def handle_endtag(self, tag):
        if tag == "script" and self._script is not None:
            self.scripts.append(tuple(self._script))
            self._script = None
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        if self._script is not None:
            self._script[1] += data
            return
        self.cur.children.append(data)


def walk(n):
    yield n
    for c in n.children:
        if isinstance(c, Node):
            yield from walk(c)


def text_of(n, skip=("script", "style", "noscript", "svg")):
    out = []
    for c in n.children:
        if isinstance(c, str):
            out.append(c)
        elif c.tag not in skip:
            out.append(text_of(c, skip))
            if c.tag in ("p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "div", "br", "tr"):
                out.append(" ")
    return re.sub(r"\s+", " ", "".join(out)).strip()


def has_class(n, frag):
    return frag in (n.attrs.get("class") or "")


def find_content(root):
    """Article body scope. WordPress/blog.se.com: wp-block-* children of <article> before tags/comments.
    Fallback: <article>, then <main>, then <body>."""
    art = next((n for n in walk(root) if n.tag == "article"), None) or \
        next((n for n in walk(root) if n.tag == "main"), None) or \
        next((n for n in walk(root) if n.tag == "body"), root)
    stop_marks = ("tags", "comment-respond", "related-posts", "post-share", "post-meta", "post-category")
    blocks = []

    def collect(n):
        for c in n.children:
            if not isinstance(c, Node):
                continue
            cls = c.attrs.get("class") or ""
            if any(m in cls.split() or cls.startswith(m) for m in stop_marks) or c.attrs.get("id") == "respond":
                continue
            if "wp-block-" in cls or c.tag in ("p", "ul", "ol", "table", "figure", "blockquote") or \
                    (c.tag in ("h2", "h3", "h4", "h5", "h6") and "wp-block-heading" in cls):
                blocks.append(c)
            else:
                collect(c)
    collect(art)
    return art, blocks


def parse_html(html):
    tb = TreeBuilder()
    tb.feed(html)
    root = tb.root
    head = next((n for n in walk(root) if n.tag == "head"), root)
    f = {}
    titles = [text_of(n) for n in walk(head) if n.tag == "title"]
    f["title_tags"] = titles
    metas = [n.attrs for n in walk(root) if n.tag == "meta"]
    f["meta_descriptions"] = [unescape(m.get("content", "")) for m in metas if (m.get("name") or "").lower() == "description"]
    f["meta_robots"] = [m.get("content", "") for m in metas if (m.get("name") or "").lower() in ("robots", "googlebot")]
    f["viewport"] = next((m.get("content", "") for m in metas if (m.get("name") or "").lower() == "viewport"), None)
    f["og"] = {m["property"]: unescape(m.get("content", "")) for m in metas if (m.get("property") or "").startswith(("og:", "article:"))}
    links = [n.attrs for n in walk(head) if n.tag == "link"]
    f["canonicals"] = [l.get("href") for l in links if "canonical" in (l.get("rel") or "").lower().split()]
    f["hreflang"] = [{"hreflang": l.get("hreflang"), "href": l.get("href")} for l in links if l.get("hreflang")]
    # JSON-LD
    graph = []
    for typ, txt in tb.scripts:
        if "ld+json" in (typ or ""):
            try:
                d = json.loads(txt)
            except Exception:
                continue
            items = d if isinstance(d, list) else d.get("@graph", [d]) if isinstance(d, dict) else []
            graph.extend(i for i in items if isinstance(i, dict))
    f["jsonld_types"] = sorted({t for i in graph for t in (i.get("@type") if isinstance(i.get("@type"), list) else [i.get("@type")]) if t})
    art_ld = next((i for i in graph if any(t in ("Article", "BlogPosting", "NewsArticle", "TechArticle")
                                           for t in (i.get("@type") if isinstance(i.get("@type"), list) else [i.get("@type")]))), None)
    by_id = {i.get("@id"): i for i in graph if i.get("@id")}
    if art_ld:
        auth = art_ld.get("author")
        auth = auth[0] if isinstance(auth, list) and auth else auth
        if isinstance(auth, dict) and auth.get("@id") in by_id:
            auth = dict(by_id[auth["@id"]], **{k: v for k, v in auth.items() if k != "@id"})
        img = art_ld.get("image")
        f["article_ld"] = {
            "type": art_ld.get("@type"), "headline": art_ld.get("headline"),
            "datePublished": art_ld.get("datePublished"), "dateModified": art_ld.get("dateModified"),
            "image": bool(img) or bool(art_ld.get("thumbnailUrl")),
            "author_name": (auth or {}).get("name") if isinstance(auth, dict) else None,
            "author_type": (auth or {}).get("@type") if isinstance(auth, dict) else None,
            "author_url": (auth or {}).get("url") if isinstance(auth, dict) else None,
            "author_sameAs": (auth or {}).get("sameAs") if isinstance(auth, dict) else None,
        }
    else:
        f["article_ld"] = None
    # visible elements
    f["h1_all"] = [text_of(n) for n in walk(root) if n.tag == "h1"]
    art, blocks = find_content(root)
    f["time_elements"] = [n.attrs.get("datetime") for n in walk(art) if n.tag == "time" and n.attrs.get("datetime")]
    author_links = [(text_of(n), n.attrs.get("href")) for n in walk(art) if n.tag == "a" and
                    ("author" in (n.attrs.get("class") or "") or "/author/" in (n.attrs.get("href") or ""))]
    f["byline_links"] = [{"text": t, "href": h} for t, h in author_links]
    heads, imgs, alinks, body_text = [], [], [], []
    for b in blocks:
        for n in walk(b):
            if n.tag in ("h2", "h3", "h4", "h5", "h6"):
                heads.append({"level": int(n.tag[1]), "text": text_of(n)})
            elif n.tag == "img":
                imgs.append({"src": n.attrs.get("src"), "alt": n.attrs.get("alt"), "role": n.attrs.get("role")})
            elif n.tag == "a" and n.attrs.get("href"):
                alinks.append({"href": unescape(n.attrs.get("href")), "anchor": text_of(n), "rel": n.attrs.get("rel") or ""})
        if b.tag not in ("h2", "h3", "h4", "h5", "h6") and "wp-block-heading" not in (b.attrs.get("class") or ""):
            body_text.append(text_of(b))
    # hero/featured image inside article but outside blocks
    f["headings"], f["images"], f["links"] = heads, imgs, alinks
    f["body_text"] = " ".join(body_text)
    f["template_h2_in_article"] = [text_of(n) for n in walk(art) if n.tag == "h2" and "wp-block-heading" not in (n.attrs.get("class") or "")]
    return f


# ---------------------------------------------------------------- markdown corpus parsing
def parse_md(md):
    f = {}
    m = re.search(r"<!--\s*[^|]*\|[^|]*\|\s*(https?://\S+)\s*-->", md)
    f["url"] = m.group(1) if m else None
    m = re.search(r"html_title:\s*(.*?)\s*\|\s*meta:", md)
    f["title_tags"] = [m.group(1)] if m else []
    m = re.search(r"\|\s*meta:\s*(\{.*?\})\s*\|\s*jsonld:", md, re.S)
    meta = {}
    if m:
        try:
            meta = json.loads(m.group(1))
        except Exception:
            meta = {}
    f["meta_descriptions"] = [meta["description"]] if "description" in meta else []
    f["og"] = {k: v for k, v in meta.items() if k.startswith(("og:", "article:"))}
    f["time_elements"] = meta.get("time_elements", [])
    f["md_author"] = meta.get("author")
    m = re.search(r"jsonld:\s*\[(.*?)\]", md)
    f["jsonld_types"] = re.findall(r"'([^']+)'", m.group(1)) if m else []
    body = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    body = body.split("## Add a comment")[0]
    f["h1_all"] = re.findall(r"^# (.+)$", body, re.M)
    f["headings"] = [{"level": len(h), "text": t.strip()} for h, t in re.findall(r"^(#{2,6}) (.+)$", body, re.M)]
    f["images"] = [{"src": s, "alt": a, "role": None} for a, s in re.findall(r"!\[([^\]]*)\]\(([^)]*)\)", body)]
    f["links"] = [{"href": h, "anchor": a, "rel": ""} for a, h in re.findall(r"(?<!!)\[([^\]]+)\]\((https?://[^)]+)\)", body)]
    lines = [l for l in body.splitlines() if l.strip() and not l.startswith("#") and not l.startswith("![")]
    # drop the meta list (date / views / read time / author) directly under H1
    f["body_text"] = " ".join(l for l in lines if not re.match(r"^- (\w+ \d{1,2}, \d{4}|\d+ views|\d+ min read)$", l.strip()))
    f["visible_date_text"] = (re.search(r"^- ((January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})$", body, re.M) or [None, None])[1]
    return f


# ---------------------------------------------------------------- computed checks
MONTHS = {m: i for i, m in enumerate("January February March April May June July August September October November December".split(), 1)}


def day(s):
    if not s:
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return m.group(0)
    m = re.match(r"(\w+) (\d{1,2}), (\d{4})", s)
    if m and m.group(1) in MONTHS:
        return f"{m.group(3)}-{MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"
    return None


def R(result, evidence):
    return {"result": result, "evidence": evidence}


def compute(f, url, keyword, brand, source):
    C, facts = {}, {}
    # ---- URL
    u = urlsplit(url or "")
    path = u.path
    slug = [p for p in path.split("/") if p][-1] if path.strip("/") else ""
    slug_words = [w for w in re.split(r"[-_]", slug) if w]
    facts["url"] = {"url": url, "scheme": u.scheme, "host": u.netloc, "path": path, "slug": slug,
                    "slug_chars": len(slug), "slug_words": len(slug_words), "query": u.query, "fragment": u.fragment,
                    "date_in_path": bool(re.search(r"/\d{4}/\d{2}/(\d{2}/)?", path))}
    id_like = [w for w in slug_words if re.fullmatch(r"\d{5,}|[0-9a-f]{8,}", w)]
    C["S4.c1"] = R("fail" if (not slug_words or id_like) else "pass", f"slug '{slug}'" + (f"; ID-like tokens {id_like}" if id_like else ""))
    bad = [ch for ch in ("_", " ", "%") if ch in slug] + (["UPPERCASE"] if slug != slug.lower() else [])
    C["S4.c2"] = R("fail" if bad else "pass", f"slug '{slug}'" + (f"; problems {bad}" if bad else "; hyphens, lowercase"))
    sess = [k for k in parse_qs(u.query) if re.search(r"sess|sid|utm_|gclid|fbclid", k, re.I)]
    C["S4.c3"] = R("fail" if (u.query or u.fragment) else "pass",
                   f"query='{u.query}' fragment='{u.fragment}'" + (f" tracking/session keys {sess}" if sess else ""))
    C["S4.c4"] = R("pass" if 0 < len(slug) <= 60 else "fail", f"slug {len(slug)} chars, {len(slug_words)} words (convention <=60 chars)")
    rep = sorted({w for w in slug_words if w.lower() not in STOP and slug_words.count(w) > 1})
    facts["url"]["repeated_slug_words"] = rep  # S4.c5 is judged (spelling, language, topic match); repetition is a hint

    # ---- Title
    titles = [t for t in f.get("title_tags", []) if t is not None]
    t = titles[0] if titles else ""
    main_t = t
    brand_pos = None
    if brand and brand.lower() in t.lower():
        i = t.lower().rfind(brand.lower())
        brand_pos = "end" if i + len(brand) >= len(t) - 1 else ("start" if i <= 1 else "middle")
        main_t = re.sub(r"\s*[-|:–—]\s*$", "", t[:i]).strip() if brand_pos == "end" else t.replace(brand, "").strip(" -|:–—")
    facts["title"] = {"count": len(titles), "text": t, "chars": len(t), "est_px_18px_arial": est_px(t),
                      "main_text": main_t, "main_chars": len(main_t), "brand": brand, "brand_position": brand_pos,
                      "brand_occurrences": t.lower().count(brand.lower()) if brand else None}
    C["S2.c1"] = R("pass" if len(titles) == 1 and len(main_t.strip()) >= 10 else "fail",
                   f"{len(titles)} <title>; text '{t}'")
    px = est_px(t)
    ok_len = 30 <= len(t) <= 60 or (len(t) <= 65 and px <= 600)
    C["S2.c2"] = R("pass" if ok_len else "fail",
                   f"{len(t)} chars, ~{px}px est. (pass band 30-60 chars, or <=65 chars and <=600px; basis Zyppy rewrite data, Yoast 600px, Screaming Frog 30-60/561px)")
    if brand:
        occ = t.lower().count(brand.lower())
        C["S2.c3"] = R("pass" if occ <= 1 and brand_pos in (None, "end", "start") else "fail",
                       f"brand '{brand}' x{occ}, position {brand_pos}")
    toks = content_tokens(t.replace(brand or "\0", ""))
    reps = sorted({w for w in toks if toks.count(w) >= 3})
    years = [int(y) for y in re.findall(r"\b(20\d{2})\b", t)]
    mod_year = (day(f.get("og", {}).get("article:modified_time")) or "0000")[:4]
    stale = [y for y in years if mod_year.isdigit() and int(mod_year) > 0 and y < int(mod_year)]
    C["S2.c5"] = R("fail" if reps or stale else "pass", f"tokens repeated >=3: {reps or 'none'}; years {years or 'none'}" + (f" older than modified year {mod_year}" if stale else ""))
    h1s = f.get("h1_all", [])
    h1 = h1s[0] if h1s else ""
    ht, tt = set(content_tokens(h1)), set(content_tokens(main_t))
    overlap = round(len(ht & tt) / len(tt), 2) if tt else 0.0
    nums_t, nums_h = set(re.findall(r"\b\d+\b", main_t)), set(re.findall(r"\b\d+\b", h1))
    num_ok = nums_t <= nums_h
    facts["title"].update({"h1": h1, "title_h1_token_overlap": overlap, "title_equals_h1": main_t.strip() == h1.strip()})
    C["S2.c6"] = R("pass" if h1 and overlap >= 0.5 and num_ok else "fail",
                   f"title main '{main_t}' vs H1 '{h1}': {int(overlap*100)}% of title content words in H1; numbers title {sorted(nums_t)} H1 {sorted(nums_h)}")
    if keyword:
        kt = content_tokens(keyword)
        front = " ".join(content_tokens(main_t[:45]))
        hit = all(k in front for k in kt)
        C["S2.c4"] = R("pass" if hit else "fail", f"keyword '{keyword}' {'within' if hit else 'not within'} first ~45 chars of '{main_t[:45]}'")

    # ---- Meta description
    md = f.get("meta_descriptions", [])
    d = md[0] if md else ""
    facts["meta_description"] = {"count": len(md), "text": d, "chars": len(d), "est_px": est_px(d) * 0.78 if d else 0}
    C["S3.c1"] = R("pass" if len(md) == 1 and d.strip() else "fail", f"{len(md)} meta description(s)")
    C["S3.c2"] = R("pass" if 120 <= len(d) <= 160 else "fail",
                   f"{len(d)} chars (pass band 120-160; basis Yoast 121-156, Screaming Frog 70-155, Portent first ~120 chars on mobile; Google sets no limit)")
    C["S3.c3_partial"] = R("fail" if d.strip() and d.strip() == main_t.strip() else "na",
                           "identical to title" if d.strip() == main_t.strip() and d else "not identical to title; judge decides if it summarises this page")
    dt = content_tokens(d)
    dreps = sorted({w for w in dt if dt.count(w) >= 3})
    C["S3.c5"] = R("fail" if dreps or not d else "pass", f"tokens repeated >=3 in meta: {dreps or 'none'}")
    if keyword:
        hit = all(k in " ".join(dt) for k in content_tokens(keyword))
        C["S3.c4"] = R("pass" if hit else "fail", f"keyword '{keyword}' {'in' if hit else 'not in'} meta description")

    # ---- Headings
    heads = f.get("headings", [])
    body = f.get("body_text", "")
    nwords = len(words(body))
    content_heads = [h for h in heads if h["level"] in (2, 3)]
    facts["headings"] = {"h1_count": len(h1s), "h1_texts": h1s, "list": heads, "body_words": nwords,
                         "words_per_subhead": round(nwords / max(1, len(content_heads))),
                         "template_h2_in_article": f.get("template_h2_in_article")}
    C["S5.c1"] = R("pass" if len(h1s) == 1 else "fail", f"{len(h1s)} H1: {h1s}")
    wps = nwords / max(1, len(content_heads))
    C["S5.c2"] = R("pass" if nwords <= 300 or (content_heads and wps <= 350) else "fail",
                   f"{nwords} body words, {len(content_heads)} H2/H3 -> ~{round(wps)} words per subhead (pass <=350; basis Yoast <=300 words per section, Starter Guide 'break long content into sections')")
    if f.get("template_h2_in_article") is not None:
        th = f["template_h2_in_article"]
        C["S5.c4"] = R("fail" if th else "pass", f"non-content H2s inside <article>: {th[:6]}" if th else "no template H2s inside <article>")

    # ---- Keyword placement (S6) only with a keyword
    first150 = " ".join(words(body)[:150])
    facts["intro_first_150_words"] = first150
    if keyword:
        kt = content_tokens(keyword)

        def has(s):
            st = {stem(w) for w in content_tokens(s)}
            return all(stem(k) in st for k in kt)
        C["S6.c1"] = R("pass" if has(main_t) else "fail", f"title: '{main_t}'")
        C["S6.c2"] = R("pass" if has(h1) else "fail", f"H1: '{h1}'")
        C["S6.c3"] = R("pass" if has(first150) else "fail", f"first 150 words {'contain' if has(first150) else 'lack'} all of {kt}")
        sh = [h["text"] for h in content_heads if has(h["text"])]
        C["S6.c4"] = R("pass" if sh else "fail", f"subheads with topic: {sh[:3] or 'none'}")
        phrase = keyword.lower()
        cnt = body.lower().count(phrase)
        dens = round(100 * cnt * len(words(keyword)) / max(1, nwords), 2)
        sh_share = len(sh) / max(1, len(content_heads))
        stuffed = dens > 3.0 or (len(content_heads) >= 4 and sh_share > 0.5)
        C["S6.c5"] = R("fail" if stuffed else "pass",
                       f"exact phrase x{cnt} (~{dens}% of words; stuffing trigger >3%); in {int(sh_share*100)}% of subheads (trigger >50%). Density is a stuffing tripwire only, never a target.")

    # ---- Dates (S10)
    og = f.get("og", {})
    ld = f.get("article_ld") or {}
    pub = day(ld.get("datePublished")) or day(og.get("article:published_time"))
    mod = day(ld.get("dateModified")) or day(og.get("article:modified_time"))
    vis = day(f.get("visible_date_text")) or (day(f["time_elements"][0]) if f.get("time_elements") else None)
    facts["dates"] = {"visible": vis, "published_markup": pub, "modified_markup": mod,
                      "source": "JSON-LD" if ld.get("datePublished") else "article:published_time"}
    C["S10.c1"] = R("pass" if vis else "fail", f"visible date {vis}" if vis else "NOT FOUND")
    C["S10.c2"] = R("pass" if vis and pub and vis == pub else ("na" if not pub else "fail"), f"visible {vis} vs markup published {pub}")
    C["S10.c3"] = R("pass" if pub and mod and mod >= pub else ("na" if not mod else "fail"), f"published {pub}, modified {mod}")
    # c4 needs to know whether an 'Updated' label is visible; only computable for the gap
    if pub and mod:
        from datetime import date
        gap = (date(*map(int, mod.split("-"))) - date(*map(int, pub.split("-")))).days
        facts["dates"]["modified_minus_published_days"] = gap
        if gap < 7:
            C["S10.c4"] = R("na", f"modified {gap} day(s) after publication (<7): no visible Updated label expected")

    # ---- Links (S11, S12)
    host = u.netloc
    links = f.get("links", [])
    internal, external = [], []
    for l in links:
        lh = urlsplit(l["href"]).netloc
        if l["href"].startswith(("mailto:", "tel:", "#")):
            continue
        (internal if (not lh or lh == host or lh.endswith(("se.com", "schneider-electric.com"))) else external).append(l)
    utm = [l["href"] for l in internal if re.search(r"[?&](utm_|gclid|fbclid|sourceId)", l["href"])]
    generic = [l["anchor"] for l in links if l["anchor"].strip().lower().rstrip(".") in GENERIC_ANCHORS or re.match(r"^https?://", l["anchor"].strip())]
    by_anchor = {}
    for l in internal + external:
        by_anchor.setdefault(l["anchor"].strip().lower(), set()).add(l["href"].split("?")[0].split("#")[0])
    ambiguous = [a for a, hs in by_anchor.items() if len(hs) > 1]
    facts["links"] = {"in_body_total": len(links), "internal": internal, "external": external,
                      "internal_with_tracking_params": utm, "generic_anchors": generic, "same_anchor_different_targets": ambiguous}
    if source == "md" and not links:
        for k in ("S11.c1", "S11.c3", "S11.c4", "S11.c5", "S12.c2"):
            C[k] = R("na", "links not present in the markdown input; supply --html")
    else:
        C["S11.c1"] = R("pass" if len(internal) >= 3 else "fail", f"{len(internal)} in-body internal links (blog.se.com/se.com) (pass >=3; heuristic, Google gives no number)")
        C["S11.c3"] = R("fail" if generic or ambiguous else "pass",
                        f"generic anchors {generic or 'none'}; same anchor -> different URLs {ambiguous or 'none'}")
        C["S11.c4"] = R("fail" if utm else "pass", f"internal links with tracking/ID params: {utm or 'none'}")
        bad_href = [l["href"] for l in links if l["href"].lower().startswith("javascript")]
        C["S11.c5"] = R("fail" if bad_href else "pass", f"non-crawlable hrefs: {bad_href or 'none'}; all in-body links are <a href>")
        ext = [l for l in external if not any(s in l["href"] for s in SOCIAL_HOSTS)]
        allnf = ext and all("nofollow" in l["rel"] for l in ext)
        C["S12.c2"] = R("fail" if allnf else ("pass" if ext else "na"),
                        f"{len(ext)} outbound editorial links; rel values {[l['rel'] for l in ext][:6]}")

    # ---- Images (S13)
    imgs = [i for i in f.get("images", [])]
    facts["images"] = imgs
    if imgs:
        empty = [i for i in imgs if not (i.get("alt") or "").strip()]
        C["S13.c1"] = R("fail" if empty else "pass", f"{len(imgs)-len(empty)}/{len(imgs)} content images have non-empty alt" +
                        (f"; empty: {[ (i.get('src') or '')[-60:] for i in empty][:5]}" if empty else ""))
        long_alt = [i["alt"] for i in imgs if i.get("alt") and len(i["alt"]) > 125]
        if long_alt:
            C["S13.c2_partial"] = R("fail", f"alt over 125 chars: {long_alt[:2]}")
        srcs = [i.get("src") or "" for i in imgs if i.get("src") and i["src"] != "img"]
        if srcs:
            def descriptive(s):
                name = re.sub(r"\.\w+$", "", s.rsplit("/", 1)[-1])
                name = re.sub(r"-\d+x\d+$", "", name)
                ws = [w for w in re.split(r"[-_\s]+", name) if w and not re.fullmatch(r"\d+|resized|scaled|small|img|image|dsc|getty(images)?|shutterstock|adobestock|istock", w, re.I)]
                return len(ws) >= 2 and not re.search(r"(GettyImages|shutterstock|AdobeStock|iStock|IMG_|DSC)", name, re.I)
            nd = [s.rsplit("/", 1)[-1] for s in srcs if not descriptive(s)]
            C["S13.c3"] = R("fail" if nd else "pass", f"non-descriptive filenames: {nd[:5] or 'none'}")
        else:
            C["S13.c3"] = R("na", "image src not in input; supply --html")
    else:
        C["S13.c1"] = R("na", "no content images found")

    # ---- Structured data & OG (S14)
    types = f.get("jsonld_types", [])
    has_art = any(x in types for x in ("Article", "BlogPosting", "NewsArticle", "TechArticle"))
    if f.get("article_ld") is not None or source == "html":
        miss = [k for k in ("headline", "datePublished", "dateModified", "image") if not ld.get(k)]
        C["S14.c1"] = R("pass" if ld and not miss else "fail", f"{ld.get('type') if ld else 'no Article/BlogPosting'}; missing {miss or 'none'}")
        generic_author = (ld.get("author_name") or "").strip().lower() in ("guest blogger", "admin", "editor", "staff", "team", "guest")
        C["S14.c2"] = R("pass" if ld and ld.get("author_name") and not generic_author and (ld.get("author_url") or ld.get("author_sameAs")) else "fail",
                        f"author {ld.get('author_type')} '{ld.get('author_name')}', url={ld.get('author_url')}, sameAs={ld.get('author_sameAs')}" if ld else "NOT FOUND")
        vis_author = (f.get("byline_links") or [{}])[0].get("text") or f.get("md_author")
        hl = (ld.get("headline") or "").strip()
        ok = ld and (hl == h1.strip() or hl == main_t.strip()) and (ld.get("author_name") or "").strip() == (vis_author or "").strip() and pub == vis
        C["S14.c3"] = R("pass" if ok else "fail", f"markup headline '{hl}' vs H1/title; markup author '{ld.get('author_name')}' vs byline '{vis_author}'; dates {pub} vs {vis}")
    else:
        C["S14.c1"] = R("pass" if has_art else "fail", f"JSON-LD types {types} (field-level check needs --html)")
    C["S14.c4"] = R("pass" if "BreadcrumbList" in types else "fail", f"JSON-LD types {types}")
    req = ["og:title", "og:type", "og:image", "og:url"]
    if source == "html":
        miss = [k for k in req if not og.get(k)]
        canon = (f.get("canonicals") or [None])[0]
        C["S14.c5"] = R("pass" if not miss and og.get("og:url") == canon else "fail",
                        f"missing {miss or 'none'}; og:url {'=' if og.get('og:url') == canon else '!='} canonical; og:title '{og.get('og:title')}'")
    else:
        C["S14.c5"] = R("na" if not og.get("og:title") else "na", "og:type/og:image/og:url not in markdown header; supply --html")

    # ---- Technical eligibility (only what HTML shows)
    E = {}
    if source == "html":
        rb = " ".join(f.get("meta_robots", [])).lower()
        E["E2"] = R("fail" if ("noindex" in rb or "none" in rb.split(",")) else "pass", f"meta robots '{rb}' (X-Robots-Tag and robots.txt need the HTTP response)")
        cs = f.get("canonicals", [])
        E["E3"] = R("pass" if len(cs) == 1 and cs[0] == url and cs[0].startswith("https://") else "fail", f"canonicals {cs}; page URL {url}")
        E["E4"] = R("na", "no hreflang tags") if not f.get("hreflang") else R("na", f"{len(f['hreflang'])} hreflang tags; reciprocity needs a crawl: {f['hreflang'][:4]}")
        E["E5"] = R("pass" if (url or "").startswith("https://") else "fail", f"scheme {u.scheme}")
        vp = f.get("viewport") or ""
        E["E6"] = R("pass" if "width=device-width" in vp else "fail", f"viewport '{vp}' (content parity needs a mobile render)")
        E["E7"] = R("fail" if ("nosnippet" in rb or "max-snippet:0" in rb or "noarchive" in rb) else "pass", f"snippet directives in '{rb}'")
        E["E8"] = R("pass" if nwords >= 150 else "fail", f"{nwords} body words in server HTML")
    return facts, C, E


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--md")
    ap.add_argument("--html")
    ap.add_argument("--url", help="page URL (taken from the .md header if omitted)")
    ap.add_argument("--keyword")
    ap.add_argument("--brand", default="Schneider Electric Blog")
    a = ap.parse_args()
    if not (a.md or a.html):
        ap.error("give --md and/or --html")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    f, url, src = {}, a.url, "md"
    if a.md:
        f = parse_md(open(a.md, encoding="utf-8").read())
        url = url or f.get("url")
    if a.html:
        h = parse_html(open(a.html, encoding="utf-8", errors="replace").read())
        vis = f.get("visible_date_text")
        md_author = f.get("md_author")
        f.update(h)
        f["visible_date_text"] = vis
        f["md_author"] = md_author
        src = "html"
        url = url or (h.get("canonicals") or [None])[0]
    facts, checks, elig = compute(f, url, a.keyword, a.brand, src)
    facts["og"] = f.get("og")
    facts["jsonld_types"] = f.get("jsonld_types")
    facts["article_ld"] = f.get("article_ld")
    facts["canonicals"] = f.get("canonicals")
    facts["meta_robots"] = f.get("meta_robots")
    facts["hreflang"] = f.get("hreflang")
    facts["byline_links"] = f.get("byline_links")
    print(json.dumps({"source": src, "facts": facts, "computed_checks": checks, "computed_eligibility": elig},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

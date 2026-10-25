"""Fetch each inventory URL, isolate main content, convert to structured markdown.
Usage: python -E -P build_corpus.py <inventory.xlsx> <outdir>
Writes <outdir>/<NN>_<type>.md (content), <outdir>/<NN>_<type>.html (raw), and index.json.
"""
import sys, os, re, json, time, urllib.request
from html.parser import HTMLParser
import openpyxl

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
SKIP = {"script", "style", "noscript", "nav", "footer", "aside", "form", "svg", "template", "iframe", "select", "dialog"}
SKIP_ROLES = {"navigation", "banner", "contentinfo", "dialog", "search"}
SKIP_CLASS = re.compile(r"(^|\s)(cookie\S*|consent\S*|modal|breadcrumbs?|share\S*|social\S*|skip-link)(\s|$)", re.I)
VOID = {"img", "br", "hr", "meta", "link", "input", "source", "wbr", "area", "col", "embed", "param", "track"}


class MD(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # (tag, skipping)
        self.out = []
        self.buf = []
        self.block = None
        self.row = None
        self.in_main = 0
        self.saw_main = False
        self.meta = {}
        self.title = ""
        self._t = False
        self.jsonld = []
        self._ld = False
        self._ldbuf = []
        self.links = []
        self._a = None

    scope = None
    def skipping(self):
        if self.scope and not any(t == self.scope for t, _ in self.stack):
            return True
        if any(t == "header" for t, _ in self.stack) and not any(t in ("main", "article") for t, _ in self.stack):
            return True
        return any(s for _, s in self.stack)

    def flush(self):
        t = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        self.buf = []
        if not t:
            return
        b = self.block or "p"
        if re.fullmatch(r"h[1-6]", b):
            self.out.append("\n" + "#" * int(b[1]) + " " + t + "\n")
        elif b == "li":
            self.out.append("- " + t)
        else:
            self.out.append("\n" + t + "\n")

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._t = True
        if tag == "meta":
            k = (a.get("name") or a.get("property") or "").lower()
            if k in ("description", "og:title", "og:description", "article:published_time", "article:modified_time", "author", "date"):
                self.meta[k] = a.get("content", "")
        if tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self._ld, self._ldbuf = True, []
        if tag == "time" and a.get("datetime"):
            self.meta.setdefault("time_elements", []).append(a["datetime"])
        cls = (a.get("class") or "") + " " + (a.get("id") or "")
        skip = tag in SKIP or (a.get("role") or "").lower() in SKIP_ROLES or bool(SKIP_CLASS.search(cls)) or a.get("aria-hidden") == "true"
        if tag in ("main",) or (a.get("role") == "main"):
            self.in_main += 1
            self.saw_main = True
        if tag in VOID:
            if tag == "img" and not self.skipping() and not skip:
                self.flush()
                self.out.append(f"![{a.get('alt') or ''}](img)")
            if tag == "br":
                self.buf.append(" ")
            return
        self.stack.append((tag, skip))
        if self.skipping():
            return
        if re.fullmatch(r"h[1-6]|p|li|td|th|dt|dd|blockquote|figcaption|caption", tag):
            self.flush()
            self.block = tag
        if tag == "tr":
            self.flush()
            self.row = []
        if tag in ("td", "th"):
            self.block = tag
        if tag == "a":
            self._a = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._t = False
        if tag == "script" and self._ld:
            self._ld = False
            self.jsonld.append("".join(self._ldbuf))
        # pop to matching tag
        idx = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                idx = i
                break
        if idx is None:
            return
        was_skipping = self.skipping()
        if not was_skipping:
            if tag in ("td", "th") and self.row is not None:
                self.row.append(re.sub(r"\s+", " ", "".join(self.buf)).strip())
                self.buf = []
            elif tag == "tr" and self.row is not None:
                if any(self.row):
                    self.out.append("| " + " | ".join(self.row) + " |")
                self.row = None
            elif re.fullmatch(r"h[1-6]|p|li|dt|dd|blockquote|figcaption|caption|div|section|article", tag):
                self.flush()
                self.block = None
            if tag == "a" and self._a is not None:
                txt = re.sub(r"\s+", " ", "".join(self._a)).strip()
                if txt:
                    self.links.append(txt)
                self._a = None
        del self.stack[idx:]
        if tag == "main":
            self.in_main = max(0, self.in_main - 1)

    def handle_data(self, d):
        if self._t:
            self.title += d
        if self._ld:
            self._ldbuf.append(d)
            return
        if self.skipping():
            return
        self.buf.append(d)
        if self._a is not None:
            self._a.append(d)


def convert(html):
    p = MD()
    # blog.se.com: article scope (sidebars/related posts outside). se.com: whole body minus header/nav/footer tags
    # (hero banners and download-page content sit outside <main> there).
    p.scope = "article" if "blog.se.com" in html[:20000] and re.search(r"<article[\s>]", html) else None
    p.feed(html)
    p.flush()
    md = "\n".join(p.out)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    types = []
    for blob in p.jsonld:
        types += re.findall(r'"@type"\s*:\s*"([^"]+)"', blob)
    return md, p.title.strip(), p.meta, sorted(set(types)), p.links


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:28]


def rebuild(outdir):
    idx = json.load(open(os.path.join(outdir, "index.json"), encoding="utf-8"))
    for rec in idx:
        h = os.path.join(outdir, rec["file"][:-3] + ".html")
        if not os.path.exists(h):
            continue
        md, ttl, meta, ld, links = convert(open(h, encoding="utf-8").read())
        rec.update({"html_title": ttl, "meta": meta, "jsonld_types": ld, "words": len(md.split()), "h1": re.findall(r"^# (.+)$", md, re.M)[:3]})
        head = (f"<!-- {rec['type']} | {rec['title']} | {rec['url']} -->\n"
                f"<!-- html_title: {ttl} | meta: {json.dumps(meta, ensure_ascii=False)} | jsonld: {ld} -->\n\n")
        open(os.path.join(outdir, rec["file"]), "w", encoding="utf-8").write(head + md)
        print(rec["n"], rec["words"], rec["h1"][:1])
    json.dump(idx, open(os.path.join(outdir, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1] == "--rebuild":
        return rebuild(sys.argv[2])
    inv, outdir = sys.argv[1], sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    ws = openpyxl.load_workbook(inv, data_only=True)["URL Inventory"]
    rows = [r for r in ws.iter_rows(min_row=2, values_only=True) if r[2]]
    index = []
    for n, (ptype, title, url, subtype, covers) in enumerate(rows, 1):
        base = f"{n:02d}_{slug(ptype)}"
        rec = {"n": n, "type": ptype, "title": title, "url": url, "subtype": subtype, "covers": covers, "file": base + ".md"}
        if url.lower().split("?")[0].endswith(".pdf"):
            rec["note"] = "Direct PDF link: not fetched (file download needs user approval)"
            index.append(rec)
            print(n, ptype, "SKIPPED PDF", flush=True)
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
            with urllib.request.urlopen(req, timeout=60) as r:
                ctype = r.headers.get("Content-Type", "")
                data = r.read()
                rec["final_url"] = r.geturl()
                rec["status"] = r.status
            if "pdf" in ctype.lower():
                rec["note"] = "PDF response, not converted"
                rec["bytes"] = len(data)
            else:
                html = data.decode("utf-8", "replace")
                open(os.path.join(outdir, base + ".html"), "w", encoding="utf-8").write(html)
                md, ttl, meta, ld, links = convert(html)
                rec.update({"html_title": ttl, "meta": meta, "jsonld_types": ld, "words": len(md.split()),
                            "h1": re.findall(r"^# (.+)$", md, re.M)[:3]})
                head = f"<!-- {ptype} | {title} | {url} -->\n<!-- html_title: {ttl} | meta: {json.dumps(meta, ensure_ascii=False)} | jsonld: {ld} -->\n\n"
                open(os.path.join(outdir, rec["file"]), "w", encoding="utf-8").write(head + md)
        except Exception as e:
            rec["error"] = repr(e)
        index.append(rec)
        print(n, ptype, rec.get("status"), rec.get("words"), rec.get("error", rec.get("note", "")), flush=True)
        time.sleep(1.0)
    json.dump(index, open(os.path.join(outdir, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()

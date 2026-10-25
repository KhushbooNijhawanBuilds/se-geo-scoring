"""Fetch a page and turn it into judge-ready text plus deterministic content signals."""
import re
import sys
import urllib.error
import urllib.request

from .catalog import ENGINE

if str(ENGINE) not in sys.path:
    sys.path.insert(0, str(ENGINE))
import geo_content_check as checker  # noqa: E402

BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/141.0 Safari/537.36")
MAX_CHARS = 150_000


class CaptureError(Exception):
    pass


def fetch_html(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA, "Accept": "text/html,application/xhtml+xml"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ctype = r.headers.get("Content-Type", "")
            if "pdf" in ctype:
                raise CaptureError("This URL is a PDF. Paste the document text instead and choose a document page type.")
            if "html" not in ctype:
                raise CaptureError(f"Not an HTML page (Content-Type: {ctype or 'unknown'}). Paste the text instead.")
            charset = r.headers.get_content_charset() or "utf-8"
            return r.read().decode(charset, errors="replace"), r.geturl()
    except urllib.error.HTTPError as e:
        raise CaptureError(f"The site returned HTTP {e.code}: it blocks automated requests from this app (se.com and Medium do). "
                           "Open the page in your browser, select all the article text, copy it, and paste it under "
                           "'Paste the page text instead'. Keep the URL filled in so it appears in the report.")
    except urllib.error.URLError as e:
        raise CaptureError(f"Could not reach the page ({e.reason}).")


def main_content_html(html):
    """Slice the page to its <article> (or <main>) element and keep the <header> inside it.

    The engine's extractor skips every <header>, but many blogs put the article's H1 in one.
    Returns None when the page has neither element, or when the slice has no H1."""
    for tag in ("article", "main"):
        start = re.search(r"<%s\b" % tag, html, re.I)
        end = html.lower().rfind("</%s>" % tag)
        if start and end > start.start():
            part = html[start.start(): end + len(tag) + 3]
            part = re.sub(r"<header\b", "<div", part, flags=re.I)
            part = re.sub(r"</header>", "</div>", part, flags=re.I)
            doc = checker.parse_html(part)
            if any(k == "h1" for k, _ in doc["blocks"]):
                return doc
    return None


def blocks_to_text(doc):
    lines = []
    for kind, text in doc["blocks"]:
        if kind.startswith("h") and kind[1:].isdigit():
            lines.append("\n" + "#" * int(kind[1:]) + " " + text)
        elif kind == "li":
            lines.append("- " + text)
        elif kind == "cell":
            lines.append("| " + text)
        else:
            lines.append(text)
    alts = [a for a in doc.get("images", []) if a]
    if alts:
        lines.append("\n[Image alt texts] " + " | ".join(alts[:40]))
    links = [l for l in doc.get("links", []) if l]
    if links:
        lines.append("[Link and button labels] " + " | ".join(dict.fromkeys(links))[:3000])
    return "\n".join(lines).strip()


def capture(url=None, pasted_text=None):
    """Return dict(text, signals, title, meta_description, source, final_url, notes)."""
    notes = []
    if pasted_text and pasted_text.strip():
        doc = checker.parse_markdown(pasted_text) if "#" in pasted_text else checker.parse_text(pasted_text)
        text, source, final_url = pasted_text.strip(), "pasted text", url or ""
    else:
        if not url:
            raise CaptureError("Enter a URL or paste the page text.")
        html, final_url = fetch_html(url)
        full = checker.parse_html(html)
        main = main_content_html(html)
        if main:
            doc = dict(main, title=full["title"], meta_description=full["meta_description"])
        else:
            doc = full
            title = (full.get("title") or "").strip()
            doc["blocks"] = [(k, t) for k, t in full["blocks"]
                             if t.strip().lstrip("﻿").strip() not in (title, "Skip to content", "Skip to main content")]
        text, source = blocks_to_text(doc).lstrip("﻿").strip(), "server HTML"
        notes.append("Scored on the HTML the server returns, which is what AI crawlers without JavaScript see. "
                     "If the page builds its content with JavaScript, paste the rendered text for a fair score.")
    signals = checker.analyse(doc, "text" if source == "pasted text" else "url")
    if signals.get("word_count", 0) < 150:
        notes.append(f"Only {signals.get('word_count', 0)} words were found. The page may load its content with JavaScript, "
                     "or block automated requests. Paste the visible text to score it properly.")
    if len(text) > MAX_CHARS:
        raise CaptureError(f"The page text is {len(text):,} characters, over the {MAX_CHARS:,} the app sends. "
                           "Paste the main content only (without navigation or comments).")
    return {"text": text, "signals": signals, "title": doc.get("title", ""), "meta_description": doc.get("meta_description", ""),
            "source": source, "final_url": final_url, "notes": notes}

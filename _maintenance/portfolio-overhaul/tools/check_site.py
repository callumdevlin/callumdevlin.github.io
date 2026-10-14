#!/usr/bin/env python3
"""Check a built Jekyll site (the _site folder) for the problems this overhaul cares about.

Usage:
    python check_site.py <path-to-_site> [--external] [--json report.json]

Checks (internal, no network unless --external):
  * every internal <a>, <img>, <link>, <script>, <iframe>, srcset target exists in the output
    (exact letter case, so a Windows build does not hide a case error that GitHub Pages would expose)
  * every #fragment points at an id/name that exists on the target page
  * heading hierarchy (no jumps such as h2 -> h4) and exactly one h1 per page
  * duplicate <title>, empty/missing <title>
  * <img> without alt, without width/height; large images
  * private or draft material accidentally published (maintenance folder, research notes, raw source)
  * <script type="math/tex"> left unrendered is reported as informational (MathJax renders it in the browser)
With --external every distinct external URL is requested (HEAD, then GET) and its status recorded. A failure
is a lead to investigate by hand, not proof the source is dead (some hosts block scripted requests).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

DENY_PATH_PARTS = ("_maintenance", "research-todo", "owner-input", "Gemfile", "_config.yml", ".md.erb")
DENY_SUFFIXES = (".md", ".markdown", ".scss.map", ".py", ".ps1")
IMG_WARN_BYTES = 400 * 1024


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.ids: set[str] = set()
        self.links: list[tuple[str, str]] = []  # (kind, url)
        self.headings: list[int] = []
        self.imgs: list[dict] = []
        self.math_scripts = 0
        self._in_main = 0
        self._tpl = 0
        self._pic = False
        self._pic_source = False
        self.fallback_imgs: set[str] = set()
        self.main_headings: list[int] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "picture":
            self._pic, self._pic_source = True, False
        if tag == "source" and self._pic:
            self._pic_source = True
        if tag == "template":
            self._tpl += 1
        if self._tpl:
            return          # Hydejack ships hidden <template> blocks (loading/error pages); not page content
        if "id" in a and a["id"]:
            self.ids.add(a["id"])
        if tag == "a" and "name" in a:
            self.ids.add(a["name"])
        if tag == "title":
            self._in_title = True
        if tag == "main":
            self._in_main += 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self.headings.append(level)
            if self._in_main:
                self.main_headings.append(level)
        if tag == "a" and a.get("href"):
            self.links.append(("a", a["href"]))
        elif tag == "img":
            if a.get("src"):
                self.links.append(("img", a["src"]))
                if self._pic and self._pic_source:
                    self.fallback_imgs.add(a["src"])
            for part in (a.get("srcset") or "").split(","):
                u = part.strip().split(" ")[0]
                if u:
                    self.links.append(("img", u))
            self.imgs.append(a)
        elif tag == "source":
            for part in (a.get("srcset") or "").split(","):
                u = part.strip().split(" ")[0]
                if u:
                    self.links.append(("img", u))
        elif tag == "link" and a.get("href") and a.get("rel") not in (None, "preconnect", "dns-prefetch"):
            self.links.append(("link", a["href"]))
        elif tag == "script":
            if a.get("src"):
                self.links.append(("script", a["src"]))
            if (a.get("type") or "").startswith("math/tex"):
                self.math_scripts += 1
        elif tag == "iframe" and a.get("src"):
            self.links.append(("iframe", a["src"]))

    def handle_endtag(self, tag):
        if tag == "picture":
            self._pic = False
        if tag == "template" and self._tpl:
            self._tpl -= 1
        if tag == "title":
            self._in_title = False
        if tag == "main" and self._in_main:
            self._in_main -= 1

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def exact_exists(root: Path, rel: str) -> Path | None:
    """Return the path if `rel` exists under root with exact letter case on every segment."""
    cur = root
    segs = [s for s in rel.split("/") if s]
    for i, seg in enumerate(segs):
        try:
            names = os.listdir(cur)
        except OSError:
            return None
        if seg not in names:
            return None
        cur = cur / seg
    return cur


SITE_URL = "https://callumdevlin.github.io"


def resolve(root: Path, page_rel: str, url: str, baseurl: str) -> tuple[str, Path | None, str]:
    """Classify and resolve a URL found on page `page_rel`. Returns (kind, path, fragment).
    The site's own absolute URLs (canonical links, og:url) are resolved against the local build, so a page
    that is not deployed yet does not show up as a dead external link."""
    if url.startswith(SITE_URL):
        url = url[len(SITE_URL):] or "/"
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme in ("mailto", "tel", "javascript", "data", "sms"):
        return "skip", None, ""
    if parsed.scheme in ("http", "https") or url.startswith("//"):
        return "external", None, parsed.fragment
    path = urllib.parse.unquote(parsed.path)
    frag = urllib.parse.unquote(parsed.fragment)
    if not path:
        return "internal", root / page_rel, frag
    if path.startswith("/"):
        if baseurl and path.startswith(baseurl):
            path = path[len(baseurl):]
        rel = path.lstrip("/")
    else:
        rel = os.path.normpath(os.path.join(os.path.dirname(page_rel), path)).replace("\\", "/")
    target = exact_exists(root, rel) if rel else root
    if target is None:
        return "internal", None, frag
    if target.is_dir():
        idx = target / "index.html"
        if idx.exists():
            return "internal", idx, frag
        return "internal", None, frag
    return "internal", target, frag


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("site")
    ap.add_argument("--external", action="store_true")
    ap.add_argument("--json")
    ap.add_argument("--baseurl", default="")
    args = ap.parse_args()
    root = Path(args.site).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 2

    problems: dict[str, list[str]] = defaultdict(list)
    info: dict[str, list[str]] = defaultdict(list)
    pages: dict[str, PageParser] = {}
    external: dict[str, set[str]] = defaultdict(set)

    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root).as_posix()
        if p.is_file():
            if any(part in rel for part in DENY_PATH_PARTS) or rel.endswith(DENY_SUFFIXES):
                problems["leak"].append(f"published but should not be: {rel}")

    html_files = [p for p in root.rglob("*.html")]
    for p in html_files:
        rel = p.relative_to(root).as_posix()
        # Lab apps and the redirect stubs are checked for links but not for page-level rules.
        text = p.read_text(encoding="utf-8", errors="replace")
        parser = PageParser()
        parser.feed(text)
        pages[rel] = parser

    titles = Counter()
    for rel, pg in pages.items():
        t = pg.title.strip()
        if not t:
            problems["title"].append(f"{rel}: empty <title>")
        else:
            titles[t] += 1
    for t, n in titles.items():
        if n > 1:
            where = [r for r, pg in pages.items() if pg.title.strip() == t]
            problems["duplicate-title"].append(f"{t!r} on {n} pages: {', '.join(where[:6])}")

    for rel, pg in pages.items():
        if rel.startswith(("tools/", "assets/")):
            continue
        h1s = pg.headings.count(1)
        if h1s != 1 and rel not in ("404.html",):
            problems["headings"].append(f"{rel}: {h1s} h1 elements")
        prev = 0
        for lvl in pg.main_headings or pg.headings:
            if prev and lvl > prev + 1:
                problems["headings"].append(f"{rel}: heading jumps h{prev} -> h{lvl}")
                break
            prev = lvl
        for img in pg.imgs:
            src = img.get("src", "")
            if "alt" not in img:
                problems["alt"].append(f"{rel}: <img> without alt: {src[:80]}")
            elif not img["alt"].strip() and img.get("role") != "presentation":
                info["alt-empty"].append(f"{rel}: empty alt (decorative?): {src[:80]}")
            if src and not src.startswith("data:") and not (img.get("width") and img.get("height")):
                info["img-size-attrs"].append(f"{rel}: no width/height attrs: {src[:80]}")
        if pg.math_scripts:
            info["math"].append(f"{rel}: {pg.math_scripts} math/tex script elements (MathJax renders client-side)")

    seen_frag_missing = set()
    for rel, pg in pages.items():
        for kind, url in pg.links:
            k, target, frag = resolve(root, rel, url, args.baseurl)
            if k == "skip":
                continue
            if k == "external":
                external[url.split("#")[0]].add(rel)
                continue
            if target is None:
                problems["broken-internal"].append(f"{rel}: {kind} -> {url}")
                continue
            if kind == "img" and target.is_file() and url not in pg.fallback_imgs:
                size = target.stat().st_size
                if size > IMG_WARN_BYTES:
                    info["large-image"].append(f"{target.relative_to(root).as_posix()} {size // 1024} KB (used on {rel})")
            if frag and target.suffix == ".html":
                trel = target.relative_to(root).as_posix()
                tp = pages.get(trel)
                if tp is not None and frag not in tp.ids and (trel, frag) not in seen_frag_missing:
                    seen_frag_missing.add((trel, frag))
                    problems["broken-anchor"].append(f"{rel}: {url} (no id {frag!r} in {trel})")

    if args.external:
        for url in sorted(external):
            status = ""
            for method in ("HEAD", "GET"):
                try:
                    req = urllib.request.Request(url, method=method, headers={"User-Agent": "Mozilla/5.0 (link check)"})
                    with urllib.request.urlopen(req, timeout=20) as r:
                        status = str(r.status)
                        break
                except urllib.error.HTTPError as e:
                    status = f"HTTP {e.code}"
                    if method == "GET" or e.code not in (403, 405, 400, 501):
                        break
                except Exception as e:  # noqa: BLE001
                    status = f"ERR {type(e).__name__}"
                    if method == "GET":
                        break
            if not status.startswith("2") and not status.startswith("3"):
                problems["external"].append(f"{status}  {url}  (on {sorted(external[url])[0]})")
            else:
                info["external-ok"].append(f"{status} {url}")
    else:
        info["external-not-checked"].append(f"{len(external)} distinct external URLs (run with --external)")

    report = {"site": str(root), "pages": len(pages), "problems": problems, "info": {k: v for k, v in info.items()}}
    print(f"Checked {len(pages)} HTML files under {root}")
    total = 0
    for k, v in sorted(problems.items()):
        print(f"\n[PROBLEM] {k}: {len(v)}")
        for line in v[:60]:
            print("  ", line)
        if len(v) > 60:
            print(f"   ... {len(v) - 60} more")
        total += len(v)
    for k, v in sorted(info.items()):
        if k == "external-ok":
            print(f"\n[info] external-ok: {len(v)}")
            continue
        print(f"\n[info] {k}: {len(v)}")
        for line in v[:12]:
            print("  ", line)
        if len(v) > 12:
            print(f"   ... {len(v) - 12} more")
    if args.json:
        Path(args.json).write_text(json.dumps(report, indent=1), encoding="utf-8")
    print(f"\nTotal problems: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())

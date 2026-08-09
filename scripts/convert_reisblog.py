#!/usr/bin/env python3
"""Zet de ruwe Wayback-archiefbestanden in reisblog-raw/ om naar Jekyll-pagina's
in _reisblog/. Eenmalig gebruikt bij het terughalen van reis.anneschuth.nl."""

import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "reisblog-raw" / "site"
OUT = ROOT / "_reisblog"

MONTHS = {
    "january": 1, "januari": 1, "february": 2, "februari": 2, "march": 3,
    "maart": 3, "april": 4, "may": 5, "mei": 5, "june": 6, "juni": 6,
    "july": 7, "juli": 7, "august": 8, "augustus": 8, "september": 9,
    "october": 10, "oktober": 10, "november": 11, "december": 12,
}
MONTHS_NL = [None, "januari", "februari", "maart", "april", "mei", "juni",
             "juli", "augustus", "september", "oktober", "november", "december"]

POST_RE = re.compile(
    r'<div class="post" id="post-(?P<id>\d+)">\s*'
    r'<h2><a href="(?P<permalink>[^"]*)"[^>]*>(?P<title>.*?)</a></h2>\s*'
    r'<small>(?P<date>[^<]+?)\s*(?:<!-- by (?P<author>[^>]*?) -->)?</small>'
    r'.*?<div class="entry">(?P<entry>.*?)</div>\s*'
    r'<p class="postmetadata">(?P<meta>.*?)</p>\s*</div>',
    re.DOTALL,
)


def slugify(title):
    text = html.unescape(re.sub(r"&#8\d\d\d;", "", title))
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def parse_date(text):
    m = re.match(r"(\w+)\s+(\d+)\w*,\s*(\d{4})", text.strip())
    month = MONTHS[m.group(1).lower()]
    return int(m.group(3)), month, int(m.group(2))


def clean_entry(entry):
    # Locatie van de reiskaart-link bewaren, daarna de servicelinks weghalen
    lat = lng = None
    loc = re.search(r'lat=([\d.]+)&(?:amp;)?lng=([\d.]+)', entry)
    if loc:
        lat, lng = loc.group(1), loc.group(2)
    entry = re.sub(r'<li><a href="[^"]*(?:page_id=16|/kaart/)[^"]*">Mijn reiskaart[^<]*</a></li>', "", entry)
    entry = re.sub(r"<p><li><a href='[^']*fotoalbum[^']*'[^>]*>Mijn fotoalbum</a></li></p>", "", entry)

    # Buitenste <ul><li> ... </li></ul> is opmaak van het oude thema
    entry = entry.strip()
    entry = re.sub(r"^\s*<ul>\s*<li>", "", entry)
    entry = re.sub(r"</li>\s*</ul>\s*$", "", entry)

    # Tracking en oude embeds opruimen
    entry = re.sub(r'\s*onclick="javascript:pageTracker[^"]*"', "", entry)
    entry = re.sub(
        r'<img src=\'[^\']*wp-includes/images/smilies/[^\']*\' alt=\'([^\']*)\'[^>]*/>',
        r"\1", entry)
    entry = re.sub(
        r'<object[^>]*data="http://www\.youtube\.com/v/([\w-]+)"[^>]*>.*?</object>',
        r'<iframe class="reisblog-video" src="https://www.youtube-nocookie.com/embed/\1" '
        r'title="YouTube-video" allowfullscreen></iframe>', entry, flags=re.DOTALL)
    entry = entry.replace("<center>", '<div class="reisblog-center">').replace("</center>", "</div>")
    entry = re.sub(r"\n{3,}", "\n\n", entry)
    return entry.strip(), lat, lng


def extract_comments(path):
    text = path.read_text(errors="replace")
    comments = []
    for m in re.finditer(
        r'<div class="commentnumber">comment number \d+ by: (?P<who>[^<]+)</div>\s*'
        r'<small class="commentmetadata"><a[^>]*>(?P<when>[^<]+)</a>\s*</small><br />\s*'
        r'(?P<body>.*?)\s*</li>', text, re.DOTALL,
    ):
        body = re.sub(r'\s*onclick="javascript:pageTracker[^"]*"', "", m.group("body"))
        body = re.sub(
            r'<img src=\'[^\']*wp-includes/images/smilies/[^\']*\' alt=\'([^\']*)\'[^>]*/>',
            r"\1", body)
        comments.append({"who": m.group("who").strip(), "when": m.group("when").strip(),
                         "body": body.strip()})
    return comments


def main():
    posts = {}
    for month_dir in sorted(RAW.glob("200[78]/[01][0-9]/index.html")):
        text = month_dir.read_text(errors="replace")
        for m in POST_RE.finditer(text):
            pid = int(m.group("id"))
            if pid in posts:
                continue
            title = html.unescape(m.group("title"))
            year, month, day = parse_date(m.group("date"))
            entry, lat, lng = clean_entry(m.group("entry"))
            slug_m = re.search(r"/\d{4}/\d{2}/\d{2}/([^/]+)/", m.group("permalink"))
            slug = slug_m.group(1) if slug_m else slugify(m.group("title"))
            cat_m = re.search(r'rel="category[^"]*">([^<]+)</a>', m.group("meta"))
            posts[pid] = {
                "id": pid, "slug": slug, "title": title,
                "date": f"{year:04d}-{month:02d}-{day:02d}",
                "date_display": f"{day} {MONTHS_NL[month]} {year}",
                "author": (m.group("author") or "Anne").strip(),
                "category": cat_m.group(1) if cat_m else None,
                "lat": lat, "lng": lng, "entry": entry,
            }

    comments = extract_comments(RAW / "2007/09/20/eindelijk-warm/index.html")

    OUT.mkdir(exist_ok=True)
    for post in sorted(posts.values(), key=lambda p: p["date"]):
        title = post["title"].replace('"', '\\"')
        fm = [
            "---", "layout: reisblog", "lang: nl", f'title: "{title}"',
            f"date: {post['date']}", f"date_display: {post['date_display']}",
            f"author: {post['author']}", f"wp_id: {post['id']}",
        ]
        if post["category"]:
            fm.append(f"category_label: {post['category']}")
        if post["lat"]:
            fm += [f"lat: {post['lat']}", f"lng: {post['lng']}"]
        fm.append("---")
        body = post["entry"]
        if post["slug"] == "eindelijk-warm" and comments:
            parts = ['\n\n<div class="reisblog-comments">',
                     f"<h2>Reacties ({len(comments)})</h2>"]
            for c in comments:
                parts.append(
                    f'<div class="reisblog-comment"><p class="reisblog-comment-meta">'
                    f'{html.escape(c["who"])} &middot; {c["when"]}</p>\n{c["body"]}</div>')
            parts.append("</div>")
            body += "\n".join(parts)
        (OUT / f"{post['slug']}.md").write_text("\n".join(fm) + "\n\n" + body + "\n")

    print(f"{len(posts)} posts geschreven naar {OUT}/")
    imgs = sorted({u for p in posts.values() for u in re.findall(r'<img src="(http[^"]+)"', p["entry"])})
    print(json.dumps(imgs, indent=1))


if __name__ == "__main__":
    main()

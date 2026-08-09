#!/usr/bin/env python3
"""Zet de verwerkte reismail-JSONs (scratchpad/india-out/) om naar
Jekyll-posts in _reisblog_india/. Eenmalig gebruikt bij het terughalen
van de reisverslagen van 2003-2004 uit het e-mailarchief."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_reisblog_india"

MAANDEN = [None, "januari", "februari", "maart", "april", "mei", "juni",
           "juli", "augustus", "september", "oktober", "november", "december"]


def main(src_dir):
    src = Path(src_dir)
    OUT.mkdir(exist_ok=True)
    written = []
    for f in sorted(src.glob("*.json")):
        d = json.loads(f.read_text())
        y, m, day = d["date"].split("-")
        title = d["title"].replace('"', '\\"')
        fm = [
            "---", "layout: reisblog", "lang: nl", f'title: "{title}"',
            f"date: {d['date']}",
            f"date_display: {int(day)} {MAANDEN[int(m)]} {y}",
            f"author: {d.get('author', 'Anne')}",
        ]
        if d.get("location_name"):
            loc = d["location_name"].replace('"', '\\"')
            fm.append(f'location: "{loc}"')
        if d.get("lat") is not None:
            fm += [f"lat: {d['lat']}", f"lng: {d['lng']}"]
        fm.append("---")
        (OUT / f"{d['slug']}.md").write_text(
            "\n".join(fm) + "\n\n" + d["body_html"].strip() + "\n")
        written.append((d["date"], d["slug"], d["title"]))
    for date, slug, title in written:
        print(date, "|", slug, "|", title)
    print(f"{len(written)} posts geschreven naar {OUT}/")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

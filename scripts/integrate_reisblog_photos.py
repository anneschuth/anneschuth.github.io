#!/usr/bin/env python3
"""Verwerk de door de workflow teruggevonden foto's: kopieer ze naar
assets/reisblog/ en herschrijf de afbeeldingen in _reisblog/*.md.
Niet-teruggevonden foto's krijgen een nette 'verloren'-markering."""

import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
PHOTOS = ROOT / "reisblog-raw" / "photos"
ASSETS = ROOT / "assets" / "reisblog"
NOTE = '<p class="reisblog-missing">[De foto die hier stond is verloren gegaan.]</p>'

manifest = json.loads((PHOTOS / "photos-manifest.json").read_text())
found = {m["url"]: m["file"] for m in manifest if m.get("file")}

ASSETS.mkdir(parents=True, exist_ok=True)
for name in set(found.values()):
    shutil.copy2(PHOTOS / name, ASSETS / name)
print(f"{len(set(found.values()))} foto's naar assets/reisblog/ gekopieerd")

img_block = re.compile(
    r'(?:<a\s[^>]*>\s*)?<img src="(?P<src>http[^"]+)"(?P<attrs>[^>]*)/>(?:\s*</a>)?')

for f in sorted(ROOT.glob("_reisblog/*.md")):
    t = f.read_text()

    def repl(m):
        src = m.group("src")
        if src in found:
            alt = re.search(r'alt="([^"]*)"', m.group("attrs"))
            alt_txt = alt.group(1) if alt else unquote(src.rsplit("/", 1)[-1])
            return f'<img src="/assets/reisblog/{found[src]}" alt="{alt_txt}" loading="lazy" />'
        return '<span class="reisblog-missing">[foto verloren gegaan]</span>'

    t2 = img_block.sub(repl, t)
    # Alinea's die alleen nog een verloren-foto-markering bevatten worden nette notities
    t2 = re.sub(
        r'<p[^>]*>\s*<span class="reisblog-missing">\[foto verloren gegaan\]</span>\s*</p>',
        NOTE, t2)
    if t2 != t:
        f.write_text(t2)
        print("bijgewerkt:", f.name)

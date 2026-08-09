#!/usr/bin/env python3
"""Probeer de Picasa-foto's uit de reisblogposts terug te vinden in de
Wayback Machine en sla gevonden exemplaren op in reisblog-raw/photos/."""

import json
import re
import time
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests

RAW = Path("reisblog-raw")
OUT = RAW / "photos"
CDX = "https://web.archive.org/cdx/search/cdx"

session = requests.Session()
session.headers["User-Agent"] = (
    "reisblog-archiver/1.0 (persoonlijk archief van eigen site; anne.schuth@gmail.com)"
)


def get(url, **kw):
    for attempt in range(6):
        try:
            r = session.get(url, timeout=60, **kw)
            if r.status_code in (429, 502, 503, 504):
                raise requests.RequestException(f"HTTP {r.status_code}")
            return r
        except requests.RequestException as e:
            wait = 2**attempt
            print(f"  retry in {wait}s: {e}", flush=True)
            time.sleep(wait)
    return None


def main():
    img_urls = set()
    for html in (RAW / "site").rglob("*.html"):
        img_urls.update(re.findall(r'<img src="(http[^"]+)"', html.read_text(errors="replace")))
    # Ook grotere varianten proberen: s288/s400 -> s800
    candidates = {}
    for url in sorted(img_urls):
        if "lh" not in urlsplit(url).netloc:
            continue
        candidates[url] = [re.sub(r"/s\d+/", "/s800/", url), url]
    print(f"{len(candidates)} foto's om te zoeken", flush=True)

    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    for orig, variants in candidates.items():
        name = unquote(orig.rsplit("/", 1)[-1])
        saved = False
        for variant in variants:
            r = get(CDX, params={"url": variant, "output": "json", "fl": "timestamp,original,statuscode", "limit": "50"})
            if r is None or r.status_code != 200:
                continue
            try:
                rows = r.json()[1:]
            except Exception:
                rows = []
            for ts, original, status in rows:
                if status != "200":
                    continue
                img = get(f"https://web.archive.org/web/{ts}id_/{original}")
                if img is not None and img.status_code == 200 and len(img.content) > 500:
                    (OUT / name).write_bytes(img.content)
                    manifest.append({"url": orig, "fetched": original, "timestamp": ts, "file": name, "bytes": len(img.content)})
                    print(f"  gevonden: {name} ({len(img.content)} bytes, via {original})", flush=True)
                    saved = True
                    break
            if saved:
                break
            time.sleep(0.3)
        if not saved:
            print(f"  niet gevonden: {name}", flush=True)
            manifest.append({"url": orig, "file": None})
        time.sleep(0.3)

    (OUT / "photos-manifest.json").write_text(json.dumps(manifest, indent=2))
    found = sum(1 for m in manifest if m["file"])
    print(f"klaar: {found}/{len(manifest)} foto's teruggevonden", flush=True)


if __name__ == "__main__":
    main()

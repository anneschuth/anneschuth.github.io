#!/usr/bin/env python3
"""Download alle gearchiveerde pagina's van reis.anneschuth.nl uit de
Wayback Machine naar reisblog-raw/, met een manifest voor latere verwerking."""

import json
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit

import requests

HOST = "reis.anneschuth.nl"
FROM, TO = "2005", "2012"
OUT = Path("reisblog-raw")
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
    raise SystemExit(f"gaf op na 6 pogingen: {url}")


def target_path(original):
    parts = urlsplit(original)
    path = parts.path or "/"
    if path.endswith("/"):
        path += "index.html"
    name = path.lstrip("/")
    if parts.query:
        safe_q = parts.query.replace("=", "_").replace("&", "__").replace("/", "-")
        name = f"{name}__q__{safe_q}.html" if not name.endswith(".html") else name.replace(
            ".html", f"__q__{safe_q}.html"
        )
    return OUT / "site" / name


def main():
    print(f"CDX-lijst ophalen voor {HOST} ({FROM}-{TO})", flush=True)
    r = get(
        CDX,
        params={
            "url": HOST,
            "matchType": "host",
            "output": "json",
            "fl": "urlkey,timestamp,original,mimetype,statuscode",
            "filter": "statuscode:200",
            "from": FROM,
            "to": TO,
            "limit": "50000",
        },
    )
    rows = r.json()
    if not rows:
        raise SystemExit("CDX gaf geen resultaten")
    header, rows = rows[0], rows[1:]
    print(f"{len(rows)} snapshots gevonden", flush=True)

    # Nieuwste snapshot per unieke URL
    latest = {}
    for urlkey, ts, original, mime, status in rows:
        if urlkey not in latest or ts > latest[urlkey][0]:
            latest[urlkey] = (ts, original, mime)
    print(f"{len(latest)} unieke URL's", flush=True)

    manifest = []
    for i, (urlkey, (ts, original, mime)) in enumerate(sorted(latest.items()), 1):
        dest = target_path(original)
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(f"[{i}/{len(latest)}] {original} @ {ts}", flush=True)
        r = get(f"https://web.archive.org/web/{ts}id_/{original}")
        if r.status_code != 200:
            print(f"  overgeslagen (HTTP {r.status_code})", flush=True)
            continue
        dest.write_bytes(r.content)
        manifest.append(
            {
                "url": original,
                "timestamp": ts,
                "mimetype": mime,
                "file": str(dest.relative_to(OUT)),
                "bytes": len(r.content),
            }
        )
        time.sleep(0.5)

    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"klaar: {len(manifest)} bestanden opgeslagen in {OUT}/", flush=True)


if __name__ == "__main__":
    sys.exit(main())

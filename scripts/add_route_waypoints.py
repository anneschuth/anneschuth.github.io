#!/usr/bin/env python3
"""Voeg route-waypoints uit scratchpad/route-out/*.json toe aan de front matter.

Eenmalig gebruikt om de tussenstops (geëxtraheerd uit de verslagteksten) als
`route:`-lijst in de front matter van de reisblogposts te zetten. Bestaande
`route:`-blokken worden vervangen, zodat het script idempotent is.
"""

import json
import math
import re
import sys
from pathlib import Path

ROUTE_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else None
REPO = Path(__file__).resolve().parent.parent


def dist_km(a, b):
    lat1, lng1, lat2, lng2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = (
        math.sin((lat2 - lat1) / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin((lng2 - lng1) / 2) ** 2
    )
    return 6371 * 2 * math.asin(math.sqrt(h))


def main():
    if not ROUTE_DIR or not ROUTE_DIR.is_dir():
        sys.exit("gebruik: add_route_waypoints.py <route-out-dir>")

    total = 0
    for jf in sorted(ROUTE_DIR.glob("*.json")):
        data = json.loads(jf.read_text())
        post = REPO / data["file"]
        if not post.is_file():
            sys.exit(f"onbekend bestand: {data['file']}")
        wps = data.get("waypoints", [])
        for w in wps:
            if not (-90 <= w["lat"] <= 90 and -180 <= w["lng"] <= 180):
                sys.exit(f"coördinaat buiten bereik in {jf.name}: {w}")

        text = post.read_text()
        head, fm, body = text.split("---", 2)
        fm = re.sub(r"\nroute:\n(?:  - .*\n(?:    .*\n)*)*", "\n", fm)
        if wps:
            lines = ["route:"]
            for w in wps:
                name = w["name"].replace('"', "'")
                lines.append(f'  - name: "{name}"')
                lines.append(f"    lat: {w['lat']}")
                lines.append(f"    lng: {w['lng']}")
            fm = fm.rstrip("\n") + "\n" + "\n".join(lines) + "\n"
        post.write_text(head + "---" + fm + "---" + body)
        total += len(wps)
        print(f"{post.name}: {len(wps)} waypoints")
    print(f"totaal: {total} waypoints")


if __name__ == "__main__":
    main()

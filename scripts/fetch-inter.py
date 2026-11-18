#!/usr/bin/env python3
"""Self-host Inter (latin subset, WOFF2) for CloudPilot.

Audit finding (2026-11-18): Inter was loaded from Google Fonts (external
stylesheet = render-blocking, ~730ms on mobile; two extra origins). Best
practice (cross-verified): self-host WOFF2 on your own origin, latin subset
only, font-display: swap, preload only the critical weight.

Fetches the Google Fonts css2 API with a modern Chrome UA (so the response
lists woff2 URLs), downloads the latin subset as a SINGLE variable font file
(fvar wght axis 100-900), saves it to public/fonts/inter-var.woff2, and
verifies it (wOF2 magic + fvar axis). Google serves Inter as a variable
font now, so requesting per-weight files returns the same file six times —
one file + `font-weight: 100 900` in @font-face is the correct setup.
Inter is OFL-licensed.
"""
import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public", "fonts")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def main():
    os.makedirs(OUT, exist_ok=True)
    css_url = "https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap"
    css = get(css_url).decode()
    blocks = re.findall(r"/\*\s*(\w[\w-]*)\s*\*/\s*@font-face\s*{([^}]*)}", css)
    url = None
    for subset, body in blocks:
        if subset == "latin":
            url = re.search(r"url\((https://[^)]+\.woff2)\)", body).group(1)
            break
    if not url:
        raise SystemExit("no latin woff2 URL found in css2 response")
    data = get(url)
    if data[:4] != b"wOF2":
        raise SystemExit("downloaded file is not woff2")
    p = os.path.join(OUT, "inter-var.woff2")
    with open(p, "wb") as f:
        f.write(data)
    print(f"inter-var.woff2: {len(data) / 1024:.1f} KB (variable, wght 100-900)")
    print("DONE")


if __name__ == "__main__":
    main()

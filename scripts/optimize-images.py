#!/usr/bin/env python3
"""Resize + convert CloudPilot images to the size they are actually displayed at.

Audit finding (2026-11-18): home shipped ~1.66 MB of images; the 44px avatars
were 1600px / ~300 KB files. Best practice (cross-verified): serve at most 2x
the CSS display size, modern formats (WebP, alpha preserved for the tool
cutouts), explicit width/height in the markup (added separately).

- Avatars (photos, no alpha): center-crop square, resize in place (same name).
  avatar-man1/man2 -> 96px (displayed 44px), hero-woman -> 128px (44px + 64px).
- Tool cutouts (transparent PNG): resize to 800px wide (displayed max ~400px
  CSS) and save as WebP next to the PNG; templates swap src .png -> .webp.
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "public", "images")


def kb(p):
    return round(os.path.getsize(p) / 1024, 1)


def square_avatar(name, size):
    p = os.path.join(IMG, name)
    before = kb(p)
    im = Image.open(p).convert("RGB")
    w, h = im.size
    side = min(w, h)
    im = im.crop(((w - side) // 2, (h - side) // 2, (w + side) // 2, (h + side) // 2))
    im = im.resize((size, size), Image.LANCZOS)
    im.save(p, "WEBP", quality=82, method=6)
    print(f"{name}: {before} KB -> {kb(p)} KB ({size}x{size})")


def tool_webp(name, width=800):
    src = os.path.join(IMG, name)
    dst = os.path.join(IMG, name.rsplit(".", 1)[0] + ".webp")
    before = kb(src)
    im = Image.open(src)
    if im.mode not in ("RGBA", "LA"):
        im = im.convert("RGBA")
    w, h = im.size
    nh = round(h * width / w)
    im = im.resize((width, nh), Image.LANCZOS)
    im.save(dst, "WEBP", quality=90, method=6)
    print(f"{name} -> {os.path.basename(dst)}: {before} KB -> {kb(dst)} KB ({width}x{nh})")


if __name__ == "__main__":
    square_avatar("avatar-man1.webp", 96)
    square_avatar("avatar-man2.webp", 96)
    square_avatar("hero-woman.webp", 128)
    for n in ["flowmaster.png", "insightpro.png", "teamsync.png", "cubes.png", "piechart.png"]:
        tool_webp(n)
    print("DONE")

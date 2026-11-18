#!/usr/bin/env python3
"""Generate the branded Open Graph image for CloudPilot (1200x630).

Audit finding (2026-11-18): no og:image anywhere, so link shares show no
image. Best practice: a 1200x630 branded image referenced by og:image and
twitter:image. Dark violet gradient matching the hero, bold "C" mark drawn
as an arc (same geometry as the LogoMark SVG), "CloudPilot" wordmark and the
tagline. Pure PIL, no external assets.
"""
import math
import os
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "public", "og-image.png")
W, H = 1200, 630


def font(path, size):
    for p in path:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]
REG = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
]


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def main():
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    top, bot = (5, 5, 5), (109, 40, 217)
    for y in range(H):
        d.line([(0, y), (W, y)], fill=lerp(top, bot, y / H))
    # soft glow circle, top-right
    glow = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([760, -180, 1320, 380], fill=90)
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    img = Image.composite(Image.new("RGB", (W, H), (139, 92, 246)), img, glow)
    d = ImageDraw.Draw(img)
    # bold C mark: arc, same open-right geometry as the logo
    cx, cy, r, sw = 205, 315, 110, 34
    d.arc([cx - r, cy - r, cx + r, cy + r], start=48, end=312, fill=(255, 255, 255), width=sw)
    f_big = font(BOLD, 92)
    f_tag = font(REG, 40)
    f_small = font(BOLD, 30)
    d.text((350, 250), "CloudPilot", fill=(255, 255, 255), font=f_big)
    d.text((352, 365), "Simplify. Automate. Scale Your Business.", fill=(196, 181, 253), font=f_tag)
    d.text((352, 430), "ALL-IN-ONE SAAS PLATFORM", fill=(255, 255, 255), font=f_small)
    img.save(OUT, "PNG")
    print(f"{OUT}: {os.path.getsize(OUT) / 1024:.1f} KB, {img.size}")


if __name__ == "__main__":
    main()

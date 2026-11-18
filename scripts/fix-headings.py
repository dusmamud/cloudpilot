#!/usr/bin/env python3
"""Fix heading order (Lighthouse `heading-order`, 96/106 runs) without
changing any visuals — Tailwind classes control the look, not the tag.

Audit root cause: on ~48 of 53 pages the first content heading after the
<h1> was an <h3> (card titles, list items, version labels), skipping <h2>;
the footer nav labels were also <h3>s (fixed separately in the layout).

Rules, applied only inside <template>:
- <h3> after the <h1> but before the first <h2>  -> <h2> (same classes)
- <h3> before the <h1> (eyebrow label, not a heading) -> <p> (same classes)
- <h3> after the first <h2> -> untouched (valid subsection)

Usage: python3 scripts/fix-headings.py [--apply]
Default is a dry run that only prints what would change.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAG = re.compile(r"<(/?)h([1-6])(\s[^>]*)?>")
APPLY = "--apply" in sys.argv


def fix_template(tpl):
    """Return (new_tpl, changes) where changes is a list of (old, new, ctx)."""
    tags = list(TAG.finditer(tpl))
    if not tags:
        return tpl, []
    first_h1 = next((m.start() for m in tags if m.group(1) == "" and m.group(2) == "1"), None)
    first_h2 = next((m.start() for m in tags if m.group(1) == "" and m.group(2) == "2"), None)
    # Decide the fate of each <h3> open tag, then mirror it onto its close tag.
    fates = {}  # open-tag start -> 'h2' | 'p' | None
    stack = []  # (start, level, fate)
    for m in tags:
        closing, lvl = m.group(1), m.group(2)
        if closing:
            if stack and stack[-1][1] == lvl:
                open_start, _, fate = stack.pop()
                if fate:
                    fates[m.start()] = fate
            continue
        if lvl != "3":
            stack.append((m.start(), lvl, None))
            continue
        if first_h1 is not None and m.start() < first_h1:
            fate = "p"
        elif first_h2 is None or m.start() < first_h2:
            fate = "h2"
        else:
            fate = None
        stack.append((m.start(), lvl, fate))
        if fate:
            fates[m.start()] = fate
    if not fates:
        return tpl, []
    out = []
    last = 0
    changes = []
    for m in tags:
        if m.start() not in fates:
            continue
        fate = fates[m.start()]
        closing, lvl = m.group(1), m.group(2)
        old = m.group(0)
        new = f"</{fate}>" if closing else f"<{fate}{m.group(3) or ''}>"
        out.append(tpl[last:m.start()])
        out.append(new)
        last = m.end()
        changes.append((old, new, tpl[max(0, m.start() - 40):m.start() + 40].replace("\n", " ")))
    out.append(tpl[last:])
    return "".join(out), changes


def main():
    total_files = 0
    total_tags = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "app", "pages", "**", "*.vue"), recursive=True)):
        src = open(path, encoding="utf-8").read()
        m = re.search(r"<template>(.*)</template>", src, re.S)
        if not m:
            continue
        new_tpl, changes = fix_template(m.group(1))
        if not changes:
            continue
        total_files += 1
        total_tags += len(changes)
        print(f"{os.path.relpath(path, ROOT)}: {len(changes)} tags")
        for old, new, ctx in changes[:4]:
            print(f"    {old!r} -> {new!r}   ...{ctx}...")
        if APPLY:
            new_src = src[:m.start(1)] + new_tpl + src[m.end(1):]
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_src)
    print(f"{'APPLIED' if APPLY else 'DRY RUN'}: {total_tags} tags in {total_files} files")


if __name__ == "__main__":
    main()

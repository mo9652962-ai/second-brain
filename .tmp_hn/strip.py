# -*- coding: utf-8 -*-
import io, sys, re, html

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def clean(fn):
    with open(fn, encoding="utf-8", errors="ignore") as f:
        raw = f.read()
    # remove scripts/styles
    raw = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", raw, flags=re.S | re.I)
    # capture title
    m = re.search(r"<title[^>]*>(.*?)</title>", raw, flags=re.S | re.I)
    title = html.unescape(m.group(1)).strip() if m else ""
    # keep main text
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return title, text[:700]

for tag in ["k1", "k2", "k4", "k10"]:
    try:
        title, text = clean(f".tmp_hn/{tag}.html")
        print(f"===== {tag} =====")
        print(f"TITLE: {title}")
        print(text)
        print()
    except Exception as e:
        print(f"{tag} ERROR: {e}")

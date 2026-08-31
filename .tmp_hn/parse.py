# -*- coding: utf-8 -*-
import json, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

with open(r"C:\Users\31954\.openclaw\workspace\.tmp_hn\hn.json", encoding="utf-8") as f:
    data = json.load(f)

hits = data.get("hits", [])
rows = []
for h in hits:
    title = h.get("title") or h.get("story_title") or ""
    url = h.get("url")
    object_id = h.get("objectID")
    link = url if url else f"https://news.ycombinator.com/item?id={object_id}"
    rows.append({
        "title": title,
        "points": h.get("points", 0) or 0,
        "comments": h.get("num_comments", 0) or 0,
        "link": link,
        "item": f"https://news.ycombinator.com/item?id={object_id}",
        "objectID": object_id,
    })

rows.sort(key=lambda r: r["points"], reverse=True)
print(f"Total front_page hits: {len(hits)}")
print("=" * 100)
for i, r in enumerate(rows[:20], 1):
    print(f"{i:2d}. [{r['points']:>4} pts | {r['comments']:>3} cmt] {r['title'][:90]}")
    print(f"    {r['link']}")

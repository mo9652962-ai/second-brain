#!/usr/bin/env python3
"""Full vault diagnostic: broken links, empty notes, tag consistency, orphans."""
import os
import re
from pathlib import Path

VAULT = Path(r"C:\Users\31954\.openclaw\workspace")
os.chdir(str(VAULT))

# Build note index
notes = {}
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in [".git", ".obsidian", ".venv", "node_modules"]]
    for f in files:
        if f.endswith(".md"):
            full_path = Path(root) / f
            rel_path = full_path.as_posix()
            basename = f[:-3] if f.endswith('.md') else f  # NO splitext!
            notes[rel_path] = {"basename": basename, "content": full_path.read_text(encoding="utf-8", errors="replace")}

# 1. Broken wikilinks
wikilink_pattern = r'(?<!`)\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\](?!`)'
broken_links = []
for path, data in notes.items():
    # Skip community skill cards
    if path.startswith("skills/@") and "skill-card.md" in path:
        continue
    for match in re.finditer(wikilink_pattern, data["content"]):
        target = match.group(1).strip()
        # Check exact path match
        target_md = target if target.endswith('.md') else f"{target}.md"
        target_md = target_md.replace('\\', '/')
        
        found = False
        # Exact match
        if target_md in notes:
            found = True
        # Basename match
        for p, d in notes.items():
            if d["basename"] == target or d["basename"] == target.replace('.md', ''):
                found = True
                break
        # Directory check (target is a directory, not a file)
        if os.path.isdir(target):
            found = True
            continue
        
        if not found:
            # Filter false positives
            if target.startswith("http://") or target.startswith("https://"):
                continue
            if target in ["AI", "Software-Development", "PCB-Design", "AI-Agent", "home"]:
                continue
            # Skip skill references
            if "skill" in target.lower() and target not in [d["basename"] for d in notes.values()]:
                continue
            broken_links.append((path, target))

# 2. Empty/near-empty notes
empty_notes = []
for path, data in notes.items():
    lines = [l.strip() for l in data["content"].splitlines() if l.strip()]
    if len(lines) <= 2:
        empty_notes.append((path, len(lines)))

# 3. Tag case variants
tags_all = []
tag_files = {}
tag_pattern = r'^tags:\s*\[([^\]]+)\]'
for path, data in notes.items():
    for line in data["content"].splitlines()[:30]:
        m = re.match(tag_pattern, line.strip())
        if m:
            tags = [t.strip() for t in m.group(1).split(',')]
            for t in tags:
                if t:
                    tags_all.append(t)
                    if t not in tag_files:
                        tag_files[t] = []
                    tag_files[t].append(path)

# Find case variants
from collections import defaultdict
lower_map = defaultdict(list)
for t in tags_all:
    lower_map[t.lower()].append(t)

case_variants = {k: set(v) for k, v in lower_map.items() if len(set(v)) > 1}

# 4. Orphan notes (zero inbound wikilinks)
inbound = {p: 0 for p in notes}
for path, data in notes.items():
    for match in re.finditer(wikilink_pattern, data["content"]):
        target = match.group(1).strip()
        target_md = target if target.endswith('.md') else f"{target}.md"
        target_md = target_md.replace('\\', '/')
        # Find matching target
        for p, d in notes.items():
            if p == target_md or target == d["basename"] or target.replace('.md', '') == d["basename"]:
                if p != path:  # don't count self-links
                    inbound[p] += 1

orphans = [(p, 0) for p, count in inbound.items() if count == 0 
           and not p.startswith("skills/@") 
           and not p.startswith("templates/")
           and not p.startswith(".learnings/")
           and not p.startswith("portfolio/")]
orphans = sorted(orphans)[:50]

# Print report
print("="*60)
print("📊 OBSIDIAN VAULT 诊断报告")
print("="*60)
print(f"\n📝 总文件数: {len(notes)}")
print(f"🔗 损坏链接: {len(broken_links)}")
print(f"📄 空文件/近空: {len(empty_notes)}")
print(f"🏷️  标签大小写不一致: {len(case_variants)} 组")
print(f"👻 孤立笔记: {len([p for p, c in inbound.items() if c == 0])}")

if broken_links:
    print("\n" + "="*60)
    print("🔗 损坏链接详情 (前30):")
    print("="*60)
    for path, target in sorted(broken_links)[:30]:
        print(f"  {path} → [[{target}]]")
    if len(broken_links) > 30:
        print(f"  ... 还有 {len(broken_links) - 30} 个")

if empty_notes:
    print("\n" + "="*60)
    print("📄 空文件/近空文件:")
    print("="*60)
    for path, lines in sorted(empty_notes):
        print(f"  {path} ({lines} 行)")

if case_variants:
    print("\n" + "="*60)
    print("🏷️  标签大小写不一致:")
    print("="*60)
    for lower, variants in sorted(case_variants.items()):
        print(f"  {lower}: {variants}")
        for v in variants:
            print(f"    → 出现在: {', '.join(tag_files[v][:3])} {'...' if len(tag_files[v]) > 3 else ''}")

if orphans:
    print("\n" + "="*60)
    print("👻 孤立笔记 (前30):")
    print("="*60)
    for path, _ in orphans[:30]:
        print(f"  {path}")

print("\n" + "="*60)

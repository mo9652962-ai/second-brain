#!/usr/bin/env python3
"""Vault audit: empty files, broken links, tag consistency."""
import os, re
from collections import defaultdict
from pathlib import Path

VAULT = r"C:\Users\31954\.openclaw\workspace"
EXCLUDE_DIRS = {'.git', 'node_modules', '.trash', '.obsidian', '__pycache__'}

# ── Scan 1: Empty files ──
print("=== SCAN 1: EMPTY FILES ===")
empty_files = []
all_md_files = []
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
    for f in files:
        if f.endswith('.md'):
            fpath = os.path.join(root, f)
            all_md_files.append(fpath)
            try:
                sz = os.path.getsize(fpath)
                if sz == 0:
                    empty_files.append(fpath)
                elif sz < 15:
                    with open(fpath, 'r', encoding='utf-8') as fh:
                        content = fh.read().strip()
                    if not content:
                        empty_files.append(fpath)
            except:
                pass

print(f"Total .md files: {len(all_md_files)}")
if empty_files:
    output_lines = []
    for f in empty_files:
        rel = os.path.relpath(f, VAULT)
        print(f"  EMPTY: {rel}")
        output_lines.append(rel)
else:
    print("  No empty .md files found.")

# Build note index
existing_notes = set()
for fp in all_md_files:
    name_no_ext = os.path.splitext(os.path.basename(fp))[0]
    existing_notes.add(name_no_ext)
    # Also add path components for nested refs
    rel = os.path.relpath(fp, VAULT).replace('\\', '/')
    path_no_ext = os.path.splitext(rel)[0]
    existing_notes.add(path_no_ext)

# ── Scan 2: Broken wiki links ──
print("\n=== SCAN 2: BROKEN LINKS ===")
WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')

broken_links = []
wikilinks_found = 0

for fp in all_md_files:
    rel = os.path.relpath(fp, VAULT).replace('\\', '/')
    try:
        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()
    except:
        continue
    
    for match in WIKILINK_RE.finditer(content):
        target = match.group(1).strip()
        if target.startswith('http://') or target.startswith('https://'):
            continue
        if target.startswith('#'):
            continue
        note_name = target.split('#')[0].split('|')[0].strip()
        if note_name and note_name not in existing_notes:
            broken_links.append((rel, match.group(0)))
        wikilinks_found += 1

print(f"  Wikilinks found: {wikilinks_found}")
print(f"  Broken links: {len(broken_links)}")
if broken_links:
    for src, link in broken_links[:40]:
        print(f"    [{src}] -> {link}")
    if len(broken_links) > 40:
        print(f"    ... and {len(broken_links)-40} more")

# ── Scan 3: Tags ──
print("\n=== SCAN 3: TAG CONSISTENCY ===")
TAG_RE = re.compile(r'(?<!\w)#(\w[\w\-/]*)')
YAML_BLOCK_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)

tag_usages = defaultdict(list)
SKIP_TAGS = {'md','txt','py','js','tsx','ts','css','json','yaml','yml',
             'png','jpg','svg','gif','webp','ico','pdf','zip','tar','gz',
             '7z','rar','mp3','mp4','avi','mov','mkv'}

for fp in all_md_files:
    rel = os.path.relpath(fp, VAULT).replace('\\', '/')
    try:
        with open(fp, 'r', encoding='utf-8') as fh:
            content = fh.read()
    except:
        continue
    
    lines = content.split('\n')
    in_code = False
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        for match in TAG_RE.finditer(line):
            tag = match.group(1)
            if tag in SKIP_TAGS:
                continue
            tag_usages[tag].append(rel)
    
    yb = YAML_BLOCK_RE.search(content)
    if yb:
        for line in yb.group(1).split('\n'):
            if re.match(r'^tags?\s*:', line):
                tags_val = line.split(':', 1)[1].strip()
                for t in re.findall(r'[\w\-/]+', tags_val):
                    if t not in SKIP_TAGS:
                        tag_usages[t].append(f"{rel}:yaml")

tag_variants = defaultdict(set)
for tag in tag_usages:
    canonical = tag.lower().replace('-', '').replace('/', '')
    tag_variants[canonical].add(tag)

inconsistent_tags = {k: v for k, v in tag_variants.items() if len(v) > 1}
print(f"  Unique tags: {len(tag_usages)}")
print(f"  Inconsistent tag groups: {len(inconsistent_tags)}")

if inconsistent_tags:
    for canonical, variants in sorted(inconsistent_tags.items()):
        variant_detail = []
        for v in sorted(variants, key=lambda x: len(tag_usages.get(x, [])), reverse=True):
            variant_detail.append(f"{v}({len(tag_usages.get(v, []))}x)")
        print(f"    {' / '.join(variant_detail)}")

print(f"\n  Top 20 tags:")
sorted_tags = sorted(tag_usages.items(), key=lambda x: len(x[1]), reverse=True)
for tag, files in sorted_tags[:20]:
    print(f"    #{tag}: {len(files)} files")

# Check for mis-tags or misspellings (rare tags used only 1-2 times)
print(f"\n  Rare tags (possible misspellings):")
for tag, files in sorted_tags:
    if len(files) <= 2 and not tag[0].isupper():  # not proper noun
        print(f"    #{tag}: {files}")

# ── Summary ──
print(f"\n{'='*50}")
print("VAULT HEALTH SUMMARY")
print(f"{'='*50}")
print(f"Total .md files: {len(all_md_files)}")
print(f"Empty files: {len(empty_files)}")
print(f"Broken wiki links: {len(broken_links)}")
print(f"Unique tags: {len(tag_usages)}")
print(f"Inconsistent tag groups: {len(inconsistent_tags)}")

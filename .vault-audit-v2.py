#!/usr/bin/env python3
"""Smart vault audit v2: accurate broken links (handles \\| escapes, folders, ../ paths, case), empty files, tags."""
import os, re, json
from collections import defaultdict
from pathlib import Path

VAULT = Path(r"C:\Users\31954\.openclaw\workspace")
EXCLUDE_DIRS = {'.git', 'node_modules', '.trash', '.obsidian', '__pycache__', '.venv', '.claude', '.codebuddy', '.gemini', '.qoder', '.clawhub', '.skillkit', '.hermes', '.learnings', '.temp', '.github', '.code-review-graph', 'site', 'graphify-out'}

# ── Collect all files ──
all_files = []
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
    for f in files:
        all_files.append(Path(root) / f)

md_files = [f for f in all_files if f.suffix.lower() == '.md']
print(f"Total .md files: {len(md_files)}")

# Build index: basename (case-insensitive) -> set of paths; full rel path (case-insensitive) -> path
by_basename = defaultdict(list)   # lower basename -> [rel paths]
by_path = {}                      # lower rel path -> rel path
for f in md_files:
    rel = f.relative_to(VAULT).as_posix()
    by_basename[os.path.splitext(os.path.basename(rel))[0].lower()].append(rel)
    by_path[rel.lower()] = rel

# Folder index (for folder links)
folders = set()
for root, dirs, files in os.walk(VAULT):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]
    for d in dirs:
        folders.add((Path(root) / d).relative_to(VAULT).as_posix().lower())
        folders.add(d.lower())

def resolve_wikilink(target_raw, src_rel):
    """Return (status, resolved_rel or reason)."""
    t = target_raw.strip()
    if t.startswith('http://') or t.startswith('https://') or t.startswith('www.'):
        return ('external', None)
    if t.startswith('#') or t.startswith('^'):
        return ('self-heading', None)
    # strip embed marker handled by caller
    name = t
    # split heading/block
    if '#' in name:
        name = name.split('#', 1)[0]
    # display text: handle escaped \| and plain |
    # Obsidian: \| inside table cells is display separator
    if '\\|' in name:
        name = name.split('\\|', 1)[0]
    if '|' in name:
        name = name.split('|', 1)[0]
    name = name.strip()
    if not name:
        return ('empty-target', None)

    # absolute path link (starts with /)
    if name.startswith('/'):
        cand = name.lstrip('/')
        if cand.lower() in by_path:
            return ('ok', by_path[cand.lower()])
        return ('broken-abs-path', name)

    # relative path link (contains / or ../)
    if name.startswith('../'):
        parts = name.split('/')
        up = 0
        for p in parts:
            if p == '..':
                up += 1
        src_dir = Path(src_rel).parent
        for _ in range(min(up, len(src_dir.parts))):
            src_dir = src_dir.parent
        remaining = [p for p in parts if p != '..']
        cand = (src_dir / '/'.join(remaining)).as_posix()
        if cand.lower() in by_path:
            return ('ok', by_path[cand.lower()])
        # try with .md
        if not cand.endswith('.md'):
            cand2 = cand + '.md'
            if cand2.lower() in by_path:
                return ('ok', by_path[cand2.lower()])
        return ('broken-relative', name)

    if '/' in name:
        # path-like link
        if name.lower() in by_path:
            return ('ok', by_path[name.lower()])
        cand = name + '.md'
        if cand.lower() in by_path:
            return ('ok', by_path[cand.lower()])
        # maybe it's a folder link
        if name.lower() in folders:
            return ('folder', name)
        # basename of last component?
        base = os.path.basename(name).lower()
        if base in by_basename:
            return ('ok-basename', by_basename[base][0])
        return ('broken-path', name)

    # plain name -> basename lookup
    key = name.lower()
    if key in by_basename:
        # check case-exact match preferred
        exact = [r for r in by_basename[key] if os.path.basename(r).lower() == key]
        return ('ok', by_basename[key][0])
    # check extension included
    if name.lower().endswith('.md') and os.path.splitext(name)[0].lower() in by_basename:
        return ('ok', by_basename[os.path.splitext(name)[0].lower()][0])
    # attachment file (image/pdf etc) at vault level?
    if not name.endswith('.md'):
        # search attachments
        for f in all_files:
            if f.name.lower() == name.lower():
                return ('ok-attachment', f.relative_to(VAULT).as_posix())
    if name.lower() in folders:
        return ('folder', name)
    return ('broken', name)

WIKILINK_RE = re.compile(r'\[\[([^\]]+)\]\]')
results = defaultdict(list)
link_total = 0
empty_files = []
for f in md_files:
    rel = f.relative_to(VAULT).as_posix()
    try:
        content = f.read_text(encoding='utf-8', errors='ignore')
    except:
        continue
    sz = f.stat().st_size
    if sz == 0 or (sz < 20 and not content.strip()):
        empty_files.append(rel)
    for m in WIKILINK_RE.finditer(content):
        raw = m.group(1)
        link_total += 1
        # embed of non-md (image etc)
        if raw.startswith('!['):
            continue
        status, res = resolve_wikilink(raw, rel)
        results[status].append((rel, raw, res))

print(f"Wikilinks total: {link_total}")
for status in ['ok', 'ok-basename', 'ok-attachment', 'folder', 'self-heading', 'external']:
    print(f"  {status}: {len(results.get(status, []))}")
print(f"\n=== REAL BROKEN ===")
for status in ['broken', 'broken-path', 'broken-relative', 'broken-abs-path', 'empty-target']:
    items = results.get(status, [])
    print(f"--- {status}: {len(items)}")
    for src, raw, res in items[:60]:
        print(f"  [{src}] -> {raw}")

# Case mismatches (file exists but different case) - informational
print(f"\n=== CASE MISMATCH (works on Windows, breaks on other OS) ===")
case_issues = []
for src, raw, res in results.get('ok', []):
    t = raw
    if '\\|' in t: t = t.split('\\|', 1)[0]
    if '|' in t: t = t.split('|', 1)[0]
    if '#' in t: t = t.split('#', 1)[0]
    t = t.strip()
    if '/' in t or t.startswith('../'):
        continue
    if res and os.path.basename(res).lower() == t.lower() and os.path.basename(res) != t:
        case_issues.append((src, t, res))
print(f"Case mismatches: {len(case_issues)}")
for src, t, res in case_issues[:30]:
    print(f"  [{src}] -> [[{t}]] resolves to {res}")

# ── Empty files (incl. whitespace-only) ──
print(f"\n=== EMPTY FILES: {len(empty_files)} ===")
for e in empty_files:
    print(f"  {e}")

# ── Tags ──
print(f"\n=== TAGS ===")
TAG_RE = re.compile(r'(?<!\w)#([\u4e00-\u9fff\w][\w\-/]*)')
YAML_BLOCK_RE = re.compile(r'^---\n(.*?)\n---', re.DOTALL)
SKIP_TAGS = {'md','txt','py','js','tsx','ts','css','json','yaml','yml','png','jpg','svg','gif','webp','ico','pdf','zip','tar','gz','7z','rar','mp3','mp4','avi','mov','mkv','cpp','c','h','sh','bat','exe','dll','xlsx','docx','pptx','stl','step','dxf','ino','vue','java','go','rs','rb','php','sql','toml','cfg','ini','lock'}
tag_usages = defaultdict(list)
for f in md_files:
    rel = f.relative_to(VAULT).as_posix()
    try:
        content = f.read_text(encoding='utf-8', errors='ignore')
    except:
        continue
    lines = content.split('\n')
    in_code = False
    in_yaml = False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == '---':
            in_yaml = True
            continue
        if in_yaml:
            if line.strip() == '---':
                in_yaml = False
            continue
        if line.strip().startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        for match in TAG_RE.finditer(line):
            tag = match.group(1)
            if tag.lower() in SKIP_TAGS:
                continue
            tag_usages[tag].append(rel)
    yb = YAML_BLOCK_RE.search(content)
    if yb:
        for line in yb.group(1).split('\n'):
            m = re.match(r'^tags?\s*:\s*(.*)', line)
            if m:
                tv = m.group(1).strip()
                if tv.startswith('['):
                    for t in re.findall(r'[\w\u4e00-\u9fff\-/]+', tv):
                        if t.lower() not in SKIP_TAGS:
                            tag_usages[t].append(f"{rel}:yaml")

tag_variants = defaultdict(set)
for tag in tag_usages:
    canonical = tag.lower().replace('-', '').replace('/', '').replace('_', '')
    tag_variants[canonical].add(tag)
inconsistent = {k: v for k, v in tag_variants.items() if len(v) > 1}
print(f"Unique tags: {len(tag_usages)}")
print(f"Inconsistent tag groups: {len(inconsistent)}")
for canonical, variants in sorted(inconsistent.items()):
    detail = sorted(variants, key=lambda x: len(tag_usages.get(x, [])), reverse=True)
    d = ' / '.join(f"{v}({len(tag_usages.get(v, []))}x)" for v in detail)
    print(f"  {d}")

print(f"\nTop 15 tags:")
for tag, files in sorted(tag_usages.items(), key=lambda x: len(x[1]), reverse=True)[:15]:
    print(f"  #{tag}: {len(files)}")

with open('.vault-audit-results.json', 'w', encoding='utf-8') as fh:
    json.dump({
        'broken': {s: results.get(s, []) for s in ['broken', 'broken-path', 'broken-relative', 'broken-abs-path', 'empty-target']},
        'case': case_issues,
        'empty': empty_files,
        'tags_inconsistent': {k: sorted(v) for k, v in inconsistent.items()},
        'tag_usages': {k: len(v) for k, v in tag_usages.items()},
    }, fh, ensure_ascii=False, indent=1)
print("\nSaved .vault-audit-results.json")

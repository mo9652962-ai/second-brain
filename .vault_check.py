#!/usr/bin/env python3
"""Vault health check - broken links, tag consistency, empty files."""
import os, re, collections, json

WORKSPACE = "."
EXCLUDE_PATTERNS = ['.git', '.obsidian']

def should_exclude(path):
    for p in EXCLUDE_PATTERNS:
        if f'/{p}/' in path or path.startswith(p) or path.startswith('./' + p):
            return True
    return False

# Collect all .md files
all_md = []
for root, dirs, files in os.walk(WORKSPACE):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_PATTERNS and not d.startswith('.git')]
    for f in files:
        if f.endswith('.md'):
            all_md.append(os.path.normpath(os.path.join(root, f)))

print(f"Total .md files: {len(all_md)}")

# Build lookup of existing notes
existing_basenames = set()    # lowercase basename without .md
existing_paths = set()         # lowercase relative path without .md
for fp in all_md:
    name = os.path.splitext(os.path.basename(fp))[0]
    existing_basenames.add(name.lower())
    rel = os.path.relpath(fp, WORKSPACE).replace('\\', '/')
    rel_no_ext = os.path.splitext(rel)[0]
    existing_paths.add(rel_no_ext.lower())

def resolve_wikilink(target):
    """Try to resolve a wikilink target to an existing file."""
    target = target.strip()
    # Strip alias: [[note|Alias]]
    target = target.split('|')[0].strip()
    # Strip heading anchor: [[note#Heading]]
    target = target.split('#')[0].strip()
    if not target:
        return False, ""
    
    norm = target.replace('\\', '/')
    # Try direct file
    p1 = os.path.join(WORKSPACE, norm + '.md')
    p2 = os.path.join(WORKSPACE, norm)
    if os.path.isfile(p1):
        return True, os.path.relpath(p1, WORKSPACE).replace('\\', '/')
    if os.path.isfile(p2):
        return True, os.path.relpath(p2, WORKSPACE).replace('\\', '/')
    # Try by basename
    base = os.path.basename(norm).lower()
    if base in existing_basenames:
        return True, f"{base}.md"
    # Try within existing_paths
    if norm.lower() in existing_paths:
        return True, norm + '.md'
    return False, ""

# Scan all files
broken_wikilinks = []
broken_mdlinks = []
broken_embeds = []
all_tags = collections.Counter()
tag_spellings = collections.defaultdict(list)
file_sizes = {}
file_issues = []

for fp in all_md:
    rel = os.path.relpath(fp, WORKSPACE).replace('\\', '/')
    sz = os.path.getsize(fp)
    file_sizes[rel] = sz
    
    try:
        with open(fp, 'r', encoding='utf-8', errors='replace') as fh:
            content = fh.read()
    except Exception as e:
        file_issues.append((rel, f"read_error: {e}"))
        continue
    
    # Check empty/near-empty
    if sz == 0:
        file_issues.append((rel, "empty_file"))
        continue
    
    non_blank = sum(1 for l in content.split('\n') if l.strip())
    if non_blank <= 2:
        file_issues.append((rel, f"near_empty: {non_blank} non-blank lines, {sz} bytes"))
    
    # --- WIKILINKS [[...]] ---
    for m in re.finditer(r'\[\[([^\]]+)\]\]', content):
        target = m.group(1)
        line_num = content[:m.start()].count('\n') + 1
        exists, resolved = resolve_wikilink(target)
        if not exists:
            broken_wikilinks.append((rel, line_num, target))
    
    # --- MD LINKS [text](path) to local .md ---
    for m in re.finditer(r'\[([^\]]*)\]\(([^)]+)\)', content):
        url = m.group(2)
        if url.endswith('.md') and not url.startswith('http') and '://' not in url:
            line_num = content[:m.start()].count('\n') + 1
            clean_url = url.split('#')[0]
            src_dir = os.path.dirname(os.path.join(WORKSPACE, rel))
            resolved = os.path.normpath(os.path.join(src_dir, clean_url))
            if not os.path.isfile(resolved):
                broken_mdlinks.append((rel, line_num, url))
    
    # --- EMBEDS ![[...]] ---
    for m in re.finditer(r'!\[\[([^\]]+)\]\]', content):
        target = m.group(1)
        line_num = content[:m.start()].count('\n') + 1
        norm = target.replace('\\', '/')
        found = False
        for candidate in [
            os.path.join(WORKSPACE, norm),
            os.path.join(WORKSPACE, norm + '.md'),
            os.path.join(WORKSPACE, 'assets', norm),
        ]:
            if os.path.isfile(candidate):
                found = True
                break
        # Check with image extensions
        if not found:
            for ext in ['png', 'jpg', 'jpeg', 'gif', 'svg', 'webp', 'bmp']:
                if os.path.isfile(os.path.join(WORKSPACE, norm + '.' + ext)):
                    found = True
                    break
                if os.path.isfile(os.path.join(WORKSPACE, 'assets', norm + '.' + ext)):
                    found = True
                    break
                # Check with figma, etc extension
                if os.path.isfile(os.path.join(WORKSPACE, norm)):
                    found = True
                    break
        if not found:
            broken_embeds.append((rel, line_num, target))
    
    # --- TAGS ---
    # Inline tags
    for m in re.finditer(r'(?:^|\s)#([a-zA-Z][\w/-]*)', content):
        tag = m.group(1)
        all_tags[tag] += 1
        tag_spellings[tag.lower()].append((tag, rel))
    
    # YAML frontmatter tags
    ym = re.match(r'^---\s*\n(.*?)\n(?:---|\.\.\.)', content, re.DOTALL)
    if ym:
        yaml_lines = ym.group(1).split('\n')
        for line in yaml_lines:
            stripped = line.strip()
            if stripped.startswith('- '):
                tag = stripped[2:].strip().strip('"\'')
                all_tags[tag] += 1
                tag_spellings[tag.lower()].append((tag, rel))

# Summary
print("=" * 60)
print("VAULT HEALTH CHECK REPORT")
print("=" * 60)

print(f"\n📁 Total: {len(all_md)} .md files")

print(f"\n📌 EMPTY / NEAR-EMPTY FILES")
issues = [i for i in file_issues if i[1].startswith('empty') or i[1].startswith('near')]
for rel, issue in issues:
    print(f"  🗑  {rel} — {issue}")
print(f"  Total: {len(issues)}")

print(f"\n🔗 BROKEN WIKILINKS [[...]]")
for rel, line, target in broken_wikilinks:
    print(f"  ❌ {rel}:{line} → [[{target}]]")
print(f"  Total: {len(broken_wikilinks)}")

print(f"\n🔗 BROKEN MARKDOWN LINKS [text](.md)")
for rel, line, url in broken_mdlinks:
    print(f"  ❌ {rel}:{line} → [{url}]")
print(f"  Total: {len(broken_mdlinks)}")

print(f"\n🔗 BROKEN EMBEDS ![[...]]")
for rel, line, target in broken_embeds:
    print(f"  ❌ {rel}:{line} → ![[{target}]]")
print(f"  Total: {len(broken_embeds)}")

print(f"\n🏷  TAG ANALYSIS (Top 50)")
for tag, count in all_tags.most_common(50):
    print(f"  #{tag}: {count}")

print(f"\n🏷  SIMILAR TAG GROUPS (possible inconsistencies)")
groups = {}
for tag_lower, variants in tag_spellings.items():
    base = tag_lower.replace('-', '').replace('_', '').replace('/', '')
    if base not in groups:
        groups[base] = set()
    for v, _ in variants:
        groups[base].add(v)

for base, variants in sorted(groups.items()):
    if len(variants) > 1:
        print(f"  ⚠️  '{base}' → {sorted(variants)}")

print(f"\n📦 FILE SIZE DISTRIBUTION")
sizes = list(file_sizes.values())
if sizes:
    print(f"  Min: {min(sizes)} bytes")
    print(f"  Max: {max(sizes)} bytes")
    print(f"  Median: {sorted(sizes)[len(sizes)//2]} bytes")
    print(f"  Total: {sum(sizes)} bytes")
    by_size = [(sz, p) for p, sz in file_sizes.items() if sz < 50]
    if by_size:
        print(f"\n  Files under 50 bytes:")
        for sz, p in sorted(by_size):
            print(f"    {p} ({sz} bytes)")

# Print all file issues
print(f"\n📋 ALL FILE ISSUES")
for rel, issue in file_issues:
    print(f"  {rel}: {issue}")

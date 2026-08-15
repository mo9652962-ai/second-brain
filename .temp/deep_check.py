# -*- coding: utf-8 -*-
"""Deep vault check: path-based wikilinks, orphan notes, empty/placeholder files, tag variants."""
import pathlib, re, sys
from collections import Counter

VAULT = pathlib.Path(r"C:\Users\31954\.openclaw\workspace")
EXCLUDE_DIRS = {'.git', '.obsidian', '.venv', 'node_modules', '.temp'}

def vault_files():
    return [f for f in VAULT.rglob('*.md')
            if not any(p in EXCLUDE_DIRS for p in f.parts)]

files = vault_files()
print(f"Total .md files: {len(files)}")

ci_map = {}
for f in files:
    ci_map.setdefault(f.stem.lower(), []).append(f)

# === 1. Path-based wikilinks: verify the actual path exists ===
path_link_re = re.compile(r'\[\[([^\[\]]+?)\]\]')
path_broken = []
for f in files:
    content = f.read_bytes().decode('utf-8', errors='ignore')
    rel = str(f.relative_to(VAULT)).replace('\\', '/')
    for m in path_link_re.finditer(content):
        raw = m.group(1)
        target = raw.split('#')[0].split('|')[0].split('^')[0].strip()
        if not target or '/' not in target:
            continue
        # skip known non-note targets
        if target.startswith('skills/') or target.startswith('http'):
            continue
        # candidate path relative to vault
        cand = (VAULT / target).with_suffix('.md')
        if not cand.exists():
            path_broken.append((rel, raw))

print(f"\n=== Path-based broken links: {len(path_broken)} ===")
for r, t in path_broken[:40]:
    print(f"  {r} -> [{t}]")

# === 2. Orphan notes (no outgoing wikilinks at all) ===
orphans = []
for f in files:
    content = f.read_bytes().decode('utf-8', errors='ignore')
    if not re.findall(r'\[\[([^\[\]]+?)\]\]', content):
        rel = str(f.relative_to(VAULT)).replace('\\', '/')
        # skip known structural files
        if f.stem.lower() in ('home', 'readme', 'index', 'knowledge-map') or rel.startswith('templates/'):
            continue
        orphans.append(rel)
print(f"\n=== Orphan notes (no outgoing links): {len(orphans)} ===")
for o in orphans[:40]:
    print(f"  {o}")

# === 3. Empty / placeholder-only files ===
empty = []
for f in files:
    content = f.read_bytes().decode('utf-8', errors='ignore').strip()
    rel = str(f.relative_to(VAULT)).replace('\\', '/')
    if not content:
        empty.append((rel, 0))
    elif len(content) < 80 and not re.match(r'^---\r?\n', content):
        empty.append((rel, len(content)))
print(f"\n=== Empty/placeholder files: {len(empty)} ===")
for e, sz in empty[:40]:
    print(f"  {sz}b: {e}")

# === 4. Tag variants beyond case: singular/plural, similar spellings ===
tag_re = re.compile(r'^tags:\s*\[(.*?)\]', re.M)
tag_counter = Counter()
for f in files:
    p = str(f.relative_to(VAULT)).replace('\\', '/')
    if p.startswith(('skills/', '.claude/', '.gemini/', '.qoder/', '.codebuddy/', 'templates/')):
        continue
    content = f.read_bytes().decode('utf-8', errors='ignore')
    m = tag_re.search(content)
    if m:
        for t in m.group(1).split(','):
            t = t.strip().strip('"\'')
            if t:
                tag_counter[t] += 1

print(f"\n=== Tag counts (top 40) ===")
for t, c in tag_counter.most_common(40):
    print(f"  {t}: {c}")

# singular/plural pairs worth noting
pairs = ['concept/concepts', 'skill/skills', 'tool/tools', 'project/projects',
         'note/notes', 'idea/ideas', 'research/researches', 'MOC/mocs',
         'AI/ai', 'PCB/pcb', 'MCP/mcp', 'API/api', 'SQL/sql', 'LLM/llm']
print(f"\n=== Singular/plural + case pairs ===")
for pair in pairs:
    a, b = pair.split('/')
    ca, cb = tag_counter.get(a, 0), tag_counter.get(b, 0)
    if ca and cb:
        print(f"  {a}({ca}) vs {b}({cb})")

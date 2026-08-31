# -*- coding: utf-8 -*-
"""Count frontmatter tag variants for the 6 case-collision groups, per-file.
Only vault notes (skip skills/, templates/, .claude/ etc. system dirs)."""
import pathlib, re
from collections import Counter, defaultdict

VAULT = pathlib.Path(r"C:\Users\31954\.openclaw\workspace")
EXCLUDE_DIRS = {'.git', '.obsidian', '.venv', 'node_modules', '.temp'}

def vault_files():
    return [f for f in VAULT.rglob('*.md')
            if not any(p in EXCLUDE_DIRS for p in f.parts)]

files = vault_files()
tag_re = re.compile(r'^tags:\s*\[(.*?)\]', re.M)

# variant -> count (across all vault notes)
variant_count = Counter()
# variant -> list of files
variant_files = defaultdict(list)

for f in files:
    p = str(f.relative_to(VAULT))
    if any(p.startswith(d) for d in ['skills/', '.claude/', '.gemini/', '.qoder/', '.codebuddy/', 'templates/']):
        continue
    content = f.read_bytes().decode('utf-8', errors='ignore')
    m = tag_re.search(content)
    if m:
        for t in m.group(1).split(','):
            t = t.strip().strip('"\'')
            if t:
                variant_count[t] += 1
                variant_files[t].append(p)

# Group by lower()
groups = defaultdict(Counter)
for t, c in variant_count.items():
    groups[t.lower()][t] += c

print("=== Case-collision tag groups (majority-wins normalization targets) ===")
for low, variants in sorted(groups.items()):
    if len(variants) > 1:
        print(f"\n[{low}] total={sum(variants.values())}")
        for v, c in variants.most_common():
            print(f"    {v}: {c} files")
            # show up to 4 files per variant
            for fp in variant_files[v][:4]:
                print(f"        - {fp}")
            if len(variant_files[v]) > 4:
                print(f"        ... +{len(variant_files[v])-4} more")

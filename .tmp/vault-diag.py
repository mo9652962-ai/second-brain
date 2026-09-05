# -*- coding: utf-8 -*-
"""Vault diagnostic: empty files + full frontmatter tag consistency check."""
import pathlib, re, collections, sys

ROOT = pathlib.Path(r"C:\Users\31954\.openclaw\workspace")
EXCLUDE_DIRS = {'.git', '.obsidian', '.venv', 'node_modules', '__pycache__', '.backup',
                '.tmp', '.temp', 'site', 'skills', 'graphify-out', '.claude', '.codebuddy',
                '.gemini', '.qoder', '.clawhub', '.hermes', '.learnings', 'mcp', 'pipelines',
                'outputs', 'traces', 'system', '.code-review-graph', '.skillkit'}
SYSTEM_FILES = {'README.md', 'AGENTS.md', 'SOUL.md', 'MEMORY.md', 'SUPPORT.md', 'HOME.md',
                'INDEX.md', 'TOOLS.md', 'CHANGELOG.md', 'USER.md', 'IDENTITY.md',
                'HEARTBEAT.md', 'SECURITY.md', 'CODE_OF_CONDUCT.md', 'CONTRIBUTING.md',
                'LICENSE', 'DREAMS.md'}

def is_skip(p: pathlib.Path):
    for part in p.parts:
        if part in EXCLUDE_DIRS:
            return True
    return False

mds = [p for p in ROOT.rglob('*.md') if not is_skip(p) and '.git' not in p.parts]
print(f"Scanned md files: {len(mds)}")

# ---- Empty / near-empty files ----
empty = []
near = []
for p in mds:
    try:
        sz = p.stat().st_size
        if sz == 0:
            empty.append(p)
            continue
        txt = p.read_text(encoding='utf-8', errors='ignore')
        if len(txt.strip()) < 3:
            near.append(p)
    except Exception as e:
        print(f"READ ERR {p}: {e}")

print(f"\n== EMPTY FILES (0 bytes): {len(empty)} ==")
for p in empty:
    print("  ", p.relative_to(ROOT))
print(f"== NEAR-EMPTY (<3 chars): {len(near)} ==")
for p in near:
    print("  ", p.relative_to(ROOT))

# ---- Tag consistency: group all frontmatter tags by lower(), flag multi-variant groups ----
variants = collections.defaultdict(collections.Counter)
for p in mds:
    if p.name in SYSTEM_FILES:
        continue
    if 'skills' in p.parts:
        continue
    try:
        txt = p.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    m = re.search(r'^tags:\s*\[([^\]]+)\]', txt, re.M)
    if not m:
        continue
    for t in m.group(1).split(','):
        t = t.strip().strip('"\'')
        if not t:
            continue
        variants[t.lower()][t] += 1

print(f"\n== TAG VARIANTS (multi-case/spelling collisions): ==")
collisions = {k: v for k, v in variants.items() if len(v) > 1}
if not collisions:
    print("  (none)")
for k in sorted(collisions):
    print(f"  {k!r}: {dict(collisions[k])}")

# also report total distinct tags for context
print(f"\n== Distinct tags: {len(variants)} ==")

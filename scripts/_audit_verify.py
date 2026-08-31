# -*- coding: utf-8 -*-
"""Verify reported broken links against actual file existence (case-insensitive,
stripping .md ext, resolving relative-to-vault paths). Also check skill dir."""
import pathlib, re, sys
from collections import Counter

VAULT = pathlib.Path(r"C:\Users\31954\.openclaw\workspace")
EXCLUDE_DIRS = {'.git', '.obsidian', '.venv', 'node_modules', '.temp'}

def vault_files():
    return [f for f in VAULT.rglob('*.md')
            if not any(p in EXCLUDE_DIRS for p in f.parts)]

files = vault_files()
# Case-insensitive stem map (no extension)
ci_stem = {}
ci_path = {}
for f in files:
    ci_stem.setdefault(f.stem.lower(), []).append(f)
    p = str(f.relative_to(VAULT)).replace('\\', '/').lower()
    ci_path.setdefault(p, []).append(f)

# Skill names known to exist in Hermes skills dirs (from skills_list)
SKILL_NAMES = {
    'shumo-paper-writing','nextjs-deploy-test','multi-end-ai-provider-config',
    'ai-freelance-pricing','grill-with-docs','xianyu-monetization',
    'src-bug-hunting','src-recon-workflow','web-security-lab-setup',
    'pentest-lab-setup','nmap-scanning','src-recon-scanning','xianyu-quote-script',
    'hermes-smart-model-router','hermes-provider-matrix',
}

link_re = re.compile(r'\[\[([^\[\]]+?)\]\]')
rows = []
for f in files:
    content = f.read_bytes().decode('utf-8', errors='ignore')
    rel = str(f.relative_to(VAULT)).replace('\\', '/')
    for m in link_re.finditer(content):
        raw = m.group(1)
        target = raw.split('#')[0].split('|')[0].split('^')[0].strip()
        if not target:
            continue
        tpath = target.replace('\\', '/').rstrip('/')
        base = tpath.split('/')[-1]
        # strip .md if present
        base_nox = base[:-3] if base.lower().endswith('.md') else base
        # case-insensitive stem exists?
        if base_nox.lower() in ci_stem:
            continue
        # known false positives
        if base_nox.lower() in ('home', 'memory'):
            continue
        if target in ('name','their-name','skill-name',':space:','[...]','...','path','path\\','celld','所属MOC'):
            continue
        if re.fullmatch(r'note-\d+|series-\d{4}-\d{2}-\d{2}', target):
            continue
        if target.lower().replace(' ', '') in ('wikilink','wikipedia'):
            continue
        if target.startswith('skills/'):
            continue
        if 'skill' in target.lower() and target.endswith('skill'):
            continue
        if 'maintenance' in rel or 'memory/.archive/' in rel or 'memory/2026/07/' in rel:
            continue
        # Is it a skill name (exists in Hermes skills, not vault)?
        is_skill = base_nox in SKILL_NAMES
        # Does the full path exist (case-insensitive)?
        path_ok = False
        if '/' in tpath:
            # strip .md for path lookup too
            tpath_nox = tpath[:-3] if tpath.lower().endswith('.md') else tpath
            path_ok = tpath_nox.lower() in ci_path or (tpath_nox + '.md').lower() in ci_path
        rows.append((rel, raw, base_nox, is_skill, path_ok))

print(f"Total .md: {len(files)}")
print(f"Reported broken links: {len(rows)}")
print(f"\n{'FILE':<70} {'TARGET':<45} {'skill?':<6} {'path_exists?':<12}")
for rel, raw, base_nox, is_skill, path_ok in rows:
    print(f"{rel[:69]:<70} {raw[:44]:<45} {str(is_skill):<6} {str(path_ok):<12}")

# What's genuinely broken = not a skill name AND no path exists
genuine = [r for r in rows if not r[3] and not r[4]]
print(f"\n=== GENUINELY BROKEN (not skill, no path): {len(genuine)} ===")
for rel, raw, base_nox, is_skill, path_ok in genuine:
    print(f"  {rel} -> [{raw}]")

#!/usr/bin/env python3
"""Vault maintenance v2 (conservative): binary-safe edits, no line-ending churn.
- delete empty files
- fix real broken links (exact string replace, binary mode)
- normalize tag case variants ONLY in frontmatter tags + inline tags outside code, skip hex colors
"""
import os, re, json
from pathlib import Path
from collections import defaultdict, Counter

VAULT = Path(r"C:\Users\31954\.openclaw\workspace")
NON_SKILL_DIRS = ['knowledge','memory','research','projects','outputs','playbooks','health','system','templates','docs','concepts','portfolio']
ROOT_FILES = ['HOME.md','INDEX.md','README.md','MEMORY.md','DREAMS.md','TOOLS.md','USER.md','IDENTITY.md','HEARTBEAT.md','CHANGELOG.md','SUPPORT.md']
SKIP = {'md','txt','py','js','tsx','ts','css','json','yaml','yml','png','jpg','svg','gif','webp','ico','pdf','zip','tar','gz','7z','rar','mp3','mp4','avi','mov','mkv','cpp','c','h','sh','bat','exe','dll','xlsx','docx','pptx','stl','step','dxf','ino','vue','java','go','rs','rb','php','sql','toml','cfg','ini','lock','MOC','Home','INDEX','tags'}
SKIP_B = {s.encode() for s in SKIP}

report = {'deleted': [], 'links_fixed': [], 'tags_fixed': {}}

def iter_files():
    for d in NON_SKILL_DIRS:
        for p in (VAULT / d).rglob('*.md'):
            yield p
    for f in ROOT_FILES:
        p = VAULT / f
        if p.exists():
            yield p

# ═══════ 1. DELETE EMPTY FILES ═══════
empty_targets = [
    'projects/ai-cad-pipeline/output_assembly/bolt.gcode',
    'projects/ai-cad-pipeline/output_assembly/nut.gcode',
    'projects/ai-cad-pipeline/output_assembly/nut_test.gcode',
    'projects/ai-cad-pipeline/output_assembly/washer.gcode',
]
for rel in empty_targets:
    p = VAULT / rel
    if p.exists() and p.stat().st_size == 0:
        p.unlink()
        report['deleted'].append(rel)

# ═══════ 2. FIX BROKEN LINKS (binary-safe exact replace) ═══════
link_fixes = {
    'memory/2026/07/2026-07-26.md': [
        (b'[[2026-07-26-review]]', b'2026-07-26-review'),
        (b'[[2026-07-25-1204]]', b'2026-07-25-1204'),
        (b'[[2026-07-26-maintenance]]', b'2026-07-26-maintenance'),
        (b'[[2026-07-26-reflection]]', b'2026-07-26-reflection'),
    ],
    'memory/2026/07/2026-07-27.md': [
        (b'[[2026-07-27-reflection]]', b'2026-07-27-reflection'),
        (b'[[2026-07-27-review]]', b'2026-07-27-review'),
    ],
    'memory/dreaming/light/2026-08-06.md': [
        (b'[[2026-07-25-1204]]', b'2026-07-25-1204'),
        (b'[[2026-07-26-maintenance]]', b'2026-07-26-maintenance'),
        (b'[[2026-07-26-reflection]]', b'2026-07-26-reflection'),
    ],
    'memory/dreaming/light/2026-08-07.md': [
        (b'[[2026-07-25-1204]]', b'2026-07-25-1204'),
        (b'[[2026-07-26-maintenance]]', b'2026-07-26-maintenance'),
        (b'[[2026-07-26-reflection]]', b'2026-07-26-reflection'),
    ],
    'knowledge/AI/qm-scope-methodology.md': [
        (b'[[../memory/2026/08/2026-08-02-eu-ai-act|EU AI Act \xe5\x8d\xa1\xe7\x89\x87]]', b'[[2026-08-02-eu-ai-act|EU AI Act \xe5\x8d\xa1\xe7\x89\x87]]'),
    ],
    'SUPPORT.md': [
        (b'[[skills/hardware/PCB-Design-Automation.md]]', b'[[skills/hardware/PCB-Design-Automation-2026.md]]'),
    ],
}
for rel, subs in link_fixes.items():
    p = VAULT / rel
    if not p.exists():
        print(f"  !! missing {rel}"); continue
    data = p.read_bytes()
    changed = False
    for old, new in subs:
        if old in data:
            data = data.replace(old, new)
            report['links_fixed'].append(f"{rel}: {old.decode('utf-8', 'ignore')} -> {new.decode('utf-8', 'ignore')}")
            changed = True
    if changed:
        p.write_bytes(data)

# ═══════ 3. TAG CASE NORMALIZATION ═══════
YAML_BLOCK_RE = re.compile(rb'^---\r?\n(.*?)\r?\n---', re.DOTALL)
INLINE_TAG_RE = re.compile(rb'(?<!\w)#([A-Za-z][A-Za-z0-9_\-/]*)')

def is_hex_color(tag: bytes) -> bool:
    # only 6/8-digit hex (typical CSS colors like #ffffff); 3-digit may be real tags (CAD)
    return re.fullmatch(rb'[0-9a-fA-F]{6}|[0-9a-fA-F]{8}', tag) is not None

# Count tag usage: frontmatter + inline (outside code), skip hex colors
tag_count = Counter()
tag_files = defaultdict(set)
for p in iter_files():
    data = p.read_bytes()
    rel = p.relative_to(VAULT).as_posix()
    lines = data.split(b'\n')
    in_code = False
    for line in lines:
        if line.strip().startswith(b'```'):
            in_code = not in_code; continue
        if in_code: continue
        for m in INLINE_TAG_RE.finditer(line):
            t = m.group(1)
            if t.lower() in SKIP_B: continue
            if is_hex_color(t): continue
            ts = t.decode()
            tag_count[ts] += 1; tag_files[ts].add(rel)
    yb = YAML_BLOCK_RE.search(data)
    if yb:
        block = yb.group(1).decode('utf-8', errors='ignore')
        for line in block.split('\n'):
            m = re.match(r'^\s*tags?\s*:\s*(.*)', line)
            if m:
                for t in re.findall(r'[A-Za-z\u4e00-\u9fff][\w\u4e00-\u9fff\-/]*', m.group(1)):
                    if t.lower() in SKIP: continue
                    # frontmatter tags are never CSS colors; skip hex check here (CAD is a real tag)
                    tag_count[t] += 1; tag_files[t].add(rel)

variants = defaultdict(set)
for t in tag_count:
    key = t.lower().replace('-','').replace('/','').replace('_','')
    variants[key].add(t)

def canonical_for(group):
    total = {v: tag_count[v] for v in group}
    mx = max(total.values())
    top = [v for v in total if total[v] == mx]
    if len(top) == 1:
        return top[0]
    lower = [v for v in top if v == v.lower()]
    return lower[0] if lower else sorted(top)[0]

tag_plan = {}
for key, group in sorted(variants.items()):
    if len(group) < 2: continue
    if key.isdigit() or all(c.isdigit() or c in '-/' for c in key):
        continue  # rule #17 refs
    canon = canonical_for(group)
    for v in group:
        if v != canon:
            tag_plan[v] = canon
# Apply: binary-safe, only replace tags that exist as actual tag tokens
def apply_tag_fix(data: bytes, mapping) -> bytes:
    """Replace #variant -> #canonical outside code fences (binary safe)."""
    lines = data.split(b'\n')
    out = []
    in_code = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith(b'```'):
            in_code = not in_code
        if not in_code:
            for v, c in mapping.items():
                vb, cb = v.encode(), c.encode()
                pat = re.compile(rb'(?<!\w)#' + re.escape(vb) + rb'(?![A-Za-z0-9\-/])')
                line = pat.sub(b'#' + cb, line)
        out.append(line)
    return b'\n'.join(out)

def apply_frontmatter_fix(data: bytes, mapping) -> bytes:
    def repl(m):
        block = m.group(0)  # full match incl. --- markers, preserves \r\n
        def line_fix(line):
            tm = re.match(rb'^(\s*tags?\s*:\s*)(.*)$', line)
            if tm:
                val = tm.group(2)
                for v, c in mapping.items():
                    vb, cb = v.encode(), c.encode()
                    pat = re.compile(rb'(?<![A-Za-z0-9\-/])' + re.escape(vb) + rb'(?![A-Za-z0-9\-/])')
                    val = pat.sub(cb, val)
                return tm.group(1) + val
            return line
        return b'\n'.join(line_fix(line) for line in block.split(b'\n'))
    return YAML_BLOCK_RE.sub(repl, data)

n_tag_files = 0
for p in iter_files():
    data = p.read_bytes()
    rel = p.relative_to(VAULT).as_posix()
    new_data = apply_tag_fix(data, tag_plan)
    new_data = apply_frontmatter_fix(new_data, tag_plan)
    if new_data != data:
        p.write_bytes(new_data)
        n_tag_files += 1
        changed = [f"#{v}->#{c}" for v, c in tag_plan.items() if rel in tag_files.get(v, set())]
        report['tags_fixed'][rel] = changed

# ═══════ OUTPUT ═══════
print("=" * 60)
print("VAULT MAINTENANCE REPORT v2")
print("=" * 60)
print(f"\n[1] Deleted empty files: {len(report['deleted'])}")
for f in report['deleted']:
    print(f"    DEL {f}")
print(f"\n[2] Broken links fixed: {len(report['links_fixed'])}")
for f in report['links_fixed']:
    print(f"    FIX {f}")
print(f"\n[3] Tag normalization: {len(tag_plan)} mappings, {n_tag_files} files touched")
for v, c in sorted(tag_plan.items()):
    print(f"    MAP #{v} -> #{c}")
for rel, ch in sorted(report['tags_fixed'].items()):
    print(f"    FILE {rel}: {', '.join(ch) if ch else '(content changed)'}")

with open(VAULT / '.vault-maintenance-report.json', 'w', encoding='utf-8') as fh:
    json.dump(report, fh, ensure_ascii=False, indent=1)
print("\nSaved .vault-maintenance-report.json")

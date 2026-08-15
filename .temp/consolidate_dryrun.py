#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vault 分支整合 dry-run：检查重名、引用清单、MOC 内容。"""
import pathlib, re, sys

root = pathlib.Path(r'C:\Users\31954\.openclaw\workspace')
DRY = '--apply' not in sys.argv

# ========== 1. knowledge 合并重名检查 ==========
merges = [
    ('knowledge/Academic', 'knowledge/Research', ['MOC-Academic.md']),
    ('knowledge/AI',       'knowledge/Dev',      ['MOC-AI.md']),
    ('knowledge/Design',   'knowledge/Hardware', ['MOC-Design.md']),
]
print("=== 1. knowledge 合并重名检查 ===")
for src, dst, exclude in merges:
    sd, dd = root/src, root/dst
    if not sd.is_dir():
        print(f"  [SKIP] {src} 不存在")
        continue
    conflicts = []
    for f in sd.glob('*.md'):
        if f.name in exclude:
            continue
        if (dd/f.name).exists():
            conflicts.append(f.name)
    n = len([f for f in sd.glob('*.md') if f.name not in exclude])
    print(f"  {src} → {dst}: {n} 篇将迁移, 重名冲突: {conflicts if conflicts else '无 ✅'}")

# ========== 2. dreaming 压平 ==========
print("\n=== 2. dreaming 压平方案 ===")
dr = root/'memory'/'dreaming'
all_targets = []
for sub in ['light', 'rem', 'deep']:
    sd = dr/sub
    if not sd.is_dir():
        continue
    for f in sd.glob('*'):
        if f.suffix == '.md':
            new_name = f'{sub}-{f.name}'  # 前缀防重名
        else:
            new_name = f'{sub}-{f.name}'
        all_targets.append((sub, f.name, new_name))
        dup = (dr/new_name).exists()
        print(f"  {sub}/{f.name} → dreaming/{new_name}" + (" ⚠️目标已存在!" if dup else ""))
print(f"  共 {len(all_targets)} 个文件")

# ========== 3. 全仓旧路径引用清单 ==========
print("\n=== 3. 需要修复的引用 ===")
SKIP = {'.git','.obsidian','.venv','__pycache__','site','skills','graphify-out','outputs','mcp','scripts','templates','pipelines','traces','docs','playbooks','system','.claude','.clawhub','.codebuddy','.gemini','.qoder','.skillkit','.hermes','.learnings','.temp','.github'}
files = [f for f in root.rglob('*.md') if not any(p in SKIP for p in f.parts)]
patterns = [
    ('[[knowledge/Academic/', '[[knowledge/Research/'),
    ('[[knowledge/AI/',       '[[knowledge/Dev/'),
    ('[[knowledge/Design/',   '[[knowledge/Hardware/'),
    ('knowledge/Academic/',   'knowledge/Research/'),
    ('knowledge/AI/',         'knowledge/Dev/'),
    ('knowledge/Design/',     'knowledge/Hardware/'),
]
from collections import Counter
hit_counter = Counter()
hit_files = {}
for f in files:
    try:
        text = f.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    for old, new in patterns:
        if old in text:
            cnt = text.count(old)
            hit_counter[old] += cnt
            hit_files.setdefault(old, set()).add(str(f.relative_to(root)))
for old, new in patterns:
    print(f"  {old!r} → {new!r}: {hit_counter.get(old,0)} 处, 涉及 {len(hit_files.get(old,set()))} 文件")
    for fn in sorted(hit_files.get(old,set()))[:6]:
        print(f"      {fn}")

# ========== 4. MOC-Academic 内容（用于合并到 MOC-Research）==========
print("\n=== 4. MOC-Academic.md 内容 ===")
try:
    ma = (root/'knowledge/Academic/MOC-Academic.md').read_text(encoding='utf-8', errors='ignore')
    print(ma[:2000])
except Exception as e:
    print(f"  ERR {e}")

# ========== 5. HOME / INDEX / knowledge-map 引用 MOC-Academic/AI/Design 的地方 ==========
print("\n=== 5. 索引文件引用旧 MOC ===")
for name in ['HOME.md', 'INDEX.md', 'knowledge/knowledge-map.md']:
    p = root/name
    if p.exists():
        text = p.read_text(encoding='utf-8', errors='ignore')
        for m in ['MOC-Academic', 'MOC-AI', 'MOC-Design', 'Academic', 'AI/', 'Design']:
            if m in text:
                lines = [l.strip() for l in text.splitlines() if m in l]
                print(f"  {name}: 含 {m!r} → {lines[:3]}")

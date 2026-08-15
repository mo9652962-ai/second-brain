#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vault 分支整合执行脚本：knowledge 三组合并 + dreaming 压平 + 引用修复 + MOC 合并。"""
import pathlib, re, sys, subprocess

root = pathlib.Path(r'C:\Users\31954\.openclaw\workspace')
APPLY = '--apply' in sys.argv
if not APPLY:
    print("[DRY-RUN] 仅打印计划，不执行。加 --apply 执行。")
    sys.exit(0)

def sh(*args):
    """git 命令，参数列表形式（无 shell，安全处理中文/空格文件名）"""
    r = subprocess.run(list(args), capture_output=True, text=True, cwd=str(root))
    if r.returncode != 0:
        print(f"  ⚠️ {' '.join(args)}: {r.stderr.strip()[:200]}")
    return r

# ========== 1. knowledge 三组合并（git mv） ==========
print("=== 1. knowledge 合并 ===")
merges = [
    ('knowledge/Academic', 'knowledge/Research', ['MOC-Academic.md']),
    ('knowledge/AI',       'knowledge/Dev',      ['MOC-AI.md']),
    ('knowledge/Design',   'knowledge/Hardware', ['MOC-Design.md']),
]
for src, dst, keep in merges:
    sd, dd = root/src, root/dst
    if not sd.is_dir():
        continue
    moved = 0
    for f in sorted(sd.iterdir()):
        if f.name in keep:
            continue
        target = dd/f.name
        sh('git', 'mv', str(root/src/f.name), str(root/dst/f.name))
        moved += 1
    # 删除空目录（剩 MOC 文件则先不管，后面 git rm）
    remaining = list(sd.iterdir())
    print(f"  {src} → {dst}: 迁移 {moved} 篇, 剩余 {[f.name for f in remaining]}")

# ========== 2. dreaming 压平 ==========
print("\n=== 2. dreaming 压平 ===")
dr = root/'memory'/'dreaming'
moved = 0
for sub in ['light', 'rem', 'deep']:
    sd = dr/sub
    if not sd.is_dir():
        continue
    for f in sorted(sd.iterdir()):
        new_name = f'{sub}-{f.name}'
        sh('git', 'mv', str(root/f'memory/dreaming/{sub}/{f.name}'), str(root/f'memory/dreaming/{new_name}'))
        moved += 1
print(f"  压平 {moved} 个文件")

# ========== 3. 全仓引用替换（二进制读写，防 CRLF 污染） ==========
print("\n=== 3. 引用替换 ===")
SKIP = {'.git','.obsidian','.venv','__pycache__','site','skills','graphify-out','outputs','mcp','scripts','templates','pipelines','traces','docs','playbooks','system','.claude','.clawhub','.codebuddy','.gemini','.qoder','.skillkit','.hermes','.learnings','.temp','.github','.temp'}
repls = [
    (b'knowledge/Academic/', b'knowledge/Research/'),
    (b'knowledge/AI/',       b'knowledge/Dev/'),
    (b'knowledge/Design/',   b'knowledge/Hardware/'),
    (b'memory/dreaming/light/', b'memory/dreaming/light-'),
    (b'memory/dreaming/rem/',   b'memory/dreaming/rem-'),
    (b'memory/dreaming/deep/',  b'memory/dreaming/deep-'),
    # MOC 引用统一改向（MOC-Academic→Research, MOC-AI→Dev, MOC-Design→Hardware）
    (b'MOC-Academic', b'MOC-Research'),
    (b'MOC-AI',       b'MOC-Dev'),
    (b'MOC-Design',   b'MOC-Hardware'),
]
files = [f for f in root.rglob('*.md') if not any(p in SKIP for p in f.parts)]
total = 0
for f in files:
    try:
        data = f.read_bytes()
    except Exception:
        continue
    orig = data
    for old, new in repls:
        data = data.replace(old, new)
    if data != orig:
        f.write_bytes(data)
        total += 1
print(f"  更新 {total} 个文件")

# ========== 4. MOC 合并 ==========
print("\n=== 4. MOC 合并 ===")
def extract_body(path):
    """去掉 frontmatter 返回正文 bytes。"""
    data = path.read_bytes()
    m = re.match(rb'^---\r?\n(.*?)\r?\n---\r?\n', data, re.S)
    return data[m.end():] if m else data

moc_merges = [
    ('knowledge/Academic/MOC-Academic.md', 'knowledge/Research/MOC-Research.md', '## 🎓 学术域（原 Academic）'),
    ('knowledge/AI/MOC-AI.md',             'knowledge/Dev/MOC-Dev.md',            '## 🤖 AI 域（原 AI）'),
    ('knowledge/Design/MOC-Design.md',     'knowledge/Hardware/MOC-Hardware.md',  '## 🎨 设计域（原 Design）'),
]
for src, dst, header in moc_merges:
    sp, dp = root/src, root/dst
    if sp.exists() and dp.exists():
        body = extract_body(sp)
        new_section = b'\n\n---\n\n' + header.encode() + b'\n\n' + body.strip() + b'\n'
        dp.write_bytes(dp.read_bytes().rstrip() + new_section)
        sh('git', 'rm', str(root/src))
        print(f"  {src} 内容并入 {dst}, 原文件已删除")
    elif sp.exists():
        print(f"  ⚠️ {dst} 不存在，跳过 {src}")
    else:
        print(f"  [skip] {src} 不存在")

# ========== 5. 删除空目录 ==========
print("\n=== 5. 清理空目录 ===")
for d in ['knowledge/Academic', 'knowledge/AI', 'knowledge/Design',
          'memory/dreaming/light', 'memory/dreaming/rem', 'memory/dreaming/deep']:
    p = root/d
    if p.exists():
        try:
            p.rmdir()
            print(f"  删除空目录 {d}")
        except OSError as e:
            print(f"  {d} 非空: {e}")

print("\n✅ 迁移完成。接下来验证。")

"""生成 memory/MOC-Memory.md —— memory 日记系统导航索引（幂等）
按 月目录 / dreaming 分类 / 顶层文件 分组，全路径 wikilink。
"""
import pathlib, re

ROOT = pathlib.Path('memory')
OUT = ROOT / 'MOC-Memory.md'

def link(p):
    """规范 wikilink：全路径、去 .md 后缀（与 MOC-Inbox 风格一致）"""
    return f'[[{p.as_posix()[:-3]}]]'

def md_files(d):
    return sorted([p for p in d.rglob('*.md') if 'MOC-Memory' not in p.name])

lines = []
lines.append('---')
lines.append('title: MOC-Memory')
lines.append('aliases: [Memory, 记忆索引, 日记索引]')
lines.append('type: moc')
lines.append('domain: META')
lines.append('status: active')
lines.append('created: 2026-09-21')
lines.append('updated: 2026-09-21')
lines.append('tags: [meta/moc, memory, knowledge/governance]')
lines.append('---')
lines.append('')
lines.append('# 🧠 Memory 索引')
lines.append('')
lines.append('> memory/ 是 sora 与 k 的日常记录系统：日记、日报、周报、reflection、dreaming 梦境日志。')
lines.append('> 本页是唯一入口，按「年/月 + 类型」组织。自动生成脚本：`scripts/gen-memory-moc.py`。')
lines.append('')

# 顶层 md（不含子目录）
top = [p for p in sorted(ROOT.glob('*.md')) if 'MOC-Memory' not in p.name]
if top:
    lines.append('## 📂 顶层')
    lines.append('')
    for p in top:
        lines.append(f'- {link(p)}')
    lines.append('')

# 年/月
for year in sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name.isdigit()]):
    lines.append(f'## 📅 {year}')
    lines.append('')
    for month in sorted([d for d in year.iterdir() if d.is_dir()]):
        files = md_files(month)
        lines.append(f'### {year}-{month.name}（{len(files)} 篇）')
        lines.append('')
        for p in files:
            lines.append(f'- {link(p)}')
        lines.append('')

# dreaming 顶层散文件
dream_root = ROOT / 'dreaming'
dream_files = [p for p in sorted(dream_root.glob('*.md'))]
if dream_files:
    lines.append(f'## 💭 dreaming（散文件 {len(dream_files)} 篇）')
    lines.append('')
    for p in dream_files:
        lines.append(f'- {link(p)}')
    lines.append('')

# dreaming 子分类
for sub in ['light', 'rem', 'deep']:
    d = dream_root / sub
    if d.exists():
        files = md_files(d)
        if files:
            lines.append(f'### dreaming/{sub}（{len(files)} 篇）')
            lines.append('')
            for p in files:
                lines.append(f'- {link(p)}')
            lines.append('')

# .archive（点目录：Obsidian 默认隐藏，归档内容经文件系统/备份访问，不生成 wikilink 避免断链误报）
arch = ROOT / '.archive'
if arch.exists():
    files = md_files(arch)
    if files:
        lines.append(f'## 🗄️ .archive（{len(files)} 篇 · 历史归档，Obsidian 隐藏目录）')
        lines.append('')
        lines.append('> 归档页不在图谱中展开（点目录被 Obsidian/vault-structure 跳过）。如需查阅：')
        lines.append('> 在 Obsidian 文件树展开 `memory/.archive/`，或见 git 历史 `git log -- memory/.archive/`。')
        lines.append('')

lines.append('---')
lines.append('> 🗺️ 属于 [[HOME|🏠 Home]] · 记忆系统说明：日记按日沉淀，reflection 按周闭环，dreaming 为离线整理')
lines.append('')
OUT.write_text('\n'.join(lines), encoding='utf-8')
total = len([p for p in ROOT.rglob('*.md') if 'MOC-Memory' not in p.name])
print(f'生成完成: {OUT}  收录 {total} 篇 memory md，{len(lines)} 行')

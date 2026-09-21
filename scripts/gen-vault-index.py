"""gen-vault-index.py — 生成 knowledge/VAULT-MAP.md（机器可读索引）+ knowledge/DASHBOARD.md（健康仪表盘）
借鉴：arkan/obsidian-vault-template 的 vault-map.md（机器可读静态索引）+ ibrahimkobeissy dashboard.md（健康指挥中心）
幂等：直接覆盖输出文件，无状态副作用。
"""
import os, re, json, pathlib
from collections import Counter, defaultdict
from datetime import datetime, timedelta

WS = pathlib.Path(__file__).resolve().parent.parent
os.chdir(WS)

IGNORE_DIRS = {'.git', '.obsidian', 'node_modules', '.hermes', '.venv', '.pytest_cache'}
SCAN_DIRS = ['knowledge', 'memory', 'skills', 'concepts', 'docs', 'projects']

# ---------- 收集 ----------
all_md = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and (d == '.archive' or not d.startswith('.'))]
    for f in files:
        if f.endswith('.md'):
            all_md.append(pathlib.Path(root) / f)

def top_dir(p):
    parts = str(p).replace('\\', '/').lstrip('./').split('/')
    return parts[0] if parts else '.'

by_top = Counter(top_dir(p) for p in all_md)
now = datetime.now()

# ---------- 断链/孤立（复用 vault-structure 口径的轻量版） ----------
name_set = {p.stem.lower() for p in all_md}
broken = []
orphan = []
incoming = set()
for p in all_md:
    try:
        txt = p.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    for m in re.finditer(r'\[\[([^\]|#]+)', txt):
        t = m.group(1).replace('\\|', '|').split('|')[0].strip()
        t = re.sub(r'^(\.\./)+', '', t).replace('\\', '/').rstrip('/')
        if t.endswith('.md'):
            t = t[:-3]
        base = os.path.basename(t).lower()
        if base in name_set:
            incoming.add(str(p).replace('\\', '/'))
        else:
            broken.append((str(p).replace('\\', '/'), t))

for p in all_md:
    sp = str(p).replace('\\', '/')
    if sp not in incoming and p.name not in ('README.md', 'LICENSE', 'HOME.md', 'SOUL.md'):
        orphan.append(sp)

# 知识域（knowledge/ 下）统计
know = [p for p in all_md if top_dir(p) == 'knowledge']
by_domain = Counter(str(p.parent).replace('\\', '/').replace('knowledge/', '', 1).split('/')[0] for p in know)

# 最近更新（7 天 / 30 天）
recent7 = [p for p in all_md if (now - datetime.fromtimestamp(p.stat().st_mtime)) <= timedelta(days=7)]
recent30 = [p for p in all_md if (now - datetime.fromtimestamp(p.stat().st_mtime)) <= timedelta(days=30)]

# MOC 清单（只列 knowledge/ 域内真实存在的，全路径链接避免子目录歧义）
mocs = sorted(p for p in all_md if top_dir(p) == 'knowledge' and p.stem.startswith('MOC-'))
home_anchors = sorted(p.stem for p in all_md if top_dir(p) == 'knowledge' and p.stem in ('knowledge-map', 'index', 'log'))

# ---------- VAULT-MAP.md ----------
L = []
L.append('---')
L.append('title: VAULT-MAP')
L.append('aliases: [VaultMap, 机器索引, vault-map]')
L.append('type: meta')
L.append('domain: META')
L.append('status: active')
L.append(f'created: {now.date().isoformat()}')
L.append(f'updated: {now.date().isoformat()}')
L.append('tags: [meta/index, knowledge/governance, ai/navigation]')
L.append('---')
L.append('')
L.append('# 🗺️ VAULT-MAP — 机器可读索引')
L.append('')
L.append(f'> 自动生成：`scripts/gen-vault-index.py`（{now.strftime("%Y-%m-%d")}）。')
L.append('> 给 AI Agent 用的静态导航索引：不用全盘扫描即可定位内容。人类入口见 [[knowledge-map]] 与 [[HOME]]。')
L.append('')
L.append('## 顶层分布')
L.append('')
L.append('| 顶层 | md 数 |')
L.append('|:---|---:|')
for d, n in sorted(by_top.items(), key=lambda x: -x[1]):
    L.append(f'| `{d}/` | {n} |')
L.append('')
L.append('## 知识域分布（knowledge/）')
L.append('')
L.append('| 域 | 笔记数 |')
L.append('|:---|---:|')
for d, n in sorted(by_domain.items(), key=lambda x: -x[1]):
    L.append(f'| {d} | {n} |')
L.append('')
L.append('## MOC 锚点')
L.append('')
for p in mocs:
    rel = str(p).replace('\\', '/').lstrip('./')
    L.append(f'- [[{rel[:-3]}]]')
L.append('')
L.append('## 导航规则')
L.append('')
L.append('- 知识笔记 → `knowledge/<域>/`；领域总览 → 对应 `MOC-*`')
L.append('- 记忆/日记/反思 → `memory/`（入口 MOC-Memory，见 memory 目录）')
L.append('- 可执行技能 → `skills/`；项目产物 → `projects/`、`outputs/`')
L.append('- 回答前先读 [[knowledge-map]]（人类地图）与本页（机器地图）')
L.append('')
(WS / 'knowledge' / 'VAULT-MAP.md').write_text('\n'.join(L), encoding='utf-8', newline='\n')

# ---------- DASHBOARD.md ----------
D = []
D.append('---')
D.append('title: DASHBOARD')
D.append('aliases: [Dashboard, 健康看板]')
D.append('type: meta')
D.append('domain: META')
D.append('status: active')
D.append(f'created: {now.date().isoformat()}')
D.append(f'updated: {now.date().isoformat()}')
D.append('tags: [meta/dashboard, knowledge/governance, health]')
D.append('---')
D.append('')
D.append('# 📊 DASHBOARD — 知识库健康看板')
D.append('')
D.append(f'> 自动生成：`scripts/gen-vault-index.py`（{now.strftime("%Y-%m-%d")}）。详细报告：`scripts/vault-audit-report.json`（CI 周一产物）。')
D.append('')
D.append('## 关键指标')
D.append('')
D.append(f'- **总 md 文件**：{len(all_md)}')
D.append(f'- **知识域笔记**：{len(know)}（18 域中的 {len(by_domain)} 域有内容）')
D.append(f'- **断裂链接**：{len(broken)}')
D.append(f'- **孤立页面**：{len(orphan)}')
D.append(f'- **MOC 锚点**：{len(mocs)}')
D.append(f'- **7 天更新**：{len(recent7)} 篇 · **30 天更新**：{len(recent30)} 篇')
D.append('')
if broken:
    D.append('## ⚠️ 断链 TOP10')
    D.append('')
    D.append('| 来源 | 目标 |')
    D.append('|:---|---|')
    for src, tgt in broken[:10]:
        D.append(f'| `{src}` | `{tgt}` |')
    D.append('')
if orphan:
    D.append('## 📄 孤立页 TOP10（挂载到 MOC 可消除）')
    D.append('')
    for o in orphan[:10]:
        D.append(f'- `{o}`')
    D.append('')
D.append('## 近 30 天活跃域')
D.append('')
recent_by = Counter(top_dir(p) for p in recent30)
D.append('| 顶层 | 30 天更新 |')
D.append('|:---|---:|')
for d, n in sorted(recent_by.items(), key=lambda x: -x[1])[:8]:
    D.append(f'| `{d}/` | {n} |')
D.append('')
D.append('> 🗺️ 属于 [[HOME|🏠 Home]] · 维护：每周一 CI 全量健康检查 + 每日 auto-sync')
D.append('')
(WS / 'knowledge' / 'DASHBOARD.md').write_text('\n'.join(D), encoding='utf-8', newline='\n')

print(f'✅ VAULT-MAP.md ({len(L)} 行) + DASHBOARD.md ({len(D)} 行)')
print(f'   断链 {len(broken)} · 孤立 {len(orphan)} · MOC {len(mocs)} · 7天更新 {len(recent7)}')

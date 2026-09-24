#!/usr/bin/env python3
"""OKM (Open Knowledge Metabolism) 知识新陈代谢分析与自愈引擎。
借鉴 Karpathy LLM Wiki 模式与 eugeniughelbur/obsidian-second-brain 架构：
- 评估卡片成熟度：🌱 Seed (萌芽) / 🌿 Budding (成长) / 🌲 Evergreen (常青) / 📦 Superseded (降级)
- 检测过期与矛盾指针 (superseded_by)
- 产出 knowledge/METABOLISM.md 代谢健康看板
"""

import os
import re
import base64
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = ROOT / 'knowledge'
METABOLISM_MD = KNOWLEDGE_DIR / 'METABOLISM.md'

_OBFUSCATED = [
    '5qGC6Iiq', '5qGC5p6X6Iiq5aSp5bel5Lia5a2m6Zmi', '6Iiq56m65a6H6Iiq5a2m6Zmi',
    '6aOe6KGM5Zmo6LSo6YeP5LiO5Y+v6Z2g5oCn', 'Z3VhdFwuZWR1XC5jbg==',
    '5qGC55S1', '5qGC5p6X55S15a2Q56eR5oqA5aSn5a2m', 'MDgwNDAw',
    '6ICD56CU6ICD6K+B6Lev57q/5Zu+', '6ICD56CU6KeE5YiS', '6ICD56CU55uu5qCH',
    'MzE5NTQ='
]

def load_privacy_patterns() -> list[str]:
    patterns = []
    pats_file = ROOT / 'scripts' / 'private-patterns.txt'
    if pats_file.is_file():
        for line in pats_file.read_text(encoding='utf-8', errors='ignore').splitlines():
            l = line.strip()
            if l and not l.startswith('#'):
                patterns.append(re.escape(l))
    else:
        for b in _OBFUSCATED:
            try:
                dec = base64.b64decode(b).decode('utf-8')
                patterns.append(dec if '\\' in dec else re.escape(dec))
            except Exception:
                pass
    return patterns

PRIVACY_REGEX = re.compile('|'.join(load_privacy_patterns()), re.IGNORECASE)

def is_safe(text: str) -> bool:
    return not bool(PRIVACY_REGEX.search(text))

def get_tracked_md_files() -> list[str]:
    res = subprocess.run(
        ['git', '-c', 'core.quotePath=false', 'ls-files', 'knowledge/*.md', 'skills/*.md'],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    if res.returncode != 0:
        return []
    return [l.strip() for l in res.stdout.splitlines() if l.strip()]

def analyze_vault() -> dict:
    tracked = get_tracked_md_files()
    
    inlinks_map: dict[str, set[str]] = {}
    outlinks_map: dict[str, set[str]] = {}
    note_details: dict[str, dict] = {}
    
    for f in tracked:
        p = ROOT / f
        if not p.is_file():
            continue
        try:
            content = p.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            continue
            
        if not is_safe(content):
            continue
            
        stem = p.stem.lower()
        links = re.findall(r'\[\[([^\]|#]+)', content)
        clean_links = {l.strip().split('/')[-1].lower() for l in links if l.strip()}
        outlinks_map[stem] = clean_links
        
        for tgt in clean_links:
            inlinks_map.setdefault(tgt, set()).add(stem)
            
        status = 'active'
        superseded_by = None
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm = parts[1]
                for l in fm.splitlines():
                    if l.startswith('status:'):
                        status = l.split(':', 1)[1].strip().strip('\'"')
                    elif l.startswith('superseded_by:'):
                        superseded_by = l.split(':', 1)[1].strip().strip('\'"')

        char_len = len(content)
        note_details[stem] = {
            'path': f,
            'title': p.stem,
            'char_len': char_len,
            'status': status,
            'superseded_by': superseded_by,
            'out_count': len(clean_links)
        }

    seeds = []
    buddings = []
    evergreens = []
    superseded = []

    for stem, meta in note_details.items():
        in_count = len(inlinks_map.get(stem, set()))
        meta['in_count'] = in_count
        
        if meta['status'] in ['archived', 'deprecated', 'superseded'] or meta['superseded_by']:
            superseded.append(meta)
        elif meta['char_len'] > 600 and in_count >= 2 and meta['out_count'] >= 2:
            evergreens.append(meta)
        elif meta['char_len'] > 200 or in_count >= 1:
            buddings.append(meta)
        else:
            seeds.append(meta)

    return {
        'total': len(note_details),
        'evergreens': evergreens,
        'buddings': buddings,
        'seeds': seeds,
        'superseded': superseded,
    }

def generate_report(data: dict):
    now_str = datetime.now().strftime('%Y-%m-%d')
    total = data['total']
    eg_cnt = len(data['evergreens'])
    bd_cnt = len(data['buddings'])
    sd_cnt = len(data['seeds'])
    sp_cnt = len(data['superseded'])

    eg_pct = round(eg_cnt / max(1, total) * 100, 1)
    bd_pct = round(bd_cnt / max(1, total) * 100, 1)
    sd_pct = round(sd_cnt / max(1, total) * 100, 1)

    lines = [
        '---',
        'title: METABOLISM',
        'aliases: [知识新陈代谢看板, OKM Dashboard]',
        'type: meta',
        'domain: META',
        'status: active',
        f'created: {now_str}',
        f'updated: {now_str}',
        'tags: [meta/metabolism, okm, knowledge/governance]',
        '---',
        '',
        '# 🌿 OKM — 开放知识新陈代谢看板 (Open Knowledge Metabolism)',
        '',
        '> 启发自 Karpathy 的 LLM Wiki 理念与现代化第二大脑自愈架构。',
        '> 知识库不是只增不减（Append-only）的死仓库，而是一座具有自我代谢、蒸馏、进化与淘汰能力的活体知识生态。',
        '',
        '## 📊 认知成熟度分布 (Maturity Funnel)',
        '',
        f'- **全库受管笔记**：{total} 篇',
        f'- 🌲 **Evergreen (常青/方法论)**：**{eg_cnt}** 篇 ({eg_pct}%) — 结构完备、双向链接闭环、实战沉淀的成熟知识',
        f'- 🌿 **Budding (成长/求证中)**：**{bd_cnt}** 篇 ({bd_pct}%) — 包含基本推演与领域上下文的进阶笔记',
        f'- 🌱 **Seed (萌芽/原子速记)**：**{sd_cnt}** 篇 ({sd_pct}%) — 初步捕获的原始事实、想法或灵感种子',
        f'- 📦 **Superseded (降级/过时归档)**：**{sp_cnt}** 篇 — 已被新技术、新决策替代，或标记为历史归档',
        '',
        '## 🔄 代谢进化法则 (The 4 Laws of OKM)',
        '',
        '1. **更新胜于追加 (Update beats Append)**：新事实输入时，优先定位已有卡片并增量更新，而非盲目新建同名碎笔记。',
        '2. **矛盾显式标注 (Resolve Contradictions)**：遇到与旧认知冲突时，不抹除旧结论，而是使用 `superseded_by: [[新笔记]]` 留下演进轨迹。',
        '3. **常青卡片提炼 (Compounding to Evergreen)**：多篇 Seed 笔记交叉印证后，由 Agent 或人工合并提炼为领域 MOC 或实战 Skill。',
        '4. **定期无损剪枝 (Zero-Waste Pruning)**：定期淘汰无入链、无语义价值的琐碎卡片，保持图谱网络的高信号密度。',
        '',
        '## 🌲 TOP Evergreen 代表性常青知识 (高连接核心节点)',
        '',
        '| 笔记名 | 领域路径 | 入链数 | 出链数 | 字符体量 |',
        '|:---|:---|:---:|:---:|:---:|'
    ]

    sorted_eg = sorted(data['evergreens'], key=lambda x: x['in_count'], reverse=True)[:15]
    for it in sorted_eg:
        lines.append(f"| [[{it['title']}]] | `{it['path']}` | {it['in_count']} | {it['out_count']} | {it['char_len']} |")

    lines.append('')
    lines.append('---')
    lines.append(f'*由 scripts/okm_metabolism.py 自动生成于 {now_str} · 保障第二大脑持久自愈与抗熵增*')

    METABOLISM_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='')
    print(f'Generated {METABOLISM_MD} successfully. Total: {total}, Evergreen: {eg_cnt}, Budding: {bd_cnt}, Seed: {sd_cnt}')

def main():
    data = analyze_vault()
    generate_report(data)

if __name__ == '__main__':
    main()

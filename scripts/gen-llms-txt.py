#!/usr/bin/env python3
"""生成符合 llmstxt.org 标准的 /llms.txt 与 /llms-full.txt 索引文件。
遵循 AI-First 与 GEO（Generative Engine Optimization）原则，严格过滤隐私红线。
"""

import os
import re
import base64
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 敏感特征从外部词表加载；若词表不存在，使用 base64 混淆的兜底列表，避免脚本源码自身出现敏感字面量
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
    patterns.append(r'1[3-9]\d{9}')
    patterns.append(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    return patterns

PRIVACY_REGEX = re.compile('|'.join(load_privacy_patterns()), re.IGNORECASE)

def is_safe(text: str) -> bool:
    return not bool(PRIVACY_REGEX.search(text))

def get_tracked_md_files() -> list[str]:
    res = subprocess.run(
        ['git', '-c', 'core.quotePath=false', 'ls-files', '*.md'],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    if res.returncode != 0:
        return []
    lines = [line.strip() for line in res.stdout.splitlines() if line.strip()]
    return lines

def extract_meta(md_path: Path) -> dict:
    try:
        content = md_path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return {}
    
    if not is_safe(content):
        return {}

    title = md_path.stem
    desc = ''
    domain = ''
    
    # 提取 YAML frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm = parts[1]
            for line in fm.splitlines():
                if line.startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('\'"')
                elif line.startswith('description:'):
                    desc = line.split(':', 1)[1].strip().strip('\'"')
                elif line.startswith('domain:'):
                    domain = line.split(':', 1)[1].strip().strip('\'"')

    if not desc:
        # 取前三行正文
        body = content.split('---', 2)[-1] if content.startswith('---') else content
        clean_lines = [l.strip().lstrip('#').strip() for l in body.splitlines() if l.strip() and not l.strip().startswith('>') and not l.strip().startswith('!')]
        if clean_lines:
            desc = clean_lines[0][:120]

    return {
        'title': title,
        'description': desc,
        'domain': domain,
        'path': str(md_path.relative_to(ROOT)).replace('\\', '/')
    }

def main():
    tracked = get_tracked_md_files()
    print(f'Tracked MD files: {len(tracked)}')

    entries = []
    for f in tracked:
        p = ROOT / f
        if not p.is_file():
            continue
        meta = extract_meta(p)
        if meta and is_safe(meta['title']) and is_safe(meta['description']):
            entries.append(meta)

    print(f'Safe indexable entries: {len(entries)}')

    # 1. 生成精简 /llms.txt (符合 llmstxt.org 规范)
    # 2026-09-25 修复：篇数改为动态统计（旧版硬编码「1,000+」，实际 tracked 767 篇 → 长期失真）
    llms_txt = [
        '# Second Brain — AI Agent 第二大脑',
        '',
        '> 一个具备自进化能力的开源第二大脑与知识图谱系统。',
        f'> 整合 {len(tracked)} 篇公开知识体系、18 知识域全景拓扑与 7 大自举进化闭环。',
        '',
        '## 知识库概览',
        '- 官网与 3D 拓扑探针: https://mo9652962-ai.github.io/second-brain/',
        '- 在线知识库 (MkDocs): https://mo9652962-ai.github.io/second-brain/kb/',
        '- 机器可读图谱清单: https://mo9652962-ai.github.io/second-brain/kb/knowledge/VAULT-MAP/',
        '',
        '## 核心知识域与重点索引 (Core Knowledge Domains)',
        ''
    ]

    # 按 domain 或顶层目录归类
    by_category: dict[str, list[dict]] = {}
    for e in entries:
        cat = e['domain']
        if not cat:
            parts = e['path'].split('/')
            cat = parts[1] if parts[0] == 'knowledge' and len(parts) > 1 else parts[0]
        by_category.setdefault(cat, []).append(e)

    for cat, items in sorted(by_category.items()):
        if len(items) < 2:
            continue
        llms_txt.append(f'### {cat.upper()} ({len(items)} 篇)')
        top_items = [i for i in items if 'MOC' in i['title'] or 'README' in i['title'] or 'INDEX' in i['title']]
        rest_items = [i for i in items if i not in top_items]
        selected = (top_items + rest_items)[:8]
        for it in selected:
            clean_desc = f': {it["description"]}' if it["description"] else ''
            llms_txt.append(f'- [{it["title"]}](https://mo9652962-ai.github.io/second-brain/kb/{it["path"].replace(".md", "")}/){clean_desc}')
        llms_txt.append('')

    llms_txt.append('## 规范与使用指南')
    llms_txt.append('- 完整知识平铺导出 (Full Flat Dump): https://mo9652962-ai.github.io/second-brain/llms-full.txt')
    llms_txt.append('- 遵循 llmstxt.org 协议，供 Claude Code、Cursor、OpenCode、Hermes 等 AI Agent 高效检索与推理。')

    llms_txt_content = '\n'.join(llms_txt) + '\n'

    # 输出到根目录与 docs-site
    (ROOT / 'llms.txt').write_text(llms_txt_content, encoding='utf-8', newline='')
    (ROOT / 'docs-site' / 'llms.txt').write_text(llms_txt_content, encoding='utf-8', newline='')
    print('Generated llms.txt successfully (Root & docs-site/)')

    # 2. 生成 /llms-full.txt (精选知识平铺，限制在 3MB 以内)
    llms_full = [
        '# Second Brain — Full Knowledge Context Dump',
        '> Generated per llmstxt.org specification for AI Agent ingestion.',
        '=' * 60,
        ''
    ]
    cur_bytes = 0
    max_bytes = 2 * 1024 * 1024 # 2MB cap
    
    # 优先抽取 HOME、INDEX、MOC 与 skills/hermes
    priority_files = [f for f in tracked if any(k in f for k in ['HOME.md', 'INDEX.md', 'MOC-', 'skills/hermes/'])]
    for pf in priority_files:
        p = ROOT / pf
        if not p.is_file():
            continue
        txt = p.read_text(encoding='utf-8', errors='ignore')
        if not is_safe(txt):
            continue
        chunk = f'\n\n## FILE: {pf}\n' + '=' * 40 + '\n' + txt
        llms_full.append(chunk)
        cur_bytes += len(chunk.encode('utf-8'))
        if cur_bytes > max_bytes:
            break

    llms_full_content = '\n'.join(llms_full) + '\n'
    (ROOT / 'llms-full.txt').write_text(llms_full_content, encoding='utf-8', newline='')
    (ROOT / 'docs-site' / 'llms-full.txt').write_text(llms_full_content, encoding='utf-8', newline='')
    print(f'Generated llms-full.txt successfully ({cur_bytes // 1024} KB)')

if __name__ == '__main__':
    main()

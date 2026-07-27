"""vault-structure.py — Obsidian vault 结构健康检查
检查: 断裂wikilinks, 孤立文件, 空文件, 标签不一致, frontmatter缺失, 大文件
"""
import os, re, sys, json
from collections import defaultdict, Counter
from datetime import datetime

VAULT = r"C:\Users\31954\.openclaw\workspace"
os.chdir(VAULT)

IGNORE_DIRS = {'.git', '.obsidian', 'node_modules', '.hermes', 'scripts', 'templates'}
SCAN_DIRS = {'knowledge', 'memory', '.'}  # 根目录的单个文件也扫

results = {
    'broken_links': [],
    'orphan_files': [],
    'empty_notes': [],
    'tag_inconsistencies': [],
    'large_files': [],
    'frontmatter_issues': [],
    'file_stats': {'total': 0, 'md': 0, 'size_total': 0},
}

# Step 1: 收集所有 .md 文件
all_notes = {}  # path -> content lines
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d.split('/')[-1].split('\\')[-1] not in IGNORE_DIRS and not d.startswith('.') and d != '_community']
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        results['file_stats']['total'] += 1
        results['file_stats']['md'] += 1
        try:
            sz = os.path.getsize(path)
            results['file_stats']['size_total'] += sz
            with open(path, 'r', encoding='utf-8', errors='replace') as fh:
                lines = fh.readlines()
            all_notes[path] = lines
            
            # 空文件检查
            content = ''.join(lines).strip()
            if not content:
                results['empty_notes'].append(path)
            elif re.match(r'^---\s*---\s*$', content.strip()):
                results['empty_notes'].append(f"{path} (仅有空frontmatter)")
        except:
            pass

print(f"📊 全景: {results['file_stats']['md']} 个 .md 文件, {results['file_stats']['size_total']/1024:.0f} KB")

# Step 2: 检查断裂 wikilinks
notes_set = set(all_notes.keys())
notes_set_norm = {os.path.normcase(p): p for p in notes_set}
note_names = {os.path.splitext(os.path.basename(p))[0]: p for p in notes_set}

for path, lines in all_notes.items():
    for lineno, line in enumerate(lines, 1):
        for m in re.finditer(r'\[\[([^\]]+)\]\]', line):
            target = m.group(1).split('|')[0].split('#')[0]
            if not target:
                continue
            # 标准化路径
            target_norm = target.replace('/', os.sep).replace('\\', os.sep)
            target_file = None
            for p in all_notes:
                base = os.path.splitext(p)[0].lstrip('.\\').lstrip('./')
                name_only = os.path.basename(base)
                if target_norm == base or target_norm == name_only:
                    target_file = True
                    break
            if not target_file:
                results['broken_links'].append(f"{path}:{lineno} → {target}")

# Step 3: 检查孤立文件
has_incoming = set()
link_pattern = re.compile(r'\[\[([^\]]+)\]\]')
for path, lines in all_notes.items():
    for line in lines:
        for m in link_pattern.finditer(line):
            target = m.group(1).split('|')[0].split('#')[0]
            for p in all_notes:
                if target in os.path.normpath(p):
                    has_incoming.add(p)
                    break

for path in all_notes:
    if path not in has_incoming and os.path.dirname(path) != '.':
        # 排除根目录文件和 README/LICENSE/HOME
        basename = os.path.basename(path)
        if basename not in ('README.md', 'LICENSE', 'HOME.md', 'SOUL.md'):
            results['orphan_files'].append(path)

# Step 4: 检查标签一致性
tag_counts = Counter()
tag_files = defaultdict(list)
for path, lines in all_notes.items():
    fm_tags = None
    in_fm = False
    fm_lines = []
    for line in lines:
        if line.strip() == '---':
            if not in_fm:
                in_fm = True
                continue
            else:
                break
        if in_fm:
            fm_lines.append(line)
    for l in fm_lines:
        m = re.match(r'tags?\s*:\s*\[?(.+?)\]?\s*$', l.strip())
        if m:
            tags_str = m.group(1)
            tags = [t.strip().strip("'\"") for t in tags_str.replace('[','').replace(']','').split(',')]
            for t in tags:
                if t:
                    tag_counts[t] += 1
                    tag_files[t].append(path)

# 找出低频标签（使用<2次）
for tag, count in tag_counts.most_common():
    if count <= 1:
        results['tag_inconsistencies'].append(f"低频标签 '{tag}': 仅使用{count}次 — 文件: {tag_files[tag][0]}")

# Step 5: 大文件检查
for path in all_notes:
    sz = os.path.getsize(path)
    if sz > 50000:  # >50KB
        results['large_files'].append(f"{path} ({sz/1024:.0f} KB)")

# Step 6: frontmatter 检查
for path, lines in all_notes.items():
    if not lines or lines[0].strip() != '---':
        if os.path.basename(path) not in ('README.md', 'LICENSE'):
            continue  # 部分文件不需要 frontmatter
    else:
        has_title = has_date = has_tags = False
        fm_content = []
        for line in lines[1:]:
            if line.strip() == '---':
                break
            fm_content.append(line)
        for l in fm_content:
            if re.match(r'^title\s*:', l):
                has_title = True
            if re.match(r'^date\s*:', l):
                has_date = True
            if re.match(r'^tags?\s*:', l):
                has_tags = True
        # knowledge 目录下的文件建议有 tags
        if '/knowledge/' in path and not has_tags:
            results['frontmatter_issues'].append(f"{path}: knowledge笔记缺tags")

# ===== 输出报告 =====
print(f"\n{'='*50}")
print(f"🔍 OBSIDIAN 全库审计报告")
print(f"{'='*50}\n")

print(f"📦 文件统计:")
print(f"   总文件: {results['file_stats']['total']}")
print(f"   .md文件: {results['file_stats']['md']}")
print(f"   总大小: {results['file_stats']['size_total']/1024:.0f} KB")

print(f"\n🔗 断裂 wikilinks: {len(results['broken_links'])}")
for bl in results['broken_links'][:10]:
    print(f"   ⚠ {bl}")
if len(results['broken_links']) > 10:
    print(f"   ... 还有 {len(results['broken_links'])-10} 个")

print(f"\n📄 孤立文件 (无入链): {len(results['orphan_files'])}")
for of in results['orphan_files'][:10]:
    print(f"   📄 {of}")
if len(results['orphan_files']) > 10:
    print(f"   ... 还有 {len(results['orphan_files'])-10} 个")

print(f"\n🗑️ 空文件: {len(results['empty_notes'])}")
for ef in results['empty_notes'][:5]:
    print(f"   ⚠ {ef}")

print(f"\n🏷️ 标签使用: {len(tag_counts)} 个唯一标签")
print(f"   高频标签: {tag_counts.most_common(10)}")
print(f"   低频标签(<=1次): {len([t for t,c in tag_counts.items() if c<=1])}")

print(f"\n📏 大文件 (>50KB): {len(results['large_files'])}")
for lf in results['large_files'][:5]:
    print(f"   📏 {lf}")

print(f"\n⚠️ Frontmatter 问题: {len(results['frontmatter_issues'])}")
for fi in results['frontmatter_issues'][:5]:
    print(f"   ⚠ {fi}")

# ===== 导出 JSON =====
report = {
    'date': datetime.now().isoformat(),
    'vault': VAULT,
    'stats': results['file_stats'],
    'broken_links_count': len(results['broken_links']),
    'orphan_files_count': len(results['orphan_files']),
    'empty_notes_count': len(results['empty_notes']),
    'unique_tags': len(tag_counts),
    'large_files_count': len(results['large_files']),
    'issues': {
        'broken_links': results['broken_links'],
        'orphan_files': results['orphan_files'],
        'empty_notes': results['empty_notes'],
        'tag_inconsistencies': results['tag_inconsistencies'][:20],
        'large_files': results['large_files'],
        'frontmatter_issues': results['frontmatter_issues'],
    }
}
with open('scripts/vault-audit-report.json', 'w') as f:
    json.dump(report, f, indent=2, ensure_ascii=False)
print(f"\n📋 完整报告已导出: scripts/vault-audit-report.json")
print(f"\n{'='*50}")

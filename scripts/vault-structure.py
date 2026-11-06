"""vault-structure.py — Obsidian vault 结构健康检查
检查: 断裂wikilinks, 孤立文件, 空文件, 标签不一致, frontmatter缺失, 大文件
"""
import os, re, sys, json
from collections import defaultdict, Counter
from datetime import datetime

VAULT = os.environ.get('VAULT_PATH', r"%USERPROFILE%\.openclaw\workspace")
if not os.path.exists(VAULT):
    VAULT = os.getcwd()  # 在 CI 中 fallback 到当前目录
os.chdir(VAULT)

IGNORE_DIRS = {'.git', '.obsidian', 'node_modules', '.hermes', 'scripts'}
# ⚠️ `templates/` 不能进 IGNORE_DIRS：它是**被链接的目标**，排除后 INDEX.md 指向
# 模板的 5 条 wikilink 全被误报断链（2026-09-29 实测）。IGNORE_DIRS 只该排除
# 「永不作为 wikilink 目标」的目录。
SCAN_DIRS = {'knowledge', 'memory', '.'}  # 根目录的单个文件也扫

# ===== 断链判据的假阳性过滤（2026-09-29，与 knowledge-lint.py 权威口径对齐）=====
# 旧实现直接把 [[...]] 当断链 → 三类误报共 33 条（实测真断链 0）：
#   1. 代码区示例：反引号/fence 内展示给用户的模板链接
#   2. 模板占位符：[[wikilink]] [[新笔记]] [[所属MOC]] [[A]] [[B]] 等
#   3. 被 IGNORE/非跟踪目录排除的目标（templates/、skills/@* 第三方技能）
CODE_SPAN_RE = re.compile(r'`[^`]*`')
FENCE_RE = re.compile(r'```.*?```', flags=re.S)
PLACEHOLDER_LINKS = {'name', 'their-name', 'wiki link', 'wikilink', ':space:', 'todo', 'link',
                     'note-1', 'series-2026-08-14', 'skill-name', '新笔记', '所属moc',
                     '页面名', 'a', 'b'}


def _strip_code(text):
    """剥离代码区（行内反引号 + fence），返回与原文行数一致、行号可信的文本。"""
    return FENCE_RE.sub('', CODE_SPAN_RE.sub('', text))


def _gitignored(paths):
    """返回被 .gitignore 忽略的路径集合（git 不可用时返回空集）

    必要性：私有文档（本地保留但被 gitignore）若被扫描，
    若不跳过会把文件名写进公开报告 → 隐私泄露。
    """
    if not paths:
        return set()
    try:
        import subprocess
        # 用 bytes 传输：text=True 在 Windows 会把换行翻成 CRLF，
        # 使 git 回显的路径带尾随 CR，导致比对全部失配。
        proc = subprocess.run(
            # -c core.quotePath=false：否则中文路径被转义成 \346\241... 八进制，无法比对
            ['git', '-c', 'core.quotePath=false', 'check-ignore', '--stdin'],
            input='\n'.join(paths).encode('utf-8'),
            capture_output=True,
        )
        # check-ignore: 命中=0（有忽略项）; 1=无忽略项; 其他=出错
        if proc.returncode in (0, 1):
            out = proc.stdout.decode('utf-8', 'replace')
            return {line.strip().strip('"').strip() for line in out.splitlines() if line.strip()}
    except Exception:
        pass
    return set()


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
_scan_candidates = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d.split('/')[-1].split('\\')[-1] not in IGNORE_DIRS and (d.split('/')[-1].split('\\')[-1] == '.archive' or not d.startswith('.')) and d != '_community']
    for f in files:
        if f.endswith('.md'):
            _scan_candidates.append(os.path.join(root, f))

# 私有文档（gitignore）不纳入扫描 → 避免文件名进入公开报告
# 注意：os.walk('.') 产生 "./knowledge/..." 前缀，git check-ignore 返回无前缀的 "knowledge/..."
def _norm(p):
    return p.replace(os.sep, '/').removeprefix('./')

_ignored = {_norm(x) for x in _gitignored([_norm(p) for p in _scan_candidates])}

for path in _scan_candidates:
    if _norm(path) in _ignored:
        continue
    if True:
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
    # 剥离代码区后再找链接（行数保持一致 → 行号仍可信）
    lines = _strip_code(''.join(lines)).splitlines()
    for lineno, line in enumerate(lines, 1):
        for m in re.finditer(r'\[\[([^\]]+)\]\]', line):
            target = m.group(1).replace('\\|', '|').split('|')[0].split('#')[0]  # \| 转义别名 + 常规别名/锚点
            if not target:
                continue
            # 模板占位符（非真实笔记名）→ 白名单跳过
            if target.strip().lower() in PLACEHOLDER_LINKS:
                continue
            # 标准化路径（统一正斜杠比较：wikilink 文本是正斜杠，Windows normpath 是反斜杠）
            target_norm = re.sub(r'^(\.\./)+', '', target).replace('\\', '/')  # 剥 ../ 相对前缀（Obsidian 解析到 vault 根）
            if target_norm.endswith('.md'):
                target_norm = target_norm[:-3]  # 显式 .md 后缀剥掉（Obsidian 兼容）
            # 第三方技能/非扫描目录（skills/@* 等）不是 vault 内容，跳过
            if target_norm.startswith('skills/@'):
                continue
            target_file = None
            for p in all_notes:
                base = os.path.splitext(p)[0].lstrip('.\\').lstrip('./').replace('\\', '/')
                name_only = os.path.basename(base)
                if target_norm == base or target_norm == name_only:
                    target_file = True
                    break
            # 大小写不敏感兜底（Obsidian 解析 [[Home]]→HOME.md，脚本比较须不敏感）
            if not target_file:
                for p in all_notes:
                    base = os.path.splitext(p)[0].lstrip('.\\').lstrip('./').replace('\\', '/')
                    name_only = os.path.basename(base)
                    if target_norm.lower() == base.lower() or target_norm.lower() == name_only.lower():
                        target_file = True
                        break
            # 扫描范围外的真实文件（如 templates/ 曾被 IGNORE_DIRS 排除）→ 非断链
            if not target_file:
                from pathlib import Path as _P
                _cand = _P(VAULT) / (target_norm + '.md')
                if _cand.is_file() or any(_P(VAULT).rglob(os.path.basename(target_norm) + '.md')):
                    target_file = True
            if not target_file:
                results['broken_links'].append(f"{path}:{lineno} → {target}")

# Step 3: 检查孤立文件
# 2026-09-29：入链统计须同样剥离代码区（否则文档里的示例链接会制造假入链），
# 且只认「目标确实存在」的链接（旧版用子串匹配，任意路径含该串即算入链）。
# 另：markdown 链接 [text](path.md) 也是真实入链——README 就是用这种方式导航
# skills/ 的，只认 wikilink 会把 19 个技能文档全报成孤立（实测）。
has_incoming = set()
link_pattern = re.compile(r'\[\[([^\]]+)\]\]')
md_link_pattern = re.compile(r'\[[^\]]*\]\(([^)]+\.md)(?:#[^)]*)?\)')

for path, lines in all_notes.items():
    stripped = _strip_code(''.join(lines)).splitlines()
    src_dir = os.path.dirname(path)
    for line in stripped:
        # --- wikilink 入链 ---
        for m in link_pattern.finditer(line):
            target = m.group(1).replace('\\|', '|').split('|')[0].split('#')[0]  # \| 转义别名 + 常规别名/锚点
            if target.strip().lower() in PLACEHOLDER_LINKS:
                continue
            target_posix = re.sub(r'^(\.\./)+', '', target).replace('\\', '/')  # 剥 ../ 相对前缀
            if target_posix.endswith('.md'):
                target_posix = target_posix[:-3]  # 显式 .md 后缀剥掉（Obsidian 兼容）
            for p in all_notes:
                norm = os.path.normpath(p).replace('\\', '/')
                if target_posix == os.path.splitext(norm)[0].lstrip('./') or \
                   target_posix == os.path.basename(os.path.splitext(norm)[0]):
                    has_incoming.add(p)
                    break
        # --- markdown 相对链接入链 ---
        for m in md_link_pattern.finditer(line):
            url = m.group(1)
            if url.startswith(('http', 'mailto:')) or '://' in url:
                continue
            resolved = os.path.normpath(os.path.join(src_dir, url.split('#')[0])).replace('\\', '/')
            if resolved in {os.path.normpath(p).replace('\\', '/') for p in all_notes}:
                has_incoming.add(next(p for p in all_notes
                                      if os.path.normpath(p).replace('\\', '/') == resolved))

# 工具/导航类目录不参与孤立判定：它们由 GitHub 界面、README 表格或各自的 MOC
# 导航，从不指望从知识库内部被 wikilink 引用（与 gen-vault-index.py 口径一致）。
ORPHAN_IGNORE_PREFIXES = ('skills/', 'portfolio/', 'scripts/', 'todo/', 'mcp/', 'system/',
                          'pipelines/', 'playbooks/', 'traces/', 'site/', 'outputs/')

for path in all_notes:
    # 跳过条件（注意德摩根展开：原判据是「不在 has_incoming 且不在根目录」才入列，
    # 故跳过条件是「在 has_incoming 或位于根目录」——写成 != '.' 会反向把
    # 所有子目录文件全部排除，孤立恒为 0。2026-09-29 由负向对照夹具抓出）
    if path in has_incoming or os.path.dirname(path) == '.':
        continue
    basename = os.path.basename(path)
    # 仓库治理/元信息文件：由 GitHub 界面或 Hermes 运行时消费，不是知识孤立页
    if basename in ('README.md', 'LICENSE', 'HOME.md', 'SOUL.md', 'INDEX.md', 'MEMORY.md',
                    'CHANGELOG.md', 'CODE_OF_CONDUCT.md', 'CONTRIBUTING.md', 'SECURITY.md',
                    'SUPPORT.md', 'IDENTITY.md', 'USER.md', 'AGENTS.md', 'DREAMS.md',
                    'HEARTBEAT.md', 'CLAUDE.md'):
        continue
    if os.path.normpath(path).replace('\\', '/').lstrip('./').startswith(ORPHAN_IGNORE_PREFIXES):
        continue
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
    # 只写相对标识，不落绝对路径（报告会进 CI artifact / 曾被跟踪，绝对路径含用户名）
    'vault': os.path.basename(os.path.abspath(VAULT)) or 'vault',
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

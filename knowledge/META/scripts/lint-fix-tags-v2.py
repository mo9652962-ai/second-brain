#!/usr/bin/env python3
"""lint-fix-tags-v2.py: 幂等修复标签一致性问题 v3（精确 token 匹配，不伤复合词）
1. 修正 Education 某高校文件异常格式 tags:knowledge/education[ ] -> tags: [knowledge/education]
2. 修复错误 YAML 列表格式 tags: '- xxx' -> tags: [xxx]（Obsidian 无法解析）
3. 统一同义标签（仅列表内精确项）: thousand-round -> 千轮研究, 安全 -> security 等
4. 去掉列表项内的多余引号（["archive", "web"] -> [archive, web]）
只改 frontmatter tags，不动正文。
"""
import os, re

vault = r"%USERPROFILE%/.openclaw/workspace/knowledge"
os.chdir(vault)

# 同义标签统一映射（仅匹配独立标签 token）
SYNONYM_MAP = {
    "thousand-round": "千轮研究",
    "安全": "security",
    "闲鱼": "xianyu",
    "变现": "monetization",
    "方法论": "methodology",
    "研究": "research",
    "每周复盘": "weekly-review",
    "自动化": "automation",
    "知识吸收": "knowledge-absorption",
    "多Agent": "multi-agent",
    "AI博主": "ai-blogger",
    "Edge ai": "边缘AI",
    "系统清理": "system-cleanup",
    "知识库治理": "vault-maintenance",
    "HN精选": "hackernews",
    "降AI": "去AI味",
    "反AI味": "去AI味",
    "GitHub Trending": "github-trending",
    "编程": "programming",
    "架构": "architecture",
    "数据库": "database",
    "缓存": "cache",
    "知识图谱": "knowledge-graph",
    "教程": "tutorial",
    "索引": "index",
    "知识管理": "knowledge-management",
    '"archive"': "archive",
    '"web"': "web",
}

# 错误 YAML 列表格式：tags: '- xxx' -> tags: [xxx]
BAD_FORMAT_PAT = re.compile(r"^tags:\s*'-(.*)'\s*$")

# 特殊修正：异常格式文件
SPECIAL_FIX = {
    "Education/某高校目标专业-学业规划路线图-2026-08.md":
        (r"^tags:\s*.*$", "tags: [knowledge/education]"),
}

def fix_tags_line(line):
    """仅处理 [a, b, c] 形式，按精确项替换 + 去重；其他形式返回 None 表示跳过"""
    m = re.fullmatch(r"(\s*)([^:\[\]]+)(\s*:\s*)(\[[^\]]*\])", line)
    if not m:
        return None
    before, key, colon, bracket = m.groups()
    inner = bracket[1:-1]
    items = [x.strip() for x in inner.split(",") if x.strip()]
    out = []
    changed = False
    for it in items:
        new = SYNONYM_MAP.get(it, it)
        if new != it:
            changed = True
        if new not in out:
            out.append(new)
    if not changed and len(out) == len(items):
        return None
    return f"{before}{key}{colon}[{', '.join(out)}]"

changed = []
# Part 1: 特殊修正
for rel, (pat, repl) in SPECIAL_FIX.items():
    p = os.path.join(vault, rel)
    if not os.path.exists(p):
        print(f"[SKIP missing] {rel}")
        continue
    text = open(p, encoding="utf-8", errors="replace").read()
    m = re.match(r"^---\n(.*?)\n---", text, flags=re.S)
    if not m:
        print(f"[SKIP no-fm] {rel}")
        continue
    fm = m.group(1)
    tm = re.search(pat, fm, flags=re.M)
    if not tm:
        print(f"[SKIP no-match] {rel}")
        continue
    new_fm = fm[:tm.start()] + repl + fm[tm.end():]
    new_text = text[:m.start()] + "---\n" + new_fm + "---" + text[m.end():]
    if new_text == text:
        print(f"[SKIP already-fixed] {rel}")
        continue
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
    print(f"[FIX] {rel}: {tm.group(0).strip()} -> {repl}")
    changed.append(rel)

# Part 1.5: 统一 tags 格式：YAML 块式列表 -> 流式 [a, b]（Obsidian 均兼容，统一便于检索与脚本）
all_md = []
for root, _, fs in os.walk(vault):
    for f in fs:
        if f.endswith(".md"):
            all_md.append(os.path.join(root, f))

# 输入:
#   tags:
#     - a
#     - b
# 输出:
#   tags: [a, b]
def convert_block_tags(fm_text):
    """把 frontmatter 内 tags 块式列表转流式；无块式则原样返回。"""
    lines = fm_text.split("\n")
    out = []
    i = 0
    changed = False
    while i < len(lines):
        line = lines[i]
        if re.match(r"^tags:\s*$", line):
            # 收集后续缩进的 - xxx 行
            items = []
            j = i + 1
            while j < len(lines) and re.match(r"^\s+-\s+", lines[j]):
                items.append(lines[j].strip()[2:].strip())
                j += 1
            if items:
                out.append("tags: [" + ", ".join(items) + "]")
                i = j
                changed = True
                continue
        out.append(line)
        i += 1
    return "\n".join(out), changed

bad = 0
for p in all_md:
    rel = os.path.relpath(p, vault)
    text = open(p, encoding="utf-8", errors="replace").read()
    m = re.match(r"^---\n(.*?)\n---", text, flags=re.S)
    if not m:
        continue
    new_fm, fm_changed = convert_block_tags(m.group(1))
    if not fm_changed:
        continue
    new_text = text[:m.start()] + "---\n" + new_fm + "---" + text[m.end():]
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
    old_first = [l for l in m.group(1).split("\n") if l.strip().startswith("tags:") or l.strip().startswith("- ")][:2]
    print(f"[BADFMT] {rel}: {' | '.join(x.strip() for x in old_first)} ...")
    bad += 1
    changed.append(rel)

# Part 2: 列表内精确 token 替换
syn = 0
for p in all_md:
    rel = os.path.relpath(p, vault)
    text = open(p, encoding="utf-8", errors="replace").read()
    m = re.match(r"^---\n(.*?)\n---", text, flags=re.S)
    if not m:
        continue
    fm = m.group(1)
    tm = re.search(r"^tags:.*$", fm, flags=re.M)
    if not tm:
        continue
    new_line = fix_tags_line(tm.group(0))
    if new_line is None:
        continue
    new_fm = fm[:tm.start()] + new_line + fm[tm.end():]
    new_text = text[:m.start()] + "---\n" + new_fm + "---" + text[m.end():]
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
    print(f"[SYN] {rel}: {tm.group(0).strip()} -> {new_line.strip()}")
    syn += 1
    changed.append(rel)

print(f"\nDONE. files changed: {len(changed)} (synonym: {syn})")

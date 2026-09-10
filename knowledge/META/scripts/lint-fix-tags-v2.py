#!/usr/bin/env python3
"""lint-fix-tags-v2.py: 幂等修复标签一致性问题 v2（精确 token 匹配，不伤复合词）
1. 修正 Education 桂航文件异常格式 tags:knowledge/education[ ] -> tags: [knowledge/education]
2. 统一同义标签（仅列表内精确项）: thousand-round -> 千轮研究, 安全 -> security
只改 frontmatter tags，不动正文。
"""
import os, re

vault = r"C:/Users/31954/.openclaw/workspace/knowledge"
os.chdir(vault)

# 同义标签统一映射（仅匹配独立标签 token）
SYNONYM_MAP = {
    "thousand-round": "千轮研究",
    "安全": "security",
}

# 特殊修正：异常格式文件
SPECIAL_FIX = {
    "Education/桂航飞行器质量与可靠性-考研考证路线图-2026-08.md":
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

# Part 2: 列表内精确 token 替换
all_md = []
for root, _, fs in os.walk(vault):
    for f in fs:
        if f.endswith(".md"):
            all_md.append(os.path.join(root, f))

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

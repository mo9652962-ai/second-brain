# -*- coding: utf-8 -*-
"""knowledge-lint 修复：补 frontmatter + 挂载孤立页（幂等）"""
import os, re, io

ROOT = r"C:\Users\31954\.openclaw\workspace\knowledge"

def read_text(p):
    with io.open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def write_text(p, s):
    with io.open(p, "w", encoding="utf-8", newline="") as f:
        f.write(s)

def has_frontmatter(content):
    return content.lstrip("\ufeff \t\r\n").startswith("---")

def prepend_frontmatter(p, fm):
    c = read_text(p)
    if has_frontmatter(c):
        print(f"[SKIP] already has frontmatter: {p}")
        return
    # 去掉文件开头的 BOM / 空行
    c = c.lstrip("\ufeff \t\r\n")
    new = fm.rstrip("\r\n") + "\n\n" + c
    write_text(p, new)
    print(f"[OK] frontmatter added: {p}")

# ---------- 1. 补 frontmatter ----------
prepend_frontmatter(os.path.join(ROOT, "Productivity", "system-cleanup-report-20260906.md"), """---
title: "系统清理报告 2026-09-06"
type: note
domain: Productivity
status: active
tags: [knowledge/productivity]
source: null
date: 2026-09-06
---""")

prepend_frontmatter(os.path.join(ROOT, "Productivity", "token-usage-report-20260906.md"), """---
date: 2026-09-06
tags: [周报, API成本, Token用量, 存储, 运维监控]
aliases: [API成本周报W36, weekly-cost-report-2026W36]
status: adopted
---""")

prepend_frontmatter(os.path.join(ROOT, "Research", "GitHub-Weekly-2026-09-06.md"), """---
title: "GitHub 宝藏挖掘 - 2026-09-06"
type: note
domain: Research
status: active
tags: [knowledge/research]
source: null
date: 2026-09-06
---""")

# ---------- 2. 挂载孤立页（幂等：检测 [[目标]] 是否已存在） ----------
def mount(moc_path, link_line, anchor=None):
    p = os.path.join(ROOT, moc_path)
    c = read_text(p)
    # 提取链接名（去掉别名和路径）
    m = re.search(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", link_line)
    target = m.group(1).strip() if m else link_line
    # 宽松匹配：路径尾段相同即视为已挂载
    tail = target.split("/")[-1]
    if re.search(r"\[\[[^\]]*" + re.escape(tail) + r"[^\]]*\]\]", c):
        print(f"[SKIP] already mounted: {target} in {moc_path}")
        return
    if anchor is None:
        c = c.rstrip("\r\n") + "\n" + link_line + "\n"
    else:
        idx = c.rfind(anchor)
        if idx == -1:
            print(f"[WARN] anchor not found in {moc_path}: {anchor!r}")
            return
        # 在 anchor 行之后插入
        end = c.find("\n", idx)
        c = c[:end+1] + link_line + "\n" + c[end+1:]
    write_text(p, c)
    print(f"[OK] mounted: {target} -> {moc_path}")

mount("MOC-Inbox.md", "- [[Daily/hackernews-2026-09-06]]", anchor="- [[Daily/hackernews-2026-09-05]]")
mount("Productivity/MOC-Productivity.md", "- [[knowledge/Productivity/token-usage-report-20260906|Token 用量报告 09-06]]", anchor="## 🆕 W37 新增（08-31 ~ 09-06：部署 + 动效 + 闲鱼运营）")
mount("Productivity/MOC-Productivity.md", "- [[knowledge/Productivity/system-cleanup-report-20260906|系统清理报告 09-06]] — 释放约 7GB", anchor="## 🆕 W37 新增（08-31 ~ 09-06：部署 + 动效 + 闲鱼运营）")
mount("Research/MOC-Research.md", "- [[arxiv-2026-09-07-agent-llm]]", anchor="- [[arxiv-2026-09-06-agent-llm]]")

print("DONE")

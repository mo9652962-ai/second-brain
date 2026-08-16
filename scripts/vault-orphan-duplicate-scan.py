#!/usr/bin/env python3
"""vault-orphan-duplicate-scan.py — 孤立笔记 + 相似标题扫描

功能:
  1. 解析全仓库 .md 笔记的 [[wikilink]] 与 [md链接](x.md)，构建入链图
  2. 孤立笔记 = 没有任何入链的笔记（结构性入口如 HOME/MOC 单独归类，不算孤立）
  3. 重复内容候选 = 同名冲突（不同目录同名）/ 规范化后同名 / 标题相似度 >= 阈值

用法:
  python scripts/vault-orphan-duplicate-scan.py                      # 全仓库
  python scripts/vault-orphan-duplicate-scan.py --scope knowledge    # 只报告 knowledge/ 下的孤立笔记
  python scripts/vault-orphan-duplicate-scan.py --json report.json   # 额外输出 JSON
  python scripts/vault-orphan-duplicate-scan.py --threshold 0.85     # 调整相似度阈值
"""
import argparse
import difflib
import json
import os
import re
import sys
from collections import defaultdict

try:  # Windows 控制台中文输出
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

VAULT = os.environ.get("VAULT_PATH", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SKIP_DIRS = {".git", ".obsidian", ".venv", "node_modules", "__pycache__",
             "site", "graphify-out", ".clawhub", ".learnings", ".skillkit",
             ".hermes", ".code-review-graph", ".temp", "traces"}

# 结构性入口：本来就是导航起点，无入链是预期行为，不计入孤立
STRUCTURAL = re.compile(
    r"^(HOME|INDEX|README|CHANGELOG|MOC-.*|knowledge-map|Cross-Domain|"
    r"SUPPORT|Support|AGENTS|AGENTS\.md|IDOCUMENT.*)$", re.IGNORECASE)

WIKILINK = re.compile(r"\[\[([^\[\]]+?)\]\]")
MDLINK = re.compile(r"\[[^\]]*\]\(([^)]+?\.md)(?:#[^)]*)?\)", re.IGNORECASE)
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
ALIAS_LINE = re.compile(r"^aliases?:\s*(.+)$", re.MULTILINE)

DATE_PAT = re.compile(r"[-_ ]?(?:20\d{2})[-._]?(?:0[1-9]|1[0-2])?[-._]?(?:0[1-9]|[12]\d|3[01])?")
STRIP_TOKENS = re.compile(
    r"(?:-|_| |)(?:absorbed|adopted|study|research|deepdive|deep-dive|guide|"
    r"reference|notes?|draft|final|v\d+|副本|备份|\d{1,2})$", re.IGNORECASE)


def collect_notes(vault):
    """返回 {绝对路径: 相对路径}，跳过生成目录与隐藏目录。"""
    notes = {}
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in files:
            if f.lower().endswith(".md"):
                p = os.path.join(root, f)
                notes[p] = os.path.relpath(p, vault).replace("\\", "/")
    return notes


def parse_aliases(text):
    fm = FRONTMATTER.match(text)
    if not fm:
        return set()
    out = set()
    for m in ALIAS_LINE.finditer(fm.group(1)):
        raw = m.group(1).strip()
        if raw.startswith("[") and raw.endswith("]"):
            raw = raw[1:-1]
        for part in raw.split(","):
            part = part.strip().strip("-\"' ")
            if part:
                out.add(part)
    return out


def extract_targets(rel_path, text):
    """提取该笔记指向的所有链接目标（去 alias / 锚点 / 外部 http）。"""
    targets = set()
    for m in WIKILINK.finditer(text):
        t = m.group(1).split("|")[0].split("#")[0].strip()
        if t:
            targets.add(t)
    for m in MDLINK.finditer(text):
        u = m.group(1).strip()
        if not u.lower().startswith(("http://", "https://")):
            targets.add(u)
    return targets


def build_resolver(notes):
    """basename / alias / 路径后缀 → 路径集合（全部小写归一）。"""
    by_base, by_alias, by_path = defaultdict(set), defaultdict(set), defaultdict(set)
    for p, rel in notes.items():
        base = os.path.basename(p)[:-3].lower()
        by_base[base].add(p)
        by_path[rel.lower()] = set([p])
        by_path[rel.lower()[:-3]] = set([p])
        with open(p, encoding="utf-8", errors="replace") as fh:
            aliases = parse_aliases(fh.read(4000))
        for a in aliases:
            by_alias[a.strip().lower()] .add(p)
    return by_base, by_alias, by_path


def resolve(target, by_base, by_alias, by_path):
    t = target.strip().lower()
    if not t.endswith(".md"):
        t_noext = t
    else:
        t_noext = t[:-3]
    cands = set()
    cands |= by_path.get(t, set()) | by_path.get(t_noext, set())
    cands |= by_base.get(os.path.basename(t_noext), set())
    cands |= by_alias.get(os.path.basename(t_noext), set())
    # 路径后缀匹配（链接写的是 knowledge/Dev/x 而 t 含目录）
    if "/" in t_noext:
        for rel, ps in by_path.items():
            if rel.endswith("/" + t_noext) or rel == t_noext:
                cands |= ps
    return cands


def normalize_title(name):
    name = os.path.basename(name)[:-3]
    name = DATE_PAT.sub("", name)
    prev = None
    while prev != name:
        prev = name
        name = STRIP_TOKENS.sub("", name)
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]", "", name.lower())


def main():
    ap = argparse.ArgumentParser(description="孤立笔记 + 相似标题扫描")
    ap.add_argument("--scope", default="", help="只报告该子目录下的孤立笔记，如 knowledge")
    ap.add_argument("--json", dest="json_out", default="", help="JSON 报告输出路径")
    ap.add_argument("--threshold", type=float, default=0.82, help="标题相似度阈值")
    args = ap.parse_args()

    notes = collect_notes(VAULT)
    by_base, by_alias, by_path = build_resolver(notes)
    inlinks = defaultdict(list)  # 被链路径 <- 来源路径列表

    for p, rel in notes.items():
        with open(p, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for t in extract_targets(rel, text):
            for hit in resolve(t, by_base, by_alias, by_path):
                if hit != p:
                    inlinks[hit].append(p)

    # ---- 孤立笔记 ----
    scope_prefix = (args.scope + "/").lower() if args.scope else ""
    orphans, structural = [], []
    for p, rel in sorted(notes.items(), key=lambda kv: kv[1].lower()):
        if inlinks.get(p):
            continue
        if scope_prefix and not rel.lower().startswith(scope_prefix):
            continue
        base = os.path.basename(p)[:-3]
        if STRUCTURAL.match(base) or "/templates/" in rel or rel.startswith("templates/"):
            structural.append(rel)
        else:
            orphans.append(rel)

    # ---- 重复标题 ----
    exact_groups = defaultdict(list)
    norm_groups = defaultdict(list)
    for p, rel in notes.items():
        base = os.path.basename(p)[:-3]
        exact_groups[base.lower()].append(rel)
        norm_groups[normalize_title(p)].append(rel)

    same_name = {k: v for k, v in exact_groups.items() if len(v) > 1}
    norm_dup = {k: v for k, v in norm_groups.items()
                if len(v) > 1 and k not in same_name and len(k) >= 4}

    names = sorted({os.path.basename(p)[:-3] for p in notes})
    fuzzy = []
    for i in range(len(names)):
        a = names[i]
        sm = difflib.SequenceMatcher(None, a.lower(), b="")
        for j in range(i + 1, len(names)):
            b = names[j]
            if abs(len(a) - len(b)) > 12:
                continue
            sm.set_seq2(b.lower())
            if sm.real_quick_ratio() < args.threshold or sm.quick_ratio() < args.threshold:
                continue
            r = sm.ratio()
            if r >= args.threshold:
                fuzzy.append((round(r, 3), a, b))

    fuzzy.sort(reverse=True)

    # ---- 报告 ----
    print(f"# vault 扫描报告（{len(notes)} 篇 md · 相似阈值 {args.threshold}）")
    print(f"\n## 孤立笔记（无入链，{len(orphans)} 篇）")
    for r in orphans:
        print(f"  - {r}")
    print(f"\n## 结构性入口（预期无入链，{len(structural)} 篇）")
    for r in structural:
        print(f"  - {r}")

    print(f"\n## 同名冲突（不同目录同名，{len(same_name)} 组）")
    for k, v in sorted(same_name.items()):
        print(f"  - [{k}]")
        for r in sorted(v):
            print(f"      {r}")

    print(f"\n## 规范化后同名（去日期/后缀后重复，{len(norm_dup)} 组）")
    for k, v in sorted(norm_dup.items()):
        print(f"  - [{k}]")
        for r in sorted(v):
            print(f"      {r}")

    print(f"\n## 相似标题对（TOP 40）")
    for r, a, b in fuzzy[:40]:
        print(f"  {r:.2f}  {a}  ~  {b}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({
                "total_notes": len(notes),
                "orphans": orphans,
                "structural_entry_points": structural,
                "same_name_groups": same_name,
                "normalized_dup_groups": norm_dup,
                "fuzzy_pairs": [{"ratio": r, "a": a, "b": b} for r, a, b in fuzzy],
            }, fh, ensure_ascii=False, indent=2)
        print(f"\nJSON 报告已写入 {args.json_out}")


if __name__ == "__main__":
    main()

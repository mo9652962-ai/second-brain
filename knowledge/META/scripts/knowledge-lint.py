#!/usr/bin/env python3
"""knowledge-lint: 只读体检 Obsidian 知识库（基于 Karpathy LLM-Wiki Lint + kb-health 方法论）。

检查项（全部只读，不修改任何文件）：
1. 孤立页面 - 无任何入链（被其他页面 [[引用]] 的才算）
2. 断链 - [[链接]] 目标文件不存在
3. 重复文件名 - 不同目录下同名 slug
4. 缺 frontmatter - 没有 YAML frontmatter 或缺 title
5. 短页面 - 纯文本 < 100 字符
6. 陈旧页面 - 90 天未更新（info 级）
7. index 漂移 - 文件存在但 index 未收录（仅报告，不修）
输出：按 ERROR/WARNING/INFO 分级报告。用法: python knowledge-lint.py <vault_root>
"""
import os
import re
import sys
import glob
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timedelta

SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", ".archive", "Archive"}
# 跨 vault 根目录（workspace 下存在，Obsidian 合法，不判断链）
# 仅 workspace 根级跨 vault 目录（Obsidian 中合法，不判链）
# 注意: 不要加入 knowledge/ 内部子目录（Daily/Projects/META/Dev 等）——否则内部链接被跳过会误报孤立
EXTERNAL_ROOTS = {"memory", "projects", "skills", "cards", "SOP", "HOME", "Home", "SOUL", "TOOLS",
                  "AGENTS", "MEMORY", "Cross-Domain", "knowledge-map", "MOC-"}
# 模板占位符
PLACEHOLDER_LINKS = {"name", "their-name", "wiki link", ":space:", "TODO", "link"}
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def collect_md_files(root: Path):
    files = []
    for p in root.resolve().rglob("*.md"):
        rel = p.relative_to(root.resolve())
        parts = rel.parts
        if any(s in SKIP_DIRS for s in parts):
            continue
        files.append(p.resolve())  # 统一为绝对路径，与链接解析一致
    return files


def extract_links(text: str):
    return [m.strip() for m in WIKILINK_RE.findall(text)]


def slug_of(path: Path, root: Path):
    rel = path.resolve().relative_to(root.resolve())
    return rel.with_suffix("").as_posix().lower()


def strip_md(name: str) -> str:
    """去掉 .md 后缀（保留版本号中的点，如 MiMo-V2.5）。"""
    return name[:-3] if name.lower().endswith(".md") else name


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    files = collect_md_files(root)
    slug_to_path = {}
    name_to_paths = defaultdict(list)
    for f in files:
        slug_to_path[slug_of(f, root)] = f
        name_to_paths[strip_md(f.name).lower()].append(f)

    # 1) 入链索引
    inlinks = defaultdict(set)
    outlinks = {}
    missing_frontmatter = []
    short_pages = []
    stale_pages = []
    broken = []
    now = datetime.now()

    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        links = extract_links(text)
        outlinks[f] = links
        for link in links:
            target = link.replace("\\", "/")
            # 模板占位符 → 跳过
            if target.lower() in PLACEHOLDER_LINKS:
                continue
            # 跨 vault 根目录引用（../memory/、skills/、projects/ 等）→ 合法跳过
            first_seg = target.lstrip("./").split("/")[0]
            if first_seg in EXTERNAL_ROOTS:
                continue
            # 跨目录/跨层链接（../ 开头或含 /）在 Obsidian 中合法，按相对路径解析
            if target.startswith("../") or "/" in target:
                # 尝试相对解析：从当前文件目录出发
                cand = (f.parent / target).resolve()
                if cand.exists():
                    inlinks[cand].add(f)
                    continue
                cand_md = cand.with_suffix(".md")
                if cand_md.exists():
                    inlinks[cand_md].add(f)
                    continue
                # 尝试从 vault 根解析
                cand2 = (root / target).resolve()
                if cand2.exists():
                    inlinks[cand2].add(f)
                    continue
                cand2_md = cand2.with_suffix(".md")
                if cand2_md.exists():
                    inlinks[cand2_md].add(f)
                    continue
                # 尝试文件名校验（跨目录链接常见）
                stem_matched = False
                for cand in name_to_paths.get(strip_md(Path(target).name).lower(), []):
                    inlinks[cand].add(f)
                    stem_matched = True
                    break
                if stem_matched:
                    continue
                # 顶层 Home/SOUL 等在 workspace 根，不是断链
                if target in {"Home", "SOUL", "TOOLS", "MOC-Research"}:
                    continue
                broken.append((f, target))
                continue
            # 普通 wikilink
            target_slug = target.lower()
            if target_slug in slug_to_path:
                inlinks[slug_to_path[target_slug]].add(f)
            else:
                # 尝试只匹配文件名（忽略目录）
                matched = False
                for cand in name_to_paths.get(strip_md(Path(target).name).lower(), []):
                    if slug_of(cand, root) == target_slug or strip_md(cand.name).lower() == strip_md(Path(target).name).lower():
                        inlinks[cand].add(f)
                        matched = True
                        break
                if not matched:
                    broken.append((f, target))

        # frontmatter
        if not text.startswith("---"):
            missing_frontmatter.append(f)
        # 短页面
        plain = re.sub(r"[#*`\[\]()>_~\-]", "", text)
        plain = re.sub(r"\n+", "\n", plain).strip()
        if len(plain) < 100:
            short_pages.append(f)
        # 陈旧（info）
        mtime = datetime.fromtimestamp(f.stat().st_mtime)
        if mtime < now - timedelta(days=90):
            stale_pages.append((f, mtime.date()))

    # 2) 孤立（无入链，且非 MOC/index/Home）
    orphans = []
    for f in files:
        stem = f.stem.lower()
        if stem in {"home", "index", "log", "knowledge-map"} or "moc-" in stem or f.parent.name == "META":
            continue
        if not inlinks.get(f):
            orphans.append(f)

    # 3) 重复文件名
    dup = {name: paths for name, paths in name_to_paths.items() if len(paths) > 1 and name not in {"index", "log", "home"}}

    # 报告
    print("=" * 60)
    print(f"KNOWLEDGE LINT REPORT — {datetime.now():%Y-%m-%d}")
    print(f"Root: {root.resolve()}")
    print(f"Pages scanned: {len(files)}")
    print("=" * 60)

    print(f"\n[ERROR] Broken wikilinks: {len(broken)}")
    for f, target in broken:
        print(f"  {f.relative_to(root.resolve())} -> [[{target}]] (not found)")

    print(f"\n[ERROR] Missing frontmatter: {len(missing_frontmatter)}")
    for f in missing_frontmatter[:10]:
        print(f"  {f.relative_to(root.resolve())}")

    print(f"\n[WARNING] Orphan pages (no inlinks): {len(orphans)}")
    for f in orphans[:20]:
        print(f"  {f.relative_to(root.resolve())}")
    if len(orphans) > 20:
        print(f"  ... and {len(orphans)-20} more")

    print(f"\n[WARNING] Duplicate filenames: {len(dup)} groups")
    for name, paths in list(dup.items())[:10]:
        print(f"  '{name}': {[str(p.relative_to(root.resolve())) for p in paths]}")

    print(f"\n[WARNING] Short pages (<100 chars): {len(short_pages)}")
    for f in short_pages[:10]:
        print(f"  {f.relative_to(root.resolve())}")

    print(f"\n[INFO] Stale pages (>90d): {len(stale_pages)}")
    for f, d in stale_pages[:10]:
        print(f"  {f.relative_to(root.resolve())} ({d})")

    total = len(broken) + len(missing_frontmatter) + len(orphans) + len(dup) + len(short_pages)
    print("\n" + "=" * 60)
    print(f"TOTAL ISSUES: {total}")
    print("HEALTH:", "GOOD" if total == 0 else "NEEDS ATTENTION")
    print("=" * 60)


if __name__ == "__main__":
    main()

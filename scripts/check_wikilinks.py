"""wikilink 断链检查（CI + 本地通用）

修复历史 bug（2026-09-20）：
  1. os.path.join 在 Windows 产生反斜杠，与链接里的正斜杠永不匹配 → 1990 条假阳性
  2. 只做 `target in p` 全路径子串匹配，Obsidian 的 basename 短链（[[note-name]]）全被误报
  3. 未跳过跨 vault 根引用（HOME/SOUL/projects/ 等），误报 740 条

对齐 knowledge/META/scripts/knowledge-lint.py 的判定逻辑（该脚本已修，本脚本为遗留副本）。
"""
import os
import re
import sys
from pathlib import Path

# 跨 vault 根引用（workspace 根或外部目录），合法跳过——与 knowledge-lint.py EXTERNAL_ROOTS 对齐
EXTERNAL_ROOTS = {
    "home", "soul", "tools", "agents", "projects", "memory", "skills",
    "outputs", "scripts", "docs", "readme", "contributing", "changelog",
}
# 模板占位符，跳过
PLACEHOLDER_LINKS = {
    "页面名", "a", "b", "note-1", "wikilink", "wiki link", "所属moc",
    "```", "` `", ":space:", "xxx", "example",
    # 2026-09-20 补充：文档/维护笔记中作为示例出现的占位符（均为 prose 描述，非真链接）
    "series-2026-08-14", "skill-name", "their-name", "name",
    "2026-07-21-2347", "。", "`。`",
}

# 代码围栏 / 行内代码：其中的 [[...]] 是语法示例，不是链接
CODE_FENCE_RE = re.compile(r"```.*?```", re.S)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def mask_code(text: str) -> str:
    """把代码围栏与行内代码替换为等长空格（保留换行，行号不变）"""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    return INLINE_CODE_RE.sub(blank, CODE_FENCE_RE.sub(blank, text))


def strip_md(name: str) -> str:
    """只剥 .md 后缀（Path.stem 会把 MiMo-V2.5 截成 MiMo-V2）"""
    return name[:-3] if name.lower().endswith(".md") else name


def collect_notes(root_dir: str):
    """返回 (all_paths, by_stem, by_basename) —— 全部使用正斜杠相对路径"""
    all_paths = set()
    by_stem = {}       # 相对路径去 .md → 路径
    by_basename = {}   # 文件名去 .md → [路径...]
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "node_modules"]
        for f in files:
            if not f.endswith(".md"):
                continue
            rel = os.path.join(root, f).replace(os.sep, "/").lstrip("./")
            all_paths.add(rel)
            by_stem.setdefault(strip_md(rel).lower(), rel)
            by_basename.setdefault(strip_md(f).lower(), []).append(rel)
    return all_paths, by_stem, by_basename


def main() -> int:
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    all_paths, by_stem, by_basename = collect_notes(root_dir)

    errors = 0
    for rel in sorted(all_paths):
        try:
            text = Path(rel).read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        # 代码围栏/行内代码里的 [[...]] 是语法示例，不是真链接 → 先屏蔽
        text = mask_code(text)
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in re.finditer(r"\[\[([^\]]+)\]\]", line):
                raw = m.group(1).split("|")[0].split("#")[0].strip()
                target = raw.replace("\\", "/")
                if not target:
                    continue
                if target.lower() in PLACEHOLDER_LINKS:
                    continue
                if target.lower().startswith("http"):
                    continue

                first_seg = target.lstrip("./").split("/")[0].lower()
                if first_seg in EXTERNAL_ROOTS:
                    continue
                # 纯 basename 短链（Obsidian 常见）
                if "/" not in target and not target.startswith(".."):
                    if strip_md(target).lower() in by_basename:
                        continue
                    print(f"⚠ Broken link: {rel}:{lineno} → {raw}")
                    errors += 1
                    continue

                # 含路径的引用：依次尝试 相对当前文件 / vault 根 / 去 knowledge 前缀 / stem 兜底
                cands = [
                    (Path(rel).parent / target),
                    Path(target),
                    Path(target[len("knowledge/"):]) if target.startswith("knowledge/") else None,
                ]
                ok = False
                for c in cands:
                    if c is None:
                        continue
                    for probe in (c, Path(str(c) + ".md")):
                        p = str(probe).replace(os.sep, "/").lstrip("./")
                        if p in all_paths:
                            ok = True
                            break
                    if ok:
                        break
                if not ok:
                    key = strip_md(target).lower()
                    if key in by_stem or strip_md(Path(target).name).lower() in by_basename:
                        continue
                    print(f"⚠ Broken link: {rel}:{lineno} → {raw}")
                    errors += 1

    if errors:
        print(f"❌ Found {errors} broken wikilinks")
        return 1
    print("✅ All wikilinks OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

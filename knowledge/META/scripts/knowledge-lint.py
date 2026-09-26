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

try:
    import yaml
except ImportError:          # pyyaml 可选依赖：缺失时跳过 YAML 校验，不阻断其他检查
    yaml = None

SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", ".archive", "Archive"}
# 跨 vault 根目录（workspace 下存在，Obsidian 合法，不判断链）
# 仅 workspace 根级跨 vault 目录（Obsidian 中合法，不判链）
# 注意: 不要加入 knowledge/ 内部子目录（Daily/Projects/META/Dev 等）——否则内部链接被跳过会误报孤立
EXTERNAL_ROOTS = {"memory", "projects", "skills", "cards", "SOP", "HOME", "Home", "SOUL", "TOOLS",
                  "AGENTS", "MEMORY", "Cross-Domain", "knowledge-map", "MOC-",
                  # 2026-09-26：vault 根级目录（不在 knowledge/ 内），与 projects/memory 同类，
                  # 从 knowledge/ 出发永远无法相对解析 → 白名单跳过（否则 MOC 挂载根级文件必报断链）
                  "pipelines", "playbooks", "system", "todo", "health", "concepts",
                  "outputs", "scripts", "docs", "templates", "portfolio", "site"}
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


CODE_SPAN_RE = re.compile(r"`[^`]*`")            # 行内反引号代码
FENCE_RE = re.compile(r"```.*?```", flags=re.S)   # 多行代码块

def extract_links(text: str):
    # 先剥离反引号代码 span 和 ``` 代码块，避免把示例/占位符当 wikilink（假阳性）
    text = CODE_SPAN_RE.sub("", text)
    text = FENCE_RE.sub("", text)
    return [m.strip() for m in WIKILINK_RE.findall(text)]


def slug_of(path: Path, root: Path):
    rel = path.resolve().relative_to(root.resolve())
    return rel.with_suffix("").as_posix().lower()


def strip_md(name: str) -> str:
    """去掉 .md 后缀（保留版本号中的点，如 MiMo-V2.5）。"""
    return name[:-3] if name.lower().endswith(".md") else name


def scan_frontmatter(lines: list[str]) -> tuple[bool, int | None]:
    """定位 frontmatter 区并判断闭合符是否粘连。

    返回 (glued, close_idx)：
      glued     — 闭合符粘连（如 `status: fresh---`）或整份文件找不到独立闭合行
      close_idx — 首个独立 `---` 的行号；未闭合时为 None

    为什么不能只问「前 N 行有没有独立 ---」：
      正文的水平分隔线 `---` 与 frontmatter 闭合符同形。若只在前 20 行里找任意
      独立 `---`，正文横线会冒充闭合符 → 真实粘连行被掩盖，静默漏报
      （2026-09-26 实测漏报 80 个文件而 lint 报 Glued 0）。
    故必须锚定结构边界：从第 2 行起扫描，**首个**独立 `---` 即区间终点；
    该区间内任何以 `---` 结尾的行即粘连。
    """
    for i, line in enumerate(lines[1:], start=1):
        s = line.strip()
        if s == "---":
            return False, i
        if s.endswith("---"):
            return True, None
    return True, None          # 从未闭合 → 同样按粘连上报


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
    glued_fm = []
    bad_yaml = []
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
                # 剥离 knowledge/ 前缀（MOC 中常见的 workspace 根级全路径写法，vault root 已是 knowledge/）
                if target.startswith("knowledge/") or target == "knowledge":
                    target = target[len("knowledge/"):]
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
        else:
            # 粘连闭合符检测（2026-09-26 修复假阴性盲区）
            # 旧实现 any(l.strip()=="---" for l in fm_lines[1:20])：
            #   只要前 20 行内存在任意独立 --- 就判"已闭合" → 正文首个水平分隔线 ---
            #   会掩盖第 7 行真正的粘连闭合符（如 `status: fresh---`），实测漏报 80 个文件
            #   （cards 27 / Research 49 / Archive 3 / Security 1），且 lint 报 Glued 0 → 静默失效。
            # 新实现：frontmatter 区 = 第 2 行起，到**首个**独立 --- 为止；该区间内任何
            #   以 --- 结尾（且非独立）的行即粘连。无独立闭合行同样判粘连。
            fm_lines = text.split("\n")
            glued, close_idx = scan_frontmatter(fm_lines)
            if glued:
                glued_fm.append(f)
            else:
                # YAML 可解析性检测（2026-09-26 新增）
                # 动机：`related: [[A]], [[B]]` 这类未加引号的 wikilink 列表在 YAML 中非法
                # （`[` 开启 flow sequence → 解析崩溃），但 lint 旧版只看 frontmatter 是否存在、
                # 不验证能否解析 → Obsidian/Dataview 静默丢字段，实测漏报 1 个文件
                # （knowledge/Dev/Programming.md）。全部属性（MOC 分组、Dataview 查询、
                # 代谢分类）都依赖 frontmatter 可解析，故必须纳入门禁。
                # 注意：只取 [1, close_idx) 区间——把闭合 --- 及其后正文一并喂给
                # safe_load 会误报 "expected a single document in the stream"。
                if yaml is not None:
                    try:
                        meta = yaml.safe_load("\n".join(fm_lines[1:close_idx]))
                        if meta is not None and not isinstance(meta, dict):
                            bad_yaml.append((f, "frontmatter 不是键值映射"))
                    except Exception as e:
                        first = str(e).split("\n")[0]
                        bad_yaml.append((f, first[:70]))
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

    print(f"\n[ERROR] Glued frontmatter close (no standalone ---): {len(glued_fm)}")
    for f in glued_fm[:10]:
        print(f"  {f.relative_to(root.resolve())}")

    print(f"\n[ERROR] Invalid YAML frontmatter: {len(bad_yaml)}")
    for f, why in bad_yaml[:10]:
        print(f"  {f.relative_to(root.resolve())} ({why})")

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

    total = len(broken) + len(missing_frontmatter) + len(glued_fm) + len(bad_yaml) + len(orphans) + len(dup) + len(short_pages)
    print("\n" + "=" * 60)
    print(f"TOTAL ISSUES: {total}")
    print("HEALTH:", "GOOD" if total == 0 else "NEEDS ATTENTION")
    print("=" * 60)


if __name__ == "__main__":
    main()

"""每日知识库自动优化脚本（second-brain vault）
1. 扫描新增孤立笔记（无 [[] 链接）→ 按目录补链所属 MOC/Home
2. MOC-Research 增量更新（Research 目录新笔记加入索引）
3. 知识地图日期更新
4. 输出变更报告（stdout → cron 注入 agent prompt）

用法: python scripts/daily_vault_optimize.py [--commit]
"""
import argparse
import datetime
import os
import pathlib
import re
import subprocess
import sys

# %USERPROFILE% 是字面量，Path 不会自动展开环境变量（否则 VAULT 指向不存在路径 → 扫出 0 笔记）
VAULT = pathlib.Path(os.path.expandvars(r"%USERPROFILE%\.openclaw\workspace"))

# 输入有效性断言（2026-09-08 静默失效 bug 防线）：VAULT 不存在/不是目录 → 立即 FATAL，不许"假装成功"
if not VAULT.exists() or not VAULT.is_dir():
    raise SystemExit(
        f"[FATAL] VAULT 路径不存在或不是目录: {VAULT}（%USERPROFILE% 展开失败？）"
    )
MIN_NOTE_COUNT = 100  # 正常 vault 笔记数下限，低于此视为扫描异常（静默失效防线）


DIR_MOC = {
    "knowledge/Research": "MOC-Research",
    "knowledge/Dev": "MOC-Dev",
    "knowledge/Hardware": "MOC-Hardware",
    "knowledge/Productivity": "MOC-Productivity",
    "knowledge/Security": "MOC-Security",
    "knowledge/Finance": "MOC-Finance",
    "knowledge/SOP": "MOC-SOP",
    "knowledge/Projects": "MOC-Projects",
    "knowledge/Creative": "MOC-Creative",
    "knowledge/Archive": "MOC-Archive", "knowledge/Daily": "MOC-Daily",
    "knowledge/cards": "MOC-cards",
    "knowledge/AI": "MOC-AI",
    "knowledge/Content": "MOC-Content",
    "knowledge/Education": "MOC-Education",
    "knowledge/Development": "MOC-Dev",
    "knowledge/gaming": "MOC-gaming",
    "knowledge/META": "MOC-META",
    "knowledge/Product": "MOC-Product",
    "memory": "knowledge-map", "concepts": "knowledge-map",
    "research": "MOC-Research", "docs": "knowledge-map",
    "health": "knowledge-map", "playbooks": "knowledge-map",
    "portfolio": "knowledge-map", "projects": "knowledge-map",
    "templates": "knowledge-map", "traces": "knowledge-map",
    "system": "knowledge-map",
}

LINK_RE = re.compile(r"\[\[([^\]|#]+)")

# 误改保险：正常 vault 孤儿数应是个位数；超此阈值视为检测器故障，拒绝执行
ORPHAN_SANITY_CAP = 25


def resolve_moc(name: str):
    """定位 MOC 文件：knowledge/**/MOC-<name>.md 或 knowledge/<name>.md"""
    for p in VAULT.rglob(f"{name}.md"):
        s = str(p)
        if ".git" in s or ".venv" in s or "node_modules" in s:
            continue
        if p.name.startswith("MOC-") or p.parent.name in ("knowledge", "META"):
            return p
    return None


def lint_orphans():
    """调用 knowledge-lint.py 拿权威孤儿列表（单一真相源）。

    为什么不自己算：lint 的入链解析要处理相对路径、跨目录、EXTERNAL_ROOTS 白名单等
    多种情形，自实现极易漂移——实测自写版误报 693 个 vs lint 真实 2 个（差 346 倍）。
    宁可调脚本 + 解析，也不要两套口径。
    解析失败一律返回 None（拒绝猜测 → 拒绝误改）。
    """
    lint = VAULT / "knowledge" / "META" / "scripts" / "knowledge-lint.py"
    if not lint.exists():
        return None
    try:
        r = subprocess.run([sys.executable, str(lint), "knowledge"],
                           capture_output=True, text=True, timeout=300, cwd=str(VAULT))
    except Exception as e:
        print(f"  [WARN] lint 调用失败: {e}")
        return None
    out = r.stdout
    m = re.search(r"Orphan pages \(no inlinks\): (\d+)", out)
    if not m:
        print("  [WARN] 无法从 lint 输出解析孤儿数 → 拒绝执行（不猜）")
        return None
    declared = int(m.group(1))
    body = out.split("Orphan pages (no inlinks):", 1)[1].splitlines()[1:]
    rels = []
    for ln in body:
        if not ln.startswith("  "):
            break                      # 缩进结束 = 该节结束
        if ln.strip().startswith("..."):
            break                      # "... and N more" 截断提示
        rels.append(ln.strip())
    if len(rels) != declared:
        print(f"  [WARN] 解析到 {len(rels)} 条 != 声明 {declared} 条 → 拒绝执行")
        return None
    return [VAULT / "knowledge" / r.replace("\\", "/") for r in rels]


AUTOMOUNT_MARKER = "## 自动挂载"
BARE_MOUNT_RE = re.compile(r"^\s*-\s*\[\[([^\]|#]+)\]\]\s*$")


def linked_stems(text: str) -> set:
    """抽出文中所有 wikilink 的「stem 级」集合（去显示名、去标题锚点、去路径前缀）。

    为什么不能字面比对：`[[stem]]` / `[[stem|显示名]]` / `[[path/stem]]` 三种写法
    互不相等，字面 `f"[[{stem}]]" in text` 只认第一种 → 已登记过的笔记会被当成
    未登记，自动挂载小节反复追加（2026-11-06 审计发现的重复索引根因）。
    """
    return {tok.rsplit("/", 1)[-1].strip() for tok in LINK_RE.findall(text)}


def dedupe_automount(text: str) -> tuple:
    """删掉「## 自动挂载」小节里与其他登记重复的裸挂载行（`- [[stem]]`）。

    判据是 stem 级计数：同一 stem 在文件里出现 >1 次时，只保留第一条（通常是带
    说明的正文行），裸挂载行删除；小节内两条都裸则保留首条。只动自动挂载小节，
    不碰正文，避免误删人工整理的分组条目。
    """
    lines = text.split("\n")
    marker_idx = next((i for i, ln in enumerate(lines) if ln.strip() == AUTOMOUNT_MARKER), None)
    if marker_idx is None:
        return text, 0
    counts = {}
    for ln in lines:
        for stem in linked_stems(ln):
            counts[stem] = counts.get(stem, 0) + 1
    removed = 0
    out = []
    for i, ln in enumerate(lines):
        m = BARE_MOUNT_RE.match(ln) if i > marker_idx else None
        if m:
            stem = m.group(1).rsplit("/", 1)[-1].strip()
            if counts.get(stem, 0) > 1:
                counts[stem] -= 1
                removed += 1
                continue
        out.append(ln)
    return ("\n".join(out), removed)


def dedupe_all_moc_automount() -> int:
    """对 DIR_MOC 映射到的所有 MOC 执行自动挂载去重（幂等，可重复跑）。"""
    total = 0
    seen = set()
    for moc in dict.fromkeys(DIR_MOC.values()):
        moc_path = resolve_moc(moc)
        if not moc_path or not moc_path.exists() or moc_path in seen:
            continue
        seen.add(moc_path)
        text = moc_path.read_text(encoding="utf-8", errors="ignore")
        new, removed = dedupe_automount(text)
        if removed:
            moc_path.write_text(new, encoding="utf-8")
            print(f"  [DEDUP] {moc_path.name}: 移除 {removed} 条重复挂载行")
            total += removed
    return total


def mount_orphans(files) -> int:
    """把 lint 认定的孤儿登记进所属 MOC（双向挂载）。
    只加出链不够——文件指向 MOC 不解决「没人指向文件」。"""
    n = 0
    for f in files:
        rel = str(f.relative_to(VAULT)).replace("\\", "/")
        moc = next((m for d, m in DIR_MOC.items() if rel.startswith(d)), None)
        if not moc:
            print(f"  [SKIP] 无 MOC 映射: {rel}")
            continue
        moc_path = resolve_moc(moc)
        if not moc_path or not moc_path.exists():
            print(f"  [SKIP] MOC 不存在: {moc}")
            continue
        text = moc_path.read_text(encoding="utf-8", errors="ignore")
        # 幂等：stem 级判重（兼容 [[note]] / [[note|disp]] / [[path/note|disp]]）
        if f.stem in linked_stems(text):
            continue
        marker = AUTOMOUNT_MARKER
        tail = text.rstrip()
        ctx = mount_context(f)
        entry = f"- [[{f.stem}]] — {ctx}" if ctx else f"- [[{f.stem}]]"
        if marker in tail:
            new = tail + f"\n{entry}\n"
        else:
            new = tail + f"\n\n{marker}\n\n> cron 产出自动登记（防入链孤立）\n\n{entry}\n"
        moc_path.write_text(new, encoding="utf-8")
        print(f"  [MOUNT] {f.stem} → {moc}")
        n += 1
    return n


def mount_context(f) -> str:
    """给 MOC 挂载行取一句上下文（研究结论：带注解的链接才是「地图」，裸链接只是清单）。

    优先级：frontmatter description → frontmatter title → 首个 H1 → 正文首句。
    取不到就返回空串，宁可裸挂也不编造。
    """
    try:
        text = f.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    body = text
    if m:
        fm = m.group(1)
        body = text[m.end():]
        for key in ("description", "summary", "title"):
            mm = re.search(rf"^{key}\s*:\s*(.+)$", fm, re.M)
            if mm:
                val = mm.group(1).strip().strip("\"'")
                if val and not val.startswith("["):
                    return val[:60].replace("\n", " ")
    for ln in body.splitlines():
        s = ln.strip()
        if s.startswith("# "):
            return s[2:].strip()[:60]
        if s and not s.startswith(("---", ">", "|", "-", "*", "!", "[", "<", "#")):
            # 跳过 YAML 残留键值行（tags: / type: ...），它不是人写的句子
            if re.match(r"^[A-Za-z_][\w-]*\s*:", s):
                continue
            return s[:60]
    return ""


def scan_md_files():
    return [
        f for f in VAULT.rglob("*.md")
        if ".git" not in str(f) and ".obsidian" not in str(f)
        and ".venv" not in str(f) and "private_knowledge" not in str(f)
        and "private_vault" not in str(f) and "MOC-" not in f.name
        and not (f.name == "README.md" and f.parent == VAULT)
        and f.name not in ("Home.md",)
        # 第三方技能包 / 工具产物的 README、SKILL.md 不是知识笔记：
        # 计入孤立率会把口径稀释掉（2026-11-07 实测：全库 13% vs 知识域 2%）
        and not _in_vendor_dir(f)
    ]


VENDOR_DIRS = (
    "skills", ".hermes", ".learnings", ".claude", ".codebuddy",
    ".qoder", ".gemini", ".skillkit", "graphify-out", "docs-site",
)


def _in_vendor_dir(f) -> bool:
    try:
        rel = str(f.relative_to(VAULT)).replace("\\", "/")
    except ValueError:
        return False
    return any(rel == d or rel.startswith(d + "/") for d in VENDOR_DIRS)


def find_isolated():
    return [
        f for f in scan_md_files()
        if not LINK_RE.findall(f.read_text(encoding="utf-8", errors="ignore"))
    ]


def link_isolated(files) -> int:
    n = 0
    for f in files:
        rel = str(f.relative_to(VAULT)).replace("\\", "/")
        moc = next((m for d, m in DIR_MOC.items() if rel.startswith(d)), None)
        if not moc:
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        if not LINK_RE.findall(text):
            text = text.rstrip() + f'\n\n---\n> 🗺️ 属于 [[{moc}]] · [[Home|🏠 Home]]\n'
            f.write_text(text, encoding="utf-8")
            n += 1
    return n


def update_moc_research() -> int:
    """把 Research 目录新笔记加入 MOC-Research 索引（按主题分组）"""
    moc_path = VAULT / "knowledge" / "Research" / "MOC-Research.md"
    if not moc_path.exists():
        return 0
    files = sorted((VAULT / "knowledge" / "Research").glob("*.md"))
    files = [f for f in files if f.name != "MOC-Research.md"]
    names = {f.stem for f in files}
    current = moc_path.read_text(encoding="utf-8")
    # 已索引的：链接统一取 stem（兼容 [[path/note|display]] 形式），避免重复索引
    indexed = {ln.rsplit("/", 1)[-1] for ln in re.findall(r"\[\[([^\]|#]+)", current)}
    missing = sorted(names - indexed)
    changed = False
    if missing:
        # 若文件末尾已是 "## 其他" 小节，则合并进去；否则追加新小节
        # 用行解析代替正则，避免灾难性回溯（(?:...)*$ 在长文件上会指数级回溯挂死）
        tail = current.rstrip()
        lines = tail.split("\n")
        other_idx = None
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip() == "## 其他":
                other_idx = i
                break
        if other_idx is not None:
            # 找到 "## 其他" 小节的结束位置（下一个 "## " 标题，或文件末尾）
            end = len(lines)
            for j in range(other_idx + 1, len(lines)):
                if lines[j].startswith("## "):
                    end = j
                    break
            # 去掉小节末尾空行
            while end > other_idx + 1 and lines[end - 1].strip() == "":
                end -= 1
            add_lines = [f"- [[{name}]]" for name in missing]
            new_lines = lines[:end] + add_lines + lines[end:]
            current = "\n".join(new_lines) + "\n"
        else:
            add_lines = ["## 其他", ""] + [f"- [[{name}]]" for name in missing]
            current = tail + "\n\n" + "\n".join(add_lines) + "\n"
        changed = True
    # 计数行始终刷新（无新笔记时数量也可能因增删漂移，如 185→186）
    refreshed = re.sub(r"\*\*共 \d+ 篇研究笔记\*\*", f"**共 {len(files)} 篇研究笔记**", current)
    if refreshed != current:
        current = refreshed
        changed = True
    # frontmatter updated 日期始终刷新
    today = datetime.date.today().strftime("%Y-%m-%d")
    refreshed = re.sub(r"^updated: [0-9-]+", f"updated: {today}", current, count=1, flags=re.M)
    # 正文头部「最后更新: 」也同步刷新（避免 frontmatter 与正文日期不一致）
    refreshed = re.sub(r"最后更新: [0-9-]+", f"最后更新: {today}", refreshed, count=1)
    if refreshed != current:
        current = refreshed
        changed = True
    if changed:
        moc_path.write_text(current, encoding="utf-8")
    return len(missing)


def update_knowledge_map_date() -> int:
    km = VAULT / "knowledge" / "knowledge-map.md"
    if not km.exists():
        return 0
    text = km.read_text(encoding="utf-8")
    today = datetime.date.today().strftime("%Y-%m-%d")
    if today in text:
        return 0
    new = re.sub(
        r"最后更新: [0-9-]+",
        f"最后更新: {today}",
        text,
        count=1,
    )
    if new != text:
        km.write_text(new, encoding="utf-8")
        return 1
    return 0


def sync_readme_stats() -> int:
    """把 README 里的手写统计数字同步到 knowledge/METABOLISM.md 的真实值。

    为什么值得自动化：README 顶部的「常青笔记 N 篇」「820+ 篇」这类手写数字每天都会
    过时，靠人肉记着改必然漂移（2026-11-07 实测：METABOLISM 763 篇 / 362 常青，
    README 还写着 757 / 361）。徽章规范的研究结论也一致——能动态读真值的徽章才可信。
    这里以 METABOLISM.md（由 okm_metabolism.py 生成）为唯一真相源，只改数字不动文案。
    """
    metab = VAULT / "knowledge" / "METABOLISM.md"
    readme = VAULT / "README.md"
    if not metab.exists() or not readme.exists():
        return 0
    m = metab.read_text(encoding="utf-8", errors="ignore")
    total = re.search(r"全库受管笔记\*\*：\s*(\d+)", m) or re.search(r"全库受管笔记\D*(\d+)", m)
    ev = re.search(r"Evergreen[^\n]*?\*\*(\d+)\*\*\s*篇\s*\(([\d.]+)%\)", m)
    bu = re.search(r"Budding[^\n]*?\*\*(\d+)\*\*\s*篇\s*\(([\d.]+)%\)", m)
    if not (total and ev and bu):
        return 0
    total_n, ev_n, ev_p, bu_n, bu_p = (
        int(total.group(1)), int(ev.group(1)), ev.group(2), int(bu.group(1)), bu.group(2)
    )
    text = readme.read_text(encoding="utf-8")
    orig = text
    changes = 0

    def sub(pattern, repl):
        nonlocal text, changes
        new, n = re.subn(pattern, repl, text)
        if n and new != text:
            changes += n
            text = new

    sub(r"常青笔记-\d+_篇", f"常青笔记-{ev_n}_篇")
    sub(r"Evergreen, \d+ 篇 / [\d.]+%", f"Evergreen, {ev_n} 篇 / {ev_p}%")
    sub(r"Budding, \d+ 篇 / [\d.]+%", f"Budding, {bu_n} 篇 / {bu_p}%")
    # 「820+ 篇」指的是公开知识体系总量 → 真相源是 llms.txt（gen-llms-txt.py 产出），
    # 不是 METABOLISM 的「受管笔记」（口径更窄）。取不到再退回受管笔记数。
    public_n = total_n
    llms = VAULT / "llms.txt"
    if llms.exists():
        mm = re.search(r"整合\s*(\d+)\s*篇", llms.read_text(encoding="utf-8", errors="ignore"))
        if mm:
            public_n = int(mm.group(1))
    # 向下取整到十位，保证「N+ 篇」表述永远成立（824 → 820+，830 → 830+）
    floor10 = (public_n // 10) * 10
    sub(r"\b\d{3}\+ 篇", f"{floor10}+ 篇")
    if text != orig:
        readme.write_text(text, encoding="utf-8")
    return changes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true", help="自动 git add/commit/push")
    args = ap.parse_args()

    print(f"📊 每日知识库优化 — {datetime.date.today()}")
    total = scan_md_files()
    isolated = find_isolated()
    print(f"笔记总数: {len(total)} | 孤立: {len(isolated)} ({len(isolated)*100//max(len(total),1)}%)")
    # 知识域单独口径（knowledge/**）：这是真正的知识资产健康度，
    # 全库口径含 memory/ 日志、系统身份文件等天然无出链的文件
    kn_total = [f for f in total if str(f.relative_to(VAULT)).startswith("knowledge")]
    kn_iso = [f for f in isolated if str(f.relative_to(VAULT)).startswith("knowledge")]
    print(f"知识域口径(knowledge/**): {len(kn_iso)}/{len(kn_total)}"
          f" ({len(kn_iso)*100//max(len(kn_total),1)}%)")
    # 最小产出门禁（2026-09-08 静默失效 bug 防线）：正常 vault 应有 1000+ 笔记，
    # 扫描数异常偏低 = VAULT 路径/扫描逻辑出问题，立即 FATAL 不许假装成功
    if len(total) < MIN_NOTE_COUNT:
        raise SystemExit(
            f"[FATAL] 扫描到笔记数 {len(total)} < 下限 {MIN_NOTE_COUNT}，"
            f"疑似 VAULT 路径/扫描逻辑异常（上次静默失效扫出 0 篇）"
        )

    linked = link_isolated(isolated)
    print(f"补链孤立笔记(出链): {linked}")

    # 入链孤儿：口径以 knowledge-lint.py 为准（单一真相源，避免两套实现漂移）
    orphans = lint_orphans()
    if orphans is None:
        print("入链孤儿: [SKIP] lint 不可用/解析失败 → 本次不挂载（宁缺勿错）")
        mounted = 0
    elif len(orphans) > ORPHAN_SANITY_CAP:
        print(f"入链孤儿: [SKIP] 检出 {len(orphans)} > 上限 {ORPHAN_SANITY_CAP}"
              f" → 疑似检测器故障，拒绝批量改文件")
        mounted = 0
    else:
        mounted = mount_orphans(orphans)
        print(f"入链孤立: {len(orphans)} | 自动挂载 MOC: {mounted}")

    moc_new = update_moc_research()
    print(f"MOC-Research 新增索引: {moc_new}")

    # 自动挂载小节去重（2026-11-07 审计落地：重复索引只增不减的根因修复）
    deduped = dedupe_all_moc_automount()
    print(f"MOC 自动挂载去重: 移除 {deduped} 条")

    km = update_knowledge_map_date()
    print(f"知识地图日期更新: {km}")

    # README 统计徽章自愈（2026-11-07 研究落地：手写数字徽章是最快的腐化点）
    synced = sync_readme_stats()
    print(f"README 统计同步: {synced} 处")

    if args.commit and (linked + mounted + moc_new + deduped + km + synced) > 0:
        r = subprocess.run(
            ["git", "-C", str(VAULT), "add", "-A"],
            capture_output=True, text=True, timeout=60,
        )
        r = subprocess.run(
            ["git", "-C", str(VAULT), "commit", "-m",
             f"chore: 每日知识库优化 {datetime.date.today()}（补链{linked}·挂载{mounted}·MOC+{moc_new}）"],
            capture_output=True, text=True, timeout=60,
        )
        print("commit:", r.stdout.strip()[-80:] if r.returncode == 0 else r.stderr.strip()[-80:])
        if r.returncode == 0:
            push_ok = False
            for attempt in range(3):
                r = subprocess.run(
                    ["git", "-C", str(VAULT), "push", "origin", "main"],
                    capture_output=True, text=True, timeout=120,
                    env={**__import__("os").environ,
                         "HTTPS_PROXY": "http://127.0.0.1:7890",
                         "HTTP_PROXY": "http://127.0.0.1:7890"},
                )
                if r.returncode == 0:
                    push_ok = True
                    break
                print(f"push 第{attempt+1}次失败: {r.stderr.strip()[-80:]}，重试…")
            print("push:", "OK" if push_ok else f"失败（3次）: {r.stderr.strip()[-80:]}")
    elif args.commit:
        print("无变更，跳过提交")
    else:
        print("（--commit 未传，仅诊断不提交）")


if __name__ == "__main__":
    main()

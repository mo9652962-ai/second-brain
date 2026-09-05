"""每日知识库自动优化脚本（second-brain vault）
1. 扫描新增孤立笔记（无 [[] 链接）→ 按目录补链所属 MOC/Home
2. MOC-Research 增量更新（Research 目录新笔记加入索引）
3. 知识地图日期更新
4. 输出变更报告（stdout → cron 注入 agent prompt）

用法: python scripts/daily_vault_optimize.py [--commit]
"""
import argparse
import datetime
import pathlib
import re
import subprocess
import sys

VAULT = pathlib.Path(r"C:\Users\31954\.openclaw\workspace")

DIR_MOC = {
    "knowledge/Research": "MOC-Research",
    "knowledge/Dev": "MOC-Dev",
    "knowledge/Hardware": "MOC-Hardware",
    "knowledge/Productivity": "MOC-Productivity",
    "knowledge/Security": "MOC-Security",
    "knowledge/Finance": "MOC-Finance",
    "knowledge/SOP": "knowledge-map",
    "knowledge/Projects": "MOC-Projects",
    "knowledge/Creative": "knowledge-map",
    "knowledge/Archive": "knowledge-map", "knowledge/Daily": "knowledge-map",
    "knowledge/cards": "knowledge-map",
    # 无独立 MOC 的域 → 挂到 MOC-Inbox（待接入/孤立审阅入口）
    "knowledge/AI": "MOC-Inbox",
    "knowledge/Content": "MOC-Inbox",
    "knowledge/Education": "MOC-Inbox",
    "knowledge/Development": "MOC-Inbox",
    "knowledge/gaming": "MOC-Inbox",
    "knowledge/META": "MOC-Inbox",
    "knowledge/Product": "MOC-Inbox",
    "memory": "knowledge-map", "concepts": "knowledge-map",
    "research": "MOC-Research", "docs": "knowledge-map",
    "health": "knowledge-map", "playbooks": "knowledge-map",
    "portfolio": "knowledge-map", "projects": "knowledge-map",
    "templates": "knowledge-map", "traces": "knowledge-map",
    "system": "knowledge-map",
}

LINK_RE = re.compile(r"\[\[([^\]|#]+)")


def scan_md_files():
    return [
        f for f in VAULT.rglob("*.md")
        if ".git" not in str(f) and ".obsidian" not in str(f)
        and ".venv" not in str(f) and "MOC-" not in f.name
        and not (f.name == "README.md" and f.parent == VAULT)
        and f.name not in ("Home.md",)
    ]


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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true", help="自动 git add/commit/push")
    args = ap.parse_args()

    print(f"📊 每日知识库优化 — {datetime.date.today()}")
    total = scan_md_files()
    isolated = find_isolated()
    print(f"笔记总数: {len(total)} | 孤立: {len(isolated)} ({len(isolated)*100//max(len(total),1)}%)")

    linked = link_isolated(isolated)
    print(f"补链孤立笔记: {linked}")

    moc_new = update_moc_research()
    print(f"MOC-Research 新增索引: {moc_new}")

    km = update_knowledge_map_date()
    print(f"知识地图日期更新: {km}")

    if args.commit and (linked + moc_new + km) > 0:
        r = subprocess.run(
            ["git", "-C", str(VAULT), "add", "-A"],
            capture_output=True, text=True, timeout=60,
        )
        r = subprocess.run(
            ["git", "-C", str(VAULT), "commit", "-m",
             f"chore: 每日知识库优化 {datetime.date.today()}（补链{linked}·MOC+{moc_new}）"],
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

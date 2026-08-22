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
    if not missing:
        return 0
    # 若文件末尾已是 "## 其他" 小节，则合并进去；否则追加新小节
    # 避免每次运行都追加一个 "## 其他" 头
    tail = current.rstrip()
    m = re.search(r"(## 其他\s*\n(?:- \[\[[^\n]*\]\]\s*\n?)*)$", tail)
    if m:
        add_lines = "".join(f"- [[{name}]]\n" for name in missing)
        current = tail[: m.start()] + m.group(1).rstrip() + "\n" + add_lines + "\n"
    else:
        add_lines = ["## 其他", ""] + [f"- [[{name}]]" for name in missing]
        current = tail + "\n\n" + "\n".join(add_lines) + "\n"
    # 更新计数行
    current = re.sub(r"\*\*共 \d+ 篇研究笔记\*\*", f"**共 {len(files)} 篇研究笔记**", current)
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

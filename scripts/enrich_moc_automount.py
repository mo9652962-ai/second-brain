"""给 MOC「## 自动挂载」小节里的裸链接补一句上下文注解。

背景（2026-11-07 研究结论）：MOC 的价值不在「列了哪些链接」，而在「每条链接旁的一句
说明」——带注解的链接是地图，裸链接只是清单（Nick Milo / dsebastien / Eric Ma 三家
Obsidian 结构实践的共同点）。cron 自动挂载早期只写 `- [[stem]]`，本脚本把历史遗留的
裸行补成 `- [[stem]] — 一句话`，与 daily_vault_optimize 的新写入格式对齐。

幂等：已有注解的行不动；找不到笔记或无上下文可取的也保持原样（宁缺勿造）。

用法: python scripts/enrich_moc_automount.py [--commit]
"""
import argparse
import pathlib
import re
import subprocess
import sys

VAULT = pathlib.Path(__file__).resolve().parent.parent
AUTOMOUNT_MARKER = "## 自动挂载"
BARE_RE = re.compile(r"^(\s*-\s*\[\[([^\]|#]+)\]\])$")


def mount_context(path) -> str:
    """同 daily_vault_optimize.mount_context：description → title → H1 → 首句。"""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
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
            if re.match(r"^[A-Za-z_][\w-]*\s*:", s):
                continue
            return s[:60]
    return ""


def build_index():
    idx = {}
    for f in VAULT.rglob("*.md"):
        s = str(f)
        if ".git" in s or ".venv" in s or "node_modules" in s:
            continue
        idx.setdefault(f.stem, f)
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true")
    args = ap.parse_args()

    idx = build_index()
    changed_files = 0
    enriched = 0
    for moc in sorted(VAULT.rglob("MOC-*.md")):
        if ".git" in str(moc):
            continue
        lines = moc.read_text(encoding="utf-8", errors="ignore").split("\n")
        try:
            start = next(i for i, l in enumerate(lines) if l.strip() == AUTOMOUNT_MARKER)
        except StopIteration:
            continue
        out = lines[: start + 1]
        touched = 0
        for ln in lines[start + 1:]:
            m = BARE_RE.match(ln)
            if m:
                stem = m.group(2).rsplit("/", 1)[-1].strip()
                target = idx.get(stem)
                ctx = mount_context(target) if target else ""
                if ctx:
                    out.append(f"{m.group(1)} — {ctx}")
                    touched += 1
                    continue
            out.append(ln)
        if touched:
            moc.write_text("\n".join(out), encoding="utf-8")
            print(f"  [ENRICH] {moc.name}: +{touched} 条注解")
            changed_files += 1
            enriched += touched

    print(f"共 {enriched} 条裸挂载补注解（{changed_files} 个 MOC）")
    if args.commit and enriched:
        subprocess.run(["git", "-C", str(VAULT), "add", "-A"], check=False)
        r = subprocess.run(
            ["git", "-C", str(VAULT), "commit", "-m",
             f"chore(moc): 自动挂载裸链接补上下文注解 {enriched} 条"],
            capture_output=True, text=True,
        )
        print("commit:", "OK" if r.returncode == 0 else r.stderr.strip()[-120:])
    return 0


if __name__ == "__main__":
    sys.exit(main())

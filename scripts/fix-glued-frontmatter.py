"""修复粘连的 frontmatter 闭合符（`status: fresh---` → `status: fresh` + 独立 `---`）。

背景：历史批量生成产生 80 个文件，其 frontmatter 闭合符粘连在最后一个字段行尾。
knowledge-lint.py 已能检出（2026-09-26 修复假阴性盲区），本脚本负责修复。

用法: python scripts/fix-glued-frontmatter.py [--apply]   # 默认 dry-run

安全约束：
- 只处理以 `---` 开头的文件
- 只在「首个独立 --- 之前」的区间内寻找粘连行（真正的 frontmatter 区）
- 行尾 --- 前引号不成对时跳过（避免误伤 title: "A --- B"）
- 保留每行原始行尾（CRLF 保持 CRLF，不扁平化为 LF）
- 幂等：修完再跑应为 0 处
"""
import argparse
import pathlib

VAULT = pathlib.Path(__file__).resolve().parent.parent
ROOT = VAULT / "knowledge"


def find_glued(lines: list[str]) -> int | None:
    """返回粘连行的下标；无粘连或已正常闭合则返回 None。"""
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        s = lines[i].strip()
        if s == "---":
            return None                 # 正常闭合
        if s.endswith("---"):
            return i
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="实际写入（默认仅预览）")
    args = ap.parse_args()

    fixed, skipped = [], []
    for f in sorted(ROOT.rglob("*.md")):
        # read_bytes().decode() 而非 read_text()：后者默认做通用换行转换，
        # 会把 \r\n 静默变成 \n，导致下面的行尾保留逻辑永远失效（实测把 CRLF 扁平化）
        lines = f.read_bytes().decode("utf-8", "replace").split("\n")
        i = find_glued(lines)
        if i is None:
            continue

        cr = "\r" if lines[i].endswith("\r") else ""
        body = lines[i].rstrip()[:-3]
        # 引号安全：`---` 前的引号必须成对，否则可能落在字符串值内部
        if body.count('"') % 2 or body.count("'") % 2:
            skipped.append((f, "引号不成对"))
            continue

        lines[i] = body.rstrip(" \t") + cr
        lines.insert(i + 1, "---" + cr)
        if args.apply:
            # 逐字节写入并保留原行尾（不可用 newline=""，否则 CRLF 会被扁平化）
            f.write_bytes("\n".join(lines).encode("utf-8"))
        fixed.append(f.relative_to(ROOT))

    tag = "APPLIED" if args.apply else "DRY-RUN"
    print(f"{tag} 修复 {len(fixed)} 个文件")
    for p in fixed:
        print("  ", p)
    for p, why in skipped:
        print(f"  [SKIP] {p} ({why})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

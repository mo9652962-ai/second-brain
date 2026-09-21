#!/usr/bin/env python3
"""tag-fix: 精确规范化标签大小写（只改 frontmatter tags 字段与行内 #tag，不动标题/正文/代码块）。

用法: python tag-fix.py <vault_root> [--apply]
不传 --apply = dry-run，只报告将修改的文件与替换。
"""
import re, sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "knowledge").resolve()
APPLY = "--apply" in sys.argv
SKIP = {".git", ".obsidian", ".trash", "Archive", "META"}
files = [f for f in root.rglob("*.md") if not any(p in SKIP for p in f.relative_to(root).parts)]

# 规范化映射: 原 token -> 目标 (仅标签上下文)
MAP = {
    "AI-agent": "ai-agent",
    "CLI": "cli",
    "Codex": "codex",
    "GitHub": "github",
    "Go": "go",
    "MCP": "mcp",
    "RL": "rl",
    "UI": "ui",
    "vibecoding": "vibe-coding",
}
TAG_TOKENS = re.compile(r"^(?:[ \t]*)([A-Za-z0-9_\-/]+)")
CODE_SPAN_RE = re.compile(r"`[^`]*`")
FENCE_RE = re.compile(r"```.*?```", flags=re.S)

def norm_token(tok):
    return MAP.get(tok)

def fix_fm_tags_line(line):
    """处理一行 `tags: [a, b]` 或 `tags:\n- x` 中的 token。"""
    # inline list 形式
    m = re.search(r"^tags:\s*\[(.*)\]$", line)
    if m:
        body = m.group(1)
        def rep(tok):
            t = tok.strip()
            return tok.replace(t, norm_token(t), 1) if norm_token(t) else tok
        # 逐 token 替换
        new_parts = []
        changed = False
        for part in body.split(","):
            p = part.strip()
            n = norm_token(p)
            if n and n != p:
                new_parts.append(n)
                changed = True
            else:
                new_parts.append(p)
        if changed:
            return "tags: [" + ", ".join(new_parts) + "]", True
        return line, False
    # YAML list 形式: `- token` 或行内 `- token`
    m2 = re.match(r"^( *-\s*)(\S+)(.*)$", line)
    if m2:
        indent, tok, rest = m2.group(1), m2.group(2), m2.group(3)
        n = norm_token(tok)
        if n and n != tok:
            return f"{indent}{n}{rest}", True
    return line, False

def fix_file(f, text):
    """返回 (new_text, changed_count)。保留原文件换行风格（CRLF/LF）。"""
    use_crlf = "\r\n" in text
    lines = [l.rstrip("\r") for l in text.split("\n")]
    changed = 0
    in_fence = False
    in_fm = text.startswith("---")
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if in_fm and i == 0:
            continue
        if in_fm and stripped == "---":
            in_fm = False
            continue
        if in_fm and stripped.startswith("tags:"):
            new_line, ch = fix_fm_tags_line(line)
            if ch:
                lines[i] = new_line
                changed += ch
            continue
        if in_fm and stripped.startswith("- "):
            # YAML list 式 tags: `- token`
            new_line, ch = fix_fm_tags_line(line)
            if ch:
                lines[i] = new_line
                changed += ch
            continue
        # 行内 #tag（含正文非 frontmatter 区）
        if not in_fence:
            def repl(m):
                nonlocal changed
                tag = m.group(1)
                n = norm_token(tag)
                if n and n != tag:
                    changed += 1
                    return "#" + n
                return m.group(0)
            # 只替换不在 code span 内的 #tag（(?![\w-]) 防止切开 GitHub-Weekly 这类连字符标签）
            tag_alt = "|".join(re.escape(k) for k in MAP)
            tag_re = re.compile(r"#(" + tag_alt + r")(?![\w-])")
            new_line = ""
            last = 0
            for sm in CODE_SPAN_RE.finditer(line):
                seg = line[last:sm.start()]
                seg = tag_re.sub(repl, seg)
                new_line += seg + sm.group(0)
                last = sm.end()
            seg = line[last:]
            seg = tag_re.sub(repl, seg)
            new_line += seg
            if new_line != line:
                lines[i] = new_line
    new_text = "\n".join(lines)
    if use_crlf:
        new_text = new_text.replace("\n", "\r\n")
    return new_text, changed

total_files = 0
total_changes = 0
for f in files:
    with open(f, encoding="utf-8", errors="replace", newline="") as fh:
        text = fh.read()
    new_text, changed = fix_file(f, text)
    if changed:
        total_files += 1
        total_changes += changed
        rel = f.relative_to(root)
        print(f"  {rel}  (+{changed})")
        if APPLY:
            f.write_bytes(new_text.encode("utf-8"))
print(f"\n{'APPLIED' if APPLY else 'DRY-RUN'}: {total_files} files, {total_changes} changes")

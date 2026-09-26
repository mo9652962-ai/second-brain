"""frontmatter 判据的回归测试（knowledge-lint + fix-glued-frontmatter）。

背景：2026-09-26 发现 lint 的「粘连闭合符」判据有假阴性盲区——它只问「前 20 行
有没有任意独立 ---」，于是**正文的水平分隔线冒充了 frontmatter 闭合符**，静默
漏报 80 个文件（Research 49 / cards 27 / Archive 3 / Security 1），且报告 Glued=0。

本文件把当时的 ad-hoc 验证固化下来，防止判据再次漂移。核心是
`test_blind_spot_would_have_failed_old_logic`——它断言旧判据在该用例上返回
「未粘连」，即证明这些回归测试**非空转**。

运行: python -m pytest tests/test_frontmatter_scan.py -q
"""
import importlib.util
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINT_PATH = ROOT / "knowledge" / "META" / "scripts" / "knowledge-lint.py"


def _load(name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


lint = _load("knowledge_lint", LINT_PATH)
fixer = _load("fix_glued", ROOT / "scripts" / "fix-glued-frontmatter.py")
scan = lint.scan_frontmatter

# ---------- 用例语料 ----------

# 真实世界的形状：第 3 行粘连闭合符，第 7 行正文有水平分隔线（旧判据的盲区）
BLIND_SPOT = "---\ntags: [x]\nstatus: fresh---\n\n# A\n\n---\n\nbody\n"
# 粘连但正文没有横线（旧判据也能抓）
SIMPLE_GLUED = "---\ntags: [x]\nstatus: fresh---\n\n# B\n\nbody\n"
# 正常闭合，且正文有横线（不得误报）
CLEAN = "---\ntags: [x]\nstatus: active\n---\n\n# C\n\n---\n\nbody\n"
# 只有开头 ---，从未闭合
NEVER_CLOSED = "---\ntags: [x]\nstatus: active\n\n# D\n\nbody\n"


class TestScanFrontmatter:
    @pytest.mark.parametrize("text", [BLIND_SPOT, SIMPLE_GLUED, NEVER_CLOSED],
                             ids=["blind_spot", "simple_glued", "never_closed"])
    def test_flags_glued(self, text):
        glued, _ = scan(text.split("\n"))
        assert glued is True

    def test_clean_is_not_glued(self):
        glued, _ = scan(CLEAN.split("\n"))
        assert glued is False

    def test_clean_reports_close_index(self):
        glued, idx = scan(CLEAN.split("\n"))
        assert not glued
        assert CLEAN.split("\n")[idx].strip() == "---"

    def test_blind_spot_would_have_failed_old_logic(self):
        """反事实：旧判据在该用例上判「已闭合」→ 证明上面的回归测试非空转。"""
        lines = BLIND_SPOT.split("\n")
        old_closed = any(l.strip() == "---" for l in lines[1:20])
        assert old_closed is True, "旧判据应当被正文横线骗过"
        assert scan(lines)[0] is True, "新判据必须抓到它"


class TestFixerFindGlued:
    def test_locates_glued_line(self):
        assert fixer.find_glued(BLIND_SPOT.split("\n")) == 2

    @pytest.mark.parametrize("text", [CLEAN, "plain text, no frontmatter\n"])
    def test_ignores_clean_and_plain(self, text):
        assert fixer.find_glued(text.split("\n")) is None

    def test_agrees_with_lint(self):
        """凡 lint 判粘连的，fixer 必须给出裁决（可修 or 需人工）——不许静默漏过。"""
        for text in (BLIND_SPOT, SIMPLE_GLUED, CLEAN, NEVER_CLOSED):
            lines = text.split("\n")
            glued, _ = scan(lines)
            handled = fixer.find_glued(lines) is not None or fixer.needs_manual(lines)
            assert handled == glued, f"lint={glued} 但 fixer 未处理: {text!r}"


class TestRepair:
    @staticmethod
    def _repair(tmp_path, body: str, name="n.md"):
        p = tmp_path / name
        p.write_bytes(body.encode("utf-8"))
        lines = p.read_bytes().decode("utf-8").split("\n")
        i = fixer.find_glued(lines)
        assert i is not None
        cr = "\r" if lines[i].endswith("\r") else ""
        lines[i] = lines[i].rstrip()[:-3].rstrip(" \t") + cr
        lines.insert(i + 1, "---" + cr)
        p.write_bytes("\n".join(lines).encode("utf-8"))
        return p

    def test_crlf_preserved(self, tmp_path):
        """回归：read_text() 的通用换行转换曾把 CRLF 静默扁平化为 LF。"""
        p = self._repair(tmp_path, "---\r\ntags: [x]\r\nstatus: fresh---\r\n\r\n# A\r\n\r\nbody\r\n")
        raw = p.read_bytes()
        assert b"status: fresh\r\n---\r\n" in raw
        assert raw.count(b"\n") - raw.count(b"\r\n") == 0, "出现了孤立 LF = 行尾被改写"

    def test_lf_stays_lf(self, tmp_path):
        p = self._repair(tmp_path, "---\ntags: [x]\nupdated: 2026-08-31---\n\n# B\n\nbody\n")
        raw = p.read_bytes()
        assert b"updated: 2026-08-31\n---\n" in raw
        assert b"\r" not in raw

    def test_net_one_line_added(self, tmp_path):
        src = "---\r\ntags: [x]\r\nstatus: fresh---\r\n\r\n# A\r\n\r\nbody\r\n"
        p = self._repair(tmp_path, src)
        assert len(p.read_bytes().split(b"\r\n")) - len(src.encode().split(b"\r\n")) == 1


class TestVaultClean:
    """真实 vault 应保持干净（修复后回归 0）。"""

    def test_no_glued_in_vault(self):
        bad = []
        for f in sorted((ROOT / "knowledge").rglob("*.md")):
            if scan(f.read_bytes().decode("utf-8", "replace").split("\n"))[0]:
                bad.append(str(f.relative_to(ROOT)))
        assert bad == [], f"仍有粘连 frontmatter: {bad[:5]}"

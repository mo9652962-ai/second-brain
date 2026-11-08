"""README 库存数字自愈的回归测试（daily_vault_optimize.sync_readme_inventory）。

背景：2026-11-08 实测 README「📊 仓库统计」代码块写 969 文件 / 824 篇 md / 733 篇
knowledge / 29 篇技能文档，git 真实值 996 / 844 / 753 / 30 —— 徽章那半边有自愈，
代码块这半边全靠手写，长期漂移无人管。

更隐蔽的坑：`git ls-files` 默认把中文路径转义成 `"knowledge/AI/\345\205..."`，
带引号的条目 `endswith(".md")` 为假，于是 223 个中文名文件被静默漏计（844 → 621）。
本文件把这两个坑都钉死：一条断言 NUL 解析后不再有转义条目，一条断言 README
声明的文件数等于 git 跟踪文件数。

运行: python -m pytest tests/test_readme_inventory.py -q
"""
import importlib.util
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "daily_vault_optimize.py"


def _load():
    spec = importlib.util.spec_from_file_location("dvo_test", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_git_ls_does_not_return_quoted_paths():
    """-z 解析后不应出现 git 转义引号条目（旧实现 223 个中文文件全被漏掉）。"""
    dvo = _load()
    files = dvo._git_ls()
    assert files, "git ls-files 返回空，环境异常"
    quoted = [f for f in files if f.startswith('"') or f.endswith('"')]
    assert not quoted, f"仍存在转义路径条目: {quoted[:3]}"
    assert any("\u4e00" <= ch <= "\u9fff" for f in files for ch in f), \
        "没有任何中文路径 → 说明测试样本与真实库不符"


def test_md_count_matches_shell_truth():
    """md 计数必须与 `git ls-files '*.md'` 的行数一致（旧实现少 223）。"""
    dvo = _load()
    files = dvo._git_ls()
    md = [f for f in files if f.lower().endswith(".md")]
    r = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "*.md"],
        capture_output=True, text=True, timeout=90,
    )
    assert r.returncode == 0, r.stderr
    shell_n = len([line for line in r.stdout.splitlines() if line.strip()])
    assert len(md) == shell_n, f"python 口径 {len(md)} != git 口径 {shell_n}"


def test_readme_declares_real_file_count():
    """README 声明的跟踪文件数必须等于 git 真实值（并顺带自愈）。"""
    dvo = _load()
    dvo.sync_readme_inventory()
    real = len(dvo._git_ls())
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    m = re.search(r"/ (\d+) 个文件", text)
    assert m, "README 里找不到「/ N 个文件」统计行"
    assert int(m.group(1)) == real, f"README 声明 {m.group(1)}，真实 {real}"


def test_sync_is_idempotent():
    """连续两次同步，第二次必须是 0 处改动（否则说明替换模式在自我打架）。"""
    dvo = _load()
    dvo.sync_readme_inventory()
    assert dvo.sync_readme_inventory() == 0

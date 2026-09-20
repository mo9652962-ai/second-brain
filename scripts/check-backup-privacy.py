"""check-backup-privacy.py — 备份包隐私门禁

背景（2026-09-20 实际事故）：
  knowledge-lint 技能的备份命令裸用 `tar -czf ... knowledge/`，
  把 .gitignore 里的私有文档（学业规划路线图：学校名/学院/专业/目标院校）
  打进了 10 个 .backup/*.tar.gz。其中 4 个被 git 跟踪 → 已推到公开仓库。

设计要点：
  敏感词表 **不硬编码在本文件**（否则脚本自身就成了泄露源，且会被
  git filter-repo 的 --replace-text 一并改写导致检测失效）。
  改为从 `scripts/private-patterns.txt`（gitignored）加载。

用法：
  python scripts/check-backup-privacy.py          # 全量检查
  python scripts/check-backup-privacy.py --quiet  # 仅返回退出码

退出码：0 = 通过；1 = 存在泄露风险
"""
import glob
import os
import subprocess
import sys
import tarfile

# 敏感词表文件（gitignored；缺失时降级为通用检查）
PATTERN_FILE = os.path.join("scripts", "private-patterns.txt")


def load_patterns() -> list:
    """从外部文件加载敏感词（每行一个，# 开头为注释）"""
    if not os.path.exists(PATTERN_FILE):
        return []
    patterns = []
    with open(PATTERN_FILE, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#"):
                patterns.append(line)
    return patterns


def check_tarball(path: str, patterns: list) -> list:
    """返回该 tar.gz 的问题列表（空=干净）"""
    issues = []
    if not patterns:
        return issues
    try:
        with tarfile.open(path, "r:gz") as tf:
            for member in tf.getmembers():
                name = member.name
                for pat in patterns:
                    if pat in name:
                        issues.append(f"私有文件名命中: {name}")
                        break
                if member.isfile() and member.size < 2_000_000:
                    if name.endswith((".md", ".txt", ".json", ".py", ".yml", ".yaml")):
                        try:
                            data = tf.extractfile(member).read().decode("utf-8", "replace")
                        except Exception:
                            continue
                        for pat in patterns:
                            if pat in data:
                                issues.append(f"私有内容命中: {name}")
                                break
    except Exception as exc:
        issues.append(f"无法读取: {exc}")
    return issues


def check_git_tracked() -> list:
    """检查 .backup/ 是否有文件被 git 跟踪（备份永远不该进版本库）"""
    issues = []
    try:
        proc = subprocess.run(
            ["git", "-c", "core.quotePath=false", "ls-files", ".backup"],
            capture_output=True,
        )
        out = proc.stdout.decode("utf-8", "replace")
        for t in [line for line in out.splitlines() if line.strip()]:
            issues.append(f".backup 被 git 跟踪（备份不应入库）: {t}")
    except Exception:
        pass
    return issues


def main() -> int:
    quiet = "--quiet" in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    patterns = load_patterns()
    if not patterns and not quiet:
        print(f"⚠️ 未找到敏感词表 {PATTERN_FILE}，仅做 .backup 跟踪检查")

    all_issues = []

    tarballs = sorted(glob.glob(".backup/**/*.tar.gz", recursive=True))
    if not quiet:
        print(f"🔍 扫描 {len(tarballs)} 个备份包（{len(patterns)} 条敏感词）…")
    for tb in tarballs:
        issues = check_tarball(tb, patterns)
        if issues:
            all_issues.append((tb, issues))

    git_issues = check_git_tracked()
    if git_issues:
        all_issues.append(("<git index>", git_issues))

    if all_issues:
        if not quiet:
            print("\n🔴 发现隐私泄露风险：\n")
            for target, issues in all_issues:
                print(f"  📦 {target}")
                for issue in issues[:5]:
                    print(f"      • {issue}")
                if len(issues) > 5:
                    print(f"      … 还有 {len(issues) - 5} 项")
                print()
            print("  修复：从 git 移除（git rm --cached）+ 用 git ls-files 驱动重建备份")
        return 1

    if not quiet:
        print(f"✅ 备份隐私检查通过（{len(tarballs)} 个包，0 泄露）")
    return 0


if __name__ == "__main__":
    sys.exit(main())

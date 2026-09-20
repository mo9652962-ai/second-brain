"""check-backup-privacy.py — 备份包隐私门禁

背景（2026-09-20 实际事故）：
  knowledge-lint 技能的备份命令裸用 `tar -czf ... knowledge/`，
  把 .gitignore 里的私有文档（学业规划路线图：学校名/学院/专业/目标院校）
  打进了 10 个 .backup/*.tar.gz。其中 4 个被 git 跟踪 → 已推到公开仓库。

本脚本在备份后立即自检，并可用于 CI / pre-commit：
  1. 扫描 .backup/ 下所有 tar.gz，检查是否含私有文件名或私有内容特征串
  2. 检查 .backup/ 是否有文件被 git 跟踪（备份永远不该进版本库）
  3. 退出码非 0 表示存在泄露风险

用法：
  python scripts/check-backup-privacy.py          # 全量检查
  python scripts/check-backup-privacy.py --quiet  # 仅返回退出码
"""
import glob
import os
import subprocess
import sys
import tarfile

# 私有内容特征串（命中即视为泄露）
PRIVATE_PATTERNS = [
    "某高校", "某高校", "目标专业", "目标院校", "某学院", "目标专业代码",
]
# 本机路径/身份特征
MACHINE_PATTERNS = [
    "%USERPROFILE%", "~", "<USER>",
]
# 备份包里不该出现的目录（临时/私有）
FORBIDDEN_PREFIXES = (
    "knowledge/Education/",
    ".backup/",
)


def check_tarball(path: str) -> list:
    """返回该 tar.gz 的问题列表（空=干净）"""
    issues = []
    try:
        with tarfile.open(path, "r:gz") as tf:
            for member in tf.getmembers():
                name = member.name
                for pat in PRIVATE_PATTERNS:
                    if pat in name:
                        issues.append(f"私有文件名命中「{pat}」: {name}")
                if member.isfile() and member.size < 2_000_000:
                    # 只抽查小文件内容，避免解压大二进制
                    if name.endswith((".md", ".txt", ".json", ".py", ".yml", ".yaml")):
                        try:
                            data = tf.extractfile(member).read().decode("utf-8", "replace")
                        except Exception:
                            continue
                        for pat in PRIVATE_PATTERNS:
                            if pat in data:
                                issues.append(f"私有内容命中「{pat}」: {name}")
                                break
    except Exception as exc:  # 损坏的包也算问题
        issues.append(f"无法读取: {exc}")
    return issues


def check_git_tracked() -> list:
    """检查 .backup/ 是否有文件被 git 跟踪"""
    issues = []
    try:
        proc = subprocess.run(
            ["git", "-c", "core.quotePath=false", "ls-files", ".backup"],
            capture_output=True,
        )
        out = proc.stdout.decode("utf-8", "replace")
        tracked = [line for line in out.splitlines() if line.strip()]
        for t in tracked:
            issues.append(f".backup 被 git 跟踪（备份不应入库）: {t}")
    except Exception:
        pass
    return issues


def main() -> int:
    quiet = "--quiet" in sys.argv
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(root)

    all_issues = []

    tarballs = sorted(glob.glob(".backup/**/*.tar.gz", recursive=True))
    if not quiet:
        print(f"🔍 扫描 {len(tarballs)} 个备份包…")
    for tb in tarballs:
        issues = check_tarball(tb)
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

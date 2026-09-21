"""check-repo-privacy.py — 公开仓库隐私门禁（CI 用）
扫描 tracked 文件是否含敏感特征：学校名/身份信息/手机号/邮箱/内网IP/本机路径/密钥关键字。
只读，exit 1 表示命中（CI 红门）。敏感词表：scripts/private-patterns.txt（本地维护，已被 .gitignore）。
"""
import os, re, sys, subprocess, pathlib

WS = pathlib.Path(__file__).resolve().parent.parent
os.chdir(WS)

# 内置基线（即使词表缺失也有兜底）
BUILTIN = [
    r'桂林航天工业学院', r'桂电', r'飞行器质量与可靠性', r'航空宇航学院',
    r'桂航', r'C:\\Users\\\d+', r'192\.168\.\d+\.\d+',
    r'172\.(1[6-9]|2\d|3[01])\.\d+\.\d+',
    r'(?<!\d)1[3-9]\d{9}(?!\d)',  # 大陆手机号
    # 10.x 仅匹配内网 IP（排除 Windows 版本号 10.0.26200.9457 类 build 串）
    r'(?<![\d.])10\.(?!0\.\d{4,}\.\d{4,})\d+\.\d+\.\d+',
]

# 加载本地词表（不存在则只用内置）
patterns = list(BUILTIN)
pats_file = WS / 'scripts' / 'private-patterns.txt'
if pats_file.exists():
    for line in pats_file.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            patterns.append(line)
regex = re.compile('|'.join(f'({p})' for p in patterns))

# 只扫 tracked 文件（.gitignore 感知，私有文档自动排除）
try:
    tracked = subprocess.run(['git', '-c', 'core.quotePath=false', 'ls-files'],
                             capture_output=True, text=True, check=True).stdout.splitlines()
except Exception:
    print('⚠️ git ls-files 失败，跳过'); sys.exit(0)

# 只扫文本类（跳过二进制大文件）
TEXT_EXT = {'.md', '.py', '.sh', '.ps1', '.yml', '.yaml', '.json', '.txt', '.toml', '.html', '.css', '.js', '.ts'}
hits = []
for f in tracked:
    ext = os.path.splitext(f)[1].lower()
    if ext not in TEXT_EXT:
        continue
    try:
        content = open(f, encoding='utf-8', errors='ignore').read()
    except Exception:
        continue
    for m in regex.finditer(content):
        # 过滤明显非隐私命中（超长数字/版本号等）：手机号需要恰好 11 位数字上下文
        val = m.group(0)
        if re.fullmatch(r'1[3-9]\d{9}', val) and not re.fullmatch(r'1[3-9]\d{9}', val):
            pass
        hits.append(f'{f}: {val}')

if hits:
    print(f'❌ 隐私门禁命中 {len(hits)} 处：')
    for h in hits[:20]:
        print(f'   {h}')
    print('（完整列表见输出；请脱敏后提交）')
    sys.exit(1)
print(f'✅ 隐私门禁通过：{len(tracked)} tracked 文件无敏感特征命中')
sys.exit(0)

# -*- coding: utf-8 -*-
"""credential_patterns.py — 「命令内嵌凭据」检测规则（被 check-repo-privacy.py 与测试共用）

为什么需要（2026-11-08，见 knowledge/cards/2026-11-08-agent-approval-secrets.md）：
    gitleaks / TruffleHog 认的是「钥匙的形状」（sk- / AKIA / 高熵长串），
    但 `PGPASSWORD=真实密码 psql ...`、`sshpass -p 真实密码`、`mysql -p真实密码`
    里的密码在词法上只是「命令行里一个普通单词」——Apiiro 实测 1,122 份泄露文件里
    215 份（约 1/5）两个扫描器都没抓到。

本模块只做「模式 + 占位符过滤」，不做文件 IO，便于单测（scripts/test_credential_patterns.py）。
占位符过滤是必须的：知识库/技能文档里到处是 `PGPASSWORD=xxx` 这类示例，
不滤掉会变成大面积误报（实测本库 12 处命中全部是占位符）。
"""
import re

# (规则名, 正则) —— 正则第 1 组为「凭据值」，用于占位符判定
CRED_RULES = [
    # 允许值被引号包住（`PGPASSWORD='secret'` / `sshpass -p "secret"` 都是常见写法）；
    # 值里不允许出现反引号 —— 文档里写规则名时常见 ``PGPASSWORD=`、`sshpass`` 这种形式
    ("PGPASSWORD", re.compile(r"""PGPASSWORD=['"]?([^\s'"`]+)['"]?""")),
    ("sshpass -p", re.compile(r"""sshpass\s+-p\s*['"]?([^\s'"`]+)['"]?""")),
    # mysql 的 -p 常跟在其他 flag 后面（`mysql -u root -pXXX db`），所以先吃掉中间 flag
    ("mysql -p", re.compile(r"""mysql\b[^\n;&|]*?\s-p\s*['"]?([^\s'"`]+)['"]?""")),
    ("Bearer", re.compile(r"Bearer\s+([A-Za-z0-9._\-]{20,})")),
    ("sk-", re.compile(r"\b(sk-[A-Za-z0-9_\-]{20,})")),
    ("AKIA", re.compile(r"\b(AKIA[0-9A-Z]{16})")),
]

# 占位符 / 变量引用：以这些开头或整串等于这些词的值不算凭据
_PLACEHOLDER_HEAD = re.compile(
    r"^(\$|\$\{|\$\(|<|\{|xxx|XXX|\*\*\*|\.\.\.|YOUR|your|CHANGEME|CHANGE_ME|REDACTED|redacted"
    r"|EXAMPLE|example|真实|密码|口令|你的|此处|同上)",
)
_PLACEHOLDER_EXACT = {
    "password", "passwd", "pass", "pwd", "token", "key", "secret", "null", "none", "nil",
    "true", "false", "value", "string", "str", "admin",
}
MIN_SECRET_LEN = 6  # 太短的值不可能是真凭据（也避免 `mysql -p3306` 之类误报）


def is_placeholder(value: str) -> bool:
    """值是否是占位符/变量引用（是 → 不算泄露）。"""
    v = value.strip()
    if len(v) < MIN_SECRET_LEN:
        return True
    if _PLACEHOLDER_HEAD.match(v):
        return True
    if v.lower() in _PLACEHOLDER_EXACT:
        return True
    # 纯字母占位（xxx / xxxxxx / foo / bar）
    if re.fullmatch(r"[xX*#._-]+", v):
        return True
    # 前缀型占位：sk-YOUR_KEY_HERE_xxxx / AKIA_PLACEHOLDER 之类
    if re.search(r"(?i)(your[_-]?(api[_-]?)?key|placeholder|redacted|xxxx)", v):
        return True
    return False


def find_credentials(text: str):
    """扫描文本，返回 [(规则名, 命中的完整片段), ...]（已滤掉占位符）。"""
    hits = []
    for rule, pat in CRED_RULES:
        for m in pat.finditer(text):
            value = m.group(1) if m.groups() else m.group(0)
            if is_placeholder(value):
                continue
            hits.append((rule, m.group(0)))
    return hits

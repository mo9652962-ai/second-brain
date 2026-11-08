# -*- coding: utf-8 -*-
"""test_credential_patterns.py — 「命令内嵌凭据」规则的阳性/阴性用例

跑法: python scripts/test_credential_patterns.py
判据: 阳性必须命中，阴性（占位符/变量/文档示例）必须不命中。
背景见 knowledge/cards/2026-11-08-agent-approval-secrets.md
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from credential_patterns import find_credentials  # noqa: E402

# (描述, 文本, 期望是否命中)
CASES = [
    # ── 阳性：命令里带着真凭据 ──
    ("PGPASSWORD 明文", "PGPASSWORD=Sup3rS3cret psql -h db.internal -U app", True),
    ("PGPASSWORD 带引号", "PGPASSWORD='hunter2pass' psql -h db", True),
    ("sshpass -p", "sshpass -p 'Tr0ub4dor3' ssh root@host", True),
    ("mysql -p", "mysql -u root -pStr0ngPass db", True),
    ("Bearer 长 token", "curl -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9abc.def' x", True),
    ("sk- 形状", "OPENAI=sk-proj-AbCdEfGhIjKlMnOpQrSt", True),
    ("AKIA 形状", "key=AKIAIOSFODNN7EXAMPL3", True),
    # ── 阴性：占位符 / 变量 / 文档示例 ──
    ("PGPASSWORD=xxx", "PGPASSWORD=xxx psql", False),
    ("PGPASSWORD=真实密码", "你让它跑 `PGPASSWORD=真实密码 psql -h ...`", False),
    ("PGPASSWORD=${DB_PASS}", "PGPASSWORD=${DB_PASS} psql", False),
    ("PGPASSWORD=$DB_PASS", "PGPASSWORD=$DB_PASS psql", False),
    ("PGPASSWORD=<你的密码>", "PGPASSWORD=<你的密码> psql", False),
    ("PGPASSWORD=***", "PGPASSWORD=*** psql", False),
    ("纯规则名（无反引号值）", "规则：`PGPASSWORD=`、`sshpass -p`、`Bearer`、`sk-`、`AKIA`", False),
    ("Bearer 短值", "Authorization: Bearer abc", False),
    ("mysql -p 无值（交互式）", "mysql -u root -p db", False),
    ("sshpass 变量", 'sshpass -p "$SSH_PASS" ssh host', False),
    ("YOUR_KEY 占位", "OPENAI_API_KEY=sk-YOUR_KEY_HERE_xxxxxxxxxx", False),
]


def main():
    fail = 0
    for desc, text, expect in CASES:
        hits = find_credentials(text)
        got = bool(hits)
        ok = got == expect
        if not ok:
            fail += 1
        print(f"{'PASS' if ok else 'FAIL'} | {desc}: 期望{'命中' if expect else '不命中'} "
              f"实际{'命中 ' + str(hits) if got else '不命中'}")
    print(f"\n{len(CASES) - fail}/{len(CASES)} PASS")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())

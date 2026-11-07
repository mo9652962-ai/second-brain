"""daily_vault_optimize 跨小节查重修复自检（2026-11-07）。

沙箱化：用 USERPROFILE 指向临时目录，避免碰真实 vault。
覆盖 3 个用例：
  1. 已用 [[stem|显示名]] 登记过的笔记 → mount_orphans 不得重复挂载（旧版必失败）
  2. 已用 [[path/stem|显示名]] 登记的 → 同样不得重复挂载
  3. 未登记的笔记 → 正常挂载 1 条
  4. dedupe_automount：自动挂载小节里的裸行与正文带说明行重复 → 删裸行、留正文
"""
import os
import pathlib
import shutil
import sys
import tempfile

SANDBOX = pathlib.Path(tempfile.mkdtemp(prefix="vault_sandbox_"))
WORKSPACE = SANDBOX / ".openclaw" / "workspace"
(SANDBOX / ".openclaw" / "workspace" / "knowledge" / "Research").mkdir(parents=True)

MOC = WORKSPACE / "knowledge" / "Research" / "MOC-Research.md"
MOC.write_text(
    "---\nupdated: 2026-11-07\n---\n\n# MOC-Research\n\n"
    "## 论文追踪\n\n"
    "- [[note-a|显示名A]] — 带说明的正文条目\n"
    "- [[knowledge/Research/note-b|显示名B]] — 路径式条目\n\n"
    "## 自动挂载\n\n"
    "> cron 产出自动登记（防入链孤立）\n\n"
    "- [[note-a]]\n"
    "- [[note-c]]\n",
    encoding="utf-8",
)

note_a = WORKSPACE / "knowledge" / "Research" / "note-a.md"
note_b = WORKSPACE / "knowledge" / "Research" / "note-b.md"
note_d = WORKSPACE / "knowledge" / "Research" / "note-d.md"
for p in (note_a, note_b, note_d):
    p.write_text("---\ntags: [test]\n---\n\n# " + p.stem + "\n", encoding="utf-8")

os.environ["USERPROFILE"] = str(SANDBOX)
sys.path.insert(0, str(pathlib.Path(r"C:\Users\31954\.openclaw\workspace\scripts")))
import daily_vault_optimize as d  # noqa: E402

assert str(d.VAULT) == str(WORKSPACE), f"VAULT 未指向沙箱: {d.VAULT}"

fails = []


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ("" if cond else f"  <- {detail}"))
    if not cond:
        fails.append(name)


# 用例 1+2：note-a / note-b 已登记（pipe 形式）→ 不得挂载；note-d 未登记 → 挂载 1 条
mounted = d.mount_orphans([note_a, note_b, note_d])
text = MOC.read_text(encoding="utf-8")
check("pipe 形式已登记不重复挂载", mounted == 1, f"mounted={mounted}")
check("note-a 未新增裸行", text.count("- [[note-a]]") == 1, f"count={text.count('- [[note-a]]')}")
check("note-b 未新增裸行", "[[note-b]]" not in text)
check("note-d 被正常挂载", text.count("- [[note-d]]") == 1)

# 用例 4：去重 —— 自动挂载小节里 note-a 裸行与正文带说明行重复 → 删裸行
new_text, removed = d.dedupe_automount(text)
check("去重删除 1 条重复裸行", removed == 1, f"removed={removed}")
check("正文带说明行保留", "- [[note-a|显示名A]] — 带说明的正文条目" in new_text)
check("自动挂载小节不再有 note-a 裸行", new_text.count("- [[note-a]]") == 0)
check("非重复项未被误删（note-d）", "- [[note-d]]" in new_text)

# 幂等：再跑一次不应再删任何东西
again, removed2 = d.dedupe_automount(new_text)
check("去重幂等（第二次 0 条）", removed2 == 0, f"removed2={removed2}")
check("去重后文本稳定", again == new_text)

shutil.rmtree(SANDBOX, ignore_errors=True)
print("\nRESULT:", "ALL PASS" if not fails else f"FAILED {fails}")
sys.exit(1 if fails else 0)

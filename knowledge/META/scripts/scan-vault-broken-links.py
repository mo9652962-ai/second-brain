"""全仓库 wikilink 断链扫描（vault-root 相对路径语义）"""
import re, os, glob

ROOT = os.getcwd()
all_md = set()
for p in glob.glob('**/*.md', recursive=True):
    if '.git' in p or 'node_modules' in p:
        continue
    all_md.add(os.path.normpath(p))

stem_map = {}
for p in all_md:
    stem_map.setdefault(os.path.splitext(os.path.basename(p))[0].lower(), p)

# 占位符/示例链接（模板、文档示例、转义示例），非真链接
PLACEHOLDERS = {':space:', '` `', 'wiki link', 'note-1', 'series-2026-08-14',
                'their-name', 'name', 'skill-name', 'wikilink', '所属MOC',
                '2026-07-21-2347', 'health-2026-07-24', 'weekly-2026-07-26',
                'hermes-session-20260723', 'suggestions-applied',
                'outputs/xianyu-master/上架素材包/上架操作清单'}

def resolve(target, cur_dir):
    t = target.strip()
    if not t or t.startswith('#') or '://' in t or t in PLACEHOLDERS:
        return None
    if t.endswith('\\'):
        t = t[:-1].strip()
    # 相对当前文件目录（../ 开头）
    if t.startswith('../') or t.startswith('./'):
        cand = os.path.normpath(os.path.join(cur_dir, t))
        return None if (cand + '.md' in all_md or cand in all_md) else t
    # 含斜杠 → 相对 vault 根
    if '/' in t:
        cand = os.path.normpath(t)
        return None if (cand + '.md' in all_md or cand in all_md) else t
    # 裸名 → 全局 stem 查重
    low = t.lower()
    if low in stem_map:
        return None
    return t

broken = []
total = 0
for f in sorted(all_md):
    try:
        content = open(f, encoding='utf-8', errors='replace').read()
    except Exception:
        continue
    cur_dir = os.path.dirname(f)
    for m in re.finditer(r'\[\[([^\]|#]+?)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]', content):
        total += 1
        r = resolve(m.group(1), cur_dir)
        if r:
            broken.append((f, r))

print(f"总链接: {total}")
print(f"真断链: {len(broken)}")
from collections import Counter
c = Counter(t for _, t in broken)
print("\n=== 断链目标 Top ===")
for t, n in c.most_common(30):
    print(f"  {n:3d}  {t}")
print("\n=== 按文件 ===")
for f, t in broken:
    print(f"  {f}  ->  [[{t}]]")

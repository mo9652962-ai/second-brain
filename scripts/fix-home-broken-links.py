"""修 HOME.md 失效 wikilink（真断链 → 反引号纯文本，保留别名/描述；幂等）
只处理指向不存在文件的链接；占位符/归档/日记历史引用不动（lint 只报告）。
"""
import pathlib, re, os

F = pathlib.Path('HOME.md')
text = F.read_text(encoding='utf-8')

# 收集 vault 所有 md（不含点目录，除 .archive）
all_md = set()
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if not d.startswith('.') or d == '.archive']
    for f in files:
        if f.endswith('.md'):
            all_md.add(os.path.normpath(os.path.join(root, f)).replace('\\', '/'))

def exists(target):
    t = re.sub(r'^(\.\./)+', '', target).replace('\\', '/')
    if t.endswith('.md'):
        t = t[:-3]
    if not t:
        return False
    # 匹配 basename 或全路径
    base = os.path.basename(t)
    for p in all_md:
        if p.endswith('/' + t + '.md') or os.path.basename(p)[:-3] == base:
            return True
    return False

pat = re.compile(r'\[\[([^\[\]]+)\]\]')
changed = 0
lines = text.splitlines()
new_lines = []
for ln in lines:
    def repl(m):
        global changed
        inner = m.group(1)
        target = inner.split('|')[0].split('#')[0].strip()
        alias = inner.split('|')[1].strip() if '|' in inner else None
        if exists(target):
            return m.group(0)
        # 失效链接 → 反引号纯文本（保留别名或 target）
        changed += 1
        return f'`{alias or target}`'
    new_lines.append(pat.sub(repl, ln))

# 保留原行尾
crlf = '\r\n' if '\r\n' in text else '\n'
F.write_text('\n'.join(new_lines) + (crlf if text.endswith(crlf) else ''), encoding='utf-8')
print(f'HOME.md 修复失效链接: {changed} 处')

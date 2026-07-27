import os, re, sys

errors = 0
notes = set()
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
    for f in files:
        if f.endswith('.md'):
            notes.add(os.path.join(root, f))

for n in sorted(notes):
    with open(n, encoding='utf-8', errors='replace') as f:
        for lineno, line in enumerate(f, 1):
            for m in re.finditer(r'\[\[([^\]]+)\]\]', line):
                target = m.group(1).split('|')[0].split('#')[0]
                found = any(target in p for p in notes)
                if not found:
                    print(f'⚠ Broken link: {n}:{lineno} → {target}')
                    errors += 1

if errors:
    print(f'❌ Found {errors} broken wikilinks')
    sys.exit(1)
else:
    print('✅ All wikilinks OK')

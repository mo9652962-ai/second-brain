#!/usr/bin/env python3
"""tag-lint: 只读扫描知识库标签一致性。输出：大小写变体组、标签家族、裸标签、双标签格式混用。"""
import re, sys, collections
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else "knowledge").resolve()
SKIP = {".git", ".obsidian", ".trash", "Archive", "META"}
files = [f for f in root.rglob("*.md") if not any(p in SKIP for p in f.relative_to(root).parts)]

fm_re = re.compile(r"^tags:\s*\[(.*?)\]", re.M)
fm_yaml_re = re.compile(r"^tags:\s*\n((?:\s*-\s*\S+\s*\n?)+)", re.M)
inline_re = re.compile(r"(?<![\w#])#([A-Za-z][A-Za-z0-9_\-/]*)")

fm_tags = collections.Counter()
inline_tags = collections.Counter()
tag_case = collections.defaultdict(set)
fm_yaml_files = []

for f in files:
    try:
        text = f.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    m = fm_re.search(text)
    if m:
        for t in re.split(r"[,\s]+", m.group(1).strip()):
            if t:
                fm_tags[t] += 1
                tag_case[t.lower()].add(t)
    m2 = fm_yaml_re.search(text)
    if m2:
        fm_yaml_files.append(f.relative_to(root))
        for t in re.findall(r"-\s*(\S+)", m2.group(1)):
            if t:
                fm_tags[t] += 1
                tag_case[t.lower()].add(t)
    text_nocode = re.sub(r"`[^`]*`", "", text)
    text_nocode = re.sub(r"```.*?```", "", text_nocode, flags=re.S)
    for t in inline_re.findall(text_nocode):
        inline_tags[t] += 1
        tag_case[t.lower()].add(t)

case_issues = {k: v for k, v in sorted(tag_case.items()) if len(v) > 1}

print("=== CASE VARIANT GROUPS ===")
for k, v in case_issues.items():
    print(f"  {k}: {sorted(v)}")
print(f"total case groups: {len(case_issues)}")

# FM-only vs inline-only overlap
fm_set = set(fm_tags)
inl_set = set(inline_tags)
print(f"\nFM tags: {len(fm_set)}, inline tags: {len(inl_set)}, in both: {len(fm_set & inl_set)}")

# families
fam = collections.Counter()
for t, c in fm_tags.items():
    fam[t.split('/')[0]] += c
print("\n=== FM tag families ===")
for k, v in fam.most_common(50):
    print(f"  {k}: {v}")

# full tag list (FM) for review
print("\n=== ALL FM TAGS ===")
for t, c in fm_tags.most_common(300):
    print(f"  {t}: {c}")

print("\n=== YAML-list style tags files ===")
for p in fm_yaml_files[:20]:
    print(f"  {p}")

print("\n=== TOP inline tags (50) ===")
for t, c in inline_tags.most_common(50):
    print(f"  {t}: {c}")

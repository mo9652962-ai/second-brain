#!/usr/bin/env python3
"""Weekly consolidation diagnostic: MOC coverage diff + orphans + misc checks.
Run from vault root. CRLF-safe, read_bytes only.
"""
import re, pathlib, sys

ROOT = pathlib.Path(r"C:/Users/31954/.openclaw/workspace")
EXCLUDE = {".git", ".obsidian", ".venv", ".temp", "node_modules", "site", "graphify-out", "__pycache__", "mcp", "traces"}

def md_files(base):
    out = []
    for f in base.rglob("*.md"):
        rel = f.relative_to(ROOT).as_posix()
        if any(part in EXCLUDE for part in rel.split("/")):
            continue
        out.append(f)
    return out

def wikilink_targets(text):
    return set(m for m in re.findall(r"\[\[([^\]|#]+)", text))

def stem(name):
    return name[:-3] if name.endswith(".md") else name

# 1. Domain dirs vs MOC coverage
print("=== DOMAIN VS MOC DIFF (files in dir missing from MOC) ===")
domain_mocs = {
    "knowledge/Research": "knowledge/Research/MOC-Research.md",
    "knowledge/Dev": "knowledge/Dev/MOC-Dev.md",
    "knowledge/Hardware": "knowledge/Hardware/MOC-Hardware.md",
    "knowledge/Productivity": "knowledge/Productivity/MOC-Productivity.md",
    "knowledge/Finance": "knowledge/Finance/MOC-Finance.md",
}
for d, moc in domain_mocs.items():
    mocf = ROOT / moc
    if not mocf.exists():
        print(f"{d}: NO MOC FILE {moc}")
        continue
    moc_text = mocf.read_bytes().decode("utf-8", errors="ignore")
    moc_links = {stem(t.split("/")[-1]) for t in wikilink_targets(moc_text)}
    files = {stem(f.name) for f in md_files(ROOT / d)}
    missing = sorted(files - moc_links - {stem(mocf.name)})
    # filter non-note files (already moved out)
    print(f"{d}: {len(files)} files, {len(moc_links)} MOC links, missing={len(missing)}")
    for m in missing:
        print(f"   MISSING: {m}")

# 2. Root-level knowledge files not in any domain
print("\n=== KNOWLEDGE ROOT FILES (not in subdomain) ===")
for f in sorted((ROOT / "knowledge").glob("*.md")):
    if f.name in ("knowledge-map.md", "Cross-Domain.md"):
        continue
    print(f"  {f.name}")

# 3. Orphan count (no inbound wikilinks from any vault md)
print("\n=== ORPHAN STATS ===")
all_files = md_files(ROOT)
all_names = {stem(f.name) for f in all_files}
inbound = set()
for f in all_files:
    text = f.read_bytes().decode("utf-8", errors="ignore")
    for t in wikilink_targets(text):
        base = stem(t.split("/")[-1])
        if base in all_names:
            inbound.add(base)
orphans = [f for f in all_files if stem(f.name) not in inbound]
print(f"Total notes: {len(all_files)}, orphan notes: {len(orphans)} ({len(orphans)*100//max(len(all_files),1)}%)")
for f in sorted(orphans, key=lambda x: x.as_posix()):
    print(f"  {f.relative_to(ROOT).as_posix()}")

# 4. Actual filename check for 内容-小君AI
print("\n=== DEV FILES MATCHING 小君AI/内容 ===")
for f in sorted((ROOT / "knowledge/Dev").glob("*.md")):
    if "小君" in f.name or "内容" in f.name:
        print(f"  {f.name}")

# 5. memory root loose date files
print("\n=== MEMORY ROOT LOOSE FILES ===")
for f in sorted((ROOT / "memory").glob("*.md")):
    print(f"  {f.name}")

# 6. research/ top-level
print("\n=== RESEARCH TOP-LEVEL ===")
for f in sorted((ROOT / "research").rglob("*.md")):
    print(f"  {f.relative_to(ROOT).as_posix()}")

# 7. Broken wikilink quick check (case-insensitive)
print("\n=== BROKEN WIKILINK QUICK CHECK ===")
ci_map = {}
for f in all_files:
    ci_map.setdefault(stem(f.name).lower(), []).append(f)
broken = 0
for f in all_files:
    text = f.read_bytes().decode("utf-8", errors="ignore")
    for t in wikilink_targets(text):
        base = stem(t.split("/")[-1]).lower()
        if base in ("home", "index", "memory", "knowledge-map", "cross-domain", "moc-research", "moc-dev", "moc-hardware", "moc-productivity", "moc-finance", "moc-concepts"):
            continue
        if base.startswith("skills/"):
            continue
        if base not in ci_map:
            broken += 1
            if broken <= 20:
                print(f"  BROKEN: {f.relative_to(ROOT).as_posix()} -> [[{t}]]")
print(f"Total broken (quick): {broken}")
print("\nDONE")

import os, re, json

skills_root = os.path.expanduser("~/AppData/Local/hermes/skills")

bundled = set()
with open(os.path.join(skills_root, ".bundled_manifest"), encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line and ":" in line:
            bundled.add(line.split(":")[0])

def extract_frontmatter(md_path):
    try:
        with open(md_path, encoding="utf-8", errors="replace") as f:
            content = f.read(3000)
    except Exception:
        return {}
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm

results = []
for entry in sorted(os.listdir(skills_root)):
    if entry.startswith("."):
        continue
    path = os.path.join(skills_root, entry)
    if not os.path.isdir(path):
        continue
    if entry.startswith("@"):
        for sub in sorted(os.listdir(path)):
            subpath = os.path.join(path, sub)
            if os.path.isdir(subpath) and os.path.isfile(os.path.join(subpath, "SKILL.md")):
                results.append({"name": f"@{entry}/{sub}", "type": "hub", "md": os.path.join(subpath, "SKILL.md")})
    else:
        md = os.path.join(path, "SKILL.md")
        if os.path.isfile(md):
            if entry in bundled:
                continue
            results.append({"name": entry, "type": "agent", "md": md})
        else:
            for sub in sorted(os.listdir(path)):
                subpath = os.path.join(path, sub)
                if os.path.isdir(subpath) and os.path.isfile(os.path.join(subpath, "SKILL.md")):
                    if sub in bundled:
                        continue
                    results.append({"name": f"{entry}/{sub}", "type": "agent-in-cat", "md": os.path.join(subpath, "SKILL.md")})

print(f"Bundled manifest: {len(bundled)} | Non-bundled: {len(results)} | agent: {sum(1 for r in results if r['type']!='hub')} hub: {sum(1 for r in results if r['type']=='hub')}")
print()
for r in results:
    fm = extract_frontmatter(r["md"])
    desc = fm.get("description", "")[:100].replace("\n", " ")
    print(f"[{r['type']}] {r['name']} | desc: {desc}")

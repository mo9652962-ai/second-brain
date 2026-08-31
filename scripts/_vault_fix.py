# -*- coding: utf-8 -*-
"""Fix vault issues from 2026-08-31 audit:
1. Skill-name wikilinks -> plain-text backticks (21 occurrences)
2. Genuine broken link: memory/2026/08/2026-08-03-research-apply (never existed) -> plain text
3. Folder link: outputs/xianyu-master/上架素材包 -> retarget to actual note inside
4. Tag case normalization (majority-wins) in frontmatter tags: only

Binary read/write to preserve CRLF. Prints a per-file change report.
"""
import pathlib, re

VAULT = pathlib.Path(r"C:\Users\31954\.openclaw\workspace")

# (filename, list of (old, new)) exact replacements
# Skill-name wikilinks -> backtick plain text
SKILL_LINKS = {
    "knowledge/AI/数模5-Skill工作流-2026-08-23.md": [("[[shumo-paper-writing]]", "`shumo-paper-writing`")],
    "knowledge/Development/VibeCoding部署全流程-下-2026-08-23.md": [
        ("[[nextjs-deploy-test]]", "`nextjs-deploy-test`"),
        ("[[multi-end-ai-provider-config]]", "`multi-end-ai-provider-config`"),
    ],
    "knowledge/Productivity/freelance-quote-4questions-2026-08-21.md": [
        ("[[ai-freelance-pricing]]", "`ai-freelance-pricing`"),
        ("[[grill-with-docs]]", "`grill-with-docs`"),
        ("[[xianyu-monetization]]", "`xianyu-monetization`"),
    ],
    "knowledge/Research/网安资料库-入口.md": [
        ("[[src-bug-hunting]]", "`src-bug-hunting`"),
        ("[[src-recon-workflow]]", "`src-recon-workflow`"),
        ("[[web-security-lab-setup]]", "`web-security-lab-setup`"),
        ("[[pentest-lab-setup]]", "`pentest-lab-setup`"),
    ],
    "knowledge/Research/网安资料库-综合研究-2026-08-22.md": [
        ("[[src-bug-hunting]]", "`src-bug-hunting`"),
        ("[[src-recon-workflow]]", "`src-recon-workflow`"),
        ("[[web-security-lab-setup]]", "`web-security-lab-setup`"),
        ("[[pentest-lab-setup]]", "`pentest-lab-setup`"),
        ("[[nmap-scanning]]", "`nmap-scanning`"),
    ],
    "knowledge/Security/nmap-tutorial-2026-08-20.md": [
        ("[[src-recon-scanning]]", "`src-recon-scanning`"),
        ("[[src-bug-hunting]]", "`src-bug-hunting`"),
    ],
    "knowledge/Security/osint-username-maigret-2026-08-21.md": [
        ("[[src-recon-scanning]]", "`src-recon-scanning`"),
        ("[[nmap-scanning]]", "`nmap-scanning`"),
        ("[[src-bug-hunting]]", "`src-bug-hunting`"),
    ],
    "outputs/xianyu-master/搭网站写脚本-商品素材包.md": [
        ("[[xianyu-quote-script|闲鱼询价话术模板（技能 templates）]]", "`xianyu-quote-script`"),
    ],
}

# Genuine broken links
GENUINE = {
    "knowledge/cards/2026-08-03-linggan-deai.md": [
        ("[[memory/2026/08/2026-08-03-research-apply]]", "memory/2026/08/2026-08-03-research-apply"),
    ],
    # folder link -> retarget to actual note 上架操作清单.md inside the folder
    "outputs/xianyu-master/搭网站写脚本-商品素材包.md": [
        ("[[outputs/xianyu-master/上架素材包]]", "[[outputs/xianyu-master/上架素材包/上架操作清单|上架素材包]]"),
    ],
}

# Tag normalization: file -> (old_tag, new_tag). Only touches frontmatter tags: [...] line.
TAG_FIXES = {
    "knowledge/Security/src-ai-automation-3tools-2026-08-21.md": [("ai", "AI")],
    "knowledge/Research/nihaixia-skill.md": [("AI-skill", "ai-skill")],
    "knowledge/Dev/game-engine-ai-research-2026-08-17.md": [("AI编程", "ai编程")],
    "knowledge/Dev/llmfit-hardware-matching-2026-08-23.md": [("llm", "LLM")],
    "knowledge/Hardware/AI-PCB设计前沿-pcbflow对比.md": [("PCB", "pcb")],
    "knowledge/Development/循环插入与缓存-两个夺命坑.md": [("redis", "Redis")],
}

tag_re = re.compile(r'^tags:\s*\[(.*?)\]', re.M)

def fix_file(rel, repls):
    p = VAULT / rel
    if not p.exists():
        print(f"  !! MISSING: {rel}")
        return 0
    data = p.read_bytes()
    content = data.decode('utf-8', errors='ignore')
    orig = content
    for old, new in repls:
        content = content.replace(old, new)
    if content != orig:
        p.write_bytes(content.encode('utf-8'))
        return 1
    return 0

def fix_tags(rel, fixes):
    p = VAULT / rel
    if not p.exists():
        print(f"  !! MISSING: {rel}")
        return 0
    data = p.read_bytes()
    content = data.decode('utf-8', errors='ignore')
    orig = content
    def sub(m):
        tags = m.group(1)
        for old, new in fixes:
            # replace whole comma-separated tag tokens (not substring)
            toks = [t for t in tags.split(',')]
            ntoks = []
            for t in toks:
                tt = t.strip().strip('"\'')
                ntoks.append(new if tt == old else t)
            tags = ','.join(ntoks)
        return 'tags: [' + tags + ']'
    content = tag_re.sub(sub, content, count=1)
    if content != orig:
        p.write_bytes(content.encode('utf-8'))
        return 1
    return 0

print("=== Skill-name wikilinks -> backticks ===")
for rel, repls in SKILL_LINKS.items():
    n = fix_file(rel, repls)
    print(f"  {rel}: {'FIXED' if n else 'no change'}")

print("\n=== Genuine broken links ===")
for rel, repls in GENUINE.items():
    n = fix_file(rel, repls)
    print(f"  {rel}: {'FIXED' if n else 'no change'}")

print("\n=== Tag normalization ===")
for rel, fixes in TAG_FIXES.items():
    n = fix_tags(rel, fixes)
    print(f"  {rel}: {'FIXED' if n else 'no change'}")

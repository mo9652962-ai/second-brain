import os
import re
from pathlib import Path

VAULT_SKILLS = Path(r"C:\Users\31954\.openclaw\workspace\skills")
SYSTEM_SKILLS = Path(r"C:\Users\31954\AppData\Local\Hermes\skills")

CATEGORIES = ["hardware", "web", "platform", "hermes"]


def slugify(name):
    name = re.sub(r'-v\d+\.\d+', '', name)
    name = re.sub(r'-\d{4}', '', name)
    name = name.replace('.md', '').lower()
    name = name.replace('_', '-').replace(' ', '-')
    return name


def extract_description(content, max_len=120):
    match = re.search(r'>\s*(.+?)\n', content)
    if match:
        desc = match.group(1).strip()
        if len(desc) > 10:
            return desc[:max_len] + "..." if len(desc) > max_len else desc
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('# '):
            for j in range(i+1, min(i+5, len(lines))):
                if lines[j].strip() and not lines[j].startswith('>') and not lines[j].startswith('---'):
                    return lines[j].strip()[:max_len]
    return "知识文档"


def sync_one_file(src_path, category):
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    skill_name = slugify(src_path.name)
    description = extract_description(content)
    # 检查是否已有包含 name 字段的标准 Skill frontmatter
    has_skill_frontmatter = bool(re.search(r'^name:\s*".+?"', content, re.MULTILINE))
    
    if has_skill_frontmatter:
        # 已有正确的 Skill 格式，直接使用
        new_content = content
    else:
        # 需要添加或合并 frontmatter
        skill_frontmatter = '''---
name: "%s"
description: "%s"
category: "%s"
---

''' % (skill_name, description, category)
        
        if content.strip().startswith('---'):
            # 已有 frontmatter（可能是 Obsidian 的 date/tags 等）
            # 提取内容部分，替换成新的 frontmatter
            match = re.match(r'^---\n.*?\n---\n', content, re.DOTALL)
            if match:
                # 有完整的 frontmatter 块，替换它
                new_content = skill_frontmatter + content[match.end():]
            else:
                # 不完整，直接加在前面
                new_content = skill_frontmatter + content
        else:
            # 没有 frontmatter，添加
            new_content = skill_frontmatter + content

    target_dir = SYSTEM_SKILLS / skill_name
    target_dir.mkdir(exist_ok=True)
    with open(target_dir / "SKILL.md", 'w', encoding='utf-8') as f:
        f.write(new_content)
    return (skill_name, "✅")


def main():
    print("=" * 50)
    print("🧠 Skill 同步：Obsidian 仓库 → Hermes 系统目录")
    print("=" * 50)
    print()

    total, success = 0, 0
    results = []

    for category in CATEGORIES:
        category_dir = VAULT_SKILLS / category
        if not category_dir.exists():
            continue
        for md_file in category_dir.glob("*.md"):
            total += 1
            name, status = sync_one_file(md_file, category)
            results.append((category, name, status))
            success += 1

    print(f"{'领域':<12} {'Skill 名称':<40} {'状态'}")
    print("-" * 70)
    for category, name, status in results:
        print(f"[{category:<10}] {name:<40} {status}")

    print()
    print("=" * 50)
    print(f"📊 总计: {success} / {total} 同步成功")
    print()
    print("💡 Obsidian 中编辑完 Skill 文档后，运行此脚本即可同步！")


if __name__ == "__main__":
    main()

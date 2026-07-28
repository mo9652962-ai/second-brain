"""
Second Brain 网页自动归档脚本
功能: 打开网页 → 提取内容 → MarkItDown 结构化 → 存入 Obsidian 知识库
使用: uv run python scripts/web-archive.py https://example.com
"""
import sys
import os
from pathlib import Path
from datetime import datetime
from markitdown import MarkItDown


def sanitize_filename(title):
    """清理文件名中的非法字符"""
    illegal = '<>:"/\\|?*'
    for c in illegal:
        title = title.replace(c, '-')
    return title.strip()[:100]


def extract_and_archive(url, output_dir=None):
    """
    提取网页内容并存入知识库
    
    Args:
        url: 网页 URL
        output_dir: 输出目录，默认 knowledge/Archive/
    """
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "knowledge" / "Archive"
        output_dir.mkdir(parents=True, exist_ok=True)
    
    print("=" * 70)
    print(f"🌐 网页归档工具")
    print("=" * 70)
    print(f"📥 源 URL: {url}")
    print(f"📂 输出目录: {output_dir}")
    print()
    
    # 1. 使用 MarkItDown 提取网页内容
    print("🔍 步骤 1/4: 提取网页内容...")
    md = MarkItDown()
    try:
        result = md.convert(url)
        print(f"   ✅ 提取成功，{len(result.markdown)} 字符")
    except Exception as e:
        print(f"   ❌ 提取失败: {e}")
        return False
    
    # 2. 生成标题和元数据
    print("📝 步骤 2/4: 生成文档元数据...")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 尝试从内容提取标题，或者使用 URL
    title = result.title if hasattr(result, 'title') and result.title else url
    safe_title = sanitize_filename(title)
    filename = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{safe_title}.md"
    
    print(f"   标题: {title}")
    print(f"   文件名: {filename}")
    
    # 3. 构建 Obsidian 格式的文档
    print("📋 步骤 3/4: 构建 Obsidian 文档...")
    frontmatter = f"""---
title: "{title}"
source: "{url}"
archived_at: "{timestamp}"
tags: ["archive", "web"]
---

# {title}

> 🔗 来源: [{url}]({url})
> 📅 归档时间: {timestamp}

---

"""
    
    full_content = frontmatter + result.markdown
    
    # 4. 写入文件
    print("💾 步骤 4/4: 写入知识库...")
    output_path = output_dir / filename
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"   ✅ 已保存: {output_path}")
    print()
    print("=" * 70)
    print("🎉 归档完成！")
    print(f"📄 文件大小: {len(full_content)} 字符")
    print(f"📍 文件路径: {output_path}")
    print()
    print("💡 下一步:")
    print("   - 可在 Obsidian 中查看和编辑")
    print("   - 可添加双向链接到相关笔记")
    print("   - Memvid 会自动建立索引，支持语义搜索")
    print("=" * 70)
    
    return True


def main():
    if len(sys.argv) < 2:
        print("使用方式: uv run python scripts/web-archive.py <URL>")
        print()
        print("示例:")
        print("  uv run python scripts/web-archive.py https://example.com")
        print()
        print("功能:")
        print("  - 自动提取网页正文内容")
        print("  - MarkItDown 智能结构化")
        print("  - 自动添加 YAML 元数据")
        print("  - 存入 Obsidian 知识库 Archive 目录")
        print("  - 支持 Memvid 向量检索")
        sys.exit(1)
    
    url = sys.argv[1]
    success = extract_and_archive(url)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

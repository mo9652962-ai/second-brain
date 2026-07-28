#!/usr/bin/env python3
"""
同步 Obsidian 知识库 (knowledge/) 到 MkDocs 文档站 (docs/knowledge/)
只同步公共文档，跳过敏感或草稿内容
"""
import shutil
from pathlib import Path

workspace = Path(__file__).parent.parent
src_dir = workspace / "knowledge"
dst_dir = workspace / "docs" / "knowledge"

# 确保目标目录存在
dst_dir.mkdir(parents=True, exist_ok=True)

# 需要同步的文件列表（明确列出，避免同步草稿或敏感内容）
sync_files = [
    "knowledge-map.md",        # 知识地图
    "AI/airi.md",              # AIRI 研究
    "Design/hallmark.md",      # Hallmark 设计
    "Design/ibelick-ui-skills.md",  # UI 设计技巧
    "Dev/codebase-memory-mcp.md",    # Codebase Memory
    "Dev/grok-build.md",       # Grok 构建
    "Dev/mattpocock-methodology.md",  # 方法论
    "Research/*.md",            # 所有研究报告
]

print("=" * 60)
print("📦 knowledge/ → docs/knowledge/ 同步")
print("=" * 60)
print()

synced_count = 0
for pattern in sync_files:
    for src_file in src_dir.glob(pattern):
        if src_file.is_file():
            # 计算目标路径
            rel_path = src_file.relative_to(src_dir)
            dst_file = dst_dir / rel_path
            
            # 确保目标目录存在
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 复制文件
            shutil.copy2(src_file, dst_file)
            print(f"✅ {rel_path}")
            synced_count += 1

print()
print("=" * 60)
print(f"✅ 同步完成: 共 {synced_count} 个文件")
print("=" * 60)

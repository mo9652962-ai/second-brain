"""
Second Brain 文档批量导入脚本
支持格式: PDF, DOCX, XLSX, PPTX, HTML, TXT, CSV, JSON
自动转换为 Markdown 并存入 Obsidian 知识库
"""
import os
import sys
from pathlib import Path
from markitdown import MarkItDown


def convert_file(input_path: Path, output_dir: Path) -> bool:
    """转换单个文件到 Markdown"""
    try:
        md = MarkItDown()
        result = md.convert(str(input_path))
        
        # 生成输出文件名
        output_file = output_dir / f"{input_path.stem}.md"
        
        # 写入 Markdown
        output_file.write_text(result.markdown, encoding='utf-8')
        
        print(f"✅ {input_path.name} -> {output_file.name}")
        print(f"   大小: {len(result.markdown)} 字符")
        return True
    except Exception as e:
        print(f"❌ {input_path.name}: {e}")
        return False


def batch_convert(input_dir: Path, output_dir: Path = None) -> dict:
    """批量转换目录下的所有支持格式"""
    if output_dir is None:
        output_dir = Path(__file__).parent.parent / "Auto-Import"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 支持的格式
    supported = {'.pdf', '.docx', '.xlsx', '.pptx', '.html', '.txt', '.csv', '.json'}
    
    stats = {
        'total': 0,
        'success': 0,
        'failed': 0,
        'files': []
    }
    
    print(f"📂 输入目录: {input_dir}")
    print(f"📂 输出目录: {output_dir}")
    print(f"📋 支持格式: {', '.join(supported)}")
    print("-" * 60)
    
    for file_path in input_dir.rglob("*"):
        if file_path.suffix.lower() in supported:
            stats['total'] += 1
            if convert_file(file_path, output_dir):
                stats['success'] += 1
                stats['files'].append((file_path.name, '✅'))
            else:
                stats['failed'] += 1
                stats['files'].append((file_path.name, '❌'))
    
    print("-" * 60)
    print(f"📊 统计: 总计 {stats['total']} 个文件")
    print(f"   成功: {stats['success']}")
    print(f"   失败: {stats['failed']}")
    
    if stats['total'] > 0:
        rate = (stats['success'] / stats['total']) * 100
        print(f"   成功率: {rate:.1f}%")
    
    return stats


def main():
    print("=" * 60)
    print("📚 Second Brain 文档批量导入工具")
    print("=" * 60)
    print()
    
    if len(sys.argv) < 2:
        print("用法: python batch-import.py <输入目录> [输出目录]")
        print()
        print("示例:")
        print("  python batch-import.py D:/我的文档/")
        print("  python batch-import.py ./待导入/ ./Auto-Import/")
        print()
        print("支持格式: PDF, DOCX, XLSX, PPTX, HTML, TXT, CSV, JSON")
        return
    
    input_dir = Path(sys.argv[1])
    if not input_dir.exists():
        print(f"❌ 目录不存在: {input_dir}")
        return
    
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    batch_convert(input_dir, output_dir)


if __name__ == "__main__":
    main()

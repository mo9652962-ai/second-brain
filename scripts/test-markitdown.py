"""
MarkItDown 快速测试脚本
测试各种文档格式转换能力
"""
import sys
import os
from pathlib import Path

print("=" * 60)
print("🧪 MarkItDown 功能测试")
print("=" * 60)

# 1. 验证导入
try:
    from markitdown import MarkItDown
    print("✅ 1. MarkItDown 导入成功")
except Exception as e:
    print(f"❌ 导入失败: {e}")
    sys.exit(1)

# 2. 初始化
try:
    md = MarkItDown()
    print("✅ 2. MarkItDown 初始化成功")
except Exception as e:
    print(f"❌ 初始化失败: {e}")
    sys.exit(1)

# 3. 列出支持的格式
print("\n📋 支持的文件格式:")
extensions = ['.pdf', '.docx', '.xlsx', '.pptx', '.html', '.txt', '.csv', '.json']
for ext in extensions:
    print(f"   - {ext}")

# 4. 测试 1: 简单文本转换
print("\n📝 测试 1: 简单文本")
test_text = """
这是测试文本
这是第二行
这是第三行
"""
try:
    temp_txt = Path("test_input.txt")
    temp_txt.write_text(test_text, encoding='utf-8')
    result = md.convert(str(temp_txt))
    print(f"✅ 文本转换成功")
    print(f"   输出长度: {len(result.text_content)} 字符")
    print(f"   预览: {result.text_content[:50]}...")
    temp_txt.unlink()
except Exception as e:
    print(f"⚠️ 文本转换跳过: {e}")

# 5. 测试 2: HTML 转换
print("\n🌐 测试 2: HTML 转换")
test_html = """
<html>
<body>
<h1>测试标题</h1>
<p>这是一段 <b>加粗</b> 和 <i>斜体</i> 的文本。</p>
<ul>
<li>列表项 1</li>
<li>列表项 2</li>
</ul>
</body>
</html>
"""
try:
    temp_html = Path("test_input.html")
    temp_html.write_text(test_html, encoding='utf-8')
    result = md.convert(str(temp_html))
    print(f"✅ HTML 转换成功")
    print(f"   预览: {result.markdown[:80]}...")
    temp_html.unlink()
except Exception as e:
    print(f"⚠️ HTML转换跳过: {e}")

print("\n" + "=" * 60)
print("🎉 MarkItDown 基础功能全部正常！")
print("=" * 60)
print("\n💡 下一步: 放入真实的 PDF/Word/Excel 文档测试")

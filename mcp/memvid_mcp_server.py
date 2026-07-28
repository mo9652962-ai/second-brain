"""
Memvid MCP Server - Second Brain 记忆层
用 fastmcp 封装 memvid-sdk，提供 AI 代理记忆功能
"""
from fastmcp import FastMCP
import memvid_sdk as memvid
from pathlib import Path

# Second Brain 记忆文件路径
MEMORY_FILE = Path(__file__).parent / "second-brain.mv2"

# 创建 MCP 服务器
mcp = FastMCP("Memvid")


@mcp.tool()
def create_memory() -> str:
    """创建一个新的空记忆文件"""
    if not MEMORY_FILE.exists():
        mv = memvid.create(str(MEMORY_FILE))
        mv.close()
        return f"✅ 已创建记忆文件: {MEMORY_FILE}"
    return f"ℹ️  记忆文件已存在: {MEMORY_FILE}"


@mcp.tool()
def put_memory(content: str, title: str = "", metadata: str = "") -> str:
    """
    向记忆中添加内容
    
    Args:
        content: 要记住的文本内容
        title: 可选标题
        metadata: 可选元数据（JSON 字符串）
    """
    mv = memvid.open(str(MEMORY_FILE))
    result = mv.put(
        text=content, 
        title=title or None, 
        metadata=metadata or {}
    )
    mv.close()  # 关闭即自动提交
    return f"✅ 已保存记忆 (ID: {result})"


@mcp.tool()
def search_memory(query: str, k: int = 5) -> str:
    """
    搜索记忆
    
    Args:
        query: 搜索查询
        k: 返回结果数量
    """
    mv = memvid.open(str(MEMORY_FILE))
    result = mv.find(query, k=k)
    mv.close()
    
    if not result:
        return "❌ 未找到匹配的记忆"
    
    output = [f"✅ 找到 {len(result)} 条相关记忆:\n"]
    for i, r in enumerate(result, 1):
        output.append(f"{i}. {r.content[:100]}...")
    return "\n".join(output)


@mcp.tool()
def memory_stats() -> str:
    """获取记忆文件统计信息"""
    if not MEMORY_FILE.exists():
        return "❌ 记忆文件不存在，请先运行 create_memory()"
    
    mv = memvid.open(str(MEMORY_FILE))
    stats = mv.stats()  # 返回字典
    size_mb = MEMORY_FILE.stat().st_size / 1024 / 1024
    total_frames = stats.get(
        'frame_count', 
        stats.get('total_frames', stats.get('frames', 'N/A'))
    )
    mv.close()
    
    return f"""📊 Memvid 记忆统计

文件: {MEMORY_FILE}
总帧数: {total_frames}
文件大小: {size_mb:.1f} MB
索引类型: BM25 + 向量混合搜索
"""


@mcp.tool()
def ask_memory(question: str) -> str:
    """
    向记忆提问，获得基于上下文的回答
    
    Args:
        question: 问题
    """
    mv = memvid.open(str(MEMORY_FILE))
    result = mv.ask(question)
    mv.close()
    
    # 处理对象或字典返回
    if hasattr(result, 'answer'):
        answer = result.answer
        confidence = result.confidence if hasattr(result, 'confidence') else 0
        sources = len(result.sources) if hasattr(result, 'sources') else 0
    else:
        answer = result.get('answer', '无法回答')
        confidence = result.get('confidence', 0)
        sources = len(result.get('sources', []))
    
    return f"""🧠 Memvid 回答

问: {question}
答: {answer}

信心: {confidence:.2f}
使用了 {sources} 个来源
"""


if __name__ == "__main__":
    # 确保记忆文件存在
    if not MEMORY_FILE.exists():
        mv = memvid.create(str(MEMORY_FILE))
        mv.put(
            text="这是 Second Brain 的第一条记忆，记录于 2026 年 7 月 28 日。Second Brain 是基于 Obsidian + Hermes 的个人知识管理系统，拥有 8,248 个代码节点和 62,226 条关系。", 
            metadata={"type": "system"}
        )
        mv.close()  # 关闭即自动提交
        print(f"✅ 已创建初始化记忆文件: {MEMORY_FILE}")
    
    print(f"🚀 Memvid MCP 服务器启动中...")
    print(f"📂 记忆文件: {MEMORY_FILE}")
    mcp.run()

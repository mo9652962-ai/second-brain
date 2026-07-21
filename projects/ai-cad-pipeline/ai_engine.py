"""
AI-CAD Pipeline — AI 驱动代码生成器 v0.2
让 AI 直接生成 build123d Python 代码，而非匹配预设零件库。

这才是真正的「课题一」核心：
  自然语言描述 → AI 推理几何 → 生成代码 → 执行 → 导出
"""
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import subprocess, tempfile, json
from pathlib import Path
from datetime import datetime

OUTPUT_DIR = Path(__file__).parent / "generated"
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_from_prompt(prompt: str) -> dict:
    """
    根据自然语言描述生成 build123d 代码 → 执行 → 导出模型

    这个函数本身由 AI Agent (k) 在对话中调用：
    1. k 理解用户需求
    2. k 生成 build123d Python 代码
    3. 保存到文件 → 执行 → 导出 STEP/STL
    4. 如果出错，k 分析错误，修正代码，重试
    """
    pass  # 由 Agent 在对话中直接生成代码


# ═══════════════════════════════════════════════════
# 真实 AI 驱动示例：以下代码由 k 直接生成
# ═══════════════════════════════════════════════════

def ai_generate_and_run(code: str, name: str) -> dict:
    """执行 AI 生成的 build123d 代码，导出模型"""
    ts = datetime.now().strftime("%H%M%S")
    script_path = OUTPUT_DIR / f"{name}_{ts}.py"
    script_path.write_text(code, encoding='utf-8')

    # 执行
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True, text=True, timeout=60,
        cwd=str(OUTPUT_DIR)
    )

    files = list(OUTPUT_DIR.glob(f"{name}*"))
    return {
        "name": name,
        "script": str(script_path),
        "success": result.returncode == 0,
        "stdout": result.stdout[-500:] if result.stdout else "",
        "stderr": result.stderr[-500:] if result.stderr else "",
        "files": [f.name for f in files],
        "files_detail": {f.name: f"{f.stat().st_size/1024:.1f}KB"
                         for f in files if f.suffix in ['.step', '.stl']}
    }


# ═══════════════════════════════════════════════════
# 🤖 AI 实时生成挑战:
# sora 说出任意零件描述 → k 立即生成代码 → 运行 → 导出
# ═══════════════════════════════════════════════════

if __name__ == "__main__":
    print("""
    ╔══════════════════════════════════════════╗
    ║   AI-CAD Pipeline v0.2                   ║
    ║   等待 sora 的自然语言输入...              ║
    ║                                          ║
    ║   使用方法:                               ║
    ║   1. 告诉 k 你想要什么零件                 ║
    ║   2. k 推理几何 + 生成 build123d 代码      ║
    ║   3. 自动执行 → STEP/STL 导出             ║
    ╚══════════════════════════════════════════╝
    """)

"""
AI-CAD Pipeline — 自然语言 → 3D 模型 Agent
将用户意图解析为 build123d 零件，自动生成 + 导出 + 报告
"""
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
from pathlib import Path
from parts_library import *

# 导出目录
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


class CADIntentParser:
    """解析用户输入 → 结构化零件描述"""

    # 意图词 → (函数, 参数映射)
    INTENT_MAP = {
        "法兰 flange": (flange, {
            "pipe_diameter": ["管径", "内径", "pipe"],
            "bolt_circle_dia": ["螺栓圆", "bolt_circle"],
            "thickness": ["厚度", "厚"],
            "bolt_holes": ["孔数", "螺孔数", "holes"],
        }),
        "螺栓 hex bolt": (hex_bolt, {
            "diameter": ["m", "直径", "diameter"],
            "length": ["长", "长度", "length"],
            "thread_pitch": ["螺距", "pitch"],
        }),
        "六角螺栓": (hex_bolt, {
            "diameter": ["m", "直径"],
            "length": ["长", "长度"],
            "thread_pitch": ["螺距"],
        }),
        "螺母 nut": (hex_nut, {
            "diameter": ["m", "直径", "diameter"],
        }),
        "垫圈 washer": (washer, {
            "diameter": ["m", "直径", "diameter"],
            "thickness": ["厚", "厚度", "thickness"],
        }),
        "支架 bracket l型": (l_bracket, {
            "width": ["宽", "宽度", "width"],
            "height": ["高", "高度", "height"],
            "thickness": ["厚", "板厚", "thickness"],
            "hole_dia": ["孔", "孔径", "hole"],
        }),
        "齿轮 gear": (spur_gear, {
            "teeth": ["齿数", "teeth", "齿"],
            "module": ["模数", "module"],
            "thickness": ["厚度", "厚"],
        }),
        "弹簧 spring": (coil_spring, {
            "outer_diameter": ["外径", "直径", "diameter"],
            "wire_diameter": ["线径", "丝径", "wire"],
            "coils": ["圈", "圈数", "coils"],
            "free_length": ["长", "高度", "length"],
        }),
    }

    @classmethod
    def parse(cls, text: str) -> dict:
        """解析用户文本 → (函数, 参数, 零件名)"""
        text_lower = text.lower()
        # 按匹配长度排序，优先匹配更具体的词
        best_match = None
        best_len = 0
        for intent_key in cls.INTENT_MAP:
            for kw in intent_key.split():
                if kw in text_lower and len(kw) > best_len:
                    best_len = len(kw)
                    best_match = intent_key

        if best_match:
            func, param_map = cls.INTENT_MAP[best_match]
            params = cls._extract_params(text, param_map)
            return {"function": func, "params": params,
                    "part_name": best_match.split()[0]}
        return None

    @staticmethod
    def _extract_params(text: str, param_map: dict) -> dict:
        """从文本中提取数值参数"""
        import re
        result = {}

        for param_name, keywords in param_map.items():
            for kw in keywords:
                # 模式1: 关键词在前，数字在后: "齿数 20"
                match = re.search(rf'{kw}\s*(\d+\.?\d*)', text, re.IGNORECASE)
                if match:
                    result[param_name] = float(match.group(1))
                    break
                # 模式2: 数字在前，关键词在后: "20 齿"
                match = re.search(rf'(\d+\.?\d*)\s*{kw}', text, re.IGNORECASE)
                if match:
                    result[param_name] = float(match.group(1))
                    break
                # 模式3: "M6" 提取直径
                if kw in ['m', '直径', 'diameter']:
                    m_match = re.search(r'\b[Mm](\d+\.?\d*)\b', text)
                    if m_match and param_name == 'diameter':
                        result[param_name] = float(m_match.group(1))
                        break

        return result


def generate_part(intent: dict, name_prefix: str = "part") -> dict:
    """执行 build123d 函数生成零件"""
    func = intent["function"]
    params = intent["params"]

    print(f"  🔧 调用: {func.__name__}({params})")
    part = func(**params)

    # 导出多种格式
    files = {}
    for fmt in ["step", "stl"]:
        filename = f"{name_prefix}.{fmt}"
        filepath = OUTPUT_DIR / filename
        if fmt == "step":
            export_step(part, str(filepath))
        else:
            export_stl(part, str(filepath))
        size_kb = filepath.stat().st_size / 1024
        files[fmt] = {"path": str(filepath), "size_kb": round(size_kb, 1)}
        print(f"  ✅ {filename} ({size_kb:.1f} KB)")

    return {
        "part": part,
        "files": files,
        "name": name_prefix,
    }


def run_pipeline(user_input: str) -> dict:
    """
    主 Pipeline: 自然语言 → 3D 模型

    示例输入:
      "我要一个 M6 螺栓，长度 30mm"
      "生成一个 20 齿模数 2 的齿轮"
      "做一个内径 50mm 厚 12mm 的法兰，6 个螺栓孔"

    返回: {
      "input": str,
      "intent": dict,
      "results": list of {part, files, name}
    }
    """
    print(f"\n{'='*60}")
    print(f"🎯 用户意图: {user_input}")
    print(f"{'='*60}")

    # Step 1: 意图解析
    print("\n📋 Step 1: 意图解析...")
    intent = CADIntentParser.parse(user_input)

    if not intent:
        print("  ❌ 无法识别的零件类型，支持:")
        for name in CADIntentParser.INTENT_MAP:
            print(f"     - {name.split()[0]}")
        return None

    print(f"  ✅ 识别为: {intent['part_name']}, 参数: {intent['params']}")

    # Step 2: 生成零件
    print("\n🔨 Step 2: 生成 3D 模型...")
    result = generate_part(intent, intent["part_name"])

    # Step 3: 质量报告
    print(f"\n📊 Step 3: 质量报告")
    print(f"  零件类型: {intent['part_name']}")
    print(f"  参数: {intent['params']}")
    print(f"  导出文件:")
    for fmt, info in result["files"].items():
        print(f"    {info['path']}")
    print(f"\n  🟢 Pipeline 完成! 文件在 output/ 目录")

    return {
        "input": user_input,
        "intent": intent,
        "results": [result],
    }


# ═══════════════════════════════════════════════════
# CLI / 测试
# ═══════════════════════════════════════════════════

if __name__ == "__main__":
    # 测试用例
    test_inputs = [
        "我要一个 M6 螺栓，长度 30",
        "生成一个 20 齿模数 2 厚度 10 的齿轮",
        "做一个内径 50 厚 12 的法兰，6 个螺栓孔",
        "M8 的螺母",
        "做一个宽 40 高 50 厚 5 的 L 型支架，4 个安装孔",
    ]

    if len(sys.argv) > 1:
        # 命令行模式
        user_text = " ".join(sys.argv[1:])
        run_pipeline(user_text)
    else:
        # 批量测试模式
        print("🏭 AI-CAD Pipeline — 批量测试")
        print(f"输出目录: {OUTPUT_DIR}\n")
        for inp in test_inputs:
            result = run_pipeline(inp)

        print(f"\n{'='*60}")
        print(f"🎉 全部完成! 共生成 {len(test_inputs)} 个零件")
        print(f"📁 输出目录: {OUTPUT_DIR}")
        for f in sorted(OUTPUT_DIR.glob("*")):
            size_kb = f.stat().st_size / 1024
            print(f"  📄 {f.name} ({size_kb:.1f} KB)")

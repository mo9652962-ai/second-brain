"""
AI-CAD Pipeline v0.3 — 装配 + 切片全自动
  自然语言 → 多零件装配 → STEP/STL → Cura 切片 → G-code
"""
import subprocess, sys, os, io, json, shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from pathlib import Path
from datetime import datetime

# 路径
OUTPUT = Path(__file__).parent / "output_assembly"
OUTPUT.mkdir(exist_ok=True)
CURA_ENGINE = Path(r"C:\Program Files\UltiMaker Cura 5.13.0\CuraEngine.exe")
CURA_CFG    = Path(r"C:\Program Files\UltiMaker Cura 5.13.0\share\cura\resources")

sys.path.insert(0, str(Path(__file__).parent))
from build123d import export_step, export_stl
from parts_library import hex_bolt, hex_nut, washer


def generate_assembly(description: str) -> dict:
    """
    一句话 → 多零件装配
    例: "M6 螺栓配螺母和垫圈"
    """
    print(f"\n{'='*50}")
    print(f"  Assembly: {description}")
    print(f"{'='*50}")

    # 识别组合意图
    parts_to_make = []
    text = description.lower()

    if "螺栓" in text or "bolt" in text:
        m = int(''.join(c for c in text.split('m')[1].split()[0] if c.isdigit()) if 'm' in text else '6')
        print(f"  → 识别: M{m} 螺栓")
        parts_to_make.append(("bolt", hex_bolt, {"diameter": m, "length": 30}))

    if "螺母" in text or "nut" in text:
        m = int(''.join(c for c in text.split('m')[1].split()[0] if c.isdigit()) if 'm' in text else '6')
        print(f"  → 识别: M{m} 螺母")
        parts_to_make.append(("nut", hex_nut, {"diameter": m}))

    if "垫圈" in text or "washer" in text:
        m = int(''.join(c for c in text.split('m')[1].split()[0] if c.isdigit()) if 'm' in text else '6')
        print(f"  → 识别: M{m} 垫圈")
        parts_to_make.append(("washer", washer, {"diameter": m}))

    results = []
    for name, func, params in parts_to_make:
        print(f"\n  🔨 生成 {name}...")
        part = func(**params)
        step_f = OUTPUT / f"{name}.step"
        stl_f  = OUTPUT / f"{name}.stl"
        export_step(part, str(step_f))
        export_stl(part, str(stl_f))
        results.append({"name": name, "step": str(step_f), "stl": str(stl_f),
                       "size_kb": stl_f.stat().st_size // 1024})
        print(f"  ✅ {name}.stl ({results[-1]['size_kb']} KB)")

    return {"parts": results, "count": len(results)}


def slice_to_gcode(stl_path: str, name: str = "print") -> str:
    """
    STL → G-code (PrusaSlicer CLI)
    """
    gcode_path = str(OUTPUT / f"{name}.gcode")
    print(f"\n  🔪 切片: {Path(stl_path).name} → {name}.gcode")

    try:
        result = subprocess.run([
            r"C:\Program Files\Prusa3D\PrusaSlicer\prusa-slicer-console.exe",
            "--export-gcode",
            "--output", gcode_path,
            stl_path
        ], capture_output=True, text=True, timeout=120)

        if Path(gcode_path).exists() and Path(gcode_path).stat().st_size > 100:
            size = Path(gcode_path).stat().st_size // 1024
            print(f"  ✅ {name}.gcode ({size} KB)")
            return gcode_path
        else:
            print(f"  ⚠️ 切片输出为空")
            return None
    except Exception as e:
        print(f"  ❌ 切片失败: {e}")
        return None


def full_pipeline(description: str):
    """
    完整流水线:
      描述 → 3D 模型 → STL → G-code → 报告
    """
    ts = datetime.now().strftime("%H%M%S")
    print(f"\n╔{'═'*48}╗")
    print(f"║  AI-CAD Pipeline v0.3 — 装配 + 切片全自动")
    print(f"╚{'═'*48}╝")

    # Step 1: 生成装配
    result = generate_assembly(description)

    if result["count"] == 0:
        print("  ❌ 未识别到任何零件")
        return

    # Step 2: 切片每个零件
    print(f"\n{'─'*50}")
    print(f"  Step 2: Cura 切片 ({result['count']} 个零件)")
    print(f"{'─'*50}")

    for part in result["parts"]:
        slice_to_gcode(part["stl"], part["name"])

    # Step 3: 报告
    print(f"\n{'─'*50}")
    print(f"  📊 最终报告")
    print(f"{'─'*50}")
    print(f"  输入: {description}")
    print(f"  零件数: {result['count']}")
    total_size = 0
    for f in sorted(OUTPUT.glob("*")):
        sz = f.stat().st_size
        total_size += sz
        unit = "KB" if sz < 1024*1024 else "MB"
        val = sz/1024 if sz < 1024*1024 else sz/1024/1024
        print(f"  {'📄' if f.suffix == '.step' else '🔧' if f.suffix == '.stl' else '🖨️'} {f.name} ({val:.1f} {unit})")
    print(f"\n  📁 输出目录: {OUTPUT}")
    print(f"  💾 总大小: {total_size/1024:.1f} KB")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        desc = " ".join(sys.argv[1:])
    else:
        desc = "M8 螺栓配螺母和垫圈"

    full_pipeline(desc)

# -*- coding: utf-8 -*-
"""回归测试：render_fan_3d.py（三维透视扇叶引擎）

【深挖阶段2 核心发现验证】
原版视频真正的"精致感"来源 = PowerPoint「三维旋转（透视：前部）」，不是平面旋转。
本测试用**像素级客观断言**验证三维投影引擎的正确性（不依赖视觉模型的主观描述）。

运行：python tests/test_fan_3d.py   （退出码 0=通过）
"""
import sys, os, math
import numpy as np
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SCRIPT_DIR)
import render_fan_3d as f3

P = F = 0
def check(name, cond, info=""):
    global P, F
    if cond:
        P += 1
        print(f"  ✅ {name}")
    else:
        F += 1
        print(f"  ❌ {name} {info}")

print("=== 1. 三维旋转矩阵 ===")
Rx = f3.rot_x(90)
v = np.array([[0.0, 1.0, 0.0]])  # 本地 y 轴向上
out = (Rx @ v.T).T[0]
check("rot_x(90°) 把 y 轴转到 z 轴", abs(out[2] - 1.0) < 1e-6 and abs(out[1]) < 1e-6, f"got {out}")

Rz = f3.rot_z(90)
outz = (Rz @ v.T).T[0]
check("rot_z(90°) 把 y 轴转到 -x 轴", abs(outz[0] + 1.0) < 1e-6, f"got {outz}")

print("\n=== 2. 透视投影（坐标符号正确性——曾修复的 bug）===")
# 本地 y 向上为正 → 屏幕 y 应向上（y 减小）
pts = np.array([[0.0, 100.0, 0.0]])  # 扇轴上方 100
proj = f3.project(pts, 1920, 1080, cx=960, cy=600, focal=3.2)
check("投影后 y 向上（屏幕 y 减小）", proj[0][1] < 600, f"got {proj[0]}")
check("投影后 x 居中", abs(proj[0][0] - 960) < 1, f"got {proj[0]}")

print("\n=== 3. 三维透视倾斜效果（核心：tilt_x 越大扇面越压缩）===")
W, H = 1920, 1080
cx, cy, radius = int(W*0.49), int(H*0.60), int(H*0.58)
n, span, gap = 6, 27.0, 1.5
total = n*(span+gap) - gap
start = 90 - total/2
angles = [(start + i*(span+gap), start + i*(span+gap) + span) for i in range(n)]

def mask_coverage(tilt_x):
    from PIL import ImageDraw
    R = f3.rot_z(0) @ f3.rot_x(tilt_x)
    m = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(m)
    for (a0, a1) in angles:
        p3 = f3.blade_polygon_3d(a0, a1, radius, 44)
        pr = (R @ p3.T).T
        d.polygon(f3.project(pr, W, H, cx, cy, 3.2), fill=255)
    a = np.asarray(m)
    ys, xs = np.nonzero(a > 128)
    return 100*(a > 128).sum()/a.size, (ys.min(), ys.max()) if len(ys) else (0, 0)

cov0, bb0 = mask_coverage(0)
cov18, bb18 = mask_coverage(18)
cov30, bb30 = mask_coverage(30)
check("平面态扇叶覆盖率 > 20%", cov0 > 20, f"cov={cov0:.1f}%")
check("tilt_x=18 产生透视压缩（覆盖率下降）", cov18 < cov0, f"{cov0:.1f}% → {cov18:.1f}%")
check("tilt_x=30 压缩更明显（单调递减）", cov30 < cov18, f"{cov18:.1f}% → {cov30:.1f}%")
check("扇叶位于扇轴上方（y 最大值 ≈ cy）", abs(bb0[1] - cy) < 5, f"maxY={bb0[1]} cy={cy}")

print("\n=== 4. 透光视差（扇内清晰 vs 扇外朦胧）===")
bg = f3.create_courtyard_bg_v3(1920, 1080)
check("背景 1920x1080 RGB", bg.size == (1920, 1080) and bg.mode == 'RGB')
bga = np.asarray(bg).astype(float)
check("背景内容丰富（std>25）", bga.std() > 25, f"std={bga.std():.1f}")

out = f3.render_fan_3d_v2(bg, True, tilt_x=30)
oa = np.asarray(out).astype(float)
# 扇内区（扇轴上方中央）应比扇外角落区对比度更高
inside = oa[200:500, 800:1100]
outside = oa[800:1080, 0:300]
check("扇内对比度 > 扇外（透光视差生效）", inside.std() > outside.std(),
      f"inside={inside.std():.1f} outside={outside.std():.1f}")

print("\n=== 5. 双态渲染 ===")
closed = f3.render_fan_3d_v2(bg, False, tilt_x=18)
opened = f3.render_fan_3d_v2(bg, True, tilt_x=18)
check("合拢/展开双态均成功渲染", closed.size == opened.size == (1920, 1080))
check("双态状态差有效", closed.tobytes() != opened.tobytes())

print(f"\n{'='*40}\n通过 {P} / 失败 {F}")
sys.exit(1 if F else 0)

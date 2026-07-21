"""
手机支架 — FreeCAD 原生 Part API
碳素钢风格: 薄壁金属感, 简洁线条
"""
import FreeCAD as App
import Part
import Mesh
from math import radians, sin, cos

doc = App.newDocument("PhoneStand")

# ═══ 参数 ═══
W, D, H = 80, 70, 6     # 底座
PH, PW = 20, 5           # 立柱 高+厚
AH, AW = 65, 25          # 背板 高+角度
SW = 3.5                 # 整体壁厚
a = radians(AW)

# ═══ 侧面轮廓 (一笔画) ═══
fy, by = -D/2, D/2
cz = H + PH
top_y = by - 3 - AH * sin(a)
top_z = cz + AH * cos(a)

# 顶点列表 (YZ平面)
pts = [
    App.Vector(0, fy, 0),           # 底前
    App.Vector(0, by, 0),           # 底后
    App.Vector(0, by-3, cz),        # 立柱顶
    App.Vector(0, top_y, top_z),    # 背板顶
    App.Vector(0, fy+6, cz),        # 前缘
    App.Vector(0, fy, 0),           # 闭合
]

# 创建线 → 面 → 实体
wire = Part.makePolygon(pts)
face = Part.Face(wire)
body = face.extrude(App.Vector(W/2, 0, 0))  # 往+X挤半宽
body2 = face.extrude(App.Vector(-W/2, 0, 0)) # 往-X挤半宽
body = body.fuse(body2)

# ═══ 减重三角 ×2 ═══
for side in [-1, 1]:
    sx = side * (W/2 - SW - 1)
    cut_pts = [
        App.Vector(sx, fy + 12, H + 1),
        App.Vector(sx, by - 6, H + 1),
        App.Vector(sx, by - 3 - AH*sin(a)*0.4, cz + AH*cos(a)*0.4),
        App.Vector(sx, fy + 12, H + 1),
    ]
    cut = Part.Face(Part.makePolygon(cut_pts)).extrude(
        App.Vector(-side * (W/2 - SW - 1), 0, 0))
    body = body.cut(cut)

# ═══ 手机托槽 (前唇) ═══
lip = Part.makeBox(W - 14, 5, 10, App.Vector(-(W-14)/2, fy + 2, cz))
body = body.fuse(lip)

# ═══ 线缆孔 ═══
cable = Part.makeCylinder(9, H + 4, App.Vector(0, fy + 14, -2))
body = body.cut(cable)

# ═══ 配重腔 ═══
cavity = Part.makeBox(W - 16, D - 12, 3, App.Vector(-(W-16)/2, -D/2+6, H-3))
body = body.cut(cavity)

# ═══ 防滑垫 ×4 ═══
for cx, cy in [(-W/2+12, fy+12), (W/2-12, fy+12), (-W/2+12, by-12), (W/2-12, by-12)]:
    pad = Part.makeCylinder(6, 2, App.Vector(cx, cy, -2))
    body = body.cut(pad)

# ═══ 导出 ═══
import os
out = os.path.dirname(os.path.abspath(__file__))
Part.export([body], os.path.join(out, "phone_stand_v8.step"))
Mesh.export([body], os.path.join(out, "phone_stand_v8.stl"))

vol = body.Volume / 1000  # cm³
weight = vol * 1.24       # PLA density
print(f"OK v8.step + v8.stl")
print(f"Volume: {vol:.1f} cm³, Weight: ~{weight:.0f}g PLA")
print(f"Material cost: ~¥{weight*0.06:.1f}")

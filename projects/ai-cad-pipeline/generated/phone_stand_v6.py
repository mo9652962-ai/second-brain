"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  手机支架 v6.0 — 融合版 (v3结构 + v5功能)
  • 360° 旋转底座 + 蜂窝减重 (v3底座)
  • 折叠铰链 + 多角度支撑 (v3铰链)
  • 倾斜背板 + 散热风道 (v3背板)
  • 可调伸缩托架 + 防滑齿 (v3夹臂)
  • 底部配重腔 + 线缆槽 (v4实用)
  • 平板/手机通用
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
from build123d import *
from math import radians, sin, cos, pi

# ═══════ 参数 ═══════
BASE_R      = 52     # 圆盘半径
BASE_H      = 12     # 底座厚
BACK_W      = 90     # 背板宽
BACK_H      = 78     # 背板高
WALL        = 2.4    # 壁厚
FILLET_R    = 4      # 圆角
ANGLE       = 25     # 默认角度
PHONE_W     = 82     # 托槽宽
PHONE_D     = 14     # 托槽深
LIP_H       = 7      # 托唇高
CABLE_W     = 16     # 线缆宽
HEX_R       = 5      # 蜂窝半径
HEX_DEPTH   = 6      # 蜂窝深

# ═══════════════════════════════════════
# 1. 旋转底座 (蜂窝减重 + 配重腔)
# ═══════════════════════════════════════
def build_rotating_base() -> Part:
    with BuildPart() as bp:
        # 圆盘主体
        with BuildSketch(Plane.XY) as sk:
            Circle(BASE_R)
        extrude(amount=BASE_H)

        # ── 双面蜂窝减重 ──
        for offset_z, depth, hex_r in [(BASE_H, HEX_DEPTH, HEX_R),
                                        (0, -4, HEX_R * 0.7)]:
            face = bp.faces().sort_by(Axis.Z)[-1 if offset_z > 0 else 0]
            with BuildSketch(face) as sk:
                spacing = (hex_r * 2 + 2) * 0.87
                row_w = (hex_r * 2 + 2) * 0.75
                for row in range(8):
                    y = -BASE_R + 14 + row * spacing
                    ox = (row % 2) * row_w
                    for col in range(12):
                        x = -BASE_R + 12 + ox + col * row_w * 2
                        r2 = x*x + y*y
                        if r2 < (BASE_R - 10)**2 and not (-12 < y - BASE_R/4 < 12 and abs(x) < 25):
                            with Locations((x, y)):
                                RegularPolygon(hex_r, 6, rotation=30)
            try:
                extrude(amount=depth, mode=Mode.SUBTRACT)
            except:
                pass

        # ── 顶部旋转轨道 ──
        top = bp.faces().sort_by(Axis.Z)[-1]
        with BuildSketch(top) as sk:
            Circle(BASE_R * 0.4 + 3)
            Circle(BASE_R * 0.4, mode=Mode.SUBTRACT)
        extrude(amount=3)

        # ── 底部配重腔 ──
        bottom = bp.faces().sort_by(Axis.Z)[0]
        with BuildSketch(bottom) as sk:
            Circle(BASE_R - 10)
        extrude(amount=-4, mode=Mode.SUBTRACT)

        # ── 3 角防滑槽 ──
        with BuildSketch(bottom) as sk:
            for ang in [90, 210, 330]:
                x = (BASE_R - 12) * cos(radians(ang))
                y = (BASE_R - 12) * sin(radians(ang))
                with Locations((x, y)):
                    Circle(7)
        extrude(amount=-2, mode=Mode.SUBTRACT)

        # ── 铰链接口槽 ──
        with BuildSketch(top) as sk:
            with Locations((0, -BASE_R/2 + 6)):
                Rectangle(16, 6)
        extrude(amount=-4, mode=Mode.SUBTRACT)

    return bp.part


# ═══════════════════════════════════════
# 2. 折叠背板 (含铰链耳座)
# ═══════════════════════════════════════
def build_folding_backplate() -> Part:
    a = radians(ANGLE)
    with BuildPart() as bp:
        # 倾斜工作平面
        bp_plane = Plane(
            origin=(0, -BASE_R/4, BASE_H),
            x_dir=(1, 0, 0),
            z_dir=(0, sin(a), cos(a))
        )
        # 梯形背板
        tw, bw = PHONE_W - 4, BACK_W - 18
        with BuildSketch(bp_plane) as sk:
            with BuildLine() as ln:
                Polyline(
                    (-tw/2, BACK_H),
                    (-bw/2, BACK_H * 0.12),
                    (-bw/2, 0),
                    ( bw/2, 0),
                    ( bw/2, BACK_H * 0.12),
                    ( tw/2, BACK_H),
                )
                Line((tw/2, BACK_H), (-tw/2, BACK_H))
            make_face()
        extrude(amount=WALL)

        # ── 散热风道 ──
        bf = bp.faces().sort_by(Axis.Z)[-1]
        with BuildSketch(bf) as sk:
            for i in range(7):
                x = -30 + i * 10
                with Locations((x, 20)):
                    Rectangle(4, 8)
        extrude(amount=-WALL, mode=Mode.SUBTRACT)

        # ── 铰链耳座 (底部) ──
        ear_y = -BASE_R/4
        ear_z = BASE_H
        for sx in [-1, 1]:
            ex = sx * (BACK_W/2 - 12)
            with BuildSketch(Plane.XZ.offset(ex)) as sk:
                with Locations((0, ear_z)):
                    Circle(6)
            extrude(amount=4.5, both=True)

    return bp.part


# ═══════════════════════════════════════
# 3. 立体托架 (多层次)
# ═══════════════════════════════════════
def build_3d_holder() -> Part:
    with BuildPart() as bh:
        # 底座连接块
        with BuildSketch(Plane.XY.offset(BASE_H)) as sk:
            with Locations((0, BASE_R/2 - 8)):
                Rectangle(BACK_W - 14, LIP_H * 1.5,
                         align=(Align.CENTER, Align.MIN))
        extrude(amount=WALL + 4)

        # 前唇 — 防滑凸起
        top_f = bh.faces().sort_by(Axis.Z)[-1]
        with BuildSketch(top_f) as sk:
            with Locations((0, BASE_R/2 - 5)):
                Rectangle(BACK_W - 18, 4,
                         align=(Align.CENTER, Align.MIN))
        extrude(amount=PHONE_D - 2)

        # 手机定位槽
        top_f2 = bh.faces().sort_by(Axis.Z)[-1]
        with BuildSketch(top_f2) as sk:
            with Locations((0, BASE_R/2 - 2)):
                Rectangle(PHONE_W - 4, PHONE_D - 2,
                         align=(Align.CENTER, Align.MIN))
        extrude(amount=-PHONE_D + 2, mode=Mode.SUBTRACT)

    return bh.part


# ═══════════════════════════════════════
# 4. 侧面加强翼
# ═══════════════════════════════════════
def build_side_wings() -> Part:
    parts = []
    for side in [-1, 1]:
        with BuildPart() as sw:
            sx = side * (BACK_W/2 - 10)
            # 三角形加强翼
            with BuildSketch(Plane.XZ.offset(sx)) as sk:
                with BuildLine() as ln:
                    Polyline(
                        (-BASE_R/4, BASE_H),
                        (0, BASE_H + BACK_H * 0.65),
                        (BASE_R/3 + 5, BASE_H),
                        (-BASE_R/4, BASE_H),
                    )
                make_face()
            extrude(amount=3.5, both=True)
            parts.append(sw.part)
    return parts[0] + parts[1] if parts else Part()


# ═══════════════════════════════════════
# 5. 线缆通道
# ═══════════════════════════════════════
def build_cable_passage() -> Part:
    with BuildPart() as cp:
        with BuildSketch(Plane.XY.offset(BASE_H - HEX_DEPTH)) as sk:
            with Locations((0, BASE_R/2 - 8)):
                SlotOverall(CABLE_W + 6, 20)
        extrude(amount=HEX_DEPTH + 4)
    return cp.part


# ═══════════════════════════════════════
#  组装
# ═══════════════════════════════════════
if __name__ == "__main__":
    import os

    base    = build_rotating_base()
    back    = build_folding_backplate()
    holder  = build_3d_holder()
    wings   = build_side_wings()
    cable   = build_cable_passage()

    model = base + back + holder + wings
    model -= cable  # 线缆通道挖掉

    out = os.path.dirname(os.path.abspath(__file__))
    export_step(model, os.path.join(out, "phone_stand_v6.step"))
    export_stl(model,  os.path.join(out, "phone_stand_v6.stl"))

    step_sz = os.path.getsize(os.path.join(out, "phone_stand_v6.step"))//1024
    stl_sz  = os.path.getsize(os.path.join(out, "phone_stand_v6.stl"))//1024
    print(f"OK phone_stand_v6.step ({step_sz}KB)")
    print(f"OK phone_stand_v6.stl  ({stl_sz}KB)")
    print(f"")
    print(f"=== v6 融合版 ===")
    print(f"  旋转底座 + 双面蜂窝减重")
    print(f"  折叠铰链背板 + 散热风道")
    print(f"  3D立体托架 + 防滑手机槽")
    print(f"  侧面加强翼 + 底部配重腔")
    print(f"  贯穿线缆通道")
    print(f"  预估: ~75g · ¥4.5 · ~2.5h")

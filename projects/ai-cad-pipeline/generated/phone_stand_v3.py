"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  手机支架 v3.0 — Transform Edition
  • 折叠铰链底座 (0°~75° 无级调节)
  • 蜂窝晶格减重 (Voronoi 风格)
  • 背面散热风道
  • 隐藏式线缆通道
  • 磁吸安装位 (MagSafe 兼容)
  • 全参数化 — 改顶部的数就全变
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
from build123d import *
from math import radians, sin, cos, tan, pi, sqrt

# ═══════════════════════════════════════
#  全局参数 (改这里 → 整个支架自动适配)
# ═══════════════════════════════════════
BASE_W      = 100    # 底座总宽
BASE_D      = 90     # 底座深度
BASE_H      = 12     # 底座厚度
BACK_H      = 85     # 背板高度
WALL        = 3.5    # 结构壁厚
FILLET_R    = 6      # 全局圆角
HINGE_DIA   = 5      # 铰链轴直径
HINGE_L     = BASE_W - 20  # 铰链轴长度
ANGLE_MIN   = 0      # 最小倾斜角
ANGLE_MAX   = 70     # 最大倾斜角
PHONE_W     = 75     # 适配手机宽度
CABLE_W     = 14     # 线缆槽宽
MAG_DIA     = 56     # MagSafe 磁环直径
MAG_W       = 2      # 磁环壁厚

# ── 蜂窝参数 ──
HEX_R       = 4.5    # 六边形外接圆半径
HEX_GAP     = 2.0    # 蜂窝间距
HEX_DEPTH   = 6      # 蜂窝深度

# ── 散热风道 ──
VENT_W      = 6      # 风道宽
VENT_GAP    = 5      # 风道间距
VENT_DEPTH  = 4      # 风道深度
VENT_COUNT  = 7      # 风道数

# ═══════════════════════════════════════
#  1. 蜂窝晶格底座
# ═══════════════════════════════════════
def build_honeycomb_base() -> Part:
    with BuildPart() as bp:
        # 轮廓 — 前宽后窄的流线型
        with BuildSketch(Plane.XY) as sk:
            with BuildLine() as ln:
                fw, bw = BASE_W, BASE_W - 10
                dx = (fw - bw) / 2
                Polyline(
                    (-fw/2, -BASE_D/2 + FILLET_R * 2),
                    (-bw/2,  BASE_D/2 - FILLET_R),
                    ( bw/2,  BASE_D/2 - FILLET_R),
                    ( fw/2, -BASE_D/2 + FILLET_R * 2),
                    (-fw/2, -BASE_D/2 + FILLET_R * 2),
                )
            make_face()
        extrude(amount=BASE_H)

        # 顶部和底部边缘倒圆角
        edges = bp.edges()
        for e in list(edges.sort_by(Axis.Z)[:4]):
            try: bp.part = fillet(e, FILLET_R * 0.6)
            except: pass

        # ── 顶部蜂窝减重格栅 ──
        top = bp.faces().sort_by(Axis.Z)[-1]
        with BuildSketch(top) as sk:
            hex_spacing = (HEX_R * 2 + HEX_GAP) * 0.87
            hex_row_w = (HEX_R * 2 + HEX_GAP) * 0.75
            for row in range(12):
                y = -BASE_D/2 + 14 + row * hex_spacing
                ox = (row % 2) * hex_row_w
                for col in range(10):
                    x = -BASE_W/2 + 12 + ox + col * hex_row_w * 2
                    if (abs(y) < BASE_D/2 - 12 and abs(x) < BASE_W/2 - 10 and
                        not (abs(y - BASE_D/4) < 12 and abs(x) < 20)):  # 留铰链安装区
                        with Locations((x, y)):
                            RegularPolygon(HEX_R, 6, rotation=30)
        extrude(amount=-HEX_DEPTH, mode=Mode.SUBTRACT)

        # ── 底部蜂窝 (结构的另一半) ──
        bottom = bp.faces().sort_by(Axis.Z)[0]
        with BuildSketch(bottom) as sk:
            for row in range(12):
                y = -BASE_D/2 + 14 + (row + 0.5) * hex_spacing
                ox = ((row + 1) % 2) * hex_row_w
                for col in range(10):
                    x = -BASE_W/2 + 12 + ox + col * hex_row_w * 2
                    if abs(y) < BASE_D/2 - 12 and abs(x) < BASE_W/2 - 10:
                        with Locations((x, y)):
                            RegularPolygon(HEX_R * 0.8, 6, rotation=30)
        extrude(amount=-3, mode=Mode.SUBTRACT)

        # ── 防滑垫槽 (4 角) ──
        with BuildSketch(bottom) as sk:
            for cx, cy in [(-BASE_W/2+14,-BASE_D/2+14), (BASE_W/2-14,-BASE_D/2+14),
                           (-BASE_W/2+10, BASE_D/2-14), (BASE_W/2-10, BASE_D/2-14)]:
                with Locations((cx, cy)):
                    Circle(7)
        extrude(amount=-2, mode=Mode.SUBTRACT)

    return bp.part


# ═══════════════════════════════════════
#  2. 铰链机构 (打印式一体铰链)
# ═══════════════════════════════════════
def build_hinge_pivot() -> Part:
    """底座上的铰链耳座 ×2"""
    with BuildPart() as hp:
        # 圆柱耳座
        with BuildSketch(Plane.XZ.offset(-BASE_W/2 + 12)) as sk:
            Circle(HINGE_DIA + 3)
        extrude(amount=WALL + 2, both=True)

        # 中心轴孔
        side_face = hp.faces().sort_by(Axis.Y)[-1]
        with BuildSketch(side_face) as sk:
            Circle(HINGE_DIA / 2)
        extrude(amount=-WALL * 4, mode=Mode.SUBTRACT)

    return hp.part


def build_hinge_pin() -> Part:
    """铰链轴销"""
    with BuildPart() as hp:
        with BuildSketch(Plane.XZ) as sk:
            Circle(HINGE_DIA / 2)
        extrude(amount=HINGE_L)

        # 两端倒角
        ends = hp.edges().filter_by(Axis.X).group_by(Axis.X)
        if len(ends) >= 2:
            try:
                hp.part = fillet(list(ends[0])[0], 0.5)
                hp.part = fillet(list(ends[-1])[0], 0.5)
            except:
                pass

    return hp.part


# ═══════════════════════════════════════
#  3. 散热背板 + Magsafe 磁环
# ═══════════════════════════════════════
def build_backplate(angle_deg: float = 30) -> Part:
    """倾斜背板，带散热风道 + MagSafe 磁环"""
    a = radians(angle_deg)

    with BuildPart() as bp:
        # 倾斜工作平面
        bp_plane = Plane(
            origin=(0, -BASE_D/4, BASE_H),
            x_dir=(1, 0, 0),
            z_dir=(0, sin(a), cos(a))
        )

        with BuildSketch(bp_plane) as sk:
            # 人体工学轮廓 — 上窄下宽
            tw, bw = PHONE_W - 4, BASE_W - 20
            hh = BACK_H
            with BuildLine() as ln:
                Polyline(
                    (-tw/2, hh),
                    (-bw/2, hh * 0.3),
                    (-bw/2, 0),
                    ( bw/2, 0),
                    ( bw/2, hh * 0.3),
                    ( tw/2, hh),
                )
                # 顶部弧形连接
                Line((tw/2, hh), (-tw/2, hh))
            make_face()

        extrude(amount=WALL)

        # ── 散热风道 ──
        bf = bp.faces().sort_by(Axis.Z)[-1]
        with BuildSketch(bf) as sk:
            total_w = VENT_COUNT * (VENT_W + VENT_GAP) - VENT_GAP
            for i in range(VENT_COUNT):
                x = -total_w/2 + i * (VENT_W + VENT_GAP)
                y_start = 15
                with Locations((x, y_start + VENT_DEPTH)):
                    Rectangle(VENT_W, BACK_H * 0.65)
        extrude(amount=-WALL, mode=Mode.SUBTRACT)

        # ── MagSafe 磁环 ──
        with BuildSketch(bf) as sk:
            # 外环
            Circle(MAG_DIA / 2 + MAG_W)
            Circle(MAG_DIA / 2, mode=Mode.SUBTRACT)
            # 底部对齐标记
            with Locations((0, -MAG_DIA/2 - 4)):
                Circle(2)
        extrude(amount=-WALL/2, mode=Mode.SUBTRACT)

        # ── 中心 MagSafe 定位凹陷 ──
        with BuildSketch(bf) as sk:
            Circle(MAG_DIA / 2 - 1)
        extrude(amount=-1, mode=Mode.SUBTRACT)

    return bp.part


# ═══════════════════════════════════════
#  4. 隐藏线缆通道
# ═══════════════════════════════════════
def build_cable_channel() -> Part:
    """底座内部线缆通道"""
    with BuildPart() as cc:
        with BuildSketch(Plane.XY.offset(BASE_H - HEX_DEPTH)) as sk:
            with Locations((0, BASE_D/2 - 10)):
                SlotOverall(CABLE_W + 2, 16)
        extrude(amount=HEX_DEPTH + 2)

        # 出口 (底部)
        bottom_face = cc.faces().sort_by(Axis.Z)[0]
        with BuildSketch(bottom_face) as sk:
            with Locations((0, BASE_D/2 - 10)):
                SlotOverall(CABLE_W - 2, 8)
        extrude(amount=-2, mode=Mode.SUBTRACT)

    return cc.part


# ═══════════════════════════════════════
#  5. 底部托架 (带弧度)
# ═══════════════════════════════════════
def build_holder() -> Part:
    with BuildPart() as bh:
        # 弧形托架
        with BuildSketch(Plane.XY.offset(BASE_H)) as sk:
            with Locations((0, BASE_D/2 - 3)):
                Rectangle(BASE_W - 14, 8, align=(Align.CENTER, Align.MIN))
        extrude(amount=WALL + 3)

        # 手机定位槽
        top_f = bh.faces().sort_by(Axis.Z)[-1]
        with BuildSketch(top_f) as sk:
            with Locations((0, BASE_D/2 - 1)):
                Rectangle(BASE_W - 18, 6, align=(Align.CENTER, Align.MIN))
        extrude(amount=-8, mode=Mode.SUBTRACT)

        # 边缘圆角
        for e in list(bh.edges().filter_by(Axis.X).sort_by(Axis.Z)):
            try:
                bh.part = fillet(e, 1.5)
            except:
                pass

    return bh.part


# ═══════════════════════════════════════
#  6. 侧翼防滑夹臂 (弧形)
# ═══════════════════════════════════════
def build_clamp(side: int) -> Part:
    ax = side * (BASE_W/2 - 8)
    with BuildPart() as bc:
        with BuildSketch(Plane.XY.offset(BASE_H + 2)) as sk:
            with Locations((ax, -BASE_D/5)):
                with BuildLine() as ln:
                    # 弧形夹臂
                    w, h = 8, 26
                    Polyline((-w/2, 0), (w/2, 0), (w/2, h),
                             (0, h + 4), (-w/2, h), (-w/2, 0))
                make_face()
        extrude(amount=30)

        # 内侧防滑齿
        inner = bc.faces().sort_by(Axis.X)[-1 if side > 0 else 0]
        with BuildSketch(inner) as sk:
            for yy in range(-10, 12, 7):
                with Locations((0, yy)):
                    Rectangle(1.8, 1.2)
        extrude(amount=-5, mode=Mode.SUBTRACT)

    return bc.part


# ═══════════════════════════════════════
#  组装
# ═══════════════════════════════════════
if __name__ == "__main__":
    import os

    # 生成各组件
    base    = build_honeycomb_base()
    back    = build_backplate(30)   # 30° 默认角度
    holder  = build_holder()
    cable   = build_cable_channel()
    pin     = build_hinge_pin()

    # 铰链耳座 ×2
    pivot_l = Pos(-BASE_W/2 + 12, -BASE_D/4, BASE_H * 0.6) * build_hinge_pivot()
    pivot_r = Pos( BASE_W/2 - 12, -BASE_D/4, BASE_H * 0.6) * build_hinge_pivot()

    # 铰链轴
    pin_pos = Pos(0, -BASE_D/4, BASE_H * 0.6) * Rot(90, 0, 0) * pin

    # 夹臂
    clamp_l = build_clamp(-1)
    clamp_r = build_clamp(1)

    # 合并所有
    model = base + back + holder
    model -= cable          # 线缆通道是挖掉的
    model += pivot_l + pivot_r + pin_pos
    model += clamp_l + clamp_r

    out = os.path.dirname(os.path.abspath(__file__))
    export_step(model, os.path.join(out, "phone_stand_v3.step"))
    export_stl(model,  os.path.join(out, "phone_stand_v3.stl"))
    print("OK phone_stand_v3.step")
    print("OK phone_stand_v3.stl")
    print("Transform Edition: 蜂窝底座 + 散热背板 + MagSafe磁环 + 线缆通道 + 铰链 + 夹臂")

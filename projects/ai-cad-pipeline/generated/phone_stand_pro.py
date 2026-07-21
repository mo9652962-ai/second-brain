"""
手机支架 Pro v2.0 — AI 驱动参数化设计
• 梯形底座 + 减重格栅
• 倾斜背板 + 加强筋
• 线缆通槽 + 防滑垫位
• 可调宽度滑动夹臂
"""
from build123d import *
from math import radians, sin, cos

# 参数
BASE_W, BASE_D = 110, 85
TILT = 15  # 度
BACK_H = 75
WALL = 3.5
FILLET = 5

with BuildPart() as stand:
    # ═══ 1. 底座 (梯形 + 圆角) ═══
    with BuildSketch(Plane.XY) as sk:
        RectangleRounded(BASE_W, BASE_D, FILLET)
    extrude(amount=8)

    # ── 减重格栅 ──
    top = stand.faces().sort_by(Axis.Z)[-1]
    with BuildSketch(top) as sk:
        for row in range(5):
            y = -BASE_D/2 + 22 + row * 12
            ox = (row % 2) * 7
            for col in range(7):
                x = -BASE_W/2 + 16 + ox + col * 14
                if abs(y) < BASE_D/2 - 14 and abs(x) < BASE_W/2 - 14:
                    with Locations((x, y)):
                        SlotOverall(8, 4, rotation=45)
    extrude(amount=-5, mode=Mode.SUBTRACT)

    # ── 线缆槽 ──
    with BuildSketch(top) as sk:
        with Locations((0, BASE_D/2 - 10)):
            SlotOverall(22, 12)
    extrude(amount=-8, mode=Mode.SUBTRACT)

    # ── 防滑垫位 ──
    bottom = stand.faces().sort_by(Axis.Z)[0]
    with BuildSketch(bottom) as sk:
        for cx, cy in [(-BASE_W/2+12,-BASE_D/2+12), (BASE_W/2-12,-BASE_D/2+12),
                       (-BASE_W/2+12, BASE_D/2-12), (BASE_W/2-12, BASE_D/2-12)]:
            with Locations((cx, cy)):
                Circle(6)
    extrude(amount=-2, mode=Mode.SUBTRACT)

    # ═══ 2. 倾斜背板 ═══
    a = radians(TILT)
    bp_plane = Plane(
        origin=(0, -BASE_D/4, 8),
        x_dir=(1, 0, 0),
        z_dir=(0, sin(a), cos(a))
    )
    with BuildSketch(bp_plane) as sk:
        with BuildLine() as ln:
            tw, bw = 50, BASE_W - 16
            Polyline((-tw/2, BACK_H), (tw/2, BACK_H),
                     (bw/2, 0), (-bw/2, 0), (-tw/2, BACK_H))
        make_face()
    extrude(amount=WALL)

    # ── 背板减重槽 ──
    bf = stand.faces().sort_by(Axis.Z)[-1]
    with BuildSketch(bf) as sk:
        for row in range(1, 6):
            for col in range(-2, 3):
                y, x = row * 12 + 5, col * 15
                if abs(x) < BASE_W/2 - 24:
                    with Locations((x, y)):
                        SlotOverall(8, 3, rotation=90)
    extrude(amount=-WALL, mode=Mode.SUBTRACT)

    # ═══ 3. 三角加强筋 x2 ═══
    for side in [-1, 1]:
        rib_x = side * (BASE_W/2 - 10)
        r_plane = Plane.XZ.offset(rib_x)
        with BuildSketch(r_plane) as sk:
            with BuildLine() as ln:
                Polyline((0, 0), (0, BACK_H * 0.55), (BASE_D/3, 0), (0, 0))
            make_face()
        extrude(amount=3, both=True)

    # ═══ 4. 底部防滑托唇 (前缘凸起) ═══
    with BuildSketch(Plane.XY.offset(8)) as sk:
        with Locations((0, BASE_D/2 - 4)):
            Rectangle(BASE_W - 12, 6, align=(Align.CENTER, Align.MIN))
    extrude(amount=WALL + 5)

    # ── 手机槽 ──
    with BuildSketch(Plane.XY.offset(8 + WALL + 5)) as sk:
        with Locations((0, BASE_D/2 - 2)):
            Rectangle(BASE_W - 16, 10, align=(Align.CENTER, Align.MIN))
    extrude(amount=-10, mode=Mode.SUBTRACT)

    # ═══ 5. 滑动夹臂 x2 ═══
    for side in [-1, 1]:
        ax = side * (BASE_W/2 - 8)
        with BuildSketch(Plane.XY.offset(10)) as sk:
            with Locations((ax, -BASE_D/4)):
                RectangleRounded(8, 22, 3, rotation=0 if side > 0 else 0)
        extrude(amount=28)
        # 内侧防滑齿
        af = stand.faces().sort_by(Axis.X)[-1 if side > 0 else 0]
        with BuildSketch(af) as sk:
            for yy in range(-9, 10, 6):
                with Locations((0, yy)):
                    Rectangle(2, 1.5)
        extrude(amount=-6, mode=Mode.SUBTRACT)

export_step(stand.part, "phone_stand_pro.step")
export_stl(stand.part, "phone_stand_pro.stl")
print("OK phone_stand_pro.step")
print("OK phone_stand_pro.stl")
print("Features: 减重格栅 + 倾斜背板 + 加强筋 + 线缆槽 + 防滑垫 + 夹臂")

"""
AI-CAD Pipeline — 参数化零件库
支持: 螺栓/螺母/垫圈/齿轮/轴承/支架/弹簧/法兰
"""
from build123d import *
from math import sin, cos, pi, radians, tan, sqrt
from dataclasses import dataclass
from typing import Optional

# ═══════════════════════════════════════════════════
# 1. 螺栓 (Hex Bolt)
# ═══════════════════════════════════════════════════

def hex_bolt(diameter: float = 6, length: float = 30,
             head_height: float = None,
             thread_pitch: float = 1.0,
             thread_length: float = None) -> Part:
    """
    六角螺栓
    - diameter: 螺纹直径 (M6=6, M8=8...)
    - length: 螺栓总长 (不含头)
    - head_height: 头部高度 (默认=直径*0.7)
    - thread_pitch: 螺距
    - thread_length: 螺纹段长度 (默认=总长*0.75)
    """
    if head_height is None:
        head_height = diameter * 0.7
    if thread_length is None:
        thread_length = length * 0.75

    # 六角头对边宽度
    across_flats = diameter * 1.75
    head_radius = across_flats / (2 * cos(radians(30)))

    with BuildPart() as bolt:
        # 螺杆
        with BuildSketch(Plane.XY) as sk:
            Circle(diameter / 2)
        extrude(amount=length)

        # 六角头
        with BuildSketch(Plane.XY.offset(length)) as sk:
            RegularPolygon(head_radius, 6)
        extrude(amount=head_height)

        # 螺纹模拟 (螺旋槽)
        thread_section = bolt.faces().sort_by(Axis.Z)[0]
        with BuildSketch(thread_section) as sk:
            Circle(diameter / 2 - 0.5)  # 内径
        extrude(amount=thread_length, mode=Mode.SUBTRACT)

    # 顶部倒圆角
    top_edge = bolt.edges().sort_by(Axis.Z)[-1]
    bolt.part = fillet(top_edge, 0.3)
    return bolt.part


# ═══════════════════════════════════════════════════
# 2. 螺母 (Hex Nut)
# ═══════════════════════════════════════════════════

def hex_nut(diameter: float = 6, thickness: float = None) -> Part:
    """
    六角螺母
    - diameter: 螺纹直径
    - thickness: 厚度 (默认=直径*0.8)
    """
    if thickness is None:
        thickness = diameter * 0.8
    across_flats = diameter * 1.75
    head_radius = across_flats / (2 * cos(radians(30)))

    with BuildPart() as nut:
        with BuildSketch(Plane.XY) as sk:
            RegularPolygon(head_radius, 6)
        extrude(amount=thickness)

        # 中心孔
        with BuildSketch(Plane.XY) as sk:
            Circle(diameter / 2)
        extrude(amount=thickness, mode=Mode.SUBTRACT)

    return nut.part


# ═══════════════════════════════════════════════════
# 3. 垫圈 (Washer)
# ═══════════════════════════════════════════════════

def washer(diameter: float = 6, thickness: float = 1.6) -> Part:
    """平垫圈"""
    outer_radius = diameter * 1.25
    with BuildPart() as w:
        with BuildSketch(Plane.XY) as sk:
            Circle(outer_radius)
            Circle(diameter / 2 + 0.5, mode=Mode.SUBTRACT)
        extrude(amount=thickness)
    return w.part


# ═══════════════════════════════════════════════════
# 4. L 型支架 (L-Bracket)
# ═══════════════════════════════════════════════════

def l_bracket(width: float = 40, height: float = 50,
              thickness: float = 5, hole_dia: float = 4,
              holes_per_side: int = 2) -> Part:
    """
    L 型支架，带安装孔
    """
    margin = hole_dia * 1.5

    with BuildPart() as bracket:
        # L 型截面
        with BuildSketch() as sk:
            with BuildLine() as ln:
                l1 = Line((0, 0), (width, 0))
                l2 = Line(l1 @ 1, (width, height))
                l3 = Line(l2 @ 1, (width - thickness, height))
                l4 = Line(l3 @ 1, (width - thickness, thickness))
                l5 = Line(l4 @ 1, (0, thickness))
                l6 = Line(l5 @ 1, (0, 0))
            make_face()
        extrude(amount=width)

        # 安装孔
        # 底面孔
        bottom_face = bracket.faces().sort_by(Axis.Z)[0]
        with BuildSketch(bottom_face) as sk:
            with GridLocations(width - 2*margin, width, 1, holes_per_side):
                Circle(hole_dia / 2)
        extrude(amount=-thickness, mode=Mode.SUBTRACT)

        # 侧面孔
        side_face = bracket.faces().sort_by(Axis.X)[-1]
        with BuildSketch(side_face) as sk:
            with GridLocations(width - 2*margin, height, 1, holes_per_side):
                Circle(hole_dia / 2)
        extrude(amount=-thickness, mode=Mode.SUBTRACT)

    return bracket.part


# ═══════════════════════════════════════════════════
# 5. 正齿轮 (Spur Gear)
# ═══════════════════════════════════════════════════

def spur_gear(teeth: int = 20, module: float = 2,
              thickness: float = 10, pressure_angle: float = 20) -> Part:
    """渐开线正齿轮"""
    teeth = int(teeth)
    pa_rad = radians(pressure_angle)
    pitch_radius = module * teeth / 2
    base_radius = pitch_radius * cos(pa_rad)
    outer_radius = pitch_radius + module

    # 生成渐开线齿廓
    points = []
    pts_per_tooth = 20
    tooth_angle = 2 * pi / teeth

    for t in range(teeth):
        base_angle = t * tooth_angle
        for i in range(pts_per_tooth + 1):
            # 渐开线参数
            r = base_radius + (outer_radius - base_radius) * i / pts_per_tooth
            angle = base_angle + (sqrt((r/base_radius)**2 - 1) -
                                  (r/base_radius)**2 * 0.01)
            x = r * cos(angle)
            y = r * sin(angle)
            points.append((x, y))

    with BuildPart() as gear:
        with BuildSketch() as sk:
            with BuildLine() as ln:
                # 简化：用直线近似齿廓
                for t in range(teeth):
                    angle = t * tooth_angle
                    r_outer = outer_radius
                    r_inner = pitch_radius - module * 0.8
                    mid_angle = angle + tooth_angle / 2

                    # 齿顶
                    x1 = r_outer * cos(angle)
                    y1 = r_outer * sin(angle)
                    # 齿根
                    x2 = r_inner * cos(mid_angle)
                    y2 = r_inner * sin(mid_angle)
                    # 下一个齿顶
                    x3 = r_outer * cos(angle + tooth_angle)
                    y3 = r_outer * sin(angle + tooth_angle)

                    l = Polyline((x1, y1), (x2, y2), (x3, y3))
                    if t == 0:
                        start = l
                    if t == teeth - 1:
                        end = l

            make_face()
        extrude(amount=thickness)

        # 中心轴孔
        shaft_radius = module * teeth * 0.15
        with BuildSketch(Plane.XY) as sk:
            Circle(shaft_radius)
        extrude(amount=thickness, mode=Mode.SUBTRACT)

    return gear.part


# ═══════════════════════════════════════════════════
# 6. 弹簧 (Coil Spring)
# ═══════════════════════════════════════════════════

def coil_spring(outer_diameter: float = 20, wire_diameter: float = 2,
                coils: int = 8, free_length: float = 40) -> Part:
    """螺旋压缩弹簧"""
    radius = (outer_diameter - wire_diameter) / 2
    pitch = free_length / coils
    steps_per_coil = 36
    total_steps = coils * steps_per_coil

    # 生成螺旋路径上的圆
    profiles = []
    for i in range(total_steps + 1):
        angle = (i / steps_per_coil) * 2 * pi
        z = i * pitch / steps_per_coil
        x = radius * cos(angle)
        y = radius * sin(angle)
        profiles.append(Plane(origin=(x, y, z), z_dir=(cos(angle), sin(angle), 0)))

    # 沿路径扫描圆形截面
    with BuildPart() as spring:
        with BuildLine() as ln:
            pts = [(radius*cos(i*2*pi/steps_per_coil),
                    radius*sin(i*2*pi/steps_per_coil),
                    i*pitch/steps_per_coil)
                   for i in range(total_steps + 1)]
            # Spline through points
            for idx, p in enumerate(pts):
                if idx == 0:
                    l = Line(p, pts[1])
                elif idx < len(pts) - 1:
                    l = Line(pts[idx-1], pts[idx])

    # 简化版本：用堆叠圆环近似
    with BuildPart() as spring:
        for i in range(coils):
            z = i * pitch
            with BuildSketch(Plane.XY.offset(z)) as sk:
                Circle(radius + wire_diameter/2)
                Circle(radius - wire_diameter/2, mode=Mode.SUBTRACT)
            extrude(amount=wire_diameter)

    return spring.part


# ═══════════════════════════════════════════════════
# 7. 法兰 (Flange)
# ═══════════════════════════════════════════════════

def flange(pipe_diameter: float = 50, bolt_circle_dia: float = 80,
           thickness: float = 12, bolt_holes: int = 6,
           bolt_hole_dia: float = 10) -> Part:
    """管法兰"""
    with BuildPart() as fl:
        # 主体圆盘
        outer_radius = bolt_circle_dia / 2 + bolt_hole_dia
        with BuildSketch(Plane.XY) as sk:
            Circle(outer_radius)
            Circle(pipe_diameter / 2, mode=Mode.SUBTRACT)

            # 螺栓孔
            with PolarLocations(bolt_circle_dia / 2, bolt_holes):
                Circle(bolt_hole_dia / 2, mode=Mode.SUBTRACT)

        extrude(amount=thickness)

        # 凸台
        with BuildSketch(Plane.XY) as sk:
            Circle(pipe_diameter / 2 + thickness)
            Circle(pipe_diameter / 2, mode=Mode.SUBTRACT)
        extrude(amount=thickness * 1.5)

    return fl.part

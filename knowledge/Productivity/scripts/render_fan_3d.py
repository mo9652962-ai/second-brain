# -*- coding: utf-8 -*-
"""扇叶开场 v3.1：正确的三维投影引擎

【修正 v3.0 的错误】v3.0 把整幅画布做了透视变换（背景也被扭曲）。
正确做法：只有扇叶形状做三维旋转，背景保持平面。

【核心算法】逐片计算扇叶的三维投影多边形：
1. 扇叶在本地平面（z=0）上是一个扇形切片
2. 施加 3D 旋转矩阵（绕 X 轴 tilt_x、绕 Z 轴 tilt_z）
3. 透视投影到 2D 平面
4. 用投影后的多边形裁剪背景（PIL mask）

这样才能得到真实的空间纵深感，且背景不受影响。
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def rot_x(deg):
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    return np.array([[1, 0, 0], [0, c, -s], [0, s, c]])


def rot_y(deg):
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    return np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])


def rot_z(deg):
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])


def project(points_3d, W, H, cx, cy, focal=3.2):
    """透视投影：3D 点 → 2D 屏幕坐标

    points_3d: (N,3) 以扇轴为原点的三维坐标
    focal: 视距倍数（越大透视越弱）
    """
    out = []
    d = focal * H  # 视距
    for x, y, z in points_3d:
        zz = d + z
        if zz < 1:
            zz = 1
        scale = d / zz
        # 本地坐标 y 向上为正，屏幕 y 向下为正 → 取负
        out.append((cx + x * scale, cy - y * scale))
    return out


def blade_polygon_3d(a_start, a_end, radius, samples=40):
    """生成一片扇叶在本地平面（z=0）的多边形顶点（3D 坐标）

    本地坐标：原点=扇轴，x 向右，y 向上，z 垂直屏幕向外
    """
    pts = [(0.0, 0.0, 0.0)]  # 扇轴顶点
    for i in range(samples + 1):
        ang = math.radians(a_start + (a_end - a_start) * i / samples)
        # 本地平面角：以 y 轴向上为 90°（数学坐标系）
        pts.append((radius * math.cos(ang), radius * math.sin(ang), 0.0))
    return np.array(pts)


def render_fan_3d_v2(base_img, is_opened=True,
                     cx_ratio=0.49, cy_ratio=0.60,
                     radius_ratio=0.58,
                     n_blades=6, blade_span=27.0, gap=1.5,
                     tilt_x=18.0, tilt_y=0.0, tilt_z=0.0,
                     focal=3.2, soften_px=7,
                     shadow=True):
    """渲染三维透视扇叶（正确版：只变换扇叶，背景保持平面）

    坐标约定：本地平面用数学坐标系（y 向上，0°=右，90°=上）
    tilt_x: 绕水平轴倾斜（正 = 扇面顶部向后倒，产生俯视纵深）
    tilt_z: 画面内旋转
    """
    W, H = base_img.size
    cx, cy = int(W * cx_ratio), int(H * cy_ratio)
    radius = int(H * radius_ratio)

    # 本地平面角度（数学系，上半圆）
    total = n_blades * (blade_span + gap) - gap
    start = 90 - total / 2  # 以 90°（正上）为中心
    if is_opened:
        angles = [(start + i * (blade_span + gap), start + i * (blade_span + gap) + blade_span)
                  for i in range(n_blades)]
    else:
        # 合拢：全部叠到最右一片的位置
        last = start + (n_blades - 1) * (blade_span + gap)
        angles = [(last, last + blade_span) for _ in range(n_blades)]

    # 组合旋转矩阵
    R = rot_z(tilt_z) @ rot_x(tilt_x) @ rot_y(tilt_y)

    # 1. 磨砂薄纱背景层（磨砂区明显朦胧化：白纱 + 提亮 + 降对比）
    frosted = base_img.convert('RGBA').copy()
    veil = Image.new('RGBA', (W, H), (255, 255, 255, 185))
    frosted = Image.alpha_composite(frosted, veil)

    # 2. 逐片生成三维投影多边形 → 累积掩膜
    blades_mask = Image.new('L', (W, H), 0)
    bm = ImageDraw.Draw(blades_mask)
    shadow_mask = Image.new('L', (W, H), 0)
    sm = ImageDraw.Draw(shadow_mask)

    for (a0, a1) in angles:
        pts3 = blade_polygon_3d(a0, a1, radius, samples=44)
        pts_rot = (R @ pts3.T).T
        pts2 = project(pts_rot, W, H, cx, cy, focal)
        bm.polygon(pts2, fill=255)
        if shadow:
            # 阴影：偏移 6px（右下）
            pts_sh = [(x + 7, y + 5) for (x, y) in pts2]
            sm.polygon(pts_sh, fill=110)

    # 3. 柔化边缘（PPT 柔化边缘 10 磅）
    if soften_px > 0:
        blades_soft = blades_mask.filter(ImageFilter.GaussianBlur(radius=soften_px))
    else:
        blades_soft = blades_mask

    # 4. 合成
    canvas = frosted.copy()
    if shadow:
        shadow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        shadow_layer.putalpha(shadow_mask.filter(ImageFilter.GaussianBlur(radius=5)))
        canvas.paste(shadow_layer, (0, 0), shadow_layer)
    # 扇叶透出清晰背景（提亮 + 提饱和，形成"扇内明亮清晰 vs 扇外朦胧"的强对比）
    fan_content = base_img.convert('RGBA').copy()
    # 提亮 8% + 提饱和 12%
    enh = Image.new('RGBA', (W, H), (255, 255, 255, 30))
    fan_content = Image.alpha_composite(fan_content, enh)
    canvas.paste(fan_content, (0, 0), blades_soft)

    # 5. 扇骨（沿投影后的扇叶边缘画骨线，增强立体）
    bone = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bone)
    for (a0, a1) in angles:
        for ang in (a0, a1):
            line3 = blade_polygon_3d(ang, ang + 0.01, radius, samples=2)[1:]
            line3r = (R @ line3.T).T
            line2 = project(line3r, W, H, cx, cy, focal)
            if len(line2) >= 2:
                bd.line([ (cx, cy), line2[-1] ], fill=(120, 105, 78, 130), width=2)
    canvas.paste(bone, (0, 0), bone)

    return canvas.convert('RGB')


def create_courtyard_bg_v3(W=1920, H=1080):
    """v3 背景：绿色系（对齐原版主色 #9FBD8A / #6C8F57 / #334A2B）"""
    img = Image.new('RGB', (W, H), (226, 230, 224))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        t = y / H
        r = int(232 * (1 - t) + 198 * t)
        g = int(238 * (1 - t) + 214 * t)
        b = int(230 * (1 - t) + 196 * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    def bamboo(dr, x, h_ratio, color, width, leaf_color, bend=12):
        base_y, top_y = H, H * h_ratio
        for i in range(26):
            t = i / 26
            xx = x + math.sin(t * 3 + x * 0.01) * bend
            yy = base_y - (base_y - top_y) * t
            w = width * (1 - 0.35 * t)
            dr.ellipse([xx - w, yy - 6, xx + w, yy + 6], fill=color)
        for k in range(5):
            ty = base_y - (base_y - top_y) * (0.25 + k * 0.16)
            tx = x + math.sin(ty * 0.01) * (bend + 2) + (-1 if k % 2 else 1) * (18 + k * 6)
            for leaf in range(3):
                ang = (k * 47 + leaf * 31) * math.pi / 180
                L = 22 + k * 4
                ex = tx + math.cos(ang) * L
                ey = ty + math.sin(ang) * L * 0.6 - 10
                dr.line([(tx, ty), (ex, ey)], fill=leaf_color, width=3)

    far = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    fd = ImageDraw.Draw(far)
    for i in range(11):
        bamboo(fd, int(W * (0.05 + i * 0.09)), 0.60, (159, 189, 138, 72), 7, (150, 182, 130, 82), 18)
    far = far.filter(ImageFilter.GaussianBlur(radius=9))
    img.paste(far, (0, 0), far)

    mid = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    md = ImageDraw.Draw(mid)
    for x in [130, 300, 460, 1520, 1700, 1850]:
        bamboo(md, x, 0.52, (108, 143, 87, 175), 9, (95, 130, 78, 190), 14)
    mid = mid.filter(ImageFilter.GaussianBlur(radius=2))
    img.paste(mid, (0, 0), mid)

    near = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    nd = ImageDraw.Draw(near)
    for x in [150, 480, 1580, 1800]:
        bamboo(nd, x, 0.46, (70, 100, 60, 255), 12, (51, 74, 43, 255), 10)
    img.paste(near, (0, 0), near)

    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W * 0.02, H * 0.02, W * 0.30, H * 0.34], fill=(255, 246, 214, 75))
    for lx in [420, 630, 850, 1070]:
        gd.ellipse([lx + 10, 95, lx + 150, 310], fill=(255, 190, 118, 68))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=68))
    img.paste(glow, (0, 0), glow)

    eave = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ed = ImageDraw.Draw(eave)
    ed.polygon([(0, 0), (0, 82), (515, 82), (755, 34), (975, 82), (1310, 82), (1310, 0)],
               fill=(66, 74, 68, 240))
    ed.polygon([(0, 82), (515, 82), (755, 34), (975, 82), (1310, 82), (1310, 122), (0, 122)],
               fill=(88, 94, 86, 255))
    for wx in range(58, 1250, 58):
        ed.line([(wx, 80), (wx + 38, 38)], fill=(50, 58, 52, 230), width=3)
    for lx in [420, 630, 850, 1070]:
        lxr = lx + 70
        ed.line([(lxr + 35, 76), (lxr + 35, 146)], fill=(88, 58, 42, 255), width=3)
        ed.ellipse([lxr, 146, lxr + 70, 246], fill=(198, 76, 58, 255))
        for k in range(1, 7):
            kx = lxr + 35 + (k - 3.5) * 8
            ed.ellipse([kx - 2, 148, kx + 2, 244], fill=(178, 60, 44, 120))
        ed.ellipse([lxr + 20, 153, lxr + 50, 239], fill=(255, 214, 150, 130))
        ed.rectangle([lxr - 2, 146, lxr + 72, 154], fill=(180, 140, 70, 255))
        ed.rectangle([lxr - 2, 238, lxr + 72, 246], fill=(180, 140, 70, 255))
        for k in range(5):
            sx = lxr + 14 + k * 11
            ed.line([(sx, 246), (sx + 6, 270)], fill=(190, 90, 66, 220), width=2)
    img.paste(eave, (0, 0), eave)

    rain = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    rd = ImageDraw.Draw(rain)
    rng = np.random.RandomState(7)
    for _ in range(300):
        x, y = rng.uniform(0, W), rng.uniform(0, H)
        ln, sl = rng.uniform(12, 44), rng.uniform(0.10, 0.40)
        rd.line([(x, y), (x + sl * ln, y + ln)],
                fill=(150, 175, 158, int(rng.uniform(22, 105))), width=1)
    img.paste(rain, (0, 0), rain)

    noise = np.random.RandomState(42).normal(0, 3.5, (H, W, 1))
    nimg = Image.fromarray(np.clip(noise + 128, 0, 255).astype(np.uint8).repeat(3, axis=2), 'RGB')
    img = Image.blend(img, nimg, 0.028)
    return img.filter(ImageFilter.GaussianBlur(radius=1.0))


if __name__ == '__main__':
    import os
    out = r'%USERPROFILE%\AppData\Local\Temp\fan_deep'
    os.makedirs(out, exist_ok=True)
    bg = create_courtyard_bg_v3(1920, 1080)
    bg.save(os.path.join(out, 'bg_v31.jpg'), quality=93)
    for tx, tz, nm in [(0, 0, 'flat'), (18, 0, 'x18'), (30, 0, 'x30'), (22, -12, 'x22z12')]:
        s = render_fan_3d_v2(bg, True, tilt_x=tx, tilt_z=tz)
        s.save(os.path.join(out, f'v31_{nm}.jpg'), quality=93)
    render_fan_3d_v2(bg, False, tilt_x=18).save(os.path.join(out, 'v31_closed.jpg'), quality=93)
    print("v3.1 rendered")

# -*- coding: utf-8 -*-
"""仿照《扇叶开场》视频的忠实还原渲染器 v2.0（评分 8.5 → 10 升级版）

对齐视频参数：
- 背景：古风庭院（淡青水墨渐变 + 三层竹影纵深感 + 雨丝 + 灯笼 + 垂帘 + 雾气 + 水洼倒影 + 孤舟飞鸟）
- 扇叶：6 片缺角圆形切片，中心对称放射，扇轴在底部中央（折扇撑开朝上）
- 扇叶效果：绢布纹理 + 径向光 + 扇骨细线 + 白色描边 + 柔光晕染 + 内部透出清晰背景
- 阴影：透明度 15%、大小 104%、模糊 5磅、距离 0、角度 0 + 左上光源方向性
- 文字：雨霖铃书法 + 柳永印章 + 右侧完整竖排诗句 + 词牌小注
"""
import math
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def draw_rain(draw, W, H, rng=np.random.RandomState(7), n=280):
    """斜向雨丝（长度/斜度/透明度随机，细而淡，避免杂乱颗粒感）"""
    for _ in range(n):
        x = rng.uniform(0, W)
        y = rng.uniform(0, H)
        ln = rng.uniform(12, 44)
        sl = rng.uniform(0.10, 0.40)
        a = rng.uniform(22, 110)
        x2 = x + sl * ln
        y2 = y + ln
        draw.line([(x, y), (x2, y2)], fill=(140, 168, 180, int(a)), width=1)


def draw_bamboo(draw, W, H, x, h_ratio, color, width, leaf_color, bend=12.0):
    """一根竹子：节杆 + 竹叶（bend 控制弯曲幅度）"""
    base_y = H
    top_y = H * h_ratio
    seg = 26
    for i in range(seg):
        t = i / seg
        xx = x + math.sin(t * 3 + x * 0.01) * bend
        yy = base_y - (base_y - top_y) * t
        w = width * (1 - 0.35 * t)
        draw.ellipse([xx - w, yy - 6, xx + w, yy + 6], fill=color)
    for i in range(1, seg - 1, 3):
        t = i / seg
        xx = x + math.sin(t * 3 + x * 0.01) * bend
        yy = base_y - (base_y - top_y) * t
        draw.line([(xx - width * 0.8, yy - 2), (xx + width * 0.8, yy - 2)], fill=leaf_color, width=2)
    for k in range(5):
        ty = base_y - (base_y - top_y) * (0.25 + k * 0.16)
        tx = x + math.sin(ty * 0.01) * (bend + 2) + (-1 if k % 2 else 1) * (18 + k * 6)
        for leaf in range(3):
            ang = (k * 47 + leaf * 31) * math.pi / 180
            L = 22 + k * 4
            ex = tx + math.cos(ang) * L
            ey = ty + math.sin(ang) * L * 0.6 - 10
            draw.line([(tx, ty), (ex, ey)], fill=leaf_color, width=3)
            ex2 = ex + math.cos(ang + 0.5) * 10
            ey2 = ey + math.sin(ang + 0.5) * 6
            draw.line([(ex, ey), (ex2, ey2)], fill=leaf_color, width=2)


def draw_boat(draw, W, H, x, y, scale=1.0, color=(58, 72, 62, 200)):
    """孤舟剪影（离别意象）：船身 + 帆影 + 人物斗笠"""
    bw = int(150 * scale)
    bh = int(42 * scale)
    draw.arc([x, y, x + bw, y + bh * 2], start=180, end=360, fill=color, width=int(5 * scale))
    draw.line([(x + bw * 0.18, y + bh), (x + bw * 0.82, y + bh)], fill=color, width=int(3 * scale))
    # 帆影（三角帆，微倾斜）
    draw.polygon([(x + bw * 0.55, y - bh * 1.1), (x + bw * 0.55, y + bh * 0.2),
                  (x + bw * 0.92, y + bh * 0.2)], fill=(64, 80, 68, 170))
    # 船篷
    draw.arc([x + bw * 0.28, y - bh * 0.9, x + bw * 0.62, y + bh * 0.6], start=180, end=360, fill=color, width=int(4 * scale))
    # 人物（斗笠 + 身）
    hx = x + bw * 0.74
    hy = y + bh * 0.55
    draw.line([(hx, hy - bh * 0.55), (hx, hy + bh * 0.1)], fill=color, width=int(3 * scale))
    draw.arc([hx - bh * 0.28, hy - bh * 0.85, hx + bh * 0.28, hy - bh * 0.35],
             start=180, end=360, fill=color, width=int(2 * scale))


def draw_birds(draw, W, H, rng, n=4):
    """飞鸟剪影（"念去去"天空留白处的点景）"""
    for _ in range(n):
        bx = rng.uniform(W * 0.55, W * 0.85)
        by = rng.uniform(H * 0.12, H * 0.30)
        s = rng.uniform(8, 15)
        a = rng.uniform(0.5, 1.0)
        draw.arc([bx - s, by - s * 0.4, bx, by + s * 0.4], start=200, end=340,
                 fill=(70, 90, 80, int(160 * a)), width=2)
        draw.arc([bx, by - s * 0.4, bx + s, by + s * 0.4], start=200, end=340,
                 fill=(70, 90, 80, int(160 * a)), width=2)


def create_courtyard_background(W=1920, H=1080):
    """古风庭院 v2.0：淡青水墨 + 三层竹影 + 雨丝 + 灯笼 + 垂帘 + 雾气 + 水洼 + 孤舟飞鸟"""
    img = Image.new('RGB', (W, H), (232, 240, 236))
    draw = ImageDraw.Draw(img)

    # 1. 淡青水墨竖向渐变（上浅下深青，更细腻三段式）
    for y in range(H):
        t = y / H
        if t < 0.45:
            tt = t / 0.45
            r = int(238 - 14 * tt); g = int(244 - 12 * tt); b = int(240 - 16 * tt)
        else:
            tt = (t - 0.45) / 0.55
            r = int(224 - 26 * tt); g = int(232 - 18 * tt); b = int(224 - 24 * tt)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # 2. 远景竹影（最远：低透明大模糊青色剪影，密布）
    far = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    fdraw = ImageDraw.Draw(far)
    for i in range(12):
        draw_bamboo(fdraw, W, H, x=int(W * (0.04 + i * 0.09)),
                    h_ratio=0.58, color=(125, 155, 142, 45), width=6,
                    leaf_color=(115, 148, 132, 55), bend=18)
    far = far.filter(ImageFilter.GaussianBlur(radius=10))
    img.paste(far, (0, 0), far)

    # 3. 中景竹影（中透明，略清晰）
    mid = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(mid)
    for i, x in enumerate([110, 260, 430, 1490, 1660, 1830]):
        draw_bamboo(mdraw, W, H, x=x, h_ratio=0.52,
                    color=(82, 120, 100, 150), width=8,
                    leaf_color=(66, 104, 84, 165), bend=14)
    mid = mid.filter(ImageFilter.GaussianBlur(radius=3))
    img.paste(mid, (0, 0), mid)

    # 4. 近景竹子（清晰、深绿，带一点侧光）
    near = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ndraw = ImageDraw.Draw(near)
    for x in [150, 500, 1560, 1780]:
        draw_bamboo(ndraw, W, H, x=x, h_ratio=0.46,
                    color=(52, 88, 70, 255), width=12,
                    leaf_color=(38, 74, 56, 255), bend=10)
        # 侧光高光条（杆左侧受光）
        for i in range(20):
            t = i / 20
            xx = x + math.sin(t * 3 + x * 0.01) * 10
            yy = H - (H - H * 0.46) * t
            ndraw.line([(xx - 4, yy), (xx - 1, yy)], fill=(130, 160, 140, 90), width=2)
    img.paste(near, (0, 0), near)

    # 5. 柔和光斑（左上光源）+ 灯笼光晕（暖色点缀，冷暖对比）
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([W * 0.02, H * 0.02, W * 0.30, H * 0.36], fill=(255, 246, 220, 70))
    gdraw.ellipse([W * 0.60, H * 0.05, W * 0.92, H * 0.48], fill=(255, 235, 195, 75))
    for lx in [430, 640, 860, 1080]:
        gdraw.ellipse([lx + 10, 100, lx + 150, 320], fill=(255, 185, 110, 65))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=70))
    img.paste(glow, (0, 0), glow)

    # 6. 屋檐 + 精致灯笼（灯罩纹理 + 穗子）
    eave = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    edraw = ImageDraw.Draw(eave)
    edraw.polygon([(0, 0), (0, 85), (520, 85), (760, 36), (980, 85), (1320, 85), (1320, 0)],
                  fill=(68, 76, 70, 240))
    edraw.polygon([(0, 85), (520, 85), (760, 36), (980, 85), (1320, 85), (1320, 125), (0, 125)],
                  fill=(92, 98, 90, 255))
    for wx in range(60, 1260, 60):
        edraw.line([(wx, 82), (wx + 40, 40)], fill=(52, 60, 54, 230), width=3)
    # 灯笼：灯身 + 竖纹 + 上下金箍 + 穗子 + 光晕
    for lx in [430, 640, 860, 1080]:
        lxr = lx + 70
        # 挂线
        edraw.line([(lxr + 35, 78), (lxr + 35, 148)], fill=(90, 60, 44, 255), width=3)
        # 灯身
        edraw.ellipse([lxr, 148, lxr + 70, 248], fill=(198, 76, 58, 255))
        # 灯罩竖纹（模拟骨架）
        for k in range(1, 7):
            kx = lxr + 35 + (k - 3.5) * 8
            edraw.ellipse([kx - 2, 150, kx + 2, 246], fill=(178, 60, 44, 120))
        # 内部暖光
        edraw.ellipse([lxr + 20, 155, lxr + 50, 241], fill=(255, 214, 150, 130))
        # 金箍上下
        edraw.rectangle([lxr - 2, 148, lxr + 72, 156], fill=(180, 140, 70, 255))
        edraw.rectangle([lxr - 2, 240, lxr + 72, 248], fill=(180, 140, 70, 255))
        # 穗子
        for k in range(5):
            sx = lxr + 14 + k * 11
            edraw.line([(sx, 248), (sx + 6, 272)], fill=(190, 90, 66, 220), width=2)
        # 灯笼底部吊坠
        edraw.ellipse([lxr + 31, 270, lxr + 39, 278], fill=(150, 60, 44, 255))
    img.paste(eave, (0, 0), eave)

    # 7. 左侧垂帘（竹帘精致版：竹节 + 绑带）
    blind = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(blind)
    for i in range(12):
        y = 178 + i * 15
        bdraw.line([(0, y), (248, y + 9)], fill=(146, 126, 94, 135), width=5)
    for i in range(14):
        x = i * 19
        bdraw.line([(x, 178), (x + 5, 340)], fill=(168, 148, 112, 100), width=3)
        # 竹节小点
        bdraw.ellipse([x - 2, 240, x + 4, 246], fill=(130, 112, 84, 120))
    # 绑带
    bdraw.line([(0, 300), (250, 300)], fill=(120, 90, 66, 160), width=6)
    bdraw.line([(0, 250), (250, 250)], fill=(120, 90, 66, 160), width=6)
    img.paste(blind, (0, 0), blind)

    # 8. 雨丝
    rain_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(rain_layer)
    draw_rain(rdraw, W, H)
    img.paste(rain_layer, (0, 0), rain_layer)

    # 9. 地面 + 水洼涟漪（扇轴下方，环线减弱避免误读为路径符号）
    ground = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gnd = ImageDraw.Draw(ground)
    # 地面深色渐变（底部）
    for i in range(140):
        yy = H - 140 + i
        a = int(38 * (i / 140))
        gnd.line([(0, yy), (W, yy)], fill=(96, 128, 110, a))
    # 水洼（椭圆形反光）
    gnd.ellipse([W * 0.30, H * 0.78, W * 0.70, H * 1.0], fill=(185, 215, 200, 60))
    # 涟漪椭圆环（弱化）
    for k in range(2):
        rx = int(W * 0.20 - k * 18)
        ry = int(H * 0.11 - k * 7)
        gnd.ellipse([W * 0.50 - rx, H * 0.88 - ry, W * 0.50 + rx, H * 0.88 + ry],
                    outline=(225, 240, 230, 55 - k * 15), width=2)
    ground = ground.filter(ImageFilter.GaussianBlur(radius=3))
    img.paste(ground, (0, 0), ground)

    # 10. 飞鸟（天空留白处点景，孤舟移到渲染层扇面外右侧）
    decor = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ddraw = ImageDraw.Draw(decor)
    draw_birds(ddraw, W, H, np.random.RandomState(9))
    img.paste(decor, (0, 0), decor)

    # 11. 宣纸噪点（细腻颗粒，绢本质感）
    noise = np.random.RandomState(42).normal(0, 4, (H, W, 1))
    noise_img = Image.fromarray(np.clip(noise + 128, 0, 255).astype(np.uint8).repeat(3, axis=2), 'RGB')
    img = Image.blend(img, noise_img, 0.03)

    # 12. 底部雾气（薄纱层叠，增强空间深度）+ 顶部轻烟
    mist = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    mdraw = ImageDraw.Draw(mist)
    for i in range(5):
        my = H * (0.55 + i * 0.09)
        mw = W * (1.3 - i * 0.12)
        mdraw.ellipse([W * 0.35 - mw / 2, my, W * 0.35 + mw / 2, my + 90],
                      fill=(245, 250, 246, 22))
    # 顶部轻烟（横向飘带，模拟炊烟/云雾）
    for i in range(3):
        sy = H * (0.06 + i * 0.05)
        sw = W * (0.9 + i * 0.15)
        mdraw.ellipse([W * 0.2 - sw / 2, sy, W * 0.2 + sw / 2, sy + 26],
                      fill=(250, 252, 248, 16 + i * 4))
    mist = mist.filter(ImageFilter.GaussianBlur(radius=30))
    img.paste(mist, (0, 0), mist)

    # 13. 整体轻微柔光
    img = img.filter(ImageFilter.GaussianBlur(radius=1.0))
    return img


def _paper_texture(W, H, seed=5, alpha=36):
    """绢布纤维纹理（细横线+噪点）"""
    tex = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    rng = np.random.RandomState(seed)
    tdraw = ImageDraw.Draw(tex)
    for _ in range(600):
        x = rng.uniform(0, W); y = rng.uniform(0, H)
        ln = rng.uniform(6, 22)
        tdraw.line([(x, y), (x + ln, y + rng.uniform(-2, 2))],
                   fill=(255, 250, 240, int(rng.uniform(10, alpha))), width=1)
    return tex


def render_fan_replica(base_img, is_opened=True):
    """渲染居中式半圆折扇双态 v2.0（绢布质感 + 扇骨 + 径向光 + 方向性阴影 + 完整诗句）"""
    W, H = base_img.size

    # 磨砂雾白外层（稍降透明度，保留背景细节）
    frosted = base_img.copy().convert('RGBA')
    veil = Image.new('RGBA', (W, H), (255, 255, 255, 150))
    frosted = Image.alpha_composite(frosted, veil)

    # 扇轴（底部中央，折扇撑开朝上呈半圆）
    cx, cy = W // 2, int(H * 0.80)
    radius = int(H * 0.62)
    n_blades = 6
    blade_span = 27.0
    gap = 1.5
    total = n_blades * (blade_span + gap) - gap
    start_angle = 180 + (180 - total) / 2
    end_angle = start_angle + total

    if is_opened:
        angles = [start_angle + i * (blade_span + gap) for i in range(n_blades)]
    else:
        angles = [start_angle + (blade_span + gap) * (n_blades - 1) for _ in range(n_blades)]

    # 扇叶掩膜
    blades_mask = Image.new('L', (W, H), 0)
    bdraw = ImageDraw.Draw(blades_mask)
    for a in angles:
        bdraw.pieslice([cx - radius, cy - radius, cx + radius, cy + radius],
                       start=a, end=a + blade_span, fill=255)

    # 方向性阴影（左上光源 → 阴影向右下偏移 6px）
    sh_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sh_layer)
    r_sh = int(radius * 1.02)
    for a in angles:
        sdraw.pieslice([cx - r_sh + 10, cy - r_sh + 8, cx + r_sh + 10, cy + r_sh + 8],
                       start=a, end=a + blade_span, fill=(0, 0, 0, 42))
    sh_layer = sh_layer.filter(ImageFilter.GaussianBlur(radius=5))

    canvas = frosted.copy()
    canvas.paste(sh_layer, (0, 0), sh_layer)

    # 扇面：透出背景 + 绢布纹理 + 径向光（中心亮边缘暗）+ 扇面水墨山水
    fan_layer = base_img.convert('RGBA').copy()
    tex = _paper_texture(W, H)
    fan_layer.paste(tex, (0, 0), tex)

    # 扇面内淡墨远山 + 淡月（扇面诗画，呼应"楚天阔"）
    ink_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    idraw0 = ImageDraw.Draw(ink_layer)
    def ink_mountain(cx0, base_y0, amp, color, blur):
        pts = []
        for x in range(int(W * 0.28), int(W * 0.72), 16):
            nx = x * 0.02
            y = base_y0 - abs(math.sin(nx * 2.3)) * amp - math.sin(nx * 5) * amp * 0.3
            pts.append((x, int(y)))
        layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ldraw = ImageDraw.Draw(layer)
        ldraw.polygon(pts + [(pts[-1][0], H), (pts[0][0], H)], fill=color)
        layer = layer.filter(ImageFilter.GaussianBlur(radius=blur))
        ink_layer.paste(layer, (0, 0), layer)
    ink_mountain(0, int(H * 0.55), 130, (70, 98, 84, 55), 6)
    ink_mountain(0, int(H * 0.62), 100, (52, 78, 66, 75), 3)
    # 淡月（扇面右上）
    idraw0.ellipse([int(W * 0.60), int(H * 0.30), int(W * 0.66), int(H * 0.36)],
                   fill=(244, 238, 222, 120))
    # 水墨只保留在扇面内
    fan_layer.paste(ink_layer, (0, 0), Image.composite(ink_layer.split()[3], Image.new('L', (W, H), 0), blades_mask))

    # 径向光遮罩：距扇轴越远越暗（模拟绢布受光衰减）
    yy, xx = np.mgrid[0:H, 0:W]
    dist = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / radius
    shade = np.clip(1.0 - dist * 0.55, 0.25, 1.0)
    shade_rgba = Image.fromarray((shade * 255).astype(np.uint8), 'L')
    fan_layer = Image.composite(
        Image.eval(fan_layer, lambda v: v),
        Image.blend(fan_layer, Image.new('RGBA', (W, H), (40, 55, 45, 255)), 0.35),
        shade_rgba
    )
    canvas.paste(fan_layer, (0, 0), blades_mask)

    # 扇骨细线（每片扇叶两侧深色骨线 + 圆柱光感：左亮右暗，强化）
    bone = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    bdraw2 = ImageDraw.Draw(bone)
    for a in angles:
        mid = a + blade_span / 2
        for t in np.linspace(0.25, 0.97, 40):
            r_t = radius * t
            bx = cx + r_t * math.cos(math.radians(mid))
            by = cy - r_t * math.sin(math.radians(mid))
            # 右侧暗线
            bdraw2.ellipse([bx - 1.5, by - 1.5, bx + 1.5, by + 1.5], fill=(70, 54, 38, 170))
            # 左侧高光线（受左上光源）
            bdraw2.ellipse([bx - 2.8, by - 2.8, bx - 0.4, by - 0.4], fill=(212, 194, 164, 140))
    canvas.paste(bone, (0, 0), bone)

    # 扇面湿痕（雨打绢布的水渍，增强可见度）+ 淡墨圆斑
    wet = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    wdraw = ImageDraw.Draw(wet)
    wrng = np.random.RandomState(21)
    for _ in range(18):
        rr = wrng.uniform(0.3, 0.9) * radius
        aa = wrng.uniform(start_angle + 4, end_angle - 4)
        dx = cx + rr * math.cos(math.radians(aa))
        dy = cy - rr * math.sin(math.radians(aa))
        rad = wrng.uniform(8, 20)
        wdraw.ellipse([dx - rad, dy - rad * 0.7, dx + rad, dy + rad * 0.7],
                      outline=(235, 242, 240, 110), width=3)
        wdraw.ellipse([dx - rad * 0.5, dy - rad * 0.35, dx + rad * 0.5, dy + rad * 0.35],
                      fill=(235, 242, 240, 26))
    # 淡墨圆斑（雨墨混染）
    for _ in range(7):
        rr = wrng.uniform(0.45, 0.92) * radius
        aa = wrng.uniform(start_angle + 6, end_angle - 6)
        dx = cx + rr * math.cos(math.radians(aa))
        dy = cy - rr * math.sin(math.radians(aa))
        rad = wrng.uniform(14, 34)
        wdraw.ellipse([dx - rad, dy - rad * 0.6, dx + rad, dy + rad * 0.6],
                      fill=(52, 76, 62, 26))
    # 扇缘淡墨晕（增强）
    ink = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    idraw = ImageDraw.Draw(ink)
    for a in angles:
        idraw.pieslice([cx - radius - 8, cy - radius - 8, cx + radius + 8, cy + radius + 8],
                       start=a + 2, end=a + blade_span - 2, outline=(46, 66, 54, 55), width=12)
    ink = ink.filter(ImageFilter.GaussianBlur(radius=7))
    canvas.paste(ink, (0, 0), Image.composite(ink.split()[3], Image.new('L', (W, H), 0), blades_mask))
    canvas.paste(wet, (0, 0), Image.composite(wet.split()[3], Image.new('L', (W, H), 0), blades_mask))

    # 扇叶边缘：白色细描边 + 外柔光晕染 + 仿古金线 + 回纹装饰
    rim = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(rim)
    for a in angles:
        rdraw.pieslice([cx - radius, cy - radius, cx + radius, cy + radius],
                       start=a, end=a + blade_span, outline=(255, 255, 255, 225), width=2)
    rim_glow = rim.filter(ImageFilter.GaussianBlur(radius=3))
    canvas.paste(rim_glow, (0, 0), rim_glow)
    canvas.paste(rim, (0, 0), rim)

    # 仿古金线 + 大号回纹装饰（金色包边带 + 大菱形独立纹样，卷轴工艺感）
    goldline = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(goldline)
    for a in angles:
        # 金带（6px 半透明金边）
        gdraw.pieslice([cx - radius - 12, cy - radius - 12, cx + radius + 12, cy + radius + 12],
                       start=a, end=a + blade_span, outline=(180, 142, 82, 175), width=6)
        gdraw.pieslice([cx - radius - 12, cy - radius - 12, cx + radius + 12, cy + radius + 12],
                       start=a, end=a + blade_span, outline=(232, 204, 156, 195), width=2)
        # 大菱形独立纹样（每 26° 一个，s=16，双层嵌套，间隔清晰可辨）
        step = 26.0
        aa = a + 9
        while aa < a + blade_span - 9:
            rr = radius + 14
            bx = cx + rr * math.cos(math.radians(aa))
            by = cy - rr * math.sin(math.radians(aa))
            s = 16
            # 外菱金 + 内菱米白
            gdraw.polygon([(bx, by - s), (bx + s * 0.82, by), (bx, by + s), (bx - s * 0.82, by)],
                          fill=(196, 160, 102, 230))
            gdraw.polygon([(bx, by - s * 0.55), (bx + s * 0.45, by), (bx, by + s * 0.55), (bx - s * 0.45, by)],
                          fill=(240, 220, 180, 245))
            gdraw.polygon([(bx, by - s * 0.2), (bx + s * 0.16, by), (bx, by + s * 0.2), (bx - s * 0.16, by)],
                          fill=(254, 246, 226, 255))
            aa += step
    canvas.paste(goldline, (0, 0), goldline)

    # 扇缘外右侧：孤舟剪影（帆影 + 人物斗笠，画在扇面外干净背景上，清晰可见）
    boat_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    bdraw3 = ImageDraw.Draw(boat_layer)
    draw_boat(bdraw3, W, H, x=int(W * 0.845), y=int(H * 0.66), scale=1.25, color=(52, 68, 58, 215))
    canvas.paste(boat_layer, (0, 0), boat_layer)

    # 扇柄（扇轴下方细长竹柄：木纹 + 包浆高光）
    handle = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    hdraw = ImageDraw.Draw(handle)
    hdraw.rounded_rectangle([cx - 7, cy - 8, cx + 7, cy + int(H * 0.14)], radius=6,
                            fill=(104, 80, 54, 235))
    hdraw.rounded_rectangle([cx - 5, cy - 5, cx + 5, cy + int(H * 0.135)], radius=4,
                            fill=(138, 108, 76, 255))
    # 木纹细线
    for i in range(1, 12):
        yy = cy + i * int(H * 0.012)
        hdraw.arc([cx - 9, yy - 6, cx + 9, yy + 6], start=0, end=180,
                  fill=(96, 70, 46, 90), width=1)
    # 包浆高光（左侧受光）
    hdraw.line([(cx - 3, cy - 4), (cx - 3, cy + int(H * 0.13))], fill=(196, 168, 130, 110), width=2)
    # 扇轴钉 + 金属箍
    hdraw.rectangle([cx - 8, cy + int(H * 0.055), cx + 8, cy + int(H * 0.065)], fill=(170, 140, 96, 255))
    hdraw.ellipse([cx - 10, cy - 12, cx + 10, cy + 8], fill=(168, 138, 100, 255),
                  outline=(110, 84, 58, 255), width=2)
    hdraw.ellipse([cx - 3, cy - 5, cx + 3, cy + 1], fill=(210, 190, 150, 220))
    canvas.paste(handle, (0, 0), handle)

    # 雨滴落在扇面上的小点（扇面范围内，提亮增加可见度）
    rain_dots = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    rng = np.random.RandomState(11)
    rdraw2 = ImageDraw.Draw(rain_dots)
    for _ in range(65):
        rr = rng.uniform(0.15, 0.95) * radius
        aa = rng.uniform(start_angle + 3, end_angle - 3)
        dx = cx + rr * math.cos(math.radians(aa))
        dy = cy - rr * math.sin(math.radians(aa))
        a = rng.uniform(70, 160)
        rdraw2.ellipse([dx - 1.6, dy - 1.6, dx + 1.6, dy + 1.6], fill=(222, 236, 238, int(a)))
    canvas.paste(rain_dots, (0, 0), Image.composite(rain_dots.split()[3], Image.new('L', (W, H), 0), blades_mask))

    # 文字与印章
    t_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(t_layer)
    try:
        f_title = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF', 108)
        f_seal = ImageFont.truetype('C:/Windows/Fonts/STLITI.TTF', 24) if os.path.exists('C:/Windows/Fonts/STLITI.TTF') else ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF', 24)
        f_poem = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 40)
        f_note = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 22)
    except Exception:
        f_title = f_seal = f_poem = f_note = ImageFont.load_default()

    if is_opened:
        # 主标题（扇面上方）
        tdraw.text((int(W * 0.53), int(H * 0.075)), '雨 霖 铃', fill=(40, 35, 30, 255), font=f_title)
        # 词牌小注
        tdraw.text((int(W * 0.795), int(H * 0.105)), '柳永 · 宋词名篇', fill=(96, 88, 74, 200), font=f_note)
        # 红色印章【柳永】（篆意隶书 + 仿古双线边框 + 四角回纹）
        sx, sy = int(W * 0.655), int(H * 0.185)
        tdraw.rectangle([sx, sy, sx + 54, sy + 94], fill=(196, 58, 54, 245), outline=(140, 34, 30), width=3)
        tdraw.rectangle([sx + 4, sy + 4, sx + 50, sy + 90], outline=(255, 228, 220, 120), width=1)
        # 四角回纹小点
        for (cx0, cy0) in [(sx + 2, sy + 2), (sx + 52, sy + 2), (sx + 2, sy + 92), (sx + 52, sy + 92)]:
            tdraw.line([(cx0 - 3, cy0), (cx0 + 3, cy0)], fill=(255, 232, 224, 160), width=2)
            tdraw.line([(cx0, cy0 - 3), (cx0, cy0 + 3)], fill=(255, 232, 224, 160), width=2)
        tdraw.text((sx + 13, sy + 10), '柳', fill=(252, 248, 244, 255), font=f_seal)
        tdraw.text((sx + 13, sy + 50), '永', fill=(252, 248, 244, 255), font=f_seal)
        # 右侧完整竖排诗句（放大 + 米白描边提高辨识度）
        poem_lines = [
            '念去去，千里烟波，',
            '暮霭沉沉楚天阔。',
            '便纵有千种风情，',
            '更与何人说。',
        ]
        px = int(W * 0.862)
        py = int(H * 0.085)
        for line in poem_lines:
            for ch in line:
                tdraw.text((px, py), ch, font=f_poem, fill=(42, 78, 58, 255),
                           stroke_width=3, stroke_fill=(250, 246, 238, 235))
                py += 50
            py += 34  # 句间空行
    else:
        pass

    canvas.paste(t_layer, (0, 0), t_layer)
    return canvas.convert('RGB')


if __name__ == '__main__':
    import os
    out_dir = r'%USERPROFILE%\AppData\Local\Temp\fan_study'
    os.makedirs(out_dir, exist_ok=True)
    bg = create_courtyard_background(1920, 1080)
    bg.save(os.path.join(out_dir, 'bg_courtyard_v2.jpg'), quality=93)
    s1 = render_fan_replica(bg, is_opened=False)
    s1.save(os.path.join(out_dir, 'replica_s1_v2.jpg'), quality=93)
    s2 = render_fan_replica(bg, is_opened=True)
    s2.save(os.path.join(out_dir, 'replica_s2_v2.jpg'), quality=93)
    print("saved v2: bg / replica_s1 / replica_s2")

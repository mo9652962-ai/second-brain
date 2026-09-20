# -*- coding: utf-8 -*-
"""仿照《扇叶开场》视频的忠实还原渲染器（背景 + 居中半圆折扇 + 文字）

对齐视频参数：
- 背景：古风庭院（淡青水墨渐变 + 竹影 + 雨丝 + 灯笼 + 垂帘 + 光斑）
- 扇叶：6 片缺角圆形切片，中心对称放射，扇轴在底部中央（折扇撑开朝上）
- 扇叶效果：内部透出清晰背景（透光窗口），外部磨砂雾白
- 阴影：透明度 15%、大小 104%、模糊 5磅、距离 0、角度 0（柔和悬浮感）
- 全屏白色柔光矩形（柔化背景、避免过曝）
- 文字：雨霖铃横排书法 + 红色印章 + 右侧竖排诗句（绿色）
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def draw_rain(draw, W, H, rng=np.random.RandomState(7), n=320):
    """斜向雨丝（长度/斜度/透明度随机，模拟自然降雨）"""
    for _ in range(n):
        x = rng.uniform(0, W)
        y = rng.uniform(0, H)
        ln = rng.uniform(10, 42)
        sl = rng.uniform(0.10, 0.40)
        a = rng.uniform(28, 130)
        x2 = x + sl * ln
        y2 = y + ln
        draw.line([(x, y), (x2, y2)], fill=(140, 168, 180, int(a)), width=1)


def draw_bamboo(draw, W, H, x, h_ratio, color, width, leaf_color):
    """一根竹子：节杆 + 竹叶"""
    base_y = H
    top_y = H * h_ratio
    # 杆（略弯）
    seg = 24
    for i in range(seg):
        t = i / seg
        xx = x + math.sin(t * 3 + x * 0.01) * 12
        yy = base_y - (base_y - top_y) * t
        w = width * (1 - 0.35 * t)
        draw.ellipse([xx - w, yy - 6, xx + w, yy + 6], fill=color)
    # 竹节横纹
    for i in range(1, seg - 1, 3):
        t = i / seg
        xx = x + math.sin(t * 3 + x * 0.01) * 12
        yy = base_y - (base_y - top_y) * t
        draw.line([(xx - width * 0.8, yy - 2), (xx + width * 0.8, yy - 2)], fill=leaf_color, width=2)
    # 竹叶簇
    for k in range(5):
        ty = base_y - (base_y - top_y) * (0.25 + k * 0.16)
        tx = x + math.sin(ty * 0.01) * 14 + (-1 if k % 2 else 1) * (18 + k * 6)
        for leaf in range(3):
            ang = (k * 47 + leaf * 31) * math.pi / 180
            L = 22 + k * 4
            ex = tx + math.cos(ang) * L
            ey = ty + math.sin(ang) * L * 0.6 - 10
            draw.line([(tx, ty), (ex, ey)], fill=leaf_color, width=3)
            # 叶尖
            ex2 = ex + math.cos(ang + 0.5) * 10
            ey2 = ey + math.sin(ang + 0.5) * 6
            draw.line([(ex, ey), (ex2, ey2)], fill=leaf_color, width=2)


def create_courtyard_background(W=1920, H=1080):
    """古风庭院：淡青水墨 + 竹影 + 雨丝 + 灯笼 + 垂帘 + 光斑"""
    img = Image.new('RGB', (W, H), (232, 240, 236))
    draw = ImageDraw.Draw(img)

    # 1. 淡青水墨竖向渐变（上浅下深青）
    for y in range(H):
        t = y / H
        r = int(236 * (1 - t) + 208 * t)
        g = int(242 * (1 - t) + 224 * t)
        b = int(238 * (1 - t) + 214 * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # 2. 远处竹影（低透明度青色剪影）
    far = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    fdraw = ImageDraw.Draw(far)
    for i in range(9):
        draw_bamboo(fdraw, W, H, x=int(W * (0.08 + i * 0.115)),
                    h_ratio=0.62, color=(120, 150, 138, 55), width=7,
                    leaf_color=(110, 145, 130, 70))
    far = far.filter(ImageFilter.GaussianBlur(radius=6))
    img.paste(far, (0, 0), far)

    # 3. 中景竹子（清晰、深绿）
    for i, x in enumerate([140, 330, 480, 1500, 1680, 1810]):
        draw_bamboo(draw, W, H, x=x, h_ratio=0.5,
                    color=(58, 96, 78, 255), width=10,
                    leaf_color=(42, 82, 62, 255))

    # 4. 柔和光斑（右上暖光）+ 灯笼光晕
    glow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([W * 0.62, H * 0.06, W * 0.95, H * 0.5], fill=(255, 240, 205, 95))
    for lx in [430, 640, 860, 1080]:
        gdraw.ellipse([lx + 25, 120, lx + 115, 300], fill=(255, 190, 120, 55))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=60))
    img.paste(glow, (0, 0), glow)

    # 5. 屋檐 + 灯笼（顶部两侧）
    # 左侧屋檐
    eave = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    edraw = ImageDraw.Draw(eave)
    edraw.polygon([(0, 0), (0, 90), (520, 90), (760, 40), (980, 90), (1320, 90), (1320, 0)],
                  fill=(70, 78, 72, 235))
    edraw.polygon([(0, 90), (520, 90), (760, 40), (980, 90), (1320, 90), (1320, 130), (0, 130)],
                  fill=(90, 96, 88, 255))
    # 瓦片暗线
    for wx in range(60, 1260, 60):
        edraw.line([(wx, 88), (wx + 40, 44)], fill=(55, 62, 56, 220), width=3)
    # 灯笼
    for lx in [430, 640, 860, 1080]:
        lxr = lx + 70
        edraw.ellipse([lxr, 150, lxr + 70, 250], fill=(196, 74, 58, 250))
        edraw.ellipse([lxr + 22, 155, lxr + 48, 245], fill=(255, 210, 150, 90))
        edraw.line([(lxr + 35, 132), (lxr + 35, 152)], fill=(120, 60, 44, 255), width=4)
        edraw.line([(lxr + 35, 250), (lxr + 35, 268)], fill=(160, 80, 58, 255), width=4)
        edraw.line([(lxr + 12, 250), (lxr + 58, 250)], fill=(160, 80, 58, 255), width=2)
    img.paste(eave, (0, 0), eave)

    # 6. 左侧垂帘（竹帘：横线 + 竖线）
    blind = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(blind)
    for i in range(11):
        y = 180 + i * 16
        bdraw.line([(0, y), (240, y + 10)], fill=(148, 128, 96, 120), width=5)
    for i in range(13):
        x = i * 20
        bdraw.line([(x, 180), (x + 6, 340)], fill=(168, 148, 112, 90), width=3)
    img.paste(blind, (0, 0), blind)

    # 7. 雨丝
    rain_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(rain_layer)
    draw_rain(rdraw, W, H)
    img.paste(rain_layer, (0, 0), rain_layer)

    # 8. 扇轴底部地面光晕（暖色倒映）+ 宣纸噪点
    ground = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    gnd = ImageDraw.Draw(ground)
    gnd.ellipse([W * 0.30, H * 0.72, W * 0.70, H * 1.02], fill=(255, 226, 170, 70))
    ground = ground.filter(ImageFilter.GaussianBlur(radius=50))
    img.paste(ground, (0, 0), ground)

    # 9. 宣纸噪点（细腻颗粒，营造绢本质感）
    noise = np.random.RandomState(42).normal(0, 4, (H, W, 1))
    noise_img = Image.fromarray(np.clip(noise + 128, 0, 255).astype(np.uint8).repeat(3, axis=2), 'RGB')
    img = Image.blend(img, noise_img, 0.045)

    # 10. 整体轻微柔光
    img = img.filter(ImageFilter.GaussianBlur(radius=1.2))
    return img


def render_fan_replica(base_img, is_opened=True):
    """渲染居中式半圆折扇双态（对齐视频：6片、中心对称、扇轴底部中央）"""
    W, H = base_img.size

    # 磨砂雾白外层
    frosted = base_img.copy().convert('RGBA')
    veil = Image.new('RGBA', (W, H), (255, 255, 255, 175))
    frosted = Image.alpha_composite(frosted, veil)

    # 扇轴（底部中央，折扇撑开朝上呈半圆）
    cx, cy = W // 2, int(H * 0.80)
    radius = int(H * 0.62)
    n_blades = 6
    blade_span = 27.0   # 每片角度
    gap = 1.5           # 片间缝隙
    total = n_blades * (blade_span + gap) - gap  # 约 170°
    # 上半圆：PIL pieslice 顺时针，start 在 9 点钟方向，end 在 3 点钟方向
    start_angle = 180 + (180 - total) / 2
    end_angle = start_angle + total

    if is_opened:
        angles = [start_angle + i * (blade_span + gap) for i in range(n_blades)]
    else:
        # 合拢态：全部挤向右侧起始位置（扇叶叠加成一条）
        angles = [start_angle + (blade_span + gap) * (n_blades - 1) for _ in range(n_blades)]

    # 扇叶掩膜（透出清晰背景）
    blades_mask = Image.new('L', (W, H), 0)
    bdraw = ImageDraw.Draw(blades_mask)
    for a in angles:
        bdraw.pieslice([cx - radius, cy - radius, cx + radius, cy + radius],
                       start=a, end=a + blade_span, fill=255)

    # 柔和阴影（透明度15%、大小104%、模糊小、距离0）
    sh_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sh_layer)
    r_sh = int(radius * 1.02)
    for a in angles:
        sdraw.pieslice([cx - r_sh + 4, cy - r_sh + 4, cx + r_sh + 4, cy + r_sh + 4],
                       start=a, end=a + blade_span, fill=(0, 0, 0, 40))
    sh_layer = sh_layer.filter(ImageFilter.GaussianBlur(radius=5))
    # 阴影只保留在扇叶之外可见——先铺阴影再贴扇叶
    canvas = frosted.copy()
    canvas.paste(sh_layer, (0, 0), sh_layer)
    canvas.paste(base_img, (0, 0), blades_mask)

    # 扇叶细描边（白色 1.5px，模拟绢布边缘）
    rim = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    rdraw = ImageDraw.Draw(rim)
    for a in angles:
        rdraw.pieslice([cx - radius, cy - radius, cx + radius, cy + radius],
                       start=a, end=a + blade_span, outline=(255, 255, 255, 215), width=2)
    canvas.paste(rim, (0, 0), rim)

    # 文字与印章
    t_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(t_layer)
    try:
        f_title = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF', 108)
        f_seal = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF', 22)
        f_poem = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 30)
    except Exception:
        f_title = f_seal = f_poem = ImageFont.load_default()

    if is_opened:
        # 主标题（扇面右上上方）
        tdraw.text((int(W * 0.55), int(H * 0.10)), '雨 霖 铃', fill=(45, 40, 35, 255), font=f_title)
        # 红色印章【柳永】
        sx, sy = int(W * 0.66), int(H * 0.20)
        tdraw.rectangle([sx, sy, sx + 46, sy + 80], fill=(199, 62, 58, 240), outline=(160, 40, 36), width=2)
        tdraw.text((sx + 12, sy + 10), '柳', fill=(255, 255, 255, 255), font=f_seal)
        tdraw.text((sx + 12, sy + 44), '永', fill=(255, 255, 255, 255), font=f_seal)
        # 右侧竖排诗句（绿色宋体，逐字竖排）
        poem = '念去去千里烟波'
        for i, ch in enumerate(poem):
            tdraw.text((int(W * 0.86), int(H * 0.16) + i * 44), ch,
                       fill=(52, 92, 72, 235), font=f_poem)
    else:
        pass  # 合拢态保持清爽

    canvas.paste(t_layer, (0, 0), t_layer)
    return canvas.convert('RGB')


if __name__ == '__main__':
    import os
    out_dir = r'%USERPROFILE%\AppData\Local\Temp\fan_study'
    os.makedirs(out_dir, exist_ok=True)
    bg = create_courtyard_background(1920, 1080)
    bg.save(os.path.join(out_dir, 'bg_courtyard.jpg'), quality=93)
    s1 = render_fan_replica(bg, is_opened=False)
    s1.save(os.path.join(out_dir, 'replica_s1.jpg'), quality=93)
    s2 = render_fan_replica(bg, is_opened=True)
    s2.save(os.path.join(out_dir, 'replica_s2.jpg'), quality=93)
    print("saved bg / replica_s1 / replica_s2")

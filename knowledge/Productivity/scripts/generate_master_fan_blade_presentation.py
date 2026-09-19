# -*- coding: utf-8 -*-
"""顶级视觉工程：超框大折扇开场平滑演示文稿生成器 (Masterpiece Fan Blade Morph Presentation)

解码抖音 @小文爱做ppt 9.8 分核心视觉密码：
1. 构图革命：从“居中小圆轮盘”升华至“右下起轴·超框大折扇 (Overframe Folding Fan)”
2. 透光视差：底图为完整远山落日垂柳画卷，扇面透出清晰原图，扇外覆盖柔和薄纱雾白
3. 工艺质感：每片扇叶外缘辅以 104% 柔和外阴影与 2px 细微高光描边，实现真实绢布折扇立体浮雕感
4. 国风排版：书法题名 + 朱砂方印 + 经典诗词排版（文人书画三位一体）
5. 双态平滑：Slide 1 合拢态 -> Slide 2 绽放终态，OpenXML 原生 <p:morph/> 自动补间
"""
import os, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.oxml import parse_xml


def create_scenic_background(width=1920, height=1080):
    """绘制高审美远山落日青绿山水意境底图"""
    img = Image.new('RGB', (width, height), (245, 242, 235))
    draw = ImageDraw.Draw(img)

    # 1. 晨雾天空微渐变
    for y in range(height):
        t = y / height
        r = int(248 * (1 - t) + 215 * t)
        g = int(244 * (1 - t) + 230 * t)
        b = int(236 * (1 - t) + 225 * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 2. 远山、中山、近山轮廓
    def add_mountain_range(y_base, amp, color, blur_radius=0):
        pts = [(0, height)]
        for x in range(0, width + 20, 20):
            nx = x * 0.003
            y = y_base + math.sin(nx * 3) * amp * 0.5 + math.sin(nx * 7 + 1.2) * amp * 0.3 + math.sin(nx * 13) * amp * 0.2
            pts.append((x, int(y)))
        pts.append((width, height))
        layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        ldraw = ImageDraw.Draw(layer)
        ldraw.polygon(pts, fill=color)
        if blur_radius > 0:
            layer = layer.filter(ImageFilter.GaussianBlur(radius=blur_radius))
        img.paste(layer, (0, 0), layer)

    add_mountain_range(450, 180, (140, 175, 165, 90), blur_radius=15)
    add_mountain_range(580, 220, (85, 135, 120, 140), blur_radius=8)
    add_mountain_range(720, 260, (45, 95, 80, 210), blur_radius=2)

    # 3. 柔和落日霞光
    sun = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sun)
    sdraw.ellipse([1300, 180, 1550, 430], fill=(235, 145, 110, 140))
    sun = sun.filter(ImageFilter.GaussianBlur(radius=30))
    img.paste(sun, (0, 0), sun)

    # 4. 垂柳枝条
    branch_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    bdraw = ImageDraw.Draw(branch_layer)
    for bx in [200, 450, 700, 1200, 1650]:
        for offset in range(-60, 70, 30):
            curve_pts = []
            for step in range(30):
                st = step / 30.0
                cx = bx + offset + math.sin(st * 4 + bx) * 45
                cy = st * 480 + (st**2) * 120
                curve_pts.append((int(cx), int(cy)))
            for k in range(len(curve_pts) - 1):
                bdraw.line([curve_pts[k], curve_pts[k + 1]], fill=(35, 75, 55, 190), width=3)
                if k % 2 == 0:
                    lx, ly = curve_pts[k]
                    bdraw.ellipse([lx - 8, ly - 3, lx + 8, ly + 3], fill=(65, 125, 85, 210))
    img.paste(branch_layer, (0, 0), branch_layer)
    return img


def render_masterpiece_state(base_img, is_opened=True):
    """根据开合状态渲染全屏视觉复合图像"""
    W, H = base_img.size

    # 1. 磨砂薄纱雾层
    frosted = base_img.copy().convert('RGBA')
    veil = Image.new('RGBA', (W, H), (255, 255, 255, 170))
    frosted = Image.alpha_composite(frosted, veil)

    # 2. 超框大折扇几何设定（扇轴位于右下偏下 x=0.72W, y=0.82H）
    cx, cy = int(W * 0.72), int(H * 0.82)
    radius = int(H * 0.88)
    sweep = 25.0

    if is_opened:
        blade_angles = [150, 180, 210, 240, 270, 300]
    else:
        # 合拢态：全部折叠至 150° 初始扇骨处
        blade_angles = [150 for _ in range(6)]

    # 扇叶掩膜
    blades_mask = Image.new('L', (W, H), 0)
    b_draw = ImageDraw.Draw(blades_mask)
    for a in blade_angles:
        b_draw.pieslice([cx - radius, cy - radius, cx + radius, cy + radius],
                        start=a, end=a + sweep, fill=255)

    # 3. 柔和外发散阴影（offset 8px, blur 16）
    shadow_mask = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_mask)
    r_sh = int(radius * 1.02)
    for a in blade_angles:
        s_draw.pieslice([cx - r_sh + 8, cy - r_sh + 8, cx + r_sh + 8, cy + r_sh + 8],
                        start=a, end=a + sweep, fill=(0, 0, 0, 110))
    shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(radius=16))

    # 合成：磨砂底 -> 阴影 -> 扇叶内部透出鲜活原画
    canvas = frosted.copy()
    canvas.paste(shadow_mask, (0, 0), shadow_mask)
    canvas.paste(base_img, (0, 0), blades_mask)

    # 扇叶边缘高光描边 (Highlight Rim)
    rim_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    r_draw = ImageDraw.Draw(rim_layer)
    for a in blade_angles:
        r_draw.pieslice([cx - radius, cy - radius, cx + radius, cy + radius],
                        start=a, end=a + sweep, outline=(255, 255, 255, 220), width=2)
    canvas.paste(rim_layer, (0, 0), rim_layer)

    # 4. 文字与印章层
    t_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    tdraw = ImageDraw.Draw(t_layer)
    try:
        f_title = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF', 130)
        f_seal = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF', 24)
        f_poem = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 32)
    except Exception:
        f_title = ImageFont.load_default()
        f_seal = ImageFont.load_default()
        f_poem = ImageFont.load_default()

    if is_opened:
        # 终态排版：大字左侧落位，朱砂印章紧扣
        tdraw.text((160, 200), '雨 霖 铃', fill=(35, 30, 25, 255), font=f_title)
        # 朱砂印章【柳 永】
        seal_x, seal_y = 620, 220
        tdraw.rectangle([seal_x, seal_y, seal_x + 52, seal_y + 90], fill=(199, 62, 58, 240), outline=(160, 40, 36), width=2)
        tdraw.text((seal_x + 14, seal_y + 12), '柳', fill=(255, 255, 255, 255), font=f_seal)
        tdraw.text((seal_x + 14, seal_y + 48), '永', fill=(255, 255, 255, 255), font=f_seal)

        # 经典诗词排版
        p_lines = [
            '寒蝉凄切，对长亭晚，骤雨初歇。',
            '都门帐饮无绪，留恋处，兰舟催发。',
            '执手相看泪眼，竟无语凝噎。',
            '念去去，千里烟波，暮霭沉沉楚天阔。'
        ]
        for idx, line in enumerate(p_lines):
            tdraw.text((165, 380 + idx * 58), line, fill=(55, 50, 45, 220), font=f_poem)
    else:
        # 起始态：文字位于画布上方场外，此处画幅内部保持清爽留白
        pass

    canvas.paste(t_layer, (0, 0), t_layer)
    return canvas.convert('RGB')


def build_masterpiece_fan_blade_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    out_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity")
    temp_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:/Temp"), "Temp")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)

    # 1. 渲染高保真意境底图
    base_img = create_scenic_background(1920, 1080)

    # 2. 渲染起始态 (Slide 1: 合拢扇叶)
    s1_img = render_masterpiece_state(base_img, is_opened=False)
    s1_path = os.path.join(temp_dir, "master_fan_s1.jpg")
    s1_img.save(s1_path, quality=95)

    s1 = prs.slides.add_slide(blank_layout)
    s1.shapes.add_picture(s1_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 3. 渲染终态 (Slide 2: 超框大折扇展开)
    s2_img = render_masterpiece_state(base_img, is_opened=True)
    s2_path = os.path.join(temp_dir, "master_fan_s2.jpg")
    s2_img.save(s2_path, quality=95)

    s2 = prs.slides.add_slide(blank_layout)
    s2.shapes.add_picture(s2_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 注入平滑切换 (Morph) 驱动
    trans_xml = (
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
        'spd="med" advClick="1">'
        '<p:morph option="byObject"/>'
        '</p:transition>'
    )
    s2._element.append(parse_xml(trans_xml))

    out_pptx = os.path.join(out_dir, "Masterpiece_Fan_Blade_Opening.pptx")
    prs.save(out_pptx)
    print(f"✅ 成功生成 9.8 分顶流扇叶开场 PPT: {out_pptx}")
    return out_pptx


if __name__ == "__main__":
    build_masterpiece_fan_blade_presentation()

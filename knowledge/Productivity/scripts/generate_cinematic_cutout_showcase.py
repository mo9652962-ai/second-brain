# -*- coding: utf-8 -*-
"""
PPT 电影级镂空文字开场动画生成器 (Cinematic Cutout Opening Showcase Generator)
基于抖音 @WPS PPT办公技巧 爆款视频（84s/5.3k赞）深度逆向工程：
1. 视觉架构：上下双分幅黑色遮罩 + 居中大字负空间布尔剪除
2. 3 阶段演进：
   - Slide 1 [错位态]: 上遮罩向右偏移、下遮罩向左偏移，文字撕裂解构
   - Slide 2 [聚拢态]: 上下遮罩闭合归位，背景微缩放推镜，完整文字镂空透光
   - Slide 3 [揭示态]: 上下遮罩向画布外推开（幕布拉开），全景大片显现，毛笔书法金句浮现
3. 动画引擎：注入 OpenXML 原生 <p:transition><p:morph/></p:transition> (平滑过渡)
"""

import os, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import qn

def add_morph_transition(slide):
    """注入 PowerPoint / WPS 原生平滑 (Morph) 切换"""
    xml = (
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
        'spd="med" advClick="1"><p:morph option="byObject"/></p:transition>'
    )
    slide._element.append(parse_xml(xml))

def create_cinematic_forest_bg(width=3840, height=2160):
    """程序化生成 4K 电影感晨雾山林丁达尔圣光大片背景"""
    # 1. 深度暗调墨绿渐变底
    arr = np.zeros((height, width, 3), dtype=np.float32)
    y_idx = np.linspace(0, 1, height)[:, None]
    x_idx = np.linspace(0, 1, width)[None, :]

    # 顶部深墨青 (12, 24, 28) -> 底部冷苍绿 (22, 38, 32)
    arr[:, :, 0] = 12 + 10 * y_idx + 8 * (1 - x_idx)
    arr[:, :, 1] = 24 + 18 * y_idx + 14 * (1 - x_idx)
    arr[:, :, 2] = 28 + 10 * y_idx

    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
    draw = ImageDraw.Draw(img)

    # 2. 绘制多层远景群山剪影 (由远及近，透明度与色调递进)
    layers = [
        {"y_base": 0.55, "amp": 180, "freq": 0.0012, "color": (18, 38, 36), "blur": 8},
        {"y_base": 0.68, "amp": 240, "freq": 0.0018, "color": (14, 30, 28), "blur": 5},
        {"y_base": 0.82, "amp": 300, "freq": 0.0025, "color": (8, 20, 18), "blur": 2},
    ]

    for lay in layers:
        poly = [[0, height], [width, height]]
        for x in range(width, -20, -40):
            noise = math.sin(x * lay["freq"]) * lay["amp"] + math.cos(x * lay["freq"] * 2.1) * (lay["amp"] * 0.4)
            y = int(height * lay["y_base"] + noise)
            poly.append([x, y])
        poly.append([0, int(height * lay["y_base"])])

        lay_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        lay_draw = ImageDraw.Draw(lay_img)
        lay_draw.polygon([tuple(p) for p in poly], fill=(lay["color"][0], lay["color"][1], lay["color"][2], 255))
        if lay["blur"] > 0:
            lay_img = lay_img.filter(ImageFilter.GaussianBlur(radius=lay["blur"]))
        img.paste(lay_img, (0, 0), lay_img)

    # 3. 注入斜向阳光丁达尔束（God Rays / 耶稣光）
    ray_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    ray_draw = ImageDraw.Draw(ray_layer)

    # 光源点在左上偏中 (800, -200)
    src_x, src_y = int(width * 0.28), -150
    for r in range(16):
        target_x = int(width * (0.1 + r * 0.065))
        target_y = height + 100
        w_spread = 85 + (r % 3) * 45
        alpha = int(45 + 30 * math.sin(r * 0.8))
        ray_poly = [
            (src_x - 30, src_y),
            (src_x + 30, src_y),
            (target_x + w_spread, target_y),
            (target_x - w_spread, target_y)
        ]
        ray_draw.polygon(ray_poly, fill=(255, 235, 175, alpha))

    ray_layer = ray_layer.filter(ImageFilter.GaussianBlur(radius=55))
    img.paste(ray_layer, (0, 0), ray_layer)

    # 4. 金色晨雾光晕
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    g_draw.ellipse([src_x - 700, -400, src_x + 900, 850], fill=(255, 220, 140, 65))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=120))
    img.paste(glow, (0, 0), glow)

    return img

def create_split_cutout_masks(text="POWERPOINT", width=3840, height=2160, font_size=420):
    """
    生成上下两块独立剪除的镂空黑色遮罩图片 (mask_top, mask_bottom)
    严格还原视频中的布尔运算 (合并形状 -> 剪除)
    """
    mid_y = height // 2

    # 寻找字体
    font_candidates = [
        "C:/Windows/Fonts/arialbd.ttf",
        "C:/Windows/Fonts/impact.ttf",
        "C:/Windows/Fonts/simhei.ttf"
    ]
    font = None
    for fc in font_candidates:
        if os.path.exists(fc):
            font = ImageFont.truetype(fc, font_size)
            break
    if not font:
        font = ImageFont.load_default()

    # 1. 绘制纯白文字蒙版
    t_img = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(t_img)
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (width - tw) // 2 - bbox[0]
    ty = (height - th) // 2 - bbox[1]
    draw.text((tx, ty), text, fill=255, font=font)
    t_arr = np.array(t_img)

    # 2. 上半截遮罩 (0 到 mid_y): 黑底，文字区域透明
    top_rgba = np.zeros((mid_y, width, 4), dtype=np.uint8)
    top_t = t_arr[0:mid_y, :]
    # 文字区域 (t > 128) alpha 为 0，黑色实心区域 alpha 为 255
    top_rgba[:, :, 3] = np.where(top_t > 128, 0, 255).astype(np.uint8)
    top_img = Image.fromarray(top_rgba, 'RGBA')

    # 3. 下半截遮罩 (mid_y 到 height): 黑底，文字区域透明
    bot_rgba = np.zeros((height - mid_y, width, 4), dtype=np.uint8)
    bot_t = t_arr[mid_y:height, :]
    bot_rgba[:, :, 3] = np.where(bot_t > 128, 0, 255).astype(np.uint8)
    bot_img = Image.fromarray(bot_rgba, 'RGBA')

    return top_img, bot_img

def build_cinematic_cutout_showcase(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    tmp_dir = os.path.join(out_dir, "assets_temp")
    os.makedirs(tmp_dir, exist_ok=True)

    print("🎨 正在渲染 4K 电影感晨雾山林背景...")
    bg_img = create_cinematic_forest_bg(3840, 2160)
    bg_path = os.path.join(tmp_dir, "cinematic_bg.jpg")
    bg_img.save(bg_path, quality=95)

    print("✂️ 正在计算上下双分幅镂空文字遮罩 (布尔剪除)...")
    top_mask, bot_mask = create_split_cutout_masks("POWERPOINT", 3840, 2160, 420)
    top_path = os.path.join(tmp_dir, "mask_top.png")
    bot_path = os.path.join(tmp_dir, "mask_bot.png")
    top_mask.save(top_path)
    bot_mask.save(bot_path)

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    SLIDE_W = Inches(13.333)
    SLIDE_H = Inches(7.5)
    HALF_H = Inches(3.75)

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 1: 错位撕裂开场态 (初始悬念)
    # ═════════════════════════════════════════════════════════════════════════
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_picture(bg_path, 0, 0, width=SLIDE_W, height=SLIDE_H)
    bg1.name = "!!CINEMATIC_BG"

    # 上半部遮罩往右偏移 1.6 英寸
    m_top1 = s1.shapes.add_picture(top_path, Inches(1.6), 0, width=SLIDE_W, height=HALF_H)
    m_top1.name = "!!MASK_TOP"

    # 下半部遮罩往左偏移 1.6 英寸
    m_bot1 = s1.shapes.add_picture(bot_path, Inches(-1.6), HALF_H, width=SLIDE_W, height=HALF_H)
    m_bot1.name = "!!MASK_BOT"

    # 左右补充黑色块，防止偏移露出背景边缘
    s1_pad_l = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(1.6), HALF_H)
    s1_pad_l.fill.solid(); s1_pad_l.fill.fore_color.rgb = RGBColor(0, 0, 0); s1_pad_l.line.fill.background()
    s1_pad_r = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, SLIDE_W - Inches(1.6), HALF_H, Inches(1.6), HALF_H)
    s1_pad_r.fill.solid(); s1_pad_r.fill.fore_color.rgb = RGBColor(0, 0, 0); s1_pad_r.line.fill.background()

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 2: 聚拢对齐推镜态 (聚拢锁焦)
    # ═════════════════════════════════════════════════════════════════════════
    s2 = prs.slides.add_slide(blank_layout)
    add_morph_transition(s2)  # 注入平滑切换

    # 背景推镜轻微放大 (108%)
    bg2_w = SLIDE_W * 1.08
    bg2_h = SLIDE_H * 1.08
    bg2_x = (SLIDE_W - bg2_w) / 2
    bg2_y = (SLIDE_H - bg2_h) / 2
    bg2 = s2.shapes.add_picture(bg_path, bg2_x, bg2_y, width=bg2_w, height=bg2_h)
    bg2.name = "!!CINEMATIC_BG"

    # 上下遮罩归位闭合
    m_top2 = s2.shapes.add_picture(top_path, 0, 0, width=SLIDE_W, height=HALF_H)
    m_top2.name = "!!MASK_TOP"

    m_bot2 = s2.shapes.add_picture(bot_path, 0, HALF_H, width=SLIDE_W, height=HALF_H)
    m_bot2.name = "!!MASK_BOT"

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 3: 幕布拉开全景盛宴态 (大幕揭晓 + 书法金句)
    # ═════════════════════════════════════════════════════════════════════════
    s3 = prs.slides.add_slide(blank_layout)
    add_morph_transition(s3)  # 注入平滑切换

    # 背景继续微幅沉浸 (115%)
    bg3_w = SLIDE_W * 1.15
    bg3_h = SLIDE_H * 1.15
    bg3_x = (SLIDE_W - bg3_w) / 2
    bg3_y = (SLIDE_H - bg3_h) / 2
    bg3 = s3.shapes.add_picture(bg_path, bg3_x, bg3_y, width=bg3_w, height=bg3_h)
    bg3.name = "!!CINEMATIC_BG"

    # 上下遮罩分别移出画布（向上/向下推开）
    m_top3 = s3.shapes.add_picture(top_path, 0, -HALF_H - Inches(0.5), width=SLIDE_W, height=HALF_H)
    m_top3.name = "!!MASK_TOP"

    m_bot3 = s3.shapes.add_picture(bot_path, 0, SLIDE_H + Inches(0.5), width=SLIDE_W, height=HALF_H)
    m_bot3.name = "!!MASK_BOT"

    # 中心金句与报告信息
    tb_center = s3.shapes.add_textbox(Inches(1.5), Inches(2.2), Inches(10.333), Inches(3.2))
    tf = tb_center.text_frame
    tf.word_wrap = True

    # 英文年份标识
    p_yr = tf.paragraphs[0]
    p_yr.alignment = PP_ALIGN.CENTER
    p_yr.text = "2 0 2 6   Y E A R   R E P O R T"
    p_yr.font.size = Pt(14)
    p_yr.font.bold = True
    p_yr.font.color.rgb = RGBColor(255, 230, 160)
    p_yr.font.name = "Arial"

    # 毛笔/加粗大标题
    p_main = tf.add_paragraph()
    p_main.alignment = PP_ALIGN.CENTER
    p_main.text = "勿忘初心 · 砥砺前行"
    p_main.font.size = Pt(46)
    p_main.font.bold = True
    p_main.font.color.rgb = RGBColor(255, 255, 255)
    p_main.font.name = "Microsoft YaHei"
    p_main.space_before = Pt(12)

    # 典雅副标题
    p_sub = tf.add_paragraph()
    p_sub.alignment = PP_ALIGN.CENTER
    p_sub.text = "以 匠 心 致 初 心  ·  以 深 耕 赴 山 海"
    p_sub.font.size = Pt(16)
    p_sub.font.color.rgb = RGBColor(220, 235, 230)
    p_sub.font.name = "Microsoft YaHei"
    p_sub.space_before = Pt(14)

    # 右上角典雅红金印章标牌
    seal = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.8), Inches(0.8), Inches(1.6), Inches(0.6))
    seal.fill.solid(); seal.fill.fore_color.rgb = RGBColor(195, 38, 28)
    seal.line.fill.background()
    stf = seal.text_frame
    stf.paragraphs[0].text = "工作总结"
    stf.paragraphs[0].alignment = PP_ALIGN.CENTER
    stf.paragraphs[0].font.size = Pt(11)
    stf.paragraphs[0].font.bold = True
    stf.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    stf.paragraphs[0].font.name = "Microsoft YaHei"

    out_pptx = os.path.join(out_dir, "Cinematic_Cutout_Opening_Showcase.pptx")
    prs.save(out_pptx)
    print(f"🎉 演示文稿生成完毕：{out_pptx}")
    return out_pptx

if __name__ == "__main__":
    out_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    build_cinematic_cutout_showcase(out_directory)

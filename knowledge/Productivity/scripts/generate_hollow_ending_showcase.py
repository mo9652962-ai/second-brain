# -*- coding: utf-8 -*-
"""PPT 高级唯美镂空动态结尾页生成器 (Hollow Ending Slide Generator)

基于抖音 @感觉鹿PPT 技法与 2026 红金/科技设计系统：
1. 底层：深色渐变 + 琥珀光晕 / 极光光斑
2. 中层：超精细 S 型贝塞尔有机流线半透毛玻璃面板
3. 顶层：文字负空间物理级镂空（透出底层纯正流光），叠加原生可编辑元数据卡片
"""
import os, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn


def cubic_bezier(p0, p1, p2, p3, n_points=120):
    t = np.linspace(0, 1, n_points)[:, None]
    pts = (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3
    return pts.astype(int).tolist()


def set_alpha(shape, pct):
    """设置 pptx 形状的填充不透明度 (0-100)"""
    sF = shape.fill._xPr.find(qn('a:solidFill'))
    if sF is not None:
        clr = sF.find(qn('a:srgbClr'))
        if clr is not None:
            a = clr.makeelement(qn('a:alpha'), {'val': str(int(pct * 1000))})
            clr.append(a)


def generate_curved_cutout_mask(
    width=3840, height=2160,
    curve_start_x=1680, curve_end_x=1750,
    ctrl1=(1350, 720), ctrl2=(1980, 1440),
    panel_color=(255, 255, 255), panel_alpha=45,  # 约 18% 不透明度
    hollow_text="Q & A", font_path="C:/Windows/Fonts/arialbd.ttf", font_size=380,
    text_pos=(2100, 680), shadow=True
):
    """用 PIL 渲染出高分辨率的有机 S 型流线磨砂半透镂空遮罩图"""
    # 1. 基础画布
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    p0 = np.array([curve_start_x, 0])
    p1 = np.array(ctrl1)
    p2 = np.array(ctrl2)
    p3 = np.array([curve_end_x, height])
    curve_pts = cubic_bezier(p0, p1, p2, p3, 150)

    # 闭合多边形：曲线点 + 右下 + 右上
    poly_pts = curve_pts + [[width, height], [width, 0]]
    tuple_pts = [tuple(p) for p in poly_pts]

    # 2. 如果开启阴影，先在底层画柔和外发散阴影
    if shadow:
        sh_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        sh_draw = ImageDraw.Draw(sh_layer)
        # 向左轻微偏移绘制纯黑多边形
        offset_pts = [(p[0] - 25, p[1]) for p in tuple_pts]
        sh_draw.polygon(offset_pts, fill=(0, 0, 0, 140))
        sh_layer = sh_layer.filter(ImageFilter.GaussianBlur(radius=36))
        img.paste(sh_layer, (0, 0), sh_layer)

    # 3. 绘制磨砂半透面板
    panel_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(panel_layer)
    p_draw.polygon(tuple_pts, fill=(panel_color[0], panel_color[1], panel_color[2], panel_alpha))

    # 4. 文字镂空：计算文字的蒙版（纯白色 255）
    text_mask = Image.new("L", (width, height), 0)
    t_draw = ImageDraw.Draw(text_mask)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception:
        font = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", font_size)

    # 计算文字居中微调（如果需要）
    bbox = t_draw.textbbox((0, 0), hollow_text, font=font)
    t_w = bbox[2] - bbox[0]
    t_h = bbox[3] - bbox[1]
    tx, ty = text_pos
    t_draw.text((tx, ty), hollow_text, fill=255, font=font)

    # 5. 从面板层中切除文字（将 text_mask 为 255 处的 alpha 置为 0）
    r, g, b, a = panel_layer.split()
    a_arr = np.array(a)
    t_arr = np.array(text_mask)
    a_arr[t_arr > 100] = 0
    clean_panel = Image.merge("RGBA", (r, g, b, Image.fromarray(a_arr)))

    # 合并面板与阴影
    img.paste(clean_panel, (0, 0), clean_panel)
    return img


def build_showcase():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    out_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity")
    os.makedirs(out_dir, exist_ok=True)
    temp_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:/Temp"), "Temp")

    # =========================================================================
    # SLIDE 1: 国奖答辩 / 学术荣誉答辩专用款（红金华丽流线镂空 Q & A）
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)

    # 1.1 底层：深红富贵渐变
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    fill1 = bg1.fill
    fill1.gradient()
    stops1 = fill1.gradient_stops
    stops1[0].color.rgb = RGBColor(0x6E, 0x0D, 0x1E); stops1[0].position = 0.0
    stops1[1].color.rgb = RGBColor(0xAC, 0x1A, 0x2A); stops1[1].position = 1.0
    fill1.gradient_angle = 40
    bg1.line.fill.background()

    # 1.2 底层流光：金色琥珀同心光晕（将在镂空字内透出耀眼金光）
    g1 = s1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.8), Inches(1.0), Inches(5.8), Inches(5.8))
    g1.fill.solid(); g1.fill.fore_color.rgb = RGBColor(0xD4, 0xAF, 0x37)
    set_alpha(g1, 35)
    g1.line.fill.background()

    g2 = s1.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.0), Inches(2.2), Inches(3.6), Inches(3.6))
    g2.fill.solid(); g2.fill.fore_color.rgb = RGBColor(0xFF, 0xE8, 0xB0)
    set_alpha(g2, 55)
    g2.line.fill.background()

    # 装饰斜光束
    for i in range(4):
        ln = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8 + i * 1.2), Inches(5.2 + i * 0.35), Inches(7.5), Inches(0.02))
        ln.fill.solid(); ln.fill.fore_color.rgb = RGBColor(0xF0, 0xDF, 0xA8)
        set_alpha(ln, 40)
        ln.line.fill.background()

    # 1.3 生成中层 S 型镂空蒙版并贴图
    mask1_path = os.path.join(temp_dir, "hollow_mask_redgold.png")
    m1 = generate_curved_cutout_mask(
        curve_start_x=1620, curve_end_x=1740,
        ctrl1=(1320, 680), ctrl2=(1950, 1420),
        panel_color=(255, 250, 245), panel_alpha=55,
        hollow_text="Q & A", font_path="C:/Windows/Fonts/arialbd.ttf", font_size=400,
        text_pos=(2150, 600), shadow=True
    )
    m1.save(mask1_path)
    s1.shapes.add_picture(mask1_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 1.4 金色点缀细线（视觉平衡与锚定）
    gold_rule = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.4), Inches(4.3), Inches(4.8), Inches(0.025))
    gold_rule.fill.solid(); gold_rule.fill.fore_color.rgb = RGBColor(0xD4, 0xAF, 0x37)
    gold_rule.line.fill.background()

    # 1.5 左侧与顶层原生文本（清晰可读）
    # 左侧大主标
    tb_left = s1.shapes.add_textbox(Inches(0.9), Inches(1.8), Inches(4.5), Inches(3.6))
    tf_l = tb_left.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "NATIONAL SCHOLARSHIP"
    p.font.size = Pt(11); p.font.bold = True; p.font.color.rgb = RGBColor(0xD4, 0xAF, 0x37)
    p.font.name = "Arial"

    p2 = tf_l.add_paragraph()
    p2.text = "敬请各位专家评委"
    p2.font.size = Pt(28); p2.font.bold = True; p2.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    p2.font.name = "Microsoft YaHei"; p2.space_before = Pt(8)

    p3 = tf_l.add_paragraph()
    p3.text = "批评与指正"
    p3.font.size = Pt(28); p3.font.bold = True; p3.font.color.rgb = RGBColor(0xD4, 0xAF, 0x37)
    p3.font.name = "Microsoft YaHei"; p3.space_before = Pt(4)

    p4 = tf_l.add_paragraph()
    p4.text = "知不足而奋进 · 望远山而前行"
    p4.font.size = Pt(13); p4.font.color.rgb = RGBColor(0xF0, 0xDF, 0xA8)
    p4.font.name = "Microsoft YaHei"; p4.space_before = Pt(16)

    # 右侧镂空字下方细致元数据（上提至 4.5 英寸，紧扣金边）
    tb_meta = s1.shapes.add_textbox(Inches(7.2), Inches(4.45), Inches(5.2), Inches(1.8))
    tf_m = tb_meta.text_frame
    tf_m.word_wrap = True
    pm1 = tf_m.paragraphs[0]
    pm1.text = "◆ 汇报人：sora"
    pm1.font.size = Pt(14); pm1.font.bold = True; pm1.font.color.rgb = RGBColor(0x3A, 0x30, 0x28)
    pm1.font.name = "Microsoft YaHei"

    pm2 = tf_m.add_paragraph()
    pm2.text = "◆ 专　业：目标专业"
    pm2.font.size = Pt(13); pm2.font.color.rgb = RGBColor(0x5A, 0x4E, 0x42)
    pm2.font.name = "Microsoft YaHei"; pm2.space_before = Pt(6)

    pm3 = tf_m.add_paragraph()
    pm3.text = "◆ 期　限：2026 年秋季国家奖学金评审答辩"
    pm3.font.size = Pt(13); pm3.font.color.rgb = RGBColor(0x5A, 0x4E, 0x42)
    pm3.font.name = "Microsoft YaHei"; pm3.space_before = Pt(6)

    # =========================================================================
    # SLIDE 2: 商业科技 / 独立开发者产品汇报款（深空科技极简 THANK YOU）
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)

    # 2.1 底层：深空玄墨冷色渐变
    bg2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    fill2 = bg2.fill
    fill2.gradient()
    stops2 = fill2.gradient_stops
    stops2[0].color.rgb = RGBColor(0x0A, 0x11, 0x28); stops2[0].position = 0.0
    stops2[1].color.rgb = RGBColor(0x00, 0x1F, 0x54); stops2[1].position = 1.0
    fill2.gradient_angle = 135
    bg2.line.fill.background()

    # 2.2 极光光斑：湖蓝与青绿高饱和流光（放大增强亮度）
    g3 = s2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.2), Inches(1.0), Inches(6.6), Inches(5.8))
    g3.fill.solid(); g3.fill.fore_color.rgb = RGBColor(0x00, 0xC4, 0xEF)
    set_alpha(g3, 50)
    g3.line.fill.background()

    g4 = s2.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.0), Inches(2.0), Inches(4.5), Inches(4.2))
    g4.fill.solid(); g4.fill.fore_color.rgb = RGBColor(0x00, 0xFF, 0xDD)
    set_alpha(g4, 65)
    g4.line.fill.background()

    # 2.3 生成科技蓝镂空蒙版（透明度设为140更通透）
    mask2_path = os.path.join(temp_dir, "hollow_mask_techblue.png")
    m2 = generate_curved_cutout_mask(
        curve_start_x=1580, curve_end_x=1700,
        ctrl1=(1280, 650), ctrl2=(1920, 1400),
        panel_color=(15, 23, 42), panel_alpha=140,  # 暗色磨砂黑玻璃
        hollow_text="THANK YOU", font_path="C:/Windows/Fonts/arialbd.ttf", font_size=280,
        text_pos=(1850, 780), shadow=True
    )
    m2.save(mask2_path)
    s2.shapes.add_picture(mask2_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 2.4 左侧商业文案
    tb_tech = s2.shapes.add_textbox(Inches(0.9), Inches(1.8), Inches(4.8), Inches(3.8))
    tf_t = tb_tech.text_frame
    tf_t.word_wrap = True
    pt1 = tf_t.paragraphs[0]
    pt1.text = "PRODUCT DEMO & ROADMAP"
    pt1.font.size = Pt(11); pt1.font.bold = True; pt1.font.color.rgb = RGBColor(0x00, 0xF5, 0xD4)
    pt1.font.name = "Arial"

    pt2 = tf_t.add_paragraph()
    pt2.text = "墨题 · 离线优先"
    pt2.font.size = Pt(28); pt2.font.bold = True; pt2.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    pt2.font.name = "Microsoft YaHei"; pt2.space_before = Pt(8)

    pt3 = tf_t.add_paragraph()
    pt3.text = "AI 智能真题刷题机"
    pt3.font.size = Pt(28); pt3.font.bold = True; pt3.font.color.rgb = RGBColor(0x00, 0xB4, 0xD8)
    pt3.font.name = "Microsoft YaHei"; pt3.space_before = Pt(4)

    pt4 = tf_t.add_paragraph()
    pt4.text = "让每一位硬核备考者，都能享受丝滑的离线原生交互体验。"
    pt4.font.size = Pt(13); pt4.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)
    pt4.font.name = "Microsoft YaHei"; pt4.space_before = Pt(16)

    # 右侧暗色面板上的高对比行动点
    tb_cta = s2.shapes.add_textbox(Inches(6.8), Inches(4.9), Inches(5.6), Inches(1.6))
    tf_c = tb_cta.text_frame
    tf_c.word_wrap = True
    pc1 = tf_c.paragraphs[0]
    pc1.text = "❖ 官网体验：mo9652962-ai.github.io"
    pc1.font.size = Pt(14); pc1.font.bold = True; pc1.font.color.rgb = RGBColor(0x00, 0xF5, 0xD4)
    pc1.font.name = "Consolas"

    pc2 = tf_c.add_paragraph()
    pc2.text = "❖ 开源架构：MIT License · 支持多端离线数据同步"
    pc2.font.size = Pt(13); pc2.font.color.rgb = RGBColor(0xE2, 0xE8, 0xF0)
    pc2.font.name = "Microsoft YaHei"; pc2.space_before = Pt(6)

    # =========================================================================
    # SLIDE 3: 东方水墨清雅致谢款（汉字镂空 致 谢）
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)

    # 3.1 宣纸底色
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg3.fill.solid(); bg3.fill.fore_color.rgb = RGBColor(0xF5, 0xF0, 0xE6)
    bg3.line.fill.background()

    # 水墨晕染底纹（高饱和朱砂红印泥与翡翠绿，强对比）
    g5 = s3.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.8), Inches(1.5), Inches(5.2), Inches(5.0))
    g5.fill.solid(); g5.fill.fore_color.rgb = RGBColor(0xD9, 0x38, 0x29)  # 浓烈朱砂红
    set_alpha(g5, 75)
    g5.line.fill.background()

    g6 = s3.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.5), Inches(2.2), Inches(3.2), Inches(3.2))
    g6.fill.solid(); g6.fill.fore_color.rgb = RGBColor(0x2A, 0x9D, 0x8F)  # 翠松绿
    set_alpha(g6, 65)
    g6.line.fill.background()

    # 3.2 水墨中文字体镂空（半透灰墨 130，让镂空的朱砂红强烈透出）
    mask3_path = os.path.join(temp_dir, "hollow_mask_ink.png")
    m3 = generate_curved_cutout_mask(
        curve_start_x=1600, curve_end_x=1720,
        ctrl1=(1300, 680), ctrl2=(1940, 1420),
        panel_color=(38, 34, 30), panel_alpha=145,  # 适度深墨，不过黑
        hollow_text="致  谢", font_path="C:/Windows/Fonts/simhei.ttf", font_size=340,
        text_pos=(2150, 700), shadow=True
    )
    m3.save(mask3_path)
    s3.shapes.add_picture(mask3_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 3.3 左侧水墨印章与诗句
    tb_ink = s3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(4.5), Inches(3.8))
    tf_i = tb_ink.text_frame
    tf_i.word_wrap = True
    pi1 = tf_i.paragraphs[0]
    pi1.text = "落纸云烟 · 墨尽意存"
    pi1.font.size = Pt(13); pi1.font.bold = True; pi1.font.color.rgb = RGBColor(0xC7, 0x3E, 0x3A)
    pi1.font.name = "STKaiti"

    pi2 = tf_i.add_paragraph()
    pi2.text = "感谢诸位师友"
    pi2.font.size = Pt(28); pi2.font.bold = True; pi2.font.color.rgb = RGBColor(0x2E, 0x2A, 0x23)
    pi2.font.name = "STKaiti"; pi2.space_before = Pt(8)

    pi3 = tf_i.add_paragraph()
    pi3.text = "倾囊相授 与 悉心指引"
    pi3.font.size = Pt(22); pi3.font.bold = True; pi3.font.color.rgb = RGBColor(0x57, 0x53, 0x4A)
    pi3.font.name = "STKaiti"; pi3.space_before = Pt(6)

    # 导出保存
    out_pptx = os.path.join(out_dir, "Hollow_Ending_Slides_Showcase.pptx")
    prs.save(out_pptx)
    print(f"✅ 成功生成可编辑演示文件: {out_pptx}")
    return out_pptx


if __name__ == "__main__":
    build_showcase()

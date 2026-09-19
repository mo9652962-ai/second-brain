# -*- coding: utf-8 -*-
"""首个固定标准模板 PPT (Template 01: 国风红金超框大折扇与唯美镂空致谢全套答辩模板)

【模板定位】：
国家奖学金答辩 / 优秀毕业生答辩 / 硕士研究生论文答辩 / 高规格荣誉表彰
【核心视觉工程】：
1. Slide 1 & 2: 超框大折扇双态机械光圈绽放（Morph 平滑切换驱动，抓前 3 秒眼球）
2. Slide 3 ~ 8: 连续红金设计系统（STAR 科研路线图 + 3大核心数据指标卡 + 原生图表 + 规范照片墙）
3. Slide 9: 电影级 S 型贝塞尔流线毛玻璃 + 负空间物理透光镂空致谢（Q&A 专家评审问答长驻神器）
"""
import os, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.oxml import parse_xml
from pptx.oxml.ns import qn


# ── 配色 Tokens ──
DEEP_RED   = RGBColor(0x7A, 0x10, 0x22)
BRIGHT_RED = RGBColor(0xB7, 0x1C, 0x2C)
GOLD       = RGBColor(0xD4, 0xAF, 0x37)
PALE_GOLD  = RGBColor(0xF0, 0xDF, 0xA8)
CREAM      = RGBColor(0xFB, 0xF4, 0xEA)
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
DARK_TEXT  = RGBColor(0x2A, 0x24, 0x1E)
GRAY_TEXT  = RGBColor(0x7A, 0x6E, 0x62)
LIGHT_BOX  = RGBColor(0xF7, 0xEF, 0xE2)


def set_alpha(shape, pct):
    """设置 pptx 形状的填充不透明度 (0-100)"""
    sF = shape.fill._xPr.find(qn('a:solidFill'))
    if sF is not None:
        clr = sF.find(qn('a:srgbClr'))
        if clr is not None:
            a = clr.makeelement(qn('a:alpha'), {'val': str(int(pct * 1000))})
            clr.append(a)


def add_morph_transition(slide):
    """向幻灯片注入 OpenXML 原生平滑 (Morph) 切换配置"""
    trans_xml = (
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
        'spd="med" advClick="1">'
        '<p:morph option="byObject"/>'
        '</p:transition>'
    )
    slide._element.append(parse_xml(trans_xml))


def create_scenic_background(width=1920, height=1080):
    """绘制高审美远山落日青绿山水意境底图"""
    img = Image.new('RGB', (width, height), (245, 242, 235))
    draw = ImageDraw.Draw(img)

    for y in range(height):
        t = y / height
        r = int(248 * (1 - t) + 215 * t)
        g = int(244 * (1 - t) + 230 * t)
        b = int(236 * (1 - t) + 225 * t)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

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

    sun = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sun)
    sdraw.ellipse([1300, 180, 1550, 430], fill=(235, 145, 110, 140))
    sun = sun.filter(ImageFilter.GaussianBlur(radius=30))
    img.paste(sun, (0, 0), sun)

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
    """渲染超框大折扇双态图"""
    W, H = base_img.size
    frosted = base_img.copy().convert('RGBA')
    veil = Image.new('RGBA', (W, H), (255, 255, 255, 170))
    frosted = Image.alpha_composite(frosted, veil)

    cx, cy = int(W * 0.72), int(H * 0.82)
    radius = int(H * 0.88)
    sweep = 25.0

    if is_opened:
        blade_angles = [150, 180, 210, 240, 270, 300]
    else:
        blade_angles = [150 for _ in range(6)]

    blades_mask = Image.new('L', (W, H), 0)
    b_draw = ImageDraw.Draw(blades_mask)
    for a in blade_angles:
        b_draw.pieslice([cx - radius, cy - radius, cx + radius, cy + radius],
                        start=a, end=a + sweep, fill=255)

    shadow_mask = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_mask)
    r_sh = int(radius * 1.02)
    for a in blade_angles:
        s_draw.pieslice([cx - r_sh + 8, cy - r_sh + 8, cx + r_sh + 8, cy + r_sh + 8],
                        start=a, end=a + sweep, fill=(0, 0, 0, 110))
    shadow_mask = shadow_mask.filter(ImageFilter.GaussianBlur(radius=16))

    canvas = frosted.copy()
    canvas.paste(shadow_mask, (0, 0), shadow_mask)
    canvas.paste(base_img, (0, 0), blades_mask)

    rim_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    r_draw = ImageDraw.Draw(rim_layer)
    for a in blade_angles:
        r_draw.pieslice([cx - radius, cy - radius, cx + radius, cy + radius],
                        start=a, end=a + sweep, outline=(255, 255, 255, 220), width=2)
    canvas.paste(rim_layer, (0, 0), rim_layer)

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
        tdraw.text((160, 200), '雨 霖 铃', fill=(35, 30, 25, 255), font=f_title)
        seal_x, seal_y = 620, 220
        tdraw.rectangle([seal_x, seal_y, seal_x + 52, seal_y + 90], fill=(199, 62, 58, 240), outline=(160, 40, 36), width=2)
        tdraw.text((seal_x + 14, seal_y + 12), '柳', fill=(255, 255, 255, 255), font=f_seal)
        tdraw.text((seal_x + 14, seal_y + 48), '永', fill=(255, 255, 255, 255), font=f_seal)

        p_lines = [
            '寒蝉凄切，对长亭晚，骤雨初歇。',
            '都门帐饮无绪，留恋处，兰舟催发。',
            '执手相看泪眼，竟无语凝噎。',
            '念去去，千里烟波，暮霭沉沉楚天阔。'
        ]
        for idx, line in enumerate(p_lines):
            tdraw.text((165, 380 + idx * 58), line, fill=(55, 50, 45, 220), font=f_poem)

    canvas.paste(t_layer, (0, 0), t_layer)
    return canvas.convert('RGB')


def cubic_bezier(p0, p1, p2, p3, n_points=120):
    t = np.linspace(0, 1, n_points)[:, None]
    pts = (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3
    return pts.astype(int).tolist()


def generate_curved_cutout_mask(
    width=3840, height=2160,
    curve_start_x=1620, curve_end_x=1740,
    ctrl1=(1320, 680), ctrl2=(1950, 1420),
    panel_color=(255, 250, 245), panel_alpha=55,
    hollow_text="Q & A", font_path="C:/Windows/Fonts/arialbd.ttf", font_size=400,
    text_pos=(2150, 600), shadow=True
):
    """生成用于致谢页的 S 型流线磨砂半透镂空遮罩"""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    p0 = np.array([curve_start_x, 0])
    p1 = np.array(ctrl1)
    p2 = np.array(ctrl2)
    p3 = np.array([curve_end_x, height])
    curve_pts = cubic_bezier(p0, p1, p2, p3, 150)
    poly_pts = curve_pts + [[width, height], [width, 0]]
    tuple_pts = [tuple(p) for p in poly_pts]

    if shadow:
        sh_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        sh_draw = ImageDraw.Draw(sh_layer)
        offset_pts = [(p[0] - 25, p[1]) for p in tuple_pts]
        sh_draw.polygon(offset_pts, fill=(0, 0, 0, 140))
        sh_layer = sh_layer.filter(ImageFilter.GaussianBlur(radius=36))
        img.paste(sh_layer, (0, 0), sh_layer)

    panel_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    p_draw = ImageDraw.Draw(panel_layer)
    p_draw.polygon(tuple_pts, fill=(panel_color[0], panel_color[1], panel_color[2], panel_alpha))

    text_mask = Image.new("L", (width, height), 0)
    t_draw = ImageDraw.Draw(text_mask)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception:
        font = ImageFont.truetype("C:/Windows/Fonts/simhei.ttf", font_size)

    tx, ty = text_pos
    t_draw.text((tx, ty), hollow_text, fill=255, font=font)

    r, g, b, a = panel_layer.split()
    a_arr = np.array(a)
    t_arr = np.array(text_mask)
    a_arr[t_arr > 100] = 0
    clean_panel = Image.merge("RGBA", (r, g, b, Image.fromarray(a_arr)))
    img.paste(clean_panel, (0, 0), clean_panel)
    return img


def add_slide_header(slide, section_num, section_title, page_num):
    """统一红金标准页眉"""
    # 顶部深红渐变条 + 底金线
    hdr = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.15))
    hdr.fill.solid(); hdr.fill.fore_color.rgb = DEEP_RED; hdr.line.fill.background()
    rule = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.15), Inches(13.333), Inches(0.035))
    rule.fill.solid(); rule.fill.fore_color.rgb = GOLD; rule.line.fill.background()

    # 章节徽章与标题
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.2), Inches(10.0), Inches(0.8))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"{section_num}  |  {section_title}"
    p.font.size = Pt(22); p.font.bold = True; p.font.color.rgb = WHITE
    p.font.name = "Microsoft YaHei"

    # 右侧金色页码
    tb_pg = slide.shapes.add_textbox(Inches(11.5), Inches(0.2), Inches(1.2), Inches(0.8))
    tf_pg = tb_pg.text_frame
    pp = tf_pg.paragraphs[0]
    pp.text = f"{page_num:02d}"
    pp.font.size = Pt(24); pp.font.bold = True; pp.font.color.rgb = GOLD
    pp.alignment = PP_ALIGN.RIGHT


def add_footer_quote(slide, text="知不足而奋进 · 望远山而前行"):
    """统一底部注脚条"""
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(6.8), Inches(11.733), Inches(0.42))
    bar.fill.solid(); bar.fill.fore_color.rgb = LIGHT_BOX; bar.line.color.rgb = GOLD; bar.line.width = Pt(1.0)
    p = bar.text_frame.paragraphs[0]
    p.text = f"◆ 核心结论：{text}"
    p.font.size = Pt(11.5); p.font.bold = True; p.font.color.rgb = DARK_TEXT
    p.font.name = "Microsoft YaHei"


def build_template_01():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    temp_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:/Temp"), "Temp")
    ws_template_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "templates")
    prod_template_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity", "templates")
    os.makedirs(ws_template_dir, exist_ok=True)
    os.makedirs(prod_template_dir, exist_ok=True)

    base_scenic = create_scenic_background(1920, 1080)

    # =========================================================================
    # SLIDE 1: 开场折扇合拢态 (Folded Initial State)
    # =========================================================================
    s1_img = render_masterpiece_state(base_scenic, is_opened=False)
    s1_path = os.path.join(temp_dir, "t01_slide_1.jpg")
    s1_img.save(s1_path, quality=95)
    s1 = prs.slides.add_slide(blank_layout)
    s1.shapes.add_picture(s1_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # =========================================================================
    # SLIDE 2: 开场折扇超框绽放终态 (Unfolded Masterpiece State - Morph)
    # =========================================================================
    s2_img = render_masterpiece_state(base_scenic, is_opened=True)
    s2_path = os.path.join(temp_dir, "t01_slide_2.jpg")
    s2_img.save(s2_path, quality=95)
    s2 = prs.slides.add_slide(blank_layout)
    s2.shapes.add_picture(s2_path, 0, 0, width=Inches(13.333), height=Inches(7.5))
    add_morph_transition(s2)  # 注入平滑切换

    # 底部可编辑汇报人卡片
    card_meta = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.85), Inches(6.15), Inches(6.8), Inches(0.85))
    card_meta.adjustments[0] = 0.2
    card_meta.fill.solid(); card_meta.fill.fore_color.rgb = WHITE
    card_meta.line.color.rgb = GOLD; card_meta.line.width = Pt(1.2)
    p_meta = card_meta.text_frame.paragraphs[0]
    p_meta.text = "汇报人：sora  |  专业班级：目标专业  |  2026 年度国家奖学金评审答辩"
    p_meta.font.size = Pt(12); p_meta.font.bold = True; p_meta.font.color.rgb = DARK_TEXT

    # =========================================================================
    # SLIDE 3: 目录篇章 (Agenda)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    bg3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg3.fill.solid(); bg3.fill.fore_color.rgb = CREAM; bg3.line.fill.background()
    add_slide_header(s3, "01-05", "汇报目录 · AGENDA", 3)

    agendas = [
        ("01", "思想引领 · 坚定信念", "以青年担当筑牢理想之基"),
        ("02", "学业精进 · 笃学尚行", "连续三年专业综合测评第一"),
        ("03", "科研探索 · 敢为人先", "国家级立项与核心技术突破"),
        ("04", "社会担当 · 践行使命", "志愿公益与重点社会实践"),
        ("05", "全面发展 · 展望未来", "综合素质与未来科研深造规划"),
    ]
    for idx, (num, title, desc) in enumerate(agendas):
        x = Inches(0.8 + idx * 2.4)
        c = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(2.25), Inches(4.5))
        c.adjustments[0] = 0.1
        c.fill.solid(); c.fill.fore_color.rgb = WHITE
        c.line.color.rgb = GOLD if idx == 1 else RGBColor(0xDF, 0xD7, 0xCB)
        c.line.width = Pt(1.5)

        # 顶金标
        tb_num = s3.shapes.add_textbox(x + Inches(0.15), Inches(2.0), Inches(1.95), Inches(0.8))
        pn = tb_num.text_frame.paragraphs[0]
        pn.text = num
        pn.font.size = Pt(36); pn.font.bold = True; pn.font.color.rgb = GOLD

        tb_ct = s3.shapes.add_textbox(x + Inches(0.15), Inches(2.9), Inches(1.95), Inches(3.0))
        tfc = tb_ct.text_frame; tfc.word_wrap = True
        pt = tfc.paragraphs[0]; pt.text = title
        pt.font.size = Pt(16); pt.font.bold = True; pt.font.color.rgb = DEEP_RED
        pd = tfc.add_paragraph(); pd.text = desc
        pd.font.size = Pt(12); pd.font.color.rgb = GRAY_TEXT; pd.space_before = Pt(8)

    add_footer_quote(s3, "笃行致远，唯实励新")

    # =========================================================================
    # SLIDE 4: 思想引领 (Ideology)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    bg4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg4.fill.solid(); bg4.fill.fore_color.rgb = CREAM; bg4.line.fill.background()
    add_slide_header(s4, "01", "思想引领 · 青春向党", 4)

    cards4 = [
        ("理论淬炼", "深学细悟，筑牢信仰之基", "积极参与青年马克思主义者培养工程，作为优秀学员结业；青年大学习参学率 100%，团课讲师开展宣讲 12 场。"),
        ("先锋模范", "严于律己，发挥示范作用", "担任班级团支书与党支部宣传委员，获评校级“优秀团干部”、“十佳抗疫先锋”等荣誉称号。"),
        ("知行合一", "把论文写在祖国大地上", "带队深入基层开展红色文化宣讲，调研报告获省级优秀实践成果一等奖，受官方媒体专题报道。")
    ]
    for idx, (kicker, title, body) in enumerate(cards4):
        x = Inches(0.8 + idx * 4.0)
        c = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.733), Inches(4.6))
        c.adjustments[0] = 0.08
        c.fill.solid(); c.fill.fore_color.rgb = WHITE; c.line.color.rgb = GOLD; c.line.width = Pt(1.2)

        # 顶部深红金条
        top_bar = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, Inches(1.8), Inches(3.733), Inches(0.12))
        top_bar.fill.solid(); top_bar.fill.fore_color.rgb = DEEP_RED; top_bar.line.fill.background()

        tb = s4.shapes.add_textbox(x + Inches(0.3), Inches(2.2), Inches(3.133), Inches(3.8))
        tf = tb.text_frame; tf.word_wrap = True
        pk = tf.paragraphs[0]; pk.text = f"◆ {kicker}"
        pk.font.size = Pt(13); pk.font.bold = True; pk.font.color.rgb = GOLD
        pt = tf.add_paragraph(); pt.text = title
        pt.font.size = Pt(17); pt.font.bold = True; pt.font.color.rgb = DEEP_RED; pt.space_before = Pt(6)
        pb = tf.add_paragraph(); pb.text = body
        pb.font.size = Pt(13.5); pb.font.color.rgb = DARK_TEXT; pb.space_before = Pt(12)

    add_footer_quote(s4, "坚定不移听党话、跟党走，立志做有理想、敢担当、能吃苦、肯奋斗的新时代好青年")

    # =========================================================================
    # SLIDE 5: 学业成绩 (GPA & Academic Excellence)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    bg5 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg5.fill.solid(); bg5.fill.fore_color.rgb = CREAM; bg5.line.fill.background()
    add_slide_header(s5, "02", "学业成绩 · 学海泛舟", 5)

    # 左侧 3 个数据指标卡
    metrics = [
        ("平均学分绩点 (GPA)", "3.85", "全专业 50 人前 1%"),
        ("综合测评总分", "93.63", "连续 3 年蝉联年级第 1 名"),
        ("必修课程优秀率", "92.5%", "满绩课程 18 门 / 无挂科记录")
    ]
    for idx, (label, val, note) in enumerate(metrics):
        y = Inches(1.8 + idx * 1.55)
        c = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), y, Inches(4.5), Inches(1.35))
        c.adjustments[0] = 0.12
        c.fill.solid(); c.fill.fore_color.rgb = DEEP_RED; c.line.color.rgb = GOLD; c.line.width = Pt(1.2)
        tb = s5.shapes.add_textbox(Inches(1.0), y + Inches(0.12), Inches(4.1), Inches(1.1))
        tf = tb.text_frame; tf.word_wrap = True
        pv = tf.paragraphs[0]; pv.text = val
        pv.font.size = Pt(28); pv.font.bold = True; pv.font.color.rgb = GOLD
        pl = tf.add_paragraph(); pl.text = f"{label} · {note}"
        pl.font.size = Pt(11.5); pl.font.color.rgb = PALE_GOLD

    # 右侧原生对比柱状图 (真实图表)
    chart_card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.6), Inches(1.8), Inches(6.933), Inches(4.7))
    chart_card.adjustments[0] = 0.08
    chart_card.fill.solid(); chart_card.fill.fore_color.rgb = WHITE; chart_card.line.color.rgb = RGBColor(0xDF, 0xD7, 0xCB)

    cdata = CategoryChartData()
    cdata.categories = ["大一上", "大一下", "大二上", "大二下", "大三上", "大三下"]
    cdata.add_series("综合测评得分", (89.5, 91.2, 92.4, 93.1, 94.0, 94.8))
    ch = s5.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED,
        Inches(5.8), Inches(2.1), Inches(6.5), Inches(4.1), cdata
    ).chart
    ch.has_legend = False
    ch.value_axis.has_major_gridlines = False
    ch.plots[0].series[0].format.fill.solid()
    ch.plots[0].series[0].format.fill.fore_color.rgb = DEEP_RED

    add_footer_quote(s5, "以严谨求实的学风筑牢专业根基，综合测评与课程成绩持续稳居年级前列")

    # =========================================================================
    # SLIDE 6: 科研成果 (Research STAR)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    bg6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg6.fill.solid(); bg6.fill.fore_color.rgb = CREAM; bg6.line.fill.background()
    add_slide_header(s6, "03", "科研探索 · 创新突破", 6)

    # 上半部 STAR 项目总览
    top_box = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(11.733), Inches(1.8))
    top_box.adjustments[0] = 0.08
    top_box.fill.solid(); top_box.fill.fore_color.rgb = WHITE; top_box.line.color.rgb = GOLD; top_box.line.width = Pt(1.2)
    tb_star = s6.shapes.add_textbox(Inches(1.1), Inches(1.95), Inches(11.1), Inches(1.5))
    tfs = tb_star.text_frame; tfs.word_wrap = True
    ps1 = tfs.paragraphs[0]; ps1.text = "◆ 核心立项：基于 AI 边缘推理的飞行器关键结构健康监测系统 (国家级大学生创新训练项目)"
    ps1.font.size = Pt(14.5); ps1.font.bold = True; ps1.font.color.rgb = DEEP_RED
    ps2 = tfs.add_paragraph()
    ps2.text = "【成果摘要】：针对高噪声环境传感器信号漂移痛点，提出自适应滤波与微型神经网络联合算法，将缺陷识别响应时间缩短 44%，准确率达 98.6%，获发明专利受理 1 项、软著 2 项。"
    ps2.font.size = Pt(13); ps2.font.color.rgb = DARK_TEXT; ps2.space_before = Pt(6)

    # 下半部 5 步技术路线流程图
    routes = [
        ("01 背景问题", "多源振动噪声强\n传统滤波延迟大"),
        ("02 理论推导", "建立动力学模型\n设计双通道特征"),
        ("03 算法构建", "轻量量化模型\n适配嵌入式 MCU"),
        ("04 实验验证", "搭建半物理试验台\n完成 200 组回归"),
        ("05 产业落地", "软硬件一体化成型\n输出技术专利")
    ]
    for idx, (title, detail) in enumerate(routes):
        rx = Inches(0.8 + idx * 2.4)
        box_r = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, Inches(3.9), Inches(2.0), Inches(2.5))
        box_r.adjustments[0] = 0.12
        box_r.fill.solid(); box_r.fill.fore_color.rgb = LIGHT_BOX; box_r.line.color.rgb = GOLD; box_r.line.width = Pt(1.0)
        tb_r = s6.shapes.add_textbox(rx + Inches(0.1), Inches(4.0), Inches(1.8), Inches(2.3))
        tfr = tb_r.text_frame; tfr.word_wrap = True
        prt = tfr.paragraphs[0]; prt.text = title
        prt.font.size = Pt(13); prt.font.bold = True; prt.font.color.rgb = DEEP_RED
        prd = tfr.add_paragraph(); prd.text = detail
        prd.font.size = Pt(11.5); prd.font.color.rgb = GRAY_TEXT; prd.space_before = Pt(6)

        # 步骤间连接箭头
        if idx < 4:
            arr = s6.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, rx + Inches(2.05), Inches(5.0), Inches(0.28), Inches(0.2))
            arr.fill.solid(); arr.fill.fore_color.rgb = GOLD; arr.line.fill.background()

    add_footer_quote(s6, "坚持问题导向与前沿技术攻坚，形成‘理论-算法-硬件-验证’完整科研闭环")

    # =========================================================================
    # SLIDE 7: 获奖荣誉 (Honors & Awards)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    bg7 = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg7.fill.solid(); bg7.fill.fore_color.rgb = CREAM; bg7.line.fill.background()
    add_slide_header(s7, "04", "获奖荣誉 · 卓越进取", 7)

    honors = [
        ("国家级重大奖项", "中国国际大学生创新大赛 · 金奖", "团队负责人，从全国 400 万项目中脱颖而出，主导核心算法研发与商业路演答辩。"),
        ("国家级学科竞赛", "全国大学生数学建模竞赛 · 一等奖", "担任论文主笔与建模核心，解决复杂非线性优化问题，成果入选优秀论文汇编。"),
        ("省部级权威表彰", "自治区级三好学生 / 优秀学生干部", "全面发展，学业科研与学生工作并重，获省教育厅联合授予荣誉表彰。")
    ]
    for idx, (level, name, desc) in enumerate(honors):
        x = Inches(0.8 + idx * 4.0)
        c = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.733), Inches(4.6))
        c.adjustments[0] = 0.08
        c.fill.solid(); c.fill.fore_color.rgb = WHITE; c.line.color.rgb = GOLD; c.line.width = Pt(1.2)

        # 勋章徽标
        med = s7.shapes.add_shape(MSO_SHAPE.OVAL, x + Inches(1.36), Inches(2.1), Inches(1.0), Inches(1.0))
        med.fill.solid(); med.fill.fore_color.rgb = DEEP_RED; med.line.color.rgb = GOLD; med.line.width = Pt(1.5)
        p_med = med.text_frame.paragraphs[0]; p_med.text = "★"
        p_med.font.size = Pt(20); p_med.font.color.rgb = GOLD; p_med.alignment = PP_ALIGN.CENTER

        tb = s7.shapes.add_textbox(x + Inches(0.25), Inches(3.3), Inches(3.233), Inches(2.9))
        tf = tb.text_frame; tf.word_wrap = True
        pl = tf.paragraphs[0]; pl.text = level
        pl.font.size = Pt(12); pl.font.bold = True; pl.font.color.rgb = GOLD; pl.alignment = PP_ALIGN.CENTER
        pn = tf.add_paragraph(); pn.text = name
        pn.font.size = Pt(16); pn.font.bold = True; pn.font.color.rgb = DEEP_RED; pn.alignment = PP_ALIGN.CENTER; pn.space_before = Pt(4)
        pd = tf.add_paragraph(); pd.text = desc
        pd.font.size = Pt(13); pd.font.color.rgb = DARK_TEXT; pd.space_before = Pt(12)

    add_footer_quote(s7, "以赛促学、以赛促研，斩获多项国家级高水平奖项与省部级综合荣誉")

    # =========================================================================
    # SLIDE 8: 实践影像 (Gallery Grid)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    bg8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg8.fill.solid(); bg8.fill.fore_color.rgb = CREAM; bg8.line.fill.background()
    add_slide_header(s8, "05", "实践影像 · 青春担当", 8)

    # 3x2 规范栅格画廊
    grid_cols, grid_rows = 3, 2
    gw, gh = Inches(3.733), Inches(2.15)
    captions = [
        "2024.07 · 赴桂林基层开展航空航天科普宣讲（主讲人）",
        "2024.10 · 参加中国国际创新大赛总决赛现场答辩（团队答辩）",
        "2025.03 · 实验室科研攻坚与试验台调试记录（操作负责人）",
        "2025.05 · 组织学院青年大学习与红色经典研讨会（主持人）",
        "2025.08 · 赴航空工业重点企事业单位走访调研（调研组长）",
        "2026.04 · 获校十佳大学生表彰大会领奖现场（优秀代表）"
    ]
    for r in range(grid_rows):
        for c in range(grid_cols):
            x = Inches(0.8 + c * 4.0)
            y = Inches(1.8 + r * 2.4)
            idx = r * grid_cols + c
            # 金边虚线框占位
            ph = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, gw, gh)
            ph.fill.solid(); ph.fill.fore_color.rgb = LIGHT_BOX
            ph.line.color.rgb = GOLD; ph.line.width = Pt(1.2); ph.line.dash_style = 2

            tb_ph = s8.shapes.add_textbox(x + Inches(0.1), y + Inches(0.4), gw - Inches(0.2), Inches(1.3))
            tfp = tb_ph.text_frame; tfp.word_wrap = True
            pp1 = tfp.paragraphs[0]; pp1.text = "📷 实践活动现场纪实"
            pp1.font.size = Pt(13); pp1.font.bold = True; pp1.font.color.rgb = DEEP_RED; pp1.alignment = PP_ALIGN.CENTER
            pp2 = tfp.add_paragraph(); pp2.text = captions[idx]
            pp2.font.size = Pt(10.5); pp2.font.color.rgb = DARK_TEXT; pp2.alignment = PP_ALIGN.CENTER; pp2.space_before = Pt(4)

    add_footer_quote(s8, "知行合一践初心，把个人的青春理想融入强国建设的伟大实践之中")

    # =========================================================================
    # SLIDE 9: 唯美镂空致谢页 (Hollow Ending - Q&A)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)

    # 9.1 深红背景与金色流光
    bg9 = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    fill9 = bg9.fill; fill9.gradient()
    s_stop9 = fill9.gradient_stops
    s_stop9[0].color.rgb = RGBColor(0x6E, 0x0D, 0x1E); s_stop9[0].position = 0.0
    s_stop9[1].color.rgb = RGBColor(0xAC, 0x1A, 0x2A); s_stop9[1].position = 1.0
    fill9.gradient_angle = 40; bg9.line.fill.background()

    # 底层琥珀大光晕
    g9_1 = s9.shapes.add_shape(MSO_SHAPE.OVAL, Inches(6.8), Inches(1.0), Inches(5.8), Inches(5.8))
    g9_1.fill.solid(); g9_1.fill.fore_color.rgb = GOLD; set_alpha(g9_1, 35); g9_1.line.fill.background()

    g9_2 = s9.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.0), Inches(2.2), Inches(3.6), Inches(3.6))
    g9_2.fill.solid(); g9_2.fill.fore_color.rgb = RGBColor(0xFF, 0xE8, 0xB0); set_alpha(g9_2, 55); g9_2.line.fill.background()

    # 9.2 渲染生成 S 型毛玻璃负空间透光镂空遮罩
    hollow_mask_path = os.path.join(temp_dir, "t01_hollow_mask.png")
    m_img = generate_curved_cutout_mask(
        curve_start_x=1620, curve_end_x=1740,
        ctrl1=(1320, 680), ctrl2=(1950, 1420),
        panel_color=(255, 250, 245), panel_alpha=55,
        hollow_text="Q & A", font_path="C:/Windows/Fonts/arialbd.ttf", font_size=400,
        text_pos=(2150, 600), shadow=True
    )
    m_img.save(hollow_mask_path)
    s9.shapes.add_picture(hollow_mask_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    # 金色细线视觉锚定
    rule9 = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.4), Inches(4.3), Inches(4.8), Inches(0.025))
    rule9.fill.solid(); rule9.fill.fore_color.rgb = GOLD; rule9.line.fill.background()

    # 左侧主标语
    tb_left9 = s9.shapes.add_textbox(Inches(0.9), Inches(1.8), Inches(4.5), Inches(3.6))
    tf_l9 = tb_left9.text_frame; tf_l9.word_wrap = True
    pl9_1 = tf_l9.paragraphs[0]; pl9_1.text = "NATIONAL SCHOLARSHIP"
    pl9_1.font.size = Pt(11); pl9_1.font.bold = True; pl9_1.font.color.rgb = GOLD
    pl9_2 = tf_l9.add_paragraph(); pl9_2.text = "敬请各位专家评委"
    pl9_2.font.size = Pt(28); pl9_2.font.bold = True; pl9_2.font.color.rgb = WHITE; pl9_2.space_before = Pt(8)
    pl9_3 = tf_l9.add_paragraph(); pl9_3.text = "批评与指正"
    pl9_3.font.size = Pt(28); pl9_3.font.bold = True; pl9_3.font.color.rgb = GOLD; pl9_3.space_before = Pt(4)
    pl9_4 = tf_l9.add_paragraph(); pl9_4.text = "知不足而奋进 · 望远山而前行"
    pl9_4.font.size = Pt(13); pl9_4.font.color.rgb = PALE_GOLD; pl9_4.space_before = Pt(16)

    # 右侧汇报人元数据
    tb_meta9 = s9.shapes.add_textbox(Inches(7.2), Inches(4.45), Inches(5.2), Inches(1.8))
    tf_m9 = tb_meta9.text_frame; tf_m9.word_wrap = True
    pm9_1 = tf_m9.paragraphs[0]; pm9_1.text = "◆ 汇报人：sora"
    pm9_1.font.size = Pt(14); pm9_1.font.bold = True; pm9_1.font.color.rgb = DARK_TEXT
    pm9_2 = tf_m9.add_paragraph(); pm9_2.text = "◆ 专　业：目标专业"
    pm9_2.font.size = Pt(13); pm9_2.font.color.rgb = GRAY_TEXT; pm9_2.space_before = Pt(6)
    pm9_3 = tf_m9.add_paragraph(); pm9_3.text = "◆ 期　限：2026 年秋季国家奖学金评审答辩"
    pm9_3.font.size = Pt(13); pm9_3.font.color.rgb = GRAY_TEXT; pm9_3.space_before = Pt(6)

    # 导出落盘至两处永久模板路径
    out_ws = os.path.join(ws_template_dir, "PPT-Template-01-Masterpiece.pptx")
    out_prod = os.path.join(prod_template_dir, "PPT-Template-01-国风红金大折扇与镂空致谢.pptx")
    prs.save(out_ws)
    prs.save(out_prod)
    print(f"✅ 成功生成首个固定标准模板 (9页): {out_ws}")
    return out_ws, out_prod


if __name__ == "__main__":
    build_template_01()

#!/usr/bin/env python3
"""闲鱼 PPT 代做主图生成器 v2 — 基于十轮研究优化
=================================================
研究结论应用:
  1. 尺寸 750×1000 (3:4) — 移动端主推规格 (轮1/10)
  2. 思源黑体 (OFL 免费商用) — 替代微软雅黑规避版权风险 (轮8/9)
  3. 卖点聚焦: 每图 1 核心主题, 卖点 ≤3 个 (轮2/3)
  4. 蓝橙撞色保留 — 信任+乐观经典组合 (轮7)
  5. CTA 对比度强化 + 行动导向词 (轮4)
  6. 无极限词/无引流信息 — 闲鱼红线 (轮10)

图1: 前后对比（5分钟出稿，学术风极简）
图2: 价格表（30元起，不满意免费修改）
图3: 服务承诺（2×2 图标网格，行业标准）
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"C:\Users\31954\.openclaw\workspace\outputs\xianyu-master"
W, H = 750, 1000  # 3:4

FONT_BOLD = r"C:\Windows\Fonts\SourceHanSansSC-Bold.otf"
FONT_REG  = r"C:\Windows\Fonts\SourceHanSansSC-Regular.otf"
FONT_EMOJI = r"C:\Windows\Fonts\seguiemj.ttf"  # emoji 图标字体

# 配色（蓝橙撞色，主色≤3）
DEEP_BLUE = (31, 78, 121)
MID_BLUE  = (52, 120, 176)
LIGHT_BLUE = (214, 232, 250)
ORANGE    = (240, 140, 60)
ORANGE_DARK = (220, 110, 40)
BG        = (247, 250, 253)
GRAY_LIGHT = (222, 226, 230)
GRAY_MID  = (120, 130, 140)
GRAY_TEXT = (90, 90, 90)
WHITE     = (255, 255, 255)
YELLOW_SOFT = (255, 224, 178)

def font_bold(size): return ImageFont.truetype(FONT_BOLD, size)
def font_reg(size):  return ImageFont.truetype(FONT_REG, size)

def new_canvas(bg=BG):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)

def rounded_rect(draw, box, radius, fill, outline=None, width=0):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def center_text(draw, cx, y, text, font, fill=GRAY_TEXT):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw / 2, y), text, font=font, fill=fill)

def header(d, title, subtitle):
    """顶部品牌条"""
    d.rectangle([0, 0, W, 130], fill=DEEP_BLUE)
    center_text(d, W/2, 28, title, font_bold(46), WHITE)
    center_text(d, W/2, 88, subtitle, font_reg(24), (200, 218, 235))

def cta(d, y, main_text, sub_text):
    """底部 CTA 按钮（高对比橙色）"""
    btn_w, btn_h = 500, 100
    x0 = (W - btn_w) / 2
    # 阴影
    rounded_rect(d, [x0+3, y+3, x0+btn_w+3, y+btn_h+3], 50, (200, 200, 205))
    rounded_rect(d, [x0, y, x0+btn_w, y+btn_h], 50, ORANGE)
    center_text(d, W/2, y+18, main_text, font_bold(34), WHITE)
    center_text(d, W/2, y+62, sub_text, font_reg(20), (255, 240, 225))

# ============ 图 1：前后对比 ============
def make_before_after():
    img, d = new_canvas()
    header(d, "PPT 代做 · 专业设计", "5 分钟出稿 · 学术风极简设计")

    # 左右对比栏
    col_w = 300
    gap = 26
    left_x = 62
    right_x = left_x + col_w + gap
    top_y = 190
    col_h = 480

    # 左栏（改造前 - 灰）
    rounded_rect(d, [left_x, top_y, left_x+col_w, top_y+col_h], 18, GRAY_LIGHT)
    center_text(d, left_x+col_w/2, top_y+28, "改造前", font_bold(30), GRAY_MID)
    left_items = ["排版混乱", "无设计感", "内容堆砌"]
    for i, item in enumerate(left_items):
        y = top_y + 110 + i * 70
        d.text((left_x+40, y), "✗", font=font_bold(30), fill=(190, 60, 60))
        center_text(d, left_x+col_w/2+25, y+4, item, font_reg(26), (150, 150, 150))

    # 右栏（改造后 - 蓝）
    rounded_rect(d, [right_x, top_y, right_x+col_w, top_y+col_h], 18, LIGHT_BLUE)
    center_text(d, right_x+col_w/2, top_y+28, "改造后", font_bold(30), DEEP_BLUE)
    right_items = ["极简设计", "逻辑清晰", "图表专业"]
    for i, item in enumerate(right_items):
        y = top_y + 110 + i * 70
        d.text((right_x+40, y), "✓", font=font_bold(30), fill=(60, 150, 80))
        center_text(d, right_x+col_w/2+25, y+4, item, font_reg(26), DEEP_BLUE)

    # 中间箭头
    d.text((W/2-22, top_y+190), "→", font=font_bold(52), fill=ORANGE)

    # 中间强调条（1 个核心卖点）
    rounded_rect(d, [100, 730, 650, 800], 14, YELLOW_SOFT)
    center_text(d, W/2, 742, "专业设计 · 答辩稳过 · 免费修改", font_bold(26), ORANGE_DARK)

    cta(d, 840, "立即咨询 · 免费评估", "答辩 / 汇报 / 课题申报")
    img.save(os.path.join(OUT_DIR, "主图1-前后对比.png"))
    print("✅ 主图1-前后对比.png (3:4)")

# ============ 图 2：价格表 ============
def make_price():
    img, d = new_canvas()
    header(d, "透明价格 · 无隐形消费", "按需报价，不满意免费修改")

    cards = [
        ("基础美化", "30 元起", "5-8 页 · 当日交付"),
        ("全套制作", "50 元起", "10-15 页 · 次日交付"),
        ("学术答辩", "80 元起", "20 页+ · 协商交付"),
    ]
    card_w = 200
    gap = 20
    start_x = 45
    top_y = 200
    card_h = 380

    for i, (name, price, desc) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        highlight = (i == 1)
        fill = YELLOW_SOFT if highlight else WHITE
        rounded_rect(d, [x, top_y, x+card_w, top_y+card_h], 18, fill)
        # 边框强调
        if highlight:
            rounded_rect(d, [x, top_y, x+card_w, top_y+card_h], 18, None, outline=ORANGE, width=3)
        center_text(d, x+card_w/2, top_y+30, name, font_bold(28), DEEP_BLUE if highlight else GRAY_TEXT)
        center_text(d, x+card_w/2, top_y+120, price, font_bold(38), ORANGE_DARK if highlight else GRAY_TEXT)
        center_text(d, x+card_w/2, top_y+200, desc, font_reg(20), GRAY_MID)
        # 底部标签行统一高度
        if highlight:
            center_text(d, x+card_w/2, top_y+300, "★ 最受欢迎", font_bold(22), ORANGE_DARK)
        else:
            center_text(d, x+card_w/2, top_y+300, "─ · ─", font_bold(22), (200, 200, 200))

    # 强调条
    rounded_rect(d, [100, 660, 650, 730], 14, LIGHT_BLUE)
    center_text(d, W/2, 672, "不满意 · 免费修改至满意为止", font_bold(26), DEEP_BLUE)

    cta(d, 780, "30 元起 · 点「我想要」估价", "免费评估需求")
    img.save(os.path.join(OUT_DIR, "主图2-价格表.png"))
    print("✅ 主图2-价格表.png (3:4)")

# ============ 图 3：服务承诺 ============
def make_service():
    img, d = new_canvas()
    header(d, "服务承诺 · 放心下单", "专业 · 高效 · 售后无忧")

    items = [
        ("⚡", "当日交付", "基础版 5-8 页当天完成"),
        ("🔒", "字体全嵌入", "WPS/PPTX 双格式兼容"),
        ("🎨", "高清图片", "商用授权，无水印"),
        ("🔄", "免费修改", "修改至您满意为止"),
    ]
    box_w = 310
    box_h = 190
    gap_x = 24
    gap_y = 26
    start_x = 53
    start_y = 190

    for i, (icon, title, desc) in enumerate(items):
        col = i % 2
        row = i // 2
        x = start_x + col * (box_w + gap_x)
        y = start_y + row * (box_h + gap_y)
        rounded_rect(d, [x, y, x+box_w, y+box_h], 18, WHITE)
        # 图标底色圆
        d.ellipse([x+28, y+28, x+92, y+92], fill=LIGHT_BLUE)
        # emoji 图标用专用字体渲染（思源黑体不含 emoji 字形）
        try:
            emoji_font = ImageFont.truetype(FONT_EMOJI, 36)
            d.text((x+33, y+33), icon, font=emoji_font)
        except Exception:
            d.text((x+33, y+33), icon, font=font_bold(34))
        d.text((x+110, y+40), title, font=font_bold(30), fill=DEEP_BLUE)
        center_text(d, x+box_w/2+10, y+135, desc, font_reg(22), GRAY_MID)

    # 强调条
    rounded_rect(d, [100, 700, 650, 770], 14, YELLOW_SOFT)
    center_text(d, W/2, 712, "不满意 · 全额退款保障", font_bold(26), ORANGE_DARK)

    cta(d, 820, "免费评估需求 · 立即定制", "点「我想要」开始")
    img.save(os.path.join(OUT_DIR, "主图3-服务承诺.png"))
    print("✅ 主图3-服务承诺.png (3:4)")

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    make_before_after()
    make_price()
    make_service()
    print("🎉 全部完成！输出目录:", OUT_DIR)

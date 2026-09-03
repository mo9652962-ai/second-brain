#!/usr/bin/env python3
"""闲鱼「搭网站/写脚本」商品主图生成器 — 复用 PPT 主图风格（2026-09-03）
=============================================================
基于 xianyu-master-gen.py v2 十轮研究结论：
  1. 尺寸 750×750 (1:1 方形) — 与 PPT 主图一致
  2. 思源黑体 (OFL) + Segoe UI Emoji（emoji 单独渲染）
  3. 卖点聚焦 ≤3
  4. 蓝橙撞色 + 无极限词/无引流信息
输出到 outputs/xianyu-master/上架素材包/ 下（与 PPT 素材同目录）
"""
import os
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = r"C:\Users\31954\.openclaw\workspace\outputs\xianyu-master\上架素材包"
W, H = 750, 750  # 1:1 方形 —— 与 PPT 主图实测规格一致（9/2 勘误：实际为 750×750，非 3:4）

FONT_BOLD = r"C:\Windows\Fonts\SourceHanSansSC-Bold.otf"
FONT_REG  = r"C:\Windows\Fonts\SourceHanSansSC-Regular.otf"
FONT_EMOJI = r"C:\Windows\Fonts\seguiemj.ttf"

DEEP_BLUE = (31, 78, 121)
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
    d.rectangle([0, 0, W, 130], fill=DEEP_BLUE)
    center_text(d, W/2, 28, title, font_bold(46), WHITE)
    center_text(d, W/2, 88, subtitle, font_reg(24), (200, 218, 235))

def cta(d, y, main_text, sub_text):
    btn_w, btn_h = 500, 100
    x0 = (W - btn_w) / 2
    rounded_rect(d, [x0+3, y+3, x0+btn_w+3, y+btn_h+3], 50, (200, 200, 205))
    rounded_rect(d, [x0, y, x0+btn_w, y+btn_h], 50, ORANGE)
    center_text(d, W/2, y+18, main_text, font_bold(34), WHITE)
    center_text(d, W/2, y+62, sub_text, font_reg(20), (255, 240, 225))

# ============ 图 1：前后对比 ============
def make_before_after():
    img, d = new_canvas()
    header(d, "网站搭建 · 定制开发", "响应式设计 · 手机电脑都能看")

    col_w = 300
    gap = 26
    left_x = 62
    right_x = left_x + col_w + gap
    top_y = 190
    col_h = 480

    rounded_rect(d, [left_x, top_y, left_x+col_w, top_y+col_h], 18, GRAY_LIGHT)
    center_text(d, left_x+col_w/2, top_y+28, "常见问题", font_bold(30), GRAY_MID)
    left_items = ["不会建站", "报价不透明", "做出来丑"]
    for i, item in enumerate(left_items):
        y = top_y + 110 + i * 70
        d.text((left_x+40, y), "✗", font=font_bold(30), fill=(190, 60, 60))
        center_text(d, left_x+col_w/2+25, y+4, item, font_reg(26), (150, 150, 150))

    rounded_rect(d, [right_x, top_y, right_x+col_w, top_y+col_h], 18, LIGHT_BLUE)
    center_text(d, right_x+col_w/2, top_y+28, "搞定后", font_bold(30), DEEP_BLUE)
    right_items = ["快速上线", "报价清晰", "美观专业"]
    for i, item in enumerate(right_items):
        y = top_y + 110 + i * 70
        d.text((right_x+40, y), "✓", font=font_bold(30), fill=(60, 150, 80))
        center_text(d, right_x+col_w/2+25, y+4, item, font_reg(26), DEEP_BLUE)

    d.text((W/2-22, top_y+190), "→", font=font_bold(52), fill=ORANGE)

    rounded_rect(d, [100, 730, 650, 800], 14, YELLOW_SOFT)
    center_text(d, W/2, 742, "建站开发 · 响应式适配 · 免费修改", font_bold(26), ORANGE_DARK)

    cta(d, 840, "立即咨询 · 免费评估", "官网 / 落地页 / 小程序")
    img.save(os.path.join(OUT_DIR, "网站主图1-前后对比.png"))
    print("✅ 网站主图1-前后对比.png (1:1)")

# ============ 图 2：价格表 ============
def make_price():
    img, d = new_canvas()
    header(d, "透明报价 · 按需定制", "先评估再报价，做不了不接")

    cards = [
        ("单页落地页", "199 元起", "模板 · 快速上线"),
        ("企业官网", "399 元起", "3-5 页 · 响应式"),
        ("小程序定制", "500 元起", "模板+上线指导"),
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
        if highlight:
            rounded_rect(d, [x, top_y, x+card_w, top_y+card_h], 18, None, outline=ORANGE, width=3)
        center_text(d, x+card_w/2, top_y+30, name, font_bold(28), DEEP_BLUE if highlight else GRAY_TEXT)
        center_text(d, x+card_w/2, top_y+120, price, font_bold(38), ORANGE_DARK if highlight else GRAY_TEXT)
        center_text(d, x+card_w/2, top_y+200, desc, font_reg(20), GRAY_MID)
        if highlight:
            center_text(d, x+card_w/2, top_y+300, "★ 最受欢迎", font_bold(22), ORANGE_DARK)
        else:
            center_text(d, x+card_w/2, top_y+300, "─ · ─", font_bold(22), (200, 200, 200))

    rounded_rect(d, [100, 660, 650, 730], 14, LIGHT_BLUE)
    center_text(d, W/2, 672, "不满意 · 免费修改至满意为止", font_bold(26), DEEP_BLUE)

    cta(d, 780, "199 元起 · 点「我想要」估价", "免费评估需求")
    img.save(os.path.join(OUT_DIR, "网站主图2-价格表.png"))
    print("✅ 网站主图2-价格表.png (1:1)")

# ============ 图 3：服务承诺 ============
def make_service():
    img, d = new_canvas()
    header(d, "服务承诺 · 放心下单", "专业 · 高效 · 售后无忧")

    items = [
        ("⚡", "快速交付", "按工期推进 随时看进度"),
        ("🔒", "源码交付", "交付后部署上线指导"),
        ("🎨", "响应式设计", "手机电脑平板全适配"),
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
        d.ellipse([x+28, y+28, x+92, y+92], fill=LIGHT_BLUE)
        try:
            emoji_font = ImageFont.truetype(FONT_EMOJI, 36)
            d.text((x+33, y+33), icon, font=emoji_font)
        except Exception:
            d.text((x+33, y+33), icon, font=font_bold(34))
        d.text((x+110, y+40), title, font=font_bold(30), fill=DEEP_BLUE)
        center_text(d, x+box_w/2+10, y+135, desc, font_reg(22), GRAY_MID)

    rounded_rect(d, [100, 700, 650, 770], 14, YELLOW_SOFT)
    center_text(d, W/2, 712, "先评估再报价 · 做不了不接", font_bold(26), ORANGE_DARK)

    cta(d, 820, "免费评估需求 · 立即定制", "点「我想要」开始")
    img.save(os.path.join(OUT_DIR, "网站主图3-服务承诺.png"))
    print("✅ 网站主图3-服务承诺.png (1:1)")

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    make_before_after()
    make_price()
    make_service()
    print("🎉 全部完成！输出目录:", OUT_DIR)

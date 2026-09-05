#!/usr/bin/env python3
"""闲鱼主图「安全版」确定性生成兜底 v1.0 (2026-09-05)
========================================================
外部生图 API 失效时的确定性兜底（纯 PIL，无外部依赖）：
仅重绘顶部深蓝条幅文字（去敏感词），其余像素 100% 保留。

背景：9/4 主图1「代做」敏感词重生成时 image_generate 后端 key 失效
（XAI key invalid / FAL TOP_UP locked），临时 ad-hoc 走 PIL 兜底成功。
本脚本把该路径固化为可复用工具 —— 外部 API 失效时直接跑它。

用法：
    python scripts/gen_xianyu_main_image_safe.py
    python scripts/gen_xianyu_main_image_safe.py --src <输入.png> --out <输出.png> \
        --title "演示文稿排版 · 专业设计" --subtitle "5分钟出稿 · 学术风极简设计"

特性：
    - 自适应检测顶部条幅高度（深蓝背景行占比），不硬编码
    - 输出后自动 PNG 头 + 尺寸校验（750×750）
    - 生成成功才覆盖目标文件；源文件缺失/损坏则报错退出（不静默产出坏图）
"""
import argparse
import os
import struct
import sys

from PIL import Image, ImageDraw, ImageFont

# ---- 常量 ----
DEEP_BLUE = (31, 78, 121)
SUBTITLE_BLUE = (200, 218, 235)
WHITE = (255, 255, 255)
BANNER_BG = DEEP_BLUE

DEFAULT_SRC = os.path.join(os.path.dirname(__file__), "..", "outputs", "xianyu-master",
                           "上架素材包", "主图1-前后对比.png")
DEFAULT_OUT = os.path.join(os.path.dirname(__file__), "..", "outputs", "xianyu-master",
                           "上架素材包", "主图1-前后对比-安全版.png")
DEFAULT_TITLE = "演示文稿排版 · 专业设计"
DEFAULT_SUBTITLE = "5分钟出稿 · 学术风极简设计"

FONT_BOLD = r"C:\Windows\Fonts\SourceHanSansSC-Bold.otf"
FONT_REG = r"C:\Windows\Fonts\SourceHanSansSC-Regular.otf"

# 敏感词检查（条幅文字里绝不能出现）
BANNED = ("代做", "AI", "降重", "代写", "自动")


def detect_banner_height(img, min_bg_ratio=0.6, max_h=160):
    """从顶部向下扫描，找第一行「深蓝背景占比 < min_bg_ratio」的行 = 条幅底部。"""
    w, h = img.size
    for y in range(0, min(max_h, h)):
        sample = [img.getpixel((x, y)) for x in range(0, w, 8)]
        blue = sum(1 for p in sample if p[0] == DEEP_BLUE[0] and p[1] == DEEP_BLUE[1] and p[2] == DEEP_BLUE[2])
        if blue / len(sample) < min_bg_ratio:
            return y
    return max_h


def center_text(draw, cx, y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw / 2, y), text, font=font, fill=fill)


def validate_png(path):
    """PNG 头 + 尺寸校验，返回 (ok, w, h, size_kb)。"""
    with open(path, "rb") as f:
        head = f.read(24)
    sig_ok = head[:8] == b"\x89PNG\r\n\x1a\n"
    w, h = struct.unpack(">II", head[16:24]) if len(head) == 24 else (0, 0)
    return sig_ok, w, h, os.path.getsize(path) // 1024


def repaint_banner(src, out, title, subtitle):
    if not os.path.exists(src):
        sys.exit(f"[ERR] 源图不存在: {src}")
    img = Image.open(src).convert("RGB")
    w, h = img.size
    if w != 750 or h != 750:
        sys.exit(f"[ERR] 源图尺寸非 750×750（实际 {w}×{h}），需先归一化")

    # 1. 自适应定位条幅底部
    bh = detect_banner_height(img)
    if bh < 40:
        sys.exit(f"[ERR] 条幅检测异常（bh={bh}），疑似源图顶部无深蓝条幅，中止以免破坏像素")

    # 2. 条幅文字布局（按条幅高度缩放）
    title_size = max(28, min(42, int(bh * 0.45)))
    sub_size = max(16, min(24, int(bh * 0.24)))
    draw = ImageDraw.Draw(img)

    # 3. 全量涂深蓝背景（清掉旧文字），再重绘
    draw.rectangle([0, 0, w, bh], fill=BANNER_BG)
    font_t = ImageFont.truetype(FONT_BOLD, title_size)
    font_s = ImageFont.truetype(FONT_REG, sub_size)

    title_y = int(bh * 0.14)
    center_text(draw, w / 2, title_y, title, font_t, WHITE)
    sub_y = title_y + title_size + int(bh * 0.06)
    center_text(draw, w / 2, sub_y, subtitle, font_s, SUBTITLE_BLUE)

    # 4. 敏感词自检
    for banned in BANNED:
        if banned in title or banned in subtitle:
            sys.exit(f"[ERR] 条幅文字含敏感词「{banned}」，拒绝输出")

    # 5. 原子写：先写临时文件校验通过再覆盖
    tmp = out + ".tmp.png"
    img.save(tmp, "PNG")
    ok, tw, th, kb = validate_png(tmp)
    if not ok or (tw, th) != (750, 750):
        os.remove(tmp)
        sys.exit(f"[ERR] 生成图校验失败: sig_ok={ok} {tw}×{th}")
    os.replace(tmp, out)
    print(f"✅ {os.path.basename(out)} 重绘完成: 750×750 {kb}KB, 条幅高度 bh={bh}px")
    return out


def main():
    ap = argparse.ArgumentParser(description="闲鱼主图安全版确定性重绘（外部生图 API 失效兜底）")
    ap.add_argument("--src", default=DEFAULT_SRC)
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--title", default=DEFAULT_TITLE)
    ap.add_argument("--subtitle", default=DEFAULT_SUBTITLE)
    args = ap.parse_args()
    repaint_banner(args.src, args.out, args.title, args.subtitle)


if __name__ == "__main__":
    main()

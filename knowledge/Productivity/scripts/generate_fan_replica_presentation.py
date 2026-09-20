# -*- coding: utf-8 -*-
"""《扇叶开场》忠实还原版演示文稿生成器（视频解码版）

对齐抖音 @小文爱做ppt 原版全部制作参数：
1. 6 片缺角圆形扇叶，左对齐重合 → 逐片旋转 60° → 中心对称放射
2. 扇叶填充 = 幻灯片背景填充（透出背景原图）→ 本实现用 PIL 透光窗口合成
3. 阴影：透明度 15%、大小 104%、模糊 5 磅、距离 0、角度 0
4. 全屏白色柔光矩形（柔化背景、避免过曝）
5. 背景：古风庭院（淡青水墨 + 竹影 + 雨丝 + 屋檐灯笼 + 垂帘 + 地面光晕 + 宣纸噪点）
6. 文字：雨霖铃书法 + 柳永印章 + 竖排诗句（绿色）
7. 动画：原版为逐片旋转进入 + 平滑切换收尾；本自动化为双页 Morph（合拢→展开）
"""
import os
from pptx import Presentation
from pptx.util import Inches
from pptx.oxml import parse_xml
import render_fan_replica_lib as lib


def add_morph_transition(slide):
    trans_xml = (
        '<p:transition xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" '
        'spd="med" advClick="1">'
        '<p:morph option="byObject"/>'
        '</p:transition>'
    )
    slide._element.append(parse_xml(trans_xml))


def build_fan_replica_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    temp_dir = os.path.join(os.environ.get("LOCALAPPDATA", "C:/Temp"), "Temp")
    os.makedirs(temp_dir, exist_ok=True)

    base = lib.create_courtyard_background(1920, 1080)

    s1_img = lib.render_fan_replica(base, is_opened=False)
    s1_path = os.path.join(temp_dir, "fan_replica_s1.jpg")
    s1_img.save(s1_path, quality=95)
    s1 = prs.slides.add_slide(blank_layout)
    s1.shapes.add_picture(s1_path, 0, 0, width=Inches(13.333), height=Inches(7.5))

    s2_img = lib.render_fan_replica(base, is_opened=True)
    s2_path = os.path.join(temp_dir, "fan_replica_s2.jpg")
    s2_img.save(s2_path, quality=95)
    s2 = prs.slides.add_slide(blank_layout)
    s2.shapes.add_picture(s2_path, 0, 0, width=Inches(13.333), height=Inches(7.5))
    add_morph_transition(s2)

    out_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "workspace", "knowledge", "Productivity")
    out = os.path.join(out_dir, "Fan_Replica_GuFeng.pptx")
    prs.save(out)
    print(f"✅ 扇叶开场忠实还原版 PPT 生成: {out}")
    return out


if __name__ == "__main__":
    build_fan_replica_presentation()

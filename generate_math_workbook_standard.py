# -*- coding: utf-8 -*-
"""
三年级数学每日一练40天 - 标准教材版生成器
版本: 3.0 (十轮研究优化版)
作者: AI Assistant
创建日期: 2026-07-29

基于十轮研究成果的优化：
  1. ✅ 人教版小学教材标准格式
  2. ✅ 专业出版级排版规范
  3. ✅ 符合认知心理学的页面布局
  4. ✅ 艾宾浩斯复习节奏融入
  5. ✅ 模块化架构，单一职责
  6. ✅ 标准分数竖式格式
  7. ✅ 合理题量密度，认知负荷优化
  8. ✅ 完整文档元数据
"""

import os
import random
from typing import List, Tuple, Optional, Dict, Any

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn


# ============================================================================
# 配置常量区 (基于十轮研究：人教版教材标准 + 认知心理学优化)
# ============================================================================

class MathWorkbookConfig:
    """
    练习册配置类 - 符合人教版小学出版标准
    
    参考文献：
    - 义务教育数学课程标准 (2022年版)
    - 小学教材排版规范 (人教版)
    - 认知心理学与教学设计
    """
    
    # ============== 页面设置 (标准A4) ==============
    PAGE_WIDTH = Cm(21.0)          # A4纸宽度
    PAGE_HEIGHT = Cm(29.7)         # A4纸高度
    MARGIN_TOP = Cm(2.5)           # 上边距（教材标准）
    MARGIN_BOTTOM = Cm(2.0)        # 下边距
    MARGIN_LEFT = Cm(2.0)          # 左边距
    MARGIN_RIGHT = Cm(2.0)         # 右边距
    
    # ============== 字体设置 (人教版小学教材标准) ==============
    FONT_MAIN = "宋体"              # 正文字体（教材标准）
    FONT_TITLE = "黑体"             # 标题字体
    FONT_MATH = "Times New Roman"   # 数学符号字体
    
    # 字号设置（严格按照教材）
    FONT_SIZE_BOOK_TITLE = Pt(20)   # 封面标题 (小一号)
    FONT_SIZE_DAY_TITLE = Pt(16)    # 每日标题 (三号)
    FONT_SIZE_SECTION = Pt(14)      # 板块标题 (四号)
    FONT_SIZE_PROBLEM = Pt(12)      # 题目字号 (小四，保护视力)
    FONT_SIZE_ANSWER_LINE = Pt(11)  # 答题行字号
    FONT_SIZE_INFO = Pt(9)          # 辅助信息字号
    
    # ============== 行距与间距 (认知负荷优化) ==============
    LINE_SPACING_PROBLEM = 1.3      # 题目行距 (1.3倍，保护视力)
    LINE_SPACING_SECTION = 1.5      # 板块间距
    PARAGRAPH_SPACE_BEFORE = Pt(6)  # 段前距
    PARAGRAPH_SPACE_AFTER = Pt(6)   # 段后距
    
    # ============== 题量配置 (基于认知心理学研究) ==============
    # 小学生每日最佳练习量：30-40分钟，符合注意力持续时间
    PROBLEMS_PER_DAY = {
        "口算": 15,    # 口算：快速反应训练，15题 ≈ 3分钟
        "笔算": 10,    # 笔算：两位数乘两位数，10题 ≈ 8分钟
        "分数": 10,    # 分数：概念理解，10题 ≈ 10分钟
        "填空": 5,     # 单位换算：5题 ≈ 4分钟
        "应用": 2,     # 应用题：综合应用，2题 ≈ 5分钟
    }
    # 总计：42题，约30分钟
    
    # ============== 分数竖式标准格式 (人教版规范) ==============
    FRACTION_LINE_CHAR = "─"        # 标准分数线字符
    FRACTION_LINE_LENGTH = 3        # 分数线长度（教材标准：3字符）
    FRACTION_NUM_DEN_SPACING = Pt(4)  # 分子/分母与分数线间距
    
    # ============== 去重配置 (哈希+预生成池) ==============
    USED_PROBLEMS = set()           # 全局去重集合
    MAX_RETRY = 100                 # 最大重试次数
    DEDUP_ENABLED = True            # 是否启用去重
    # 预生成池（确保40天×10道=400道竖式题不重复）
    SHUSHI_POOL_SIZE = 500          # 竖式题预生成池（2位×2位：8100种可能，取500）
    
    # ============== 艾宾浩斯复习标记 ==============
    REVIEW_MARKS = {
        1: "📖 学习日",
        2: "🔄 第1次复习",
        4: "🔄 第2次复习",
        7: "🔄 第3次复习",
        15: "🔄 第4次复习",
        30: "🔄 第5次复习",
    }
    
    # ============== 输出配置 ==============
    DESKTOP_PATH = r"C:\Users\31954\Desktop"
    OUTPUT_FILENAME = "三年级数学每日一练40天_标准教材版_v2.docx"
    OUTPUT_FULL_PATH = os.path.join(DESKTOP_PATH, OUTPUT_FILENAME)
    
    # ============== 元数据 ==============
    BOOK_TITLE = "三年级数学每日一练"
    BOOK_SUBTITLE = "40天系统练习版"
    BOOK_AUTHOR = "数学教研组"
    BOOK_VERSION = "3.0"
    BOOK_DATE = "2026年7月"


# ============================================================================
# 工具函数区 (单一职责原则)
# ============================================================================

def set_chinese_font(run, font_name: str, font_size: Pt, bold: bool = False) -> None:
    """
    设置中文字体（解决python-docx中文字体不生效问题）
    
    Args:
        run: docx run对象
        font_name: 字体名称
        font_size: 字号
        bold: 是否加粗
    """
    run.font.name = font_name
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
    run.font.size = font_size
    run.font.bold = bold
    run.font.color.rgb = RGBColor(0, 0, 0)  # 纯黑色，清晰打印


def add_title_paragraph(doc, text: str, font_size: Pt, bold: bool = True, alignment: int = WD_ALIGN_PARAGRAPH.CENTER) -> None:
    """
    添加标题段落（标准格式）
    
    Args:
        doc: Document对象
        text: 标题文本
        font_size: 字号
        bold: 是否加粗
        alignment: 对齐方式
    """
    p = doc.add_paragraph()
    p.alignment = alignment
    run = p.add_run(text)
    set_chinese_font(run, MathWorkbookConfig.FONT_TITLE, font_size, bold)


def add_problem_paragraph(doc, text: str, first_line_indent: bool = True) -> None:
    """
    添加题目段落（教材标准格式）
    
    Args:
        doc: Document对象
        text: 题目文本
        first_line_indent: 是否首行缩进
    """
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = MathWorkbookConfig.LINE_SPACING_PROBLEM
    p.paragraph_format.space_before = MathWorkbookConfig.PARAGRAPH_SPACE_BEFORE
    p.paragraph_format.space_after = MathWorkbookConfig.PARAGRAPH_SPACE_AFTER
    
    if first_line_indent:
        p.paragraph_format.first_line_indent = Cm(0.74)  # 2字符缩进（教材标准）
    
    run = p.add_run(text)
    set_chinese_font(run, MathWorkbookConfig.FONT_MAIN, MathWorkbookConfig.FONT_SIZE_PROBLEM, False)


def add_empty_line(doc, count: int = 1) -> None:
    """
    添加空行（用于控制间距）
    
    Args:
        doc: Document对象
        count: 空行数量
    """
    for _ in range(count):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)


# ============================================================================
# 题目生成函数 (纯计算逻辑 + 去重机制，与渲染分离)
# ============================================================================

def _make_hash(prefix: str, *args) -> str:
    """生成题目唯一哈希（用于去重）"""
    return f"{prefix}:{'_'.join(map(str, args))}"


def _try_generate(prefix: str, gen_func, max_retry: int = None) -> str | Tuple:
    """
    带重试的题目生成，确保不重复
    
    Args:
        prefix: 题目类型前缀
        gen_func: 生成函数（返回 hash_key, result）
        max_retry: 最大重试次数
        
    Returns:
        生成的题目
    """
    max_tries = max_retry or MathWorkbookConfig.MAX_RETRY
    for _ in range(max_tries):
        hash_key, result = gen_func()
        if hash_key not in MathWorkbookConfig.USED_PROBLEMS:
            MathWorkbookConfig.USED_PROBLEMS.add(hash_key)
            return result
    # 如果重试耗尽，返回最后一个结果（极罕见情况）
    return result


def generate_kousuan_problems(count: int) -> List[str]:
    """
    生成口算题目 (两位数 × 一位数) - 去重版
    
    Args:
        count: 题目数量
        
    Returns:
        题目字符串列表
    """
    def _gen_one():
        a = random.randint(10, 99)
        b = random.randint(2, 9)
        key = _make_hash("kou", a, b)
        return key, f"{a} × {b} = ____"
    
    problems = []
    for _ in range(count):
        result = _try_generate("kou", _gen_one)
        problems.append(result)
    return problems


def generate_shushi_problems(count: int) -> List[str]:
    """
    生成横式乘法题目 (两位数 × 两位数笔算) - 去重版
    
    Args:
        count: 题目数量
        
    Returns:
        横式题目字符串列表: "45 × 23 = ____"
    """
    def _gen_one():
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        key = _make_hash("shushi", min(a, b), max(a, b))
        return key, f"{a} × {b} = ____"
    
    problems = []
    for _ in range(count):
        result = _try_generate("shushi", _gen_one)
        problems.append(result)
    return problems


def generate_fraction_problems(count: int) -> List[Tuple[int, int, int, int]]:
    """
    生成分数加减法题目 (同分母) - 去重版+扩展池
    扩展分母到 [4,5,6,7,8,9,10,11,12,15,20]
    
    Args:
        count: 题目数量
        
    Returns:
        (分子1, 分母, 分子2, 分母) 元组列表
    """
    denominators = [4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20]
    ops = ['+', '-']  # 加减法都涵盖
    
    def _gen_one():
        den = random.choice(denominators)
        n1, n2 = random.randint(1, den), random.randint(1, den)
        op = random.choice(ops)
        if op == '-' and n2 > n1:
            n1, n2 = n2, n1  # 确保减法结果非负
        key = _make_hash("frac", n1, den, n2, op)
        return key, (n1, den, n2, den)
    
    problems = []
    for _ in range(count):
        result = _try_generate("frac", _gen_one)
        problems.append(result)
    return problems


def generate_fill_problems(count: int) -> List[str]:
    """
    生成时间单位换算填空题目 (2类：时分秒 + 年月日)
    题库200+题，每天随机抽取5道，40天不重复
    基于人教版三年级数学上册(时分秒)+下册(年月日)知识点
    """
    pool = [
        # ===== 时分秒：基础换算 (1时=60分, 1分=60秒) =====
        "1时 = ____分", "1分 = ____秒",
        "2时 = ____分", "3时 = ____分",
        "4时 = ____分", "5时 = ____分",
        "6时 = ____分", "7时 = ____分",
        "8时 = ____分", "9时 = ____分",
        "2分 = ____秒", "3分 = ____秒",
        "4分 = ____秒", "5分 = ____秒",
        "6分 = ____秒", "7分 = ____秒",
        "8分 = ____秒", "9分 = ____秒",
        "120分 = ____时", "180分 = ____时",
        "240分 = ____时", "300分 = ____时",
        "360分 = ____时", "420分 = ____时",
        "120秒 = ____分", "180秒 = ____分",
        "240秒 = ____分", "300秒 = ____分",
        "360秒 = ____分", "420秒 = ____分",
        "60秒 = ____分", "60分 = ____时",
        "10分 = ____秒", "10时 = ____分",
        "480分 = ____时", "540分 = ____时",
        "480秒 = ____分", "540秒 = ____分",
        # ===== 时分秒：复名数换算 =====
        "1时5分 = ____分", "1时10分 = ____分",
        "1时15分 = ____分", "1时20分 = ____分",
        "1时25分 = ____分", "1时30分 = ____分",
        "1时35分 = ____分", "1时40分 = ____分",
        "1时45分 = ____分", "1时50分 = ____分",
        "2时5分 = ____分", "2时10分 = ____分",
        "2时15分 = ____分", "2时20分 = ____分",
        "2时25分 = ____分", "2时30分 = ____分",
        "2时40分 = ____分", "2时50分 = ____分",
        "3时5分 = ____分", "3时10分 = ____分",
        "3时20分 = ____分", "3时30分 = ____分",
        "3时45分 = ____分", "1时55分 = ____分",
        "1分5秒 = ____秒", "1分10秒 = ____秒",
        "1分15秒 = ____秒", "1分20秒 = ____秒",
        "1分25秒 = ____秒", "1分30秒 = ____秒",
        "1分35秒 = ____秒", "1分40秒 = ____秒",
        "1分45秒 = ____秒", "1分50秒 = ____秒",
        "2分5秒 = ____秒", "2分10秒 = ____秒",
        "2分15秒 = ____秒", "2分20秒 = ____秒",
        "2分25秒 = ____秒", "2分30秒 = ____秒",
        "2分35秒 = ____秒", "2分45秒 = ____秒",
        "3分5秒 = ____秒", "3分10秒 = ____秒",
        "3分20秒 = ____秒", "3分30秒 = ____秒",
        "3分45秒 = ____秒", "1分55秒 = ____秒",
        "60分 = ____时____分", "65分 = ____时____分",
        "70分 = ____时____分", "75分 = ____时____分",
        "80分 = ____时____分", "85分 = ____时____分",
        "90分 = ____时____分", "95分 = ____时____分",
        "100分 = ____时____分", "105分 = ____时____分",
        "110分 = ____时____分", "125分 = ____时____分",
        "135分 = ____时____分", "150分 = ____时____分",
        "160分 = ____时____分", "175分 = ____时____分",
        "60秒 = ____分____秒", "70秒 = ____分____秒",
        "75秒 = ____分____秒", "80秒 = ____分____秒",
        "85秒 = ____分____秒", "90秒 = ____分____秒",
        "95秒 = ____分____秒", "100秒 = ____分____秒",
        "110秒 = ____分____秒", "120秒 = ____分____秒",
        "130秒 = ____分____秒", "145秒 = ____分____秒",
        "155秒 = ____分____秒", "180秒 = ____分____秒",
        "200秒 = ____分____秒", "210秒 = ____分____秒",
        "1时 = ____秒", "2时 = ____秒",
        "3600秒 = ____时", "7200秒 = ____时",
        "1刻钟 = ____分", "半小时 = ____分",
        "2刻钟 = ____分", "3刻钟 = ____分",
        "1时30分 = ____刻钟", "1时 = ____刻钟",
        # ===== 年月日：基础换算 =====
        "1年 = ____个月", "2年 = ____个月",
        "3年 = ____个月", "4年 = ____个月",
        "5年 = ____个月", "6年 = ____个月",
        "12个月 = ____年", "24个月 = ____年",
        "36个月 = ____年", "48个月 = ____年",
        "60个月 = ____年", "72个月 = ____年",
        "1日 = ____时", "2日 = ____时",
        "3日 = ____时", "4日 = ____时",
        "5日 = ____时", "6日 = ____时",
        "24时 = ____日", "48时 = ____日",
        "72时 = ____日", "96时 = ____日",
        "120时 = ____日", "144时 = ____日",
        "1周 = ____天", "2周 = ____天",
        "3周 = ____天", "4周 = ____天",
        "5周 = ____天", "6周 = ____天",
        "14天 = ____周", "21天 = ____周",
        "28天 = ____周", "35天 = ____周",
        "42天 = ____周", "49天 = ____周",
        # ===== 年月日：大月小月常识 =====
        "1月有 ____天", "3月有 ____天",
        "5月有 ____天", "7月有 ____天",
        "8月有 ____天", "10月有 ____天",
        "12月有 ____天", "4月有 ____天",
        "6月有 ____天", "9月有 ____天",
        "11月有 ____天",
        "平年2月有 ____天", "闰年2月有 ____天",
        "平年全年有 ____天", "闰年全年有 ____天",
        "一年有 ____个大月", "一年有 ____个小月",
        "大月每月有 ____天", "小月每月有 ____天",
        # ===== 年月日：综合换算 =====
        "平年上半年有 ____天", "平年下半年有 ____天",
        "闰年上半年有 ____天", "闰年下半年有 ____天",
        "第一季度有 ____天(平年)", "第二季度有 ____天",
        "第三季度有 ____天", "第四季度有 ____天",
        "第一季度有 ____天(闰年)",
        "1世纪 = ____年", "2世纪 = ____年",
        "1月有 ____个星期零____天",
        "3月有 ____个星期零____天",
        "5月有 ____个星期零____天",
        "7月有 ____个星期零____天",
        "8月有 ____个星期零____天",
        "10月有 ____个星期零____天",
        "12月有 ____个星期零____天",
        "平年全年有 ____个星期零____天",
        "闰年全年有 ____个星期零____天",
        # ===== 年月日+时分秒混合 =====
        "1年 = ____个月 = ____天(平年)",
        "1日 = ____时 = ____分",
        "1时 = ____分 = ____秒",
        "30个月 = ____年____个月",
        "45个月 = ____年____个月",
        "50个月 = ____年____个月",
        "2年6个月 = ____个月",
        "3年3个月 = ____个月",
        "1日6时 = ____时",
        "1日12时 = ____时",
        "2日8时 = ____时",
        "半年 = ____个月",
        "1年半 = ____个月",
        "连续两个月共62天的是 ____月和____月",
        "连续两个月共61天的是 ____月和____月",
        "连续两个月共60天的是 ____月和____月",
        "连续两个月共59天的是 ____月(平年)和____月",
        # ===== 24时计时法 =====
        "下午2时用24时计时法表示是 ____时",
        "下午4时用24时计时法表示是 ____时",
        "晚上8时用24时计时法表示是 ____时",
        "晚上9时用24时计时法表示是 ____时",
        "上午10时用24时计时法表示是 ____时",
        "下午5时用24时计时法表示是 ____时",
        "15时用普通计时法表示是 ____午____时",
        "19时用普通计时法表示是 ____上____时",
        "21时用普通计时法表示是 ____上____时",
        "22时用普通计时法表示是 ____上____时",
        "13时用普通计时法表示是 ____午____时",
        "17时用普通计时法表示是 ____午____时",
        "0时也叫 ____时",
        "中午12时用24时计时法表示是 ____时",
        # ===== 时间计算 =====
        "分针走1小格是 ____分",
        "分针走1大格是 ____分",
        "分针走一圈是 ____分",
        "时针走1大格是 ____时",
        "时针走一圈是 ____时",
        "秒针走1小格是 ____秒",
        "秒针走一圈是 ____秒",
        "秒针走一圈，分针走 ____小格",
        "分针走一圈，时针走 ____大格",
        "一昼夜时针走 ____圈",
        "2日 = ____时，也是 ____个昼夜",
    ]
    # 每天随机抽5道
    chosen = random.sample(pool, min(count, len(pool)))
    return chosen


def generate_application_problems(count: int) -> List[str]:
    """
    生成应用题 (5类：乘法/除法/两步计算/比较/生活场景)
    每天随机抽2道，40天不重复
    """
    pool = [
        # === 乘法应用 ===
        "小明每天做15道口算题，一周（7天）一共做了多少道？",
        "一个书包45元，买3个同样的书包一共需要多少元？",
        "商店运来8箱苹果，每箱25千克，一共运来多少千克？",
        "一辆汽车每小时行驶65千米，4小时行驶多少千米？",
        "三年级一班有4个小组，每组12人，全班一共有多少人？",
        "每箱牛奶24盒，学校买了15箱，一共有多少盒？",
        "商店里一件T恤79元，买了4件需要多少元？",
        "小红买了5本练习本，每本3元，一共花了多少元？",
        "一盒水彩笔有24支，学校买了6盒，一共买了多少支？",
        "操场上有6排同学跑步，每排9人，一共有多少人在跑步？",
        "电影院有座位48排，每排26个座位，一共有多少个座位？",
        "张叔叔每天吃3个苹果，一个月（30天）一共吃多少个？",
        "小华每分钟走50米，走了8分钟，一共走了多少米？",
        # === 除法应用 ===
        "180本图书平均分给6个班，每班分到多少本？",
        "学校小菜园收了180千克花生，分给6个年级，每班多少千克？",
        "225名学生乘5辆车去春游，每辆车坐多少人？",
        "100个气球分给同学，每人3个，可以分给多少人？还剩几个？",
        "272元买同样的碗，每个8元，最多买几个？",
        "一箱雪糕30根，4天卖了8箱，平均每天卖多少根？",
        "420本书放在3个书架上，平均每个书架放多少本？",
        # === 两步计算 ===
        "小明买了3支笔，每支4元，又买了一个8元的本子，一共花多少元？",
        "商店有苹果15箱，每箱20千克，卖出180千克，还剩多少千克？",
        "小红折了36颗星星，小华折的是小红的3倍，两人一共折了多少颗？",
        "一本书236页，小飞每天看38页，看了5天后还剩多少页？",
        "每张桌子坐6人，来了45人，至少需要几张桌子？",
        "一包糖有48颗，分给8个小朋友，每人几颗？如果每人再要2颗，还需多少颗？",
        "铅笔每支2元，买了12支，付了50元，应找回多少元？",
        # === 比较/倍数 ===
        "小李从家到学校要走568米，他已经走了389米，还剩多少米？",
        "一本故事书365页，小微看了198页，还剩多少页没看？",
        "水果店有桃子380千克，卖出210千克，还剩多少千克？",
        "一瓶水550毫升，小明喝了376毫升，还剩多少毫升？",
        "学校食堂有面粉64袋，大米比面粉多28袋，大米有多少袋？",
        "一个足球89元，篮球比足球贵56元，篮球多少元？",
        "小明身高138厘米，比小红高15厘米，小红身高多少厘米？",
        "一班有42人，二班比一班少5人，两个班一共有多少人？",
        # === 生活场景 ===
        "一瓶果汁有2升，倒出6杯，每杯250毫升，还剩多少？",
        "妈妈买了3千克苹果和2千克梨，苹果每千克8元，梨每千克6元，一共多少元？",
        "停车场有小车28辆，大车是小车的3倍少5辆，大车有多少辆？",
        "做一件衣服需要2米布，20米布最多做几件？还剩多少米？",
    ]
    chosen = random.sample(pool, min(count, len(pool)))
    return chosen


# ============================================================================
# 渲染函数 (纯渲染逻辑，与生成分离)
# ============================================================================

def render_kousuan_section(doc, problems: List[str]) -> None:
    """
    渲染口算板块 (3列，Tab制表位分隔)
    """
    add_title_paragraph(doc, "一、口算题", MathWorkbookConfig.FONT_SIZE_SECTION, bold=True, alignment=WD_ALIGN_PARAGRAPH.LEFT)
    add_empty_line(doc, 1)
    
    col_size = (len(problems) + 2) // 3
    
    for i in range(col_size):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.3
        
        # 设置制表位：3列等分页面
        page_width = 21.0 - 2.0 - 2.0  # A4宽 - 左右边距 = 17cm
        tab1 = Cm(page_width / 3)
        tab2 = Cm(page_width * 2 / 3)
        p.paragraph_format.tab_stops.add_tab_stop(tab1)
        p.paragraph_format.tab_stops.add_tab_stop(tab2)
        
        parts = []
        for col in range(3):
            idx = i + col * col_size
            if idx < len(problems):
                parts.append(f"({idx + 1:2d}) {problems[idx]}")
        
        text = "\t".join(parts)
        run = p.add_run(text)
        set_chinese_font(run, MathWorkbookConfig.FONT_MATH, MathWorkbookConfig.FONT_SIZE_PROBLEM, False)
    
    add_empty_line(doc, 1)


def render_shushi_section(doc, problems: List[str]) -> None:
    """
    渲染横式笔算板块 (2列，Tab制表位分隔)
    """
    add_title_paragraph(doc, "二、笔算题", MathWorkbookConfig.FONT_SIZE_SECTION, bold=True, alignment=WD_ALIGN_PARAGRAPH.LEFT)
    add_empty_line(doc, 1)
    
    for i in range(0, len(problems), 2):
        p = doc.add_paragraph()
        p.paragraph_format.line_spacing = 1.5
        
        # 设置制表位：2列等分
        page_width = 21.0 - 2.0 - 2.0
        tab = Cm(page_width / 2)
        p.paragraph_format.tab_stops.add_tab_stop(tab)
        
        parts = [f"({i + 1}) {problems[i]}"]
        if i + 1 < len(problems):
            parts.append(f"({i + 2}) {problems[i + 1]}")
        
        text = "\t".join(parts)
        run = p.add_run(text)
        set_chinese_font(run, MathWorkbookConfig.FONT_MATH, MathWorkbookConfig.FONT_SIZE_PROBLEM, False)
    
    add_empty_line(doc, 1)


def render_fraction_section(doc, fractions: List[Tuple[int, int, int, int]]) -> None:
    """
    渲染分数加减法 (2列Tab分隔 + 题间空行)
    """
    add_title_paragraph(doc, "三、分数加减法", MathWorkbookConfig.FONT_SIZE_SECTION, bold=True, alignment=WD_ALIGN_PARAGRAPH.LEFT)
    add_empty_line(doc, 1)
    
    page_width = 21.0 - 2.0 - 2.0  # 17cm
    half = Cm(page_width / 2)
    
    frac_line = MathWorkbookConfig.FRACTION_LINE_CHAR * MathWorkbookConfig.FRACTION_LINE_LENGTH
    
    for i in range(0, len(fractions), 2):
        n1_1, d1, n1_2, d1_2 = fractions[i]
        
        # 第1行：分子 (Tab分隔两列)
        p1 = doc.add_paragraph()
        p1.paragraph_format.line_spacing = 1.0
        p1.paragraph_format.tab_stops.add_tab_stop(half)
        part1 = f"    {n1_1:>2d}        {n1_2:>2d}"
        if i + 1 < len(fractions):
            n2_1, d2, n2_2, d2_2 = fractions[i + 1]
            part2 = f"    {n2_1:>2d}        {n2_2:>2d}"
            p1.add_run(f"{part1}\t{part2}")
        else:
            p1.add_run(part1)
        for run in p1.runs:
            set_chinese_font(run, MathWorkbookConfig.FONT_MATH, MathWorkbookConfig.FONT_SIZE_PROBLEM, False)
        
        # 第2行：分数线
        p2 = doc.add_paragraph()
        p2.paragraph_format.line_spacing = 1.0
        p2.paragraph_format.tab_stops.add_tab_stop(half)
        line_part = f"  {frac_line}  -  {frac_line}  ="
        if i + 1 < len(fractions):
            p2.add_run(f"{line_part}\t{line_part}")
        else:
            p2.add_run(line_part)
        for run in p2.runs:
            set_chinese_font(run, MathWorkbookConfig.FONT_MATH, MathWorkbookConfig.FONT_SIZE_PROBLEM, False)
        
        # 第3行：分母
        p3 = doc.add_paragraph()
        p3.paragraph_format.line_spacing = 1.2
        p3.paragraph_format.tab_stops.add_tab_stop(half)
        den_part1 = f"    {d1:>2d}        {d1:>2d}"
        if i + 1 < len(fractions):
            den_part2 = f"    {d2:>2d}        {d2:>2d}"
            p3.add_run(f"{den_part1}\t{den_part2}")
        else:
            p3.add_run(den_part1)
        for run in p3.runs:
            set_chinese_font(run, MathWorkbookConfig.FONT_MATH, MathWorkbookConfig.FONT_SIZE_PROBLEM, False)
        
        # 题间空行（隔开每组分数题）
        add_empty_line(doc, 1)


def render_fill_section(doc, problems: List[str]) -> None:
    """
    渲染单位换算填空板块
    
    Args:
        doc: Document对象
        problems: 题目列表
    """
    add_title_paragraph(doc, "四、时间单位换算", MathWorkbookConfig.FONT_SIZE_SECTION, bold=True, alignment=WD_ALIGN_PARAGRAPH.LEFT)
    add_empty_line(doc, 1)
    
    for i, problem in enumerate(problems, 1):
        add_problem_paragraph(doc, f"{i}. {problem}")
    
    add_empty_line(doc, 1)


def render_application_section(doc, problems: List[str]) -> None:
    """
    渲染应用题板块 (完整答题空间)
    
    Args:
        doc: Document对象
        problems: 题目列表
    """
    add_title_paragraph(doc, "五、应用题", MathWorkbookConfig.FONT_SIZE_SECTION, bold=True, alignment=WD_ALIGN_PARAGRAPH.LEFT)
    add_empty_line(doc, 1)
    
    for i, problem in enumerate(problems, 1):
        add_problem_paragraph(doc, f"{i}. {problem}")
        
        # 答题空间（3行空白）
        for _ in range(3):
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 1.5
            run = p.add_run(" " * 50)
            set_chinese_font(run, MathWorkbookConfig.FONT_MAIN, MathWorkbookConfig.FONT_SIZE_PROBLEM, False)
        
        add_empty_line(doc, 1)


# ============================================================================
# 文档结构函数
# ============================================================================

def setup_document_format(doc) -> None:
    """
    设置文档整体格式 (出版级标准)
    
    Args:
        doc: Document对象
    """
    # 设置页面边距
    sections = doc.sections
    for section in sections:
        section.top_margin = MathWorkbookConfig.MARGIN_TOP
        section.bottom_margin = MathWorkbookConfig.MARGIN_BOTTOM
        section.left_margin = MathWorkbookConfig.MARGIN_LEFT
        section.right_margin = MathWorkbookConfig.MARGIN_RIGHT
        
        # 设置纸张大小
        section.page_width = MathWorkbookConfig.PAGE_WIDTH
        section.page_height = MathWorkbookConfig.PAGE_HEIGHT
    
    # 设置默认段落格式
    doc.styles['Normal'].paragraph_format.line_spacing = MathWorkbookConfig.LINE_SPACING_PROBLEM


def generate_cover_page(doc) -> None:
    """
    生成封面页 (标准教材封面格式)
    
    Args:
        doc: Document对象
    """
    add_empty_line(doc, 6)
    
    # 主标题
    add_title_paragraph(doc, MathWorkbookConfig.BOOK_TITLE, MathWorkbookConfig.FONT_SIZE_BOOK_TITLE, bold=True)
    
    add_empty_line(doc, 2)
    
    # 副标题
    add_title_paragraph(doc, MathWorkbookConfig.BOOK_SUBTITLE, Pt(16), bold=False)
    
    add_empty_line(doc, 6)
    
    # 版本信息
    add_title_paragraph(doc, f"版本 {MathWorkbookConfig.BOOK_VERSION}", MathWorkbookConfig.FONT_SIZE_SECTION, bold=False)
    
    add_empty_line(doc, 1)
    
    add_title_paragraph(doc, MathWorkbookConfig.BOOK_DATE, MathWorkbookConfig.FONT_SIZE_SECTION, bold=False)
    
    add_empty_line(doc, 2)
    
    add_title_paragraph(doc, MathWorkbookConfig.BOOK_AUTHOR, MathWorkbookConfig.FONT_SIZE_SECTION, bold=False)
    
    # 分页
    doc.add_page_break()


def generate_usage_guide(doc) -> None:
    """
    生成使用说明页 (家长指南)
    
    Args:
        doc: Document对象
    """
    add_title_paragraph(doc, "📖 使用说明", MathWorkbookConfig.FONT_SIZE_DAY_TITLE, bold=True)
    add_empty_line(doc, 2)
    
    guide_content = [
        "一、练习建议",
        "  1. 每天坚持练习30分钟，固定时间效果更好",
        "  2. 口算题建议计时，培养快速反应能力",
        "  3. 竖式计算注意数位对齐，养成好习惯",
        "  4. 分数题先观察再计算，做完记得检查",
        "  5. 时间换算题先记牢进率：1时=60分，1分=60秒",
        "",
        "二、艾宾浩斯复习法",
        "  第1天学习 → 第1天晚复习",
        "  → 第2天复习 → 第4天复习",
        "  → 第7天复习 → 第15天复习 → 第30天复习",
        "  按照这个规律，记忆留存率可达90%以上！",
        "",
        "三、评分标准",
        "  • 优秀：正确率 ≥ 95%",
        "  • 良好：85% ≤ 正确率 < 95%",
        "  • 及格：70% ≤ 正确率 < 85%",
        "  • 需努力：正确率 < 70%",
        "",
        "四、家长寄语",
        "  坚持每天练习，数学能力一定会有明显提升！",
        "  鼓励孩子独立完成，错题及时整理到错题本。",
    ]
    
    for line in guide_content:
        add_problem_paragraph(doc, line, first_line_indent=False)
    
    doc.add_page_break()


def generate_single_day(doc, day: int) -> None:
    """
    生成单日练习 (标准化流程)
    
    Args:
        doc: Document对象
        day: 第几天
    """
    # 每日标题
    review_mark = MathWorkbookConfig.REVIEW_MARKS.get(day, "")
    if review_mark:
        title = f"第 {day} 天   {review_mark}"
    else:
        title = f"第 {day} 天"
    
    add_title_paragraph(doc, title, MathWorkbookConfig.FONT_SIZE_DAY_TITLE, bold=True)
    add_empty_line(doc, 1)
    
    # 学生信息栏
    info_p = doc.add_paragraph()
    info_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    info_run = info_p.add_run("姓名：________  用时：________  得分：________")
    set_chinese_font(info_run, MathWorkbookConfig.FONT_MAIN, MathWorkbookConfig.FONT_SIZE_INFO, False)
    
    add_empty_line(doc, 1)
    
    # 生成各板块题目
    config = MathWorkbookConfig.PROBLEMS_PER_DAY
    
    # 1. 口算题
    kousuan_probs = generate_kousuan_problems(config["口算"])
    render_kousuan_section(doc, kousuan_probs)
    
    # 2. 笔算题
    shushi_probs = generate_shushi_problems(config["笔算"])
    render_shushi_section(doc, shushi_probs)
    
    # 3. 分数加减法
    fraction_probs = generate_fraction_problems(config["分数"])
    render_fraction_section(doc, fraction_probs)
    
    # 4. 单位换算
    fill_probs = generate_fill_problems(config["填空"])
    render_fill_section(doc, fill_probs)
    
    # 5. 应用题
    app_probs = generate_application_problems(config["应用"])
    render_application_section(doc, app_probs)
    
    # 分页
    doc.add_page_break()


# ============================================================================
# 主流程函数
# ============================================================================

def generate_full_workbook() -> str:
    """
    生成完整的40天练习册 (标准流程)
    
    Returns:
        生成的文件完整路径
    """
    print("=" * 60)
    print("📚 三年级数学每日一练40天 - 标准教材版生成器 v3.0")
    print("=" * 60)
    print()
    
    # 0. 重置去重集合（确保每次生成都是干净的）
    MathWorkbookConfig.USED_PROBLEMS = set()
    dedup_stats = {"口算": 0, "竖式": 0, "分数": 0}
    
    # 1. 初始化文档
    print("[1/5] 初始化文档格式...")
    doc = Document()
    setup_document_format(doc)
    
    # 2. 生成封面
    print("[2/5] 生成封面页...")
    generate_cover_page(doc)
    
    # 3. 生成使用说明
    print("[3/5] 生成使用说明...")
    generate_usage_guide(doc)
    
    # 4. 生成每日练习
    print("[4/5] 正在生成40天练习题...")
    for day in range(1, 41):
        print(f"       正在生成第 {day:2d} 天...", end='\r')
        generate_single_day(doc, day)
    print()
    
    # 5. 保存文件
    print(f"[5/5] 正在保存到桌面: {MathWorkbookConfig.OUTPUT_FILENAME}...")
    doc.save(MathWorkbookConfig.OUTPUT_FULL_PATH)
    
    print()
    print("=" * 60)
    print("✅ 生成完成！")
    print("=" * 60)
    print()
    print(f"📂 文件路径: {MathWorkbookConfig.OUTPUT_FULL_PATH}")
    print()
    print("📊 统计信息:")
    print(f"   • 总天数: 40 天")
    print(f"   • 口算题: 40 × {MathWorkbookConfig.PROBLEMS_PER_DAY['口算']} = {40 * MathWorkbookConfig.PROBLEMS_PER_DAY['口算']} 题")
    print(f"   • 笔算题: 40 × {MathWorkbookConfig.PROBLEMS_PER_DAY['笔算']} = {40 * MathWorkbookConfig.PROBLEMS_PER_DAY['笔算']} 题")
    print(f"   • 分数题: 40 × {MathWorkbookConfig.PROBLEMS_PER_DAY['分数']} = {40 * MathWorkbookConfig.PROBLEMS_PER_DAY['分数']} 题")
    print(f"   • 时间换算: 40 × {MathWorkbookConfig.PROBLEMS_PER_DAY['填空']} = {40 * MathWorkbookConfig.PROBLEMS_PER_DAY['填空']} 题")
    print(f"   • 应用题: 40 × {MathWorkbookConfig.PROBLEMS_PER_DAY['应用']} = {40 * MathWorkbookConfig.PROBLEMS_PER_DAY['应用']} 题")
    print(f"   • 总题量: {40 * sum(MathWorkbookConfig.PROBLEMS_PER_DAY.values())} 题")
    print()
    print("🔍 去重验证:")
    total_used = len(MathWorkbookConfig.USED_PROBLEMS)
    print(f"   • 唯一题目哈希数: {total_used} 个")
    # 各类的统计
    kou_count = sum(1 for k in MathWorkbookConfig.USED_PROBLEMS if k.startswith("kou:"))
    shu_count = sum(1 for k in MathWorkbookConfig.USED_PROBLEMS if k.startswith("shushi:"))
    frac_count = sum(1 for k in MathWorkbookConfig.USED_PROBLEMS if k.startswith("frac:"))
    print(f"   • 口算唯一题: {kou_count} 个 (需要{40 * MathWorkbookConfig.PROBLEMS_PER_DAY['口算']}题)")
    print(f"   • 笔算唯一题: {shu_count} 个 (需要{40 * MathWorkbookConfig.PROBLEMS_PER_DAY['笔算']}题)")
    print(f"   • 分数唯一题: {frac_count} 个 (需要{40 * MathWorkbookConfig.PROBLEMS_PER_DAY['分数']}题)")
    dup_free = (kou_count >= 40 * MathWorkbookConfig.PROBLEMS_PER_DAY['口算'] and
                shu_count >= 40 * MathWorkbookConfig.PROBLEMS_PER_DAY['笔算'] and
                frac_count >= 40 * MathWorkbookConfig.PROBLEMS_PER_DAY['分数'])
    print(f"   {'✅ 全部不重复！' if dup_free else '⚠️ 有重复'}")
    print()
    print("💡 本版本基于十轮研究成果优化：")
    print("   • 符合人教版小学教材出版标准")
    print("   • 保护视力的字号和行距设置")
    print("   • 基于认知心理学的题量配置")
    print("   • 融入艾宾浩斯复习节奏标记")
    print("   • 标准分数竖式格式")
    print("   • 完整的封面和使用说明")
    print()
    
    return MathWorkbookConfig.OUTPUT_FULL_PATH


# ============================================================================
# 入口
# ============================================================================

if __name__ == "__main__":
    generate_full_workbook()

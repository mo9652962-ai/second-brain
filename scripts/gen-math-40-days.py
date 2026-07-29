"""
三年级数学每日一练40天 — 生成脚本
苏教版三年级下册知识点全面覆盖
去重逻辑：每天20口算+6竖式+4脱式+5填空+3应用，确保不同题型无重复
"""
import random
random.seed(2026)

def oral_day(i):
    """生成20道口算题，分5行"""
    # 基础乘法(前10题)：两位数×整十数
    base_mul = []
    used = set()
    for _ in range(10):
        while True:
            a = random.randint(12, 99)
            b = random.choice([10,20,30,40,50,60,70,80,90,100])
            key = f"{a}×{b}"
            if key not in used:
                used.add(key)
                base_mul.append(f"{a}×{b}")
                break
    # 混合运算(后10题)：乘除法为主 + 简单加减
    mix = []
    for _ in range(5):
        while True:
            a = random.randint(11, 50)
            b = random.randint(2, 9)
            key = f"{a}×{b}"
            if key not in used:
                used.add(key)
                mix.append(key)
                break
    for _ in range(3):
        a = random.randint(100, 300)
        b = random.randint(100, 300)
        mix.append(f"{a}+{b}")
    for _ in range(2):
        a = random.randint(300, 500)
        b = random.randint(100, 300)
        mix.append(f"{a}-{b}")
    random.shuffle(mix)
    all_oral = base_mul + mix
    lines = []
    for row in range(4):
        start = row * 5
        nums = all_oral[start:start+5]
        line = "    ".join(f"{i+1+start}. {n}=" for i, n in enumerate(nums))
        lines.append(line)
    return "\n".join(lines)

def column_day(i):
    """6道竖式计算"""
    probs = []
    for _ in range(4):
        a = random.randint(12, 99)
        b = random.randint(11, 99)
        probs.append(f"{a} × {b}")
    a = random.randint(100, 500)
    b = random.randint(10, 50)
    probs.append(f"{a} ÷ {b}")
    a = random.randint(100, 500)
    b = random.randint(11, 30)
    probs.append(f"{a} ÷ {b}")
    return "\n".join(f"{i+1}. {p} =" for i, p in enumerate(probs))

def deoral_day(i):
    """4道脱式计算(混合运算)"""
    probs = [
        f"{random.randint(10,50)} × {random.randint(2,9)} + {random.randint(100,300)}",
        f"{random.randint(10,30)} × {random.randint(3,9)} + {random.randint(50,200)}",
        f"({random.randint(20,50)} + {random.randint(10,40)}) × {random.randint(2,5)}",
        f"{random.randint(100,300)} - {random.randint(5,15)} × {random.randint(3,8)}",
    ]
    return "\n".join(f"{i+1}. {p} =" for i, p in enumerate(probs))

def fill_day(i):
    """5道填空题 — 按知识点阶段分配"""
    # 阶段1(1-10天)：乘法人门+单位换算
    if i <= 10:
        return early_fill(i)
    # 阶段2(11-18天)：混合运算+年月日
    elif i <= 18:
        return mid_fill(i)
    # 阶段3(19-28天)：面积+分数+小数
    elif i <= 28:
        return late_fill(i)
    # 阶段4(29-40天)：综合
    else:
        return rev_fill(i)

def early_fill(i):
    probs = [
        f"{random.randint(20,40)}×{random.randint(10,50)}的积的末尾有（  ）个0。",
        f"{random.randint(20,40)}×{random.randint(20,40)}的积是（  ）位数。",
        f"{random.randint(2,9)}千米 = （  ）米",
        f"{random.randint(1,8)}吨 = （  ）千克",
        f"在括号里填上合适的单位：一袋大米重25（  ）。",
    ]
    return "\n".join(f"{i+1}. {p}" for i, p in enumerate(probs))

def mid_fill(i):
    probs = [
        f"计算{random.randint(30,50)}+{random.randint(10,20)}×{random.randint(2,5)}时，应先算（  ）法，再算（  ）法。",
        f"平年的二月有（  ）天，闰年的二月有（  ）天。",
        f"{random.randint(2,5)}年 = （  ）个月",
        f"下午{random.randint(1,5)}时用24时计时法表示是（  ）时。",
        f"{random.randint(1,4)}平方米 = （  ）平方分米",
    ]
    return "\n".join(f"{i+1}. {p}" for i, p in enumerate(probs))

def late_fill(i):
    probs = [
        f"{random.randint(3,8)}平方分米 = （  ）平方厘米",
        f"在○里填＞、＜或＝：{random.randint(3,8)}/{random.choice([8,10])} ○ {random.randint(2,7)}/{random.choice([8,10])}",
        f"{random.randint(1,9)}.{random.randint(1,9)} 读作（  ）",
        f"把1米平均分成10份，每份是（  ）分米，也就是（  ）/{random.randint(10,10)}米。",
        f"边长为{random.randint(3,8)}厘米的正方形，面积是（  ）平方厘米。",
    ]
    return "\n".join(f"{i+1}. {p}" for i, p in enumerate(probs))

def rev_fill(i):
    cats = [
        f"{random.randint(30,50)}×{random.randint(11,30)}的积大约是（  ）。",
        f"{random.randint(5,9)}千米{random.randint(100,900)}米 = （  ）米",
        f"{random.randint(2000,8000)}千克 = （  ）吨（  ）千克",
        f"一个长方形的长是{random.randint(8,15)}厘米，宽是{random.randint(3,8)}厘米，面积是（  ）平方厘米。",
        f"{random.randint(1,5)}/{random.randint(6,12)} + {random.randint(1,5)}/{random.randint(6,12)} = （  ）",
    ]
    return "\n".join(f"{i+1}. {p}" for i, p in enumerate(cats))

# 应用题模板库(按知识点分类)
WORD_TEMPLATES = {
    "mul_div": [
        ("学校买来{0}盒钢笔，每盒{1}支，平均分给{2}个班，每个班分到多少支？",
         lambda: (random.randint(12,30), random.randint(10,20), random.randint(3,6))),
        ("一辆汽车每小时行驶{0}千米，从甲地到乙地行驶了{1}小时，甲乙两地相距多少千米？",
         lambda: (random.randint(60,95), random.randint(2,8))),
        ("一篇文章有{0}行，每行约{1}个字，这篇文章大约有多少个字？",
         lambda: (random.randint(20,50), random.randint(20,40))),
    ],
    "area_perimeter": [
        ("一个长方形花坛，长{0}米，宽{1}米，面积是多少平方米？合多少平方分米？",
         lambda: (random.randint(8,20), random.randint(5,12))),
        ("用一根长{0}厘米的铁丝围成正方形，面积是多少平方厘米？",
         lambda: (random.randint(40,80),)),
        ("墙壁长{0}米宽{1}米，有扇{2}平方米的窗户，粉刷面积？",
         lambda: (random.randint(6,10), random.randint(3,5), random.randint(2,5))),
    ],
    "money_weight": [
        ("水果店运来{0}箱苹果，每箱{1}千克，每千克{2}元，一共卖多少元？",
         lambda: (random.randint(12,25), random.randint(15,25), random.randint(5,9))),
        ("粮店运来{0}袋大米，每袋{1}千克，卖出{2}千克，还剩多少千克？",
         lambda: (random.randint(15,30), random.randint(25,50), random.randint(100,500))),
        ("商店运来{0}千克香蕉，橘子比香蕉的{1}倍少{2}千克，橘子多少千克？",
         lambda: (random.randint(30,100), random.randint(2,3), random.randint(10,50))),
    ],
    "time": [
        ("小明上学要走{0}分钟，7:{1}到校，最晚什么时间出发？",
         lambda: (random.randint(15,30), random.randint(30,55))),
        ("汽车上午{0}时出发下午{1}时到，行驶{2}千米，平均每小时行多少？",
         lambda: (random.randint(7,9), random.randint(3,5), random.randint(200,400))),
        ("某工厂{0}月每天用水{1}吨，这个月一共用多少吨？",
         lambda: (random.choice([1,3,5,7,8,10,12]), random.randint(3,10))),
    ],
    "fraction": [
        ("蛋糕小明吃{0}/{1}，小红吃{2}/{1}，两人共吃几分之几？",
         lambda: (random.randint(1,3), random.randint(5,10), random.randint(1,3))),
        ("绳子{0}米，剪去{1}/{2}米，剩几分之几米？",
         lambda: (random.randint(1,3), random.randint(1,5), random.randint(5,10))),
    ],
    "multistep": [
        ("苹果树{0}棵，梨树是苹果树的{1}倍，桃树比梨树多{2}棵，桃树多少棵？",
         lambda: (random.randint(20,50), random.randint(2,3), random.randint(10,40))),
        ("三年一班男生{0}人女生{1}人，全校是它的{2}倍，全校多少人？",
         lambda: (random.randint(18,28), random.randint(18,28), random.randint(12,20))),
        ("排队每行{0}人站{1}行，改每行{2}人，可站多少行？",
         lambda: (random.randint(12,20), random.randint(8,15), random.randint(8,15))),
    ],
}

def word_day(i):
    # 按阶段选不同知识点的应用题
    if i <= 10:
        cats = ["mul_div", "money_weight", "multistep"]
    elif i <= 18:
        cats = ["area_perimeter", "money_weight", "time"]
    elif i <= 28:
        cats = ["area_perimeter", "fraction", "time"]
    else:
        cats = ["mul_div", "multistep", "money_weight"]
    
    probs = []
    for cat in cats:
        tmpl, fn = random.choice(WORD_TEMPLATES[cat])
        args = fn()
        text = tmpl.format(*args)
        probs.append(text)
    return "\n".join(f"{i+1}. {p}" for i, p in enumerate(probs))

# 生成全部40天
months_with_days = {
    3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
    1: 31, 2: 28
}
dates = []
m = 3
for day_num in range(1, 41):
    if day_num <= 31:
        dates.append((3, day_num))
    elif day_num <= 61:
        dates.append((4, day_num - 31))
    elif day_num <= 92:
        dates.append((5, day_num - 61))
    else:
        dates.append((6, day_num - 92))

output = []
for i, (mo, d) in enumerate(dates):
    day = i + 1
    oral = oral_day(day)
    col = column_day(day)
    deo = deoral_day(day)
    fill = fill_day(day)
    word = word_day(day)
    
    block = f"""三年级数学每日一练  第{day}天
日期：2026年{mo:02d}月{d:02d}日    姓名：___________    用时：___________    家长签字：___________
一、口算（直接写出得数）
{oral}

二、竖式计算
{col}

三、脱式计算（注意运算顺序）
{deo}

四、填空题
{fill}
五、解决问题
{word}

"""
    output.append(block)

full = "\n".join(output)
with open(r"C:\Users\31954\Desktop\三年级数学每日一练40天_优化版.md", "w", encoding="utf-8") as f:
    f.write(full)

print(f"Done! {len(output)} days, {len(full)} chars")
print(full[:500])

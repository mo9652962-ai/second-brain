# -*- coding: utf-8 -*-
"""
艾宾浩斯遗忘曲线复习计划生成器
基于艾宾浩斯记忆规律：
    第1天学习 → 第1天复习（12小时后）
    → 第2天复习 → 第4天复习 → 第7天复习
    → 第15天复习 → 第30天复习
"""
import os
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class ReviewDay:
    """单日复习计划"""
    day: int                  # 第几天
    date: str                 # 日期字符串
    topics: List[str]         # 复习主题
    problem_count: int        # 复习题目数量
    difficulty: str           # 难度级别
    is_review: bool = True    # 是否为复习日（第一天为学习日）


@dataclass
class EbbinghausPlan:
    """完整的艾宾浩斯复习计划"""
    start_date: str                   # 开始日期
    total_days: int = 30             # 总计划天数
    learning_days: List[int] = field(default_factory=list)  # 学习日
    review_intervals: List[int] = field(default_factory=lambda: [1, 2, 4, 7, 15, 30])  # 复习间隔
    schedule: List[ReviewDay] = field(default_factory=list)  # 详细日程

    def get_review_days_for_learning_day(self, learning_day: int) -> List[int]:
        """计算某个学习日对应的复习日"""
        return [learning_day + interval for interval in self.review_intervals]


class EbbinghausGenerator:
    """艾宾浩斯复习计划生成器"""

    # 标准复习间隔（从学习日开始计算天数）
    STANDARD_INTERVALS = [1, 2, 4, 7, 15, 30]

    # 难度随复习次数递减
    DIFFICULTY_PROGRESSION = ['基础', '巩固', '强化', '进阶', '挑战', ' mastery']

    # 各类型题目复习优先级
    TOPIC_PRIORITY = {
        '两位数乘法口算': 3,    # 高频复习
        '两位数乘两位数笔算': 2,
        '分数加减运算': 4,        # 分数最难，优先复习
        '单位换算填空': 2,
        '应用题': 5,              # 应用题最重要
    }

    def __init__(self, start_date: Optional[str] = None, total_days: int = 30):
        """
        初始化复习计划生成器

        Args:
            start_date: 开始日期，格式 'YYYY-MM-DD'，默认今天
            total_days: 总计划天数，默认30天
        """
        self.start_date = start_date or datetime.now().strftime('%Y-%m-%d')
        self.total_days = total_days
        self.plan = EbbinghausPlan(
            start_date=self.start_date,
            total_days=total_days
        )

    def _add_days(self, date_str: str, days: int) -> str:
        """日期加减"""
        date = datetime.strptime(date_str, '%Y-%m-%d')
        new_date = date + timedelta(days=days)
        return new_date.strftime('%Y-%m-%d')

    def generate_learning_topics(self, day: int) -> List[str]:
        """生成某天的学习主题"""
        all_topics = [
            '两位数乘法口算',
            '两位数乘两位数笔算',
            '分数加减运算',
            '单位换算填空',
            '应用题'
        ]

        # 每天学习2-3个主题，循环轮换
        idx = (day - 1) % len(all_topics)
        topics = [all_topics[idx]]

        # 第二天开始加入之前的主题
        if day > 1:
            topics.append(all_topics[(idx + 1) % len(all_topics)])

        return topics

    def generate_review_topics(self, day: int) -> Tuple[List[str], int]:
        """
        生成某天的复习主题
        根据艾宾浩斯曲线，第N天需要复习之前特定天数学习的内容
        """
        review_topics = []
        total_problems = 0

        # 检查每个复习间隔点
        for interval in self.STANDARD_INTERVALS:
            learning_day = day - interval
            if learning_day > 0 and learning_day <= self.total_days:
                # 这一天应该复习第learning_day学的内容
                topics = self.generate_learning_topics(learning_day)
                for topic in topics:
                    if topic not in review_topics:
                        review_topics.append(topic)
                        total_problems += self.TOPIC_PRIORITY.get(topic, 2) * 2

        # 如果是纯复习日，至少保证一定题量
        if not review_topics:
            # 取之前学习过的所有主题
            for i in range(1, min(day, 6)):
                topics = self.generate_learning_topics(i)
                for topic in topics[:1]:
                    if topic not in review_topics:
                        review_topics.append(topic)
                        total_problems += 5

        return review_topics, max(10, total_problems)

    def get_difficulty_level(self, day: int) -> str:
        """根据天数获取难度级别"""
        if day <= 7:
            return '基础'
        elif day <= 15:
            return '巩固'
        elif day <= 22:
            return '强化'
        elif day <= 30:
            return '进阶'
        else:
            return '挑战'

    def generate_full_schedule(self) -> EbbinghausPlan:
        """生成完整的30天复习计划"""
        schedule = []

        for day in range(1, self.total_days + 1):
            current_date = self._add_days(self.start_date, day - 1)

            # 判断是学习日还是复习日
            # 第1,3,5,8,12,19,26天为主要学习日
            learning_days = [1, 3, 5, 8, 12, 19, 26]
            is_learning_day = day in learning_days

            if is_learning_day:
                # 学习日：学习新内容 + 复习旧内容
                learning_topics = self.generate_learning_topics(day)
                review_topics, problem_count = self.generate_review_topics(day)
                all_topics = learning_topics + [t for t in review_topics if t not in learning_topics]
                difficulty = self.get_difficulty_level(day)
                problem_count = max(20, problem_count + 10)  # 学习日题量更多
            else:
                # 复习日：只复习
                review_topics, problem_count = self.generate_review_topics(day)
                all_topics = review_topics
                difficulty = self.get_difficulty_level(day)

            schedule.append(ReviewDay(
                day=day,
                date=current_date,
                topics=all_topics,
                problem_count=problem_count,
                difficulty=difficulty,
                is_review=not is_learning_day
            ))

        self.plan.schedule = schedule
        self.plan.learning_days = learning_days
        return self.plan

    def generate_day_problems(self, day: int, problem_count: int = 20) -> Dict:
        """
        生成某天的具体复习题目
        根据遗忘规律，重点复习之前学过的易错题
        """
        # 根据天数决定复习重点
        if day <= 7:
            # 前期：侧重基础口算
            kou_ratio = 0.5
            shu_ratio = 0.3
            frac_ratio = 0.2
        elif day <= 15:
            # 中期：侧重竖式计算
            kou_ratio = 0.3
            shu_ratio = 0.4
            frac_ratio = 0.3
        else:
            # 后期：侧重分数和应用题
            kou_ratio = 0.2
            shu_ratio = 0.3
            frac_ratio = 0.5

        return {
            'day': day,
            'date': self._add_days(self.start_date, day - 1),
            'problem_distribution': {
                '口算': int(problem_count * kou_ratio),
                '竖式': int(problem_count * shu_ratio),
                '分数': int(problem_count * frac_ratio),
                '填空': max(3, int(problem_count * 0.1)),
            },
            'difficulty': self.get_difficulty_level(day),
            'memory_strength': self._calculate_memory_strength(day)
        }

    def _calculate_memory_strength(self, day: int) -> float:
        """
        计算记忆留存率（基于艾宾浩斯曲线）
        t天后的记忆留存率：R = 100 * e^(-t/S)
        S为记忆强度系数，取S=2
        """
        import math
        retention = 100 * math.exp(-day / 2)
        return max(10, min(100, retention))

    def generate_plan_summary(self) -> Dict:
        """生成计划摘要"""
        if not self.plan.schedule:
            self.generate_full_schedule()

        learning_days = [d for d in self.plan.schedule if not d.is_review]
        review_only_days = [d for d in self.plan.schedule if d.is_review and d.topics]

        total_problems = sum(d.problem_count for d in self.plan.schedule)

        return {
            'start_date': self.start_date,
            'end_date': self._add_days(self.start_date, self.total_days - 1),
            'total_days': self.total_days,
            'learning_days_count': len(learning_days),
            'review_days_count': len(review_only_days),
            'total_problems': total_problems,
            'avg_problems_per_day': round(total_problems / self.total_days, 1),
            'review_intervals': self.STANDARD_INTERVALS,
            'schedule_preview': [
                {
                    'day': d.day,
                    'date': d.date,
                    'topics': d.topics[:2],
                    'problems': d.problem_count,
                    'type': '📖 学习日' if not d.is_review else '🔄 复习日'
                }
                for d in self.plan.schedule[:7]  # 前7天预览
            ]
        }

    def export_plan_to_text(self, filepath: str) -> None:
        """导出复习计划为文本文件"""
        if not self.plan.schedule:
            self.generate_full_schedule()

        summary = self.generate_plan_summary()

        content = []
        content.append('=' * 70)
        content.append('                📚 艾宾浩斯记忆法 - 数学复习计划')
        content.append('=' * 70)
        content.append('')
        content.append(f'📅 开始日期: {summary["start_date"]}')
        content.append(f'📅 结束日期: {summary["end_date"]}')
        content.append(f'📊 总计划天数: {summary["total_days"]} 天')
        content.append(f'📖 学习日: {summary["learning_days_count"]} 天')
        content.append(f'🔄 复习日: {summary["review_days_count"]} 天')
        content.append(f'📝 总题量: {summary["total_problems"]} 题')
        content.append(f'📈 日均题量: {summary["avg_problems_per_day"]} 题')
        content.append('')
        content.append('💡 复习规律: 第1天学习 → 第1/2/4/7/15/30天复习')
        content.append('=' * 70)
        content.append('')
        content.append('📋 详细日程:')
        content.append('-' * 70)

        for day_info in self.plan.schedule:
            type_mark = '📖' if not day_info.is_review else '🔄'
            topics_str = '、'.join(day_info.topics[:3])
            if len(day_info.topics) > 3:
                topics_str += '...'

            content.append(
                f'  第{day_info.day:2d}天 [{day_info.date}] {type_mark} '
                f'【{day_info.difficulty}】{day_info.problem_count:3d}题 - {topics_str}'
            )

        content.append('')
        content.append('=' * 70)
        content.append('💡 使用说明:')
        content.append('  1. 严格按照日期完成每日题量，切勿贪多求快')
        content.append('  2. 每做完一天的题目，用AI批改功能检查正确率')
        content.append('  3. 错题记录下来，第二天重点复习')
        content.append('  4. 第7、15、30天进行综合测试，检验学习效果')
        content.append('  5. 坚持完成整个周期，数学计算能力将显著提升！')
        content.append('=' * 70)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

        print(f'✅ 复习计划已导出: {filepath}')


# ============================================
# 便捷使用函数
# ============================================
def generate_ebbinghaus_plan(
    start_date: Optional[str] = None,
    total_days: int = 30,
    export_path: Optional[str] = None
) -> EbbinghausPlan:
    """
    便捷生成艾宾浩斯复习计划

    Args:
        start_date: 开始日期，默认今天
        total_days: 总天数，默认30天
        export_path: 导出文件路径，如果提供则导出

    Returns:
        EbbinghausPlan 对象

    示例:
        >>> plan = generate_ebbinghaus_plan(total_days=30, export_path='复习计划.txt')
        >>> print(plan.schedule[0])  # 查看第一天计划
    """
    generator = EbbinghausGenerator(start_date=start_date, total_days=total_days)
    plan = generator.generate_full_schedule()

    if export_path:
        generator.export_plan_to_text(export_path)

    return plan


def get_day_recommendation(day: int) -> Dict:
    """获取某天的复习建议"""
    generator = EbbinghausGenerator()
    plan = generator.generate_day_problems(day)

    # 根据记忆留存率给出建议
    retention = plan['memory_strength']
    if retention >= 80:
        suggestion = '✅ 记忆牢固，可加快进度'
    elif retention >= 50:
        suggestion = '⚠️  需加强复习，建议多做5题'
    else:
        suggestion = '❌ 记忆模糊，建议重新学习该知识点'

    return {
        **plan,
        'suggestion': suggestion,
        'recommended_extra_problems': 0 if retention >= 80 else 5 if retention >= 50 else 10
    }


# ============================================
# 测试代码
# ============================================
if __name__ == '__main__':
    print('=' * 60)
    print('🧪 艾宾浩斯复习计划生成器 - 测试')
    print('=' * 60)
    print()

    # 生成30天计划
    plan = generate_ebbinghaus_plan(
        start_date=datetime.now().strftime('%Y-%m-%d'),
        total_days=30,
        export_path='数学复习计划_艾宾浩斯.txt'
    )

    # 打印摘要
    generator = EbbinghausGenerator()
    summary = generator.generate_plan_summary()

    print('📊 计划摘要:')
    print(f'  日期范围: {summary["start_date"]} → {summary["end_date"]}')
    print(f'  总天数: {summary["total_days"]} 天')
    print(f'  学习日: {summary["learning_days_count"]} 天')
    print(f'  复习日: {summary["review_days_count"]} 天')
    print(f'  总题量: {summary["total_problems"]} 题')
    print(f'  日均题量: {summary["avg_problems_per_day"]} 题')
    print()
    print('📅 前7天预览:')
    for day in summary['schedule_preview']:
        print(f'  第{day["day"]:2d}天 [{day["date"]}] {day["type"]} '
              f'【{day["problems"]:3d}题】 {"、".join(day["topics"])}')

    print()
    print('=' * 60)
    print('✅ 计划生成完成！')
    print('=' * 60)

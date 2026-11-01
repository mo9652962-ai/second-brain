# -*- coding: utf-8 -*-
"""
PDF答案生成器
为数学练习册生成配套的标准答案PDF
支持：题目答案、详细解析、难度标注、错题分析
"""
import os
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProblemAnswer:
    """单题答案数据结构"""
    problem_id: int          # 题目编号
    problem_text: str        # 题目内容
    answer: str              # 标准答案
    solution: str            # 解题步骤/解析
    difficulty: str          # 难度: 简单/中等/困难
    category: str            # 题型分类: 口算/竖式/分数/填空/应用


class PDFAnswerGenerator:
    """练习册答案PDF生成器"""

    def __init__(self, title: str = "三年级数学每日一练 参考答案"):
        self.title = title
        self.answers: Dict[int, List[ProblemAnswer]] = {}  # key=天数

    def add_day_answers(self, day: int, answers: List[ProblemAnswer]) -> None:
        """添加某天的答案"""
        self.answers[day] = answers

    def generate_kousuan_answer(self, expr: str) -> Tuple[str, str]:
        """
        生成口算题答案和解析
        支持: a + b, a - b, a × b, a ÷ b
        安全实现：不使用eval，手动解析和计算
        """
        try:
            # 清理表达式
            expr_clean = expr.replace('×', '*').replace('÷', '/').replace('=', '').strip()

            # 手动解析运算符（安全替代eval）
            if '+' in expr_clean:
                a, b = map(int, expr_clean.split('+'))
                result = a + b
                op = '+'
            elif '-' in expr_clean:
                parts = expr_clean.split('-')
                a = int(parts[0])
                b = int(parts[1])
                result = a - b
                op = '-'
            elif '*' in expr_clean:
                a, b = map(int, expr_clean.split('*'))
                result = a * b
                op = '×'
            elif '/' in expr_clean:
                a, b = map(int, expr_clean.split('/'))
                result = a // b  # 整数除法
                op = '÷'
            else:
                return '?', '无法解析的运算'

            # 生成解析
            solution = f'{a} {op} {b} = {result}'
            if op == '×' and b >= 10:
                # 两位数乘法的更详细解析
                solution += f' （分解: {a} × {b // 10} = {a * (b // 10)}, {a} × {b % 10} = {a * (b % 10)}）'

            return str(result), solution
        except Exception as e:
            return '?', f'解析错误: {str(e)}'

    def generate_fraction_answer(self, num1: int, den1: int, num2: int, den2: int, op: str = '-') -> Tuple[str, str]:
        """
        生成分数题答案和解析
        """
        try:
            if op == '-':
                result_num = num1 - num2
            else:  # '+'
                result_num = num1 + num2

            result_den = den1  # 同分母分数

            # 约分
            from math import gcd
            common_divisor = gcd(result_num, result_den)
            simplified_num = result_num // common_divisor
            simplified_den = result_den // common_divisor

            answer = f'{simplified_num}/{simplified_den}' if simplified_den != 1 else str(simplified_num)

            # 详细解析
            if op == '-':
                solution = f'{num1}/{den1} - {num2}/{den2} = {result_num}/{den1}'
                if common_divisor > 1:
                    solution += f' = {answer}（约分）'
            else:
                solution = f'{num1}/{den1} + {num2}/{den2} = {result_num}/{den1}'
                if common_divisor > 1:
                    solution += f' = {answer}（约分）'

            return answer, solution
        except:
            return '?', '无法解析'

    def generate_sample_answers_for_day(self, day: int) -> List[ProblemAnswer]:
        """
        生成某天的样例答案（用于演示）
        实际使用时应与题目生成器对接
        """
        answers = []
        difficulty_levels = ['简单', '简单', '中等', '中等', '困难']

        # 口算题答案
        for i in range(1, 11):
            import random
            a, b = random.randint(10, 99), random.randint(2, 9)
            expr = f'{a} × {b} ='
            answer, solution = self.generate_kousuan_answer(expr)
            answers.append(ProblemAnswer(
                problem_id=i,
                problem_text=expr,
                answer=answer,
                solution=solution,
                difficulty=random.choice(difficulty_levels),
                category='口算'
            ))

        # 竖式题答案
        for i in range(11, 16):
            import random
            a, b = random.randint(10, 99), random.randint(10, 99)
            expr = f'{a} × {b} ='
            answer, solution = self.generate_kousuan_answer(expr)
            answers.append(ProblemAnswer(
                problem_id=i,
                problem_text=expr,
                answer=answer,
                solution=solution,
                difficulty=random.choice(difficulty_levels),
                category='竖式'
            ))

        # 分数题答案
        for i in range(16, 21):
            import random
            den = random.choice([6, 8, 10])
            n1, n2 = random.randint(1, den - 1), random.randint(1, den - 1)
            n1, n2 = max(n1, n2), min(n1, n2)  # 确保结果非负
            answer, solution = self.generate_fraction_answer(n1, den, n2, den, '-')
            answers.append(ProblemAnswer(
                problem_id=i,
                problem_text=f'{n1}/{den} - {n2}/{den} =',
                answer=answer,
                solution=solution,
                difficulty=random.choice(difficulty_levels),
                category='分数'
            ))

        self.add_day_answers(day, answers)
        return answers

    def generate_answer_sheet_text(self, day: int, include_solutions: bool = True) -> str:
        """
        生成答案页的文本内容
        """
        if day not in self.answers:
            return f'第{day}天暂无答案'

        answers = self.answers[day]

        lines = []
        lines.append('=' * 70)
        lines.append(f'                        第 {day} 天 参考答案')
        lines.append('=' * 70)
        lines.append(f'生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        lines.append('')

        # 按题型分类
        categories = {'口算': [], '竖式': [], '分数': [], '填空': [], '应用': []}
        for ans in answers:
            if ans.category in categories:
                categories[ans.category].append(ans)

        for cat_name, cat_answers in categories.items():
            if not cat_answers:
                continue

            lines.append(f'【{cat_name}题答案】')
            lines.append('-' * 70)

            for i, ans in enumerate(cat_answers, 1):
                # 题目编号和答案
                line = f'  {ans.problem_id:2d}. {ans.problem_text:<20s} 答案: {ans.answer:<6s}'

                # 难度标记
                difficulty_marks = {'简单': '⭐', '中等': '⭐⭐', '困难': '⭐⭐⭐'}
                line += f'  {difficulty_marks.get(ans.difficulty, "")}'

                lines.append(line)

                # 解析（如果需要）
                if include_solutions and ans.solution:
                    lines.append(f'        💡 解析: {ans.solution}')

            lines.append('')

        # 统计信息
        total_count = len(answers)
        easy_count = sum(1 for a in answers if a.difficulty == '简单')
        medium_count = sum(1 for a in answers if a.difficulty == '中等')
        hard_count = sum(1 for a in answers if a.difficulty == '困难')

        lines.append('📊 题目难度统计:')
        lines.append(f'   简单: {easy_count} 题 ({easy_count/total_count*100:.0f}%)')
        lines.append(f'   中等: {medium_count} 题 ({medium_count/total_count*100:.0f}%)')
        lines.append(f'   困难: {hard_count} 题 ({hard_count/total_count*100:.0f}%)')
        lines.append('')

        # 得分预估（假设难度系数）
        expected_score = (easy_count * 0.95 + medium_count * 0.75 + hard_count * 0.5) / total_count * 100
        lines.append(f'📈 预期正确率参考: {expected_score:.0f}%')
        lines.append(f'   - 优秀学生: {expected_score + 10:.0f}%')
        lines.append(f'   - 普通学生: {expected_score:.0f}%')
        lines.append(f'   - 需加强: {expected_score - 15:.0f}% 以下')
        lines.append('')
        lines.append('=' * 70)

        return '\n'.join(lines)

    def export_answers_to_text(self, filepath: str, days: Optional[List[int]] = None, include_solutions: bool = True) -> None:
        """导出答案到文本文件"""
        export_days = days or sorted(self.answers.keys())

        content = []
        content.append('╔' + '=' * 68 + '╗')
        content.append('║' + ' ' * 15 + '📚 三年级数学每日一练 参考答案' + ' ' * 16 + '║')
        content.append('╚' + '=' * 68 + '╝')
        content.append('')
        content.append(f'📅 覆盖天数: 第{min(export_days)}天 ~ 第{max(export_days)}天')
        content.append(f'⏱️  生成时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        content.append(f'💡 答案说明:')
        content.append('   ⭐ = 简单题 | ⭐⭐ = 中等题 | ⭐⭐⭐ = 困难题')
        content.append('')
        content.append('=' * 70)
        content.append('')

        for day in export_days:
            content.append(self.generate_answer_sheet_text(day, include_solutions))
            content.append('')
            content.append('\\f')  # 分页标记
            content.append('')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

        print(f'✅ 答案已导出: {filepath}')
        print(f'   覆盖天数: {len(export_days)} 天')

    def generate_error_analysis(self, day: int, wrong_problems: List[int]) -> Dict:
        """
        生成错题分析报告
        """
        if day not in self.answers:
            return {}

        wrong_answers = [a for a in self.answers[day] if a.problem_id in wrong_problems]

        # 按类别和难度统计
        category_stats = {}
        difficulty_stats = {}

        for ans in wrong_answers:
            category_stats[ans.category] = category_stats.get(ans.category, 0) + 1
            difficulty_stats[ans.difficulty] = difficulty_stats.get(ans.difficulty, 0) + 1

        # 分析建议
        suggestions = []
        for category, count in category_stats.items():
            if count >= 3:
                suggestions.append(f'⚠️  {category}题错误较多（{count}题），建议加强该题型练习')
            elif count >= 2:
                suggestions.append(f'📝 {category}题需关注，建议多做几道同类题目')

        for difficulty, count in difficulty_stats.items():
            if difficulty == '困难' and count >= 2:
                suggestions.append('💡 难题错误较多属正常现象，可先从基础题开始巩固')

        return {
            'day': day,
            'total_wrong': len(wrong_answers),
            'total_questions': len(self.answers[day]),
            'accuracy': (len(self.answers[day]) - len(wrong_answers)) / len(self.answers[day]) * 100,
            'category_stats': category_stats,
            'difficulty_stats': difficulty_stats,
            'suggestions': suggestions,
            'wrong_answers': wrong_answers
        }


# ============================================
# 便捷使用函数
# ============================================
def generate_answer_sheet(
    days: int = 40,
    output_path: str = '数学练习册_参考答案.txt',
    include_solutions: bool = True
) -> None:
    """
    便捷生成答案册

    Args:
        days: 生成天数
        output_path: 输出文件路径
        include_solutions: 是否包含解析

    示例:
        >>> generate_answer_sheet(days=40, output_path='参考答案.txt')
    """
    generator = PDFAnswerGenerator()

    for day in range(1, days + 1):
        generator.generate_sample_answers_for_day(day)

    generator.export_answers_to_text(output_path, include_solutions=include_solutions)
    print(f'✅ 答案册生成完成: {output_path}')


def generate_error_report(
    day: int,
    wrong_problems: List[int],
    output_path: Optional[str] = None
) -> Dict:
    """
    生成错题分析报告

    Args:
        day: 第几天
        wrong_problems: 错题编号列表
        output_path: 输出文件路径（可选）

    示例:
        >>> report = generate_error_report(day=3, wrong_problems=[2, 5, 8])
        >>> print(report['suggestions'])
    """
    generator = PDFAnswerGenerator()
    generator.generate_sample_answers_for_day(day)
    report = generator.generate_error_analysis(day, wrong_problems)

    if output_path:
        lines = []
        lines.append('=' * 70)
        lines.append(f'                    第 {day} 天 错题分析报告')
        lines.append('=' * 70)
        lines.append(f'📊 正确率: {report["accuracy"]:.1f}%')
        lines.append(f'📝 错题数: {report["total_wrong"]} / {report["total_questions"]}')
        lines.append('')
        lines.append('📋 按题型统计:')
        for cat, count in report['category_stats'].items():
            lines.append(f'   {cat}: {count} 题')
        lines.append('')
        lines.append('🎯 改进建议:')
        for sug in report['suggestions']:
            lines.append(f'   {sug}')
        lines.append('')
        lines.append('📖 错误题目与解析:')
        for ans in report['wrong_answers']:
            lines.append(f'   第{ans.problem_id:2d}题: {ans.problem_text}')
            lines.append(f'         正确答案: {ans.answer}')
            lines.append(f'         解析: {ans.solution}')
        lines.append('')
        lines.append('=' * 70)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f'✅ 错题分析报告已导出: {output_path}')

    return report


# ============================================
# 测试代码
# ============================================
if __name__ == '__main__':
    print('=' * 60)
    print('🧪 PDF答案生成器 - 测试')
    print('=' * 60)
    print()

    # 生成5天的样例答案
    generator = PDFAnswerGenerator()
    for day in range(1, 6):
        generator.generate_sample_answers_for_day(day)
        print(f'✅ 第{day}天答案生成完成')

    print()

    # 导出答案册
    generator.export_answers_to_text('数学练习册_参考答案_样例.txt', days=list(range(1, 6)))
    print()

    # 生成错题分析报告
    print('📊 生成错题分析报告...')
    wrong_list = [2, 5, 7, 12, 15]  # 假设错了这些题
    report = generate_error_report(day=3, wrong_problems=wrong_list, output_path='第3天_错题分析.txt')

    print(f'   正确率: {report["accuracy"]:.1f}%')
    print(f'   错题数: {report["total_wrong"]}/{report["total_questions"]}')
    print(f'   改进建议: {len(report["suggestions"])}条')

    print()
    print('=' * 60)
    print('✅ 答案生成器测试完成！')
    print('=' * 60)

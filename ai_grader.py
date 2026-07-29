# -*- coding: utf-8 -*-
"""
AI自动批改模块
功能：
    1. 接收学生答题数据
    2. 与标准答案对比
    3. 自动评分
    4. 错题分析与诊断
    5. 个性化学习建议
    6. 对接Kimi AI进行智能解析（可选）
"""
import os
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class StudentAnswer:
    """学生答题数据"""
    problem_id: int          # 题目编号
    student_answer: str      # 学生答案
    correct_answer: str      # 标准答案
    is_correct: bool = False # 是否正确
    error_type: str = ''     # 错误类型：计算错误/进位错误/概念错误等


@dataclass
class GradingResult:
    """批改结果"""
    day: int                        # 第几天
    student_name: str               # 学生姓名
    total_problems: int             # 总题数
    correct_count: int              # 正确数
    wrong_count: int                # 错误数
    score: float                    # 得分(百分制)
    accuracy: float                 # 正确率
    wrong_answers: List[StudentAnswer] = field(default_factory=list)  # 错题详情
    category_accuracy: Dict[str, float] = field(default_factory=dict)  # 各题型正确率
    suggestions: List[str] = field(default_factory=list)  # 改进建议
    grading_time: str = ''          # 批改时间


class AIGrader:
    """AI自动批改器"""

    # 错误类型分类
    ERROR_TYPES = {
        '计算错误': '加减法计算失误',
        '进位错误': '乘法进位错误',
        '借位错误': '减法借位错误',
        '概念错误': '数学概念理解错误',
        '粗心错误': '漏看题目、抄错数字',
        '书写错误': '答案书写不规范、字迹不清',
    }

    # 难度权重
    DIFFICULTY_WEIGHTS = {
        '简单': 1.0,
        '中等': 1.5,
        '困难': 2.0,
    }

    def __init__(self, use_kimi_ai: bool = False):
        """
        初始化批改器

        Args:
            use_kimi_ai: 是否使用Kimi AI进行深度分析（需要配置API密钥）
        """
        self.use_kimi_ai = use_kimi_ai
        self.kimi_client = None

        if use_kimi_ai:
            try:
                from kimi_api import KimiAPI
                self.kimi_client = KimiAPI(
                    api_key='sk-kcWs7KsFkwnx5xY862fyIacqN2Wlf9I39YFB56WPLnGb22mD'
                )
                print('✅ Kimi AI 深度分析已启用')
            except Exception as e:
                print(f'⚠️  Kimi AI 初始化失败: {e}，将使用基础批改模式')
                self.use_kimi_ai = False

    def grade_answers(
        self,
        day: int,
        student_answers: Dict[int, str],
        correct_answers: List,
        student_name: str = '学生',
        weighted_scoring: bool = True  # 是否按难度加权计分
    ) -> GradingResult:
        """
        批改学生答案

        Args:
            day: 第几天
            student_answers: 学生答案字典 {题目编号: 学生答案}
            correct_answers: 标准答案列表（ProblemAnswer对象）
            student_name: 学生姓名
            weighted_scoring: 是否启用难度加权计分

        Returns:
            GradingResult 批改结果对象
        """
        result = GradingResult(
            day=day,
            student_name=student_name,
            total_problems=len(correct_answers),
            correct_count=0,
            wrong_count=0,
            score=0.0,
            accuracy=0.0,
            grading_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        wrong_answers = []
        total_weight = 0.0
        earned_weight = 0.0

        # 按题型统计正确率
        category_stats = {}  # {题型: [正确数, 总数]}

        for problem in correct_answers:
            prob_id = problem.problem_id
            student_ans = student_answers.get(prob_id, '').strip()
            correct_ans = str(problem.answer).strip()

            # 初始化题型统计
            if problem.category not in category_stats:
                category_stats[problem.category] = [0, 0]
            category_stats[problem.category][1] += 1

            # 获取题目权重
            weight = self.DIFFICULTY_WEIGHTS.get(problem.difficulty, 1.0)
            total_weight += weight

            # 智能判分（支持多种格式）
            is_correct = self._smart_compare(student_ans, correct_ans)

            if is_correct:
                result.correct_count += 1
                earned_weight += weight
                category_stats[problem.category][0] += 1
            else:
                result.wrong_count += 1
                error_type = self._analyze_error_type(problem, student_ans, correct_ans)
                wrong_answers.append(StudentAnswer(
                    problem_id=prob_id,
                    student_answer=student_ans,
                    correct_answer=correct_ans,
                    is_correct=False,
                    error_type=error_type
                ))

        # 计算得分和正确率
        result.wrong_answers = wrong_answers

        if weighted_scoring and total_weight > 0:
            result.score = round((earned_weight / total_weight) * 100, 1)
            result.accuracy = result.score
        else:
            result.accuracy = round(result.correct_count / result.total_problems * 100, 1)
            result.score = result.accuracy

        # 计算各题型正确率
        for category, (correct, total) in category_stats.items():
            result.category_accuracy[category] = round(correct / total * 100, 1) if total > 0 else 0

        # 生成改进建议
        result.suggestions = self._generate_suggestions(result)

        # 如果启用Kimi AI，进行深度分析
        if self.use_kimi_ai and self.kimi_client:
            try:
                ai_analysis = self._kimi_deep_analysis(result)
                result.suggestions.extend(ai_analysis)
            except Exception as e:
                print(f'⚠️  Kimi AI 深度分析失败: {e}')

        return result

    def _smart_compare(self, student_ans: str, correct_ans: str) -> bool:
        """
        智能答案对比（支持多种格式）
        """
        if not student_ans:
            return False

        s = str(student_ans).strip()
        c = str(correct_ans).strip()

        # 完全匹配
        if s == c:
            return True

        # 忽略空格
        if s.replace(' ', '') == c.replace(' ', ''):
            return True

        # 分数格式兼容（支持 1/2 和 0.5）
        try:
            if '/' in c and '/' not in s:
                # 标准答案是分数，学生写的是小数
                num, den = map(int, c.split('/'))
                if abs(float(s) - num / den) < 0.001:
                    return True
            elif '/' in s and '/' in c:
                # 都是分数，比较数值
                s_num, s_den = map(int, s.split('/'))
                c_num, c_den = map(int, c.split('/'))
                if abs(s_num / s_den - c_num / c_den) < 0.001:
                    return True
        except:
            pass

        return False

    def _analyze_error_type(self, problem, student_ans: str, correct_ans: str) -> str:
        """
        分析错误类型
        """
        if not student_ans:
            return '未作答'

        # 尝试计算差异
        try:
            s = float(student_ans)
            c = float(correct_ans)
            diff = abs(s - c)

            if problem.category == '口算':
                if diff <= 5:
                    return '计算错误'
                elif diff <= 20:
                    return '进位错误'
                else:
                    return '粗心错误'
            elif problem.category == '竖式':
                if diff <= 50:
                    return '进位错误'
                else:
                    return '计算错误'
            elif problem.category == '分数':
                return '概念错误'
        except:
            pass

        return '未知错误'

    def _generate_suggestions(self, result: GradingResult) -> List[str]:
        """
        基于批改结果生成改进建议
        """
        suggestions = []

        # 总体评价
        if result.accuracy >= 95:
            suggestions.append('🎉 表现优秀！继续保持！')
        elif result.accuracy >= 85:
            suggestions.append('👍 表现不错，继续努力！')
        elif result.accuracy >= 70:
            suggestions.append('📝 还有提升空间，建议多练习')
        else:
            suggestions.append('💪 需要加强基础练习，建议从简单题开始')

        # 按题型分析
        for category, accuracy in sorted(result.category_accuracy.items(), key=lambda x: x[1]):
            if accuracy < 60:
                suggestions.append(f'⚠️  {category}题正确率较低({accuracy:.0f}%)，建议重点加强')
            elif accuracy < 80:
                suggestions.append(f'📌 {category}题需关注({accuracy:.0f}%)，建议多做几道练习')

        # 错题数量建议
        if result.wrong_count >= 10:
            suggestions.append('💡 错误较多，建议当天重新做一遍全部题目')
        elif result.wrong_count >= 5:
            suggestions.append('💡 建议把错题抄在错题本上，第二天重新做')

        return suggestions

    def _kimi_deep_analysis(self, result: GradingResult) -> List[str]:
        """
        使用Kimi AI进行深度错题分析
        """
        if not self.kimi_client:
            return []

        # 构建错题分析prompt
        wrong_summary = []
        for wa in result.wrong_answers[:5]:  # 最多取前5题分析
            wrong_summary.append(
                f'第{wa.problem_id}题: 学生答案={wa.student_answer}, '
                f'正确答案={wa.correct_answer}, 错误类型={wa.error_type}'
            )

        prompt = f'''
        请作为小学数学老师，分析以下学生的答题情况并给出针对性建议：

        学生：{result.student_name}
        第{result.day}天练习
        得分：{result.score}分
        正确率：{result.accuracy}%
        错题数：{result.wrong_count}/{result.total_problems}

        错题详情：
        {chr(10).join(wrong_summary)}

        各题型正确率：
        {chr(10).join([f'{cat}: {acc:.1f}%' for cat, acc in result.category_accuracy.items()])}

        请用中文给出：
        1. 总体评价
        2. 主要薄弱环节分析
        3. 3-5条具体的改进建议（要实际可操作）
        4. 鼓励的话

        控制在150字以内，语气亲切。
        '''

        try:
            response = self.kimi_client.chat(prompt, use_history=False)
            # 分行整理
            lines = [line.strip() for line in response.split('\n') if line.strip()]
            return lines[:5]  # 最多5条建议
        except Exception as e:
            return [f'AI分析暂时不可用: {str(e)[:30]}']

    def generate_grading_report(self, result: GradingResult, filepath: str) -> None:
        """
        生成批改报告并保存到文件
        """
        content = []
        content.append('╔' + '=' * 68 + '╗')
        content.append('║' + ' ' * 22 + '📊 AI自动批改报告' + ' ' * 26 + '║')
        content.append('╚' + '=' * 68 + '╝')
        content.append('')
        content.append(f'👤 学生姓名: {result.student_name}')
        content.append(f'📅 第{result.day}天练习')
        content.append(f'⏱️  批改时间: {result.grading_time}')
        content.append('')
        content.append('=' * 70)
        content.append('📈 成绩概览')
        content.append('=' * 70)
        content.append('')

        # 评分等级
        if result.score >= 90:
            grade = '🌟 优秀'
        elif result.score >= 80:
            grade = '👍 良好'
        elif result.score >= 60:
            grade = '📝 及格'
        else:
            grade = '💪 需努力'

        content.append(f'  得分: {result.score} 分  [{grade}]')
        content.append(f'  正确率: {result.accuracy:.1f}%')
        content.append(f'  正确题数: {result.correct_count}/{result.total_problems}')
        content.append(f'  错误题数: {result.wrong_count}/{result.total_problems}')
        content.append('')

        content.append('=' * 70)
        content.append('📋 各题型正确率')
        content.append('=' * 70)
        content.append('')
        for category, accuracy in sorted(result.category_accuracy.items(), key=lambda x: x[1], reverse=True):
            bar = '█' * int(accuracy / 10)
            content.append(f'  {category:6s}: {accuracy:5.1f}%  {bar}')
        content.append('')

        content.append('=' * 70)
        content.append('💡 改进建议')
        content.append('=' * 70)
        content.append('')
        for i, suggestion in enumerate(result.suggestions, 1):
            content.append(f'  {i}. {suggestion}')
        content.append('')

        if result.wrong_answers:
            content.append('=' * 70)
            content.append('📖 错题详情')
            content.append('=' * 70)
            content.append('')
            for wa in result.wrong_answers[:10]:  # 最多显示10题
                content.append(f'  第{wa.problem_id:2d}题:')
                content.append(f'      ❌ 你的答案: {wa.student_answer or "未作答"}')
                content.append(f'      ✅ 正确答案: {wa.correct_answer}')
                content.append(f'      📝 错误类型: {wa.error_type}')
                content.append('')

            if len(result.wrong_answers) > 10:
                content.append(f'  ... 还有 {len(result.wrong_answers) - 10} 道错题')
                content.append('')

        content.append('=' * 70)
        content.append('🎯 下一步行动')
        content.append('=' * 70)
        content.append('')
        content.append('  1. 把所有错题抄到错题本上')
        content.append('  2. 明天重新做一遍错题')
        content.append('  3. 针对薄弱题型做专项练习')
        content.append('  4. 每周末复习本周所有错题')
        content.append('')
        content.append('=' * 70)
        content.append(f'💪 加油 {result.student_name}！每天进步一点点！')
        content.append('=' * 70)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(content))

        print(f'✅ 批改报告已生成: {filepath}')


# ============================================
# 便捷使用函数
# ============================================
def grade_student_paper(
    day: int,
    student_answers: Dict[int, str],
    student_name: str = '学生',
    use_kimi_ai: bool = False,
    output_report: Optional[str] = None
) -> GradingResult:
    """
    便捷批改学生作业

    Args:
        day: 第几天
        student_answers: 学生答案字典 {题目编号: 答案}
        student_name: 学生姓名
        use_kimi_ai: 是否使用Kimi AI深度分析
        output_report: 输出报告文件路径（可选）

    Returns:
        GradingResult 批改结果

    示例:
        >>> answers = {1: '123', 2: '456', 3: '789'}  # 学生答案
        >>> result = grade_student_paper(
        ...     day=3,
        ...     student_answers=answers,
        ...     student_name='小明',
        ...     output_report='批改报告.txt'
        ... )
        >>> print(f'得分: {result.score}')
    """
    from pdf_answer_generator import PDFAnswerGenerator

    # 生成标准答案
    answer_gen = PDFAnswerGenerator()
    correct_answers = answer_gen.generate_sample_answers_for_day(day)

    # 批改
    grader = AIGrader(use_kimi_ai=use_kimi_ai)
    result = grader.grade_answers(
        day=day,
        student_answers=student_answers,
        correct_answers=correct_answers,
        student_name=student_name,
        weighted_scoring=False  # 默认使用简单计分，更直观
    )

    # 生成报告
    if output_report:
        grader.generate_grading_report(result, output_report)

    return result


def simulate_grading_demo(use_kimi_ai: bool = False) -> GradingResult:
    """
    演示：模拟学生答题并批改
    """
    print('=' * 60)
    print('🧪 AI自动批改演示')
    print('=' * 60)
    print()

    # 生成标准答案（这是实际的题目）
    from pdf_answer_generator import PDFAnswerGenerator
    answer_gen = PDFAnswerGenerator()
    correct_answers = answer_gen.generate_sample_answers_for_day(day=3)

    # 模拟学生答案（基于同一套题）
    import random
    student_answers = {}
    for ans in correct_answers:
        if random.random() < 0.88:  # ~88%正确率
            student_answers[ans.problem_id] = ans.answer
        else:
            # 模拟错误答案
            try:
                correct_val = int(ans.answer)
                student_answers[ans.problem_id] = str(correct_val + random.randint(-5, 5))
            except:
                student_answers[ans.problem_id] = '?'

    print(f'📝 模拟学生答案 (共{len(student_answers)}题)')
    print(f'   随机正确率: ~88%')
    print()

    # 直接使用AIGrader批改（使用同一套correct_answers）
    grader = AIGrader(use_kimi_ai=use_kimi_ai)
    result = grader.grade_answers(
        day=3,
        student_answers=student_answers,
        correct_answers=correct_answers,
        student_name='小明',
        weighted_scoring=False
    )

    # 生成报告
    grader.generate_grading_report(result, '第3天_AI批改报告.txt')

    print(f'✅ 批改完成！')
    print(f'   得分: {result.score} 分')
    print(f'   正确率: {result.accuracy:.1f}%')
    print(f'   错题: {result.wrong_count}/{result.total_problems}')
    print()
    print(f'   改进建议: {len(result.suggestions)}条')
    for i, sug in enumerate(result.suggestions[:3], 1):
        print(f'   {i}. {sug[:50]}...')

    return result


# ============================================
# 测试代码
# ============================================
if __name__ == '__main__':
    # 基础批改演示（不使用Kimi AI）
    simulate_grading_demo(use_kimi_ai=False)

    print()
    print('=' * 60)
    print('✅ AI批改模块测试完成！')
    print('=' * 60)

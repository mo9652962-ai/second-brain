# -*- coding: utf-8 -*-
"""
数学练习生成器 - GUI界面
功能：
    1. 配置练习参数（天数、题量、难度）
    2. 预览和生成练习册Word文档
    3. 艾宾浩斯复习计划生成
    4. 查看AI批改报告
    5. 生成配套答案
"""
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime, timedelta
from typing import Optional


class MathWorkbookGUI:
    """数学练习生成器主界面"""

    def __init__(self, root):
        self.root = root
        self.root.title('📚 三年级数学每日一练生成器')
        self.root.geometry('800x600')
        self.root.resizable(True, True)

        # 设置全局字体
        self.default_font = ('Microsoft YaHei UI', 10)
        self.title_font = ('Microsoft YaHei UI', 12, 'bold')

        # 配置变量
        self.total_days_var = tk.IntVar(value=40)
        self.kousuan_count_var = tk.IntVar(value=15)
        self.shushi_count_var = tk.IntVar(value=10)
        self.fraction_count_var = tk.IntVar(value=10)
        self.fill_count_var = tk.IntVar(value=5)
        self.application_count_var = tk.IntVar(value=2)
        self.output_path_var = tk.StringVar(value=os.path.expanduser('~/Desktop'))
        self.student_name_var = tk.StringVar(value='学生')

        # 创建界面
        self._create_menu()
        self._create_notebook()

        # 状态栏
        self.status_var = tk.StringVar(value='✅ 系统就绪')
        self._create_status_bar()

    def _create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)

        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='📄 生成练习册', command=self.generate_workbook)
        file_menu.add_command(label='📅 生成复习计划', command=self.generate_review_plan)
        file_menu.add_separator()
        file_menu.add_command(label='📤 导出答案', command=self.export_answers)
        file_menu.add_separator()
        file_menu.add_command(label='🚪 退出', command=self.root.quit)
        menubar.add_cascade(label='📁 文件', menu=file_menu)

        # 工具菜单
        tool_menu = tk.Menu(menubar, tearoff=0)
        tool_menu.add_command(label='📝 AI批改演示', command=self.show_grading_demo)
        tool_menu.add_command(label='📊 查看已生成的报告', command=self.view_reports)
        menubar.add_cascade(label='🛠️  工具', menu=tool_menu)

        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label='📖 使用说明', command=self.show_help)
        help_menu.add_command(label='ℹ️  关于', command=self.show_about)
        menubar.add_cascade(label='❓ 帮助', menu=help_menu)

        self.root.config(menu=menubar)

    def _create_notebook(self):
        """创建选项卡"""
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 选项卡1：练习册配置
        self._create_config_tab()

        # 选项卡2：艾宾浩斯复习计划
        self._create_review_tab()

        # 选项卡3：AI批改
        self._create_grading_tab()

        # 选项卡4：答案生成
        self._create_answer_tab()

    def _create_config_tab(self):
        """配置选项卡"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='📝 练习册配置')

        # 主框架
        main_frame = ttk.Frame(tab, padding='20')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 标题
        ttk.Label(
            main_frame,
            text='📚 三年级数学每日一练生成器',
            font=self.title_font
        ).pack(pady=(0, 20))

        # 基础配置区
        config_frame = ttk.LabelFrame(main_frame, text='基础配置', padding='15')
        config_frame.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(config_frame, text='总天数：', font=self.default_font).grid(row=0, column=0, sticky='w', pady=5)
        ttk.Entry(config_frame, textvariable=self.total_days_var, width=10).grid(row=0, column=1, sticky='w', pady=5)
        ttk.Label(config_frame, text='天', font=self.default_font).grid(row=0, column=2, sticky='w', pady=5)

        ttk.Label(config_frame, text='学生姓名：', font=self.default_font).grid(row=1, column=0, sticky='w', pady=5)
        ttk.Entry(config_frame, textvariable=self.student_name_var, width=20).grid(row=1, column=1, columnspan=2, sticky='w', pady=5)

        ttk.Label(config_frame, text='输出路径：', font=self.default_font).grid(row=2, column=0, sticky='w', pady=5)
        ttk.Entry(config_frame, textvariable=self.output_path_var, width=40).grid(row=2, column=1, sticky='w', pady=5)
        ttk.Button(config_frame, text='浏览...', command=self._browse_path).grid(row=2, column=2, sticky='w', pady=5, padx=5)

        # 题量配置区
        quantity_frame = ttk.LabelFrame(main_frame, text='每日题量配置', padding='15')
        quantity_frame.pack(fill=tk.X, pady=(0, 15))

        # 口算题
        ttk.Label(quantity_frame, text='口算题：', font=self.default_font).grid(row=0, column=0, sticky='w', pady=5)
        ttk.Entry(quantity_frame, textvariable=self.kousuan_count_var, width=10).grid(row=0, column=1, sticky='w', pady=5)
        ttk.Label(quantity_frame, text='题', font=self.default_font).grid(row=0, column=2, sticky='w', pady=5)

        # 笔算题
        ttk.Label(quantity_frame, text='笔算题：', font=self.default_font).grid(row=1, column=0, sticky='w', pady=5)
        ttk.Entry(quantity_frame, textvariable=self.shushi_count_var, width=10).grid(row=1, column=1, sticky='w', pady=5)
        ttk.Label(quantity_frame, text='题', font=self.default_font).grid(row=1, column=2, sticky='w', pady=5)

        # 分数题
        ttk.Label(quantity_frame, text='分数题：', font=self.default_font).grid(row=2, column=0, sticky='w', pady=5)
        ttk.Entry(quantity_frame, textvariable=self.fraction_count_var, width=10).grid(row=2, column=1, sticky='w', pady=5)
        ttk.Label(quantity_frame, text='题', font=self.default_font).grid(row=2, column=2, sticky='w', pady=5)

        # 填空题
        ttk.Label(quantity_frame, text='单位换算：', font=self.default_font).grid(row=0, column=3, sticky='w', pady=5, padx=20)
        ttk.Entry(quantity_frame, textvariable=self.fill_count_var, width=10).grid(row=0, column=4, sticky='w', pady=5)
        ttk.Label(quantity_frame, text='题', font=self.default_font).grid(row=0, column=5, sticky='w', pady=5)

        # 应用题
        ttk.Label(quantity_frame, text='应用题：', font=self.default_font).grid(row=1, column=3, sticky='w', pady=5, padx=20)
        ttk.Entry(quantity_frame, textvariable=self.application_count_var, width=10).grid(row=1, column=4, sticky='w', pady=5)
        ttk.Label(quantity_frame, text='题', font=self.default_font).grid(row=1, column=5, sticky='w', pady=5)

        # 操作按钮
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)

        ttk.Button(
            btn_frame,
            text='🚀 生成练习册',
            command=self.generate_workbook,
            width=20
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            btn_frame,
            text='🔄 恢复默认配置',
            command=self._reset_config,
            width=15
        ).pack(side=tk.LEFT, padx=5)

        # 输出预览区
        preview_frame = ttk.LabelFrame(main_frame, text='📋 配置预览', padding='15')
        preview_frame.pack(fill=tk.BOTH, expand=True)

        self.preview_text = tk.Text(preview_frame, height=8, font=('Consolas', 10))
        self.preview_text.pack(fill=tk.BOTH, expand=True)

        # 初始预览
        self._update_preview()

        # 绑定变量变化事件
        for var in [self.total_days_var, self.kousuan_count_var, self.shushi_count_var,
                    self.fraction_count_var, self.fill_count_var, self.application_count_var]:
            var.trace_add('write', lambda *args: self._update_preview())

    def _create_review_tab(self):
        """复习计划选项卡"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='📅 艾宾浩斯复习计划')

        main_frame = ttk.Frame(tab, padding='20')
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            main_frame,
            text='🧠 艾宾浩斯遗忘曲线复习计划生成器',
            font=self.title_font
        ).pack(pady=(0, 20))

        # 说明文字
        info_text = '''
💡 艾宾浩斯复习规律：
  第1天学习 → 第1天复习（12小时后）
  → 第2天复习 → 第4天复习 → 第7天复习
  → 第15天复习 → 第30天复习

按照这个规律复习，记忆留存率可达90%以上！
        '''.strip()
        ttk.Label(main_frame, text=info_text, font=('Microsoft YaHei UI', 9)).pack(pady=(0, 20))

        # 配置区
        config_frame = ttk.LabelFrame(main_frame, text='计划配置', padding='15')
        config_frame.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(config_frame, text='开始日期：', font=self.default_font).grid(row=0, column=0, sticky='w', pady=5)
        self.start_date_var = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
        ttk.Entry(config_frame, textvariable=self.start_date_var, width=15).grid(row=0, column=1, sticky='w', pady=5)
        ttk.Label(config_frame, text='（格式：YYYY-MM-DD）', font=('Microsoft YaHei UI', 8)).grid(row=0, column=2, sticky='w', pady=5, padx=5)

        ttk.Label(config_frame, text='计划天数：', font=self.default_font).grid(row=1, column=0, sticky='w', pady=5)
        self.plan_days_var = tk.IntVar(value=30)
        ttk.Entry(config_frame, textvariable=self.plan_days_var, width=10).grid(row=1, column=1, sticky='w', pady=5)
        ttk.Label(config_frame, text='天', font=self.default_font).grid(row=1, column=2, sticky='w', pady=5)

        # 按钮
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)

        ttk.Button(
            btn_frame,
            text='📅 生成复习计划',
            command=self.generate_review_plan,
            width=20
        ).pack(side=tk.LEFT, padx=5)

        # 计划预览区
        preview_frame = ttk.LabelFrame(main_frame, text='📋 计划预览', padding='15')
        preview_frame.pack(fill=tk.BOTH, expand=True)

        self.review_text = tk.Text(preview_frame, height=15, font=('Consolas', 9))
        self.review_text.pack(fill=tk.BOTH, expand=True)

    def _create_grading_tab(self):
        """AI批改选项卡"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='🤖 AI批改')

        main_frame = ttk.Frame(tab, padding='20')
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            main_frame,
            text='📊 AI自动批改与错题分析',
            font=self.title_font
        ).pack(pady=(0, 20))

        # 配置区
        config_frame = ttk.LabelFrame(main_frame, text='批改配置', padding='15')
        config_frame.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(config_frame, text='第几天练习：', font=self.default_font).grid(row=0, column=0, sticky='w', pady=5)
        self.grading_day_var = tk.IntVar(value=3)
        ttk.Entry(config_frame, textvariable=self.grading_day_var, width=10).grid(row=0, column=1, sticky='w', pady=5)

        ttk.Label(config_frame, text='学生姓名：', font=self.default_font).grid(row=1, column=0, sticky='w', pady=5)
        ttk.Entry(config_frame, textvariable=self.student_name_var, width=20).grid(row=1, column=1, sticky='w', pady=5)

        # 功能按钮
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)

        ttk.Button(
            btn_frame,
            text='🎲 模拟学生答题演示',
            command=self.show_grading_demo,
            width=20
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            btn_frame,
            text='📖 查看批改报告',
            command=self.view_reports,
            width=15
        ).pack(side=tk.LEFT, padx=5)

        # 结果显示区
        result_frame = ttk.LabelFrame(main_frame, text='📋 批改结果', padding='15')
        result_frame.pack(fill=tk.BOTH, expand=True)

        self.grading_result_text = tk.Text(result_frame, height=15, font=('Consolas', 9))
        self.grading_result_text.pack(fill=tk.BOTH, expand=True)

    def _create_answer_tab(self):
        """答案生成选项卡"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='📄 答案生成')

        main_frame = ttk.Frame(tab, padding='20')
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(
            main_frame,
            text='✅ 练习册配套答案与解析生成器',
            font=self.title_font
        ).pack(pady=(0, 20))

        # 配置区
        config_frame = ttk.LabelFrame(main_frame, text='答案配置', padding='15')
        config_frame.pack(fill=tk.X, pady=(0, 15))

        ttk.Label(config_frame, text='生成天数：', font=self.default_font).grid(row=0, column=0, sticky='w', pady=5)
        self.answer_days_var = tk.IntVar(value=10)
        ttk.Entry(config_frame, textvariable=self.answer_days_var, width=10).grid(row=0, column=1, sticky='w', pady=5)
        ttk.Label(config_frame, text='天', font=self.default_font).grid(row=0, column=2, sticky='w', pady=5)

        self.include_solution_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            config_frame,
            text='包含详细解题解析',
            variable=self.include_solution_var
        ).grid(row=1, column=0, columnspan=3, sticky='w', pady=5)

        # 按钮
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)

        ttk.Button(
            btn_frame,
            text='📄 生成答案文档',
            command=self.export_answers,
            width=20
        ).pack(side=tk.LEFT, padx=5)

        # 预览区
        preview_frame = ttk.LabelFrame(main_frame, text='📋 答案预览', padding='15')
        preview_frame.pack(fill=tk.BOTH, expand=True)

        self.answer_preview_text = tk.Text(preview_frame, height=15, font=('Consolas', 9))
        self.answer_preview_text.pack(fill=tk.BOTH, expand=True)

    def _create_status_bar(self):
        """创建状态栏"""
        status_bar = ttk.Frame(self.root, relief=tk.SUNKEN)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        ttk.Label(
            status_bar,
            textvariable=self.status_var,
            font=('Microsoft YaHei UI', 8)
        ).pack(side=tk.LEFT, padx=5, pady=2)

    def _browse_path(self):
        """浏览输出路径"""
        path = filedialog.askdirectory(title='选择输出路径')
        if path:
            self.output_path_var.set(path)

    def _update_preview(self):
        """更新配置预览"""
        preview = f'''
{'=' * 60}
📚 练习册配置预览
{'=' * 60}

📅 总天数：      {self.total_days_var.get()} 天
👤 学生姓名：    {self.student_name_var.get()}
📂 输出路径：    {self.output_path_var.get()}

📝 每日题量配置：
   • 口算题：    {self.kousuan_count_var.get()} 题
   • 竖式题：    {self.shushi_count_var.get()} 题
   • 分数题：    {self.fraction_count_var.get()} 题
   • 单位换算：  {self.fill_count_var.get()} 题
   • 应用题：    {self.application_count_var.get()} 题

📊 每日总计：    {self.kousuan_count_var.get() + self.shushi_count_var.get() + self.fraction_count_var.get() + self.fill_count_var.get() + self.application_count_var.get()} 题
📈 总题量：      {self.total_days_var.get() * (self.kousuan_count_var.get() + self.shushi_count_var.get() + self.fraction_count_var.get() + self.fill_count_var.get() + self.application_count_var.get())} 题

{'=' * 60}
        '''.strip()

        self.preview_text.delete('1.0', tk.END)
        self.preview_text.insert('1.0', preview)

    def _reset_config(self):
        """恢复默认配置"""
        self.total_days_var.set(40)
        self.kousuan_count_var.set(15)
        self.shushi_count_var.set(10)
        self.fraction_count_var.set(10)
        self.fill_count_var.set(5)
        self.application_count_var.set(2)
        self.student_name_var.set('学生')
        self.output_path_var.set(os.path.expanduser('~/Desktop'))

        self.status_var.set('✅ 已恢复默认配置')
        messagebox.showinfo('提示', '已恢复默认配置！')

    def generate_workbook(self):
        """生成练习册（标准教材版）"""
        self.status_var.set('⏳ 正在生成练习册...')
        self.root.update()

        try:
            from generate_math_workbook_standard import MathWorkbookConfig, generate_full_workbook

            # 更新配置
            MathWorkbookConfig.OUTPUT_FILENAME = f'{self.student_name_var.get()}_数学每日一练_{self.total_days_var.get()}天_标准教材版.docx'
            MathWorkbookConfig.OUTPUT_FULL_PATH = os.path.join(
                self.output_path_var.get(),
                MathWorkbookConfig.OUTPUT_FILENAME
            )
            MathWorkbookConfig.PROBLEMS_PER_DAY = {
                "口算": self.kousuan_count_var.get(),
                "竖式": self.shushi_count_var.get(),
                "分数": self.fraction_count_var.get(),
                "填空": self.fill_count_var.get(),
                "应用": self.application_count_var.get(),
            }

            # 生成文档
            filepath = generate_full_workbook()

            self.status_var.set(f'✅ 练习册已生成: {filepath}')
            messagebox.showinfo('成功', f'✅ 练习册生成完成！\n\n📂 文件路径：\n{filepath}')

        except Exception as e:
            self.status_var.set(f'❌ 生成失败: {str(e)}')
            messagebox.showerror('错误', f'生成练习册失败：\n{str(e)}')

    def generate_review_plan(self):
        """生成复习计划"""
        self.status_var.set('⏳ 正在生成复习计划...')
        self.root.update()

        try:
            from ebbinghaus_review import generate_ebbinghaus_plan

            plan = generate_ebbinghaus_plan(
                start_date=self.start_date_var.get(),
                total_days=self.plan_days_var.get(),
                export_path=None
            )

            # 显示预览
            preview = f'''
{'=' * 60}
📅 艾宾浩斯复习计划
{'=' * 60}

开始日期: {plan.start_date}
总天数: {len(plan.schedule)} 天

前10天预览：
{'-' * 60}
'''
            for day_info in plan.schedule[:10]:
                type_mark = '📖' if not day_info.is_review else '🔄'
                topics = '、'.join(day_info.topics[:2])
                preview += f'  第{day_info.day:2d}天 [{day_info.date}] {type_mark} {day_info.problem_count:3d}题 - {topics}\n'

            preview += f'''
{'-' * 60}
💡 提示：完整计划已保存到 数学复习计划_艾宾浩斯.txt
    '''

            self.review_text.delete('1.0', tk.END)
            self.review_text.insert('1.0', preview.strip())

            self.status_var.set('✅ 复习计划已生成')
            messagebox.showinfo('成功', '✅ 艾宾浩斯复习计划生成完成！')

        except Exception as e:
            self.status_var.set(f'❌ 生成失败: {str(e)}')
            messagebox.showerror('错误', f'生成复习计划失败：\n{str(e)}')

    def show_grading_demo(self):
        """显示批改演示"""
        self.status_var.set('⏳ 正在进行AI批改演示...')
        self.root.update()

        try:
            from ai_grader import simulate_grading_demo

            # 执行批改演示
            result = simulate_grading_demo(use_kimi_ai=False)

            # 显示结果
            result_text = f'''
{'=' * 60}
📊 AI自动批改结果
{'=' * 60}

👤 学生姓名：{result.student_name}
📅 第 {result.day} 天练习

📈 成绩统计：
   • 得分：      {result.score} 分
   • 正确率：    {result.accuracy:.1f}%
   • 正确题数：  {result.correct_count}/{result.total_problems}
   • 错题数：    {result.wrong_count}/{result.total_problems}

📋 各题型正确率：
'''
            for category, accuracy in result.category_accuracy.items():
                result_text += f'   • {category}：{accuracy:.1f}%\n'

            result_text += f'''
💡 改进建议：
'''
            for i, suggestion in enumerate(result.suggestions, 1):
                result_text += f'   {i}. {suggestion}\n'

            result_text += f'''
{'=' * 60}
📄 详细报告已保存到：第{result.day}天_AI批改报告.txt
            '''

            self.grading_result_text.delete('1.0', tk.END)
            self.grading_result_text.insert('1.0', result_text.strip())

            self.status_var.set('✅ AI批改演示完成')

        except Exception as e:
            self.status_var.set(f'❌ 批改失败: {str(e)}')
            messagebox.showerror('错误', f'AI批改失败：\n{str(e)}')

    def export_answers(self):
        """导出答案"""
        self.status_var.set('⏳ 正在生成答案...')
        self.root.update()

        try:
            from pdf_answer_generator import generate_answer_sheet

            output_path = os.path.join(
                self.output_path_var.get(),
                f'数学练习册_{self.answer_days_var.get()}天_参考答案.txt'
            )

            generate_answer_sheet(
                days=self.answer_days_var.get(),
                output_path=output_path,
                include_solutions=self.include_solution_var.get()
            )

            # 显示预览
            with open(output_path, 'r', encoding='utf-8') as f:
                content = f.read()

            self.answer_preview_text.delete('1.0', tk.END)
            self.answer_preview_text.insert('1.0', content[:2000] + '\n\n...\n（文件内容过长，仅显示前2000字符）')

            self.status_var.set(f'✅ 答案已生成: {output_path}')
            messagebox.showinfo('成功', f'✅ 答案文档生成完成！\n\n📂 文件路径：\n{output_path}')

        except Exception as e:
            self.status_var.set(f'❌ 生成失败: {str(e)}')
            messagebox.showerror('错误', f'生成答案失败：\n{str(e)}')

    def view_reports(self):
        """查看报告"""
        import subprocess
        import platform

        try:
            # 尝试打开报告文件
            report_files = [
                '第3天_AI批改报告.txt',
                '数学复习计划_艾宾浩斯.txt',
                '数学练习册_参考答案_样例.txt'
            ]

            found_files = []
            for f in report_files:
                if os.path.exists(f):
                    found_files.append(f)

            if found_files:
                msg = '📄 找到以下报告文件：\n\n'
                for f in found_files:
                    msg += f'  • {f}\n'
                msg += '\n点击确定将打开文件所在文件夹。'

                if messagebox.askyesno('找到报告文件', msg + '\n\n是否打开文件夹？'):
                    # 打开当前目录
                    if platform.system() == 'Windows':
                        os.startfile('.')
                    elif platform.system() == 'Darwin':  # macOS
                        subprocess.run(['open', '.'])
                    else:  # Linux
                        subprocess.run(['xdg-open', '.'])
            else:
                messagebox.showinfo('提示', '未找到报告文件，请先生成练习册或执行批改。')

        except Exception as e:
            messagebox.showerror('错误', f'打开报告失败：\n{str(e)}')

    def show_help(self):
        """显示帮助"""
        help_text = '''
📚 三年级数学每日一练生成器 - 使用说明

📝 【练习册配置】
   1. 设置总天数和每日题量
   2. 选择输出路径（默认桌面）
   3. 点击"生成练习册"按钮

📅 【艾宾浩斯复习计划】
   1. 设置开始日期和计划天数
   2. 点击"生成复习计划"
   3. 按照计划安排复习，记忆效果更佳

🤖 【AI批改】
   1. 点击"模拟学生答题演示"查看效果
   2. 自动生成批改报告和错题分析
   3. 提供针对性改进建议

📄 【答案生成】
   1. 设置生成天数
   2. 选择是否包含解题解析
   3. 生成配套答案文档

💡 小贴士：
   • 艾宾浩斯复习规律：学习后第1、2、4、7、15、30天复习
   • 建议每天固定时间练习，效果更佳
   • 错题要及时整理到错题本，第二天重做

📞 如有问题，请联系开发者
        '''.strip()

        messagebox.showinfo('使用说明', help_text)

    def show_about(self):
        """显示关于"""
        about_text = '''
📚 三年级数学每日一练生成器 v2.0

🎯 功能特点：
   • 自动生成口算、竖式、分数、单位换算、应用题
   • 标准Word文档格式，可直接打印
   • 艾宾浩斯遗忘曲线复习计划
   • AI自动批改与错题分析
   • 配套答案与详细解析

👨‍💻 技术实现：
   • Python 3.x + python-docx
   • tkinter GUI界面
   • 模块化设计架构

📅 开发时间：2026年

💝 祝愿每一位小朋友都能：
   快乐学习，天天进步！
        '''.strip()

        messagebox.showinfo('关于', about_text)


def main():
    """主函数"""
    root = tk.Tk()
    app = MathWorkbookGUI(root)

    # 居中显示
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    root.mainloop()


if __name__ == '__main__':
    main()

---
tags: [research, github, python, tutorial, article-study]
created: 2026-07-31
status: absorbed
source: https://github.com/jackfrued/Python-100-Days
---

# Python-100-Days — 研究笔记

> 来源：小黑盒文章（前沿情报站 07-20）· 2026-07-31 验证 + 评估

## 项目验证

| 项 | 值 |
|----|-----|
| Stars | **183,394**（文章说 184,228，基本吻合） |
| 作者 | 骆昊（jackfrued），2018 年创建，8 年维护 |
| 语言 | Jupyter Notebook 99.2%（浏览器直接跑，免装 IDE） |
| 内容 | 100 天分 10 个阶段：基础→进阶→Django→爬虫→数据分析→机器学习→工程化 |

## 文章推荐的结构（100 天怎么分）

| 阶段 | 天数 | 内容 |
|------|------|------|
| 基础关 | Day 1-15 | 变量、循环、函数、面向对象 |
| 进阶关 | Day 16-40 | 文件、正则、并发、网络 |
| 实战关 | Day 41-100 | Django、数据库、爬虫、数据分析 |

## 我们的评估：不是学习资料，是按需参考知识源

**关键判断：我们不是 Python 新手，我们每天都在用 Python 干活。**

我们已有的 Python 技能覆盖：
- `python-toolchain`（uv/venv/pip 日常）
- `python-document-generator`（参数化配置/KISS/DRY）
- `docx` / `xlsx` / `pdf` / `ocr-and-documents`（文档处理）
- `math-worksheet-generation` / `educational-worksheet-generator`（练习册）
- `android-automation`（uiautomator2）

## 决策

| 选项 | 决策 | 理由 |
|------|:---:|------|
| 下载/安装 | ❌ | 仓库巨大（含图片资源），全量拉取不值 |
| 作为学习路线 | ❌ | 我们不是新手，不需要 100 天规划 |
| **按需参考** | ✅ | Day21-30（Excel/Word/PPT/PDF/图像）和 Day58（Celery 定时）在接单/写脚本时可按需查阅 |

## 对我们有参考价值的章节（按需时再看）

| 章节 | 场景 |
|------|------|
| Day21-30 文件/Excel/Word/PPT/PDF | 闲鱼接单做文档/表格时参考 |
| Day58 Celery 异步+定时任务 | 与我们的 cron 体系对比 |
| Day62-65 爬虫（requests/XPath/Selenium/Scrapy） | 信息采集单参考 |
| Day92 Docker | 我们已有 docker 经验 |
| Day99-100 面试宝典 | 博主做"Python 就业"内容时参考 |

## 结论

- 项目真实（183K★，8 年维护），文章数据准确
- **对我们：按需参考知识源，不下载不学习**——我们已有的技能体系覆盖了日常 Python 工作
- 对博主身份：这是长青选题（Python 就业/100 天路线），可参考做内容
- 对新手：是好资源，但我们不是目标用户

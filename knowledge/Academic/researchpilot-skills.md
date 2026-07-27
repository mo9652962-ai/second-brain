---
tags: [research, AI-Agent, skills, academic-workflow, paper-writing]
domain: Academic
---
# ResearchPilot-Skills · AI 科研全流程 Skill 套件

来源：GitHub LMDHQ-0420/ResearchPilot-Skills
更新：2026-07-25 | v2.0

## 简介
7 阶段独立 Skill，从方向探索到论文发表全覆盖。
适用于 Claude Code / Codex / CodeBuddy。
MIT 开源协议。

## 七阶段流程

| 阶段 | Skill 名 | 工作内容 | 产出 |
|:----|:---------|:---------|:-----|
| **A** 方向探索 | `research[A]-exploration` | 文献检索≥15篇→3层RQ确认→必要性论证 | `idea_report.md` Part1 |
| **B** 深化 | `research[B]-development` | 完善流程→补充可行/不可行证据→Part2 | `idea_report.md` Part2 |
| **C** 实验设计 | `research[C]-design` | Baseline/消融/指标/资源预估→设计文档 | `implementation.md` |
| **D** 实现设计 | `research[D]-implementation` | 架构/数据流/模块/评估→编码方案 | `implementation.md` 最终版 |
| **E** 编码 | `research[E]-coding` | 项目结构/代码生成/配置管理 | 可运行实验代码 |
| **F** 迭代 | `research[F]-iteration` | 诊断→回溯→先改文档→再改代码 | 优化后代码+文档 |
| **G** 论文写作 | `research[G.*]` | G.0-G.8：规划→各章节→审阅→翻译 | 论文初稿→终稿 |

## 核心设计

### 设计文档与代码强绑定
- 改代码前必须先更新 `idea_report.md` / `implementation.md`
- 禁止只在代码里打补丁绕过设计问题
- 回溯全链路进行

### 实验设计不妥协
- 实验唯一目的：严格证明 idea 有效性
- 资源约束不参与设计，方案完成后才做预估

### 论文写作（基于彭思达学习笔记）
- G.1-G.7 每章有写作框架和范例
- 写完过一轮审阅
- 中英文翻译（G.8）

## 安装
```bash
git clone https://github.com/LMDHQ-0420/ResearchPilot-Skills.git
cd ResearchPilot-Skills
bash install-zh.sh   # 中文版
# 或 bash install-en.sh  # 英文版
```

## 使用
在 Claude Code / Codex 中触发：
```
/research[A] 探索方向
/research[START] 检测当前状态，决定从哪继续
```

## 与 academic-paper-writing Skill 的关系
- ResearchPilot 偏**实验驱动**（ML/CV/NLP方向），全流程管理 idea→code→paper
- academic-paper-writing 偏**写作驱动**，精修论文语言和结构
- 可互补：实验阶段用 ResearchPilot，精修阶段用 academic-paper-writing

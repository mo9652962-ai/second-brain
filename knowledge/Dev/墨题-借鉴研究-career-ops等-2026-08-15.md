---
tags: [墨题, 刷题机, 借鉴研究, 千轮研究, career-ops]
type: research
date: 2026-08-15
status: adopted
---

# 墨题改进借鉴研究（基于小君AI测评推荐项目）

> 2026-08-15 · 研究 7 个开源项目 → 提炼可借鉴点 → 映射到墨题（D:\english-multiple-choice-practice-machine）

## 一、七个项目画像

| 项目 | Stars | 定位 | 与墨题相关度 |
|:---|:---|:---|:---|
| **career-ops** | 63.9K | AI 求职全流程（评估/简历/跟踪，本地 CLI） | ⭐⭐⭐⭐⭐ 最相关 |
| **private-gpt** | 57.4K | 本地 AI API 层（RAG/skills/MCP，接任何 OpenAI 兼容服务器）| ⭐⭐⭐⭐ 高 |
| **meilisearch** | 59.0K | 极速搜索 + AI 混合搜索（Rust）| ⭐⭐⭐ 中 |
| **Supabase** | 108K | Postgres 开发平台（数据库/认证/实时）| ⭐⭐ 低（墨题本地优先）|
| **ToolJet** | 39.2K | 企业内部工具/仪表盘生成平台 | ⭐⭐ 低 |
| **shannon** | 46.8K | AI 渗透测试（安全）| ⭐ 无 |
| **public-apis** | 459K | 免费 API 列表 | ⭐ 数据源参考 |

## 二、career-ops 深度拆解（63.9K stars 的启示）

**一句话**：把任何 AI 编码 CLI 变成求职指挥中心——12 个 mode 各是独立 skill 文件，AI 分析、人决定（HITL），数据全本地。

### 可借鉴的 6 大设计

1. **HITL 设计哲学**：AI 分析 → 人决定 → 系统永不自动提交
   - 「自动化分析，不自动化决策」
2. **结构化评估 rubric**：5 维度 + 全局分 1.0-5.0
   - 无公式，模型整体判断；低于 4.0 不推荐申请；每个评分带证据引用（CV 行 + JD 要求）
3. **数据契约**：系统更新永远不碰数据层
   - cv.md/applications.md/reports/*.md 是用户数据，代码只读写约定格式
4. **12 mode 模块化**：每个 mode 独立 skill 文件（上下文/规则/工具隔离）
   - 加新 mode 不用改其他部分
5. **批处理 conductor**：conductor 编排 + N 个 headless worker 并行 + 状态 TSV + 断点续跑
6. **Pipeline 完整性**：merge/dedup/status 归一化/健康检查 4 个脚本保证数据一致

### 增长启示（对 AI 博主/产品）

- **真实数据故事**：740 职位 → 68 申请 → 12 面试 → 1 offer（自己真实求职驱动开发）
- **方法论公开**：完整 rubric 发布在 career-ops.org/methodology
- **Manifesto**：7 月发布 CareerOps Manifesto（60K stars 时）造势
- **插件生态**：opt-in、BYO-key、commit 钉住、5/6 社区贡献

## 三、墨题改进借鉴点（按优先级）

### 🥇 P0：AI 学习诊断（career-ops 评估模式 → 学习场景）

**现状**：墨题有 Report/Wrong/Calendar 但无「AI 诊断教练」
**借鉴**：答题 → 结构化诊断报告（仿 A-F rubric）：
- 薄弱维度：词汇/语法/阅读技巧/题型（每题带证据：错题 + 原题出处）
- 全局评估：当前水平 1-5 + 推荐练习路径
- 错题归因：AI 分析每道错题（知识点缺口/粗心/时间压力）
- 低于阈值 → 推荐针对性练习（接现有题库/词库）

### 🥈 P1：本地 AI 服务层（private-gpt 思路）

**现状**：AI 标注散在导入流程（deepseek 批量标注）
**借鉴**：后端加统一 AI 服务层（services/ai_provider.py）：
- 可插拔 Provider：本地 Qwen3-8B（sora 已有）/ DeepSeek API / 百炼
- 统一接口：explain(word) / analyze(wrong_set) / generate(exam)
- 离线优先：本地模型可用时走本地，云端 API 为增强
- 支撑功能：单词讲解、错题归因、真题解析、作文批改

### 🥉 P2：数据完整性校验（career-ops pipeline integrity）

**现状**：3 库同步（后端词库/frontend DB/手机内置）靠流程约束
**借鉴**：加 4 个校验脚本：
- merge-tracker 等价：3 库 diff 检查
- dedup 等价：词条/题目去重
- status 归一化等价：库间状态一致性
- health check 等价：外键/引用完整性 + 定期 cron 跑

### P3：容错搜索（meilisearch 思路）

**现状**：词库/题库搜索大概率 LIKE
**借鉴**：拼写容忍 + 前缀 + 相关性排序（轻量实现：分词 + 编辑距离阈值；不必引入 Rust 服务）

### P4：真实数据故事（增长/内容）

**借鉴 career-ops 叙事**：墨题也可以有「真实用户数据故事」：刷题量 → 正确率提升 → 上岸
**内容素材**：career-ops 增长拆解（63K stars 怎么来的：真实需求 + 方法论公开 + Manifesto + 社区）

## 四、落地建议

1. P0 最值钱：**「错题 AI 诊断」是刷题机 → 学习教练的升级**，也是差异化卖点（竞品大多只有统计没有归因）
2. P1 支撑 P0：AI 服务层先搭，Provider 先接 DeepSeek（现成），本地 Qwen 后续
3. P2 保稳定：3 库同步校验做成自动化，防止「数据丢失」类问题（sqlite-data-loss-diagnosis 技能已有雏形）
4. 搜索升级排后：现状够用，别为炫技引入重依赖

## 参考

- github.com/santifer/career-ops（ARCHITECTURE.md 全文已读）
- github.com/zylon-ai/private-gpt
- github.com/meilisearch/meilisearch
- 小君AI测评部署测试报告（推荐来源）

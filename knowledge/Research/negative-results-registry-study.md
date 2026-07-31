---
tags: [research, github, negative-results, methodology, open-science]
created: 2026-07-31
status: absorbed
source: https://github.com/redamancy231-create/negative-results-registry
license: CC BY 4.0
---

# AI 协作阴性结果登记册 — 研究笔记

> 来源：小黑盒文章 + Attached GitHub 数据 · 2026-07-31 验证 + 吸收

## 项目验证

| 项 | 值 |
|----|-----|
| Stars | 0（刚创建 2026-07-25，v0.2.0） |
| 条目 | 22 条（NRR-2026-001 ~ 022），10 领域 × 4 类型 |
| License | CC BY 4.0 |
| 结构 | md（人读）+ json（机读，JSON Schema Draft 2020-12 校验）+ registry.json 聚合索引 |
| CI | GitHub Actions：Schema 校验 + 链接检查 + 一致性检查 |
| 前端 | GitHub Pages 单文件 HTML（搜索/筛选/标签云/三语） |
| 角色模型 | 三角色：source_authors / analyst / submitted_by |

## 核心概念：文件抽屉问题（File Drawer Problem）

- 1979 年 Rosenthal 首次描述：阳性结果发表，阴性结果塞抽屉
- AI 协作领域同样：GitHub 满是"我用 AI 做了 X"，几乎没人记"我试了 X 失败了"
- **核心信念：阴性结果不是失败——是数据**

## 关键发现：这是 2026 年学术趋势（不只作者个人想法）

| 来源 | 内容 |
|------|------|
| arXiv 2606.21024 | 《Negative Knowledge as Failure-aware Shared Memory for AutoResearch》— 结构化负面知识是知识资产 |
| t46/negative-result-repository | 失败结构化 + 相似性搜索 + check_proposal 接口（proceed/caution/avoid） |
| hch-wang/Negative_Knowledge | curator agent 把失败转成 bounded typed record |

三者 + 本文档 = 2026 年"阴性结果结构化"赛道正在形成。

## Schema 设计（14 必填字段）

**6 元数据**：id / title / domain / category / submitted_by / date
**8 内容**：hypothesis / method / expected_result / actual_result / interpretation / source_project / source_authors / analyst
**10 可选**：effect_size / sample_size / models_used / reproducibility / lessons_learned / tags 等

## 三条证据门槛

1. 假设可证伪（"我认为 X 比 Y 在 Z 上提高 N%"）
2. 方法可复核（模型版本/样本/指标）
3. 证据可追溯（至少一个链接）

## 对我们的落地

### 识别出的缺口
我们的 ERRORS.md（56 条）只记"错误+修复"（阳性），漏记"尝试+无效"（阴性）——**这正是文件抽屉问题在我们体系的体现**。

### 落地动作
1. ✅ `.learnings/NEGATIVE-RESULTS.md` — 适配版登记模板（8 核心字段 + 8 分类 + 证据门槛）
2. ✅ 规则 #25「阴性结果登记」加入 hermes-workflow-preferences v1.19.0
3. ✅ 回填第一条真实阴性结果（NRR-20260731-001: jcode 因 SAC 封杀 abandoned）

## 结论

- 项目本身是结构化原型（单人维护，尚不能声称社区价值——作者自己也承认）
- **价值在方法论**：对抗文件抽屉问题 + Schema 强制结构 + 三角色溯源
- 学术印证充分（arXiv 2606.21024），2026 年赛道正在形成
- 我们已落地：登记模板 + 规则 #25 + 首条回填

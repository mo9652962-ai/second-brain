---
tags: [academic, paper, research]
domain: academic
cross-domain: [ai-agent, ppt-design, vibe-coding, workflow]
related: ["knowledge/AI-Agent", "knowledge/AI-Workflow", "knowledge/PPT-Design", "knowledge/Vibe-Coding"]
created: 2026-07-21
updated: 2026-07-23
status: adopted
---

# 学术知识库

```dataview
TABLE domain, tags, updated
FROM #ai-agent OR #workflow OR #ppt OR #academic OR #coding
WHERE file.name != this.file.name
SORT updated DESC
LIMIT 8
```

---

> 本知识库同时兼容 **OpenClaw** 与 **Hermes Agent** 环境。以下 9 个论文 skills 通过 ClawHub 安装，在两个平台中均可正常使用。

## 论文 Skills 全家桶

| 阶段 | Skill | 用途 |
|------|-------|------|
| 检索 | cnki-scholar | 知网/万方/维普 |
| 检索 | cnki-advanced-search | 知网高级检索自动化 |
| 检索 | journal-sci-ssci-checker | SCI/SSCI 索引检查 |
| 阅读 | paper-parse | 双模式深度研读 |
| 阅读 | paper-summarize-academic | 结构化摘要 |
| 写作 | chinese-academic-writing | 中文学术写作（去AI化） |
| 写作 | sci-paper-three-pass | SCI 三轮精修 |
| 写作 | paper-writing-workflow | 标准论文写作流程 |

- **实战复盘（2026-10-16）**：[[2026-10-16-thesis-reference-and-docx-linkage-lessons]] —— 文献真实/匹配/可访问三分、购买意向指标边界、DOCX 字段码链接和目标应用分层验收。

## 中文学术去 AI 化要点

- AI 痕迹特征识别
- 学术习语库
- 句式多样性注入
- 论证非线性重构
- 策略性不完美

## 变现方向

- 论文翻译润色（200-800 元/篇）
- 文献检索报告（100-200 元/次）
- SCI/SSCI 期刊推荐（50-100 元/次）
- 论文答辩 PPT（200-400 元/套）→ 详见 [[PPT-Design#学术 PPT 规范]]

---

## 🔗 知识关联

- **[[AI-Agent]]** — 由 9 个论文 skills 全家桶驱动（ClawHub 安装，Hermes / OpenClaw 双平台兼容）
- **[[PPT-Design]]** — 论文答辩 PPT 制作与学术汇报设计
- **[[Vibe-Coding]]** — 文献管理工具与写作环境
- **[[projects/current]]** — 学术服务变现进度
- **[[HOME]]** — 返回知识中枢
---
> 关联: [[PPT-Design]] · [[AI-Workflow]] · [[Cross-Domain|🔀 知识地图]] | [[HOME|🏠 首页]]

- **工具主张核验与代码静态审查（2026-10-16）**：[[2026-10-16-douyin-academic-tools-audit]] —— PubScholar/国家数据/AIGC 说法分级核验，撤回未经证实的 API、检测算法与商业服务断言；审计本地检索脚本，未作运行实测。 本日复核补记覆盖国家数据新版发布库、原型实现缺陷及检索协议冻结/覆盖/变更留痕。


- **书目元数据与 OA 复核升级（2026-10-16）**：[[2026-10-16-reference-metadata-audit-upgrade]] —— Crossref 元数据初筛、Unpaywall 关键词 API 退役、OpenAlex OA 版本线索与人工验收边界。

- **复测记录补充**：本次三类 Crossref 输入和技能校验通过；细节见 [[2026-10-16-reference-metadata-audit-upgrade]]。


- **论文写作生态评估（2026-10-16）**：[[2026-10-16-academic-writing-ecosystem-evaluation]] —— GitHub 写作/引文项目与 ResearchRabbit、Connected Papers、Elicit 等平台的免费优先组合、WPS 兼容边界和原文核验要求。


- **学术写作智能体工作流 v1.0（2026-10-16）**：[[2026-10-16-academic-writing-agent-workflow-v1]] —— 来源身份/全文/主张支持分离、证据账本、研究设计适配审查、阻断门与格式验证层级。

- **AIGC 检测与本地工具链核验（2026-10-16）**：[[2026-10-16-aigc-detection-toolchain-verification]] —— 媒体案例与学术研究的证据边界、ASI 假置信区间、生成批注不等于作者过程证明，以及本地 citation verifier 的静态问题。

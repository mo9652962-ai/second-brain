---
title: "数模竞赛「真正会用 AI」工作流生态调研（2026-08-23）"
type: note
domain: Productivity
status: active
tags: [knowledge/productivity]
source: null
date: 2026-08-23
---
# 数模竞赛「真正会用 AI」工作流生态调研（2026-08-23）

> 来源：抖音「Baby横空出世」作品——在数模竞赛里真正会用 AI 是什么体验（把琐碎环节交给 AI）
> 调研：数模 AI 工作流已从「提示词」进化到「全自动流水线 + 证据门禁」

## 核心认知升级

数模 AI 使用已进入第三阶段：
1. **提示词时代**（2024-25）：让 AI 写某段内容/代码
2. **Skill 工作流时代**（2026 初）：六阶段 SOP + 模板（mathmodel-pro 等）
3. **Autopilot 时代**（2026 中）：AI 全自动跑完流水线，人类只在关键节点拍板（AutoMCM-Pro / MathModel-Skill）

## 生态项目实证（按工作流成熟度）

| 项目 | 形式 | 关键设计 | 可借鉴点 |
|:---|:---|:---|:---|
| **AutoMCM-Pro**（RealSeaberry） | Claude Code Skill | **AI Autopilot/人类 Copilot**、AP/Manual 双模式、GitOps 流水线、**强制代码自证**、多 Agent 并行 | 自证脚本、状态机、demo 1h34m 出 2025A 题 |
| **MathModel-Skill**（yushui2022） | 10 个协作 Skills | **证据门禁**（SHA-256 防陈旧结果）、S0-S8 流程、workflow_guard 防漂移、Word OMML 公式 | 防漂移机制、断点恢复 |
| **math-modeling.skill**（ai-lcs） | Codex Skill | 选题可行性 → 证据链 → 提交审计，当届规则合规 | 合规检查边界 |
| **mathmodel-pro**（ll2010650） | 六阶段手册 | 9 份获奖论文范式、两级验收门禁 | 验收标准表 |
| Beacon（已调研） | LangGraph 10 节点 | checkpoint 恢复、HITL | 已入库 |

## 对 sora 数模代写业务的落点

**定位判断：对标物 + 提效工具，不是替代。** 客户买的是确定性交付，AI 流水线产出仍需人工质检。

1. **借鉴「强制代码自证」**（最重要）：代写交付前，每个模型脚本配独立验证脚本（约束满足/数值稳定/物理合理），全 PASS 才能写进论文 → 提高交付质量、减少客户返工
2. **借鉴「证据门禁」**：论文里的每个数字必须可追溯到实际运行结果，防 AI 编造 → 直接对应我们已踩过的「数值幻觉」坑
3. **借鉴「AP/Manual 双模式」**：接单分两种——「全自动初稿」（低价快单）+「人工精修」（高价单）
4. **防漂移机制**：长任务用 workflow_memory.json 记录断点，中断可恢复 → 我们的 paper-service 也可以加

## 反哺 shumo-paper-writing 技能

建议新增「质量门禁」章节：
- 数值一致性：正文/表格/附录三处一致
- 代码自证：每个求解脚本配 verify 脚本
- 证据追溯：每个数字来自真实运行，无占位符
- AI 声明合规：按当届规则核查 AI 使用声明

## 参考
- AutoMCM-Pro: github.com/RealSeaberry/AutoMCM-Pro（2025A题 demo 144 项验证）
- MathModel-Skill: github.com/yushui2022/MathModel-Skill
- math-modeling.skill: github.com/ai-lcs/math-modeling.skill

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]

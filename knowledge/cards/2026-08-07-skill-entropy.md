---
aliases:
  - skill-entropy-card-2026-08-07
tags:
  - knowledge-card
  - arxiv
  - ai-agent
  - skill
  - research
created: 2026-08-07
source: "[[knowledge/Research/arxiv-2026-08-07-agent-llm]]"
status: adopted
---

# 🃏 知识卡片 · 技能熵：技能编排 > 技能获取

> **来源**：arXiv 2608.05139（Gen-Verse）· 2026-08-07 检索 · ✅ 开源代码已发布
> **一句话**：长程推理的瓶颈不是「会多少技能」，而是「会不会在推理链里正确切换技能」——技能熵衡量的正是这种切换难度。

---

## 核心洞察 / 影响

| 维度 | 内容 |
|------|------|
| 问题 | 现有基准只测单技能（数学就是数学、代码就是代码），但长程任务要求模型在推理链内来回切换：先数学推导 → 再调度规划 → 再写代码 |
| 方法 | **Skill Entropy** 量化技能切换难度 → **Skill²-Bench**（558 技能 × 9 域）→ **Skill-Entropy RL**：每步同时预测答案与所用技能，reward 对齐预测技能序列与金标序列 |
| 效果 | Qwen3-4B：34.4% → **68.4%**；Qwen3-1.7B：14.6% → **40.1%**；同一训练信号可迁移到 OpenR1-Math 等现成数据 |
| 开源 | github.com/Gen-Verse/Skill-Entropy-RL |

## 关键数据 / 对 sora 的影响

1. ✅ **印证技能库组织思路**：「技能获取给能力，技能编排才给可靠长程智能」——skills/ 不只是收集，还要有编排；技能孤岛 = 隐性瓶颈
2. 💡 **可借鉴**：用 skill-switching 视角评估 Hermes 多技能编排质量（如 web_search → 提取 → 分析 → 写作 的切换是否顺畅、是否每次切换都掉链子）
3. 💡 **内容选题**：AI 博主可做一期「为什么 AI Agent 会『东一榔头西一棒子』」——技能切换成本是系统性解释，比单讲模型聪明度更有深度

## 行动项

- [x] 审视技能库是否存在「技能孤岛」：一个技能调用另一个技能时有没有损耗（可先用 graphify 看技能引用图）
- [x] ~~（可选）把 Skill²-Bench 思路迁移到刷题机~~ 📖 条件触发参考（等刷题机功能稳定后再做）

## ✅ 审视结论（2026-08-07 daily-todo-executor 落地）

**技能熵真实存在，主要来源 = 来源重复 + 近义重复（≥6 组、30+ 技能）**：

| 组 | 技能 | 说明 |
|:---|:-----|:-----|
| ① openclaw-imports 副本 | 8051-embedded-dev / cad-design-master / engineering-workflow / web-dev-2026 | 与顶层同名技能 100% 重复，纯冗余 |
| ② 水墨 UI | chinese-aesthetic-web-ui / chinese-ink-wash-ui / ink-wash-ui-theming / ink-wash-web-ui-theming / ink-wash-ui-design | 5 个同域技能，内容高度重叠 |
| ③ 找技能 | find-skills ×2（@guipi888 + @miknasbh-stack） | 双副本 |
| ④ CAD | cad / cad-design-complete-guide / cad-design-master / text-to-cad / text2cad-cad / implicit-cad / cad-viewer / step-parts | 8+ 个，部分为工具/MCP 类（可保留） |
| ⑤ Sims4 | sims4-mod-development / sims4-mp-protocol-engineering / sims4-mp-regression-testing / sims4-launcher-dev / sims4-mp-launcher-dev / s4mp-protocol-engineering / sims-4-modding-multiplayer | 7 个，可合并为 1-2 个 |
| ⑥ 论文写作 | academic-paper-writing / paper-writing-workflow / sci-paper-three-pass / chinese-academic-writing / academic-presentation | 5 个，互为补充但可收敛 |

**孤岛观察**：多数技能 SKILL.md 无 cross-reference；切换损耗主要在「每次切换都要重新 skill_view 全文加载」——与卡片「技能编排 > 技能获取」主题一致。
**合并动作**：与 `projects/current.md`「Skill 重复合并 6 组（待 sora 一句话确认）」一致，确认后按 ①→②→③→⑤→⑥ 优先级执行；④ 因含工具类暂缓。

## 为什么重要

- 直接回答「模型能力很强但长程任务总掉链子」——切换技能是隐性瓶颈，不是能力问题
- 与 sora 的技能库 / Second Brain 组织思想同构，有实操落点而非纯理论
- 开源代码可复现，训练信号可迁移，属于「能用」的知识

---

*卡片来源：当天知识库精选 · arXiv 08-07 Agent/LLM 速览（🥇 ★★★★★ 关联度最高 + 开源可落地）*

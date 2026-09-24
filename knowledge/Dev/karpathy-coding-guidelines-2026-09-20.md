---
tags: [github, W39, ClaudeCode, 编码规范, Karpathy, 提示词工程, codex]
aliases: [andrej-karpathy-skills, karpathy-guidelines, Karpathy 编码四原则]
date: 2026-09-20
source: https://github.com/multica-ai/andrej-karpathy-skills
---

# andrej-karpathy-skills — 单文件 CLAUDE.md 修复 LLM 编码四大通病

> 2026-09-20 W39 精选。从 Andrej Karpathy 对 LLM 编码坑的观察提炼成**一个 CLAUDE.md 文件**（也可作为 SKILL.md / Cursor 规则），改善 Claude Code/Codex 等编码 agent 行为。≈ 205k★（+21k/周），MIT。

## 一句话定位

Karpathy 指出 LLM 编码三大病：① 替你瞎假设还不检查；② 爱过度设计（1000 行当 100 行写）；③ 顺手改/删没搞懂的代码。本项目用 **4 条原则一个文件** 对症下药——行为约束，而非功能。

## 核心特征：四原则

| 原则 | 治的病 | 关键行为 |
|:--|:--|:--|
| **Think Before Coding** | 错误假设、隐藏困惑、不展示权衡 | 明确列出假设；不确定就问；多种解释都摆出来不沉默选一个；有更简单方案要 push back；困惑就停下指名道姓地问 |
| **Simplicity First** | 过度复杂、抽象膨胀 | 不要需求外的功能；不为单次使用建抽象；不要没要的「灵活/可配置」；不为不可能场景写错误处理；200 行能写成 50 行就重写 |
| **Surgical Changes** | 越界改动、顺手优化 | 只动必须动的；不改相邻代码/注释/格式；不重构没坏的东西；匹配现有风格；发现无关死代码只提不删；只清理自己造成的新孤儿 |
| **Goal-Driven Execution** | 弱验收、来回扯皮 | 把命令式任务转成可验证目标：「加校验」→「写无效输入测试再让它过」；多步任务带 verify 检查点；强成功标准让 agent 独立循环 |

关键洞察（Karpathy 原话）：「LLMs 极其擅长循环直到达成具体目标……**别告诉它做什么，给它成功标准，看它跑**」。

## 创新点详解

1. **一个文件治行为**：不装框架、不写插件逻辑，就是一份行为守则——可合并进任何项目 CLAUDE.md / SKILL.md / Cursor rule，零依赖零学习成本。
2. **「每行改动都可溯源到请求」判据**：把「外科手术式修改」变成可检查的测试（改的每行都能 trace 回用户请求）——质量门禁不靠感觉靠标准。
3. **反过度设计的 timing 洞察**：例子里的过度设计「不是错」，是**时机错**——过早引入复杂度。核心判据 = 复杂度到需要时再加。
4. **Tradeoff 明说**：原则偏「谨慎优先于速度」，平凡任务（改 typo）可跳过完整流程——不是一刀切慢。

## 💎 可借鉴点（对 sora 工作流）

1. **Codex 委派模板升级**：sora 用 Codex CLI 做编码委派（codex-task-*.md）——把四原则直接写进委派模板/提示词：假设清单前置、success criteria + verify 检查点、禁止越界重构、每行改动可溯源。与 hermes-codex-security-gate 的验证分级天然互补（行为约束 + 验证分级 = 双保险）。
2. **Hermes 自身代码任务**：k 接编码任务（墨题/脚本）时，Surgical Changes 尤其对症——别顺手改不相干代码。可考虑吸收为 skill 要点（code-quality-bootstrapping / engineering-workflow）。
3. **与已有方法论合并而非新装**：sora 已有 ponytail（极简编程）、TDD、engineering-workflow——本项目不是新框架，是**行为清单**，合并进现有技能即可，不建新 skill。
4. **Goal-Driven 与验证文化同源**：与 ai-code-review 的「修复后必须重新 scan 验证」、OverclaimBench 的「完成声明核验」完全一致——「给成功标准 + 验证闭环」是 sora 已在走的路，这个文件是现成话术库。

## 安装 / 验证命令

```bash
# 方式 A：Claude Code 插件
/plugin marketplace add multica-ai/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-guidelines
# 方式 B：合入项目 CLAUDE.md（curl 追加）
curl -o CLAUDE.md https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/main/CLAUDE.md
# 方式 C：SKILL.md 形态（skills/karpathy-guidelines/SKILL.md 可直接取用）
# 验证：跑一个已知会过度设计的小任务，检查 diff 是否只剩请求内改动
```

## 总结评价表

| 维度 | 评价 |
|:--|:--|
| 技术含金量 | ★★★★ 不是技术架构，是行为工程——4 条原则直击 LLM 编码高频失误 |
| 值得安装 | 🟢 合并进 Codex 委派模板 + 已有技能，不单独安装 |
| 趋势判断 | 编码 agent 行为约束/提示词规范成为热赛道（205k★ 说明刚需）；「成功标准而非指令」是共识方向 |
| 风险 | 纯守则无自动化；过度谨慎会拖慢平凡任务（作者已明说 tradeoff） |

---
> 🗺️ 属于 [[MOC-Dev]] · [[MOC-GitHub]] · 周报 [[GitHub-Weekly-2026-09-20|W39]]

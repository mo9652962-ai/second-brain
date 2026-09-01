---
tags: [agent-skills, google, skills.sh, 生态, W34]
aliases: [google-skills, google-agent-skills]
date: 2026-08-16
source: https://github.com/google/skills
status: watch
---

# google/skills — Google 官方 Agent Skills 仓库

> **简介**：Google 官方出品的 Agent Skills（agentskills.io 标准），覆盖 Google Cloud / Gemini / BigQuery / Android / Flutter / Dart / Firestore / Ads / Analytics 等产品线。本周 18,356⭐ **+1,821/周**（Python，Apache-2.0，244 commits，copybara 持续同步）。

## 核心思路

1. **官方 skill 生态 = 产品文档的 agent 化**：每个 skill 是一个 SKILL.md（agentskills.io 标准），把产品 API 用法、认证、最佳实践做成 agent 可直接消费的技能，替代/补充传统文档。
2. **三层结构**：
   - `skills/` 单产品 skill（认证、API 基础、平台配置）
   - `skills/cloud/` 多产品 solution skill（架构工作流、agentic analytics、RAG 方案、迁移指南）——**组合配方而非单 API 说明**
   - `plugins/` 捆绑 MCP server 的插件（data-agent-kit 等）
3. **多 harness 统一分发**：`npx skills add google/skills`（skills.sh 标准）+ Claude Code / Codex / Antigravity CLI 各自 plugin marketplace 安装——一套技能三端复用。
4. **生态扩展**：README 链接了更多官方 skill 仓库（google-cloud-storage、google/agents-cli、android/skills、dart-lang/skills、flutter/skills、firebase/agent-skills、genkit-ai/skills）。

## 精妙细节

- **copybara 自动同步**：提交人是 cloud-ix-copybara，内部 Piper 仓库自动外发——官方团队维护模式。
- **Skill Registry**：Agent Platform 里已有 skill registry 管理——技能进平台成为一等公民。
- **命名规范**：`google-cloud-recipe-*`（recipe 系列）、`google-cloud-solution-*`（solution 系列）——命名即分类。

## 💎 可借鉴点（对 sora 最值）

1. **「单产品 skill + solution skill」分层**：Google 把「怎么用 BigQuery API」和「怎么搭一套 agentic analytics 方案」分成不同层级。sora 的技能库可借鉴：现有 100+ skills 多为单工具操作，缺少「solution skill」——如「墨题接单全流程」可做成一个 solution skill 串联需求对齐→报价→交付→售后。
2. **Agent Skills 成为跨厂商标准**：anthropic 发明、OpenAI/Codex 跟进、Google 官方背书（skills.sh 安装器 + agentskills.io 规范）——「技能」是 2026 agent 生态的装配单元，sora 的技能体系与标准对齐（Hermes SKILL.md 格式已基本兼容，值得跟踪 agentskills.io 是否出 schema 校验器）。
3. **文档即技能**：Google 用 skill 仓库替代/增强产品文档——sora 对外输出（AI 博主内容、付费社群）可参考：把「教程」做成「可直接安装的 skill 包」是差异化卖点。

## 综合评估

| 维度 | 评价 |
|:---|:---|
| 技术含金量 | ★★★☆☆（内容多为官方文档 agent 化，工程创新一般，但生态意义大）|
| 与 sora 工作流关联 | ★★★☆☆（Google Cloud 技能与 sora 场景弱相关；但 skill 分层方法论和标准信号重要）|
| 值得安装 | 🔵 不装——Google 产品线技能对 sora 无直接使用场景，跟踪生态标准即可 |
| 趋势判断 | Agent Skills 标准被 Google 官方背书 = 跨厂商标准确立，2026 下半年「技能经济」成型 |

> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]] · 平行参考：[[agent-skills-addyosmani-2026-08-14]]（生产级工程技能）· [[mattpocock-skills]]（技能方法论）· [[diagram-design-2026-08-16]]（skill 商业化案例）

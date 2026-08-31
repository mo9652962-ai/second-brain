---
tags: [maintenance, vault, 断链修复, 标签归一]
type: maintenance
date: 2026-08-31
---

# 🔧 2026-08-31 知识库维护

> 例行维护 cron：断链审计 + 空文件清理 + 标签一致性优化

## 概览

| 指标 | 结果 |
|:-----|:-----|
| 断链（wikilink） | 25 → 0 |
| README markdown 路径断链 | 6 → 0 |
| 空文件 | 0（全仓 945 个 .md 无空壳） |
| 标签冲突 | 6 组 → 0 |

## 一、断链修复（25 处，10 文件）

**技能名引用 → 纯文本反引号**（Hermes 技能不是 vault 笔记，按惯例转 `code`）：
- `knowledge/AI/数模5-Skill工作流-2026-08-23.md` → `shumo-paper-writing`
- `knowledge/Development/VibeCoding部署全流程-下-2026-08-23.md` → `nextjs-deploy-test` / `multi-end-ai-provider-config`
- `knowledge/Productivity/freelance-quote-4questions-2026-08-21.md` → `ai-freelance-pricing` / `grill-with-docs` / `xianyu-monetization`
- `knowledge/Research/网安资料库-入口.md` + `综合研究-2026-08-22.md` → `src-bug-hunting` / `src-recon-workflow` / `web-security-lab-setup` / `pentest-lab-setup` / `nmap-scanning`
- `knowledge/Security/nmap-tutorial-2026-08-20.md` / `osint-username-maigret-2026-08-21.md` → `src-recon-scanning` 等

**已归档删除文件链接 → 纯文本**（目标在 git 历史被归档后清理，HEAD 不存在）：
- `knowledge/cards/2026-08-03-linggan-deai.md` → `memory/2026/08/2026-08-03-research-apply`（2 处）
- `memory/2026/08/2026-08-07-maintenance.md` → `2026-08-06-maintenance`

**目录链接 → 指向实际文件**：
- `outputs/xianyu-master/搭网站写脚本-商品素材包.md` → `[[outputs/xianyu-master/上架素材包/上架操作清单|上架素材包]]`

**README markdown 路径修正（6 处）**：`memory/2026-08-1X.md` / `memory/2026/2026-08-1X.md` → `memory/2026/08/2026-08-1X.md`（每日日志已归位 08/ 目录）

## 二、标签归一（6 组冲突 → 0，6 文件）

按多数派优先（平局走 vault 小写惯例）：

| 组 | 分布 | 归一为 | 修改文件 |
|:---|:---|:---|:---|
| ai | AI(4) > ai(1) | AI | src-ai-automation-3tools |
| ai-skill | ai-skill(1) = AI-skill(1) | ai-skill | nihaixia-skill |
| ai编程 | ai编程(1) = AI编程(1) | ai编程 | game-engine-ai-research |
| llm | LLM(10) > llm(1) | LLM | llmfit-hardware-matching |
| pcb | pcb(8) > PCB(1) | pcb | AI-PCB设计前沿-pcbflow对比 |
| redis | Redis(2) > redis(1) | Redis | 循环插入与缓存-两个夺命坑 |

## 三、审计脚本误报确认（无需处理）

`[[MEMORY.md]]` ×2、`[[knowledge/Productivity/github-monetization-2026-08-20.md]]` ×2 —— 目标文件实际存在且被 git 跟踪，是 `vault_link_audit.py` 对带 `.md` 后缀链接目标的解析 bug，非真断链。

## 四、隔离记录

- 今日 `memory/2026/08/` 无空文件（近空阈值 <40 字节 0 命中）
- 临时脚本已清理（.temp-* 均被 .gitignore 覆盖）
- 提交 `ca75030` 已推送 origin/main

> 关联：[[HOME|🏠 首页]] · [[memory/2026/08/2026-08-18-maintenance|上次维护 08-18]]

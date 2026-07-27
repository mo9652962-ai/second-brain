---
tags: [absorbed, codex, workflow, ai-coding]
source: Reddit/知乎 — "使用Codex两周能做出什么游戏" · RIVERSOFT
status: absorbed
date: 2026-07-27
---

# Codex 两周游戏开发 · 工作流吸收

> 1000 commits / 2 周 / 多人合同系统 / AI 配图

---

## 最值的借鉴：ChatGPT 额度耗尽后的替代方案

### GPT GitHub 插件 + GitHub Actions = 无限额度的 Codex

```
ChatGPT (无额度)
  ↓ GitHub 插件    ← 读取仓库、提交代码
  ↓ GitHub Actions ← 自动编译、验证
  ↓ SSH 部署       ← 编译通过后自动部署到服务器
```

**关键**：ChatGPT 内置虚拟机 + GitHub 插件 + Actions = 编写/上传/编译/调试/部署全闭环

### 全自动编程的雏形

```
用户提交 Issue
  ↓ ChatGPT 定时任务读取
  ↓ 修改代码 → 提交 PR
  ↓ GitHub Actions 编译验证
  ↓ 自动部署
  ↓ 完成
```

## 对我们闲鱼服务的启发

| 他的做法 | 我们能借鉴的 |
|:---------|:------------|
| AI 生成带 alpha 通道的 PNG 配图 | 接单时用 AI 生成样例图/配图 |
| PR 管理提交 | 闲鱼订单也用类似"审核→交付"流程 |
| 合同系统（玩家供料） | 论文/PPT 接单的"多次修改→定稿"流程 |
| Fallback: GPT+GitHub 插件 | 我们的 8 级 fallback 链思路一致 |

## 核心理念

> "随着 AI 的发展，代码能力不再重要，重要的是设计、创新的能力，以及约束 AI 的能力。"

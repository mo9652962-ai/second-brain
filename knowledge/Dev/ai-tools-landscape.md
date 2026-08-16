---
tags: [workflow, AI, automation, guide, hermes]
domain: AI
---
# AI 工作流搭建实战指南

来源：10 轮搜索引擎研究 + 现有知识整合
更新：2026-07-25

## 一、工具全景

| 工具 | 定位 | 部署方式 | 适合你吗？ |
|:----|:-----|:---------|:----------|
| **Hermes Agent** | AI Agent 编排（已有） | 已部署 | ✅ **主引擎** |
| **WorkBuddy** | 腾讯 AI 办公助手 | 桌面端 | ⚠️ 可试试 |
| **n8n** | 开源工作流自动化引擎 | Docker/自部署 | ❌ Docker 不可用 |
| **Dify** | 开源 LLM 应用平台 | Docker/自部署 | ❌ Docker 不可用 |
| **Coze (扣子)** | 字节零代码 AI 平台 | SaaS 免费 | ✅ **补充** |
| **RAGFlow** | 开源 RAG 知识库 | Docker | ❌ Docker 不可用 |

## 二、选型结论

```
推荐方案：
  主力 → Hermes Agent（已有，够用）
  补充 → Coze（扣子），零代码免费，注册即用
```

## 三、Hermes 工作流核心能力

| 能力 | 用途 | 当前状态 |
|:-----|:-----|:---------|
| **cron 定时任务** | 18 个任务覆盖日/周/月 | ✅ 已配置 |
| **delegate_task** | 并行派生子 Agent | ✅ 可用 |
| **skill_manage** | 按需加载 93 个 Skills | ✅ 全活跃 |
| **web_search** | 5 路搜索引擎并行 | ✅ 正常 |
| **context_from** | 链式传递 cron 输出 | ⚠️ 待配 |
| **mcp_servers** | GitHub + FileSystem | ✅ 已配 |
| **curator** | Skill 自动维护 | ✅ 已启用 |

## 四、context_from 链式串联

让 cron 任务接力传递数据：

```
arxiv-fetch (7:00) → 输出论文列表
       │ context_from
       ▼
arxiv-summarize (8:00) → 读取 fetch 输出做摘要
```

创建链式任务：
```bash
hermes cron create "0 8 * * *" "总结 arxiv-fetch 的论文" \
  --name arxiv-summarize --context-from arxiv-fetch
```

## 五、工作流稳定性优化

| 问题 | 方案 | 说明 |
|:-----|:-----|:------|
| cron 超时 | 缩短 prompt，限制输出长度 | memory-prune 之前 604s timeout |
| API 401 | 检查 Key 配置 | obsidian-maintenance 401 |
| 子 Agent 超时 | delegate_task 设置合理 timeout | 默认 300s，长任务调大 |
| 重复执行 | cron 幂等设计 | 同一天只写一次日志 |

## 六、工作流路线图

### 第 1 层：单次任务层级（已有）
```
用户需求 → Hermes 调用对应 Skill → 交付结果
```

### 第 2 层：定时自动化层级（已有 18 个 cron）
```
定时触发 → 自动执行 → 结果推送
每日: 论文 → 健康 → 技能 → 变现复盘
每周: 知识整合 → 趋势吸收 → 成本报告
```

### 第 3 层：多步骤 Pipeline（context_from）
```
步骤 A → [context_from] → 步骤 B → [context_from] → 步骤 C
```

### 第 4 层：多 Agent 并行（fan-out）
```
delegate_task(tasks=[搜索, 分析, 写作]) → 汇总
```

### 第 5 层：条件路由
```
判断任务类型 → 论文/academic / PPT/design / PCB/hardware
```

---
> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]]

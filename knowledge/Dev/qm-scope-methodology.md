---
tags: [methodology, AI-Agent, multi-agent, architecture, qm]
aliases: [qm-scope-methodology, hermes-multi-user-scope]
date: 2026-08-02
source: https://github.com/yc-software/qm
status: adopted
---

# 🏗️ qm 方法论：Scope 隔离 → Hermes 多人协作架构

> 2026-08-02 从 GitHub 热门仓库 yc-software/qm（4.5k⭐，MIT）提炼的方法论
> 核心问题：**如何让一个 Agent 系统安全地服务多人/多项目，而不互相干扰？**

## 一句话

qm 证明了：多人 Agent 协作的答案不是"一个全能 Agent"，而是**"每人一个隔离 scope + 共享能力按需授权"**——这与 Hermes/vault 的单人多项目结构是同一思想的工程化放大。

---

## 1️⃣ qm 的四个核心概念（原样提炼）

### 1.1 Scope 隔离（每用户/每房间独立环境）
- 每个人、每个聊天房间有**独立**的：memory、文件、keychain（密钥）、权限、crons、web apps、持久沙箱
- 各自干活互不影响，也可在群聊/项目中协作

### 1.2 Shared Skills（技能按 grant 分享）
- Skills 是 **scope-owned**（属于某个 scope），通过 **grant（授权）** 分享给别人
- 管理员可**晋升**到全组织可用
- 技能包可以从 **git 仓库导入**（版本化）

### 1.3 Deployment Directory（核心与配置分离）
- 核心引擎通用（Node + Fastify + Postgres + 可插拔 harness）
- 公司特定的一切（org 配置、自定义工具/技能、沙箱镜像、基础设施）放**部署目录**
- 换 harness（Pi/OpenCode/Codex/Claude Code）不换核心

### 1.4 Security 三档（组织级安全姿态）
| 档位 | 行为 | 对应 |
|:---:|------|------|
| **Strict** | 每个工具调用暂停等人工审批（除两个无副作用收尾动作） | Hermes 全程审批 |
| **Auto**（默认）| 分类器对 provenance 标记的外部数据和工具结果做内容筛查 | 内容安全过滤 |
| **Dangerous** | 无筛查、无暂停 | 无审批 |

> 所有档位下，**预声明命令策略**（递归删除、破坏性 SQL 等硬拒绝）始终生效。

---

## 2️⃣ 映射到 Hermes/vault 体系

| qm 概念 | Hermes/vault 现状 | 差距 | 借鉴价值 |
|---------|------------------|------|:---:|
| Scope 隔离 | 单一 profile（default）+ 单一 vault | **无多用户隔离** | ★★★★★ |
| Shared Skills | skills/ 全局共享，无授权粒度 | **无 grant 机制** | ★★★★ |
| Deployment Directory | vault 分层（knowledge/projects/memory） | ✅ 已有，思想一致 | ★★★ |
| Security 三档 | Hermes approval（命令/工具两级）+ SOUL 边界 | 有"批准/拒绝"二元，**无三档分类** | ★★★★ |
| 持久沙箱 | 无（直接操作真实文件系统） | **风险最大缺口** | ★★★★ |

---

## 3️⃣ 可落地设计（Hermes 多人协作扩展）

### 设计 A：多 Profile = Scope（最接近现状）
```
Hermes profiles/           ← qm 的 scope
├── default/               ← sora 个人（现状）
│   ├── skills/
│   ├── memories/
│   └── cron/
├── client-x/              ← 未来：客户/项目隔离（闲鱼接单）
│   ├── skills/            ← 只放该项目技能
│   ├── memories/          ← 独立记忆（客户上下文不串）
│   └── cron/              ← 独立定时任务
```
- ✅ 现状已支持多 profile（`hermes profiles`）
- 💡 应用：**闲鱼接单按客户开 profile** → 客户 A 的论文细节不会污染客户 B 的上下文

### 设计 B：Skill Grant（技能授权粒度）
现状：`skill_manage` 创建的技能全局可见。
借鉴：
- 技能 frontmatter 加 `scope: private|shared|public` 字段
- 接单专用技能（如某客户合同模板）标记 `scope: private` → 只在对应 profile 加载
- 方法论技能（如本笔记）标记 `shared` → 所有 profile 可读

### 设计 C：安全三档（对应 Bounded Autonomy）
衔接 eu-ai-act 三件套 + MEMORY「Bounded Autonomy」最佳实践：

| 档位 | 适用 | 工具策略 | EU AI Act 对齐 |
|:---:|------|---------|:---:|
| **Strict** | 对外产品/高价值任务 | 每个外部副作用（发消息/提交/删除）都审批 | Art.14 HITL ✅ |
| **Auto**（默认）| sora 日常 | 外部副作用审批 + 内部读取自由 + 内容筛查 | 部分 ✅ |
| **Dangerous** | 本地实验（如 Krea2 测试） | 全自动无审批 | ⚠️ 仅限本地 |

> 🔑 关键：**三档是组织级配置，窄 scope 只能收紧不能放宽**（qm 原则）——即客户 profile 只能用 Strict，不能自己降到 Dangerous。

### 设计 D：审计日志（衔接 eu-ai-act 三件套）
qm "everything it does is audited" + EU AI Act 审计日志要求：
- 每个 profile 记录 `scope + 动作 + 时间戳 + 审批人` 到 `.learnings/audit/`
- 对外产品（未来）直接导出为合规日志

---

## 4️⃣ 实施路径（P1 → P3）

| 阶段 | 动作 | 工作量 |
|:---:|------|:---:|
| **P1（现在）** | 本笔记落地 + 确认 Hermes profile 切换流程（`hermes profile` 命令） | 0.5h |
| **P2** | 闲鱼接单试点：新建 client-XX profile，验证上下文隔离 | 1h |
| **P3** | 设计 Skill scope 字段 + 安全三档配置模板 | 待评估 |

## 5️⃣ 验证方式

1. ✅ `hermes profile list` 已确认多 profile 机制（2026-08-02 实测：仅 default，支持扩展）
2. ✅ **P2 试点验证通过（2026-08-02）**：
   - `hermes profile create client-1 --description "..."` 创建成功（69 技能同步，独立目录）
   - client-1 有独立 `memories/` `sessions/` `cron/` `skills/` `workspace/`
   - 写入假数据"客户 A 论文需求"到 client-1/memories/MEMORY.md → **default 全局 MEMORY.md 0 匹配** = 文件级隔离 ✅
   - ⚠️ 注意：跨 profile 写记忆会触发 Hermes 软保护（cross_profile guard），需显式确认
3. ✅ **接单工作流 SOP 增加"按客户开 profile"步骤**（2026-08-08 确认已落实）：
   - `knowledge/Research/接单工作流-SOP.md` 已有 §1.4 客户隔离（Hermes profile）

---

## 关联
- [[eu-ai-act-2026-08-assessment]] — EU AI Act 三件套（审计/人工升级/透明度）
- [[AI-Agent]] — Hermes 架构总览
- [[github-trending-2026-08-02-study]] — qm 原始研究
- [[2026-08-02-eu-ai-act|EU AI Act 卡片]]

---
*2026-08-02 · 从 yc-software/qm 提炼 · 待实施 P2 试点验证*

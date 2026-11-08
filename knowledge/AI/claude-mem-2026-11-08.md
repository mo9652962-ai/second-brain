---
tags: [github, W45, ai, memory, context-engineering, agent, 记忆]
aliases: [claude-mem, Claude-Mem, cmem]
date: 2026-11-08
source: https://github.com/thedotmack/claude-mem
status: watching
---

# claude-mem — 给所有 agent 装一个「旁听生」记忆层

> W45 精选。**114,601★ / 359 contributors / 4,023 commits / v15.12.0（2026-11-07）/ Apache-2.0**。本周 trending 第 1（+7,482★/周）。实测真实性：高（活跃 release + 359 贡献者 + 4000+ commits，不是刷星）。
> 关键：repo 描述里点名支持 **Hermes**、OpenClaw、Codex、Gemini、Copilot；README 正文给了 Claude Code / Codex / Cursor / OpenCode / T3 Code / Antigravity / OMP / Pi / **DeepSeek Harness（`--ide dsh --dsh-profile tui`）** / Grok Bot / OpenClaw Gateway 的安装命令。

## 一句话定位

「你的 coding agent 每次开新会话都从零开始」——claude-mem 在它旁边跑**第二个 agent 做笔记**：把工具调用流压成短观察（observation），会话结束写总结，下次开会话先给一份**分层索引**，需要细节时才拉全文。

## 架构（四层，全部本地）

```
agent hooks（PreToolUse/PostToolUse/Stop/SessionEnd…）
        ↓ 每次工具调用 → 一条 shell-free 命令
本地 worker（Bun 管理的 HTTP 服务）
        ↓
observer agent（第二个模型：claude-mem 托管 / 自备 OpenRouter·Gemini key / 走 Anthropic 计划）
        ↓
存储：SQLite（sessions / observations / summaries）+ FTS5 关键词 + Chroma 向量
        ↓
下次 SessionStart 注入：分层索引（header 会标每层花多少 token）
```

- 数据落在 `~/.claude-mem`，云同步 opt-in
- 匿名遥测**默认开**，`npx claude-mem telemetry disable` 关掉
- `<private>…</private>` 包裹的内容永不入库
- 观察有 ID，可被引用/回查（web viewer `/viewer`，工作面板 `/`）

## 三级检索：省 token 的真正手法

| 步骤 | 工具 | 成本 |
|:--|:--|:--|
| 1 索引 | `search`（全文 + 类型/日期/项目过滤） | ~50-100 tokens/条 |
| 2 时间线 | `timeline`（围绕某条观察的前后上下文） | 中 |
| 3 取详情 | `get_observations(ids=[...])`（**必须批量**） | ~500-1,000 tokens/条 |

官方口径：**先过滤再取详情，约 10x token 节省**。另有 `smart_search / smart_outline / smart_unfold` 做代码导航，`save_memory` 主动记一条。

## 商业模式（值得注意的一面）

- 免费试用托管 observer 30 天 → 之后**回落到你自己的 Anthropic 计划**（不订阅也能用，只是花自己额度）
- 可选自带 OpenRouter / Gemini key
- TeamBrain 团队共享工作区（成员归属 + 关联发现，个人请求不共享）
- 一句话：**开源客户端 + 托管记忆服务**，标准的 open-core 变现

## 💎 可借鉴点

| 借鉴 | 映射到 sora 的现状 | 落地动作 |
|:--|:--|:--|
| 第二 agent 做笔记 | Hermes 有 mnemon（130 insights / 3,362 edges），但记的是「结论」，不记「过程」 | 高价值任务（接单交付、PCB、墨题迭代）结束时补一条「过程观察」：卡在哪、怎么绕过去 |
| 分层索引 + 按需展开 | 现在 recall 直接返回全文片段，token 花得粗 | 检索分两跳：先拿 ID + 一句话摘要，确认相关再取全文 |
| ~10x token 节省的量化口径 | 与 [[knowledge/AI/dsh-superagent-2026-11-08|dsh 的 Inline & Spill]] 同源 | 长任务上下文做「内联短的、落盘长的」 |
| `<private>` 标签 | sora 的隐私红线（学校/考研/路径/凭据绝不上网） | 在写记忆/生成报告前，先扫一遍 `<private>` 段并剔除 |
| 观察 ID 可引用 | 周报里现在引用靠文件名 | 以后关键结论带「观察 ID / 文件行号」，可回查 |
| 遥测默认开的坑 | 任何 agent 工具默认开遥测 | 装新工具第一步：`telemetry disable` / 检查上报端点（NOIR 正好是查这个的，见 [[knowledge/Security/noir-android-privacy-audit-2026-11-08]]） |

## 与 Hermes 的关系（判断）

- **观察**：repo 描述点名 Hermes；README 正文给出 dsh 与 OpenClaw 的专用安装参数，**没有** Hermes 专用 `--ide` 值。
- **推断**：Hermes 大概率走「通用 hook + MCP」路径接入（README 的 worker runtime / MCP 三工具是通用的），不是一等公民适配。
- **未知**：没在 Hermes 上实测过；若要试，先用 `--provider` 跳过账号交互，观察是否真能捕获 Hermes 的会话事件。
- **结论**：**不装**。Hermes 已有 mnemon + skills + memory 三层，再叠一个记忆层只会造成「记忆打架」（参见共装技能冲突那期）。**抄机制不装工具**。

## 评价

| 维度 | 判断 |
|:--|:--|
| 技术含金量 | ★★★★☆（架构朴素但工程完整：hooks→worker→observer→SQLite+FTS5+Chroma） |
| 可迁移性 | ★★★★★（分层索引 / 按需展开 / 私有标签三条都能立刻用） |
| 风险 | 遥测默认开、observer 需付费或吃自己额度、与现有记忆体系重叠 |
| 建议 | 只吸收检索分层与 `<private>` 约定；不安装 |

---
*W45 · 2026-11-08 · 观察：star/commits/contributors/releases/README 实读；推断：Hermes 接入路径；未知：未实测捕获效果*

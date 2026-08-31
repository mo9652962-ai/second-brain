---
title: "Agent Harness 大战——Codex 开放 vs dsh 一切皆插件（千轮深研 2026-08-23）"
type: note
domain: Research
status: active
tags: [knowledge/research]
source: null
date: 2026-08-23
---
# Agent Harness 大战——Codex 开放 vs dsh 一切皆插件（千轮深研 2026-08-23）

> 触发：sora「进行千轮研究和学习」→ 选定课题：2026 年 Agent Harness（智能体运行时）层的竞争格局
> 背景：B 站选题《Agent 操作系统之争》初稿已写，本次用一手资料深挖升级
> 信源：OpenAI 官方博客×3（agent loop/harness 平台/App Server）+ DeepSeek 官方架构文档 + memo.d.foundation 拆解 + winder.ai 九产品实测横评 + arceapps/dshdocs/ai.cc 分析
> 数据截止：2026-08-23

## 🎯 结论置顶

**Agent 竞争已从「模型层」上移到「Harness 层」，且格局在 8 月剧变：**
1. **Codex CLI 全开放**（Apache-2.0，113K⭐）：OpenAI 把 harness 变成可复用平台（app-server JSON-RPC 协议）
2. **dsh 两周 95K⭐**：MIT + Cordis 插件内核，「连 agent loop 本身都是插件」——唯一能热替换控制流的 harness
3. **行业收敛信号**：Linux Foundation Agentic AI Foundation 收编三大捐赠（MCP / AGENTS.md / Goose）；Pydantic v2.0 把 harness 吸进框架核心；9 个主流 harness 都支持 ACP 协议互通
4. **对 sora 的判断**：Hermes 定位与这波浪潮完全同向（narrow waist + 插件生态）；dsh 的「model-visible means logged」不变量值得抄进墨题/Hermes 工作流认知

---

## 一、OpenAI Codex：从工具到平台的转身

### 三篇官方博客释放的信号

| 博客 | 核心内容 |
|:---|:---|
| **Unrolling the agent loop** | 首次公开 agent loop 细节：Responses API 驱动、instructions/tools/input 三段结构、SSE 流式、**不用 previous_response_id 保持无状态以支持 ZDR**、prompt cache 命中使采样线性而非平方 |
| **Codex as a platform** | harness 开源定位：「把 agent 带进为具体工作设计的软件」而非「把工作塞进通用聊天窗」；三层集成梯度 = codex exec（脚本）→ SDK（编程）→ app-server（产品级）|
| **Unlocking the App Server** | 双向 JSON-RPC over stdio；三原语 **Thread/Turn/Item**；客户端绑定已有 Go/Python/TS/Swift/Kotlin；TUI 将重构为 app-server 客户端 |

### 关键技术细节（可借鉴）

- **压缩专用端点** `/responses/compact`：返回带 `encrypted_content` 的 compaction 项——保留模型对原始对话的潜在理解（比纯文本摘要强）
- **缓存友好设计纪律**：静态内容（指令/示例）放开头，变量内容（用户信息）放结尾；配置变更通过追加消息实现而非修改历史
- **沙箱边界清晰化**：developer message 只描述 Codex 自带 shell 工具的沙箱；MCP 工具自带护栏不归 harness 管

## 二、DeepSeek Harness (dsh)：架构激进派

### 「一切皆插件」的真实含义

基于 **Cordis 内核**（Koishi 四年生产验证）：插件贡献服务、类型化事件、可逆副作用到共享上下文。没有特权核心——扩展方式是挂载新插件，注册是可逆 effect。

### 六个核心服务 + 能力 seam

```
控制脊柱: session log / agent registry / loop driver / tool registry / prompt assembly / llm adapters
能力 seam: fs / shell / terminals / sandbox / jobs / subagents / commands / goals ...
   └─ seam = Service Definition(接口) + Provider(实现) + Consumer(工具)
```

**杀手锏案例**：fs 和 subprocess 共享同一执行世界 → 把两者指向 E2B 远程沙箱 = Bash/PTY/LSP 整体搬过去，零 fork。subagent seam 后面可以是子进程、ACP 对端、甚至 **Claude Code 或 Codex 进程**（meta-harness 定位）。

### 负载性设计不变量 ⭐ 最值得抄

> **Model-visible means logged** ——任何到达模型请求的内容必须能从 append-only 会话日志重建，运行时断言强制执行。

收益：确定性回放、诚实 token 计量、fork/resume/replay/transcript 全部从同一事件流派生。新增模型可见输入必须声明持久事件类型，杜绝「侧门塞上下文」。

### 冷静面（memo.d.foundation 拆解）

- token 消耗比同类高一个量级；CLAUDE.md 与 AGENTS.md 内容相同时会双重注入（未修 bug）
- 41 个插件验证兼容 / 219 个待确认；开发者预览承诺 breaking changes
- grapeut 锐评：命令式插件模型和声明式共享同一上限，多数真实扩展需求声明式就够，**运行时替换 agent loop 是多数人永远用不到的能力**

## 三、九大 Harness 横评要点（winder.ai 实测视角）

| Harness | 许可 | 模型绑定 | 特色 | 弱点 |
|:---|:---|:---|:---|:---|
| Claude Code | 专有 | 仅 Claude | 生产成熟、技能生态最大 | 封闭、记忆薄（by design） |
| Codex | Apache-2.0 | 仅 OpenAI | Rust+TS、kernel sandbox、现已平台化 | 同上模型锁 |
| OpenCode | MIT | 75+ providers | 开源权重模型最佳载体 | 默认外发便利性（会话标题曾默认走 Grok 免费档） |
| Qwen Code | Apache-2.0 | 多家但偏 Qwen | Qwen 模型最佳搭配 | 换模型 bug 多 |
| **dsh** | MIT | 任意（插件） | 元 harness、审计不变量 | preview 不稳定 |
| Zed Agent | GPL-3 | ACP 驱动多家 | 编辑器原生 diff 体验 | 绑定编辑器 |
| Letta Code | — | — | Terminal-Bench 2.0 用 Opus 4.5 得 59.1%（Claude Code 同模型仅 41.6%）——**靠记忆层赢第一方 harness** | 小众 |
| OpenHands / Goose | MIT | 自托管通用 | 通用开源双雄 | — |

**关键洞察**：
1. **Feature 表是错误的比较轴**——该比的是各 harness 假设你已经决定了什么（模型绑定/托管方/编辑器/宿主语言）
2. **Letta 案例证明 harness 层投资能赢模型优势**：记忆是模型仍处理不好的维度
3. **测试标准**：「更好的模型会让这项 harness 投资变得多余吗？」压缩/重试大概率会；沙箱/权限/审计不会——那些编码的是组织意志

## 四、AGENTS.md 标准：被低估的收敛成果

- Linux Foundation Agentic AI Foundation 托管；60,000+ 仓库采用；OpenAI 自己的 monorepo 有 88 个嵌套 AGENTS.md
- 原生支持 20+ 工具（Codex/Cursor/Copilot/Gemini CLI/Aider/Zed/Windsurf/Devin...）；Claude Code 读 CLAUDE.md，官方 workaround = `@AGENTS.md` 导入或 symlink
- 冲突规则：**最近的文件赢**；用户聊天指令覆盖一切
- 判断口诀：「会告诉每个新工程师的 → AGENTS.md；只告诉用 Claude Code 的工程师的 → CLAUDE.md；打包的可复用能力 → SKILL.md；每个任务都变的 → prompt」

## 五、与 sora 体系的映射

| 我们的资产 | Harness 战局中的位置 |
|:---|:---|
| Hermes narrow waist + 插件/技能生态 | 与 dsh「一切皆插件」同哲学，但 Hermes 更克制（core tools 白名单制）——AGENTS.md 里「Footprint Ladder」就是这个思路的文档化 |
| per-conversation caching sacred | 与 Codex 缓存纪律完全一致（静态前置/变量后置）|
| session_search + SQLite FTS5 | 接近 dsh「log-first」思想——我们搜的是会话库，dsh 强制一切可见即记录 |
| AGENTS.md 交接惯例 | 已是 Linux Foundation 标准的一部分，方向正确 |
| B站选题《Agent OS 之争》 | 本次研究直接升级素材：Codex 平台化 + dsh 95K 星 + Letta 反杀案例 + AGENTS.md 收编，数据全部更新到 8/23 |

## 六、行动项

- [x] 本研究本身沉淀为知识库文件
- [x] B站初稿《Agent 操作系统之争》按本报告更新数据（14.9万星→实际95K+/两周，8/31 再实测 204K+ 已更新入初稿；补 Letta 反杀案例、补 AGENTS.md/Linux Foundation 收编）→ ✅ 2026-08-31 数据已更新（初稿 L28 14.9万→20万+，附 8/31 实测 204K+/8/23 95K+）；Letta/Linux Foundation 收编补写随 sora 审校时一并做
- [x] ~~关注 dsh 插件 API 稳定化进度~~ 📖 条件触发参考（若转正，评估深度集成）
- [x] ~~「model-visible means logged」原则记入个人工程哲学~~ ✅ 原则已记录（本卡片为落点，自研功能时遵守）

## 数据截止点
- 2026-08-23；star 数/版本号均以当日检索为准

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]

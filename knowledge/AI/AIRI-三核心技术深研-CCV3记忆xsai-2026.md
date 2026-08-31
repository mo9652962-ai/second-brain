---
title: "AIRI 三核心技术深研：CCV3 色卡体系 / 记忆设计 / xsai 生态"
type: note
domain: AI
status: active
tags: [knowledge/ai]
source: null
---
# AIRI 三核心技术深研：CCV3 色卡体系 / 记忆设计 / xsai 生态

> 来源：抖音 @代码侦探《属于你的开源AI角色 AIRI》→ GitHub moeru-ai/airi（⭐44.8k, MIT）
> 研究：k · 2026-08-23 · 基于本地 clone（D:\airi）源码实证

## 结论置顶

AIRI 的三大技术点（CCV3 角色卡 / DuckDB WASM 记忆 / xsai 多提供商）**均与我们现有体系互补而非竞争**：CCV3 可借鉴进 SOUL.md 人设方法论；DuckDB 记忆验证了「浏览器端本地记忆」可行性（我们 TencentDB 是服务端，正好互补）；xsai 的 56-provider adapter 模式是墨题多模型接入的现成参考。

---

## 一、CCV3 色卡体系（Character Card V3 + AIRI Extension）

### 1.1 色卡是什么
CCV3 = AI 角色卡行业标准格式（`chara_card_v3`），AIRI 用它定义「角色灵魂」。AIRI Card 是 zip 包（manifest.json + card.json）。

### 1.2 核心字段（源码 packages/ccc/src/define/card.ts + 官方模板）

```json
{
  "spec": "chara_card_v3",
  "spec_version": "3.0",
  "data": {
    "name": "角色名",
    "nickname": "昵称",
    "description": "角色是谁（短描述）",
    "personality": "性格（好奇、温暖、俏皮…）",
    "scenario": "场景设定（初次见面…）",
    "first_mes": "开场白",
    "alternate_greetings": ["替代开场白..."],
    "creator_notes": "创作者备注",
    "character_version": "1.0.0",
    "system_prompt": "系统提示词",
    "post_history_instructions": "对话后指令",
    "extensions": { "airi": { ... } }
  }
}
```

### 1.3 AIRI Extension（模块化配置核心——源码 packages/stage-ui/src/types/airiCard.ts）

```typescript
interface AiriExtension {
  modules: {
    consciousness: { provider, model }        // 意识=对话 LLM
    vision:       { provider, model }          // 视觉
    speech:       { provider, model, voice_id, pitch?, rate?, ssml?, language? }  // 语音
    vrm?:         { source, file?, url? }      // 3D 形象
    live2d?:      { source, file?, url? }      // 2D 形象
    artistry?:    { enabled, provider, promptPrefix, ... }  // 图像生成
  }
  agents: Record<string, { prompt, enabled? }>  // 行为智能体：minecraft/discord/twitter 等
}
```

### 1.4 设计理念：三层拆分

| 层 | 内容 | 类比 |
|:---|:---|:---|
| **人格核心** | name/personality/system_prompt/scenario | = 我们的 SOUL.md（身份/信念/声音） |
| **模块配置** | consciousness/speech/vision/vrm 各用什么模型 | = 我们的模型分配（小任务 Qwen/复杂云端） |
| **行为智能体** | agents：不同平台/场景各一套 prompt | = 我们的场景切换（正事/闲聊/情绪/忙） |

### 1.5 与 SOUL.md 对比 + 可借鉴点

| 维度 | AIRI CCV3 | 我们 SOUL.md | 借鉴 |
|:---|:---|:---|:---|
| 格式 | JSON 卡片（可打包分享/导入） | Markdown 文件 | **可加「导出 CCV3」兼容** |
| 人格 | 字段固定（personality/scenario/first_mes） | 自由文本（身份/信念/支柱+矛盾） | 我们更丰富（有张力） |
| 模块 | 每个能力显式配 provider/model | 隐含在配置里 | **可形式化「模块段」** |
| 行为 | agents 字典（平台→prompt） | 场景×行为表（文字） | **agents 化：场景=agent** |
| 记忆 | DuckDB WASM | MEMORY.md + TencentDB | 互补 |

**可落地建议**：
1. SOUL.md 增加「模块配置」段（consciousness=当前模型/语音偏好）——让人格文件可移植
2. 场景切换表形式化成 agents 结构（正事=agent_professional，闲聊=agent_casual）
3. 若做 AI 角色产品（sora 的 B 站方向），CCV3 是行业互通格式——导出/导入兼容有价值

---

## 二、记忆设计（DuckDB WASM / pglite 浏览器端）

### 2.1 方案（源码 packages/stage-ui/src/composables/use-duck-db.ts + database/storage.ts）

- **DuckDB WASM**（@proj-airi/drizzle-duckdb-wasm）：浏览器内跑 SQL，**原生支持向量列** `vec FLOAT[768]`——内置向量检索（记忆语义搜索）
- **pglite**：PostgreSQL WASM 备选
- **IndexedDB**（unstorage）：持久化（local 挂载点 + outbox 同步队列）
- 未来：**Memory Alaya**（受佛教阿赖耶识启发的长期记忆层，WIP）

### 2.2 设计特点

- **数据不出浏览器**：纯客户端，隐私第一
- **向量原生**：DuckDB 直接存 embedding 列——不需要单独向量数据库
- **零部署**：WASM 加载即用

### 2.3 与我们 TencentDB 对比

| 维度 | AIRI（浏览器端） | TencentDB（我们，服务端） |
|:---|:---|:---|
| 部署 | 纯前端 WASM | 本地 Gateway 服务（8420） |
| 数据 | 本机浏览器（用户隐私） | 本地磁盘（多 Agent 共享） |
| 共享 | 单用户单浏览器 | **多 Agent（k/WorkBuddy/dsh）共享** |
| 向量 | DuckDB 原生 vec | BM25 关键词（embedding 未开） |
| 分层 | 记忆池（未来 Alaya 分层） | L0-L3 金字塔（已有） |

**互补结论**：
- **多 Agent 协作记忆** → 用我们的 TencentDB（服务端共享）
- **单用户隐私记忆**（如墨题用户自己的学习记忆）→ 借鉴 AIRI 的 DuckDB WASM 方案（浏览器端零部署 + 向量）

---

## 三、xsai 生态（轻量 AI SDK + 56 providers + unspeech 语音）

### 3.1 架构（源码 packages/stage-ui/src/libs/providers/）

- `@xsai-ext/providers`：统一抽象，**56 个 provider adapter**（DeepSeek/OpenAI/Anthropic/Gemini/Groq/SiliconFlow/腾讯云/阿里云/智谱/百川/MiniMax/Moonshot/302-ai/aihubmix...）
- 每个 provider = 一个 adapter 文件（zod schema + create + validators）——**极简注册模式**
- DeepSeek adapter 示例：`createDeepSeek` + 配置 schema（apiKey/baseUrl/thinkingMode）
- unspeech：语音统一端点（TTS/STT 类 LiteLLM）

### 3.2 墨题接入价值

| 场景 | 现在（墨题） | xsai 模式 |
|:---|:---|:---|
| 多模型（精讲/批改/口语） | llm-direct.ts 手写多端 | 56 adapter 统一抽象 |
| 新 provider 接入 | 手写 SDK 调用 | 写一个 adapter 文件 |
| 语音（口语评测） | 自建 | unspeech 统一端点 |

**借鉴**：墨题的 `llm-direct.ts` 已有多端 AI 直连（记忆里有）——xsai 的「provider adapter + zod schema + validators」注册模式可以重构它：每个模型一个 adapter，统一调用层。

---

## 附：AIRI 其他值得关注的点

- **游戏代理**（Minecraft Mineflayer / Factorio）：AI 真·玩游戏——B 站内容选题素材
- **Web 技术栈**（WebGPU/WebAudio/WASM）：数字形象渲染全浏览器方案
- **Sub-projects**：xsai / unspeech / webai-realtime-voice-chat（VAD+STT+LLM+TTS 完整示例）等十几个独立仓库
- **本地推理**（WebGPU + candle CUDA/Metal）：未来本地模型

## 参考

- 仓库：D:\airi（本地 clone，5199 文件）
- 官方文档：airi.moeru.ai/docs
- 角色卡模板：docs/content/en/docs/manual/tamagotchi/character-card-template.md

---
> 🗺️ 属于 [[MOC-Inbox]] · [[Home|🏠 Home]]

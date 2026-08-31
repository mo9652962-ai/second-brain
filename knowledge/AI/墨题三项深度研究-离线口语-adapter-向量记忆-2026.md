---
title: "墨题三项深度研究：离线口语 / 多模型 adapter / 本地向量记忆"
type: note
domain: AI
status: active
tags: [knowledge/ai]
source: null
---
# 墨题三项深度研究：离线口语 / 多模型 adapter / 本地向量记忆

> 研究：k · 2026-08-23 · 源码实证（本地 clone：D:\xsai-transformers / D:\xsai / D:\duckdb-wasm / D:\airi）
> 目标：墨题（Vue3 + Capacitor 手机端）三项 AI 能力的集成可行性

## 结论置顶

三项全部**可行**，且技术栈与墨题前端（Vue3 + TS + Vite + Capacitor）完全兼容：

| 项 | 技术 | 可行性 | 手机端注意 |
|:--|:---|:---|:---|
| 口语全离线 | xsai-transformers 浏览器 Whisper | ✅ 高 | WebGPU（Android Chrome 支持）→ 快；无 WebGPU 降级 WASM → 慢 |
| 多模型重构 | xsai adapter 模式 | ✅ 高 | 纯代码重构，无运行时风险 |
| 本地向量记忆 | duckdb-wasm FLOAT[] | ✅ 中高 | WASM 体积 ~50MB，首次加载慢；需 embedding 模型 |

---

## 一、xsai-transformers 浏览器 Whisper（口语全离线）

### 原理（源码 D:\xsai-transformers\packages\transcription）

```
音频(base64/WAV) → Web Worker
  → @huggingface/transformers pipeline('automatic-speech-recognition')
  → 自动检测: WebGPU 支持 ? webgpu : wasm
  → 转写文本
```

### 关键实现（worker/index.ts）

| 点 | 实现 |
|:---|:---|
| 设备选择 | `isWebGPUSupported() ? 'webgpu' : 'wasm'`（自动降级） |
| 输入处理 | base64 → 自动剥 WAV 44 字节头 → Int16 → Float32(-1,1) |
| 模型 | `onnx-community/whisper-*`（HuggingFace ONNX） |
| 输出 | `MAX_NEW_TOKENS = 64`（控制回复长度） |

### 墨题集成方案

```bash
npm i xsai-transformers @xsai/generate-transcription
```

```ts
// 口语评测：录音段 → 浏览器 Whisper（零服务器 ASR）
import { createTranscriptionProvider } from '@xsai-transformers/transcription'
import transcriptionWorkerURL from '@xsai-transformers/transcription/worker?worker&url'
import { generateTranscription } from '@xsai/generate-transcription'

const transformers = createTranscriptionProvider({
  baseURL: `xsai-transformers:///?worker-url=${transcriptionWorkerURL}`
})
const { text } = await generateTranscription({
  ...transformers.transcribe('onnx-community/whisper-tiny'),  // tiny 手机端快
  file: wavBlob
})
```

### 可行性评估

| 维度 | 评估 |
|:---|:---|
| **精度** | whisper-large-v3-turbo（服务器级）→ 浏览器端同样模型可选 |
| **手机端** | Android Chrome 支持 WebGPU（2024+）；旧 WebView 降级 WASM（慢但可用） |
| **体积** | 模型 ONNX：tiny ~75MB / base ~145MB（首次下载，可缓存）——**手机端推荐 tiny/base** |
| **隐私** | 音频不出设备（离线） |
| **与现有 VAD 衔接** | VAD speech-ready 的 Float32Array → toWav → 直接喂 transcription ✅ |

**结论**：✅ 可行。推荐 **whisper-tiny/base**（手机端速度），VAD 切好的语音段直接转写，**口语评测全链路离线**。

---

## 二、xsai adapter 模式（墨题多模型重构）

### 模式（源码 D:\airi\packages\stage-ui\src\libs\providers）

56 个 provider 目录（302-ai/aihubmix/anthropic/deepseek/...），每个 = 一个 index.ts：

```ts
// 1. zod schema 定义配置
const deepSeekConfigSchema = z.object({
  apiKey: z.string('API Key'),
  baseUrl: z.string('Base URL').optional().default('https://api.deepseek.com/'),
  thinkingMode: z.enum(['auto', 'disable', 'enable']).default('auto'),
})

// 2. create 统一创建（@xsai-ext/providers/create）
const create = createDeepSeek

// 3. validators 校验
const validators = createOpenAICompatibleValidators()

// 4. defineProvider 注册
export const providerDeepSeek = defineProvider<DeepSeekConfig>({
  id: 'deepseek', order: 4, ... })
```

### 墨题重构方案（llm-direct.ts）

墨题现有 `llm-direct.ts`（记忆：v9.29 手机端 AI 直连：精讲/作文/口语离线可用 + IDB 缓存）——**不必引入 xsai 全套**，借鉴**模式**：

```
现结构: 手写各家调用（可能 switch/if 分 provider）
重构为: 
  providers/
    deepseek.ts    (schema + chat_completion + validators)
    siliconflow.ts (schema + chat_completion + validators)
    fangzhou.ts    (schema + chat_completion + validators)
  registry.ts      (defineProvider + 按 id 路由)
  index.ts         (统一 chat() 入口)
```

| 收益 | 说明 |
|:---|:---|
| 新 provider 接入 = 加一个文件 | 不再改调用层 |
| 配置校验统一 | zod schema 一处定义 |
| 模型/能力矩阵统一 | 每 provider 声明支持的模型+能力（精讲/批改/口语） |

### 可行性评估

✅ 高。纯前端 TS 重构，无运行时风险；墨题已有 3 个 provider（DeepSeek/硅基流动/方舟）+ 可能的中转——adapter 化后各加一个文件。

---

## 三、duckdb-wasm 本地向量记忆（错题语义检索）

### 原理（源码 D:\duckdb-wasm + AIRI use-duck-db.ts）

```ts
// AIRI 记忆表（768 维 embedding）
await db.execute(`CREATE TABLE IF NOT EXISTS memory_test (vec FLOAT[768]);`)

// 测试实证：FLOAT[26880] 也支持
await db.execute('CREATE TABLE vector_test_table (v FLOAT[26880], v2 text)')
```

- **DuckDB 原生数组列** `FLOAT[N]` + `array_distance`/`array_cosine_similarity` = **无需单独向量库**
- Drizzle ORM 驱动：`@proj-airi/drizzle-duckdb-wasm`
- 持久化：IndexedDB（unstorage/OPFS）

### 墨题集成方案（错题/单词语义检索）

```bash
npm i @proj-airi/drizzle-duckdb-wasm
# vite.config.ts 加 optimizeDeps.exclude（README 明确要求，Vite bug 规避）
```

```ts
import { drizzle } from '@proj-airi/drizzle-duckdb-wasm'

const db = drizzle('duckdb-wasm://?bundles=import-url', { schema })
// 错题表: id, question_text, embedding FLOAT[768]
// 检索: WHERE array_cosine_similarity(embedding, ?) > 0.8 ORDER BY 相似度
```

### 可行性评估

| 维度 | 评估 |
|:---|:---|
| 向量检索 | ✅ DuckDB 原生（cosine/distance） |
| embedding 来源 | ❓ 需 embedding 模型（xsai-transformers embed 可浏览器跑 MiniLM；或服务器算好存本地） |
| 体积 | ⚠️ duckdb-wasm ~50MB WASM——手机端首次加载慢（可接受，本地记忆场景低频加载） |
| 持久化 | IndexedDB（手机 WebView 支持） |

### 结论

✅ 可行但**优先级低于前两项**——先解决「有没有数据」：墨题错题已存后端 SQLite，本地向量检索的价值 = 离线语义查重/相似题推荐。建议：**embedding 走服务器算（复用现有 AI 链路），duckdb-wasm 只做本地存储+检索**（省掉浏览器端 embedding 模型体积）。

---

## 落地路线（更新）

```
1. ✅ 已完成：VAD 自动切句（webai-realtime-voice-chat）
2. 🔥 推荐先做：口语全离线（xsai-transformers whisper-tiny/base）——独立功能，价值最直接
3. 📌 次优先：多模型 adapter 重构（xsai 模式借鉴）——等 llm-direct.ts 有改动需求时一起做
4. ⏳ 最后：本地向量记忆（duckdb-wasm）——embedding 服务器算 + 本地检索
```

## 参考（本地源码）

- D:\xsai-transformers（transcription worker 实现）
- D:\xsai（SDK 核心）
- D:\duckdb-wasm（FLOAT[] 向量实证）
- D:\airi（use-duck-db.ts / providers 56 adapter）
- 已落地：墨题 frontend/src/libs/vad/ + SpeakingView.vue

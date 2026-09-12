# 墨题 AI 化千轮研究报告：AI 精讲 / AI 批改 / AI 口语 技术路线

> 研究时间：2026-09-12 · 研究员：Hermes 千轮研究子代理（教育产品 AI 化）
> 产品背景：墨题 = sora 自研英语刷题机（GitHub 开源，源码 `D:/english-multiple-choice-practice-machine`），前端 Vue3+TS，后端 FastAPI/uvicorn（:8765），SQLite，已接入 DashScope text-embedding-v4 做 RAG；考研 C 端主推（Pro ¥98-128）；ESQ 题库（阅读/完形/作文）。
> 现状声明：据 `epm-ai-feature-rollout` 技能实录，三功能**已有 DeepSeek 单模型 MVP**（精讲 `deep-explain`、批改 `/api/essays/evaluate`、口语 `/api/speaking/*`，实测成本：单题精讲 ¥0.0034、批改单篇 ¥0.004、口语单轮 ¥0.001）。本报告给出**生产级升级路线**：模型分层选型、流式化、成本规模化模型、优先级与风险。

---

## 0. 结论置顶（TL;DR）

1. **模型主用 DeepSeek-V4-Flash 官方直连**（输入 ¥1/输出 ¥2 每百万 tokens，平峰），全部三功能默认跑 Flash 即可达标；批改高价值单提供可选的 V4-Pro 深度版（¥3/¥6）。通义 qwen-plus（¥0.8/¥2）与 SiliconFlow Step-3.5-Flash（¥0.7/¥2.1）做备胎降级。**不建议用 SiliconFlow 的 V4-Flash**（¥3/¥9，比官方贵 3 倍）——DeepSeek 官方直连是当前性价比最优解，且墨题用户集中在 19-23 点（谷段价，正好避开 9-12/14-18 高峰翻倍）。
2. **精讲/口语/批改的流式输出统一走 SSE**（`StreamingResponse` + `text/event-stream`，AsyncOpenAI + `stream=True`），已有多轮对话用 WebSocket。
3. **成本量级（@1000 DAU）：精讲 ~¥100-450/月、批改 ~¥30/月、口语 ~¥30-195/月，合计 <¥700/月**；核心降本手段 = 应用层缓存（question_explanations 表已有）+ DeepSeek 硬盘缓存（命中价 ¥0.02/M，约为未命中 1/50）。
4. **优先级：精讲（P0）> 批改（P1）> 口语（P2）**。精讲成本最低、覆盖最广（留存）；批改付费意愿最强、是 Pro ¥98-128 的变现支点；口语工程最重、需求集中在复试季（次年 2-4 月），后置但需在 12 月前开工。
5. **最大风险是批改的"评分漂移 + 幻觉纠错"**，解法 = 证据精确匹配（markups 必须是原文子串，后端校验）+ 分项锚点规则 + 校准集回归（MAE / ±0.5 命中率）。

---

## 1. 模型选型与定价（2026-09 实时价，¥/百万 tokens）

### 1.1 LLM 定价速查

| 模型 | 输入 | 输出 | 缓存命中 | 说明 / 来源 |
|---|---|---|---|---|
| **DeepSeek-V4-Flash**（官方直连） | **1** | **2** | **0.02** | 平峰价；高峰（北京 9-12/14-18 点）×2。上下文 1M，非思考+思考双模式，支持 JSON Output。`https://api-docs.deepseek.com/quick_start/pricing/` |
| DeepSeek-V4-Pro（官方直连） | **3** | **6** | 0.025 | 原价 ¥12/¥24 已永久降为 1/4（2.5 折转正）；高峰 ×2 |
| SiliconFlow `deepseek-ai/DeepSeek-V4-Flash` | 3（深夜 2-8 点 1.5） | 9（深夜 4.5） | 0.3 | 比官方贵 ~3 倍，仅作降级/免费额度过期兜底 `siliconflow.cn/pricing` |
| SiliconFlow `DeepSeek-V3.2` | 4 | 6 | 0.4 | 全开源旧版，质量上限低于 V4 |
| 通义 qwen-turbo（百炼） | 0.3 | 0.6（非思考）/3（思考） | — | 最便宜备胎，英语讲解能力弱一档 `help.aliyun.com/zh/model-studio/model-pricing` |
| 通义 qwen-plus（2025-12-01） | 0.8 | 2 | — | 均衡备胎（128K 内） |
| 通义 qwen3-max | 2.5（≤32K） | 10 | 有折扣 | 高质量备选，比 V4-Pro 贵 |
| SiliconFlow `Qwen3.5-35B-A3B` | 0.4 | 3.2 | — | MoE 小模型，<128K 档，性价比高但需实测英语教育场景 |
| SiliconFlow `Step-3.5-Flash` | 0.7 | 2.1 | — | 极低价备胎（阶跃） |
| 豆包 Doubao-Seed-2.1-turbo | 3 | 15 | 0.6 | 火山引擎，仅作参考 |
| OpenAI GPT-4o（对比） | ~$2.5 | ~$10 | — | 贵 10-20 倍，无国内直连，不推荐 |

要点：平峰价以 2026-08-16 峰谷计费上线后为准（官方邮件确认，见 `aitop100.cn/infomation/details/34153.html`）；DeepSeek 硬盘缓存默认开启、自动计费，命中价 = 未命中的 1/50，多轮对话/固定 system prompt/热门题二次请求天然命中（`api-docs.deepseek.com/zh-cn/guides/kv_cache`）。

### 1.2 语音（ASR/TTS）定价速查

| 服务 | 价格 | 备注 |
|---|---|---|
| SiliconFlow `FunAudioLLM/SenseVoiceSmall`（ASR） | **免费** | 免费模型 Rate Limits 固定（低 L0 档），文件 ≤50MB/≤1h，OpenAI 兼容 `/v1/audio/transcriptions`；中文+英语口音容错好 |
| SiliconFlow `Qwen3-ASR-1.7B`（ASR） | 免费 | 备选 |
| SiliconFlow `FunAudioLLM/CosyVoice2-0.5B`（TTS） | **¥0.05/千字符** | ≈ ¥0.015/分钟（按 300 字/分钟），流式 TTS 首包 ~150ms |
| 阿里 Paraformer 文件转写 | ¥0.00008/秒 | ≈ ¥0.005/分钟；每主账号每月免 10 小时（36000 秒）`help.aliyun.com/zh/isi/developer-reference/metering-and-billing` |
| 豆包流式语音识别 | ¥4.5/小时 | 免费 20 小时 `ai.volcengine.com/model` |
| 豆包语音合成 | ¥5/万字符 | 免费 5000 字符 |
| 豆包端到端实时语音模型（Realtime API） | 输入/输出各 ¥80/M tokens | QPM 60；端到端方案，¥≈$0.18/min 级别，贵且可控性差 |
| 浏览器端 Whisper（transformers.js，WebGPU/WASM 离线） | **0** | 已实测可行（墨题离线口语研究 2026-08-23），手机端推荐 whisper-tiny/base |

### 1.3 三功能选型结论

| 功能 | 主模型 | 备胎/降级 | 选型理由 |
|---|---|---|---|
| **AI 精讲** | DeepSeek-V4-Flash（非思考模式） | 通义 qwen-plus / Step-3.5-Flash | 讲解 = 中长文本生成，Flash 中文+英语均强、TTFT 快、¥1/¥2 最便宜的主力档；难题尾部（10%）可切 V4-Pro |
| **AI 批改** | DeepSeek-V4-Flash（JSON 结构化）+ 可选 V4-Pro 深度版 | qwen3-max | 评分质量由 JSON schema + 分项标准约束，不依赖模型玄学上限；分层模式对标 ielts.international（免费 DeepSeek / 付费 Gemini 深度分析） |
| **AI 口语** | DeepSeek-V4-Flash（非思考、低 max_tokens） | qwen-turbo（更低延迟） | 每轮回复需 <200 tokens 保证低延迟；ASR = SenseVoiceSmall（云免费）或浏览器 Whisper（离线），TTS = CosyVoice2，VAD = Silero（已集成），经典级联架构，不上端到端 Realtime |

口语架构决策依据（`yudonglee.me/voiceagent-explained` + `qubittool.com` 语音 Agent 延迟研究）：85% 生产语音 Agent 跑经典级联（VAD→ASR→LLM→TTS），串行预算 ~930ms、pipeline 后 ~600ms，成本 ~$0.05/min；端到端 Realtime 延迟 200-320ms 但贵 10 倍、黑盒不可控。墨题口语是"复试考官问答练习"场景（turn-taking 简单、无情感/笑声需求），经典级联是正确选择。

---

## 2. 输入输出设计

### 2.1 题型适配矩阵

| 题型 | 输入组装 | 输出 schema（JSON） |
|---|---|---|
| 阅读理解（整篇 + 5 题） | 文章 + 5 题题干/选项 + 官方解析 + 用户作答 | `{passage_analysis, question_explanations:[{q_idx, correct, why, option_breakdown:[4], trap_tags:[], long_sentence_parse}]}` |
| 完形填空 / 错题单题 | 题干 + 选项 + 解析 + 用户选项 | `{answer, explanation, option_breakdown, trap_tags, related_knowledge, example}` |
| 作文批改（小作文 10 分 / 大作文 20 分） | 题目要求 + 学生作文 + 五档评分标准 | `{total_score, dimension_scores:{content,structure,language,vocabulary}, comments, markups:[{original_snippet, correction, reason}], lexical_upgrades:[], model_essay}` |
| 口语（graduate_interview / daily_fluency / pronunciation 三场景） | 场景开场白（本地模板 0 成本）+ 历史 6 轮 + 本轮 user text | `{reply, grammar_corrections:[], native_upgrade, fluency_score}` |

要点（沿用现有 `gemini-design-rollout` 实录的约定）：
- 系统提示词固定写死"只输出合法 JSON，不含 Markdown 代码块标记"；输出 JSON 规范逐字段列出；后端 `parsed.setdefault(...)` 兜底所有必填字段。
- **缓存前缀设计**：system prompt 必须放在 messages[0] 且版本稳定（DeepSeek 硬盘缓存只匹配从第 0 个 token 起的前缀，改动任何历史消息即破坏缓存）；题目文本放 user 消息中段，同题二次请求整段命中。
- 精讲对"错题"自动触发：答错即调精讲（错题场景转化最高），正确题用户点按才生成。

### 2.2 流式输出（SSE）方案

```
Vue3 前端 (fetch + ReadableStream reader；POST SSE 不能用 EventSource)
   └─ FastAPI (uvicorn :8765)
        ├─ POST /api/questions/{id}/deep-explain-stream   (SSE)
        ├─ POST /api/essays/evaluate-stream               (SSE)
        ├─ POST /api/speaking/sessions/{id}/turns         (短轮询/WS，口语已有聊天室 WS 基建)
        └─ app.services.ai_client (AsyncOpenAI 统一入口 + provider 路由 + Model Pool 降级)
```

实现要点（证据：CommonTrace / theneuralbase / callsphere 的 FastAPI SSE 最佳实践）：
- `AsyncOpenAI(api_key, base_url, timeout=30)` —— **必须异步客户端**，同步 `OpenAI()` 在 async 函数里会阻塞事件循环、并发下超时。
- `stream = await client.chat.completions.create(..., stream=True)`，`async for chunk` 取 `chunk.choices[0].delta.content`。
- 返回 `StreamingResponse(generator, media_type="text/event-stream", headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no", "Connection": "keep-alive"})`。`X-Accel-Buffering: no` 防 Nginx 吞流。
- 事件帧：`data: {"type":"start","meta":{...}}\n\n` → 若干 `data: {"type":"delta","content":"..."}\n\n` → `data: {"type":"done","id":123,"cached":false}\n\n`；错误在 generator 内 `yield {"type":"error",...}`（SSE 发出 header 后无法再回 HTTP 错误码）。
- 生成同时全量文本落库（流式 + 持久化两不误），命中缓存时直接快流（一次性 delta）或返回 200 整包。
- 前端 `fetch` + `response.body.getReader()` + `TextDecoder`，按 `data: ` 行拆帧、`[DONE]`/`done` 事件收尾；断连自动重试并兜底非流式。

### 2.3 提示词策略

- **角色 + 任务 + 评分标准 + 样例 + 分步思考**：学术实证（《大语言模型作文评价反馈质量的实证分析》2026）表明「评分标准+样例+思维链指示」显著提升反馈质量；LLM 普遍短板在"引导思考"与"词汇同质化"，故提示词需显式要求追问式引导句、禁用模板套话。
- **批改防幻觉三条铁律**（借鉴 `AustinWang668/ielts-writing-scorer` + ielts.international）：
  1. 所有错误/批注必须精确匹配考生原文（markups.original_snippet 必须是原文字符串），后端校验子串存在，禁止"评语里编造原文没有的错误"。
  2. 分档锚点规则写死：如≥目标档必须有明确立场+两段论据+复杂句；字数不足 150 词仅内容维度降档；综合分 = 分项均值四舍五入到 0.5 档。
  3. 加校准提示（23 个官方样例的分数锚点），上线前用校准集回归测 MAE / ±0.5 命中率。
- **口语三明治反馈**：先肯定（2 句）→ 语法/表达纠错（≤3 条，附正确说法）→ 追问式引导下一轮；`max_tokens` 120-200，要求口语化、无 Markdown、短句，控制 TTS 时长。
- 所有生成入口带 `temperature=0.2` 左右 + `response_format={"type":"json_object"}`（OpenAI 兼容，DeepSeek/通义均支持）。

---

## 3. 成本测算

### 3.1 单次成本（DeepSeek-V4-Flash 平峰价，输入 ¥1/M、输出 ¥2/M）

| 功能 | 输入 tokens | 输出 tokens | 单次成本 | 缓存后 | 实测对照 |
|---|---|---|---|---|---|
| 精讲·单题（阅读/错题） | ~1200 | ~550 | **¥0.0023** | 硬盘缓存命中 ~¥0.0012；应用层缓存 0 | 实录 ¥0.0034（pro 档）✓ |
| 精讲·整篇阅读（文章+5题） | ~2000 | ~2500 | **¥0.007** | 同上 | — |
| 批改·大作文（150-200 词） | ~1750 | ~1500 | **¥0.0048** | 同题重批很少，靠 prompt 前缀缓存 | 实录 ¥0.004 ✓ |
| 批改·小作文（100 词） | ~1300 | ~1100 | **¥0.0035** | — | — |
| 口语·单轮 | ~600 | ~250 | **¥0.001** | 多轮对话天然命中历史前缀 | 实录 ¥0.001 ✓ |
| 口语·10 分钟会话（8-12 轮） | — | — | LLM ¥0.01 | — | — |

### 3.2 语音成本（10 分钟口语会话，用户说话约 2 分钟）

| 环节 | 方案 | 成本/会话 |
|---|---|---|
| ASR | 阿里 Paraformer（¥0.00008/s × 120s） | ¥0.0096 |
| ASR（更优） | SenseVoiceSmall（SiliconFlow 免费）/ 浏览器 Whisper 离线 | ¥0 |
| TTS | CosyVoice2（¥0.05/千字符 × ~900 字符） | ~¥0.045 |
| TTS 兜底 | 浏览器 speechSynthesis | ¥0 |
| **合计** | 云端链路 | **≈ ¥0.065/会话**（离线 ASR 则 ¥0.055） |

### 3.3 规模化模型（@1000 DAU 假设：人均每天刷 10 题、5% 错题触发精讲=50% 利用率；批改 20% 用户每周 1 篇；口语 10% 用户每天 1 个 10 分钟会话）

| 项 | 月调用量 | 单位成本 | 月成本 | 备注 |
|---|---|---|---|---|
| 精讲 | ~15 万次（缓存命中 ~40%） | 均值 ¥0.0015 | **¥225**（应用层缓存做足后可压到 ¥100 内） | 热门题第二次起 0 成本 |
| 批改 | 6000 篇 | ¥0.0048 | **¥30** | — |
| 口语 | 3000 会话 | ¥0.065 | **¥195**（离线 ASR 后 ¥165） | — |
| **合计** | | | **<¥500/月** | 对比：1000 DAU × 5% 转化 × Pro ¥98 ≈ ¥4900/月 收入，成本占比 <10%，毛利 >90% |

调度建议：DeepSeek 高峰（北京 9-12/14-18 点）价格 ×2，墨题批改/预生成等**非实时批量任务排到 19-23 点谷段**（恰是用户活跃窗口，双赢）；深夜可用后台批量预热精讲缓存（先生成热门题讲解落库，用户点开即缓存命中 0 成本）。

---

## 4. 实现优先级建议

| 优先级 | 功能 | 依据 | 本轮要做的事 |
|---|---|---|---|
| **P0** | AI 精讲 | 已 MVP、成本最低（缓存后趋零）、覆盖全部做题场景、错题自动触达 = 留存核心 | ① 流式化（SSE）；② 错题自动触发 + 整篇阅读模式；③ 应用层缓存落库（已有表）+ 批量预热；④ 难题尾部切 V4-Pro |
| **P1** | AI 批改 | 已 MVP、考研作文是**付费刚需**（市面单篇批改 5-20 元），Pro ¥98-128 的变现支点 | ① 流式化；② 证据精确校验（防幻觉）+ 校准集回归；③ 免费版（Flash 简评）/ Pro 版（深度批改 + 范文）分层；④ 批改历史 + 进步曲线 |
| **P2** | AI 口语 | 已 MVP（文本 + Web Speech）、工程最重、需求集中在复试季（次年 2-4 月） | ① 语音链路升级：SenseVoiceSmall / 浏览器 Whisper 离线 ASR + CosyVoice2 TTS + 打断；② 场景题库扩充；③ 12 月前开工，1 月底前上线抓复试季 |

商业节奏：9-12 月初试冲刺（精讲+批改跑量变现）→ 1 月开始口语复试产品预热 → 2-4 月复试季收割。

---

## 5. 技术风险与规避

| # | 风险 | 影响 | 规避方案 |
|---|---|---|---|
| 1 | **批改评分漂移 / 幻觉纠错**（编造原文没有的错误、分数忽高忽低） | 用户信任崩塌，付费转化归零 | markups 证据子串后端校验（不匹配即剔除并重试）；分项锚点规则；温度 ≤0.2；每周用 20-30 篇带教评分校准集回归（MAE、±0.5 命中率），劣化即回滚 prompt 版本 |
| 2 | **缓存失效**（DeepSeek 硬盘缓存只匹配全前缀；改 system prompt/历史消息即失效） | 成本回升 50 倍 | prompt 版本化管理（`prompt_version` 字段入库）；system prompt 放 messages[0] 且改版走灰度；应用层缓存（question_explanations 表）为主、硬盘缓存为辅，不依赖 100% 命中（官方明示"尽力而为"） |
| 3 | **流式中断**（SSE 断连、Nginx 缓冲、代理 kill 长连接） | 前端卡死/丢内容 | `X-Accel-Buffering: no`；`[DONE]` 哨兵 + 前端重连；生成落库，重连后从 DB 回放；兜底非流式整包 |
| 4 | **语音延迟超标**（串行 930ms+，用户感知"机器人慢"） | 口语体验差 | pipeline 重叠（ASR partial → 意图预判 → LLM 流式 → TTS 首包即播）；`max_tokens` 120-200；打断处理 150ms 内（取消 TTS 流 + abort LLM + 上下文追加"被打断"记录）；优先 p50 首音频响应 |
| 5 | **限流 429**（免费模型/低用量档 TPM 限制；SiliconFlow 免费模型固定限流、L0 档 <¥50/月） | 高峰期不可用 | DeepSeek 官方直连多 key 轮换 + 已有 Model Pool 多 provider 自动降级（403/429 降级机制已在墨题落地）；SenseVoice 免费 ASR 仅做兜底，主链路用 Paraformer 或离线 Whisper |
| 6 | **合规与数据安全**（作文含个人信息、未成年人、内容安全） | 法律/平台风险 | 作文/语音数据脱敏存储；不采集未成年信息（考研用户 21+ 为主，仍需提示）；AI 估分显著标注"非官方分数"；输出内容安全关键词过滤（复用墨题现有审核） |
| 7 | **定价波动**（峰谷计费 2026-08 上线、产品叠代降价） | 成本失控 | 预算熔断 + 用量监控（记录每请求 usage 与费用）；批量任务排谷段；多供应商比价脚本月度巡检 |
| 8 | **ASR 口音容错不足**（中式口音英语识别错误率） | 口语评分失真 | SenseVoice/whisper 对中式口音容忍度高（SenseVoice 覆盖中英多语）；v1 流利度/时长用启发式（本地四维汇总已实现），音素级逐音纠错后置（2027 路线） |

---

## 6. 证据来源

- DeepSeek 定价与峰谷计费：`https://api-docs.deepseek.com/quick_start/pricing/`、`https://www.aitop100.cn/infomation/details/34153.html`
- DeepSeek 上下文硬盘缓存：`https://api-docs.deepseek.com/zh-cn/guides/kv_cache`
- SiliconFlow 模型价格：`https://siliconflow.cn/pricing`；限流规则：`https://docs.siliconflow.cn/cn/userguide/rate-limits/rate-limit-and-upgradation`；ASR API：`https://docs.siliconflow.cn/cn/api-reference/audio/create-audio-transcriptions`
- 通义百炼定价：`https://help.aliyun.com/zh/model-studio/model-pricing`
- 阿里 Paraformer 计费：`https://help.aliyun.com/zh/isi/developer-reference/metering-and-billing`
- 豆包语音与 Realtime：`https://ai.volcengine.com/model`、`https://www.volcengine.com/product/doubao`
- FastAPI SSE 流式最佳实践：`https://www.commontrace.org/zh/trace/openai-streaming-chat-completions-with-fastapi-sse/`、`https://theneuralbase.com/ai-streaming/qna/fastapi-streamingresponse-for-llm/`
- 语音 Agent 架构与延迟预算：`https://yudonglee.me/voiceagent-explained/`、`https://qubittool.com/zh/blog/voice-conversation-ai-agent-latency-architecture`
- 作文自动评分方法学：`https://www.sciopen.com/local/article_pdf/10.3969/j.issn.1009-8097.2026.03.007.pdf`（大语言模型作文评价反馈质量实证）、`https://github.com/AustinWang668/ielts-writing-scorer`（证据精确匹配 + 校准集）、`https://www.ielts.international/zh/how-scoring-works`（分档锚点 + 分层模型）
- 墨题既有资产：`epm-ai-feature-rollout` 技能（MVP 落地实录、实测成本、Model Pool 降级）、`C:\Users\31954\.openclaw\workspace\knowledge\AI\墨题三项深度研究-离线口语-adapter-向量记忆-2026.md`（浏览器 Whisper 离线 ASR 实证）
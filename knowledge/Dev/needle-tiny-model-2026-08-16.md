---
tags: [on-device-ai, tiny-model, JAX, LoRA, 边缘AI, 硬件, W34]
aliases: [needle, cactus-needle]
date: 2026-08-16
source: https://github.com/cactus-compute/needle
status: watch
---

# Needle 2 — 14MB 端侧工具调用基础模型

> **简介**：Cactus Compute 出品，**14MB / 45M 参数**的端侧工具调用基础模型（手机/可穿戴/智能家居/机器人）。本周 6,159⭐ **+2,488/周**（Python，MIT，263 commits，活跃）。论文引用标题即定位：*Needle 2: A 45M-Parameter Foundation Tool-Calling Model for Tiny Devices*。

## 核心思路

1. **45M 参数做到工具调用**：`needle.Needle(weights=..., tools=[...])` → `agent.run("...")`——微型模型直接对话式调用工具，面向微型设备。
2. **全 JAX 训练 + 四步产品化管线**：
   - `needle finetune data.jsonl --epochs 10 --generate 300 --lora-rank 16`：LoRA 微调，`--generate` 先用 LLM（OpenRouter）合成更多训练样例
   - `needle build base.pkl --lora adapter.pkl --out my_needle.cact --bits 2`：合并 adapter + 量化（默认按 checkpoint 位图，可降 2-bit）
   - `needle download <you>/<model>/my_needle.cact`：HF 发布/拉取
   - 引擎 **weights-agnostic**：换权重不重新编译，`.cact` 直接跑
3. **OpenRouter 兼容网关**：训练数据合成走 `OPENROUTER_API_KEY`，也可 `OPENROUTER_URL` 指向任意 OpenAI 兼容网关。
4. **GPU 覆盖面**：NVIDIA CUDA / Apple Silicon metal extra 都能训。

## 精妙细节

- **llms.txt**：仓库自带 llms.txt 给 LLM 消费文档——agent 友好文档策略。
- **daily release workflow**：每日自动 release，版本迭代快。
- **离线导向**：README 强调 offline pointers，模型下载/部署均支持离线。

## 💎 可借鉴点（对 sora 最值）

1. **「合成数据 → 微调 → 量化打包」三步产品化**：`--generate N`（LLM 合成样例）→ LoRA 微调 → build 合并量化，这条管线 sora 可复用到自己的本地模型场景（如刷题机错因分类器、私有小模型定制）——不是只训模型，是把「训-打包-发布」做成 CLI。
2. **微型工具调用模型验证边缘方向**：45M 就能 tool calling——对 sora 的单片机/边缘 AI 兴趣（8051/ESP32 兴趣 + RTX4060 本地部署）是强信号：端侧 agent 不是科幻。可以关注后续与 llama.cpp / GGUF 生态的互通。
3. **weights-agnostic 引擎**：换权重不重编译——类似 GGUF 的思路，但更轻。若 sora 做硬件产品（PCB 接单升级成智能硬件），这种「模型即文件」模式是端侧部署的正确抽象。
4. **llms.txt 文档策略**：给 agent 消费的文档入口，sora 的项目（墨题等）可加一份 llms.txt。

## 综合评估

| 维度 | 评价 |
|:---|:---|
| 技术含金量 | ★★★★☆（45M 工具调用模型 + 完整微调/量化管线，论文背书）|
| 与 sora 工作流关联 | ★★★★☆（本地 LLM/边缘 AI/硬件兴趣强相关，但当前无 tiny device 部署需求）|
| 值得安装 | 🟡 关注——不装（无端侧部署场景），但「合成-微调-打包」管线方法论可沉淀 |
| 趋势判断 | 端侧模型走向「小到能进单片机」，工具调用是主卖点；2026 下半年边缘 agent 会继续升温 |

> 🗺️ 属于 [[MOC-Dev]] · [[Home|🏠 Home]] · 平行参考：`local-llm-inference`（本地推理）· `microcontroller-edge-ai` · `8051-embedded-dev`

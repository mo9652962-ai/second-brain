---
tags: [ai VTuber, 开源工具, 学习笔记, ai-agent]
aliases: [Airi, Project AIRI, アイリ]
date: 2026-07-22
source: https://github.com/moeru-ai/airi
status: learning
---

# AIRI (アイリ) — 开源 AI VTuber / 数字伙伴

> 来源: [moeru-ai/airi](https://github.com/moeru-ai/airi) | [中文文档](https://github.com/moeru-ai/airi/blob/main/docs/README.zh-CN.md)
> 学习时间: 2026-07-22
> 所属知识网络: [[knowledge-map]] | 相关: [[grok-build]] | [[mattpocock-skills]]

## 简介

Airi 是一个**自托管、开源的数字伙伴/AI VTuber**，受 [Neuro-sama](https://www.youtube.com/@Neurosama) 启发。目标是让你拥有自己的「数字生命」，随时陪伴聊天、玩游戏。

## 核心能力

| 模块 | 能力 |
|:---:|------|
| 🧠 大脑 | 支持 25+ LLM 供应商（OpenAI、Claude、DeepSeek、Qwen、Gemini、xAI、SiliconFlow...） |
| 👁️ 视觉 | 屏幕画面理解、Minecraft/Factorio 游戏画面识别 |
| 👂 听觉 | 浏览器麦克风输入、Discord 语音、客户端语音识别、说话检测 |
| 🗣️ 语音 | ElevenLabs、Azure TTS、OpenAI TTS、Kokoro 本地 TTS |
| 🦾 身体 | VRM 模型（含动画、眨眼、视线追踪）、Live2D 模型 |
| 🧠 记忆 | RAG 记忆系统、DuckDB WASM 嵌入式数据库 |
| 🎮 游戏 | **Minecraft**、**Factorio**、Kerbal Space Program、Helldivers 2 |

## 技术栈

- **前端**: Vue.js + TypeScript
- **图形**: WebGPU、Three.js、WebGL
- **音频**: WebAudio API
- **桌面**: Electron
- **移动**: Capacitor (PWA)
- **AI 推理**: WebGPU 本地推理（Transformers.js、ONNX Runtime）
- **本地加速**: NVIDIA CUDA、Apple Metal（通过 HuggingFace Candle）
- **构建**: pnpm monorepo

## 部署方式

| 方式 | 命令 |
|:---:|------|
| **Web 版** | `pnpm dev` |
| **桌面版** | `pnpm dev:tamagotchi`（Electron） |
| **macOS** | `brew install --cask airi` |
| **Windows** | `winget install MoeruAI.AIRI` 或 Scoop |
| **NixOS** | `nix run github:moeru-ai/airi` |
| **在线体验** | [airi.moeru.ai](https://airi.moeru.ai) |

## 版本信息

- 当前版本: v0.10.2
- 许可证: 未明确但仓库可用
- 生态组织: [@proj-airi](https://github.com/proj-airi)

## 子项目

| 项目 | 说明 |
|:----|------|
| [unspeech](https://github.com/moeru-ai/unspeech) | ASR/TTS 统一代理（类 LiteLLM） |
| [airi-factorio](https://github.com/moeru-ai/airi-factorio) | 让 Airi 玩 Factorio |
| [webai-realtime-voice-chat](https://github.com/proj-airi/webai-realtime-voice-chat) | ChatGPT 实时语音从零实现 |
| [awesome-ai-vtuber](https://github.com/proj-ari/awesome-ai-vtuber) | AI VTuber 项目精选列表 |

## 综合评估

| 维度 | 评价 |
|:---:|------|
| 适合做 skill | ❌ 是一个应用产品，不是 AI Agent 技能 |
| 当前成熟度 | 🟡 v0.10.2，仍在早期开发，活跃更新中 |
| 值得关注 | ✅ 自托管 AI 伙伴、支持 25+ 模型供应商、Minecraft/Factorio 游戏能力 |
| 与我（k）的关系 | 🤔 同类但不同方向：我是助手/生活管家，Airi 是 VTuber/数字伙伴 |

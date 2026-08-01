---
tags: [research, ai-daily, digest, llm, ocr, security]
created: 2026-08-01
status: absorbed
---

# AI 日报消化笔记（2026-07-27~31 热点）

> 来源：小黑盒 AI 日报 + 电商生图 TOP10 · 2026-08-01 验证 + 吸收

## 📊 高价值信号（按对我们的影响排序）

| # | 新闻 | 验证 | 决策 |
|:-:|------|:---:|:---:|
| 1 | **llama.cpp GGUF 兼容性提醒** | ✅ 真实（unsupported GGUF version 机制） | ✅ **更新 llama-cpp 技能**（新增 GGUF 兼容性检查章节） |
| 2 | **MOSS-OCR 0.3B 开源** | ✅ 真实（patsnap/Hiro-MOSS-OCR, Apache-2.0） | 🟡 存档按需参考（需 CUDA GPU） |
| 3 | **Kimi K3 开源** | ✅ 真实（2.8T MoE, 英伟达/AMD 双平台） | 🟡 关注（我们有 Kimi key） |
| 4 | **共享对话泄露** | ✅ 真实（ChatGPT/Claude 分享链接被 Google 收录） | ✅ **安全教训吸收到记忆** |
| 5 | 微软 MAI-Cyber-1-Flash | 🟡 未深验 | 🟡 参考（不搞安全） |
| 6 | Qoder 免费额度 | ⚠️ 活动 7/31 截止 | ❌ 已过期 |
| 7 | 电商生图 TOP10 | ✅ 工具列表 | 🟡 已有 ai-image-generation 覆盖 |

## 🔴 重点 1：MOSS-OCR（值得关注的开源 OCR）

**patsnap/Hiro-MOSS-OCR** 验证：
- 0.3B 参数（320.8M），从零训练 5000 万样本
- Apache-2.0，Python 3.12+，支持中/日/英
- 结构化输出：LaTeX（公式）/ HTML（表格）/ Markdown（文本）
- 基准：OmniDocBench v1.6 = 94.46（追平 MinerU 2.5 94.46）；**专利领域 93.49 反超**（MinerU 2.5 = 89.78，GLM-OCR = 91.33）
- 推理：CUDA Graph / vLLM（OpenAI 兼容）/ Transformers 快速调用
- 权重 1.35GB（FP32/BF16），HF: PatSnap/Hiro-MOSS-OCR-0.3B

**我们的判断**：0.3B 轻量 + 结构化公式/表格输出是杀手锏，但需 CUDA GPU。当前环境不满足 → **存档按需参考**。若未来接专利/论文公式提取类订单（闲鱼），这是首选模型。

## 🔴 重点 2：llama.cpp GGUF 兼容性（已落地）

2026-07-30 llama.cpp 改动后，**旧版 GGUF 必须重新生成**（模型序列化/运行时路径变化）。
- 已更新 `llama-cpp` 技能：新增「GGUF 兼容性检查」章节
- 含诊断流程（xxd 查版本）、错误速查表、预防措施

## 🔴 重点 3：共享对话泄露（安全教训）

**事件**：ChatGPT/Claude 共享对话页面被 Google 收录 → API 密钥、医疗咨询、商业计划、含住址简历曝光。
**本质**：不是黑客入侵，是分享链接默认可被搜索抓取（相关功能已被移除，但去索引仍在进行）。

**教训**：生成任何"共享链接"前必须检查：
1. 内容是否含敏感信息（密钥/个人信息/未公开计划）
2. 平台默认分享权限（是否可被搜索引擎收录）
3. 分享后定期检查是否被索引

## 🟡 其余信号（简要）

- **Kimi K3**：2.8T MoE 首个 3T 级开源，SGLang/Miles day-0 支持，百万级上下文，AIME 12h LoRA 43.3%→76.7%。我们有 Kimi key，可关注 API 上线。
- **MAI-Cyber-1-Flash**：微软首个网络安全模型，CyberGym 96%，目标自动处理 90% 常规漏洞检测。
- **OpenAI 43.5% 跨界工作**：岗位边界加速变化（营销×工程最交叉）——博主选题素材。
- **Google 86% 对话与工作无关**：AI 从生产力工具融入日常生活——博主选题素材。
- **AI 音乐 44%**：Deezer 称 44% 新上传是 AI 生成，Spotify 不标注——行业观察。
- **τ₀-VLA 机器人**：12 分钟连续自主操作，具身智能进展。

## 📄 产出
- llama-cpp 技能更新（GGUF 兼容性章节）
- 本笔记存档

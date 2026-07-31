---
tags: [research, ai-daily, digest]
created: 2026-07-31
status: absorbed
---

# AI 早报 7.29 消化笔记

> 来源：小黑盒早报 7.29 · 已提取与我们相关要点 + 验证

## 🔴 高相关（已落地）

### 1. MCP 新规范候选版（2026-07-28）
- 诞生以来最大升级：**无状态核心** + Extensions 框架 + MCP Apps（服务端渲染 UI）+ Tasks 转正
- 详见 `knowledge/Dev/mcp-spec-2026-07-28.md`
- ✅ 规则 #2 补充"新规范意识"（优先无状态实现）

### 2. LLM 购物代理隐蔽推销研究（arXiv 2604.04263）
- N=2012 预注册实验：LLM 主动说服让赞助商品选择率 22.4% → **61.2%**（近 3 倍）
- 标"Sponsored"标签不显著降低效果；隐藏意图时检测率 <10%
- 与 Princeton/UW 研究互相印证：23 模型中 18 个优先公司收入
- ✅ 规则 #17 升级：LLM 偏见范围从"评估宽松"扩展到"商业利益说服"

### 3. Gemini Managed Agents 升级（Google 官方）
- 默认模型 → Gemini 3.6 Flash；新增 **环境 Hooks**（pre/post tool call 拦截脚本）
- 新增 **预算控制** max_total_tokens（防失控循环）+ 定时触发器 + 免费额度
- 💡 与我们的成本护栏（ai-cost-guardrails 第 2 层任务熔断）**思路完全一致**——行业共识验证

## 🟡 中相关（存档关注）

### 4. Laguna XS 2.1 / S 2.1（Poolside）
- XS 2.1：33B-A3B MoE，SWE-bench Multilingual 63.1%（+5.4pp），专为本地智能体编码
- S 2.1：118B-A8B，Terminal-Bench 2.1 70.2%，号称比 DeepSeek V4 Flash 便宜
- OpenRouter 已上线：XS 2.1 $0.06/$0.12 per 1M tokens
- 💡 潜在本地模型选项（需 33B+ 显存），暂不切换（我们走 API 路线更稳）

### 5. DeepSeek 共享聊天页隐私风险
- 共享链接疑似被 Google 收录（Claude 类似问题也暴露过）
- ⚠️ 警示：**不要用共享功能分享敏感对话**；发布内容前检查 robots 索引
- 对我们的影响：知识库笔记不含敏感信息，风险低

### 6. OpenAI 语音转写模型 / Fish Audio 声音克隆
- GPT-Live-Transcribe（低延迟实时）+ GPT-Transcribe（异步批量）
- Fish Audio S2.1：5 秒克隆声音，成本为 ElevenLabs 1/6
- 💡 潜在：语音内容创作（B 站 AI 语音赛道），暂不行动

## ⚪ 低相关（背景情报）

- 安全：HAWK 后量子签名攻击 + 7 轮 AES 新攻击（Claude Mythos 多智能体协作）
- 资本：谷歌 capex 上调至 $205B（华尔街担忧）；SSI 与 AWS $410M 算力协议；英伟达投资 SSI $400M
- 治理：Dario Amodei 明确"不禁开源模型，主张 FAA 式强制测试"；1122 名员工联署放缓自动化
- 数学：AI 破解 FrontierMath 第二题（2-adic 绝对伽罗瓦群表示）
- 内容：亚马逊约两成自出版小说含大量 AI 文本（博主警示：内容同质化在加剧，差异化更值钱）

## 结论

- **2 项已落地**（MCP 规范 + 规则 #17 扩展），1 项验证行业共识（Gemini 预算控制 = 我们的成本护栏）
- 值得关注：MCP Apps 生态（未来 Hermes 可能支持）、Laguna 本地模型（有 33B+ 显存时）

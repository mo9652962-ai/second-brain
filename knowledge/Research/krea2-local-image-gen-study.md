---
tags: [research, github, article-study, image-generation, krea2, comfyui]
created: 2026-08-01
status: absorbed
source: 小黑盒《本地部署AI生成无审查内容（16）Krea2生图》
---

# Krea2 生图模型 — 研究笔记

> 来源：小黑盒教程（听白o 07-14）· 2026-08-01 验证 + 评估

## 模型验证（多源交叉 ✅）

**Krea 2 真实存在**（Krea AI 官方开源）：
- 官方仓库：github.com/krea-ai/krea-2 + huggingface.co/krea/Krea-2-Raw / Krea-2-Turbo
- ComfyUI 0.25.0+ 原生支持（无需自定义节点）
- 架构：Krea2 DiT 主模型 + Qwen3-VL 4B 文本编码器 + Qwen Image VAE
- 两版本：RAW（52 步/CFG 3.5，适合 LoRA 训练）+ Turbo（8 步/CFG 1.0，快速生成）

## int8-convrot 算法验证

**真实存在**（lilcheaty/Krea2-INT8-ConvRot + chfm 多量化版本）：
- ConvRot = Hadamard rotation 预旋转减少离群值 → INT8 量化精度接近无损（~GGUF-Q8 质量）
- **RTX 30xx 上 INT8 比 FP8 快**（Ampere 无 FP8 张量核加速），显存约 BF16 一半
- 40 系原生 FP8 支持但 int8-convrot 更快 20-50%
- 模型大小：INT8 ConvRot 14.1GB；FP8 12GB；BF16 24.76GB
- 各卡推荐：30xx→INT8 ConvRot / 40xx→FP8 或 INT8 / 50xx→NVFP4

## 我们的硬件评估

| 项 | 值 | 达标 |
|----|-----|:---:|
| GPU | RTX 4060 Laptop **8GB** | ✅（要求 6G） |
| 内存 | 16GB+ | ✅ |
| ComfyUI | ❌ 未安装 | 需装 |
| 模型 | ❌ 未下载 | 需下 14GB |

## 文章技术要点（已吸收）

1. **工作流**：Load Diffusion Model (W8A8) → CLIPLoader(type: krea2) → VAELoader → CLIPTextEncode → KSampler(8步/euler/simple/shift 1.15) → VAEDecode
2. **Conditioning 节点**：仅 Krea2 可用（增强提示词遵从度，针对 Krea2 层数设计）
3. **提示词**：支持自然语言 + 中文，越精细效果越好（镜头焦段/暗角/虚化/柔光都可写）
4. **跨次元**：Krea2 独特能力（现实+二次元同一画面，z-image/qwen/klein 做不到）
5. **生态**：社区活跃（LoRA/风格参考/生成滑块/扩展节点爆发式增长）

## 落地决策

| 选项 | 决策 | 理由 |
|------|:---:|------|
| 安装 ComfyUI + Krea2 | 🟡 待确认 | 硬件达标，但需 14GB 下载 + 环境搭建 |
| 存档技术要点 | ✅ 完成 | 工作流/提示词技巧已记录 |
| 补充 ai-image-generation 技能 | 🟡 待确认 | 若安装则补 Krea2 工作流章节 |

## 与其他生图方案对比
| 方案 | 成本 | 特点 |
|------|------|------|
| xAI grok-imagine（现用） | API 按量 | 云端，简单 |
| 硅基流动 FLUX | API 按量 | 云端 |
| **Krea2 本地** | 免费 | 真实照片级 + 快速 + 无审查（本地） |

## 结论
- Krea2 + int8-convrot 全部真实，硬件达标
- 价值：本地免费生图 + 真实照片级 + 跨次元能力
- 成本：ComfyUI 搭建 + 14GB 模型下载
- **待用户确认是否现在安装**（大工程，需安排下载时间）

---
> 关联: [[krea2-comfyui-deploy-notes]]（本地部署完整踩坑） | [[HOME|🏠 首页]]

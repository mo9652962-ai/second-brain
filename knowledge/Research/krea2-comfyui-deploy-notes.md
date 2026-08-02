---
tags: [research, comfyui, krea2, image-generation, int8, troubleshooting]
created: 2026-08-01
status: absorbed
---

# Krea2 ComfyUI 本地部署 — 完整踩坑记录（含解决方案）

> 2026-08-01 部署 · RTX 4060 Laptop 8GB · Windows 10 · ComfyUI 0.29

## ✅ 最终可用方案（2026-08-02 十轮研究定版）

| 组件 | 文件 | 版本 | 位置 |
|------|------|------|------|
| 主模型 | `krea2_turbo_fp8_scaled.safetensors` | 12.24GB (**官方 Comfy-Org 版**) | `models/diffusion_models/` |
| 文本编码器 | `qwen3vl_4b_bf16.safetensors` | 8.27GB (bf16 版!) | `models/text_encoders/` |
| VAE | `qwen_image_vae.safetensors` + **自定义 Krea2VAEDecodeOfficial** | diffusers AutoencoderKLQwenImage | — |

### 🎯 关键修复（2026-08-02 十轮研究结论）

1. **weight_dtype 必须 `default`**！`fp8_e4m3fn`/`fp8_e5m2` 在 RTX 4060 上反量化坏掉 → **全黑图**
2. **CFG 必须 1.0**！脚本默认曾误设为 0.0 → 黑图
3. **8GB 显存只能用 512×512 采样**！1024 采样 latent 通道退化（无内容）→ 黑图
4. **512 出图后 `--upscale2x` PIL LANCZOS 放大到 1024**（8GB 卡高清方案）
5. latent 处理链路（To5D + ProcessOut）**是正确的**——diffusers `_decode` 内部不做 latents 缩放，必须手动 x*std+mean
6. ComfyUI 0.29 原生 VAELoader 加载 qwen_image_vae **恒定输出灰图（bug 仍在）** → 必须用 diffusers 自定义节点
7. 官方 workflow 无 latent 转换节点（0.3.5x 版本原生 VAE 已可用）——**升级 ComfyUI 后可用官方链路**

### ✅ 稳定命令
```bash
py -3.12 scripts/krea2-gen.py "提示词" --size 512x512 --cfg 1.0 --upscale2x
```

## 📜 商用许可（2026-08-01 研究确认）

**Krea 2 Community License：免费商用**，条件是**公司年收入 < $100 万美元**（trailing 12 个月，含关联实体全部收入）。满足则无需企业许可即可：
- 自托管运行 Krea2（本地/自建服务器）✅
- 用于商业项目（为客户生成资产）✅
- 微调 / 嵌入产品 ✅

**sora 场景**：闲鱼 PPT 代做 / 论文配图 / 数学练习册插图 → **完全合规**（年收入远低于门槛）。
> ⚠️ 超出门槛需联系 `opensource@krea.ai` 购买商业许可。
> 官方来源：https://www.krea.ai/krea-2-licensing

## 🎨 官方风格 LoRA（2026-08-01 研究整理）

下载源：`Comfy-Org/Krea-2/loras` → 放 `models/loras/`，用 LoraLoaderModelOnly + 触发词，强度 1.0：

| LoRA | 触发词 | 用途 |
|------|--------|------|
| krea2_darkbrush | `monochrome ink wash style` | 黑白水墨插画 |
| krea2_dotmatrix | `monochrome stippling style` | 单色点阵 |
| krea2_kidsdrawing | `naive expressive sketch style` | 儿童手绘风 |
| krea2_neondrip | `textured abstract style` | 霓虹抽象 |
| krea2_rainywindow | `rainy window style` | 雨窗氛围 |
| krea2_retroanime | `purple retro anime style` | 复古动漫 |
| krea2_softwatercolor | `art deco watercolor style` | 水彩装饰风 |
| krea2_sunsetblur | `ethereal motion blur style` | 日落虚化 |
| krea2_vintagetarot | `vintage tarot style` | 复古塔罗 |
| krea2_style_reference | — | 风格参考（图生图） |

## 🔍 已知问题（社区确认）

- **GitHub issue `#14717`** "Artefacts when running Krea 2"（2026-07-01）：噪声伪影与我们的乱码问题同源，社区仍未解决（标注 User Support）。**我们的 Triton + 官方 VAE 节点方案是有效 workaround**。
- **JSON 区域提示词**：Krea2 的 Qwen3-VL 编码器支持 Ideogram 式结构化提示（bounding box + 调色板），可用 `Ideogram4PromptBuilderKJ` 节点（需安装 Krea2 JSON pack）。

## ✅ 关键部署结论
 1. 用 ComfyUI 0.29 **原生加载器**（UNETLoader + CLIPLoader type=krea2）
 2. **必须 `--enable-triton-backend` 启动**（否则 FP8 量化走降级路径→乱码！）
 3. **VAE 用自定义节点 `Krea2VAEDecodeOfficial`**（ComfyUI 0.29 的 WanVAE 加载 qwen_image_vae 恒定输出=bug）
 4. KSampler 后接 `Krea2LatentTo5D` → `Krea2LatentProcessOut`（**std 必须用官方值 2.8184...**，写 0.85 会出黑图）→ `Krea2VAEDecodeOfficial`
 5. **CFG 1.0**（参考 AlperKTS workflow） + er_sde + 8 步 + ConditioningZeroOut 负面
 6. **8GB 显存必须 `--lowvram` 启动**（否则 1024×1024 OOM 崩溃/黑图；实测 512×512 稳定）

### 一键出图
```bash
py -3.12 ~/.openclaw/workspace/scripts/krea2-gen.py "提示词" -o 输出目录
# 启动 ComfyUI 必须带: --enable-triton-backend
# 依赖: pip install diffusers (官方 Qwen VAE 解码器)
```

### 可用 workflow（API 模式）
```json
{"3": UNETLoader(unet_name="Krea2_Turbo_convrot_int8mixed.safetensors"),
 "4": CLIPLoader(clip_name="qwen3vl_4b_bf16.safetensors", type="krea2"),
 "5": VAELoader(vae_name="qwen_image_vae.safetensors"),
 "6": CLIPTextEncode(正提示词), "6b": CLIPTextEncode(负提示词),
 "7": EmptyLatentImage(1024x1024),
 "8": KSampler(steps=8, cfg=1.0, euler/simple),
 "9": VAEDecode, "10": SaveImage}
```

## 🔥 三个坑（全踩了）

### 坑1: lilcheaty 的 INT8 模型 comfy_quant 空字段 → 崩溃
- **现象**: CLIPLoader/加载时 `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`
- **根因**: `comfy/ops.py:1104` 读 `comfy_quant` 张量当 JSON 解析，但 lilcheaty 版该张量是 **60 字节全零占位符**
- **解决**: 换 Winnougan 版（ctq 转换 + 原生格式）

### 坑2: fp8_scaled 文本编码器也有空 comfy_quant
- **现象**: 换了主模型后 CLIPLoader 节点仍报同样错误
- **根因**: `qwen3vl_4b_fp8_scaled.safetensors` 有 252 个 comfy_quant 但内容全零
- **解决**: 换 **bf16 版**（`qwen3vl_4b_bf16.safetensors`，713 张量 0 个 comfy_quant，干净）

### 坑3: 用原生 UNETLoader 而非 INT8-Fast
- ComfyUI 0.29 已原生支持 INT8，`OTUNetLoaderW8A8` 反而触发旧格式兼容问题
- 正确: 原生 `UNETLoader` + `weight_dtype: default`

## 📦 部署环境要点

- Python 3.12.10 + venv（**必须 `env -u PYTHONPATH`**，否则 Hermes 的 PYTHONPATH 污染）
- torch 2.11.0+cu128（官方源，清华镜像有 sha256 损坏风险）
- ComfyUI 0.29.0 + comfyui-frontend 1.47.11
- 模型下载: hf-mirror.com + aria2 16线程（huggingface.co 直连不通）

## 🔧 日常使用

```bash
# 启动（后台）
cd /c/Users/31954/ComfyUI && env -u PYTHONPATH ./venv/Scripts/python.exe main.py --listen 127.0.0.1 --port 8188
# 访问 GUI: http://127.0.0.1:8188
# 模型放: models/diffusion_models/ + text_encoders/ + vae/
```

---
> 关联: [[krea2-local-image-gen-study]]（模型研究笔记） | [[HOME|🏠 首页]]

---
tags: [research, comfyui, krea2, image-generation, int8, troubleshooting]
created: 2026-08-01
status: absorbed
---

# Krea2 ComfyUI 本地部署 — 完整踩坑记录（含解决方案）

> 2026-08-01 部署 · RTX 4060 Laptop 8GB · Windows 10 · ComfyUI 0.29

## ✅ 最终可用方案

| 组件 | 文件 | 版本 | 位置 |
|------|------|------|------|
| 主模型 | `Krea2_Turbo_convrot_int8mixed.safetensors` | 12.02GB (Winnougan ctq 版) | `models/diffusion_models/` |
| 文本编码器 | `qwen3vl_4b_bf16.safetensors` | 8.27GB (bf16 版!) | `models/text_encoders/` |
| VAE | `qwen_image_vae.safetensors` | 242MB | `models/vae/` |

**关键**: 用 ComfyUI 0.29 **原生加载器**（UNETLoader + CLIPLoader type=krea2），不用 INT8-Fast 自定义节点。

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

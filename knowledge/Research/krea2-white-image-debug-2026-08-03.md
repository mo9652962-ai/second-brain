---
title: "Krea2 全白图排障报告 · 2026-08-03"
type: note
domain: Research
status: active
tags: [knowledge/research]
source: null
date: 2026-08-03
---
# Krea2 全白图排障报告 · 2026-08-03

> 症状：Krea2 生成全白/全黑/灰图 → 逐步定位 → **双重缩放 root cause**
> 结论：ComfyUI 0.29 已内置 Krea2 支持，旧部署笔记的 ProcessOut 方案**已过时**

## 🐛 症状时间线

| # | 测试 | 结果 | 诊断 |
|---|------|------|------|
| 1 | 商务白底背景 | 过曝抽象图 | 提示词问题（非 bug）|
| 2 | 水墨仕女（bf16 编码器 + ProcessOut）| 全白 | **双重缩放** |
| 3 | 红苹果测试（同配置）| 全白 | 排除提示词因素 → 链路 bug |
| 4 | 安装 accelerate | 仍全白 | 非根因 |
| 5 | 加 --enable-triton-backend | 仍全白 | 非根因 |
| 6 | debug 节点插桩 | **定位！** KSampler 输出 std≈1.8，ProcessOut 后 std≈3.9 | **双重缩放** |
| 7 | 移除 ProcessOut | 苹果图内容成形 ✅ | 修复生效 |
| 8 | 换 fp8_scaled 编码器 | 内容质量提升 | 官方推荐配置 |
| 9 | 水墨 LoRA + CFG 2.5 | 人物轮廓可见 | 风格需调优 |
| 10 | 写实人物 | **人物成功生成** ✅ | 链路完全修复 |

## 🔬 根因分析

### 为什么 ProcessOut 导致全白？

ComfyUI 0.29 的 `Krea2` 模型类绑定 `latent_format = Wan21`：
```python
# comfy/latent_formats.py: Wan21.process_out
def process_out(self, latent):
    return latent * latents_std / self.scale_factor + latents_mean
```

**KSampler 输出时已自动调用 process_out**（x*std+mean），latent 已在解码空间。

而旧部署笔记（2026-08-02）要求采样后再手动接 `Krea2LatentProcessOut`（也做 x*std+mean）→ **双重缩放**：
- KSampler 输出：min=-3.8, max=3.5, std=1.8 ✅ 正常
- ProcessOut 后：min=-11, max=9.5, std=3.9 ❌ 爆炸
- VAE decode clamp(-1,1) → 全白

> 旧笔记结论适用于当时 ComfyUI 版本（可能无内置 Krea2 类）；**0.29 已内置，方案需更新**

### 其他确认的坑（08-03 实测）

| 坑 | 表现 | 解决方案 |
|----|------|---------|
| PYTHONPATH 污染 | numpy 崩溃 | `env -u PYTHONPATH` 启动 |
| 缺 triton backend | FP8 降级乱码 | `--enable-triton-backend` |
| 缺 accelerate | diffusers 警告 | `pip install accelerate` |
| 原生 VAELoader | 恒定灰图 (std≈7.5) | 用 `Krea2VAEDecodeOfficial`（diffusers）|
| 1024 直接采样 | 灰图退化 | 512/768 基础采样 |
| 低 CFG 复杂主题 | 空白图 | CFG 2-3 |
| hires 超分 | 只放大模糊 | 512 底图质量是天花板 |

## ✅ 最终正确配置

| 组件 | 值 |
|------|-----|
| 主模型 | `krea2_turbo_fp8_scaled.safetensors` |
| 编码器 | `qwen3vl_4b_fp8_scaled.safetensors`（官方推荐，**非 bf16**）|
| VAE | `Krea2VAEDecodeOfficial`（diffusers）|
| latent 链路 | KSampler → Krea2LatentTo5D → Krea2VAEDecodeOfficial（**无 ProcessOut**）|
| 启动参数 | `env -u PYTHONPATH python main.py --listen 127.0.0.1 --port 8188 --enable-triton-backend --lowvram` |
| 采样 | 512/768 基础 + CFG 1-3（复杂 2-3）|
| LoRA | `--lora krea2_darkbrush.safetensors` + 触发词 |

## 🎨 能力实测结论（8GB 卡）

- ✅ **写实风格**：人物/物体能正确生成（512 下细节受限但轮廓清晰）
- ⚠️ **水墨 LoRA**：低对比风格在 512 下难出细节（需要更高分辨率）
- ❌ **1024 直接采样**：8GB 卡灰图退化，无解
- ❌ **hires 超分**：无法凭空增加 512 底图缺失的细节

## 📌 沉淀

- 部署笔记已更新至 08-03 修复版：`knowledge/Research/krea2-comfyui-deploy-notes.md`
- 脚本已升级：`scripts/krea2-gen.py`（--lora/--cfg 支持 + 移除 ProcessOut + fp8_scaled）
- **教训**：模型支持更新后必须重验旧方案；调试用插桩看中间值而非只看输出

---
_生成: Krea2 全白图排障 · k (Hermes) · 2026-08-03_

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]

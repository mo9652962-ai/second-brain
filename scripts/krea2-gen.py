#!/usr/bin/env python3
"""
krea2-gen.py — Krea2 一键出图脚本
=================================
用法:
  python krea2-gen.py "一只橘猫在阳光下打盹，特写，照片级"
  python krea2-gen.py "赛博朋克城市夜景" -o D:/output -s 42 -n 2
  python krea2-gen.py "山水画风格" --size 512x512 --hires

参数:
  prompt            提示词（中文/英文均可，必填）
  -o, --output      输出目录 (默认: ComfyUI/output)
  -s, --seed        随机种子 (默认: 随机)
  -n, --count       生成数量 (默认: 1)
  --size WxH        基础采样分辨率 (默认: 512x512, 8GB 卡安全值)
  --hires           hires fix: latent 2x 放大 + denoise 0.5 二次采样（推荐，出 1024 高清）
  --steps           采样步数 (默认: 8, Turbo 模型)
  --cfg             CFG scale (默认: 1.0, Turbo 蒸馏模型必须 1.0，0 会黑图)
  --negative        负面提示词 (默认: 空, Turbo 不需要负面)
  --url             ComfyUI 地址 (默认: http://127.0.0.1:8188)
  --poll-interval   轮询间隔秒 (默认: 5)
  --timeout         超时秒 (默认: 600)
"""

import argparse
import json
import random
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

# ============ 配置 ============
DEFAULT_URL = "http://127.0.0.1:8188"
MODEL_NAME = "krea2_turbo_fp8_scaled.safetensors"
CLIP_NAME = "qwen3vl_4b_fp8_scaled.safetensors"  # 2026-08-03: 官方模板推荐 fp8_scaled 编码器
VAE_NAME = "qwen_image_vae.safetensors"
# Turbo 是蒸馏模型：不需要负面提示词（官方文档明确 "negative prompt not required"）
DEFAULT_NEGATIVE = ""


def build_workflow(prompt: str, negative: str, width: int, height: int,
                   steps: int, cfg: float, seed: int, hires: bool = False,
                   lora: str = None, lora_strength: float = 1.0) -> dict:
    """构建 Krea2 生图 workflow（2026-08-03 修复版）

    链路（ComfyUI 0.29 官方模板等价）:
      512 基础采样 → To5D → diffusers VAE 解码 → (hires) 4x-UltraSharp 超分

    2026-08-03 关键修复（相对旧部署笔记）:
    - 【移除 ProcessOut】Krea2 类已绑定 Wan21 latent_format，KSampler 输出时
      自动 process_out (x*std+mean)。再加 ProcessOut = 双重缩放 → 值爆炸 → 全白
    - 【fp8_scaled 编码器】官方模板推荐 qwen3vl_4b_fp8_scaled.safetensors
      （bf16 版在 0.29 反而有问题）
    - 【原生 VAELoader 灰图 bug 仍在】qwen_image_vae 需 diffusers 解码
    - 【1024 直接采样灰图】8GB 卡必须 512/768 基础采样
    - 【CFG 建议 1.0-3.0】蒸馏模型低 CFG 会出空白，复杂主题建议 2-3
    """
    wf = {
        "3": {"class_type": "UNETLoader", "inputs": {
            "unet_name": MODEL_NAME, "weight_dtype": "default"}},
    }
    # 可选风格 LoRA（官方: LoraLoaderModelOnly + 触发词 + strength 1.0）
    model_ref = ["3", 0]
    if lora:
        wf["3b"] = {"class_type": "LoraLoaderModelOnly", "inputs": {
            "model": ["3", 0], "lora_name": lora, "strength_model": lora_strength}}
        model_ref = ["3b", 0]
    wf["4"] = {"class_type": "CLIPLoader", "inputs": {
        "clip_name": CLIP_NAME, "type": "krea2", "device": "default"}}
    wf["6"] = {"class_type": "CLIPTextEncode", "inputs": {
        "text": prompt, "clip": ["4", 0]}}
    wf["6b"] = {"class_type": "CLIPTextEncode", "inputs": {
        "text": negative, "clip": ["4", 0]}}
    wf["7"] = {"class_type": "EmptyLatentImage", "inputs": {
        "width": width, "height": height, "batch_size": 1}}
    wf["8"] = {"class_type": "KSampler", "inputs": {
        "model": model_ref, "positive": ["6", 0], "negative": ["6b", 0],
        "latent_image": ["7", 0], "seed": seed, "steps": steps, "cfg": cfg,
        "sampler_name": "er_sde", "scheduler": "simple", "denoise": 1.0}}
    wf["8b"] = {"class_type": "Krea2LatentTo5D", "inputs": {
        "latent": ["8", 0]}}
    # 2026-08-03 修复（ComfyUI 0.29）:
    # - Krea2 类已绑定 Wan21 latent_format, KSampler 输出时自动 process_out (x*std+mean)
    # - 再加 ProcessOut = 双重缩放 → 值爆炸 → 全白图（旧版 ComfyUI 才需要 ProcessOut）
    # - 原生 VAELoader 加载 qwen_image_vae 结构不匹配 → 灰图（需 diffusers 解码）
    wf["9"] = {"class_type": "Krea2VAEDecodeOfficial", "inputs": {
        "samples": ["8b", 0]}}
    # AI 超分 (4x-UltraSharp): 512 → 2048 高清（比 LANCZOS 好 64%，8GB 卡最优解）
    if hires:
        wf["11"] = {"class_type": "UpscaleModelLoader", "inputs": {
            "model_name": "4x-UltraSharp.pth"}}
        wf["12"] = {"class_type": "ImageUpscaleWithModel", "inputs": {
            "upscale_model": ["11", 0], "image": ["9", 0]}}
        wf["10"] = {"class_type": "SaveImage", "inputs": {
            "filename_prefix": "krea2_gen", "images": ["12", 0]}}
    else:
        wf["10"] = {"class_type": "SaveImage", "inputs": {
            "filename_prefix": "krea2_gen", "images": ["9", 0]}}
    return wf


def http_json(url: str, data: dict = None, timeout: int = 30) -> dict:
    """HTTP GET/POST JSON 辅助"""
    if data is not None:
        req = urllib.request.Request(url, data=json.dumps(data).encode(),
                                     headers={"Content-Type": "application/json"})
    else:
        req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {body[:300]}")


def wait_for_completion(url: str, prompt_id: str, poll_interval: int = 5,
                        timeout: int = 600) -> dict:
    """轮询 ComfyUI 直到任务完成"""
    start = time.time()
    while time.time() - start < timeout:
        try:
            history = http_json(f"{url}/history/{prompt_id}", timeout=10)
            if prompt_id in history:
                entry = history[prompt_id]
                status = entry.get("status", {})
                if status.get("completed"):
                    outputs = []
                    for node_id, node_out in entry.get("outputs", {}).items():
                        for img in node_out.get("images", []):
                            outputs.append(img)
                    return {"status": "success", "outputs": outputs}
                if status.get("status_str") == "error":
                    msgs = entry.get("status", {}).get("messages", [])
                    err = ""
                    for mtype, mdata in msgs:
                        if mtype == "execution_error":
                            err = f"{mdata.get('node_type','')}: {mdata.get('exception_message','')}"
                    return {"status": "error", "error": err}
        except Exception:
            pass  # 网络抖动，继续轮询
        time.sleep(poll_interval)
    return {"status": "timeout", "error": f"超过 {timeout}s 未完成"}


def main():
    parser = argparse.ArgumentParser(description="Krea2 一键出图")
    parser.add_argument("prompt", help="提示词（中文/英文均可）")
    parser.add_argument("-o", "--output", default=None, help="输出目录")
    parser.add_argument("-s", "--seed", type=int, default=None, help="随机种子")
    parser.add_argument("-n", "--count", type=int, default=1, help="生成数量")
    parser.add_argument("--size", default="512x512",
                        help="基础采样分辨率 WxH（8GB 显存建议 512x512；配合 --hires 输出 1024 高清）")
    parser.add_argument("--hires", action="store_true",
                        help="AI 超分: 4x-UltraSharp 把 512 输出放大到 2048（比 LANCZOS 锐利，8GB 卡高清方案）")
    parser.add_argument("--steps", type=int, default=8, help="采样步数")
    parser.add_argument("--cfg", type=float, default=1.0,
                        help="CFG scale (Turbo 蒸馏模型用 1.0，0 会导致黑图)")
    parser.add_argument("--negative", default=DEFAULT_NEGATIVE, help="负面提示词")
    parser.add_argument("--lora", default=None,
                        help="风格 LoRA 文件名（如 krea2_darkbrush.safetensors）")
    parser.add_argument("--lora-strength", type=float, default=1.0, help="LoRA 强度")
    parser.add_argument("--url", default=DEFAULT_URL, help="ComfyUI 地址")
    parser.add_argument("--poll-interval", type=int, default=5, help="轮询间隔")
    parser.add_argument("--timeout", type=int, default=600, help="超时秒")
    args = parser.parse_args()

    # 解析尺寸
    try:
        w, h = map(int, args.size.lower().split("x"))
    except ValueError:
        print("❌ 尺寸格式错误，应为 WxH 如 512x512")
        sys.exit(1)

    # 检查 ComfyUI 是否运行
    try:
        http_json(f"{args.url}/system_stats", timeout=5)
    except Exception:
        print("❌ ComfyUI 未运行！请先启动:")
        print("   cd C:\\Users\\31954\\ComfyUI && env -u PYTHONPATH ./venv/Scripts/python.exe main.py --listen 127.0.0.1 --port 8188 --enable-triton-backend --lowvram")
        print("   ⚠️ 8GB 显存建议带 --lowvram；必须 --enable-triton-backend")
        sys.exit(1)

    # 输出目录（确保绝对路径）
    if args.output:
        output_dir = Path(args.output).resolve()
    else:
        output_dir = Path(r"C:\Users\31954\ComfyUI\output").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    out_size = f"{w*2}x{h*2}" if args.hires else f"{w}x{h}"
    print(f"🎨 Krea2 出图: {args.prompt[:50]}{'...' if len(args.prompt) > 50 else ''}")
    print(f"   基础采样: {w}x{h} | 输出: {out_size} | hires: {'✅' if args.hires else '—'} | 步数: {args.steps} | CFG: {args.cfg} | 数量: {args.count}")

    saved = []
    for i in range(args.count):
        seed = args.seed if args.seed is not None else random.randint(0, 2**31)
        if args.count > 1:
            print(f"\n[{i+1}/{args.count}] seed={seed}")
        else:
            print(f"\nseed={seed}")

        wf = build_workflow(args.prompt, args.negative, w, h, args.steps, args.cfg, seed, args.hires, args.lora, args.lora_strength)
        try:
            result = http_json(f"{args.url}/prompt", {"prompt": wf}, timeout=30)
        except RuntimeError as e:
            print(f"❌ 提交失败: {e}")
            sys.exit(1)

        prompt_id = result.get("prompt_id", "")
        if not prompt_id:
            print(f"❌ 提交失败: {result}")
            sys.exit(1)

        done = wait_for_completion(args.url, prompt_id, args.poll_interval, args.timeout)
        print()  # 换行

        if done["status"] == "success" and done.get("outputs"):
            for img in done["outputs"]:
                filename = img["filename"]
                subfolder = img.get("subfolder", "")
                # ComfyUI 输出在 output/ 目录（用绝对路径避免拼接错误）
                src = Path(r"C:\Users\31954\ComfyUI\output") / subfolder / filename
                if src.exists():
                    dst = output_dir / filename
                    import shutil
                    shutil.copy2(src, dst)
                    saved.append(dst)
                    print(f"✅ 已保存: {dst}")
                else:
                    print(f"✅ 已生成 (未找到文件: {src})")
        elif done["status"] == "error":
            print(f"❌ 生成失败 [{done.get('node','')}]: {done.get('error','')}")
            sys.exit(1)
        else:
            print(f"❌ {done.get('error','超时')}")
            sys.exit(1)

    print(f"\n🎉 完成！共 {len(saved)} 张图片")
    for s in saved:
        print(f"   {s}")


if __name__ == "__main__":
    main()

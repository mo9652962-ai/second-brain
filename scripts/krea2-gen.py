#!/usr/bin/env python3
"""
krea2-gen.py — Krea2 一键出图脚本
=================================
用法:
  python krea2-gen.py "一只橘猫在阳光下打盹，特写，照片级"
  python krea2-gen.py "赛博朋克城市夜景" -o D:/output -s 42 -n 2
  python krea2-gen.py "山水画风格" --size 768x768 --steps 8

参数:
  prompt            提示词（中文/英文均可，必填）
  -o, --output      输出目录 (默认: ComfyUI/output)
  -s, --seed        随机种子 (默认: 随机)
  -n, --count       生成数量 (默认: 1)
  --size WxH        分辨率 (默认: 1024x1024)
  --steps           采样步数 (默认: 8, Turbo 模型)
  --cfg             CFG scale (默认: 1.0, Turbo 推荐)
  --negative        负面提示词 (默认: 通用负面)
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
CLIP_NAME = "qwen3vl_4b_bf16.safetensors"
VAE_NAME = "qwen_image_vae.safetensors"
# Turbo 是蒸馏模型：不需要负面提示词（官方文档明确 "negative prompt not required"）
DEFAULT_NEGATIVE = ""


def build_workflow(prompt: str, negative: str, width: int, height: int,
                   steps: int, cfg: float, seed: int) -> dict:
    """构建 Krea2 生图 workflow（ComfyUI 0.29 原生加载器）"""
    return {
        "3": {"class_type": "UNETLoader", "inputs": {
            "unet_name": MODEL_NAME, "weight_dtype": "default"}},
        "4": {"class_type": "CLIPLoader", "inputs": {
            "clip_name": CLIP_NAME, "type": "krea2", "device": "default"}},
        "5": {"class_type": "VAELoader", "inputs": {
            "vae_name": VAE_NAME}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {
            "text": prompt, "clip": ["4", 0]}},
        "6b": {"class_type": "CLIPTextEncode", "inputs": {
            "text": negative, "clip": ["4", 0]}},
        "7": {"class_type": "EmptyLatentImage", "inputs": {
            "width": width, "height": height, "batch_size": 1}},
        "8": {"class_type": "KSampler", "inputs": {
            "model": ["3", 0], "positive": ["6", 0], "negative": ["6b", 0],
            "latent_image": ["7", 0], "seed": seed, "steps": steps, "cfg": cfg,
            "sampler_name": "er_sde", "scheduler": "simple", "denoise": 1.0}},
        "9": {"class_type": "VAEDecode", "inputs": {
            "samples": ["8", 0], "vae": ["5", 0]}},
        "10": {"class_type": "SaveImage", "inputs": {
            "filename_prefix": "krea2_gen", "images": ["9", 0]}},
    }


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
        body = e.read().decode() if e.fp else str(e)
        raise RuntimeError(f"HTTP {e.code}: {body[:200]}")


def wait_for_completion(base_url: str, prompt_id: str,
                        poll_interval: int, timeout: int) -> dict:
    """轮询等待任务完成，返回输出信息"""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            history = http_json(f"{base_url}/history/{prompt_id}", timeout=15)
        except Exception:
            history = {}
        if prompt_id in history:
            entry = history[prompt_id]
            status = entry.get("status", {})
            status_str = status.get("status_str", "")
            if status_str == "success":
                outputs = []
                for node_out in entry.get("outputs", {}).values():
                    for img in node_out.get("images", []):
                        outputs.append(img)
                return {"status": "success", "outputs": outputs}
            if status_str == "error":
                for msg in status.get("messages", []):
                    if msg[0] == "execution_error":
                        err = msg[1]
                        return {"status": "error",
                                "error": err.get("exception_message", "unknown")[:300],
                                "node": f'{err.get("node_id")}({err.get("node_type")})'}
                return {"status": "error", "error": "unknown error"}
        # 打印进度
        sys.stdout.write(f"\r⏳ 生成中... ({int(time.time() % 1000)}s)")
        sys.stdout.flush()
        time.sleep(poll_interval)
    return {"status": "timeout", "error": f"超过 {timeout}s 未完成"}


def main():
    parser = argparse.ArgumentParser(description="Krea2 一键出图")
    parser.add_argument("prompt", help="提示词（中文/英文均可）")
    parser.add_argument("-o", "--output", default=None, help="输出目录")
    parser.add_argument("-s", "--seed", type=int, default=None, help="随机种子")
    parser.add_argument("-n", "--count", type=int, default=1, help="生成数量")
    parser.add_argument("--size", default="1024x1024", help="分辨率 WxH")
    parser.add_argument("--steps", type=int, default=8, help="采样步数")
    parser.add_argument("--cfg", type=float, default=1.0, help="CFG scale")
    parser.add_argument("--negative", default=DEFAULT_NEGATIVE, help="负面提示词")
    parser.add_argument("--url", default=DEFAULT_URL, help="ComfyUI 地址")
    parser.add_argument("--poll-interval", type=int, default=5, help="轮询间隔")
    parser.add_argument("--timeout", type=int, default=600, help="超时秒")
    args = parser.parse_args()

    # 解析尺寸
    try:
        w, h = map(int, args.size.lower().split("x"))
    except ValueError:
        print("❌ 尺寸格式错误，应为 WxH 如 1024x1024")
        sys.exit(1)

    # 检查 ComfyUI 是否运行
    try:
        http_json(f"{args.url}/system_stats", timeout=5)
    except Exception:
        print("❌ ComfyUI 未运行！请先启动:")
        print("   cd C:\\Users\\31954\\ComfyUI && env -u PYTHONPATH ./venv/Scripts/python.exe main.py --listen 127.0.0.1 --port 8188")
        sys.exit(1)

    # 输出目录（确保绝对路径）
    if args.output:
        output_dir = Path(args.output).resolve()
    else:
        output_dir = Path(r"C:\Users\31954\ComfyUI\output").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🎨 Krea2 出图: {args.prompt[:50]}{'...' if len(args.prompt) > 50 else ''}")
    print(f"   尺寸: {w}x{h} | 步数: {args.steps} | CFG: {args.cfg} | 数量: {args.count}")

    saved = []
    for i in range(args.count):
        seed = args.seed if args.seed is not None else random.randint(0, 2**31)
        if args.count > 1:
            print(f"\n[{i+1}/{args.count}] seed={seed}")
        else:
            print(f"\nseed={seed}")

        wf = build_workflow(args.prompt, args.negative, w, h, args.steps, args.cfg, seed)
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

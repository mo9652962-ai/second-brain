#!/usr/bin/env python3
"""Hermes provider connectivity check - no secrets printed."""
import json, os, re, ssl, sys, time, urllib.request, urllib.error

CONFIG = r"C:/Users/31954/AppData/Local/hermes/config.yaml"
ENV = r"C:/Users/31954/AppData/Local/hermes/.env"

def load_env(path):
    env = {}
    if os.path.exists(path):
        for line in open(path, encoding="utf-8", errors="ignore"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env

def load_providers():
    try:
        import yaml
        cfg = yaml.safe_load(open(CONFIG, encoding="utf-8"))
        return cfg.get("custom_providers", [])
    except Exception:
        # fallback: regex parse
        content = open(CONFIG, encoding="utf-8").read()
        provs = []
        for m in re.finditer(r"- api_key:\s*([^\n]*)\n(.*?)(?=\n  - |\n\S|\Z)", content, re.S):
            body = m.group(2)
            name = re.search(r"name:\s*(\S+)", body)
            base = re.search(r"base_url:\s*(\S+)", body)
            keyenv = re.search(r"key_env:\s*(\S+)", body)
            api_key = m.group(1).strip()
            provs.append({
                "name": name.group(1) if name else "?",
                "base_url": base.group(1) if base else "",
                "key_env": keyenv.group(1) if keyenv else "",
                "api_key": api_key,
            })
        return provs

def resolve_key(prov, env):
    key = prov.get("api_key") or ""
    if not key and prov.get("key_env"):
        key = env.get(prov["key_env"], "")
    # strip ${VAR} syntax
    m = re.match(r"\$\{(\w+)\}", key)
    if m:
        key = env.get(m.group(1), "")
    return key.strip() if key else ""

def test(base_url, api_key, model, timeout=20):
    url = base_url.rstrip("/") + "/chat/completions"
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": "hi"}],
        "max_tokens": 1,
    }).encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", "Bearer " + api_key)
    t0 = time.time()
    try:
        # standard TLS verification (default context); keys travel over HTTPS only
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
            dt = time.time() - t0
            model_used = (data.get("model") or data.get("id") or "?").split("/")[-1]
            return f"OK   {dt*1000:6.0f}ms  model={model_used}"
    except urllib.error.HTTPError as e:
        dt = time.time() - t0
        try:
            msg = json.loads(e.read().decode()).get("error", {}).get("message", "")[:120]
        except Exception:
            msg = e.reason
        return f"HTTP {e.code} {dt*1000:6.0f}ms  {msg}"
    except Exception as e:
        dt = time.time() - t0
        return f"FAIL {dt*1000:6.0f}ms  {str(e)[:120]}"

env = load_env(ENV)
provs = load_providers()

# test matrix: provider name -> (base_url, model) - resolved after load
results = []
tested = set()

# built-in providers first
builtin = [
    ("deepseek (官方)", "https://api.deepseek.com/v1", env.get("DEEPSEEK_API_KEY", ""), "deepseek-v4-flash"),
    ("dashscope (百炼)", "https://dashscope.aliyuncs.com/compatible-mode/v1", env.get("DASHSCOPE_API_KEY", ""), "qwen-plus"),
    ("siliconflow", "https://api.siliconflow.cn/v1", env.get("SILICONFLOW_API_KEY", ""), "deepseek-ai/DeepSeek-V4-Flash"),
    ("opencode-go", "https://opencode.ai/zen/go/v1", env.get("OPENCODE_GO_API_KEY", ""), "minimax-m3"),
    ("moonshot (kimi)", "https://api.moonshot.cn/v1", None, "kimi-k2.7-code"),
]
for name, url, key, model in builtin:
    if key is None:
        # try from custom providers
        continue
    status = test(url, key, model) if key else "SKIP (no key)"
    results.append((name, status))

for p in provs:
    pname = p["name"]
    key = resolve_key(p, env)
    url = p["base_url"]
    if not url:
        results.append((pname, "SKIP (no base_url)"))
        continue
    # choose a model from config if available
    models = p.get("models", [])
    model = models[0] if models else "deepseek-v4-flash"
    if pname == "jiyuanlvdong":
        model = "deepseek-v4-flash-0731"
    elif pname == "fangzhou-1":
        model = "doubao-seed-2-0-pro"
    elif pname == "fangzhou-2":
        model = "doubao-seed-2-0-pro-260215"
    elif pname == "dengzhen":
        model = "deepseek-v4-flash-0731"
    status = test(url, key, model) if key else "SKIP (no key)"
    results.append((f"custom:{pname}", status))

print("=== Provider connectivity ===")
for name, status in results:
    print(f"{name:24s} {status}")

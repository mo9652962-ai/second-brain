#!/usr/bin/env python3
"""Hermes provider connectivity check - no secrets printed.
Verified 2026-08-09: reads config.yaml custom_providers + .env key_env,
POSTs minimal chat/completions (max_tokens=1), prints status/latency/model only.
"""
import json, os, re, time, urllib.request, urllib.error

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

def _balance_flag(code, msg):
    """Detect balance shortage from an HTTP error body. Relays (keylink/
    jiyuanlvdong) report '剩余额度: ¥0.05' inside the error text, no separate
    balance endpoint. Returns an alarm suffix or ''. """
    if code not in (402, 403, 429):
        return ""
    low = (msg or "").lower()
    kw = ("额度", "余额", "balance", "insufficient balance",
          "suspended", "credits", "quota", "预扣", "余额不足")
    if not any(k in low for k in kw):
        return ""
    m = re.search(r"[¥￥]?\s*([0-9]+(?:\.[0-9]+)?)\s*元?", (msg or ""))
    amount = ""
    if m:
        try:
            v = float(m.group(1))
            amount = f"¥{v:.2f}" if v < 100 else f"¥{v:,.0f}"
        except Exception:
            amount = m.group(1)
    return f" [⚠️余额告警{' ' + amount if amount else ''}]"

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
            raw = e.read().decode(errors="ignore")
            try:
                msg = json.loads(raw).get("error", {}).get("message", "")[:200]
            except Exception:
                msg = raw[:200]
        except Exception:
            msg = e.reason
        flag = _balance_flag(e.code, msg)
        return f"HTTP {e.code} {dt*1000:6.0f}ms  {msg}{flag}"
    except Exception as e:
        dt = time.time() - t0
        return f"FAIL {dt*1000:6.0f}ms  {str(e)[:120]}"

env = load_env(ENV)
provs = load_providers()

results = []

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
    # choose a reliable model per provider (models[0] may be a YAML-string artifact)
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

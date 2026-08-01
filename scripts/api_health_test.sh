#!/bin/bash
# API Key connectivity test - masks keys, prints only status
ENV_FILE="C:/Users/31954/AppData/Local/hermes/.env"
set -a
source "$ENV_FILE"
set +a

echo "=== 1. DeepSeek 官方 API (deepseek-v4-flash) ==="
curl -s -o /tmp/ds.json -w "HTTP %{http_code} in %{time_total}s\n" --max-time 25 \
  https://api.deepseek.com/v1/chat/completions \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"ping"}],"max_tokens":5}'
head -c 300 /tmp/ds.json; echo

echo ""
echo "=== 2. opencode-go (fallback 链第1项) ==="
curl -s -o /tmp/oc.json -w "HTTP %{http_code} in %{time_total}s\n" --max-time 25 \
  https://opencode.ai/zen/go/v1/chat/completions \
  -H "Authorization: Bearer $OPENCODE_GO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"ping"}],"max_tokens":5}'
head -c 300 /tmp/oc.json; echo

echo ""
echo "=== 3. fangzhou-1 火山方舟 (当前默认 provider) ==="
ARK_KEY=$(python -c "import yaml;print(yaml.safe_load(open(r'C:/Users/31954/AppData/Local/hermes/config.yaml',encoding='utf-8'))['custom_providers'][3]['api_key'])" 2>/dev/null)
if [ -z "$ARK_KEY" ]; then echo "ARK_KEY 提取失败"; else
curl -s -o /tmp/ark.json -w "HTTP %{http_code} in %{time_total}s\n" --max-time 25 \
  https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions \
  -H "Authorization: Bearer $ARK_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"doubao-seed-2-0-mini-260428","messages":[{"role":"user","content":"ping"}],"max_tokens":5}'
head -c 300 /tmp/ark.json; echo
fi

echo ""
echo "=== 4. 搜索后端: TAVILY / EXA / FIRECRAWL ==="
curl -s -o /tmp/tv.json -w "TAVILY HTTP %{http_code}\n" --max-time 20 \
  -X POST https://api.tavily.com/search \
  -H "Content-Type: application/json" \
  -d "{\"api_key\":\"$TAVILY_API_KEY\",\"query\":\"ping\",\"max_results\":1}"
head -c 300 /tmp/tv.json; echo
curl -s -o /tmp/exa.json -w "EXA HTTP %{http_code}\n" --max-time 20 \
  -X POST https://api.exa.ai/search \
  -H "Content-Type: application/json" \
  -H "x-api-key: $EXA_API_KEY" \
  -d '{"query":"ping","numResults":1}'
head -c 300 /tmp/exa.json; echo
curl -s -o /tmp/fc.json -w "FIRECRAWL HTTP %{http_code}\n" --max-time 20 \
  https://api.firecrawl.dev/v1/scrape \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url":"https://example.com"}'
head -c 300 /tmp/fc.json; echo

echo ""
echo "=== 5. Kimi / SiliconFlow / XAI ==="
KIMI_KEY=$(python -c "import yaml;print(yaml.safe_load(open(r'C:/Users/31954/AppData/Local/hermes/config.yaml',encoding='utf-8'))['providers']['moonshot']['api_key'])" 2>/dev/null)
if [ -n "$KIMI_KEY" ]; then
  curl -s -o /tmp/kimi.json -w "KIMI HTTP %{http_code}\n" --max-time 20 \
    https://api.moonshot.cn/v1/chat/completions \
    -H "Authorization: Bearer $KIMI_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"kimi-k2.7-code","messages":[{"role":"user","content":"ping"}],"max_tokens":5}'
  head -c 200 /tmp/kimi.json; echo
else echo "KIMI key 提取失败"; fi
curl -s -o /tmp/sf.json -w "SILICONFLOW HTTP %{http_code}\n" --max-time 20 \
  https://api.siliconflow.cn/v1/chat/completions \
  -H "Authorization: Bearer $SILICONFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-ai/DeepSeek-V4-Flash","messages":[{"role":"user","content":"ping"}],"max_tokens":5}'
head -c 200 /tmp/sf.json; echo

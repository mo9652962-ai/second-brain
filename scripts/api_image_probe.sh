#!/bin/bash
# External image/media API weekly probe - masks keys, prints only status.
# Created by daily-todo-executor 2026-09-08 (reflection 09-07 action item, 当场建).
# Probes: XAI (grok-imagine-image) / FAL (flux) / SiliconFlow (vision+tts+img).
# Output: memory/YYYY/MM/YYYY-MM-DD-api-probe.md + exit 0 (probe ran) even on API failures.

set -a
source "C:/Users/31954/AppData/Local/hermes/.env"
set +a

TODAY=$(date +%Y-%m-%d)
MONTH=$(date +%m)
YEAR=$(date +%Y)
OUT="C:/Users/31954/.openclaw/workspace/memory/${YEAR}/${MONTH}/${TODAY}-api-probe.md"
mkdir -p "C:/Users/31954/.openclaw/workspace/memory/${YEAR}/${MONTH}"

{
echo "---"
echo "tags: [api-probe, cron, media-api]"
echo "created: ${TODAY}"
echo "type: api-probe"
echo "---"
echo ""
echo "# 🔌 外部生图/媒体 API 周探活 · ${TODAY}"
echo ""
echo "| 服务 | 状态 | HTTP | 说明 |"
echo "|:-----|:-----|:-----|:-----|"
} > "$OUT"

# 一次 curl 调用同时拿 body + HTTP code（避免 -o /tmp 的 Windows/MSYS 路径不一致坑）
probe() {
  local name="$1" out="$2" http="$3" note="$4"
  echo "| ${name} | ${out} | ${http} | ${note} |" >> "$OUT"
}

# 1. XAI (grok-imagine-image 生图后端)
XAI_ALL=$(curl -s -w $'\n%{http_code}' --max-time 15 \
  https://api.x.ai/v1/models -H "Authorization: Bearer ${XAI_API_KEY}" 2>/dev/null)
XAI_HTTP=$(echo "$XAI_ALL" | tail -1)
XAI_BODY=$(echo "$XAI_ALL" | sed '$d' | head -c 200 | tr -d '\n')
if [ "$XAI_HTTP" = "200" ]; then
  probe "XAI (grok-imagine)" "✅ OK" "$XAI_HTTP" "key 有效"
elif echo "$XAI_BODY" | grep -q "Incorrect API key"; then
  probe "XAI (grok-imagine)" "❌ key 失效" "$XAI_HTTP" "Incorrect API key，需控制台重生成"
else
  probe "XAI (grok-imagine)" "⚠️ 异常" "$XAI_HTTP" "$(echo "$XAI_BODY" | head -c 80)"
fi

# 2. FAL (flux 生图备用后端)
FAL_ALL=$(curl -s -w $'\n%{http_code}' --max-time 15 \
  "https://fal.run/fal-ai/flux/schnell" -X POST \
  -H "Authorization: Key ${FAL_KEY}" -H "Content-Type: application/json" \
  -d '{"prompt":"test"}' 2>/dev/null)
FAL_HTTP=$(echo "$FAL_ALL" | tail -1)
FAL_BODY=$(echo "$FAL_ALL" | sed '$d' | head -c 200 | tr -d '\n')
if [ "$FAL_HTTP" = "200" ]; then
  probe "FAL (flux)" "✅ OK" "$FAL_HTTP" "账户可用"
elif echo "$FAL_BODY" | grep -q "TOP_UP"; then
  probe "FAL (flux)" "❌ 锁定" "$FAL_HTTP" "TOP_UP：需充值解锁"
else
  probe "FAL (flux)" "⚠️ 异常" "$FAL_HTTP" "$(echo "$FAL_BODY" | head -c 80)"
fi

# 3. SiliconFlow (视觉/图片/TTS 主力)
SF_ALL=$(curl -s -w $'\n%{http_code}' --max-time 15 \
  https://api.siliconflow.cn/v1/models -H "Authorization: Bearer ${SILICONFLOW_API_KEY}" 2>/dev/null)
SF_HTTP=$(echo "$SF_ALL" | tail -1)
SF_BODY=$(echo "$SF_ALL" | sed '$d' | head -c 120 | tr -d '\n')
if [ "$SF_HTTP" = "200" ]; then
  probe "SiliconFlow (vision/img/tts)" "✅ OK" "$SF_HTTP" "key 有效"
elif echo "$SF_BODY" | grep -q "401\|Unauthorized"; then
  probe "SiliconFlow (vision/img/tts)" "❌ key 失效" "$SF_HTTP" "401，需控制台重生成"
else
  probe "SiliconFlow (vision/img/tts)" "⚠️ 异常" "$SF_HTTP" "$(echo "$SF_BODY" | head -c 80)"
fi

# 4. DeepSeek 官方 (fallback 链参考)
DS_ALL=$(curl -s -w $'\n%{http_code}' --max-time 15 \
  https://api.deepseek.com/v1/models -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" 2>/dev/null)
DS_HTTP=$(echo "$DS_ALL" | tail -1)
DS_BODY=$(echo "$DS_ALL" | sed '$d' | head -c 80 | tr -d '\n')
if [ "$DS_HTTP" = "200" ]; then
  probe "DeepSeek 官方" "✅ OK" "$DS_HTTP" "key 有效"
else
  probe "DeepSeek 官方" "⚠️ 异常" "$DS_HTTP" "$(echo "$DS_BODY" | head -c 80)"
fi

# 5. EXA 搜索后端
EXA_ALL=$(curl -s -w $'\n%{http_code}' --max-time 15 \
  -X POST https://api.exa.ai/search \
  -H "Authorization: Bearer ${EXA_API_KEY}" -H "Content-Type: application/json" \
  -d '{"query":"test","num_results":1}' 2>/dev/null)
EXA_HTTP=$(echo "$EXA_ALL" | tail -1)
EXA_BODY=$(echo "$EXA_ALL" | sed '$d' | head -c 80 | tr -d '\n')
if [ "$EXA_HTTP" = "200" ]; then
  probe "EXA (搜索)" "✅ OK" "$EXA_HTTP" "key 有效"
else
  probe "EXA (搜索)" "⚠️ 异常" "$EXA_HTTP" "$(echo "$EXA_BODY" | head -c 80)"
fi

# 汇总
FAIL_COUNT=$(grep -c '❌' "$OUT" || true)
WARN_COUNT=$(grep -c '⚠️' "$OUT" || true)
{
echo ""
echo "## 汇总"
echo ""
echo "- ❌ 失败: ${FAIL_COUNT} 项 / ⚠️ 异常: ${WARN_COUNT} 项"
if [ "$FAIL_COUNT" -gt 0 ] || [ "$WARN_COUNT" -gt 0 ]; then
  echo "- ⚠️ 有异常项：见上方表格，需 sora 处理（重生成 key / 充值）"
else
  echo "- ✅ 全部关键 API 健康"
fi
echo ""
echo "_生成: api-probe cron · k (Hermes) · ${TODAY}_"
} >> "$OUT"

# stdout 交付逻辑：全健康 → 静默（no-agent 模式 empty stdout = silent）；有异常 → 输出报告全文提醒
if [ "$FAIL_COUNT" -gt 0 ] || [ "$WARN_COUNT" -gt 0 ]; then
  cat "$OUT"
fi
exit 0

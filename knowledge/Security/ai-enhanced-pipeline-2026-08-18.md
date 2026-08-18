# AI 增强挖洞流水线（2026-08-18 落地）

> 技能：`src-bug-hunting` → 「AI 增强流水线」章节 + `scripts/ai_secret_scan.py`
> 实测：正则 10 匹配 + LLM 9 条新增（base64 还原 AK / 数据库串 / Redis / 内网 IP）

## 核心工具
| 工具 | 位置/命令 | 说明 |
|:---|:---|:---|
| ai_secret_scan.py | 技能 scripts/ | 正则初筛 + LLM 深挖 + JSON/MD 报告 |
| unveilr | C:\Users\31954\tools\unveilr\ | 小程序反编译 wxapkg→JS |
| FOFA/Quake/Hunter | 网页/API | 三引擎资产测绘 |

## AI 审计流水线（6 步）
```
采集(URL/小程序) → 正则初筛(13类) → 可疑片段(关键词窗口) 
→ LLM深挖(OpenAI兼容API, 还原拆分/编码/混淆) → 云SDK验证(只读) → 报告(JSON/MD)
```

## 实测结论
- 正则抓硬编码（AK/SK/token/password/ghp/AIza/私钥/云AK）
- LLM 补盲区：base64 解码 AK、数据库连接串、Redis 密码、内网 IP
- **去重按 value**（LLM 同一密钥多类型标签会重复）
- **LLM 结果必须人工验证**（防幻觉），AK/SK 用 GetCallerIdentity 只读确认

## 关键命令
```bash
# URL 模式
python ai_secret_scan.py https://example.com --out report.json
# 本地目录 (小程序反编译产物) + LLM
python ai_secret_scan.py ./src --dir --llm --llm-key $DEEPSEEK_API_KEY \
  --llm-base https://api.deepseek.com/v1 --llm-model deepseek-chat
# 小程序反编译
unveilr.exe "C:\Users\31954\Documents\WeChat Files\<wx>\Applet\<appid>" -o ./out
```

## 红线
只测 SRC 授权 scope；AI 发现的密钥验证只读、不碰数据；不利用他人密钥。

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]

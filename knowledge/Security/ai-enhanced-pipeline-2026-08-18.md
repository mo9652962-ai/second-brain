---
title: "AI 增强挖洞流水线（2026-08-18 落地）"
type: note
domain: Security
status: active
tags: [knowledge/security]
source: null
date: 2026-08-18
---
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

## AI 报告合规红线（30+ SRC 联合规范，2026-07 正式版）★最重要

> 来源: 补天联合 30+ SRC 发布《AI生成漏洞报告提交规范》（字节/阿里/腾讯/百度/京东/滴滴/美团/快手/小米/360/蚂蚁/vivo/OPPO 等）
> 行业级标准: 所有主流平台统一执行

### 双面定位
✅ 鼓励 AI 使用（辅助/自动化挖掘，提升效率）
❌ 但报告必须「人工验证」后提交（AI 幻觉是最大问题）

### 3 条硬规则
1. 严格人工验证: 提交前评估+复现，报告必须含: 漏洞说明 + 详细复现步骤 + 完整 POC + 关键步骤及结果截图
2. 无效处理: AI 生成未经人工复现/无验证截图 → 直接驳回，不提供驳回原因
3. 违规处罚: >3个AI报告未人工验证=提醒 / >5个=扣信用值 / 严重=封号

### 报告必含 4 件套（缺一被驳）
漏洞说明 | 详细复现步骤 | 完整 POC | 关键步骤及结果截图

### 流水线合规改造（不变）
AI 允许: 信息收集/初步分析/报告草稿
人工必做: 复现验证(2-3次) + 补 POC/数据包 + 截图 + 描述核实
禁止: 自动生成报告直接提交（30+ 平台统一执行）

来源: 补天平台《关于提交AI生成漏洞报告的行为规范及违规行为通告》
影响: 所有使用 AI 辅助挖洞的白帽

### 3 条红线
1. 报告必须基于本人真实测试发现（真实/可复现/准确）
2. AI 辅助生成 → 必须人工逐条验证后才能提交
3. 禁止 AI 自动扫描 + 自动生成描述 + 直接批量上报

### 报告硬性要求
URL + 功能点 + 验证流程 + 完整数据包/POC + 验证证明（截图/视频）+ 文字描述
不得用 AI 通用模板代替真实测试流程

### 处罚梯度
| 违规 | 处罚 |
|:---|:---|
| >3 个 AI 报告未人工验证 | 提醒 |
| >5 个 AI 报告未人工验证 | 扣信誉值，严重封号 |
| 情节严重 | 直接封号 |

### 流水线合规改造
AI 允许: 信息收集 / 初步分析 / 漏洞线索
人工必做: 复现验证(2-3次) + 补 POC/数据包 + 截图 + 描述核实
禁止: ai_secret_scan.py 的 JSON/MD 报告直接提交平台
提交前清单: 每条发现手动验证 + 补截图 + 确认危害真实

## 红线
只测 SRC 授权 scope；AI 发现的密钥验证只读、不碰数据；不利用他人密钥。

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]

---
tags: [skill-audit]
---

# 双周技能审计 (2026-09-15)

## 📊 概览
- 总 Skills: 479 个（skills_list）/ 483 个（文件系统 SKILL.md 计数）
- 内置(bundled): 57 个（.bundled_manifest，不可改）
- 安装(hub): 26 个（@author/ 目录，不可改）
- 创建(agent): 400 个（可维护）

## ✅ 已更新（4 处 patch）

| Skill | 更新内容 |
|:---|:---|
| `primary-math-daily-practice` | 删除错位 VERIFIED 行（误把 `ark-code-latest`/火山引擎塞进数学练习文档技能，属会话串扰噪音；正确规则「标题无日期」保留） |
| `skill-library-audit` | 刷新自身文档的过时数字：bundled 69→57、hub 27→26、agent ~111→~400、skills_list 193→479；补充扫描盲区提示（depth-3 技能如 apple/*、devops/sdlc-review 不在 skill-audit-scan.py 覆盖内） |
| `hermes-configuration-patterns` | fallback 链格式示例补注：OpenRouter 已于 2026-07-26 移除（402 余额耗尽），示例仅为展示格式，实际最优链见 3.2.1 |
| `hermes-model-configuration` | 同上补注 + 指向 hermes-provider-matrix 当前链 |

## 🔍 发现

**过时陷阱扫描**（agent 技能全量 grep）：
- `deepseek-chat`/`deepseek-reasoner` 退役别名：0 处 ✅
- `ark-code-latest`（API 层未部署）：6 处均正确标注「未部署/勿写」，仅 primary-math-daily-practice 一处错位（已修）✅
- `doubao-vision-pro-128k`：仅出现在审计技能自身的陷阱清单里 ✅
- OpenRouter：provider 类技能（provider-matrix/low-cost-model-guide/model-supplier-strategy）已正确记录移除；仅 hermes-configuration-patterns 与 hermes-model-configuration 的格式示例缺提示（已补注）

**重复对（建议合并，待确认）**：
- `fangzhou-ark-config` (256L) vs `hermes/fangzhou-ark-setup` (152L)
- `hermes-search-config` (516L) vs `productivity/hermes-web-search-config` (178L)
- `local-llm-inference-windows` (120L) vs `mlops/local-llm-inference` (149L) vs `mlops/local-llm-windows-gpu` (89L) — 三件套
- `hermes/ai-api-provider-evaluation` (510L) vs `research/ai-api-relay-evaluation` (112L) vs `mlops/model-provider-testing` (123L) — 三件套
- 题库导入六件套：`edtech/epm-question-bank-import`、`esq-question-bank-import`、`exam-paper-web-import`、`exam-question-bank-import`、`exam-question-bank-ingestion`、`exam-question-import`（77-142L，同域高度重叠）
- 水墨 UI 五件套：`chinese-aesthetic-web-ui`、`design/ink-wash-ui-design`、`web-development/chinese-ink-wash-ui`、`ink-wash-ui-theming`、`ink-wash-web-ui-theming`
- 去 AI 味家族（creative/ 下 7 个 + hub 的 chinese-academic-writing 等）

**孤儿/盲区**：
- `apple/`（apple-notes、apple-reminders、findmy、imessage）——depth-3，扫描脚本不覆盖；.usage.json 全部 `stale` + 0 使用。sora 是 Windows 用户，AppleScript 技能大概率无用
- `devops/sdlc-review` ——depth-3，`active` 但 0 使用
- `@miknasbh-stack/` 空目录（find-skills 已迁 @guipi888）——可清理
- 111 个技能 0 使用（.usage.json），多为工具类参考技能（airtable/box/gif-search 等），暂不动

## 📋 建议操作

1. **确认合并**（优先级①）：题库导入六件套 → 保留 `exam-question-bank-import`（最长 142L）为主；`fangzhou-ark-config` vs `fangzhou-ark-setup` 保留长版
2. **确认删除/归档**（优先级②）：`apple/` 四技能（Windows 用户无用，stale）；`@miknasbh-stack/` 空目录
3. **暂缓**：水墨 UI / 去 AI 味 / 本地 LLM 家族——各有细分场景差异，建议保留观察
4. **扫描脚本增强**（下次可做）：skill-audit-scan.py 增加 depth-3 覆盖，避免 apple/devops 类盲区

> 注：所有合并/删除需 sora 确认后执行，本审计未做任何删除。

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]

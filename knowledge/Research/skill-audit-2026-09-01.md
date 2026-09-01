---
tags: [skill-audit]
created: 2026-09-01
type: audit
---

# 双周技能审计 (2026-09-01)

## 📊 概览
- 总 Skills: 446 个（manifest 82 + 非内置 364）
- 内置(bundled): 82 个（不可修改）
- 安装(hub): 27 个
- 创建(agent): 337 个
- 上次审计: 2026-08-12（agent 212 → 337，+125 增量巨大）

## ✅ 已更新（14 技能 / 21 处 patch）

### 退役模型别名修复（deepseek-chat / deepseek-reasoner → deepseek-v4-flash）
> 官方 API 直连已退役旧别名（2026-07-31），全部改为 `deepseek-v4-flash`

| 技能 | 改动 |
|:---|:---|
| chaoxing-automation | API 示例 `deepseek-chat` → `deepseek-v4-flash` |
| ai-assisted-vulnerability-hunting | LLM 提示 `deepseek-chat` → `deepseek-v4-flash` |
| src-bug-hunting | `--llm-model deepseek-chat` → `deepseek-v4-flash` |
| miniapp-reversing | 2 处 `deepseek-chat` → `deepseek-v4-flash` |
| wechat-miniapp-reversing | `--llm-model deepseek-chat` → `deepseek-v4-flash` |
| ai-code-review | 2 处（ocr 配置 + 端点说明，注明旧名已退役） |
| deepseek-api-clients | 日常模型 → `deepseek-v4-flash`；推理 → `deepseek-r1-250528` |
| tencentdb-agent-memory | `TDAI_LLM_MODEL` → `deepseek-v4-flash` |
| tencentdb-memory-ops | 同上 |
| hermes-workflow-preferences | ocr 配置 → `deepseek-v4-flash` |
| hermes-model-configuration | 成本表 `deepseek-chat` → `deepseek-v4-flash` |

### 豆包视觉模型名修复（doubao-vision-pro-128k → doubao-vision-pro-32k-241028）
> 旧文档常写 128k，实际模型名为 32k-241028

| 技能 | 改动 |
|:---|:---|
| hermes-smart-model-router | 已配置模型表 `128k` → `32k-241028` |
| hermes-configuration-patterns | 3 处（表格/故障现象/curl 测试） |
| hermes-model-configuration | 2 处故障排查示例 |

### OpenRouter 残留修复
| 技能 | 改动 |
|:---|:---|
| low-cost-model-guide | 价格表 3 个 OpenRouter 模型行标注「已于 2026-07-26 移除」+ 推荐表同步（消除内部矛盾：开头已写移除但表格仍推荐） |

## 🔍 发现

### 重复技能（需 sora 确认，暂不合并）
| 重复组 | 详情 | 建议 |
|:---|:---|:---|
| **cad**（3 份） | 顶层 `cad/SKILL.md`（111 行，8-22 增强版）+ `text-to-cad/cad/` + `text2cad-cad/`（两者逐字节相同，102 行旧版 7-31） | 保留顶层增强版，删 2 份旧副本 |
| **find-skills**（2 份） | @guipi888/find-skills v1.7（明示「已完全替代官方」）vs @miknasbh-stack/miknas-find-skills（官方旧版，SkillKit CLI） | 删 miknas 旧版，留 guipi888 |
| **image-generation-workflow** | 顶层 ai-image-generation（use 11，GenRouter 增强）vs creative/image-generation-workflow（338 行，use 29）内容高度重叠 | 合并到顶层 ai-image-generation |
| **fangzhou-ark-config** | 顶层（use 8）vs hermes/fangzhou-ark-setup（use 5）同主题 | 合并，留 use 高的 |
| **android-automation** | development/android-automation（use 3）vs hardware/uiautomator2-android-automation 同主题 | 合并 |
| **hermes-search-config** | hermes-search-config（use 94）vs productivity/hermes-web-search-config（use 11）同主题 | 合并，留 use 94 |

> 注：ai-image-generation 顶层 vs @okaris hub 版为**有意区分**（workflow 方法论 vs infsh CLI 工具执行），保留，不算重复。

### 空目录 / 遗留
- `@evolinkai/`、`@nitishgargiitd/` 空 hub 目录（无 SKILL.md）→ 可清理
- `openclaw-imports/` 仅剩 DESCRIPTION.md（08-12 报告的 4 组顶层副本已解决）→ 目录可删

## 📋 建议操作
- [ ] 合并 `cad` 三副本 → 保留顶层增强版（8-22，含千轮研究），删 text-to-cad/cad 与 text2cad-cad
- [ ] 删 @miknasbh-stack/miknas-find-skills（被 guipi888 完全替代）
- [ ] 合并 image-generation-workflow → 顶层 ai-image-generation
- [ ] 合并 fangzhou-ark-config / hermes/fangzhou-ark-setup
- [ ] 合并 android-automation / uiautomator2-android-automation
- [ ] 合并 hermes-search-config / hermes-web-search-config
- [ ] 清理空目录 @evolinkai @nitishgargiitd + openclaw-imports 残留
- [ ] 观察：agent 技能 8 月净增 ~125 个，建议下月审查技能库膨胀（加载变慢）

## 说明
- 社区 hub 技能（27 个）未修改——由原作者维护
- 内置技能（82 个）未修改——bundled 不可编辑
- 本次聚焦退役模型名 / 失效服务引用，全部为 agent 创建技能，可直接 patch
- 合并/删除均待 sora 确认后执行，本次未动

---
> 🗺️ 属于 [[MOC-Research]] · [[Home|🏠 Home]]

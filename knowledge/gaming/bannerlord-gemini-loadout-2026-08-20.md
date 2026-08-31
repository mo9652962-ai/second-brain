---
tags: [bannerlord, mods, gemini, 骑砍2, 电影级战斗]
domain: Gaming
status: fresh
date: 2026-08-20
---

# 骑砍2 e1.4.7 mod 装载 Gemini 评估落地（2026-08-20）

> 来源：Gemini 网页第二意见（问题包 gemini-batch-bannerlord-loadout.md）+ k 逐条查证
> 结论：Gemini 推荐基本可靠，两个重点 mod 已验证存在；版本兼容性有 nuance

## Gemini 方案（已验证部分）

### 风险与隐患（✅ 全部合理）

| 风险 | 结论 | 验证 |
|:---|:---|:---|
| ButterLib v2.2.2 偏旧 | → 升级 **v2.10.4**（官方支持 v1.0.x-v1.4.x beta）| ✅ 与技能记录一致 |
| CE + MarryAnyone 双重怀孕 | → 装 **CE 兼容补丁**（中文站 thread-2107106）| ✅ 技能已有记录 |
| MarryAnyone 免费版 1.4.6 vs 1.4.7 beta | 偶发 Hero.Spouse 空指针 → 赞助版或避免高频代孕 | ⚠️ 合理，按建议执行 |
| HotButter 勿升 v2.x | v2 需 Better Core，1.4.7 未确认 → 保持 v1.3.14 | ✅ 与技能「观望」一致 |

### 画面路线决断（✅ 采纳）

- **主存档推荐 OSA 路线**（Open Source Armory v2.0.1，download_2565，明确支持 1.4.x，8G）
- GT_CarbonBody+KOTK 只在**新档试错**（1.4.7 下骨骼拉伸 T-Pose 风险 + 拔除损坏存档）
- 漂亮女服装 download_238 纯网格替换安全

### 增强 mod 验证结果

| mod | Gemini 推荐 | k 查证 | 结论 |
|:---|:---|:---|:---|
| **RTS Camera**（nexus 355 / 中文站 download_2000）| 自由视角/电影运镜 | ✅ **明确支持本体 1.4.7**，v5.4.15（2026-08-06 更新），中文站直链 22 万下载，作者中国人 | 🟢 **直接装** |
| **DismembermentPlus**（nexus 2190 / 中文站 thread-2078518）| 肢解+慢动作 | ⚠️ 存在但中文站标注 z1.2.7/1.1.5；**Save Game friendly（可加可删）**；Steam 工坊有 v1.4.8 版（2875093027）；600MB 完全版/150MB 轻量版 | 🟡 可试（存档无风险）|
| **CE-Marriage Patch**（thread-2107106）| 修双重怀孕 | ✅ 技能已记录 | 🟢 必装 |
| **Arena Experience** | 角斗补充 | ❌ 未验证（Gemini 名字可能不准）——需查证 Improved Tournaments 等 | ⚪ 待查 |
| **Reshade 预设** | 电影调色 | ✅ 外部注入零坏档 | 🟢 可选 |

## 执行顺序（Gemini 3 步走）

1. **底层加固**：ButterLib → v2.10.4 + CE 兼容补丁
2. **视听增强**：RTS Camera + DismembermentPlus + Reshade
3. **装备扩充**：OSA（主存档）/ GT+KOTK（新档试错）

## 最终推荐排序表（Gemini 完整版）

```
Harmony → ButterLib(升 v2.10.4) → UIExtenderEx → MCM → [官方模块]
→ RTS Camera → zBeauties → HotButter v1.3.14 → HotScenes v2.4.2
→ MarryAnyone → CaptivityEvents v1.4.5.1400 → CE_MarryAnyone_Patch
→ BirthAndDeath → ComplexCharacters → Ludus → [Arena Experience?]
→ ChaosBattle → [DismembermentPlus?] → AutoHideoutAttack → LivingWanderers
→ FQ_Editor2 → FastMode/CustomBattle → [OSA] → [漂亮女服装/KOTK] → [GT_CarbonBody 最底]
```

---
*k (Hermes) 2026-08-20 · 问题包 → Gemini → 逐条验证落地*

---
> 🗺️ 属于 [[MOC-Inbox]] · [[Home|🏠 Home]]

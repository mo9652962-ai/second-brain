---
tags: [bannerlord, mods, gemini, 骑砍2, 升级方案]
domain: Gaming
status: fresh
date: 2026-08-20
---

# 骑砍2 e1.4.7 绅士体系完整升级方案（整合版）

> 两份 Gemini 回答整合 + k 查证 + 用户决策（2026-08-20）
> 用户决策：**升级 HotButter v2 体系**（第二份迁移路径采纳，第一份风险警示作备注）
> 完整可操作文档：`桌面/骑砍2-绅士体系完整升级方案-20260820.md`

## 一、现状基线
- e1.4.7 beta；前置四件套（ButterLib **v2.2.2** 旧）+ BLSE
- 绅士：HotButter v1.3.14 + HotScenes v2.4.2 + CE v1.4.5.1400 + MarryAnyone + BirthAndDeath
- 备份：`/d/ModBackup-20260820/`（存档 + 24 mod 清单 + HotButter v1.3.14 回滚目录）

## 二、风险清单（两份回答合并）
1. ButterLib v2.2.2 旧 → 升 v2.10.4（多事件 Tick 卡顿/闪退）
2. CE+MarryAnyone 双重怀孕 → **CE 兼容补丁必装**（thread-2107106）
3. MarryAnyone 免费版 1.4.6 vs 1.4.7 → 偶发空指针，避免高频代孕
4. HotButter v2 + Better Core 1.4.7 未确认 → 备份兜底 + 旧档测试 + 可回滚
5. GT+KOTK 1.4.7 T-Pose/拔除毁存档 → 只在新档试错

## 三、执行 5 步
1. 备份 ✅（已完成）
2. 核心升级：ButterLib 2.10.4 + Better Core（nexus 6367）+ HotButter v2.0.5（nexus 6389，**删旧装新**）+ CE 补丁
3. 后宫：MarryAnyone 深度启用（多配偶/俘虏娶妻/代孕/对赌）
4. 外观：路线 A（GT+KOTK 新档试错）/ 路线 B（漂亮女服装+OSA 主存档直装）
5. BLSE 校验排序 → 旧档测试 → 崩溃回滚

## 四、排序表（完整）
Harmony → ButterLib(2.10.4) → UIExtenderEx → MCM → 官方模块 → BetterCore → zBeauties → HotButter v2 → HotScenes → MarryAnyone → CE → CE_MarryAnyone_Patch → BirthAndDeath → ComplexCharacters → Ludus → [Arena?] → ChaosBattle → [DismembermentPlus?] → RTS Camera → AutoHideoutAttack → LivingWanderers → FQ_Editor2 → FastMode → [OSA] → [漂亮女服装] → [KOTK 在 GT 上] → [GT_CarbonBody 最底]

## 五、关键决策
| 决策 | 结论 |
|:---|:---|
| HotButter v2 | ✅ 升（用户决定，备份兜底）|
| CE 补丁 | ✅ 必装 |
| MarryAnyone | 免费版先用，避免高频代孕；有预算赞助版 |
| 画面 | 主存档 B 路线，A 只新档试错 |
| RTS Camera | ✅ 装（明确支持 1.4.7）|

---
*k 2026-08-20*

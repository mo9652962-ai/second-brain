---
tags: [skyrim, multiplayer, modlist, guide]
date: 2026-08-02
---

# 🎮 天际特别版 2 人联机 + 美化模组下载清单

> 场景：2 人基于原版联机 + 人物/环境美化
> 方案：Skyrim Together Reborn + 客户端侧美化（无需双方同步）
> 生成日期：2026-08-02 · 基于社区 2026 年实践

## ⚠️ 核心原则（先读！）

1. **联机 mod = Skyrim Together Reborn**（唯一活跃维护的方案）
2. **美化 mod 只选"客户端侧"**（纹理/身形/发型/皮肤）——只管自己画面，不需要双方同步，朋友不装也不冲突
3. **避免**：脚本类、玩法大修、任务/地点大改、随从管理（不同步会出问题）
4. **先纯净版联机跑通 → 再加美化 → 逐步验证**

---

## 📋 第一步：联机核心（必须）

| # | Mod | Nexus 链接 | 说明 |
|:-:|-----|-----------|------|
| 1 | **Vortex** 模组管理器 | https://www.nexusmods.com/about/vortex/ | 免费，装 mod 用 |
| 2 | **Address Library for SKSE Plugins** | https://www.nexusmods.com/skyrimspecialedition/mods/32444 | SKSE 基础库，**必需** |
| 3 | **Skyrim Together Reborn** | https://www.nexusmods.com/skyrimspecialedition/mods/69993 | 联机本体，选 "All in One (Anniversary Edition)" 包 |

**服务器 3 选 1**：
- 🥇 **PlayTogether.gg**（免费网页私服，一键启动，给 IP+密码）——首选
- 🥈 **Hamachi** 虚拟局域网（两人直连，主机输 localhost）
- 🥉 **自建 Docker**（镜像 `tiltedphoques/st-reborn-server`，需 24h 开机）

---

## 🎨 第二步：人物美化（客户端侧 ✅）

| # | Mod | Nexus 链接 | 联机兼容性 |
|:-:|-----|-----------|-----------|
| 1 | **CBBE** 身形 | https://www.nexusmods.com/skyrimspecialedition/mods/198 | ✅ 社区确认安全（纯身形） |
| 2 | **Fair Skin Complexion** 皮肤 | https://www.nexusmods.com/skyrimspecialedition/mods/516 | ✅ 纯纹理，安全 |
| 3 | **KS Hairdos** 发型 | https://www.nexusmods.com/skyrimspecialedition/mods/6817 | ⚠️ 发型可用，但改 facegen 的头发在 1.8 前有兼容风险（见下方说明） |
| 4 | ~~Bijin AIO~~ NPC 美化 | ~~https://www.nexusmods.com/skyrimspecialedition/mods/1986~~ | ⚠️ **官方标记 "Can cause issues"**（`#111`）：改 facegen → NPC 土豆脸/紫发。**1.8 已部分修复**（re-enabled bUseFaceGenPreprocessedHeads），但仍有风险，建议**先不加** |

> 💡 **facegen 规则**：凡是**替换 NPC 脸部网格/预计算头型**的 mod（Bijin、Pandorable、NPC 美化包）在联机下都可能不同步。纯**玩家角色**美化（CBBE 身形、皮肤纹理、KS Hairdos 发型）只影响自己画面，安全。

> 🎯 **NPC 美化安全替代（不碰 facegen）**：
> - **Total Character Makeover**（[Nexus 1037](https://www.nexusmods.com/skyrimspecialedition/mods/1037)）：**全种族皮肤/眼睛/眉毛/胡子/伤疤纹理，官方声明 "Changes to individual NPCs: NO"**——纯纹理，联机安全 ✅
> - **The Eyes of Beauty**（Nexus 13722）：眼睛纹理，安全
> - **Beards of Power**（可选）：胡子网格，只影响男性
> - 想要"脸型更好看"但又怕风险 → 装完 **先单人模式测试**，确认 NPC 无塑料脸/紫发再联机

## 🏔️ 第三步：环境美化（客户端侧 ✅）

| # | Mod | Nexus 链接 | 联机兼容性 |
|:-:|-----|-----------|-----------|
| 1 | **Skyland AIO** 全环境纹理 | https://www.nexusmods.com/skyrimspecialedition/mods/34179 | ✅ 纯纹理，官方 FAQ 认可图形 mod |
| 2 | **SMIM** 网格增强 | https://www.nexusmods.com/skyrimspecialedition/mods/659 | ✅ 纯网格，安全 |
| 3 | **Realistic Water Two** 水体 | https://www.nexusmods.com/skyrimspecialedition/mods/2182 | ✅ 纯纹理/网格 |
| 4 | **Azurite Weathers** 天气 | Nexus 搜 "Azurite Weathers" | ✅ 官方 FAQ "图形 mod 一般没问题"；追踪器无负面记录 |
| 5 | **Lux** 光照 | https://www.nexusmods.com/skyrimspecialedition/mods/43158 | ✅ **官方追踪器明确标记 "Mod IS compatible"**（#48）！Lux Orbis/Via/补丁都可用 |

---

## 🚫 第四步：避坑清单（联机会出问题）

| 类别 | 例子 | 原因 |
|------|------|------|
| UI 类 | SkyUI（旧版） | 脚本冲突 |
| 玩法大修 | Ordinator、战斗大修 | 不同步 |
| 随从管理 | AFT、EFF | 不同步 |
| 地点大改 | Cities of the North | 需双方同版+同步风险 |
| 生存模式 | Frostfall | 状态不同步 |

> ✅ **安全判断法**：纯纹理/网格/身形/发型（无脚本）→ 安全；带 .esp 游戏逻辑 → 小心

---

## 🛠️ 安装顺序（推荐）

```
1. 双方 Steam 启动一次 SSE（生成配置）
2. 装 Vortex → 管理 SSE
3. Vortex 装 Address Library → Reborn 本体
4. 纯净版联机测试（PlayTogether.gg 建服 → 双方连接）
5. 确认联机 OK 后，Vortex 逐个加美化（CBBE → Fair Skin → KS Hairdos → Skyland → SMIM → RWT）
6. 每加 2-3 个 mod 联机测一次，出问题就关掉排查
```

---

## 🔗 参考资料

- 官方 Wiki：https://wiki.tiltedphoques.com/tilted-online/
- 安装视频（2026）：https://www.youtube.com/watch?v=Lpdt474o7Sg
- 图文教程：https://www.windowscentral.com/gaming/skyrim-together-reborn-mod-how-to-play-download-install-and-make-a-server
- 兼容性清单视频：https://www.youtube.com/watch?v=JpAI_TX2WAc

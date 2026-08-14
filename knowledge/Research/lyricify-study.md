---
tags: [research, github, article-study, lyricify, tools]
created: 2026-07-31
status: absorbed
source: https://github.com/WXRIW/Lyricify-App
---

# Lyricify — 研究笔记

> 来源：小黑盒文章（软件格律诗 07-02）· 2026-07-31 验证 + 评估

## 项目验证

| 项 | 值 |
|----|-----|
| Lyricify 4 | v4.3.52（2026-07-14 发布，活跃维护） |
| Lyricify Lite | v1.2.2（2026-07-01 同期更新） |
| Lyricify-Lyrics-Helper | **193★，Apache-2.0，C#**（歌词核心开源） |
| Lyricify-App | 主应用仓库（闭源分发，GitHub releases） |
| 平台 | Lyricify 4: Windows + Spotify；Lite: Windows 全播放器；Mobile: 安卓/iOS/Mac |

## 三版本区分

| 版本 | 平台 | 适配播放器 | 核心功能 |
|------|------|-----------|---------|
| Lyricify 4 | Windows | 仅 Spotify | 灵动词岛/妙控条/完整歌词管理 |
| Lyricify Lite | Windows | 所有 SMTC 播放器（QQ音乐/网易云/酷狗/Foobar） | 灵动词岛+桌面歌词，轻量 |
| Lyricify Mobile | 安卓/iOS/Mac | Spotify/Apple Music | 锁屏歌词/小组件/多端同步 |

## 开源状态（重要发现）

**主应用源码未全开源**——只有歌词处理库（Lyricify-Lyrics-Helper）Apache-2.0 开源：
- 歌词解析：LRC/QRC/KRC/YRC/TTML/Syllable 等 8 种格式
- 歌词搜索：QQ音乐/网易云/酷狗/汽水/Apple Music/Musixmatch
- 对唱识别、YRC 优化、Explicit 处理

## 评估决策

| 选项 | 决策 | 理由 |
|------|:---:|------|
| 安装 Lyricify 4/Lite | ❌ | **用户当前无任何音乐播放器**——Lyricify 是歌词工具非播放器，无前置 = 无意义 |
| 安装 Lyricify Mobile | ❌ | 同上，且 Android 真机主要用于自动化测试 |
| **技术参考** | ✅ | Lyrics-Helper 的歌词解析库架构（多格式/多源/优化）可参考 |

## 技术参考价值（Lyricify-Lyrics-Helper）

如果未来做歌词相关项目（B站视频歌词字幕、音乐可视化）：
- 8 种歌词格式解析器（LRC/QRC/KRC/YRC/TTML/Syllable/Lines/Spotify JSON）
- 6 个歌词源搜索（QQ/网易云/酷狗/汽水/Apple/Musixmatch）
- 歌词优化：SyncDowngrade（逐字→逐行降级）/ OffsetHelper / 对唱识别

## 结论

- 项目真实且活跃（4 代 + Lite 双线并行更新）
- **对我们 = 无前置条件的工具，当前不装**（用户无音乐播放器）
- 技术参考价值已存档（Lyrics-Helper 多格式解析架构）
- 若未来安装 Spotify/QQ音乐 + 想提升歌词体验，装 Lyricify Lite（轻量通用）即可

---
> 🗺️ 属于 [[MOC-Research|🔬 研究笔记]] · [[knowledge-map|🗺️ 知识地图]]

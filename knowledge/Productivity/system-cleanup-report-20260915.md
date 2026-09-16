---
tags: [cron, maintenance, system-cleanup, windows, report]
title: 系统清理报告 2026-09-15
type: report
created: 2026-09-15
status: adopted
---
# 系统清理报告 2026-09-15

**结论：三轮累计释放约 25 GB，C 盘已用 338G → 313G（使用率 76% → 70%，可用空间 110G → 135G）。**
本轮（含用户两轮「继续」深挖）是近期释放量最大的一轮，首轮即清出 22GB 用户临时目录堆积，后续两轮又分别清出 ~2.1GB 与 ~1.8GB 的安装包/构建缓存/模型缓存残留。

## 清理明细（三轮合计）

### 第一轮（~23.8 GB）

| 类别 | 路径 | 释放 |
|---|---|---|
| 用户 Temp | `%TEMP%` | ~22.13 GB |
| Windows Temp | `C:\Windows\Temp` | ~16.9 MB |
| pip / uv / npm 缓存 | `%LOCALAPPDATA%\...` | ~1.13 GB |
| Chrome + Edge 浏览器缓存 | `...\Default\Cache` 等 | ~538 MB |
| Hermes 轮转旧日志 | `hermes\logs\*.log.1` | ~7.2 MB |
| 工具安装包残留 zip | `EasyCLIProxyAPI-*.zip` | ~30 MB |

### 第二轮（~2.1 GB）

| 类别 | 路径 | 释放 |
|---|---|---|
| Windows Update 下载缓存 | `SoftwareDistribution\Download` | ~564 MB |
| Gradle 构建缓存 | `%USERPROFILE%\.gradle\caches` | ~706 MB |
| pnpm store prune | `%LOCALAPPDATA%\pnpm` | ~827 MB |

### 第三轮（~1.8 GB）

| 类别 | 路径 | 释放 |
|---|---|---|
| 软件安装包目录 | `Desktop\软件安装包`（DeepSeek Harness + 墨题 beta.15 安装包） | ~461 MB |
| SolidWorks 安装包 | `Downloads\SolidWorksSetup.exe` | ~209 MB |
| ModelScope 模型缓存 | `%USERPROFILE%\.cache\modelscope` | ~900 MB |
| Windows CBS 日志 | `C:\Windows\Logs\CBS` | ~260 MB |

## 安全边界（明确未动，绝不清理）

| 项 | 大小 | 原因 |
|---|---|---|
| 桌面「备份」目录 | 10.5 GB | 用户主动备份（图片视频.zip 7.1G + Documents/Download 备份 + 墨题历史 APK） |
| Documents | 32 GB | 工作文档/项目 |
| Pictures | 7.5 GB | 图片素材 |
| Downloads 主体 | 5.4 GB | 用户下载文件 |
| codex-runtimes | 1.8 GB | Codex 运行环境（编码委派依赖） |
| .vscode extensions | 1.0 GB | VS Code 扩展本体 |
| huggingface 模型缓存 | 629 MB | faster-whisper（视频转写 skill 在用）+ Qwen-Image |
| 桌面 Hermes.exe | 205 MB | 疑似安装包残留，用户未确认，保留 |

## 保留说明（删不掉的已知项）

- **回收站 `.xxx` 残留 538.7 MB**：非标准回收站条目，被进程持有句柄，`Clear-RecycleBin` 与 `Remove-Item` 均无效，需重启持有进程（浏览器/下载工具）后方可清，属正常现象。
- **hiberfil.sys / pagefile.sys**：均不存在（休眠已关闭、虚拟内存未设置在 C 盘），无清理空间。

## 后续建议

- 本轮释放量大主因是用户 Temp 堆积 22GB（大文件构建/解压残留），建议每 2-3 周跑一次常规清理即可。
- 若 C 盘仍需进一步瘦身，剩余大头均为用户真实数据/备份，需用户主动归档到 D 盘（个人文件夹转移），而非清理垃圾。

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]
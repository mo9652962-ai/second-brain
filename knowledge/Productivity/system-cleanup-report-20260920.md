---
tags: [system-cleanup, productivity, report]
type: report
created: 2026-09-20
title: 系统清理报告 2026-09-20
---
# 系统清理报告 2026-09-20

**结论：共释放约 2.2 GB，C 盘 373G/448G（84%）——5 天内从 313G 涨到 374G 的 61G 增长主因已定位（Codex 桌面版内置 Docker vhdx 42.5G），清理后未回到低水位是因为该大头保留未动。**

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|---|---|---|---|---|
| Electron updater 缓存（7 个应用） | `%LOCALAPPDATA%\*-updater\installer.exe` | ~1.85 GB | ~0.2 MB | ~1.85 GB |
| OpenSquilla 更新安装包 | `%APPDATA%\@opensquilla\desktop-electron\update-downloads` | 747 MB | 0 | ~747 MB |
| 用户 Temp | `%LOCALAPPDATA%\Temp` | 531 MB | 88 MB | ~443 MB |
| BurpSuite 更新包 | `%APPDATA%\BurpSuite\updates` | 410 MB | 0 | ~410 MB |
| npm 缓存 + _npx | `%LOCALAPPDATA%\npm-cache` | 211 MB | ~10 MB | ~200 MB |
| Chrome/Edge 缓存 | Cache + Code Cache + CacheStorage | 54 MB | 0 | ~54 MB |
| pip / uv 缓存 | pip-cache / uv-cache | ~30 MB | ~0 | ~30 MB |
| Windows Temp | `C:\Windows\Temp` | 5.7 MB | 0 | ~5.7 MB |
| Hermes 轮转日志 | `hermes\logs\*.1/.2/.3` | 36 MB | ~29 MB | ~7 MB |
| CBS 组件日志 | `C:\Windows\Logs\CBS\*.log` | 21 MB | 0 | ~21 MB |
| Windows Update 下载缓存 | `SoftwareDistribution\Download` | 17 MB | 0 | ~17 MB |

**本次发现的新清理目标**：Electron 应用 updater 目录（7 个应用共 ~1.85G 旧 installer.exe 残留，应用本体已装完，删除安全，下次更新自动重下）。antigravity-updater（287M）因 installer 日期为昨天（可能刚更新）保留。

## 保留未动（说明）

| 项目 | 大小 | 原因 |
|---|---|---|
| ⛔ Codex 桌面版 Docker vhdx（`Packages\OpenAI.Codex_*\LocalCache\Local\Docker\wsl\disk\docker_data.vhdx`） | **42.5 GB** | 61G 增长主因（9/17 创建）。Codex 是核心编码工具，其内置 Docker 沙箱数据盘不可擅删；若确认不用 Codex 沙箱/容器，可在 Codex 设置中清理或卸载该应用组件，可释放 ~42.5G |
| ⛔ Docker Desktop docker_data.vhdx（`%LOCALAPPDATA%\Docker\wsl\disk`） | 10.8 GB | 本机无虚拟化 Docker 实际不可用，理论纯白占；但 9/17 有活动痕迹，删前需用户确认（卸载 Docker Desktop 或 WSL 卸载发行版） |
| ⛔ WSL ext4.vhdx（`%LOCALAPPDATA%\wsl\{GUID}`） | 2.4 GB | 9/20 有活动，疑似在用的 WSL 发行版 |
| hermes state-snapshots（20260910-pre-update） | 791 MB | 更新前安全网快照，仅 1 份，保留 |
| hiberfil.sys / pagefile.sys / swapfile.sys | 6.7G / 26.3G / 16M | 系统文件只报告不动；`powercfg /h off` 可省 ~6.7G（关休眠/快速启动，需确认） |
| Desktop 备份目录（`备份` 等） | 10.8 GB | 用户主动备份，绝不碰 |
| .cache（codex-runtimes 1.8G + 模型缓存） | 3.4 GB | 运行环境/可能引用，保留 |
| 回收站 `.xxx…` 残留（188M+177M 等） | ~540 MB | 进程持有句柄清不掉（已知坑 6/8），重启浏览器类进程后可清 |

## 可释放建议（下次手动确认后执行）

1. **Codex 桌面版 Docker vhdx 42.5G**——确认 Codex 沙箱功能不用后，在 Codex 应用内清理容器/镜像或卸载重装，立省 ~42.5G（C 盘可回到 65% 以下）
2. **Docker Desktop 10.8G**——本机无虚拟化，Docker 实际无法使用，卸载 Docker Desktop 立省
3. **`powercfg /h off`**——省 6.7G（代价：关休眠/快速启动）
4. 回收站残留重启后重试清一次

## 关键发现（61G 增长的真相）

9/15 清理后 used=313G → 9/20 用前 used=374G（+61G）。定位结果：
- Codex 桌面版内置 Docker 数据盘 42.5G（9/17 创建）≈ 70%
- Docker Desktop 10.8G + WSL 2.4G ≈ 21%
- 其余为常规增量（updater/缓存/日志）

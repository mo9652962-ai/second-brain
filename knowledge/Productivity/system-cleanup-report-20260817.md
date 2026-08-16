---
tags: [清理报告, 系统维护, 2026-08]
domain: Productivity
---

# 系统清理报告 2026-08-17

**结论：C 盘释放约 1 GB（226G → 225G 已用，使用率 51% 不变——总量 448G）。D 盘另有机会清理 2.4G（待确认）。**

## 清理明细

| 类别 | 路径 | 清理前 | 清理后 | 释放 |
|:---|:---|:---|:---|:---|
| uv 缓存 | AppData/Local/uv/cache | 728M | 0 | **~678 MiB** |
| Chrome Code Cache | .../Chrome/Default/Code Cache | 294M | 0 | **294M** |
| Chrome Service Worker | .../CacheStorage | 316M | 4K | **316M** |
| pip 缓存 | AppData/Local/pip/cache | 720K | — | 少量 |
| npm 缓存 + _npx | AppData/Local/npm-cache | 1.3M | 0 | 少量 |
| 用户 Temp | %TEMP% | 207M | 101M | ~106M |
| 系统 Temp | C:\Windows\Temp | 12M | — | 少量 |
| Edge 缓存 | .../Edge/Default/Cache | 9.2M | 0 | 9.2M |
| 回收站 C | C:\$Recycle.Bin | 539M | 539M | 0（被占用残留）|
| 回收站 D | D:\$Recycle.Bin | 37M | 29M | 8M |
| Hermes 轮转日志 | hermes/logs/agent.log.{1,2,3} | — | 删除 | 少量 |

## 保留未动（说明）

| 项 | 大小 | 原因 |
|:---|:---|:---|
| **unsloth_env（D 盘）** | **2.4G** | ⏸️ 已暂停项目残留（torch cu130 wheel 1.9G + venv）。**待 sora 确认删除**——wheel 重下需 ~13 分钟，若近期可能重启微调可保留 |
| hermes-agent 目录 | 9.2G | 安装本体（venv 2.7G + node_modules + .git），运行必需 |
| 回收站残留 | 539M | 被进程持有句柄的已删 $R 文件，Clear-RecycleBin 删不掉（重启持有进程后可清），已知正常 |
| pagefile/hiberfil | — | 系统文件不动 |

## 备注

- 本轮未做桌面/文件夹整理（无此需求）
- Chrome Code Cache/Service Worker 清空不影响登录态（只影响缓存图片/脚本，下次访问自动重建）

---
> 🗺️ 属于 [[MOC-Productivity]] · [[Home|🏠 Home]]

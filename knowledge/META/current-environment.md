---
type: current-state
verified_at: 2026-09-20
status: active
tags: [meta, environment, fact-source]
---

# 当前运行环境

> **事实源**：本文只记录**当前可验证状态**。数值随时间变化，引用时请以本文为准，不要在其他文档里写死。
> 下次复核：环境变更时（装/卸 Docker、启停 WSL、换机器）。

## 虚拟化与 WSL

| 项 | 实测值 | 验证方式 |
|:---|:---|:---|
| HypervisorPresent | **True** | `Get-CimInstance Win32_ComputerSystem` |
| hns 服务 | **Running** | `Get-Service hns` |
| vmcompute 服务 | **Running** | `Get-Service vmcompute` |
| WSL 版本 | **2.7.10.0** | `wsl --version` |
| WSL 内核 | **6.18.33.2-2** | `wsl --version` |
| Windows 版本 | **10.0.26200.9457** | `wsl --version` |

**已注册发行版**（均为 Stopped，按需启动）：

| 发行版 | 状态 | WSL 版本 |
|:---|:---|:---|
| Ubuntu-22.04 | Stopped | 2 |
| docker-desktop | Stopped | 2 |

**结论：本机具备完整的 Hyper-V / WSL2 虚拟化基础设施。**

**运行时实证**（不只是读属性）：
```bash
wsl.exe -d Ubuntu-22.04 -e uname -a
# Linux nk 6.18.33.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC ... x86_64 GNU/Linux
# → WSL 发行版真实启动成功
```

> ⚠️ **历史文档中的「本机无虚拟化」是 2026-09 之前的结论，与当前实测冲突，已作废。**

### ⚠️ 属性陷阱：不要用 `VirtualizationFirmwareEnabled` 判断

历史文档（如 `src-ai-automation-3tools-2026-08-21.md`）曾据以下属性判定「无虚拟化」：

| 属性 | 实测值 | 能否用于判断 |
|:---|:---|:---|
| `VirtualizationFirmwareEnabled` | **False** | ❌ **假阴性，会误判** |
| `VMMonitorModeExtensions` | **False** | ❌ 同上 |
| `SecondLevelAddressTranslationExtensions` | **False** | ❌ 同上 |
| `HypervisorPresent` | **True** | ✅ **正确判据** |

**为什么是假阴性**：当 Hyper-V/hypervisor **已经激活**时，宿主 Windows 自身运行在 hypervisor 之上，
CPU 的 VT-x/AMD-V 特性不再直接暴露给宿主 OS，这三个属性就会报 `False`。
**它们是「虚拟化未启用」的指示器，不是「硬件不支持」的指示器** —— 而这里恰恰是已启用。

**正确判据**：`Win32_ComputerSystem.HypervisorPresent` + 运行时实证（`wsl -e uname -a` 能返回内核版本）。

## Docker —— 三层状态（不要合并成一句）

Docker 的「能不能用」是三层独立的判断，必须分开描述：

| 层 | 状态 | 证据 |
|:---|:---|:---|
| **① 虚拟化基础设施** | ✅ **就绪** | HypervisorPresent=True；vmcompute/hns Running |
| **② Docker CLI** | ✅ **已安装** | `Docker version 29.8.0, build 88096ef` |
| **③ Docker Daemon** | ❌ **未运行** | Docker Desktop 进程未启动；`npipe:////./pipe/dockerDesktopLinuxEngine` 不存在 |

**CLI 位置**（非标准路径，注意）：
```
%USERPROFILE%\AppData\Local\Programs\DockerDesktop\resources\bin\docker.exe
```
> 标准路径 `C:\Program Files\Docker\Docker\Docker Desktop.exe` **不存在**——Docker Desktop 是 per-user 安装。
> 该路径已在用户 PATH 中（`Get-Command docker` 可解析），git-bash 与 PowerShell 均可调用。

**当前可用性判定**：

```bash
docker info
# failed to connect to the docker API at npipe:////./pipe/dockerDesktopLinuxEngine
# → daemon 未运行，容器操作不可用
```

**要启用 Docker**：启动 Docker Desktop → 等 daemon 就绪 → `docker info` 返回 ServerVersion 即可用。

**不要写成**：
- ❌「本机无 Docker」（CLI 明明在）
- ❌「Docker 完全正常」（daemon 没起）
- ✅「虚拟化就绪，CLI 已装，daemon 未运行——启动 Docker Desktop 后可用」

## 知识库文件数量

> 数量随文件同步变化。**引用时请以本节为准**，或跑审计脚本，不要在其他文档写死。

| 位置 | 数量 | 说明 |
|:---|:---|:---|
| `knowledge/` | **669** 个 `.md` | 知识主体 |
| `memory/` | **379** 个 `.md` | 历史记忆（只读，见下） |
| `.hermes/` | **4** 个 `.md` | Hermes 工作区文档 |
| `skills/` | **131** 个 `.md`（其中 `SKILL.md` **31**） | OpenClaw 遗产技能区 |
| `AppData/Local/hermes/skills/` | **503** 个 `SKILL.md` | **Hermes 实际加载入口** |

> 技能目录的权威定义见 [[knowledge/META/knowledge-sources]]。

## 本机硬件约束（仍有效）

| 项 | 值 |
|:---|:---|
| GPU | RTX 4060 8GB |
| 内存 | 16GB（易卡；`RAMMap64 -E` 清 Standby 可缓解） |
| 虚拟化 | ✅ 可用（2026-09-20 复核，此前记录已过期） |

## 相关

- [[knowledge/META/knowledge-sources]] — 路径与数量事实源
- [[knowledge/META/current-model-status]] — 模型与 API 事实源
- [[index]] — 知识库路由层

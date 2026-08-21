---
tags: [nmap, security, 端口扫描, 渗透测试, 教程]
domain: Security
status: fresh
date: 2026-08-20
---

# Nmap 保姆级教程笔记（安全小子 · 抖音 2026-08-20）

> 来源：抖音 @安全小子《Kali 保姆级教程之 Nmap 全流程扫描实战》（33 分钟，03/10）——SenseVoice 分块转写 7010 字
> 技能：`security/nmap-scanning`（已建）
> 合规：只扫授权目标/本地靶场

## 课程结构（7 节内容）

1. 环境准备（VMware 桥接模式 → 同局域网）
2. 扫描单个 IP（默认 1000 常用端口）
3. 扫描整个网段（-sn 主机发现 + 厂商识别）
4. TCP vs UDP 通信原理
5. 三种扫描类型：-sT 全连接 / -sS 半开（默认）/ -sU
6. 全端口 -p- + 时间模板 -T4
7. 服务版本探测 -sV + 组合实战

## 核心知识点

### 单机扫描
```
nmap 192.168.1.38
→ Starting Nmap / Nmap scan report / 5 个 open 端口 / 995 closed
→ 135/139/445 = Windows 共享/打印；902/903 = VMware
```

### 网段资产盘点（重点——SRC/内网渗透第一步）
```
nmap -sn 192.168.1.0/24
→ 在线设备 IP + 主机名 + 厂商（小米/OPPO/联想/iPhone/ipcam 摄像头）
→ 联想/华硕 → 查高危系统服务；物联设备 → 默认弱口令/公开漏洞
```

### 三种扫描类型对比
| 类型 | 命令 | 原理 | 优点 | 缺点 |
|:---|:---|:---|:---|:---|
| 全连接 | `-sT` | 完整三次握手+断开 | 结果准（closed 显 refused）| 系统日志完整记录——易暴露 |
| 半开 | `-sS` | 不回确认包就断开 | 隐蔽（closed 显 reset），**nmap 默认** | 略不如 -sT 准 |
| UDP | `-sU` | 无确认机制 | 能扫 UDP 服务 | 慢、结果 open\|filtered 模糊 |

### 提速与全面
- `-p-` 全端口（1-65535）——发现高端口/未知服务，单机约 16s
- `-T0`~`-T5` 时间模板——**-T4 实战最常用**；-T5 太快易被发现+漏报
- 组合：`nmap -sS -sV -T4 <IP>` = 半开+版本+提速

### 版本探测
- `-sV` 精确到软件名+版本号 → 查对应漏洞（ExploitDB/NVD）
- 识别操作系统 → 针对性渗透

## 关联

- [[src-recon-scanning]]（子域侦察——Nmap 是 IP/端口层）
- [[src-bug-hunting]]（拿到端口后挖漏洞）
- 安全技能：`security/nmap-scanning`

---
*k (Hermes) 2026-08-20 · SenseVoice 转写 + 蒸馏建技能*

---
tags: [src, 漏洞挖掘, 业务逻辑, 靶场, 3个月, 新手]
domain: Security
status: fresh
date: 2026-08-21
---

# SRC 3 个月路线 + 业务逻辑专项靶场（周小粥 · 抖音 2026-08-21）

> 来源：抖音 @网安-周小粥《从0开局如果用3个月拿下第一个漏洞？1700字讲透白帽src的核心知识点和赏金思路》（3:41，76K 赞，107K 粉）
> 转写 1448 字（SenseVoice 分块）

## 核心认知

- 挖洞门槛不高：15-35 岁 + 能开机的电脑 + 不是三分钟热度
- **70% 新手首笔赏金来自业务逻辑漏洞**（不需要代码功底）
- 别贪多：新手最大通病 = 浪费精力学全套操作系统/数据库

## 三个月节奏（视频原版）

### 第 1 月：学刚需技术
- 前 3 天：Web 地基——HTML 表单 + HTTP 协议 + 请求头/响应头 + GET/POST 差异
- 4 天：TOP 主流漏洞原理——**重点业务逻辑漏洞**（不需敲代码，新手最容易拿分）
- 剩余：工具实操——**Chrome 开发者工具 + 抓包改包**（两大神器）
- 地坑：操作系统只学文件路径/基本权限；数据库仅简单 SQL 查询——高深往后放

### 第 2 月：靶场实操
- 前 7 天：三大主力工具——爆破模块 + 扫描模块 + dirsearch 目录扫描（精通几个，贪多无效）
- 刷靶场顺序：DVWA + Pikachu 入门（3 天）→ 业务逻辑 + SQL 专项（1 周）
- 组合拳后 → **公益 SRC 找感觉**（适应真实厂商节奏）
- 敲黑板：**别执着通关所有靶场**——死死盯住越权 / 未授权访问 / 密码重置三类高频逻辑漏洞

### 第 3 月：冲 SRC 第一桶金
- 平台：**补天 + 漏洞盒子**（项目多、过审快，最适合练手）
- 上半月：公益 SRC 打磨手感 + 熟悉提交规范 + 养成复盘习惯（主攻低危逻辑）
- 下半月：**教育类 SRC**（容错率高、审核宽松 = 新手积累战绩的绝佳跳板）

## 赏金现实

- 低危 50-200 元 / 中危 200-1000 元 / 高危上千起步
- 熟练后每月稳定 3000-4000 元非常普遍
- 3 个月挖高危确实有难度——**稳扎稳打拿中低危才是王道**
- 未来：AI 依赖越高 → 逻辑漏洞 + AI 层漏洞只会越来越多

## 业务逻辑专项靶场（2026-08-21 建）

DVWA 没有业务逻辑模块 → 自建 Flask 靶场：

**位置**：`C:\Users\31954\AppData\Local\hermes\skills\security\web-security-lab-setup\scripts\bizlogic_lab.py`
**启动**：`python bizlogic_lab.py`（127.0.0.1:8090）
**演示**：`python bizlogic_lab.py --demo`

| 漏洞 | 漏洞版（200）| 修复版（403）|
|:---|:---|:---|
| 越权 IDOR | `/api/profile/<username>` 无身份校验 | `/api/profile-fixed/` 校验 session |
| 未授权 | `/api/admin/delete/<user>` 无角色校验 | `/api/admin/delete-fixed/` 校验 admin |
| 密码重置 | `/api/reset-password` 无旧密码 | `/api/reset-password-fixed` 旧密码校验 |

## sora 现状对照（2026-08-21 实测）

| 视频要求 | sora 状态 |
|:---|:---|
| 靶场实操 | ✅ DVWA 四类漏洞（SQLi/盲注/XSS/命令注入）实跑通（dvwa_practice.py）|
| 业务逻辑三类 | ✅ bizlogic_lab 三类漏洞全演示成功 |
| 公益 SRC → 教育 SRC | ⚠️ 未开始——T3 首单被忽略的教训：先练靶场再冲 |

## 端口冲突坑

SRC-Hunter 占 8080 → DVWA 换 8081：
```bash
php -S 127.0.0.1:8081 -t D:/phpstudy_pro/WWW/DVWA
DVWA_BASE=http://127.0.0.1:8081 python dvwa_practice.py
```

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]

# DVWA 靶场实战（2026-08-17 七漏洞全通关）

> 技能：`src-bug-hunting` → 「DVWA 靶场实战」章节 + `scripts/dvwa_practice.py`

## 环境
- D:\phpstudy_pro（MySQL 5.7.26 + PHP 7.3.4），启动：`start_dvwa.bat`
- 访问 http://127.0.0.1:8080/，admin/password，等级 low
- 一键脚本：`dvwa_practice.py`（6 模块全自动）

## 7 漏洞实战记录
| 漏洞 | 关键操作 | 结果 |
|:---|:---|:---|
| SQLi | `1'` 报错 → ORDER BY 3 报错(2列) → UNION 拖库 | 5 用户+hash 破解(password/abc123) |
| Blind | AND 1=1/1=2 → LENGTH/SUBSTRING | 库名 dvwa |
| Reflected XSS | `<script>` 反射 | 原样输出 |
| Stored XSS | guestbook POST 入库 | 恶意脚本持久化 |
| Command Inj | exec 页 POST `&& whoami` | 输出 31954 |
| CSRF | 无 token 改密 | 密码被改→恢复 |
| File Upload | shell.php 上传 | whoami 执行 |

## 坑与修复
1. MySQL/PHP 进程会话切换被杀 → netstat 查 3306/8080，重跑 bat
2. php.ini extension_dir/session.save_path 开发路径 → 已改实际路径
3. DVWA 初始化只建 users 表 → 手动建 guestbook
4. CSRF 改密后必须恢复（UPDATE users SET password=MD5('password')）
5. exec 模块是 POST 不是 GET

## 红线
DVWA 随便打；真实 SRC：只测授权/注入只证明/越权≤5条/XSS 只 console.log/上传证明即可。

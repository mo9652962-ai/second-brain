---
tags: [research, awesome-list, devops, security, cli, reference]
created: 2026-07-31
status: archived-reference
source: "https://github.com/trimstray/the-book-of-secret-knowledge"
---

# The Book of Secret Knowledge — 运维/安全/CLI 手册（备查）

> 2026-07-31 存档 · 高频参考手册，按需查阅

## 是什么

集合了 CLI 工具、cheatsheet、博客、hacks、one-liners 的精华手册，面向系统/网络管理员、DevOps、渗透测试、安全研究者。

- GitHub: [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge)
- **235K stars / 14K forks** — 超级流行
- MIT 协议

## 章节结构

| 章节 | 内容 |
|------|------|
| CLI Tools | Shells (bash/zsh/oh-my-zsh)、编辑器 (vim/neovim)、网络 (nmap/masscan/netcat) |
| GUI Tools | 桌面工具 |
| Web Tools | 在线工具 |
| Systems/Services | 系统服务 |
| Networks | 网络工具 (DNS/HTTP/防火墙) |
| Containers | Docker/K8s 编排 |
| Manuals/Howtos | 教程 |
| Inspiring Lists | 灵感清单 |
| Hacking/Pentest | 渗透测试 |
| Shell One-liners | 单行命令集（grep/perl/awk 实战） |

## 对我们最有价值的部分

### Shell 单行命令（日常自动化直接用）

```bash
# 搜索模式
grep -rn "pattern" .
grep -RnisI "pattern" *
fgrep "pattern" * -R

# 多模式搜索
grep -e INFO -e WARN filename
grep -E '(INFO|WARN)' filename

# 去注释/空行
grep -v ^[[:space:]]*# filename
egrep -v '#|^$' filename

# perl 就地替换（带备份）
perl -p -i.orig -e 's/\bfoo\b/bar/g' *.conf
```

### Shell 函数模板

```bash
# 域名解析
function DomainResolve() {
  local _host="$1"
  curl -ks -m 15 "https://dns.google.com/resolve?name=${_host}&type=A" | \
    jq '.Answer[0].data' | tr -d '"'
}

# 查询 ASN
function GetASN() {
  local _ip="$1"
  curl -s "http://ip-api.com/line/${_ip}?fields=as"
}
```

## 何时启用

- [x] 需要 CLI 工具选型（找 xx 类工具时查） (参考清单)
- [x] 写 shell 自动化脚本遇到疑难 (参考清单)
- [x] 安全/网络排查 (参考清单)

## 使用方式

不安装，作为**按需查阅手册**：需要找工具/命令时先 grep 这个仓库的 README。

---

*存档 2026-07-31 · 按需查阅手册，非立即执行*

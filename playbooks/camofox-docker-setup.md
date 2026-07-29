---
date: 2026-07-29
tags: [browser, anti-detection, camofox, docker]
status: ready
trigger: 遇到 Cloudflare 5秒盾 / 验证码 / 反Bot拦截
---

# Camofox Docker 反检测 — 启动预案

> 状态：🟢 就绪（配置文档已备，遇到反Bot时按此执行）
>
> 无需预装，触发时一次性配置

---

## 触发判断

| 症状 | 是否触发 Camofox |
|-----|:-----------------:|
| `browser_navigate` 返回空白页 | ❌ 先检查 CDP 连接 |
| Cloudflare "Checking your browser" | ✅ **立即启用** |
| 验证码/滑块验证 | ✅ **立即启用** |
| 403 Forbidden / "检测到自动化工具" | ✅ **立即启用** |
| 正常加载但元素缺失 | ❌ 先试 browser_vision |

---

## 一键启动

```bash
# 1. 克隆（首次）
git clone https://github.com/jo-inc/camofox-browser
cd camofox-browser

# 2. 启动 Docker
make up
# 访问 VNC 监控: http://localhost:6080

# 3. Hermes config 添加（config.yaml）
# browser:
#   camofox:
#     enabled: true
#     url: http://localhost:9377
#     managed_persistence: true
```

## 验证

```bash
# 确认 Camofox 运行
curl http://localhost:9377/health

# 在 Hermes 中测试
# > 用浏览器打开 https://www.cloudflare.com 并截图
```

---

## 注意事项

- Docker 需先安装（Windows: Docker Desktop）
- 首次启动需拉取镜像（~500MB）
- VNC 端口 6080 可在浏览器中实时查看浏览器操作
- 持久化会话：登录一次后 Cookie 保留，下次直接用

---

*预案创建：2026-07-29 | 下次更新：首次启用后记录耗时*

---
title: "SOP-003: dsh 升级（npm 12 ETARGET 绕道方案）"
type: sop
domain: SOP
status: active
tags: [knowledge/sop]
source: null
---
# SOP-003: dsh 升级（npm 12 ETARGET 绕道方案）

- **ID**: SOP-003
- **Category**: OPS（运维）
- **状态**: Active
- **维护者**: k

## 1. 前置条件与触发上下文

- **触发**: dsh（DeepSeek Harness）需要升级（npm 有新版 rc 时）
- **前置**: npm 全局安装于 `C:\Users\31954\AppData\Local\hermes\node`；FlClash 代理可用
- **当前版本**: 0.1.0-rc.7（2026-08-19 升级）

## 2. 确定性执行步骤

```
① 查最新版本:
   curl -x http://127.0.0.1:7890 https://registry.npmjs.org/@deepseek-ai/dsh/latest
   → version 字段
② 先试常规升级: npm install -g @deepseek-ai/dsh@<ver>
   报 ETARGET（date before 时间 bug）→ 走绕道方案
③ 绕道方案（npm 12 有 bug 时）:
   a. 下载主包 tarball:
      curl -x http://127.0.0.1:7890 -L ".../dsh-<ver>.tgz"   ← 必须 -L 跟随重定向
      tar -xzf → 备份旧 dsh → 替换 node_modules/@deepseek-ai/dsh
   b. 递归补齐依赖（脚本从 npmmirror 批量下载）:
      - 读 dsh package.json 的 dependencies
      - 对每个 @deepseek-ai/* 和第三方包: 下载 tarball 解压到 node_modules
      - semver 解析必须含 rc 后缀数字（rc.7 > rc.2）
      - 循环直到无缺失（子包还有依赖）
   c. @types/* 特殊处理: python urllib 下载 + tar 解压到 node_modules/@types/
④ 验证:
   dsh --version → 目标版本
   dsh --profile web --dump-config → 插件树完整（auto-mode/mnemon/orchestrator/billing）
   dsh --profile headless --dump-config → 正常
⑤ 保留旧版备份（dsh-rc6-backup）几天，确认稳定后删
```

## 3. 验证与验收边界

```
✅ dsh --version 显示目标版本
✅ web/headless profile 均正常加载（无 ERR_MODULE_NOT_FOUND）
✅ 插件（auto-mode/mnemon/orchestrator/billing）在 dump-config 中可见
```

## 4. 异常恢复与常见陷阱

```
⚠️ ETARGET "date before 2026/x/x" = npm 12 pacote 时间过滤 bug（registry 数据正常也触发）
   → 不要反复重试 npm install，直接走 tarball 绕道
⚠️ EALLOWREMOTE = npm 12 禁远程 tarball → 手动 curl 下载
⚠️ ERR_MODULE_NOT_FOUND = 缺依赖 → 递归补齐（子包也有依赖）
⚠️ semver 前缀匹配 bug: 只取前 3 段数字会装成 rc.2（须含 rc 后缀）
⚠️ npmmirror tarball 302 到 CDN → curl 必须 -L，或 python urllib（自动跟随）
⚠️ 升级后 node_modules 残留旧版组件 → 按依赖树核对版本
```

## 5. 演进记录

| 日期 | 变更 | 原因 |
|:---|:---|:---|
| 2026-08-19 | 新建 | dsh rc.6→rc.7 升级完整踩坑记录（npm 12 ETARGET）|

---
> 🗺️ 属于 [[SOP-INDEX]] · [[knowledge-map]] · [[Home|🏠 Home]]

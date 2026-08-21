---
tags: [后端, 异常处理, 空catch, 静默失败, 日志, 反模式]
domain: Development
status: fresh
date: 2026-08-21
---

# 空 catch 吞异常（程序员Orion · 抖音 2026-08-21）

> 来源：抖音 @程序员Orion（创业中）《页面没报错就算成功？你写的一个空 catch，让公...》（1:24）
> 转写 497 字（SenseVoice）
> 与 `python-silent-failure-debugging` 技能同源（墨题 UI 黑屏静默异常）

## 坏习惯

```
try {
  coreLogic();
} catch (Exception e) {
  // 大括号里空空如也 — 什么都不处理
}
```

页面不报错了，但问题被强行藏起来。用户点提交毫无反应；开发查日志一片空白。

## 保命打法（错误要被正确处理，不是消灭）

| 异常类型 | 处理 |
|:---|:---|
| 能恢复的 | 用户明确弹窗「请稍后重试」|
| 不能恢复的致命 | 记录 + 打进日志系统（含堆栈）|
| 关键业务流程 | 向外返回明确的失败状态 |

> 金句：假装看不见异常不是优雅，而是把 bug 强行塞进了地毯下面。

## 落地检查

```
□ 全局搜空 catch / except: pass（Python）— 至少记日志
□ 前端请求失败有用户提示（toast/弹窗）
□ 后端有统一异常处理（@ControllerAdvice / 中间件）+ 日志落盘
□ 日志含: 时间/接口/错误码/堆栈/入参(脱敏)
```

## 关联

- `python-silent-failure-debugging` 技能（UI 黑屏静默异常排查）
- `Development/写码前扫坑清单.md`（第 15 项）

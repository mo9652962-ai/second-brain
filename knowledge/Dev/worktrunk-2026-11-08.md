---
tags: [github, W45, dev, git, worktree, 并行agent, codex]
aliases: [Worktrunk, wt]
date: 2026-11-08
source: https://github.com/max-sixty/worktrunk
status: watching
---

# Worktrunk — 把 git worktree 做成「并行 agent 的工位管理」

> W45 精选。**11,982★ / 89 contributors / 5,511 commits / v0.81.0（2026-10-20）/ MIT OR Apache-2.0 / Rust**，2026 年初发布，作者称已是「最流行的 git worktree 管理器」。本周 trending +2,292★。
> 真实性：**高**（5,500+ commits、89 贡献者、11 个月持续发布、有 CI/Codecov/crates.io）。

## 一句话定位

Claude Code / Codex 这类 agent 能长时间无人值守跑，所以「同时开 5-10 个」变得可行——但原生 `git worktree` 的 UX 很烂（起一个新 worktree 要把分支名打三遍）。Worktrunk 让 **worktree 像分支一样好用**：按分支名寻址、路径由模板算出来。

## 三条核心命令

| 任务 | Worktrunk | 原生 git |
|:--|:--|:--|
| 切换 worktree | `wt switch feat` | `cd ../repo.feat` |
| 建 + 直接起 Claude | `wt switch -c -x claude feat` | `git worktree add -b feat ../repo.feat && cd ../repo.feat && claude` |
| 清理 | `wt remove` | `cd ../repo && git worktree remove ../repo.feat && git branch -d feat` |
| 带状态列清单 | `wt list` | `git worktree list`（只有路径） |

## 进阶能力（对多 agent 工作流真正有用的部分）

- **Hooks**：create / pre-merge / post-merge 等生命周期挂命令——比如「建好 worktree 自动装依赖」「合并前跑门禁」
- **LLM commit message**：从 diff 生成提交信息
- **copy-on-write 构建缓存**：多个 worktree 共享编译产物，不用每个都冷启（对 Rust/Node 大项目是决定性优化）
- 分支与路径解耦：路径由可配置模板生成；接受分支名的地方也接受路径

## 为什么这周值得写

这周三个项目（dsh-superagent、agent-autoloop、worktrunk）指向同一件事：**agent 的并行度已经是工程问题，不是模型问题**。

- dsh 用 **Router/Worker 两层**解决「并行但不混乱」
- agent-autoloop 用**事件内核**解决「并行但不互相踩」
- worktrunk 用 **worktree** 解决「并行但不共享工作区」

三者拼起来正好是「一个 agent 团队」的三块基础设施：调度、状态、工作区隔离。

## 💎 可借鉴点

| 借鉴 | 映射到 sora 的现状 | 落地动作 |
|:--|:--|:--|
| 一任务一 worktree | 现在 Codex 委派多个任务时共用 D:\english-multiple-choice-practice-machine 一个工作区，容易互相污染 | 多任务并行时用 `git worktree add` 开独立目录；不必装 worktrunk，原生命令够用 |
| 生命周期 hooks | 墨题已有「完成即 push + 跑门禁」约定 | 固化成脚本：worktree 创建即装依赖，合并前自动跑 `npm build` + `pytest` |
| 合并前门禁 | 记忆里已有「merge 后跑门禁（grep 冲突 + npm build/pytest）」 | 升级为**合并前**跑，别等合完才发现 |
| 带状态的清单 | `wt list` 一屏看清每个工位在干什么 | 委派 3 个以上任务时，先列一张「任务→目录→分支→状态」表再开工 |
| copy-on-write 缓存 | 本机 16GB 内存 + RTX4060，多份 node_modules 会拖死 | 并行 worktree 时复用同一个 node_modules（软链或 pnpm store），别复制 |

## 评价

| 维度 | 判断 |
|:--|:--|
| 技术含金量 | ★★★★☆（把 git 的边角功能做成主流程，UX 价值 > 算法价值） |
| 可复用性 | ★★★★☆（Rust 单二进制，`cargo install worktrunk` 或 release 下载；不装也能用原生 git 达到 80% 效果） |
| 风险 | NOASSERTION license（README 写 MIT OR Apache-2.0，GitHub 识别不出来）——商用前需自行确认 |
| 建议 | **先不装**。并行任务变多（≥3 个同时）时再装；现阶段用 `git worktree` 原生命令 + 手写 hooks 就够 |

---
*W45 · 2026-11-08 · 观察：star/commits/contributors/releases/README 实读；推断：与另两个项目构成并行三件套；未知：未实机安装*

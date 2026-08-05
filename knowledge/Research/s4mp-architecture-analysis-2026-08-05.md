---
aliases:
  - s4mp-analysis
tags:
  - simsync
  - research
  - s4mp
  - benchmark
created: 2026-08-05
updated: 2026-08-05
status: studied
domain: simsync
---

# S4MP 架构分析（v0.74.1）— 可借鉴点

> 2026-08-05 · 反编译 S4MP mod（855KB ts4script）+ 分析启动器 exe（143MB）
> 结论：**S4MP 深度复用 EA 引擎内置模块，装饰器模式 + 原生 protobuf 是核心差异**

---

## 一、源码结构（18 模块）

| 模块 | 文件数 | 职责 |
|:-----|:------|:-----|
| `base/` | 2 | 基础管理（`manager_base`） |
| `chat/` | 1 | 聊天系统 |
| `client/` | 3 | 客户端配置、覆盖 EA `server.client.Client` |
| `command/` | 3 | 命令覆盖（游戏内作弊命令） |
| `config.py` | 1 | 全局配置（版本 v0.74.1、调试开关） |
| `debug/` | 5 | 日志、调试命令、调试覆盖 |
| `decorator/` | 7 | **核心架构**：`@networked`、`@message_handler`、`@timed_task`、`@override` 等 |
| `distributor/` | 2 | 消息分发（复用 EA `distributor` 系统） |
| `hook/` | 2 | **EventHook 挂 tick**（`core_services.on_tick`） |
| `inspector/` | 2 | 调试检查器（JSON 协议） |
| `interaction/` | 1 | 交互同步 |
| `launcher/` | 0 | 在 exe 里（不在 mod 中） |
| `lib/` | 0 | 库 |
| `network/` | 0 | 在 exe 里（不在 mod 中） |
| `protobuf/` | 0 | **复用 EA 引擎自带**（`protocolbuffers` 模块），不是自己写 |
| `scheduling/` | 0 | 调度 |
| `support/` | 0 | 支持 |
| `ui/` | 0 | 游戏内 UI |
| `util/` | 0 | 工具 |

**关键发现**：网络层 + 启动器逻辑在 exe 里（136MB），不在 mod 的 ts4script 中。mod 只负责游戏内集成。

---

## 二、核心架构差异（S4MP vs SimSync）

| 维度 | S4MP v0.74.1 | SimSync v9.18 |
|:-----|:------------|:------------|
| 序列化 | **EA 原生 protobuf**（`protocolbuffers` 模块） | pickle（自实现） |
| 网络化标记 | **装饰器 `@networked`** | 手动 `collect_*` / `process_message` |
| 消息分发 | **复用 EA `distributor` 系统** | 自实现消息路由 |
| 客户端 | 覆盖 `server.client.Client` | 自实现 TCP 客户端 |
| 事件循环 | **EventHook 挂 `core_services.on_tick`** | 自建事件循环 |
| 本地过滤 | **LOCAL_ONLY_OPS 列表**（明确不同步的操作） | 无 |
| 热重载 | `sims4.reload` API | 无（需重启游戏） |
| 调试协议 | Inspector（JSON） | 无 |
| 配置 | JSON 文件（`s4mpconfig`） | 硬编码 |
| 模块规模 | 18 模块 | 12 模块 |
| mod 大小 | 855KB | 69KB |

---

## 三、可借鉴点（按价值排序）

### 🥇 1. EA 原生 protobuf 复用（最大发现）

S4MP **不自己写 proto 定义**，而是直接 import Sims4 引擎自带的：

```python
from protocolbuffers import Distributor_pb2, DistributorOps_pb2, Consts_pb2
```

游戏引擎里已经有完整的 protobuf 消息类型（`Distributor_pb2`、`Consts_pb2`、`DistributorOps_pb2` 等），S4MP 直接复用。这意味着：
- 不需要自己定义 proto 文件
- 不需要自己写序列化/反序列化
- 消息类型与 EA 引擎一致，兼容性更好

**⚠️ 注意**：SimSync 当前用 pickle——如果切换 protobuf，不是"自己写 proto"，而是"复用 EA 引擎已有的"。这比之前讨论的"Protobuf vs pickle 自己写"更高效。

### 🥈 2. 装饰器模式

S4MP 用装饰器标记网络化行为，而不是手动调用：

```python
# S4MP 方式：
@networked           # 这个函数的结果要同步到所有客户端
def set_sim_position(sim, x, y, z):
    ...

@message_handler     # 这个函数处理特定类型的网络消息
def handle_position_update(msg):
    ...

@timed_task(interval=1.0)  # 这个函数每 1 秒执行一次
def heartbeat():
    ...
```

**对比 SimSync**：每个模块都需要手动实现 `collect_*()` 和 `process_message()`，代码分散且容易遗漏。

### 🥉 3. LOCAL_ONLY_OPS 过滤

```python
LOCAL_ONLY_OPS = [
    Operation.FOCUS,                   # 焦点
    Operation.HOVERTIP_CREATED,        # 悬停提示
    Operation.SET_SIM_ACTIVE,          # 设置活动小人
    Operation.SET_VFX_MASK,            # 视觉特效
    Operation.CLIENT_CREATE,           # 客户端创建
    Operation.CLIENT_DELETE,           # 客户端删除
    ...
]
```

明确列出哪些 EA 操作**只在本地执行、不同步**——避免浪费带宽。SimSync 目前没有这个区分，所有操作都尝试同步。

### 4. EventHook 挂 tick

```python
class CoreServicesHooks:
    on_tick = EventHook()
    
    @classmethod
    def setup_hooks(cls):
        cls.__original_on_tick = core_services.on_tick
        core_services.on_tick = cls._on_tick_wrapper(core_services.on_tick)
```

S4MP 通过 `EventHook` 把自定义逻辑注入到游戏主循环，而不是自建事件循环。这意味着：
- 与游戏引擎时钟同步（不需要自己做时钟同步）
- 不需要额外的线程/进程

### 5. 热重载（`reload_service.py`）

```python
import sims4.reload as r
# mod 更新后自动重载，不需要重启游戏
```

直接用 EA 的 `sims4.reload` API。调试时改动 mod 不用重启游戏——**这个对开发效率影响巨大**。

### 6. Inspector 协议（JSON 调试）

```python
class InspectorProtocol(NetworkProtocolBase):
    def _deserialize_message(self, msg):
        return json.loads(msg)  # 用 JSON，不用 protobuf
```

生产消息用 protobuf（高效），调试消息用 JSON（可读）。两者分离。

### 7. 配置用 JSON 文件

```json
{"is_server":true, "player_name":"Emeraldglazer Gazelle", "player_count":2,
 "server_id":0, "player_id":0, "room_code":"local/host/192.168.0.112;fe80::..."}
```

mod 启动时读取，比命令行参数或硬编码方便。

---

## 四、不适用/不建议借鉴的

1. **代码混淆**（`obfuscated\sims4multiplayer\...`）——闭源策略，不开源项目不适合
2. **exe 体积 136MB**——网络层在 exe 里，mod 和启动器分离（SimSync 可以保持一体）
3. **launcher 逻辑在 exe 里**——无法反编译看启动器设计（UPX 压缩/加密）

---

## 五、对 SimSync 的启发

| 优先级 | 借鉴项 | 落地难度 | 收益 |
|:------:|:------|:------:|:-----|
| 🔴 | EA 原生 protobuf 复用（替代 pickle） | 中（需研究 `protocolbuffers` 模块 API） | **高**（类型安全 + 引擎兼容） |
| 🔴 | 装饰器模式（`@networked`/`@message_handler`） | 中（需重构 12 模块） | **高**（代码简洁 + 不易遗漏） |
| 🟡 | LOCAL_ONLY_OPS 过滤 | 低（加一个列表） | 中（减少带宽浪费） |
| 🟡 | 热重载（`sims4.reload`） | 低（一个 import） | 中（开发效率） |
| 🟡 | EventHook 挂 tick | 高（需改事件循环） | 中（引擎时钟同步） |
| 🟢 | Inspector 协议 | 低（加 JSON 通道） | 低（调试便利） |
| 🟢 | JSON 配置文件 | 低（替换硬编码） | 低（便利性） |

---

*研究完成：2026-08-05 · 状态: studied（暂不落实，等待双机验证后决策）*
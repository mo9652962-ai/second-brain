---
aliases:
  - s4mp-multiplayer-10round-2026-08-04
tags:
  - research
  - s4mp
  - sims4
  - multiplayer
  - ten-round
created: 2026-08-04
updated: 2026-08-04
status: adopted
---

# 🎮 S4MP 联机方式十轮研究 + 自制 mod 对齐方案

> 十轮搜索引擎研究 + S4MP 反编译源码交叉验证（2026-08-04）
> 目标：自制联机 mod 先与 S4MP 一致（同存档+同家庭+各控不同 sim），再解决场景切换 bug

---

## 一、S4MP 联机架构（十轮研究结论）

### 1. 核心模型：host 权威 + 同家庭多人控制

| 维度 | S4MP 做法 | 来源 |
|:-----|:----------|:-----|
| 玩家模型 | **同一存档 + 同一家庭（household）+ 各控不同 sim** | sims-multiplayer.com 官方："live together with other players in the same household" |
| 家庭限制 | "Each player has the ability to control sims within the same household. **Separate households are not possible**" | SimSync FAQ + Reddit |
| 房间模型 | host 开服务器（S4MP Launcher），client 用房间码/IP 加入 | CurseForge 安装指南 |
| 权威性 | **只有 host 能改时间**（client 改无效）；host 暂停 → 全员暂停 | 0.3.2 教程实测 |
| 连接方式 | 同网络直连（LAN）；异地需 VPN（Hamachi/Radmin）| 官方 FAQ |
| 玩家上限 | 最多 12 人（家庭上限 8 sims）| 官方 |
| 存档同步 | **共享 save 文件**（host 准备，分发到各客户端 Saves 目录）| thesimstree 指南 |

### 2. 场景切换（旅行）机制——本轮研究重点

**S4MP 的旅行设计（官方文档 + 教程）：**
- **必须全员一起旅行**：`When sims leave the home lot, both the client and the host will travel together`（SimSync FAQ 原话）
- **旅行后暂停时间**：`Time is paused after traveling until all clients have loaded`（S4MP 0.10.0 changelog）——这是防 desync 的核心机制
- **2026.7.0 Travel Rework（Patreon 付费版）**："major rework to multiplayer travel, resolving travel-related issues, including the occasional black screen bug affecting client players"——官方自己也承认免费版旅行有 bug

**反编译源码确认的旅行实现（travel_overrides.pyc）：**
```python
@NetworkedCommand(travel_commands.travel_sims_to_zone, ["travel.travel_sims_to_zone"],
                  override_server=True, send_message_optionally=True)
def __travel_sims_to_zone(wrapper, opt_sim_id, zone_id, *traveling_sim_ids, _connection=None):
    NotificationManager.show_travel_notification()
```
- S4MP **hook 了游戏的旅行命令**（`travel.travel_sims_to_zone`），用 `NetworkedCommand` 装饰器把命令变成网络广播
- 每个客户端独立执行游戏原生的旅行流程，通过网络同步"谁在旅行、去哪个 zone"

**场景加载同步（zone_spin_up_client.pyc）：**
```python
@Override(SimSpawnerService.batch_spawn_during_zone_spin_up, Override.Type.CLIENT)
def __batch_spawn_during_zone_spin_up_client(_, self):
    # 客户端版：跳过部分生成逻辑，等服务器同步
```

### 3. 玩家 ID 管理（KeyError:2 bug 根源）——反编译确认

```python
active_sims: Dict[int, int] = {}  # player_id -> sim_id

@MessageHandler(SetActiveSimMessage, Networked.Type.SERVER)
def __on_set_active_sim_message_server(message):
    if active_sims[message.player_id] == message.sim_id:  # ← KeyError 源头！
        return
    active_sims[message.player_id] = message.sim_id
```

**根因**：`active_sims` 用 `player_id` 做字典 key。客机**断开重连后 player_id 递增**（1→2），但主机侧字典没有 key 2 → `KeyError: 2`。这是 2026-08-03 实测的 404 次 KeyError 的确切代码位置。

**修复方向**：player_id 分配后不复用不递增（稳定 ID），或改用 `defaultdict` / `dict.get()` 容错。

### 4. 消息协议（网络层）

| 层 | S4MP 做法 | 我们的做法 |
|:---|:----------|:-----------|
| 序列化 | **Protobuf**（WrapperMessage_pb2，多种 Message 类型）| JSON（已有，简单够用）|
| 消息路由 | client_id 匹配 + 队列 + 主线程 on_tick 处理 | alarm 轮询队列（已有，v4.8 修好）|
| 消息类型 | Travel / SetActiveSim / LiveDrag / Buy... 几十种 | 目前 chat + sim_pos，按需扩展 |
| 同步对象 | 位置（live_drag）+ 状态（mood/career/buy...84 类互动）| 位置（M2 已有）|

### 5. 存档管理

- **共享 save 文件**：host 创建 save（所有玩家的 sim 在同一家庭），复制到各客户端 `Saves/` 目录
- **保存规则**：`Save As...` 覆盖当前 save（不要普通 Save，会丢数据）——SimSync FAQ 实测
- **mod/CC 同步**：所有玩家必须相同 mod 集（或纯净版）

---

## 二、对齐方案：自制 mod v5.x 设计

### 目标（用户明确）
1. **先对齐 S4MP**：同存档 + 同家庭 + 各控制不同 sim
2. **再做场景切换**：不出 bug、顺利切换（S4MP 免费版做不到的）

### 架构设计

```
同存档（共享 save，两台 Saves/ 目录同一文件）
  ↓
A 控制 sim_A（家庭内）    B 控制 sim_B（家庭内）
  ↓                        ↓
A 广播 (sim_id=sim_A, pos) ──TCP──▶ B 收到 → 在 B 的世界里移动 sim_A
B 广播 (sim_id=sim_B, pos) ──TCP──▶ A 收到 → 在 A 的世界里移动 sim_B
```

### 关键改动点

| 模块 | 改动 | 对齐 S4MP 的哪部分 |
|:-----|:-----|:-------------------|
| sync.py | sim_pos 消息加 `sim_id`；接收按 sim_id 查找 sim（不是移动自己的 active_sim）| sim_select.py 的 active_sims 映射 |
| network.py | 加 `set_active_sim` 消息类型（玩家切换控制时广播）| SetActiveSimMessage |
| 新模块 zone.py | **场景切换同步**（见下）| travel_overrides.py |

### 场景切换设计（我们的差异化优势）

**S4MP 的教训**：
1. 旅行后不暂停时间 → desync（0.10.0 才修）
2. player_id 递增 → KeyError（免费版至今有）
3. 客户端黑屏（2026.7.0 才修）

**我们的方案**（针对每个 bug）：

| S4MP bug | 我们的对策 |
|:---------|:-----------|
| 旅行 desync | **旅行命令广播 + 双方确认**：发起旅行方广播 `travel_req` → 双方都执行旅行 → 双方加载完成发 `travel_ready` → host 收到全部 ready 才恢复时间 |
| KeyError: 2 | **player_id 固定分配**：连接时 host 分配（1、2...），断开不清除映射，重连用原 ID；字典用 `.get()` 容错 |
| 黑屏 | 不 hook 游戏的旅行 UI；用**命令式旅行**（`travel.travel_sims_to_zone` 直接调用），双方各自加载，进度日志化 |

**实现步骤**（M3 路线）：
1. **M3a**：sim_id 字段 + 同家庭多 sim 位置同步（先跑通"各控不同 sim"）
2. **M3b**：player_id 分配协议（连接握手时 host 分配固定 ID）
3. **M3c**：旅行同步（travel_req / travel_ready 两阶段确认 + 时间恢复）
4. **M3d**：实测（同存档 + 同家庭 + 两小人 + 旅行切换）

---

## 三、90 天行动路线

| 阶段 | 内容 | 预估 |
|:-----|:-----|:-----|
| 立即 | M3a：sim_id + 多 sim 位置同步（v5.2）| 1-2 天 |
| 本周 | M3b：player_id 握手协议（v5.3）| 1 天 |
| 下周 | M3c：旅行两阶段确认（v5.4）| 2-3 天 |
| 两周 | M3d：双端实测 + bug 修复 | 3-5 天 |
| 之后 | 状态同步（mood/动画）、平滑移动 | 按需 |

---

## 四、关键资源

| 资源 | 链接/位置 |
|:-----|:----------|
| S4MP 官网 | sims-multiplayer.com |
| S4MP 反编译源码 | D:\Sims4-Multiplayer-Dev\python\ + /d/tmp_s4mp/ |
| CurseForge 指南 | curseforge.com/sims4/mods/sims-4-multiplayer-mod |
| SimSync FAQ（已停更但有参考）| simsync.io/faq |
| 玩家教程 | thesimstree.com/en/blog/the-sims-tips/how-to-play-the-sims-4-with-friends-complete-multiplayer-guide.html |

---

## 变更记录
- 2026-08-04: 初版（十轮研究 + 反编译交叉验证 + M3 路线）

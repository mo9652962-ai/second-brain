---
aliases:
  - s4mp-protocol-network-100round-2026-08-05
tags:
  - research
  - s4mp
  - sims4
  - multiplayer
  - protocol
  - network
created: 2026-08-05
updated: 2026-08-05
status: adopted
---

# 🔌 S4MP 消息协议（网络层）百轮研究 + 自制 mod 改进

> 知识库消息协议笔记 + 4 批搜索引擎研究（借鉴 S4MP/业界标准）+ 百次虚拟测试（v9.12）
> 目标：对照 S4MP 网络层，找出自制 mod 协议差距并改进

---

## 一、现状盘点（自制 mod v9.11 协议）

- **序列化**：pickle 二进制帧（8 字节大端长度前缀 + pickle）——比 JSON 快 2.8x、体积 84%
- **消息类型**：29 种（hello/welcome/lobby/ready/in_lot/heartbeat/chat/clock/mood/money_sync/stats_sync/sim_pos/save_*/travel_*）
- **可靠性**：TCP 保证有序可靠；seq 序号（位置丢包检测）；心跳 5s + 超时 15s
- **容错**：断线重连（指数退避 + jitter）、主机迁移、8MB 帧上限、线程锁

## 二、百轮研究结论（4 批搜索）

### 第 1 批：协议架构与帧格式
| 研究 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| Protobuf vs Flatbuffers vs JSON | 二进制比文本小 3 倍；Protobuf 序列化快 | pickle 已满足局域网需求 ✅ |
| Length-prefix framing（Eli Bendersky）| 长度前缀帧是标准做法 | 我们的 8 字节前缀 ✅ |
| **协议版本协商**（MCP handshake / QUIC RFC 9368）| **握手时交换版本，不兼容拒绝** | **❌ 缺失 → 已实现** |

### 第 2 批：心跳/可靠性/安全
| 研究 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| WebSocket heartbeat（WebSocket.org）| 应用层心跳是唯一可靠检测僵尸连接的方法 | 心跳 5s/15s ✅ |
| Reliable Ordered（Gaffer）| TCP 本身处理可靠有序，无需应用层重传 | seq 仅用于丢包检测 ✅ |
| HMAC（RFC 2104/FIPS 198-1）| 包签名防篡改；局域网信任对端可省略 | 低优先（局域网）|

### 第 3 批：S4MP 具体实现
| 研究 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| S4MP 官方 | 最新 0.74.1；host 权威 + 同家庭多控 | 我们对齐 ✅ |
| SmartFoxServer 房间 | public/private（密码）+ 6 位房间码 | 我们已实现 ✅ |
| **位置量化**（Gaffer 4096 values/meter）| 位置量化到整数大幅省带宽 | **❌ 缺失 → 已实现（0.01m）** |

### 第 4 批：编码/连接管理
| 研究 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| varint（Protobuf encoding）| 小整数 1 字节 vs 固定 8 字节 | 低价值（局域网）|
| 连接池/复用（OneUptime）| 服务器管理多连接 | host 多 client ✅ |
| **player_id 管理**（知识库 S4MP 笔记）| 重连 ID 递增 → KeyError:2 | **❌ 递增 → 已实现复用池** |

## 三、改进实施（v9.12）

### 1. 协议版本协商（MCP/QUIC 模式）
```python
PROTO_VERSION = 2  # 1=JSON时代, 2=pickle帧(当前)
# hello 带 proto_version → host 校验 → 不匹配发 version_mismatch + 拒绝
# 客户端收到 version_mismatch → 提示"协议版本不兼容，请更新"
```
- 防旧 mod 连新 host 导致消息字段错乱
- welcome 也带 proto_version（客户端可校验）

### 2. player_id 复用池（防 KeyError:2）
```python
_released_pids = []  # 断开时回收，重连复用原 ID
# 连接分配：优先 _released_pids.pop(0)，否则 _next_player_id
```
- 断开 → `_clients.pop` + 加入复用池
- 重连 → 复用原 player_id（不递增）→ 不会 KeyError

### 3. 位置量化（Gaffer 4096 values/meter）
```python
def _quantize(v): return int(round(float(v) * 100))  # 0.01m 精度
# 发送：delta_q = [量化后的整数 delta]
# 接收：pos = base + delta_q[i] / 100.0
```
- 传输整数（pickle 体积更小），接收端 /100 还原
- 0.01m 精度远小于人物可见位移
- 兼容旧协议（delta 未量化仍可处理）

## 四、百次虚拟测试（v9.12，19 断言全过）

| 测试 | 内容 | 结果 |
|:-----|:-----|:-----|
| A. 版本协商 | 匹配加入 / 旧版本拒绝 / 无版本拒绝 / 客户端提示 | ✅ |
| B. player_id 复用 | 断开进池 / 重连复用 / 20 次循环不递增 | ✅ |
| C. 位置量化 | 0.01m 精度 / banker's rounding / 还原累加 / 20 步误差 <0.5m | ✅ |
| D. 兼容性 | 旧 delta / position 绝对值 / welcome 带版本 | ✅ |

## 五、回归体系（11 套件 / 165 断言）

```
v92 端到端(12) + v93 传输层(10) + v94 协议语义(15) + v95 生命周期(11)
+ v96 纯逻辑(10) + v97 内存GUI(8) + v98 新领域(17) + v99 同步行为(19)
+ v910 容错(19) + v911 旅行(26) + v912 协议增强(19) = 一键全跑全过
```

---

## 变更记录
- 2026-08-05: 初版（百轮研究 + 3 项协议改进 + v9.12 测试）

## 六、第二轮改进（v9.13——批处理 + 协议目录）

### 研究（第 5-6 批）
| 主题 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| 消息批处理（Vanilla Java/Unity）| TCP 小消息合并到阈值（4KB）大幅提吞吐 | **❌ 无批处理 → 已实现 `_send_batch`** |
| 帧损坏恢复（工业标准）| 坏帧边界检测是关键；TCP 校验已覆盖局域网 | 低价值跳过 |
| Schema Registry（Kafka）| 集中管理消息 schema + 兼容规则 | **❌ 无文档 → 已写 docs/PROTOCOL.md** |
| 自适应拥塞（TCP BBR）| RTT 调整速率；已有自适应 tick | 低优先 |

### 改进
1. **`_send_batch(sock, payloads)`**：多条小消息合并成一个 `{"type":"batch","msgs":[...]}` 帧
   - 单条→直发，空→跳过，多条→batch 帧
   - 接收端 `_process_incoming` 拆包逐个处理
2. **`docs/PROTOCOL.md` 协议消息目录**：30 种消息类型全表（方向/字段/用途）+ 帧格式 + 版本兼容规则

### 测试（v9.13，14 断言全过）
- A. _send_batch 逻辑（空/单条/多条/20 次合并正确）
- B. batch 拆包（拆开处理/chat 分发/空不崩/非 dict 跳过）
- C. **真实 TCP 批处理闭环**（client batch → host 拆包 → add_chat）
- D. 协议目录完整性（30 种消息全覆盖检查）

### 回归体系升级（12 套件 / 179 断言）
```
v92(12)+v93(10)+v94(15)+v95(11)+v96(10)+v97(8)
+v98(17)+v99(19)+v910(19)+v911(26)+v912(19)+v913(14) = 一键全跑全过
```

## 七、第三轮改进（v9.14——连接健康监控）

### 研究（第 7-8 批）
| 主题 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| 游戏 QoS（pvigier）| 消息可分级（可靠/不可靠）+ 多流分离 | 位置低优/聊天高优思路 |
| RTT 测量（游戏 ping）| 应用层 ping/pong 带时间戳测 RTT | **❌ 无 RTT → 已实现** |
| 自适应频率（DACC/RFC 6298）| 高延迟降频防拥塞 | **❌ 无自适应 → 已实现** |
| 健康评分（Cloudflare/PingPlotter）| latency/jitter/loss → 质量分 | **❌ 无评分 → 已实现** |

### 改进
1. **应用层 ping/pong RTT 测量**（network.py）
   - `ping` 带 ts → 对端回 `pong`（带原 ts）→ RTT = now - ts
   - 主动 ping 每 3s（alarm 循环 `_send_ping`）
   - 滚动窗口 20 样本，异常值（>5s）过滤
2. **连接健康评分**（Cloudflare 模型）
   - `get_health_score()`：100 - RTT 扣分（50ms 内不扣，每超 5ms 扣 1，上限 60）
   - `get_health_label()`：🟢优秀/🟡良好/🟠一般/🔴差
3. **自适应位置广播频率**（sync.py）
   - RTT > 200ms → 间隔 1.5x；RTT > 400ms → 2x（网络差降频防拥塞）

### 测试（v9.14，19 断言全过）
- A. ping/pong RTT（回 pong/计算/异常过滤/无 ts 不崩）
- B. 健康评分（无样本/优秀/差/20 次范围）
- C. 滚动平均（20 窗口/平均正确/新样本挤旧）
- D. 自适应频率（无 RTT 默认/200-400 1.5x/>400 2x/低 RTT 默认）
- E. **真实 TCP ping/pong 闭环**（host 发 ping → client 回 pong → host 算 RTT）

### 修复（百次测试挖出）
1. **ping 处理引用未定义 `sock` 变量**（NameError 被吞→不回 pong）——改为 sender_pid 查 _clients
2. v911 `_fake_timer` 立即执行改变旅行时序——改 no-op
3. PROTOCOL.md 缺 ping/pong——已补（32 种消息）

### 回归体系升级（13 套件 / 198 断言）
```
v92(12)+v93(10)+v94(15)+v95(11)+v96(10)+v97(8)+v98(17)
+v99(19)+v910(19)+v911(26)+v912(19)+v913(14)+v914(19) = 一键全跑全过
```

## 八、协议层累计 9 项增强（三轮）
```
v9.12: 版本协商 + player_id 复用 + 位置量化
v9.13: 消息批处理 + 协议目录
v9.14: RTT 测量 + 健康评分 + 自适应频率
```

## 九、第四轮改进（v9.15——CRC 帧校验 + 消息优先级）

### 研究（第 9-10 批）
| 主题 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| CRC32（Ethernet FCS）| 0x04C11DB7 标准，检测突发错误强于校验和；Python binascii.crc32 | **❌ 无校验 → 已实现** |
| CRC vs 校验和 | CRC 检测模式错误（burst errors），简单 checksum 漏检 | 用 CRC32 |
| QoS 优先级（pvigier）| 消息分级（可靠/不可靠）+ 多流分离 | **❌ 无分级 → 已实现** |

### 改进
1. **CRC32 帧校验**（network.py）
   - 帧格式升级：`[8长度][4 CRC32][pickle]`（12 字节头）
   - 发送 `_send_json` 算 CRC；接收 `_recv_loop` 校验——坏帧丢弃不崩
   - 帧损坏/位翻转 → 丢弃；坏帧后连接存活（TCP 连续流不受影响）
2. **消息优先级**（QoS，pvigier 多流分离）
   - `_send_json(sock, payload, prio)`：0=紧急 1=普通 2=低优
   - 紧急（hello/welcome/ready/travel_*）直发；位置（sim_pos）低优可 batch
   - PROTOCOL.md 记录优先级分级

### 测试（v9.15，16 断言全过）
- A. CRC 帧格式（8长度+4CRC/20 次 CRC 正确）
- B. CRC 校验（正常通过/数据位翻转检测/CRC 字段损坏/20 次随机损坏全检测）
- C. **真实 TCP CRC 闭环**（正常帧到达/坏帧丢弃/坏帧后连接存活）
- D. 消息优先级（默认 1/紧急 0/低优 2/batch 合并低优）

### 百次测试挖出 3 个真实 bug（帧格式升级连锁）
1. **测试 mock `Net._send_json` 缺 prio 参数** → host 发 welcome 崩溃 → recv 线程没启动（v913/v914 真实 TCP 失败根因）
2. **v93 手工帧没带 proto_version** → 版本协商拒绝 → 握手失败
3. **v93 缺 binascii import**（单行 import 替换没匹配）+ **`fc` 变量覆盖全局失败计数器**

### 回归体系升级（14 套件 / 208 断言）
```
v92(12)+v93(10)+v94(15)+v95(11)+v96(10)+v97(8)+v98(17)+v99(19)
+v910(19)+v911(26)+v912(19)+v913(14)+v914(19)+v915(16) = 一键全跑全过
```

## 十、协议层累计 11 项增强（四轮）
```
v9.12: 版本协商 + player_id 复用 + 位置量化
v9.13: 消息批处理 + 协议目录
v9.14: RTT 测量 + 健康评分 + 自适应频率
v9.15: CRC 帧校验 + 消息优先级
```

## 十一、第五轮改进（v9.16——HMAC 消息签名，跨网安全）

### 研究（第 11 批）
| 主题 | 结论 | 借鉴 |
|:-----|:-----|:-----|
| HMAC（RFC 2104）| 密钥散列消息认证，防篡改+认证；TLS 1.3 用 HMAC 派生密钥 | **❌ 裸 pickle → 已实现** |
| HKDF（RFC 5869）| 主密钥 → 会话密钥派生；TLS 1.3 同款 | 握手 nonce 交换派生 |
| MAC 性能 | HMAC-SHA256 每消息微秒级，游戏无感 | 始终签名不降级 |

### 方案
1. **握手密钥交换**：client 生成 client_nonce（随机16B hex）→ hello 携带；host 生成 host_nonce → welcome 携带；双方独立派生 `key = HMAC-SHA256(房间密码, client_nonce + host_nonce)`
2. **帧签名**：帧格式升级 `[8长度][4CRC][32 HMAC-SHA256][pickle]`（44 字节头）——发送算 HMAC，接收**先验签再反序列化**（Encrypt-then-MAC 顺序）
3. **多客户端独立密钥**：`_hmac_keys[pid]` 每 client 各自 key，互不通用；host 按 pid 反查，client 用自己的 key

### 关键 bug 修复（5 个，测试挖出）
1. **帧头长度不固定**：无 key 返回 0 字节签名 → 收端固定 44 偏移错位（把 data 前 32 字节当签名）→ **修正：无 key 填 32 字节零签名占位，帧头恒 44 字节**
2. **client 端发送 key 选择**：`_sock_to_pid` 对 client socket 无效 → 改用 `_my_player_id` 查 key
3. **同进程双端测试的 `_my_nonce` 覆盖**（host 覆盖 client）——真实双端独立进程无此问题；测试手动按握手语义重建 key
4. **lobby.network = Net 污染**（C 段 mock 后 D 段真实 TCP 写错对象）——D 段前恢复真实引用
5. **旧测试帧格式连锁**：v92-v915 全部升级 44 字节头（+真 null 字节转义修复）

### 测试（v9.16，22 断言全过）
- A. 密钥派生（相同输入→同 key/不同密码/不同 nonce/20 次确定性）
- B. 签名/验签（正确通过/篡改拒绝/错误 key 拒绝/无 key 通过/20 次随机篡改检测）
- C. 握手密钥交换（host/client 各自派生 32B key）
- D. **真实 TCP 签名闭环**（签名消息到达/篡改帧被拒/篡改后连接存活）
- E. 多客户端独立密钥（各自验签/跨 client 互斥）

### 回归体系升级（15 套件全过）
```
v92(12)+v93(10)+v94(15)+v95(11)+v96(10)+v97(8)+v98(17)+v99(19)
+v910(19)+v911(26)+v912(19)+v913(14)+v914(19)+v915(16)+v916(22)
```

## 十二、协议层累计 12 项增强（五轮）
```
v9.12: 版本协商 + player_id 复用 + 位置量化
v9.13: 消息批处理 + 协议目录
v9.14: RTT 测量 + 健康评分 + 自适应频率
v9.15: CRC 帧校验 + 消息优先级
v9.16: HMAC 消息签名 + 握手密钥交换（跨网安全）
```

### 安全评估（跨网 pickle 风险闭环）
- 签名前：pickle 反序列化任意代码执行（跨网风险高）
- 签名后：**无密钥无法构造合法帧**（HMAC-SHA256 前像不可伪造）；篡改必被拒绝（先验签再反序列化）
- 残余风险：pickle 数据本身仍明文（未加密）——签名防伪造/篡改，不防窃听；局域网/信任对端可接受
- 下一步候选：Protobuf 序列化（S4MP 方案）——类型安全 + 跨语言，替代 pickle


## 十三、真机排障实战（2026-08-05 双机实测挖出 3 个测试没抓到的 bug）

> 虚拟测试全绿 ≠ 真机没问题——真机日志是最终裁判。

### 1. 模块内 `network.` 前缀 NameError
- 现象：房主建房后房间页不显示自己（members 空 + room_code 空）
- 根因：`mp_host`/`mp_apply` 里 `network._my_player_id = 0` —— **network.py 模块内没有 `network` 这个名字**（函数内 `network.xxx` 是全局查找）→ NameError → 被 `except: _log("lobby setup error")` 吞 → `add_host_self` 没执行
- 教训：**模块内函数引用自己模块的全局变量，直接写变量名，不要加模块名前缀**；真机日志 `lobby setup error: name 'network' is not defined` 是排障关键信号
- 虚拟测试没抓到：测试直接调 add_host_self，不走 mp_host 命令路径

### 2. 帧格式不兼容 → 对端秒断（协议升级破坏性实测）
- 现象：对端连上主机 1 秒内断开，host 日志 `send error: [WinError 10053]`（对端已关）
- 根因：对端装 v9.15 及更早（12 字节帧头）→ 收到 v9.16 的 44 字节头 welcome → 解析错位 → unpickle error → 主动断开
- 更早版本（JSON 时代）：客机日志 `recv error: 'utf-8' codec can't decode byte 0x81` —— **v9.16 根本不按 utf-8 解码**，出现 utf-8 解码错误 = 对端是 v7.2 之前的 JSON 协议时代
- 教训：**帧格式升级是 breaking change，两端必须同版本**；分发时强调版本一致 + 验证日志首行版本号

### 3. 打包交付完整性（bat 版本号）
- 现象：zip 里安装mod.bat 显示 v5.3（用户误以为旧版）
- 根因：bat 标题行版本号从未随版本递增
- 教训：打包核对清单含 mod/说明/bat/zip 文件名四件套版本一致性

## 十四、协议版本协商深度研究（2026-08-05 web 研究）

> 触发：真机遇到「旧客户端连新服务器秒断」——版本协商的行业最佳实践是什么？

### 研究结论
| 来源 | 方案 | 借鉴点 |
|:-----|:-----|:-------|
| **MCP spec（modelcontextprotocol.io）** | `server/discover` 协商——客户端先问服务器支持的版本列表 → 选双方都支持；不兼容返回结构化错误（`UnsupportedProtocolVersionError`）而非静默断连 | 协商放握手早期；错误要**结构化可识别**（客户端能据此给用户友好提示） |
| **Martin Evans（游戏网络协议）** | 协议必须有**版本标识符**，旧消息可检测并丢弃；向后兼容 = 同时支持新旧版本，连接建立时协商 | 帧头 magic number 快速识别协议时代 |
| **TLS / OneUptime** | 客户端服务器对齐支持的版本，双方声明支持列表 | 版本列表协商是标准做法 |
| **jser.dev** | 版本比较 + 降级计划（先支持新旧，一段时间后移除旧） | 兼容窗口期概念 |

### 我们的差距与改进候选（后续）
- ✅ 已有：PROTO_VERSION 协商（hello 带版本，不匹配发 version_mismatch）
- ❌ **盲点：帧格式不兼容发生在握手之前**——旧客户端 hello（12 字节头）在新服务器（44 字节解析）上错位 → 版本字段都读不到 → 无法发 version_mismatch → 秒断
- 🔧 候选改进：**帧头加 magic number + 协议版本**（固定偏移，任何版本都能读）→ 收端先读 magic → 判断对端协议时代 → 能兼容则降级解析，不能则发结构化错误（含"请更新到 vX"提示）而非裸断连
- 🔧 或：hello 帧用"版本无关最小编帧"（前 8 字节 = magic + version，之后才是长度前缀 + 载荷）
- 优先级：局域网信任对端场景收益低（知道更新即可），**跨网公开场景才值得做**（防恶意/误连错版本）

## 十五、五轮总结（v9.12-v9.16 完整链路）
- **研究驱动**：4 批 web 研究 → 12 项增强（版本协商/ID 复用/量化/批处理/协议目录/RTT/健康评分/自适应频率/CRC/优先级/HMAC/密钥交换）
- **测试体系**：15 套件 237 断言（端到端 TCP + 传输层 + 协议语义 + 生命周期 + 纯逻辑 + 内存/GUI/配置/fuzz + UDP 发现 + 迟滞阈值 + 容错 + 场景切换 + 版本协商 + 批处理 + 健康 + 帧校验 + 签名闭环）
- **真机验证**：双机 LAN 实测（建房/加入/聊天/位置同步）+ 双机排障（NameError/版本不兼容）
- **最大短板**：跨网真机验证（UPnP/STUN 代码就绪但从未在真实公网环境跑通）

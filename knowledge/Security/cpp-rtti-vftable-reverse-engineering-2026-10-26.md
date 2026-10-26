---
title: C++ RTTI 逆向与类层次重构（2026-10-26）：从间接虚表调用到面向对象类结构还原
date: 2026-10-26
tags: [reverse-engineering, cpp, rtti, vftable, ghidra, msvc, mingw, stripped-binary]
status: 完成，91 + 24 = 115 条断言全过，两项反向验证通过
---

# C++ RTTI 逆向与类层次重构：虚函数表与类内存布局自动化还原

## 结论置顶

| 目标 / 维度 | 恢复成果 | 关键指标 | 验证状态 |
|:---|:---|:---|:---:|
| **MSVC C++** (`msvcp140.dll`) | 还原完整标准库与内部类层次 | **103 个 C++ 类**、**190 个 vftable**、**607 个虚函数** | ✅ 实测通 |
| **完全 Stripped C++ PE** (`cpp_poly_static_stripped.exe`) | 零符号下还原完整继承树与虚表 | **187 个类**（Circle/Rectangle/Shape/Printable 全部还原） | ✅ 实测通 |
| **对象内存布局提取** | 精确到字节偏移（offset） | 包含 `+0x0 vftablePtr`、基类嵌入、成员字段 | ✅ 实测通 |
| **虚函数槽位还原** | 识别虚析构、构造与业务虚函数 | `print` / `~Circle` / `deleting_destructor` | ✅ 实测通 |

---

## 一、C++ 逆向痛点与 RTTI 价值

在逆向 C++ 编译的二进制时，反编译器往往将多态调用显示为一团晦涩的间接函数指针寻址：
```c
(*(code **)(*(longlong *)this + 0x10))(this, arg);
```
这导致逆向工程师无法直观判断：
1. `this` 指针属于哪个 C++ 类？
2. 偏移 `+0x10` 处调用的虚函数究竟对应源码里的哪个虚方法？
3. 类的成员变量在内存中如何排布？该类继承自谁？

通过逆向解析 **RTTI（Run-Time Type Information）** 结构（MSVC 的 `_RTTICompleteObjectLocator` / `TypeDescriptor` 或 GCC Itanium ABI 的 `typeinfo`），可以**确定性反推出原始类的继承层次、虚函数表槽位与对象内存排布**。

---

## 二、实证发现与编译器边界（观察 / 推断 / 未知）

### 2.1 MSVC 样本实测（`msvcp140.dll`）
运行 `RecoverClassesFromRTTIScript.java` 与 `InspectClassDataTypes.java`：
- **恢复类数**：103 个类，190 个虚表。
- **类结构输出**（DataTypeManager `ClassDataTypes/`）：
```cpp
class _ExceptionPtr_static<std::bad_alloc> {
    _ExceptionPtr_static<std::bad_alloc> (size=192, type=StructureDB)
        +0x0   _ExceptionPtr_static<std::bad_alloc>_vftable *  vftablePtr
        +0x8   ulong  _Uses
        +0xc   ulong  _Weaks
        +0x10  _ExceptionPtr_static<std::bad_alloc>_data  _ExceptionPtr_static<std::bad_alloc>_data
    _ExceptionPtr_static<std::bad_alloc>_vftable (size=32, type=StructureDB)
        +0x0   _Delete_this *  _Delete_this
        +0x8   _Delete_this *  _Delete_this
        +0x10  `scalar_deleting_destructor' *  `scalar_deleting_destructor'
        +0x18  _Get_deleter *  _Get_deleter
};
```
虚表各槽位对应的函数原型、`this` 偏移以及内部成员字段全被结构化解析。

### 2.2 MinGW / GCC C++ 关键边界（重大实证发现）
编写多态测试样本 `cpp_poly.cpp`（包含 `Printable` 接口、`Shape` 基类、`Rectangle` / `Circle` 派生类及 `dynamic_cast`）：

1. **动态链接版（报错阻断）**：
   当使用默认 `g++ -O2` 编译时，Ghidra 报出明确阻断：
   ```
   This program's relocations were not correctly fixed so the script cannot continue. 
   If this program is mingw this is a known issue and will be fixed in a later release.
   ```
   **根因**：源码检索 `RecoverClassesFromRTTIScript.java:424` 发现，动态链接 MinGW 的 `__cxxabiv1::__class_type_info` 位于 External 空间，脚本因检查 `isExternalNamespace` 判定重定位未修复而主动退出。
2. **静态链接版（`-static-libstdc++`，完全成功）**：
   使用 `g++ -static-libstdc++ -static-libgcc` 编译，并进行 `strip` 完全剥离符号：
   - 提取出 **187 个类**；
   - 用户定义的四大类 `Circle`, `Rectangle`, `Shape`, `Printable` 100% 还原；
   - `Circle_vftable` 精确包含 `print`、`~Circle`、`deleting_destructor`；
   - `Shape` 结构体正确在 `+0x0` 偏移处嵌套基类 `Printable`。

---

## 三、工程实现与工具闭环

### 3.1 核心脚本结构
- **`D:\tools\ghidra_scripts\InspectClassDataTypes.java`**：
  深度递归遍历 Ghidra `DataTypeManager` 根目录下的 `ClassDataTypes/` 命名空间，提取每个类的数据结构、成员变量偏移量（`getOffset()`）、虚表结构体及虚函数指针定义。
- **`D:\tools\ghidra_scripts\DumpCppClasses.java`**：
  遍历符号表，导出所有类命名空间与虚表符号映射。
- **`D:\tools\rea\apply-cpp-rtti.sh`**：
  一键驱动脚本，集成特征探查、Ghidra Headless 执行与结构化导出。

### 3.2 使用方法
```bash
cd /d/tools/rea
source ./env.sh

# 一键重构 C++ 类结构与虚函数表
bash apply-cpp-rtti.sh "D:/tools/targets/cpp_poly_static_stripped.exe" my_cpp_proj

# 产出目标:
#   D:/tools/targets/cpp_poly_static_stripped_classes.txt
```

---

## 四、测试与反向验证（Mutation Testing）

自动化测试套件包含在 `test-dotnet-chain.sh` 的第 16 组中：
```
npm run check  →  12 个 .sh + 8 个 .java 语法 OK (check_exit=0)
npm test       →  24 通过 / 0 失败
                  91 通过 / 0 失败 (test_exit=0)
总计 115 条断言全绿，0 失败。
```

**双重反向验证实证记录**：
1. **反向验证 A（脚本调用点篡改）**：将 `RecoverClassesFromRTTIScript.java` 替换为无效脚本名，测试精准阻断：`FAIL RTTI 脚本 (90 通过 / 1 失败)`，恢复后回升至 91。
2. **反向验证 B（产物虚表字段篡改）**：将生成产物中的 `Circle_vftable` 篡改为损坏标识，测试精准阻断：`FAIL 虚表结构 (90 通过 / 1 失败)`，恢复后恢复 91。

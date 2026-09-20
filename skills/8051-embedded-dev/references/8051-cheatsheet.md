# 8051 寄存器速查表

## 引脚定义模式
```c
// GPIO
sbit LED = P1^0;

// 特殊位
sbit EA = 0xAF;  // IE.7 全局中断
sbit TI = 0x98;  // SCON.1 发送完成
sbit RI = 0x99;  // SCON.0 接收完成
```

## 中断向量表
| 中断号 | 中断源 | 入口地址 |
|--------|--------|----------|
| 0 | INT0 (P3.2) | 0x0003 |
| 1 | Timer 0 | 0x000B |
| 2 | INT1 (P3.3) | 0x0013 |
| 3 | Timer 1 | 0x001B |
| 4 | UART | 0x0023 |

## Keil vs SDCC 差异
| 语法 | Keil C51 | SDCC |
|------|----------|------|
| 中断函数 | `void isr() interrupt 1` | `void isr() __interrupt(1)` |
| 头文件 | `#include <reg52.h>` | `#include <mcs51/8052.h>` |
| 位变量 | `bit flag;` | `__bit flag;` 或 `bool flag;` |
| 内联汇编 | `#pragma asm` / `#pragma endasm` | `__asm` / `__endasm` |
| 指定存储区 | `data` / `idata` / `xdata` / `code` | 同 Keil, 加 `__` 前缀 |

## 常用 __sfr 地址
```c
__sfr __at(0x80) P0;
__sfr __at(0x90) P1;
__sfr __at(0xA0) P2;
__sfr __at(0xB0) P3;
__sfr __at(0x89) TMOD;
__sfr __at(0x88) TCON;
__sfr __at(0x8C) TH0;
__sfr __at(0x8A) TL0;
__sfr __at(0x8D) TH1;
__sfr __at(0x8B) TL1;
__sfr __at(0x98) SCON;
__sfr __at(0x99) SBUF;
__sfr __at(0xA8) IE;
__sfr __at(0xB8) IP;
```
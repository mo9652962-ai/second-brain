# STC89C52 智能温控器

> **技能**: 8051-embedded-dev v2.0 | **复杂度**: ⭐⭐⭐
> **关键词**: 8051、DS18B20、LCD1602、PID、定时器中断

---

## 项目概述

基于 STC89C52RC 的数字温控系统，实时采集温度并通过 LCD 显示，支持继电器控制加热设备。

## 硬件设计

### 系统框图
```
DS18B20 ─→ P3.7 (单总线)
               ↓
STC89C52RC ───→ P0: LCD1602 数据
               → P2.0-2.2: LCD 控制
               → P1.0: 继电器控制
               → P1.1: 按键输入
```

### 元件清单
| 元件 | 型号/规格 | 数量 |
|:----|:---------|:---:|
| 单片机 | STC89C52RC | 1 |
| 温度传感器 | DS18B20 (TO-92) | 1 |
| 显示屏 | LCD1602 + IIC 转接板 | 1 |
| 继电器 | 5V 单路继电器模块 | 1 |
| 晶振 | 12MHz | 1 |
| 电容 | 30pF ×2, 10μF ×1 | |
| 电阻 | 10KΩ 排阻 ×1, 4.7KΩ ×1 | |
| 按键 | 轻触开关 ×2 | |

## 核心代码

### 温度采集 (DS18B20)
```c
#include <reg52.h>
#include <intrins.h>

typedef unsigned char u8;
typedef unsigned int u16;

sbit DQ = P3^7;  // DS18B20 数据线

// 延时函数 (12MHz)
void delay_us(u8 us) {
    while (us--) _nop_();
}

// DS18B20 复位
u8 ds18b20_reset() {
    u8 presence;
    DQ = 0; delay_us(480);
    DQ = 1; delay_us(60);
    presence = DQ;
    delay_us(420);
    return presence;  // 0=存在
}

// 写字节
void ds18b20_write_byte(u8 dat) {
    u8 i;
    for (i = 0; i < 8; i++) {
        DQ = 0; _nop_();
        DQ = dat & 0x01;
        delay_us(60);
        DQ = 1; _nop_();
        dat >>= 1;
    }
}

// 读字节
u8 ds18b20_read_byte() {
    u8 i, dat = 0;
    for (i = 0; i < 8; i++) {
        dat >>= 1;
        DQ = 0; _nop_(); _nop_();
        DQ = 1; _nop_();
        if (DQ) dat |= 0x80;
        delay_us(60);
    }
    return dat;
}

// 读取温度 (返回摄氏温度×10)
int ds18b20_read_temp() {
    u8 temp_l, temp_h;
    int temp;
    
    ds18b20_reset();
    ds18b20_write_byte(0xCC);  // 跳过ROM
    ds18b20_write_byte(0x44);  // 启动转换
    
    delay_ms(750);  // 等待转换完成
    
    ds18b20_reset();
    ds18b20_write_byte(0xCC);
    ds18b20_write_byte(0xBE);  // 读取暂存器
    
    temp_l = ds18b20_read_byte();
    temp_h = ds18b20_read_byte();
    
    temp = (temp_h << 8) | temp_l;
    temp = temp * 10 / 16;  // 转换为℃×10
    
    return temp;
}
```

### LCD1602 驱动
```c
sbit RS = P2^0;  sbit RW = P2^1;  sbit EN = P2^2;
#define LCD_DATA P0

void lcd_cmd(u8 cmd) {
    RS=0; RW=0; LCD_DATA=cmd;
    EN=1; delay_us(5); EN=0; delay_ms(2);
}

void lcd_dat(u8 dat) {
    RS=1; RW=0; LCD_DATA=dat;
    EN=1; delay_us(5); EN=0; delay_ms(2);
}

void lcd_init() {
    lcd_cmd(0x38); lcd_cmd(0x0C);
    lcd_cmd(0x06); lcd_cmd(0x01);
}

void lcd_str(u8 row, u8 col, u8 *s) {
    u8 addr = row ? 0x40 : 0x00;
    lcd_cmd(0x80 | (addr + col));
    while (*s) lcd_dat(*s++);
}

void lcd_digit(int val, u8 row, u8 col) {
    u8 buf[8];
    u8 i = 0;
    if (val < 0) { lcd_dat('-'); val = -val; }
    do { buf[i++] = val % 10 + '0'; val /= 10; } while (val);
    while (i) lcd_dat(buf[--i]);
}
```

### PID 控制
```c
typedef struct {
    int setpoint;    // 目标温度(℃×10)
    int kp, ki, kd;  // PID 参数
    int prev_error;
    int integral;
    int output;      // 输出 0-100
} PID;

void pid_init(PID *pid, int sp, int kp, int ki, int kd) {
    pid->setpoint = sp;
    pid->kp = kp; pid->ki = ki; pid->kd = kd;
    pid->prev_error = 0;
    pid->integral = 0;
}

void pid_compute(PID *pid, int input) {
    int error = pid->setpoint - input;
    pid->integral += error;
    if (pid->integral > 500) pid->integral = 500;
    if (pid->integral < -500) pid->integral = -500;
    int derivative = error - pid->prev_error;
    pid->output = (pid->kp * error + pid->ki * pid->integral + pid->kd * derivative) / 100;
    if (pid->output > 100) pid->output = 100;
    if (pid->output < 0) pid->output = 0;
    pid->prev_error = error;
}
```

### 主程序
```c
void main() {
    int temp;
    PID pid;
    
    lcd_init();
    lcd_str(0, 0, "Temp:     .   C");
    lcd_str(1, 0, "Target:   25.0 C");
    
    pid_init(&pid, 250, 30, 2, 10);  // 目标25℃, PID参数
    
    while (1) {
        temp = ds18b20_read_temp();  // 读取温度
        
        pid_compute(&pid, temp);      // PID计算
        
        // 控制继电器
        if (pid.output > 50) P1_0 = 0;  // 开启加热
        else P1_0 = 1;                   // 关闭加热
        
        // LCD 显示
        lcd_digit(temp, 0, 6);           // 个位
        lcd_dat('.');                     // 小数点
        lcd_digit(temp % 10, 0, 8);       // 十分位
        lcd_digit(pid.setpoint / 10, 1, 7);  // 目标温度
        
        delay_ms(1000);  // 每秒刷新
    }
}
```

## 烧录指南

### 硬件接线
```
USB-TTL      STC89C52RC
 TXD  ────── P3.0/RXD
 RXD  ────── P3.1/TXD
 GND  ────── GND
 VCC  ────── 独立5V供电 (烧录时断电再上电)
```

### 烧录步骤
1. 打开 STC-ISP 软件
2. 选择芯片型号: STC89C52RC
3. 选择串口号
4. 加载编译好的 .hex 文件
5. 点击「下载/编程」
6. **断电 → 重新上电** (冷启动)
7. 等待烧录完成

## 技术要点

| 要点 | 说明 |
|:----|:----|
| DS18B20 时序 | 单总线协议对时序敏感，12MHz 下延时需微调 |
| P0 口上拉 | 必须外接 10KΩ 排阻到 VCC |
| PID 参数整定 | kp=30, ki=2, kd=10 适用于小体积加热腔 |
| 温度精度 | DS18B20 默认 12 位分辨率，0.0625°C |

## 生成日期
2026-07-22 | 由 8051-embedded-dev skill 生成

---
> 🗺️ 属于 [[knowledge-map]] · [[Home|🏠 Home]]

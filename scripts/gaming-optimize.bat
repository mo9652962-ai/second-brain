@echo off
chcp 65001 >nul
echo ============================================
echo   游戏性能优化脚本 (需管理员权限运行)
echo   RTX 4060 Laptop + i7-13620H
echo ============================================
echo.

echo [1/8] 停止遥测和诊断服务...
sc stop DiagTrack >nul 2>&1
sc config DiagTrack start=disabled >nul 2>&1
echo  ✓ DiagTrack 已禁用

echo [2/8] 优化 Superfetch (减少游戏时磁盘占用)...
sc config SysMain start=manual >nul 2>&1
sc stop SysMain >nul 2>&1
echo  ✓ SysMain 已设为手动

echo [3/8] 设置 CPU 优先级偏向前台程序...
reg add "HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl" /v Win32PrioritySeparation /t REG_DWORD /d 38 /f >nul 2>&1
echo  ✓ CPU 调度已优化

echo [4/8] 启用硬件加速 GPU 调度 (HAGS)...
reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v HwSchMode /t REG_DWORD /d 2 /f >nul 2>&1
echo  ✓ HAGS 已启用

echo [5/8] 禁用游戏录屏和 Game Bar...
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\GameDVR" /v AppCaptureEnabled /t REG_DWORD /d 0 /f >nul 2>&1
reg add "HKCU\System\GameConfigStore" /v GameDVR_Enabled /t REG_DWORD /d 0 /f >nul 2>&1
echo  ✓ 游戏录屏已禁用

echo [6/8] 禁用窗口动画 (节省 GPU 资源)...
reg add "HKCU\Control Panel\Desktop" /v UserPreferencesMask /t REG_BINARY /d 9012038010000000 /f >nul 2>&1
reg add "HKCU\Control Panel\Desktop\WindowMetrics" /v MinAnimate /t REG_SZ /d 0 /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v TaskbarAnimations /t REG_DWORD /d 0 /f >nul 2>&1
echo  ✓ 视觉特效已调整为性能模式

echo [7/8] 禁用网络节流...
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v NetworkThrottlingIndex /t REG_DWORD /d ffffffff /f >nul 2>&1
echo  ✓ 网络节流已禁用

echo [8/8] 设置系统响应性优化为游戏模式...
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" /v SystemResponsiveness /t REG_DWORD /d 0 /f >nul 2>&1
echo  ✓ 系统响应已优化为游戏模式

echo.
echo ============================================
echo   优化完成！ 请重启电脑让所有设置生效。
echo ============================================
echo.
echo 重启后请在 NVIDIA 控制面板中手动设置:
echo   1. 管理3D设置 → 电源管理模式 → 最高性能优先
echo   2. 管理3D设置 → 纹理过滤质量 → 高性能
echo   3. 配置 PhysX → 处理器 → RTX 4060
echo.
pause

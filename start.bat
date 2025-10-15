@echo off
chcp 65001 >nul

echo 🚀 Java面试八股文阅读器启动中...
echo ==========================================

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ 找到 Python
    python start.py
) else (
    echo ❌ 未找到 Python，请先安装 Python
    echo 💡 安装方法：
    echo    1. 访问 https://www.python.org/downloads/
    echo    2. 下载并安装 Python
    echo    3. 重新运行此脚本
    pause
    exit /b 1
)
#!/bin/bash

# Java面试八股文阅读器启动脚本 (macOS/Linux)

echo "🚀 Java面试八股文阅读器启动中..."
echo "=========================================="

# 检查Python是否安装
if command -v python3 &> /dev/null; then
    echo "✅ 找到 Python3"
    python3 start.py
elif command -v python &> /dev/null; then
    echo "✅ 找到 Python"
    python start.py
else
    echo "❌ 未找到 Python，请先安装 Python"
    echo "💡 安装方法："
    echo "   macOS: brew install python3"
    echo "   或访问: https://www.python.org/downloads/"
    exit 1
fi
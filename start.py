#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Java面试八股文阅读器启动脚本
使用方法：python start.py 或 python3 start.py
"""

import http.server
import socketserver
import webbrowser
import os
import sys

def main():
    # 获取当前目录
    port = 8000
    directory = os.path.dirname(os.path.abspath(__file__))

    print("🚀 Java面试八股文阅读器")
    print("=" * 40)
    print(f"📁 服务器目录: {directory}")
    print(f"🌐 服务地址: http://localhost:{port}")
    print("=" * 40)
    print("按 Ctrl+C 停止服务器")
    print()

    # 切换到脚本所在目录
    os.chdir(directory)

    try:
        # 创建HTTP服务器
        with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
            print(f"✅ 服务器已启动在端口 {port}")

            # 自动打开浏览器
            try:
                webbrowser.open(f'http://localhost:{port}')
                print("🌐 已自动打开浏览器")
            except:
                print("⚠️  无法自动打开浏览器，请手动访问: http://localhost:{port}")

            print()
            print("📖 开始阅读你的Java八股文吧！")
            print()

            # 启动服务器
            httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n👋 服务器已停止")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {port} 已被占用，请尝试其他端口")
            print("💡 修改脚本中的 port 变量为其他数字，比如 8001")
        else:
            print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本 - 验证文件路径修复效果
"""

import os
import requests
import time
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def test_file_paths():
    """测试文件路径是否正确"""
    base_dir = "/Users/liyang/Desktop/03-学习资料/hollis八股文(1)"

    test_files = [
        "必读/必读.md",
        "必读/我该看哪些东西？.md",
        "面试必备/面试前必须要准备哪些内容？.md",
        "面试必备/简历指导.md",
        "Java基础/如何理解面向对象和面向过程？.md",
        "JVM/Java是如何实现的平台无关？.md",
        "Spring/介绍一下Spring的IOC.md",
        "MySQL/有了关系型数据库，为什么还需要NOSQL？.md",
        "Redis/Redis为什么这么快？.md"
    ]

    print("🔍 测试文件路径...")
    print("=" * 50)

    available = 0
    missing = 0

    for file_path in test_files:
        full_path = os.path.join(base_dir, file_path)
        if os.path.exists(full_path):
            print(f"✅ {file_path}")
            available += 1
        else:
            print(f"❌ {file_path}")
            missing += 1

    print("=" * 50)
    print(f"📊 测试结果: {available} 个可用, {missing} 个缺失")

    return available > 0

def test_server():
    """测试本地服务器"""
    port = 8001  # 使用不同端口避免冲突
    base_dir = "/Users/liyang/Desktop/03-学习资料/hollis八股文(1)"

    print(f"\n🚀 启动测试服务器 (端口 {port})...")

    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass  # 静默处理日志

    os.chdir(base_dir)

    try:
        with TCPServer(("", port), QuietHandler) as httpd:
            print(f"✅ 服务器已启动: http://localhost:{port}")

            # 测试几个关键文件
            test_urls = [
                f"http://localhost:{port}/index.html",
                f"http://localhost:{port}/必读/必读.md",
                f"http://localhost:{port}/面试必备/简历指导.md"
            ]

            print("\n🔍 测试URL访问...")
            for url in test_urls:
                try:
                    response = requests.get(url, timeout=2)
                    if response.status_code == 200:
                        print(f"✅ {url} - 状态码: {response.status_code}")
                    else:
                        print(f"❌ {url} - 状态码: {response.status_code}")
                except Exception as e:
                    print(f"❌ {url} - 错误: {str(e)}")

            print(f"\n🌐 测试服务器运行中... 访问: http://localhost:{port}")
            print("按 Ctrl+C 停止测试服务器")

            # 运行5秒后自动停止
            def stop_server():
                time.sleep(5)
                print("\n🛑 测试完成，停止服务器")
                httpd.shutdown()

            stop_thread = threading.Thread(target=stop_server)
            stop_thread.daemon = True
            stop_thread.start()

            httpd.serve_forever()

    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ 端口 {port} 已被占用")
        else:
            print(f"❌ 服务器启动失败: {e}")

if __name__ == "__main__":
    print("🧪 Java八股文阅读器 - 修复验证测试")
    print("=" * 60)

    # 测试文件路径
    files_ok = test_file_paths()

    if files_ok:
        print("\n✅ 文件路径测试通过！")
        print("\n现在可以运行以下命令启动完整版本:")
        print("python3 start.py")
        print("\n或直接双击 index.html 文件使用离线模式")
    else:
        print("\n❌ 文件路径测试失败，请检查文件是否存在于正确位置")

    # 可选: 启动测试服务器
    user_input = input("\n是否启动测试服务器? (y/n): ").lower()
    if user_input == 'y':
        test_server()
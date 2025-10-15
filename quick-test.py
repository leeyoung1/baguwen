#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速测试脚本 - 验证服务器模式下的文档加载
"""

import os
import sys
import time
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def quick_test():
    """快速测试服务器模式"""
    port = 8002
    base_dir = "/Users/liyang/Desktop/03-学习资料/hollis八股文(1)"

    print("🚀 快速测试 - 服务器模式")
    print("=" * 50)

    # 检查关键文件
    key_files = [
        "index.html",
        "index.md",
        "Tomcat/Tomcat的启动流程是怎样的？.md",
        "面试必备/面试前必须要准备哪些内容？.md",
        "Java基础/如何理解面向对象和面向过程？.md"
    ]

    missing_files = []
    for file_path in key_files:
        full_path = os.path.join(base_dir, file_path)
        if not os.path.exists(full_path):
            missing_files.append(file_path)

    if missing_files:
        print("❌ 缺失关键文件:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False

    print("✅ 关键文件检查通过")

    # 启动测试服务器
    print(f"\n🚀 启动测试服务器 (端口 {port})...")
    print(f"📁 服务目录: {base_dir}")

    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass  # 静默处理日志

    os.chdir(base_dir)

    try:
        with TCPServer(("", port), QuietHandler) as httpd:
            print(f"✅ 服务器已启动: http://localhost:{port}")
            print("📖 测试内容:")
            print("   - 主页面加载")
            print("   - 文档索引解析")
            print("   - 关键文档访问")
            print("\n⏳ 3秒后自动打开浏览器...")

            # 延迟打开浏览器
            def delayed_open():
                time.sleep(3)
                try:
                    webbrowser.open(f'http://localhost:{port}')
                    print("🌐 浏览器已打开")
                except:
                    print("❌ 无法自动打开浏览器，请手动访问")

            browser_thread = threading.Thread(target=delayed_open)
            browser_thread.daemon = True
            browser_thread.start()

            # 运行10秒后停止
            def auto_stop():
                time.sleep(10)
                print("\n🛑 测试完成")
                httpd.shutdown()

            stop_thread = threading.Thread(target=auto_stop)
            stop_thread.daemon = True
            stop_thread.start()

            print("🔄 服务器运行中... (10秒后自动停止)")
            httpd.serve_forever()

    except OSError as e:
        print(f"❌ 端口 {port} 被占用或无法使用")
        return False
    except KeyboardInterrupt:
        print("\n👋 测试已停止")
        return False

    return True

if __name__ == "__main__":
    success = quick_test()

    if success:
        print("\n✅ 测试完成！")
        print("📖 现在可以正常运行完整版本:")
        print("   python3 start.py")
    else:
        print("\n❌ 测试失败，请检查文件是否正确")
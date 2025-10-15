#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试特定文件：Thread.sleep(0)的作用是什么？.md
"""

import requests
import urllib.parse

def test_specific_file():
    """测试Thread.sleep文件"""
    base_url = "http://localhost:8002"
    file_path = "Java并发/Thread.sleep(0)的作用是什么？.md"

    print("🧪 测试特定文件: Thread.sleep(0)的作用是什么？.md")
    print("=" * 60)

    # 编码路径
    encoded_path = urllib.parse.quote(file_path)
    full_url = f"{base_url}/{encoded_path}"

    print(f"原始路径: {file_path}")
    print(f"编码路径: {encoded_path}")
    print(f"完整URL: {full_url}")
    print()

    try:
        # 测试HEAD请求
        print("📡 测试HEAD请求...")
        response = requests.head(full_url, timeout=5)
        print(f"   状态码: {response.status_code}")

        if response.status_code == 200:
            print("   ✅ 文件存在且可访问")
        else:
            print(f"   ❌ 文件不可访问: {response.reason}")

        # 测试GET请求
        print("\n📡 测试GET请求...")
        response = requests.get(full_url, timeout=5)
        print(f"   状态码: {response.status_code}")

        if response.status_code == 200:
            content = response.text
            print(f"   ✅ 文件内容加载成功")
            print(f"   内容长度: {len(content)} 字符")
            print(f"   前100个字符: {content[:100]}...")
        else:
            print(f"   ❌ 文件内容加载失败: {response.reason}")

    except Exception as e:
        print(f"❌ 请求失败: {e}")

    # 测试原始路径（不编码）
    print(f"\n📡 测试原始路径（不编码）...")
    original_url = f"{base_url}/{file_path}"
    print(f"URL: {original_url}")

    try:
        response = requests.head(original_url, timeout=5)
        print(f"   状态码: {response.status_code}")

        if response.status_code == 200:
            print("   ✅ 原始路径也可访问")
        else:
            print(f"   ❌ 原始路径不可访问: {response.reason}")
    except Exception as e:
        print(f"   ❌ 原始路径请求失败: {e}")

if __name__ == "__main__":
    test_specific_file()
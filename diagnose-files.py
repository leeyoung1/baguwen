#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件名诊断脚本 - 找出可能存在问题的文件名
"""

import os
import re
from urllib.parse import quote, unquote

def diagnose_special_chars():
    """诊断包含特殊字符的文件名"""
    base_dir = "/Users/liyang/Desktop/03-学习资料/hollis八股文(1)"

    print("🔍 诊断包含特殊字符的文件名")
    print("=" * 60)

    problem_files = []
    special_char_files = []

    # 遍历所有MD文件
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, base_dir)

                # 检查特殊字符
                has_special_chars = bool(re.search(r'[()（）&，、？?！!]', file))
                has_parentheses = '(' in file or ')' in file or '（' in file or '）' in file
                has_chinese = any('\u4e00' <= char <= '\u9fff' for char in file)

                if has_special_chars or has_parentheses:
                    special_char_files.append({
                        'original': relative_path,
                        'quoted': quote(relative_path),
                        'exists': os.path.exists(full_path)
                    })

                # 检查常见的可能有问题的情况
                if any(char in file for char in ['(', ')', '（', '）', '&', '，', '？', '!', '。']):
                    problem_files.append({
                        'file': file,
                        'path': relative_path,
                        'encoded': quote(relative_path, safe='')
                    })

    print(f"📊 发现 {len(special_char_files)} 个包含特殊字符的文件")
    print(f"⚠️  发现 {len(problem_files)} 个可能存在问题的文件")

    if problem_files:
        print("\n🔍 详细问题文件列表:")
        print("-" * 50)
        for i, file_info in enumerate(problem_files[:10], 1):  # 只显示前10个
            original = file_info.get('file', 'unknown')
            encoded = file_info.get('encoded', 'unknown')
            print(f"{i:2d}. 原始: {original}")
            print(f"    编码: {encoded}")
            print()

    if len(problem_files) > 10:
        print(f"... 还有 {len(problem_files) - 10} 个文件")

    # 测试一些具体的问题文件
    test_files = [
        "Java基础/BigDecimal(double)和BigDecimal(String)有什么区别？.md",
        "Java基础/Java中创建对象有哪些种方式.md",
        "Java基础/如何理解Java中的多态？.md"
    ]

    print("\n🧪 测试具体文件:")
    print("-" * 30)
    for test_file in test_files:
        full_path = os.path.join(base_dir, test_file)
        if os.path.exists(full_path):
            print(f"✅ {test_file} - 存在")
        else:
            print(f"❌ {test_file} - 不存在")
            # 尝试查找可能的变体
            print(f"   尝试查找类似文件...")
            base_dir_part = os.path.dirname(full_path)
            base_name = os.path.basename(full_path)

            if os.path.exists(base_dir_part):
                similar_files = [f for f in os.listdir(base_dir_part)
                               if f.endswith('.md') and 'BigDecimal' in f]
                for similar in similar_files[:3]:
                    print(f"   📄 {similar}")

    return problem_files

def fix_url_paths():
    """修复URL路径处理"""
    print("\n🔧 URL路径修复建议:")
    print("=" * 30)
    print("1. 在服务器模式下，需要对文件路径进行URL编码")
    print("2. 在浏览器中访问时，特殊字符会被自动编码")
    print("3. 需要确保JavaScript正确处理URL解码")

    print("\n💡 建议的修复方案:")
    print("1. 在loadDocument函数中添加URL编码处理")
    print("2. 使用encodeURIComponent对文件路径进行编码")
    print("3. 确保服务器能正确处理编码后的URL")

if __name__ == "__main__":
    problem_files = diagnose_special_chars()
    fix_url_paths()
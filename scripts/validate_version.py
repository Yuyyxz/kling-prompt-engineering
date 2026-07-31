#!/usr/bin/env python3
"""验证版本号"""
import re
import sys

def validate_version(version):
    """验证版本号（语义化版本）"""
    # 语义化版本规范：主版本号.次版本号.修订号
    pattern = r'^\d+\.\d+\.\d+$'
    return bool(re.match(pattern, version))

def main():
    if len(sys.argv) < 2:
        print("用法: python validate_version.py <version>")
        sys.exit(1)
    
    version = sys.argv[1]
    is_valid = validate_version(version)
    print(f"{'✅' if is_valid else '❌'} 版本号: {version}")
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()

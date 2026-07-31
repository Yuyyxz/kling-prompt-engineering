#!/usr/bin/env python3
"""验证命名规范"""
import re
import sys

def validate_naming_convention(name):
    """验证命名规范（kebab-case）"""
    # kebab-case 规范：小写字母、数字、连字符
    pattern = r'^[a-z0-9]+(-[a-z0-9]+)*$'
    return bool(re.match(pattern, name))

def main():
    if len(sys.argv) < 2:
        print("用法: python validate_naming_convention.py <name>")
        sys.exit(1)
    
    name = sys.argv[1]
    is_valid = validate_naming_convention(name)
    print(f"{'✅' if is_valid else '❌'} 命名规范: {name}")
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()

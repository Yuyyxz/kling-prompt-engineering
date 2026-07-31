#!/usr/bin/env python3
"""验证 YAML 文件格式"""
import yaml
import sys
import os

def validate_yaml(file_path):
    """验证 YAML 文件格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml.safe_load(f)
        return True, "YAML 格式正确"
    except yaml.YAMLError as e:
        return False, f"YAML 格式错误: {e}"
    except FileNotFoundError:
        return False, f"文件不存在: {file_path}"
    except Exception as e:
        return False, f"未知错误: {e}"

def main():
    if len(sys.argv) < 2:
        print("用法: python validate_yaml.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    is_valid, message = validate_yaml(file_path)
    print(f"{'✅' if is_valid else '❌'} {message}")
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""验证必需字段"""
import yaml
import sys

REQUIRED_FIELDS = ["name", "version", "description", "philosophy"]

def validate_required_fields(file_path):
    """验证必需字段"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if not isinstance(data, dict):
            return False, "文件内容不是有效的字典格式"
        
        missing_fields = []
        for field in REQUIRED_FIELDS:
            if field not in data:
                missing_fields.append(field)
        
        if missing_fields:
            return False, f"缺少必需字段: {', '.join(missing_fields)}"
        return True, "所有必需字段都存在"
    except yaml.YAMLError as e:
        return False, f"YAML 格式错误: {e}"
    except FileNotFoundError:
        return False, f"文件不存在: {file_path}"
    except Exception as e:
        return False, f"未知错误: {e}"

def main():
    if len(sys.argv) < 2:
        print("用法: python validate_required_fields.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    is_valid, message = validate_required_fields(file_path)
    print(f"{'✅' if is_valid else '❌'} {message}")
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()

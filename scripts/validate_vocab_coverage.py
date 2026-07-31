#!/usr/bin/env python3
"""验证词汇覆盖"""
import yaml
import sys

REQUIRED_CATEGORIES = ["visual_styles", "camera_language", "lighting", "emotions"]
MINIMUM_COUNTS = {
    "visual_styles": 5,
    "camera_language": 10,
    "lighting": 5,
    "emotions": 5
}

def validate_vocab_coverage(file_path):
    """验证词汇覆盖"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if not isinstance(data, dict):
            return False, "文件内容不是有效的字典格式"
        
        issues = []
        for category in REQUIRED_CATEGORIES:
            if category not in data:
                issues.append(f"缺少类别: {category}")
            elif not isinstance(data[category], list):
                issues.append(f"{category} 不是列表格式")
            elif len(data[category]) < MINIMUM_COUNTS[category]:
                issues.append(f"{category} 词汇数量不足: {len(data[category])} < {MINIMUM_COUNTS[category]}")
        
        if issues:
            return False, "; ".join(issues)
        return True, "词汇覆盖完整"
    except yaml.YAMLError as e:
        return False, f"YAML 格式错误: {e}"
    except FileNotFoundError:
        return False, f"文件不存在: {file_path}"
    except Exception as e:
        return False, f"未知错误: {e}"

def main():
    if len(sys.argv) < 2:
        print("用法: python validate_vocab_coverage.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    is_valid, message = validate_vocab_coverage(file_path)
    print(f"{'✅' if is_valid else '❌'} {message}")
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""综合验证脚本 - 运行所有验证"""
import yaml
import sys
import os
import re

# 验证函数
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

def validate_required_fields(file_path):
    """验证必需字段"""
    REQUIRED_FIELDS = ["name", "version", "description", "philosophy"]
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
    except Exception as e:
        return False, f"验证失败: {e}"

def validate_naming_convention(name):
    """验证命名规范"""
    pattern = r'^[a-z0-9]+(-[a-z0-9]+)*$'
    return bool(re.match(pattern, name))

def validate_version(version):
    """验证版本号"""
    pattern = r'^\d+\.\d+\.\d+$'
    return bool(re.match(pattern, version))

def validate_skill_file(file_path):
    """验证单个 Skill 文件"""
    results = []
    
    # 1. 验证 YAML 格式
    is_valid, message = validate_yaml(file_path)
    results.append(("Schema Check - YAML 格式", is_valid, message))
    
    if not is_valid:
        return results
    
    # 2. 验证必需字段
    is_valid, message = validate_required_fields(file_path)
    results.append(("Schema Check - 必需字段", is_valid, message))
    
    # 3. 验证命名规范
    filename = os.path.basename(file_path)
    name_without_ext = os.path.splitext(filename)[0]
    is_valid = validate_naming_convention(name_without_ext)
    results.append(("Design Audit - 命名规范", is_valid, f"文件名: {filename}"))
    
    # 4. 验证版本号
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        if 'version' in data:
            is_valid = validate_version(data['version'])
            results.append(("Design Audit - 版本号", is_valid, f"版本: {data['version']}"))
    except:
        pass
    
    return results

def main():
    if len(sys.argv) < 2:
        print("用法: python validate_all.py <file_path_or_directory>")
        print("示例:")
        print("  python validate_all.py skills/director-engine.skill")
        print("  python validate_all.py skills/")
        sys.exit(1)
    
    target = sys.argv[1]
    
    # 获取要验证的文件列表
    files_to_validate = []
    if os.path.isfile(target):
        files_to_validate.append(target)
    elif os.path.isdir(target):
        for filename in os.listdir(target):
            if filename.endswith('.skill') or filename.endswith('.yaml') or filename.endswith('.yml'):
                files_to_validate.append(os.path.join(target, filename))
    else:
        print(f"❌ 路径不存在: {target}")
        sys.exit(1)
    
    if not files_to_validate:
        print(f"❌ 没有找到可验证的文件: {target}")
        sys.exit(1)
    
    # 运行验证
    total_files = len(files_to_validate)
    passed_files = 0
    failed_files = 0
    
    print(f"🔍 开始验证 {total_files} 个文件...\n")
    
    for file_path in files_to_validate:
        print(f"📄 验证文件: {file_path}")
        results = validate_skill_file(file_path)
        
        file_passed = True
        for check_name, is_valid, message in results:
            status = "✅" if is_valid else "❌"
            print(f"  {status} {check_name}: {message}")
            if not is_valid:
                file_passed = False
        
        if file_passed:
            passed_files += 1
            print(f"  ✅ 文件验证通过\n")
        else:
            failed_files += 1
            print(f"  ❌ 文件验证失败\n")
    
    # 输出总结
    print("=" * 50)
    print(f"📊 验证总结:")
    print(f"  总文件数: {total_files}")
    print(f"  通过: {passed_files}")
    print(f"  失败: {failed_files}")
    print(f"  通过率: {passed_files/total_files*100:.1f}%")
    
    if failed_files > 0:
        print(f"\n❌ 有 {failed_files} 个文件验证失败")
        sys.exit(1)
    else:
        print(f"\n✅ 所有文件验证通过")
        sys.exit(0)

if __name__ == "__main__":
    main()

import os
import sys
import re

def generate_mock_python(class_name, methods=None):
    if methods is None:
        methods = ["execute", "get_status", "submit"]
    
    mock_code = f"class Mock{class_name}:\n"
    mock_code += "    def __init__(self, *args, **kwargs):\n"
    mock_code += "        print(f'Initialized Mock {class_name}')\n\n"
    
    for method in methods:
        mock_code += f"    def {method}(self, *args, **kwargs):\n"
        mock_code += f"        print(f'Mock {class_name}.{method} called')\n"
        mock_code += "        return {'status': 'mocked_success', 'data': []}\n\n"
    
    return mock_code

def patch_file_with_mock(file_path, dependency_name):
    if not os.path.exists(file_path):
        return False
        
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Simple replacement heuristic: if 'import dep' exists, comment it and add mock
    if f"import {dependency_name}" in content or f"from {dependency_name}" in content:
        mock_class = generate_mock_python(dependency_name.capitalize())
        new_content = f"# MOCKED BY ANTIGRAVITY\n{mock_class}\n{content}"
        # Comment out the real import
        new_content = re.sub(f"(import {dependency_name})", r"# \1", new_content)
        new_content = re.sub(f"(from {dependency_name})", r"# \1", new_content)
        
        with open(file_path, 'w') as f:
            f.write(new_content)
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python mock_generator.py <file_to_patch> <dependency_name>")
        sys.exit(1)
        
    target_file = sys.argv[1]
    dep = sys.argv[2]
    
    if patch_file_with_mock(target_file, dep):
        print(f"Successfully patched {target_file} with mock for {dep}")
    else:
        print(f"Could not find {dep} in {target_file}")

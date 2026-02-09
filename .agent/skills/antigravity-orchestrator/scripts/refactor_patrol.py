import os
import ast
import json
from typing import List

# Paths
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SKILL_ROOT))

class RefactorPatrol:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.findings = []

    def analyze_complexity(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())
            
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    # Ensure line numbers exist and are integers
                    start_ln = getattr(node, 'lineno', None)
                    end_ln = getattr(node, 'end_lineno', None)
                    
                    if isinstance(start_ln, int) and isinstance(end_ln, int):
                        lines = end_ln - start_ln
                        if lines > 50:
                            self.findings.append({
                                "file": os.path.relpath(file_path, self.root_dir),
                                "type": "Complexity",
                                "item": getattr(node, 'name', 'anonymous'),
                                "severity": "MEDIUM",
                                "msg": f"Function '{getattr(node, 'name', 'anonymous')}' is too long ({lines} lines)."
                            })
                    
                    # Detect cognitive load via nesting depth
                    nesting_hits: List[int] = []
                    for subnode in ast.walk(node):
                        if isinstance(subnode, (ast.If, ast.For, ast.While, ast.With)):
                            nesting_hits.append(1)
                    
                    if len(nesting_hits) > 10:
                        self.findings.append({
                            "file": os.path.relpath(file_path, self.root_dir),
                            "type": "Nesting",
                            "item": getattr(node, 'name', 'anonymous'),
                            "severity": "HIGH",
                            "msg": f"Function '{getattr(node, 'name', 'anonymous')}' has high cognitive load (depth={len(nesting_hits)})."
                        })
        except Exception as e:
            pass

    def scan_project(self):
        for root, dirs, files in os.walk(self.root_dir):
            if ".sandbox" in root or ".git" in root or "__pycache__" in root:
                continue
            for file in files:
                if file.endswith(".py"):
                    self.analyze_complexity(os.path.join(root, file))
        
        return self.findings

if __name__ == "__main__":
    print("🚀 Antigravity Refactor Patrol: Scanning for architectural decay...")
    patrol = RefactorPatrol(PROJECT_ROOT)
    results = patrol.scan_project()
    
    report_path = os.path.join(SKILL_ROOT, "resources", "refactor_report.json")
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    if results:
        print(f"Patrol Complete: Found {len(results)} potential refactors. Report saved.")
    else:
        print("Patrol Complete: Codebase is currently Architecture-Healthy. Report cleared.")

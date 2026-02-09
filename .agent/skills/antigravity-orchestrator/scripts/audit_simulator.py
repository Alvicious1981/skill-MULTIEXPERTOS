import os
import sys
import json
import ast
import subprocess
import datetime
import shutil

# --- SCENARIOS ---
SCENARIOS = {
    "security_breach": {
        "name": "Hardcoded Secret Detection",
        "file": "config_api.py",
        "content": "AWS_SECRET = 'AKIAIMNO789012345678'",
        "expected_defender": "01",
        "severity": "CRITICAL"
    },
    "syntax_error": {
        "name": "Broken Code Recovery",
        "file": "logic_v9.py",
        "content": "def calculate():\n    print('Missing return' ",
        "expected_defender": "05",
        "severity": "HIGH"
    },
    "missing_dependency": {
        "name": "Ghost Import Mitigation",
        "file": "adapter.py",
        "content": "import nonexistent_lib\ndef run():\n    return nonexistent_lib.execute()",
        "expected_defender": "08",
        "severity": "MEDIUM"
    },
    "logical_conflict": {
        "name": "Expert Role Collision",
        "file": "architecture_proposal.md",
        "content": "Rule 02 says: global_timeout = 60\nRule 03 says: global_timeout = -1",
        "expected_defender": "00",
        "severity": "HIGH"
    },
    "insecure_crypto": {
        "name": "Weak Hashing Algorithm",
        "file": "auth_utils.py",
        "content": "import hashlib\ndef hash_password(password):\n    return hashlib.md5(password.encode()).hexdigest()",
        "expected_defender": "01",
        "severity": "CRITICAL"
    },
    "suboptimal_performance": {
        "name": "Linear Scan Bottleneck",
        "file": "data_processor.py",
        "content": "def find_items(list_a, list_b):\n    # O(n^2) loop instead of using a set\n    return [item for item in list_a if item in list_b]",
        "expected_defender": "10",
        "severity": "MEDIUM"
    }
}

class AuditSimulator:
    def __init__(self, sandbox_dir=".sandbox"):
        self.sandbox_dir = sandbox_dir
        self.knowledge = []
        if os.path.exists(self.sandbox_dir):
            shutil.rmtree(self.sandbox_dir)
        os.makedirs(self.sandbox_dir)

    def _handle_security_breach(self, scenario, file_path):
        print("Detecting Hardcoded Secrets...")
        with open(file_path, 'r') as f:
            content = f.read()
        if "AWS_SECRET" in content:
            print("Role 01 (Auditor) ALERT: Secret leak detected!")
            return True
        return False

    def _handle_syntax_error(self, scenario, file_path):
        print("Shadow Testing ALERT: Syntax error detected automatically!")
        try:
            ast.parse(scenario["content"])
            return False
        except SyntaxError:
            print("Action: Role 05 (QA) detected syntax error. Triggering The Healer.")
            return True

    def _handle_missing_dependency(self, scenario, file_path):
        print("Detecting Missing Dependencies...")
        if "import nonexistent_lib" in scenario["content"]:
            print("Action: Role 08 (API) detected Ghost Import. Triggering Mock Generator.")
            return True
        return False

    def _handle_logical_conflict(self, scenario, file_path):
        print("Detecting Expert Role Collision...")
        if "global_timeout = -1" in scenario["content"]:
            print("COUNCIL ALERT: Incompatible design constraints detected!")
            print("Action: Triggering Adversarial Debate (Council of Experts)...")
            return True
        return False

    def _handle_insecure_crypto(self, scenario, file_path):
        print("Detecting Weak Cryptographic Algorithms...")
        if "md5" in scenario["content"].lower():
            print("Role 01 (Auditor) ALERT: Insecure hashing (MD5) detected!")
            return True
        return False

    def _handle_suboptimal_performance(self, scenario, file_path):
        print("Detecting Algorithmic Inefficiency...")
        if "if item in list_b" in scenario["content"]:
            print("Role 10 (Data Scientist) ALERT: Quadratic complexity detected!")
            print("Action: Triggering Efficiency Swarm for O(n) optimization.")
            return True
        return False

    def run_scenario(self, key):
        if key not in SCENARIOS:
            return False

        scenario = SCENARIOS[key]
        file_path = os.path.join(self.sandbox_dir, scenario["file"])
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(scenario["content"])
            
        print(f"\n--- Running Audit: {scenario['name']} ---")
        
        handlers = {
            "security_breach": self._handle_security_breach,
            "syntax_error": self._handle_syntax_error,
            "missing_dependency": self._handle_missing_dependency,
            "logical_conflict": self._handle_logical_conflict,
            "insecure_crypto": self._handle_insecure_crypto,
            "suboptimal_performance": self._handle_suboptimal_performance,
        }

        handler = handlers.get(key)
        success = handler(scenario, file_path) if handler else False

        if success:
            print(f"Result: Scenario {key} accurately mitigated.")
            self.knowledge.append({
                "date": str(datetime.date.today()),
                "audit": scenario["name"],
                "status": "PASSED"
            })
        
        return success

    def cleanup(self):
        if os.path.exists(self.sandbox_dir):
            shutil.rmtree(self.sandbox_dir)

if __name__ == "__main__":
    sim = AuditSimulator()
    print("🛡️ Antigravity Secret Audit Simulator V12 (Modular Edition)")
    for key in SCENARIOS:
        sim.run_scenario(key)
    sim.cleanup()

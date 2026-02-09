import os
import json
import sys
import subprocess
import datetime
from typing import List, Dict, Any, Optional

# --- CONFIGURATION ---
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(SKILL_ROOT, "resources")
STATE_FILE = os.path.join(RESOURCES_DIR, "project-state.json")

# --- ROLE DEFINITIONS (Source of Truth) ---
ALL_ROLES = {
    "00": {"name": "MANAGER", "desc": "Strategy, Resource Allocation", "tools": ["find-skills", "project-state"], "critical": True},
    "01": {"name": "AUDITOR", "desc": "Security, STRIDE, Vulnerability", "tools": ["agent-browser (CVEs)", "grep"], "triggers": ["security", "auth", "audit"]},
    "02": {"name": "ARCHITECT", "desc": "System Design, Specs", "tools": ["notebooklm-query", "uml-gen"], "triggers": ["design", "plan", "structure"]},
    "03": {"name": "DEVOPS", "desc": "Infra, CI/CD, Deployment", "tools": ["terminal", "docker-expert"], "triggers": ["docker", "k8s", "deploy", "ci/cd"]},
    "04": {"name": "DOCS", "desc": "Tech Documentation", "tools": ["git-history", "agent-browser"], "triggers": ["docs", "readme"]},
    "05": {"name": "QA", "desc": "Testing, Chaos Eng", "tools": ["playwright", "agent-browser"], "triggers": ["test", "verify", "qa"]},
    "06": {"name": "DB_EXPERT", "desc": "SQL, Schemas, Migrations", "tools": ["supabase-best-practices", "sql"], "triggers": ["sql", "database", "schema", "migration"]},
    "07": {"name": "UI_UX", "desc": "Design, CSS, Accessibility", "tools": ["figma-api", "css-validator"], "triggers": ["css", "ui", "design", "frontend"]},
    "08": {"name": "API_ENGINEER", "desc": "Backend, API Integration", "tools": ["curl", "json-validator"], "triggers": ["api", "json", "backend"]},
    "09": {"name": "MOBILE", "desc": "iOS, Android, Flutter", "tools": ["react-native", "flutter"], "triggers": ["ios", "android", "mobile"]},
    "10": {"name": "DATA_SCIENTIST", "desc": "Data Analysis, ML", "tools": ["pandas", "jupyter"], "triggers": ["data", "ml", "analysis"]}
}

class ResourceManager:
    @staticmethod
    def load_state() -> Dict[str, Any]:
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        return data
            except:
                pass
        return ResourceManager.create_default_state()

    @staticmethod
    def create_default_state():
        return {
            "project_name": "Unknown",
            "current_phase": "0_SOLICITATION",
            "active_role_id": "00",
            "last_updated": datetime.datetime.now().isoformat(),
            "completed_milestones": [],
            "pending_tasks": [],
            "critical_blockers": []
        }

    @staticmethod
    def save_state(state):
        state["last_updated"] = datetime.datetime.now().isoformat()
        with open(STATE_FILE, 'w') as f:
            json.dump(state, f, indent=2)

class KnowledgeManager:
    @staticmethod
    def load_knowledge() -> List[str]:
        kb_path = os.path.join(RESOURCES_DIR, "knowledge-base.md")
        if os.path.exists(kb_path):
            with open(kb_path, 'r', encoding='utf-8') as f:
                content = f.read()
                found_lines = [l.strip() for l in content.split('\n') if l.strip().startswith('*')]
                # Explicit list conversion to handle slice safety
                safe_list: List[str] = list(found_lines)
                if len(safe_list) > 5:
                    result_list: List[str] = []
                    start_idx = len(safe_list) - 5
                    for i in range(start_idx, len(safe_list)):
                        result_list.append(safe_list[i])
                    return result_list
                return safe_list
        return []

class ContextPruner:
    @staticmethod
    def analyze_files(root_dir):
        files_detected = []
        try:
            # Simple shallow scan
            root_files = os.listdir(root_dir)
            files_detected = root_files
        except:
            pass
        return files_detected

    @staticmethod
    def get_relevant_role_ids(files_detected, state):
        relevant_ids = {"00"} # Manager is always active
        
        # 1. State-based relevance
        phase = state.get("current_phase", "")
        if "SOLICITATION" in phase or "SPEC" in phase:
            relevant_ids.add("02") # ARCHITECT
        if "AUDIT" in phase:
            relevant_ids.add("01") # AUDITOR
            
        # 2. File-based relevance (Heuristics)
        file_str = " ".join(files_detected).lower()
        
        # Mappings
        file_triggers = {
            "docker": "03", "k8s": "03", "terraform": "03",
            "test": "05", "spec": "05", "cypress": "05",
            "sql": "06", "schema": "06", "migration": "06",
            "css": "07", "html": "07", "tsx": "07",
            "api": "08", "json": "08", 
            "ios": "09", "android": "09", "flutter": "09",
            "csv": "10", "pandas": "10", "ipynb": "10"
        }
        
        for key, role_id in file_triggers.items():
            if key in file_str:
                relevant_ids.add(role_id)
                
        # If no specific tech context, default to Architect and Docs
        if len(relevant_ids) <= 1:
            relevant_ids.add("02")
            relevant_ids.add("04")
            
        return list(relevant_ids)

    @staticmethod
    def generate_context_block(root_dir):
        state = ResourceManager.load_state()
        files = ContextPruner.analyze_files(root_dir)
        relevant_ids = ContextPruner.get_relevant_role_ids(files, state)
        lessons = KnowledgeManager.load_knowledge()
        
        valid_roles_table = []
        for rid in sorted(relevant_ids):
            role = ALL_ROLES[rid]
            # Ensure tools is a list of strings before joining
            tools = role.get('tools', [])
            if isinstance(tools, list):
                tools_str = ', '.join([str(t) for t in tools])
            else:
                tools_str = str(tools)
                
            valid_roles_table.append(f"| **{rid}** | **{role['name']}** | {role['desc']} | `{tools_str}` |")
            
        # Ensure detected files is a list and slice safely
        detected_list: List[str] = list(files) if files else []
        final_files: List[str] = []
        for i in range(min(10, len(detected_list))):
            final_files.append(detected_list[i])
        
        report: Dict[str, Any] = {
            "PROJECT_STATE": state,
            "DETECTED_FILES": final_files, # Limit output
            "RELEVANT_ROLES": sorted(relevant_ids),
            "LESSONS_LEARNED": lessons,
            "CONTEXT_BLOCK": "\n".join([
                "### 🧠 DYNAMIC CONTEXT (Real-Time)",
                f"**Phase**: {state['current_phase']}",
                f"**Health Status**: {state.get('health_status', 'Unknown')}",
                f"**Active Roles**: {', '.join(sorted(relevant_ids))}",
                "",
                "#### 📚 KNOWLEDGE BASE (Last 5 Lessons)"] + 
                ([f"> {l}" for l in lessons] if lessons else ["> No recorded lessons yet."]) +
                [
                "",
                "#### 🛡️ AVAILABLE EXPERT SQUAD (Pruned)",
                "| ID | Role | Mission | Tools |",
                "| :--- | :--- | :--- | :--- |"
            ] + valid_roles_table)
        }
        return report

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    # Mode switch could be added here (e.g., --update-state)
    
    report = ContextPruner.generate_context_block(target_dir)
    
    # Level 9: Check for evolutionary updates
    try:
        if len(report.get("LESSONS_LEARNED", [])) > 0:
            evolver_path = os.path.join(os.path.dirname(__file__), "evolver.py")
            subprocess.Popen([sys.executable, evolver_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

    # Level 11: Trigger Refactor Patrol in background
    try:
        patrol_path = os.path.join(os.path.dirname(__file__), "refactor_patrol.py")
        subprocess.Popen([sys.executable, patrol_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # If report exists, inject into context
        report_file = os.path.join(RESOURCES_DIR, "refactor_report.json")
        if os.path.exists(report_file):
            with open(report_file, 'r', encoding='utf-8') as f:
                refactors_data = json.load(f)
                if isinstance(refactors_data, list) and len(refactors_data) > 0:
                    # Explicit list conversion and safe limit
                    ref_list: List[Dict[str, Any]] = [r for r in refactors_data if isinstance(r, dict)]
                    top_refactors: List[Dict[str, Any]] = []
                    for i in range(min(3, len(ref_list))):
                        top_refactors.append(ref_list[i])
                    report["REFACTOR_PROPOSALS"] = top_refactors
                    
                    context_update_lines = ["\n\n#### 🏗️ ARCHITECTURAL DECAY (Refactor Swarm Proposals)"]
                    for r in top_refactors:
                        if isinstance(r, dict):
                            r_type = str(r.get('type', 'Unknown'))
                            r_file = str(r.get('file', 'Unknown'))
                            r_msg = str(r.get('msg', ''))
                            context_update_lines.append(f"> * **[{r_type}]** {r_file} -> {r_msg}")
                    
                    # Safe string update
                    current_ctx = str(report.get("CONTEXT_BLOCK", ""))
                    report["CONTEXT_BLOCK"] = current_ctx + "\n".join(context_update_lines) + "\n"
    except:
        pass
        
    print(json.dumps(report, indent=2))

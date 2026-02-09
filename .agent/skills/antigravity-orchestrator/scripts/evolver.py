import os
import re
import datetime

# Paths
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(SKILL_ROOT, "resources")
KNOWLEDGE_BASE = os.path.join(RESOURCES_DIR, "knowledge-base.md")
RULES_FILE = os.path.join(SKILL_ROOT, "rules.md")

def analyze_lessons():
    if not os.path.exists(KNOWLEDGE_BASE):
        return []
    
    with open(KNOWLEDGE_BASE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple pattern matching for lessons
    lessons = re.findall(r"\*   \[.*?\] \*\*(.*?)\*\*: (.*)", content)
    return lessons

def synthesize_rule(title, lesson):
    # Basic logic to convert a lesson into a rule format
    timestamp = datetime.date.today().isoformat()
    return f"### [EVOLVED {timestamp}] {title}\n*   **Derived Strategy**: {lesson}\n*   **Status**: Active (Self-Optimized)\n"

def update_rules():
    lessons = analyze_lessons()
    if not lessons:
        print("No lessons found to evolve.")
        return False
    
    with open(RULES_FILE, 'r', encoding='utf-8') as f:
        rules_content = f.read()
    
    # Check for Evolutionary section or create it
    if "## 🧬 Evolutionary Rules (Self-Optimized)" not in rules_content:
        rules_content += "\n\n## 🧬 Evolutionary Rules (Self-Optimized)\n\n"
    
    # Extract existing evolved rule titles to avoid duplicates
    existing_titles = re.findall(r"### \[EVOLVED .*?\] (.*)", rules_content)
    
    new_rules = []
    for title, lesson in lessons:
        if title not in existing_titles:
            print(f"Evolving new rule: {title}")
            new_rules.append(synthesize_rule(title, lesson))
    
    if new_rules:
        updated_content = rules_content + "\n".join(new_rules)
        with open(RULES_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    
    print("No new evolutionary updates required.")
    return False

if __name__ == "__main__":
    print("Running Antigravity Evolutionary Logic Engine...")
    if update_rules():
        print("Evolution Cycle: SUCCESS. rules.md updated.")
    else:
        print("Evolution Cycle: IDLE. No new patterns detected.")

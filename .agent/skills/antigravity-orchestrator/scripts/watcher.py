import os
import sys
import time
import json
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Paths
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCES_DIR = os.path.join(SKILL_ROOT, "resources")
STATE_FILE = os.path.join(RESOURCES_DIR, "project-state.json")

class ShadowTester(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        
        filename = os.path.basename(event.src_path)
        
        # Avoid infinite loops by ignoring the state file itself
        if filename == "project-state.json" or ".git" in event.src_path:
            return
        
        print(f"Shadow Testing triggered by: {filename}")
        self.run_checks(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {os.path.basename(event.src_path)}")
            # Clear status if it was related to this file
            self.update_health("Healthy")

    def run_checks(self, file_path):
        # 1. Basic Syntax Check (Python)
        if file_path.endswith(".py"):
            try:
                subprocess.check_output([sys.executable, "-m", "py_compile", file_path], stderr=subprocess.STDOUT)
                self.update_health("Healthy")
            except subprocess.CalledProcessError as e:
                self.update_health(f"Degraded: Syntax Error in {os.path.basename(file_path)}")
                print(f"Alert: {e.output.decode()}")

    def update_health(self, status):
        if not os.path.exists(STATE_FILE):
            return
            
        try:
            with open(STATE_FILE, 'r') as f:
                state = json.load(f)
            
            if state.get("health_status") != status:
                state["health_status"] = status
                with open(STATE_FILE, 'w') as f:
                    json.dump(state, f, indent=2)
                print(f"Health Status Updated: {status}")
        except Exception as e:
            print(f"Error updating health: {e}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    event_handler = ShadowTester()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    print(f"Antigravity Shadow Testing active on: {os.path.abspath(path)}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

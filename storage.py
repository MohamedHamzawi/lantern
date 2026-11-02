import json
import os
TASKS_FILE = "tasks.json"
def load():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE) as f:
        return json.load(f)
def save(tasks):
    with open(TASKS_FILE,"w") as f:
        json.dump(tasks, f)
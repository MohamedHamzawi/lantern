import json
import os
def load():
    if not os.path.exists("tasks.json"):
        return []
    with open("tasks.json") as f:
        return json.load(f)
def save(tasks):
    with open("tasks.json","w") as f:
        json.dump(tasks, f)
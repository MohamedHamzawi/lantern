import csv
import sys


def export_csv(tasks, out=sys.stdout):
    writer = csv.DictWriter(out, fieldnames=["title", "done"])
    writer.writeheader()

    for task in tasks:
        writer.writerow({
            "title": task["title"],
            "done": task.get("done", False)
        })
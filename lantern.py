# in-memory
import argparse
from tasks import add_task, list_tasks

def print_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(f"- {task['title']}")

def main():
    parser = argparse.ArgumentParser(prog="lantern", description="Tiny task tracker")
    sub = parser.add_subparsers(dest="command", required=True)
    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")
    list_parser = sub.add_parser("list")
    args = parser.parse_args()
    if args.command == "add":
        task = add_task(args.title)
        print(f"Added: {task['title']}")
    elif args.command == "list":
        tasks = list_tasks()
        print_tasks(tasks)

if __name__ == "__main__":
    main()
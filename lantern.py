# in-memory
import argparse
from tasks import add_task, list_tasks

def print_tasks(tasks):
    for task in tasks:
        print(f"- {task['title']}")

def main():
    parser = argparse.ArgumentParser(prog="lantern", description="Tiny task tracker")
    sub = parser.add_subparsers(dest="command", required=True)
    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")
    list_parser = sub.add_parser("list")
    list_parser.add_argument("--sort", action="store_true", help="sort tasks alphabetically by title")
    args = parser.parse_args()
    if args.command == "add":
        task = add_task(args.title)
        print(f"Added: {task['title']}")
    elif args.command == "list":
        tasks = list_tasks()
        if args.sort:
            tasks = sorted(tasks,key = lambda t:t["title"])
        print_tasks(tasks)

if __name__ == "__main__":
    main()
# in-memory
import argparse
from tasks import add_task, list_tasks
from export import export_csv


def print_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(f"- {task['title']}")


def main():
    parser = argparse.ArgumentParser(
        prog="lantern",
        description="Tiny task tracker"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    add_parser = sub.add_parser("add")
    add_parser.add_argument("title")

    list_parser = sub.add_parser("list")
    list_parser.add_argument(
        "--done",
        action="store_true",
        help="show only completed tasks"
    )

    export_parser = sub.add_parser("export")
    export_parser.add_argument(
        "--csv",
        action="store_true",
        help="print tasks as CSV"
    )

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print(f"Added: {task['title']}")

    elif args.command == "list":
        tasks = list_tasks()
        if args.done:
            tasks = [t for t in tasks if t.get("done")]
        print_tasks(tasks)

    elif args.command == "export":
        if args.csv:
            export_csv(list_tasks())


if __name__ == "__main__":
    main()
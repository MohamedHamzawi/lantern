_TASKS = []
def add_task(title):
    task = {"title": title.strip(), "done": False}
    _TASKS.append(task)
    return task
def list_tasks():
    return list(_TASKS)
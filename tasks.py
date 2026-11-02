_TASKS = []
def add_task(title):
    task = {"title": title}
    _TASKS.append(task)
    return task
def list_tasks():
    return list(_TASKS)
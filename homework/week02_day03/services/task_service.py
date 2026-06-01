tasks = [
    {"id":1,"title":"学习 HTTP","status":"done"},
    {"id":2,"title":"学习 FastAPI","status":"todo"},
    {"id":3,"title":"学习参数","status":"doing"}
]

def get_all_tasks():
    return tasks

def get_task_by_id(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def search_tasks_by_keyword(keyword:str):
    result = []
    for task in tasks:
        if keyword in task["title"]:
            result.append(task)
    return result
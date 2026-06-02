tasks = [
    {"id":1,"title":"学习 HTTP","status":"done","difficulty":2},
    {"id":2,"title":"学习 FastAPI","status":"todo","difficulty":3},
    {"id":3,"title":"学习参数","status":"doing","difficulty":1}
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

def create_task(title:str,status:str,difficulty:int):
    new_id = len(tasks) + 1
    new_task = {
        "id":new_id,
        "title":title,
        "status":status,
        "difficulty":difficulty
    }
    tasks.append(new_task)
    return new_task

def update_task(task_id:int,title:str|None , status:str|None,difficulty:int|None):
    for task in tasks:
        if task["id"] == task_id:
            if title is not None:
                task["title"] = title
            if status is not None:
                task["status"] = status
            if difficulty is not None:
                task["difficulty"] = difficulty
            return task
    return None
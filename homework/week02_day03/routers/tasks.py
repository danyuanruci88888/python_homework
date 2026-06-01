from fastapi import APIRouter
from services.task_service import get_all_tasks,get_task_by_id,search_tasks_by_keyword

router = APIRouter(prefix = "/tasks",tags = ["任务"])

@router.get("")
def list_tasks(status:str|None = None,keyword:str|None = None):
    all_tasks = get_all_tasks()
    if keyword is not  None:
        return {"data":search_tasks_by_keyword(keyword)}
    if status is not None :
        result = []
        for task in all_tasks:
            if task["status"] == status:
                return {"data":result}
    return {"data":all_tasks}

@router.get("/{task_id}")
def get_task(task_id:int):
    task = get_task_by_id(task_id)
    if task is None:
        return {"message":"任务不存在"}
    return {"data":task}
from asyncio import Task

from fastapi import APIRouter
from  services.task_service import (
    get_all_tasks,
    get_task_by_id,
    search_tasks_by_keyword ,
    create_task,
    update_task
)
from schemas.task import TaskCreate,TaskUpdate

router = APIRouter(prefix = "/tasks",tags = ["任务"])

@router.get("")
def list_tasks(status:str|None = None,keyword:str|None = None):
    all_tasks = get_all_tasks()

    if keyword is not None:
        return {"data":search_tasks_by_keyword(keyword)}

    if status is not None:
        result = []
        for task in all_tasks:
            if task["status"] == status:
                result.append(task)
        return {"data":result}

    return {"data":all_tasks}

@router.get("/{task_id}")
def get_task(task_id:int):
    task = get_task_by_id(task_id)
    if task is None:
        return{"message":"任务不存在"}
    return {"data":task}

@router.post("")
def create_new_task(task_create:TaskCreate):
    task = create_task(
        title = task_create.title,
        status = task_create.status,
        difficulty = task_create.difficulty
    )
    return {"message":"创建成功","data":task}

@router.put("/{task_id}")
def update_existing_task(task_id:int,task_update:TaskUpdate):
    task = update_task(
        task_id = task_id,
        title = task_update.title,
        status = task_update.status,
        difficulty = task_update.difficulty
    )
    if task is None:
        return {"message":"任务不存在"}
    return {"message":"修改成功","data":task}
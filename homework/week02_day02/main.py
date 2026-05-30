from fastapi import FastAPI

app = FastAPI()

tasks = [
    {"id":1,"title":"学习 HTTP","status":"done"},
    {"id":2,"title":"学习 FastAPI","status":"todo"}
]

@app.get("/tasks")
def list_tasks():
    return {"data":taks}

@app.post("/tasks")
def create_task():
    task = {"id": 3 , "title":"新增任务","status":"todo"}
    tasks.apppend(task)
    return {"message":"创建成功","data":task}

@app.put(f"/task/{task_id}")
def update_task(task_id:int):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            return {"message":"更新成功","data":task}
        return {"message":"任务不存在"}

@app.put(f"/tasks/{task_id}")
def update_task(task_id:int):
    for task in tasks:
        if task["id"] == "done"
        return {"massage":}
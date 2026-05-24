import json

def load_tasks():
    try:
        with open("tasks.json","r",encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json","w",encoding="utf-8") as f :
        json.dump(tasks,f,ensure_ascii=False,indent=2)

def add_task(tasks,title):
    task={
        "title":title,
        "status":"todo"
    }
    tasks.append(task)

def show_tasks(tasks):
    for task in tasks:
        print(task["title"],task["status"])
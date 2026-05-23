# import json

# def load_tasks():
#     try:
#         with open("tasks.json","r",encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

# def save_tasks(tasks):
#     with open("tasks.json","w",encoding="utf-8") as f:
#         json.dump(tasks,f,ensure_ascii=False,indent=2)

# def add_task(task,title):
#     task={
#         "title":title,
#         "status":"todo"
#     }
#     tasks.append(task)

# def show_tasks(tasks):
#     for task in tasks:
#         print(task["title"],task["status"])

# tasks = load_tasks()
# add_task(tasks,"学习 JSON 文件保存")
# save_tasks(tasks)
# print("保存成功")

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

tasks = load_tasks()
add_task(tasks,"学习JSON文件保存")
save_tasks(tasks)
print("保存成功")

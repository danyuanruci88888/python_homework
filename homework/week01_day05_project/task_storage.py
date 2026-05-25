# import json


# def load_tasks():
#     try:
#         with open("tasks.json", "r", encoding="utf-8") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []


# def save_tasks(tasks):
#     with open("tasks.json", "w", encoding="utf-8") as f:
#         json.dump(tasks, f, ensure_ascii=False, indent=2)


# def show_tasks(tasks):
#     if len(tasks) == 0:
#         print("暂无任务")
#         return
#     for index, task in enumerate(tasks, start=1):
#         print(index, task["title"], "-", task["status"])


# def add_task(tasks):
#     title = input("请输入任务名称：")
#     task = {
#         "title": title,
#         "status": "todo"
#     }
#     tasks.append(task)
#     save_tasks(tasks)
#     print("任务已添加")


# def complete_task(tasks):
#     show_tasks(tasks)
#     if len(tasks) == 0:
#         return
#     try:
#         num = int(input("请输入要完成的任务编号："))
#         if num < 1 or num > len(tasks):
#             print("编号不存在，请重新输入")
#             return
#         tasks[num - 1]["status"] = "done"
#         save_tasks(tasks)
#         print("任务已完成")
#     except ValueError:
#         print("请输入数字")


# def show_menu():
#     print("====================")
#     print("1. 查看任务")
#     print("2. 新增任务")
#     print("3. 完成任务")
#     print("0. 退出")
#     print("====================")

import json

def load_tasks():
    try:
        with open("task.json","r","encoding = utf_8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_task(tasks):
    with open("task.json","w","utf-8") as f :
        json.dump(task,f,ensure_ascii=False,indent=2)

def show_tasks(tasks):
    if len(tasks) == 0:
        print("暂无任务")
    else :
        print("任务列表:")
        for index,task in enumerate(tasks,start = 1):
            print (f"{index},{task['title']},{task['status']}")

def add_task(tasks):
    title = input("请输入任务名称:")
    task={
        "title":title,
        "status":"todo"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("任务已添加")

def complete_tasks(tasks):
    show_tasks(tasks)
    if len(tasks) == 0:
        return
    try:
        num = int(input("请输入要完成的任务编号:"))
        if num < 1 or num>len(tasks):
            print("编号不存在,请重新输入")
            return
        tasks[num - 1]["status"] = "done"
        save_task(tasks)
        print("任务已完成")
    except ValueError:
        print("请输入数字")

def show_menu():
    print("=============")
        print("1. 查看任务")
        print("2. 新增任务")
        print("3. 完成任务")
        print("0. 退出")

    print("================")


tasks = [
    {"title":"学习判断","status":"todo","difficulty":1},
    {"title":"学习循环","status":"done","difficulty":2},  
    {"title":"学习列表和字典","status":"doing","difficulty":3},
    {"title":"学习数据类型","status":"todo","difficulty":1},
    {"title":"学习函数","status":"done","difficulty":2},
    {"title":"复习整理","status":"todo","difficulty":3}
]

for task in tasks:
    if task["status"] != "done" :
        print(task["title"],"未完成任务")

for task in tasks:
    if task["difficulty"] >= 3:
        print(task["title"],"难度较高")

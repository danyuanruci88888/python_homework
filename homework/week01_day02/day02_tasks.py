tasks = [
    {"title":"学习变量","status":"done"},
    {"title":"学习判断","status":"todo"},
    {"title":"学习循环","status":"todo"},
    {"title":"学习列表和字典","status":"doing"},
    {"title":"学习数据类型","status":"todo"},
    {"title":"学习函数","status":"done"},
]
for task in tasks:
    if task["status"]=="done":
            print(task["title"],"已经完成") 
    elif task["status"]=="doing":
            print(task["title"],"正在进行") 
    else :
            print(task["title"],"还没开始") 

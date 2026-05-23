# Day02 任务筛选器

## 项目说明

本项目包含两个 Python 脚本，用于练习 Python 的判断、循环、列表和字典基础知识。

## 文件说明

- `day02_tasks.py` — 任务列表练习，使用循环打印任务状态
- `task_filter.py` — 任务筛选器，筛选未完成任务和高难度任务

## 作业怎么运行

在终端进入项目目录后，分别运行以下命令：

python day02_tasks.py
python task_filter.py

## 今天学了什么

### if 是用来做什么的

if 用来让程序做条件判断。当某个条件成立时，执行对应的代码块；
条件不成立时，跳过或执行 else / elif 里的代码。
多个条件可以用 elif 连接，只有前面的条件不满足时才会继续往下判断。

if task["status"] == "done":
    print("已完成")
elif task["status"] == "doing":
    print("进行中")
else:
    print("未开始")

### for 适合什么场景

for 循环适合遍历一组已知数据，比如列表里有多少个元素，
就自动循环多少次，不需要手动控制次数。

for task in tasks:
    print(task["title"])

### 列表和字典分别适合保存什么

列表适合保存"一组同类型的数据"，比如多个任务、多个名字。
用方括号 [] 表示，通过数字索引（0、1、2）来取出元素。

字典适合描述"一个事物的多个属性"，比如一个任务的标题、状态、难度。
用花括号 {} 表示，通过键名（"title"、"status"）来取出对应的值。

实际项目中最常见的是列表里套字典：

tasks = [
    {"title": "学习变量", "status": "done", "difficulty": 1},
    {"title": "学习判断", "status": "todo", "difficulty": 2},
]

## 遇到了什么问题

-问题一：
    ​for 循环那行出现 IndentationError，报缩进错误。
    
-问题二：​
    用 tasks["status"] 访问列表时报 TypeError，
    提示 list indices must be integers or slices, not str。

-问题三：​
    difficulty 的比较值加了引号写成 "3"，
    导致报错 '>=' not supported between instances of 'int' and 'str'。

## 是怎么解决的

-问题一：​ 
    for 是顶层代码，前面不能有缩进，把多余的空格删掉后解决。

-问题二：​
    tasks 是列表，不能直接用字符串键访问。
    需要先用 for task in tasks 把每个字典取出来，
    再用 task["status"] 访问字典里的值。

-问题三：​
    difficulty 存的是数字类型，比较时也要用数字 3，
    不能加引号写成字符串 "3"，去掉引号后解决。

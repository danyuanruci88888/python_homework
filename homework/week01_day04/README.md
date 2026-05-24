# Day04 模块拆分与虚拟环境

## 项目说明

本项目将昨天的任务保存器拆分成两个文件，
task_utils.py 负责存放函数，main.py 负责调用函数。
同时完成了虚拟环境创建、依赖安装和 requirements.txt 生成。

## 文件说明

- `main.py` — 程序入口，调用 task_utils.py 里的函数
- `task_utils.py` — 存放四个函数：load_tasks、save_tasks、add_task、show_tasks
- `tasks.json` — 本地任务数据文件，由程序自动生成
- `requirements.txt` — 项目依赖清单

## 如何创建虚拟环境

在项目根目录的终端里运行：

python -m venv .venv

## 如何安装依赖

1.先激活虚拟环境：
    Git Bash
    source .venv/Scripts/activate

    Windows CMD
    .venv\Scripts\activate

2.激活后安装依赖：
    pip install -r requirements.txt

## 如何运行项目

确保虚拟环境已激活，然后运行：

python main.py

每运行一次，tasks.json 里会新增一条任务记录。

## 为什么不提交 .venv

.venv 文件夹体积很大，而且每台电脑的环境路径不同，
直接提交没有意义。别人拿到项目后用 requirements.txt
重新安装依赖即可，不需要你的 .venv。

## 今天学到了什么

- 模块就是一个 .py 文件，可以用 import 导入其他文件里的函数
- 拆分文件让代码结构更清晰，每个文件只负责一件事
- pip 是 Python 的包管理工具，相当于应用商店
- 虚拟环境给每个项目一个独立的依赖空间，互不干扰
- requirements.txt 是项目的依赖清单，方便别人复现环境

## 遇到的问题

Git Bash 终端里路径分隔符必须用 /，不能用 \，
否则 cd 命令会报 No such file or directory 错误。

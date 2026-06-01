# Week02 Day03 - FastAPI 项目结构、路径参数和查询参数

## 项目简介

本项目是 Python 后端学习阶段的第三天作业。完成了一个基于 FastAPI 的任务管理接口，采用分层项目结构，支持路径参数和查询参数两种方式访问任务数据。

---

## 项目结构

week02_day03/
├── main.py                  # 应用入口，创建 app 并挂载路由
├── routers/
│   └── tasks.py             # 路由层，定义接口地址
├── services/
│   └── task_service.py      # 服务层，处理业务逻辑
├── requirements.txt         # 项目依赖
├── README.md                # 项目说明文档
└── 测试截图/                 # 接口测试截图

---

## 环境准备与运行方式

第一步：进入项目目录

    cd week02_day03

第二步：激活虚拟环境

    Windows：
    .venv\Scripts\activate

    Mac / Linux：
    source .venv/bin/activate

第三步：安装依赖

    pip install -r requirements.txt

第四步：启动服务

    uvicorn main:app --reload

第五步：打开接口文档

浏览器访问 http://127.0.0.1:8000/docs，可以在 Swagger 页面上直接测试所有接口。

---

## 支持的接口

| 方法 | 路径                        | 说明                   |
|------|-----------------------------|------------------------|
| GET  | /tasks                      | 返回全部任务           |
| GET  | /tasks/{task_id}            | 按 id 查询某一条任务   |
| GET  | /tasks?status=todo          | 按状态筛选任务         |
| GET  | /tasks?keyword=FastAPI      | 按关键词搜索任务标题   |

---

## 为什么要拆文件

把所有代码堆在一个文件里，项目一大就难以维护，改一处可能牵连多处。拆分之后每个文件只负责一件事：

- main.py 只做组装，不写业务逻辑
- routers/tasks.py 只定义接口地址，不处理数据
- services/task_service.py 只写数据查询逻辑，不关心外部请求

这样改接口只改 router，改逻辑只改 service，职责清晰，互不干扰。

---

## 路径参数和查询参数的区别

路径参数把要查询的内容直接写进 URL 地址里，适合精确定位某一条数据：

    GET /tasks/1        查询 id 为 1 的任务

查询参数写在问号后面，适合筛选、搜索、分页：

    GET /tasks?status=todo       筛选所有待办任务
    GET /tasks?keyword=FastAPI   搜索标题含 FastAPI 的任务

---

## 实现了哪些筛选能力

- 支持不传任何参数，返回全部任务
- 支持传入 status 参数，按任务状态筛选（done / todo / doing）
- 支持传入 keyword 参数，按任务标题关键词搜索
- 支持传入 task_id 路径参数，精确查询某一条任务

---

## 今天学了什么

- FastAPI 推荐的三层项目结构（main / routers / services）
- APIRouter 的作用：把相关接口打包，统一挂载到 app
- 路径参数的写法：/{task_id}，FastAPI 自动提取并传入函数
- 查询参数的写法：函数参数加默认值 = None，FastAPI 自动识别
- include_router 的作用：把路由模块注册进主应用
- Python in 运算符可以判断字符串是否包含某个关键词

---

## 遇到的问题与解决过程

问题一：Attribute "app" not found in module "main"

routers.tasks 拼成了 routers.task（少了 s），import 失败导致 app 没有被创建。
解决方法：对照文件名改正拼写，改为 from routers.tasks import router as task_router。

问题二：SyntaxError: invalid syntax

from 拼成了 form，Python 不认识这个关键字，直接报语法错误。
解决方法：仔细检查关键字拼写，改回 from。

问题三：ImportError: cannot import name 'get_all_tasks'

task_service.py 里的函数没有写完整，router 层找不到对应函数。
解决方法：补全三个函数：get_all_tasks、get_task_by_id、search_tasks_by_keyword。

问题四：SyntaxError: cannot assign to subscript

条件判断里把 == 写成了 =，= 是赋值，== 才是比较判断。
解决方法：把 if task["status"] = status 改成 if task["status"] == status。

问题五：return result 缩进错误

return result 缩进层级太深，跑进了 if 块里，只找到第一条就返回了。
解决方法：把 return result 和 for 对齐，让循环全部跑完再统一返回。


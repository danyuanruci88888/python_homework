# Week02 Day04 - 请求体、Pydantic 和 Swagger

## 项目简介

本项目在上一天拆分项目结构的基础上，新增了请求体处理能力，使用 Pydantic 定义数据模型，支持新增和修改任务，并通过 Swagger页面进行接口测试。

---

## 项目结构

week02_day04/
├── main.py                  # 应用入口，创建 app 并挂载路由
├── routers/
│   └── tasks.py             # 路由层，定义所有接口
├── services/
│   └── task_service.py      # 服务层，处理数据逻辑
├── schemas/
│   └── task.py              # 数据模型层，定义请求体格式和校验规则
├── requirements.txt         # 项目依赖
├── README.md                # 项目说明文档
└── Swagger测试截图/          # 接口测试截图

---

## 环境准备与运行方式

第一步：进入项目目录

    cd week02_day04

第二步：激活虚拟环境

    Windows PowerShell：
    .venv\Scripts\activate

第三步：安装依赖

    pip install -r requirements.txt

第四步：启动服务

    uvicorn main:app --reload

第五步：打开接口文档

浏览器访问 http://127.0.0.1:8000/docs，在 Swagger 页面上可以直接测试所有接口。

---

## 支持的接口

| 方法   | 路径                   | 说明                   |
|--------|------------------------|------------------------|
| GET    | /tasks                 | 返回全部任务           |
| GET    | /tasks?status=todo     | 按状态筛选任务         |
| GET    | /tasks?keyword=FastAPI | 按关键词搜索任务标题   |
| GET    | /tasks/{task_id}       | 按 id 查询某一条任务   |
| POST   | /tasks                 | 新建任务               |
| PUT    | /tasks/{task_id}       | 修改某一条任务         |

---

## 请求体是什么

GET 请求的数据通过 URL 传递，但新增或修改任务时需要传递更多字段，
不适合放在 URL 里。这时候把数据打包成 JSON 格式，随请求一起发给后端，
这包数据就叫请求体。

比如新建一条任务，发给后端的请求体长这样：

    {"title": "学习 Pydantic", "status": "todo", "difficulty": 3}

---

## Pydantic 起什么作用

Pydantic 是用来定义请求体数据格式和校验规则的工具。
后端收到用户发来的数据之后，先用 Pydantic 模型做一次自动检查：
字段有没有填、类型对不对、值是否在允许范围内。
检查通过才进入业务逻辑，不通过直接返回错误信息，不需要手动写 if 判断。

本项目定义了两个模型：

TaskCreate 用于新建任务，规则较严格，title 为必填项。
TaskUpdate 用于修改任务，所有字段均为可选，只传需要修改的字段即可。

---

## 设置了哪些字段校验

| 字段       | 规则                                      |
|------------|-------------------------------------------|
| title      | 必填（TaskCreate），长度 1~50 个字符      |
| status     | 只能是 todo、doing、done 之一             |
| difficulty | 整数，范围 1~5，默认值为 1               |

故意传入不合法数据（如 title 为空、status 填 abc）时，
后端会返回 422 状态码和具体的校验错误信息。

---

## 今天学了什么

- 请求体的概念：POST 和 PUT 通过请求体传递数据，而不是 URL
- Pydantic BaseModel 的用法：class 定义数据结构和校验规则
- Field 的用法：min_length、max_length、ge、le 等参数
- Literal 的用法：限制字段只能是几个固定值之一
- str | None 的写法：表示字段可选，不传时为 None


---

## 遇到的问题与解决过程

问题一：PowerShell 无法激活虚拟环境

报错 无法加载模块".venv"，原因是 PowerShell 默认禁止运行脚本。
解决方法：执行 Set-ExecutionPolicy RemoteSigned -Scope CurrentUser 解除限制。

问题二：week02_day04 没有虚拟环境

之前的 .venv 是在 week02_day03 里创建的，新文件夹需要重新创建。
解决方法：在 week02_day04 目录下执行 python -m venv .venv 重新创建。

问题三：ImportError，找不到 TaskCreate

原因是 schemas/task.py 文件修改后没有按 Ctrl+S 保存，
uvicorn 读取的还是旧版本的文件内容。
解决方法：保存文件后服务自动热更新，问题消失。

问题四：三个文件内容混在了一起

在编辑时不小心把 main.py、tasks.py、task_service.py 的内容写进了同一个文件。
解决方法：逐一打开每个文件，清空内容后重新粘贴对应的正确代码。

问题五：多处拼写错误导致启动失败

包括 sppend（应为 append）、TaskUpdata（应为 TaskUpdate）、
@router.put 用在了查询接口上（应为 @router.get）等。
解决方法：逐行对照检查，修正拼写和装饰器类型。

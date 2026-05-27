# Week02 Day01 — 第一个 FastAPI 接口

## 今天学了什么

今天从 Python 脚本正式进入后端开发，核心是理解 HTTP 协议和用 FastAPI 写接口。

**HTTP 和 FastAPI 的关系：​**
HTTP 是一套规则，规定了请求和响应应该长什么样。
FastAPI 是帮你遵守这套规则的框架，它把底层的 HTTP 细节都封装好了，
你只需要写业务逻辑，它自动处理好所有通信格式。

**今天学到的核心概念：​**
- HTTP 请求包含：请求方法、请求地址、请求参数、请求体
- HTTP 响应包含：状态码（200成功/404找不到）、返回数据、错误信息
- 装饰器：`@app.get("/")` 是贴在函数上的标签，告诉 FastAPI 这个函数是一个接口
- Uvicorn：负责把 FastAPI 代码真正跑起来对外开放的服务器程序
- Swagger：FastAPI 自动生成的接口测试页面，不需要写前端就能测试接口
- `127.0.0.1:8000`：本机地址 + 端口号，代表"我自己这台电脑上的 8000 号服务"

## 如何安装依赖

进入项目文件夹，创建并激活虚拟环境：

    python -m venv .venv
    .venv\Scripts\activate

安装依赖（终端前面出现 (.venv) 说明激活成功）：

    pip install -r requirements.txt

## 如何启动服务

确保虚拟环境已激活，运行：

    uvicorn main:app --reload

看到以下提示说明启动成功：

    INFO: Uvicorn running on http://127.0.0.1:8000

注意：终端要保持开着，关掉终端服务就停了。
`--reload` 的作用是：修改代码保存后，服务自动重启，不需要手动重新运行命令。

## 三个接口分别做什么

| 接口地址     | 方法  | 说明                | 返回示例                                                      |
| /           | GET  | 首页，验证服务正常运行 | {"message": "Hello FastAPI"}                                 |
| /health     | GET  | 健康检查，确认服务存活 | {"status": "ok"}                                             |
| /profile    | GET  | 返回个人学习信息      | {"name": "张三", "target": "AI应用开发工程师", "week": 2}       |

## Swagger 地址

服务启动后访问：

    http://127.0.0.1:8000/docs

Swagger 是 FastAPI 自动生成的接口文档页面，可以直接在网页上点击测试每个接口，
看到请求参数和返回结果，不需要写任何前端代码。

## 我遇到了什么问题

1. `cd week02_day01` 报错路径不存在——文件夹还没创建，需要先 `mkdir week02_day01`
2. 进错了目录层级，`week02_day01` 在 `homework` 子文件夹里，
   需要 `cd homework\week02_day01`
3. 代码误写进了 `.venv` 里面的 `main.py`，
   `.venv` 是虚拟环境的内部文件夹，不能在里面写业务代码
4. `@app.get("/")` 和 `def read_root():` 写在同一行，
   装饰器必须单独占一行，紧接着下一行才写 `def`
5. `app = FastAPI()` 前面多了空格，报 `IndentationError`——
   顶层代码必须顶格写，不能有任何缩进
6. 接口地址拼成了 `/healthy`，访问 `/health` 时返回 404
7. 改完代码忘记按 `Ctrl+S` 保存，`--reload` 检测不到变化，服务没有重启
8. 用 `python main.py` 运行项目，报 `ModuleNotFoundError`——
   FastAPI 项目必须用 `uvicorn main:app --reload` 启动，不能直接用 python 执行

## 我是怎么解决的

每次报错先看终端提示的错误类型和行号，找到对应位置再修改。
问题主要集中在三类：路径搞错、拼写错误、缩进不对。
最重要的习惯：改完代码先按 `Ctrl+S` 保存，再看效果。
复习依赖：项目运行需要用到的外部库（FastAPI、Uvicorn），记录在 requirements.txt 里方便别人一键安装



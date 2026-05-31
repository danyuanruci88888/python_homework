# Week02 Day02 — GET、POST、PUT、DELETE 与 RESTful

## 今天学了什么

今天学习了 HTTP 的四种请求方法，以及 RESTful 接口设计风格。

**RESTful 的核心思路：​**
- 用路径表示资源（名词）：比如 `/tasks` 代表"任务"这个东西
- 用方法表示动作（动词）：GET 查询、POST 新增、PUT 修改、DELETE 删除
- 不要把动作写进路径里，`/getTasks` 这种写法不专业

**四种方法的区别：​**
- GET：查询数据，不改变任何内容
- POST：新增一条数据
- PUT：修改一条已有的数据
- DELETE：删除一条数据

**路径参数的写法：​**
`/tasks/{task_id}` 里的花括号是 FastAPI 的路径参数语法，
不能写成 f-string 格式 `f"/tasks/{task_id}"`，两者完全不同。

**内存数据的概念：​**
这次的 tasks 列表直接写在代码里，只存在内存中，
服务重启后数据会恢复原样，这不是 bug，第三周接数据库后才会持久化。

## 接口列表

| Method | URL               | 作用           |
|--------|-------------------|----------------|
| GET    | /tasks            | 查询所有任务   |
| GET    | /tasks/{task_id}  | 查询单个任务   |
| POST   | /tasks            | 新增任务       |
| PUT    | /tasks/{task_id}  | 将任务标记完成 |
| DELETE | /tasks/{task_id}  | 删除任务       |

## 如何运行

进入项目文件夹并激活虚拟环境：

    cd homework\week02_day02
    .venv\Scripts\activate

安装依赖：

    pip install -r requirements.txt

启动服务：

    uvicorn main:app --reload

看到以下提示说明启动成功：

    INFO: Uvicorn running on http://127.0.0.1:8000

## 如何测试

打开浏览器访问 Swagger 页面：

    http://127.0.0.1:8000/docs

在 Swagger 页面上，每个接口都可以点击 Try it out 直接测试：
- GET /tasks：直接点 Execute，返回所有任务列表
- GET /tasks/{task_id}：输入 1 或 2，返回对应任务；输入 99 返回"任务不存在"
- POST /tasks：直接点 Execute，新增一条固定任务
- PUT /tasks/{task_id}：输入 1，把第一个任务状态改为 done
- DELETE /tasks/{task_id}：输入 2，删除第二个任务

## 我遇到了什么问题

1. 把路径参数写成了 f-string 格式 `@app.put(f"/tasks/{task_id}")`，
   报 `NameError: name 'task_id' is not defined`——
   装饰器里的花括号是 FastAPI 语法，不能加 f
2. 写了两个重复的 `@app.put` 接口，导致逻辑混乱
3. `tasks.append` 拼成了 `tasks.apppend`，多打了一个 p
4. `message` 拼成了 `massage`（按摩），返回字段名写错
5. PUT 接口里 `return {"message":"任务不存在"}` 缩进写错，
   放在了 for 循环里面，导致第一个任务不匹配就立刻返回，
   永远不会继续找下一个
6. `week02_day02` 没有创建虚拟环境就直接激活，报"无法加载模块"——
   每个新项目文件夹都要重新执行 `python -m venv .venv`
7. 不小心进入了 Python 交互模式（终端出现 `>>>`），
   在里面输 `cd` 命令报 SyntaxError——需要先 `exit()` 退出再操作

## 我是怎么解决的

每次报错先看终端里的错误类型和行号，找到对应代码位置再修改。
f-string 问题是理解了路径参数的语法后解决的——FastAPI 的 `{task_id}` 
是框架自己的占位符，和 Python 的 f-string 是两回事。
缩进问题通过仔细对比 for 循环和 return 的层级关系发现并修正。

## 我最想优化的地方

- POST 接口目前新增的任务内容是写死的，希望能让用户自己输入任务名称
- PUT 接口只能把状态改成 done，希望能修改更多字段
- id 是硬编码的 3，多次新增会出现重复 id，需要动态生成
- 希望接上数据库，让数据在重启后不丢失

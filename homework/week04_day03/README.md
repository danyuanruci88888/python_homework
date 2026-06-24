# Week04 Day03 学习总结

## 一、今天学了什么

今天学习了三个工程化能力：**Docker、环境变量、日志**。

### Docker
Docker 可以理解成项目的"打包盒"。它的作用是减少"环境不一致"的问题——我自己电脑能跑的项目，换了老师或面试官的电脑不一定能跑，但用 Docker 打包后，环境就统一了。

### 环境变量
以前我把数据库密码直接写在代码里，今天学会了放到 `.env` 文件中，代码通过 `os.getenv()` 读取。这样密码不会提交到 Git，也更方便不同环境切换配置。

### 日志
学会了用 Python 的 `logging` 模块替代 `print()`。日志可以分级别（INFO、WARNING、ERROR 等），还能配置格式和时间戳，更适合真实项目排查问题。

---

## 二、作业结构

```
week04_day03/
├── 项目代码/              # FastAPI 项目
│   ├── main.py
│   ├── database.py
│   ├── routers/
│   ├── services/
│   └── ...
├── docker-compose.yml     # 启动 MySQL 和 Redis
├── .env.example           # 环境变量模板
├── log_test.py            # 日志测试脚本
├── README.md              # 本文件
└── 运行截图/              # 运行截图
```

---

## 三、关于 log_test.py 的说明

`log_test.py` 是今日小练习中要求的**日志测试脚本**，用于演示 `logging` 模块的基本用法。

按照飞书给出的提交要求，最终的文件夹结构里并没有明确要求包含这个文件。但是我认为，保留这个脚本能够更直接地证明我确实完成了"写一个日志测试脚本"这个小练习，也便于体现了我理解了日志级别、格式配置等基础内容。

因此，我把 `log_test.py` 放在了 `week04_day03/` 的根目录下，而不是 `项目代码/` 里面。原因是：它不是 FastAPI 项目的一部分，而是一个独立的练习文件。如果把所有练习文件都塞进项目代码里，反而会让项目结构变得混乱。

> 提交结构以老师要求为准，`log_test.py` 作为额外的练习成果一并提交。

---

## 四、作业怎么运行

### 1. 准备环境变量

先复制环境变量模板：

```bash
cp .env.example .env
```

然后修改 `.env` 中的 `SECRET_KEY`，换成自己的密钥。

### 2. 启动 Docker 容器

确保 Docker Desktop 已经打开，然后执行：

```bash
docker compose up -d
```

验证容器是否启动：

```bash
docker ps
```

应该能看到 `ai_mysql` 和 `ai_redis` 两个容器。

### 3. 启动 FastAPI 项目

```bash
cd 项目代码
source .venv/Scripts/activate
uvicorn main:app --reload
```

> 注意：`database.py` 会从当前目录读取 `.env`，所以运行前请确认 `项目代码/` 目录下也有 `.env` 文件。如果没有，可以从 `week04_day03/` 复制一份进来。

### 4. 测试接口

打开浏览器访问：

```
http://127.0.0.1:8000/docs
```

由于 Docker 里的 MySQL 是全新的数据库，旧用户数据不存在，需要先：

1. 调用 `POST /users/register` 注册一个新用户
2. 调用 `POST /auth/login` 登录，获取 token
3. 在 Swagger 顶部点击 Authorize，输入 `Bearer <你的token>`
4. 调用 `GET /statistics/progress` 查看学习进度统计

---

## 五、遇到的问题和解决方法

### 问题 1：Docker Desktop 安装时提示 WSL 未安装

第一次打开 Docker Desktop 时，弹窗提示 `WSL not installed`。

**解决方法：**

1. 以管理员身份打开 PowerShell
2. 执行 `wsl --install` 时提示 `已禁止(403)`
3. 改用 `wsl --install --web-download` 成功下载并安装 WSL 和 Ubuntu
4. 重启电脑后 Docker Desktop 正常打开

### 问题 2：本机 MySQL 占用了 3306 端口

执行 `docker compose up -d` 时，`ai_mysql` 容器启动失败，报错：

```
ports are not available: exposing port TCP 0.0.0.0:3306 ... bind: Only one usage...
```

**解决方法：**

原因是本机已经运行了 MySQL 服务，占用了 3306 端口。我打开 `services.msc`，找到 MySQL 服务并停止，然后重新执行 `docker compose up -d`，两个容器都启动成功。

### 问题 3：运行日志测试脚本时文件名打错

输入 `python log_text.py` 报错找不到文件，实际上文件名是 `log_test.py`。

**解决方法：**

改成 `python log_test.py` 运行成功。

### 问题 4：Docker MySQL 里没有旧用户数据

用第 3 周注册的账号登录时返回 401 Unauthorized。

**解决方法：**

因为 Docker 启动的是一个全新的 MySQL 数据库，旧数据不存在。我通过 `POST /users/register` 重新注册了一个用户，然后登录成功。


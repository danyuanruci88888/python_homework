# AI 就业陪跑任务管理系统后端

## 项目介绍

本项目面向应届生 AI 应用开发求职准备场景，提供学习任务管理、岗位收藏、投递记录、学习进度统计等能力，帮助学生系统化管理学习和求职过程。

通过本项目，用户可以注册登录后管理自己的学习任务、收藏感兴趣的岗位、记录投递进度，并通过 Redis 缓存加速学习进度统计查询。

## 技术栈

- **Python 3.11**
- **FastAPI**：Web 框架，自动生成 Swagger 接口文档
- **SQLAlchemy**：ORM 框架，操作 MySQL 数据库
- **MySQL 8**：持久化存储用户、任务、岗位、收藏、投递等数据
- **Redis 7**：缓存学习进度统计结果
- **Docker**：通过 Docker Compose 一键启动 MySQL 和 Redis
- **JWT**：用户认证，保护需要登录的接口
- **Pydantic**：接口请求和响应数据校验

## 功能模块

### 1. 用户模块
- 用户注册
- 用户登录（JWT Token）
- 获取当前用户信息

### 2. 任务模块
- 创建学习任务
- 查询任务列表（按用户隔离）
- 修改任务状态
- 删除任务

### 3. 岗位模块
- 创建岗位信息
- 查询岗位列表

### 4. 收藏模块
- 收藏岗位
- 查询我的收藏

### 5. 投递模块
- 新增投递记录
- 查询我的投递记录
- 修改投递状态（如：已投递 → 面试中）

### 6. 统计模块
- 查询学习进度统计
- Redis 缓存加速

## 项目结构

```
week04_day04/
├── README.md                  # 本文件
├── api_test_checklist.md      # 接口测试清单
├── screenshots/               # Swagger 测试截图
├── demo_video_link.txt        # 演示视频链接
├── docker-compose.yml         # 启动 MySQL 和 Redis
└── 项目代码/                   # FastAPI 后端项目
    ├── main.py                # 应用入口
    ├── database.py            # 数据库连接
    ├── models.py              # 数据库模型
    ├── schemas.py             # 数据校验模型
    ├── requirements.txt       # 依赖列表
    ├── .env.example           # 环境变量模板
    ├── .env                   # 环境变量（不提交到 Git）
    ├── routers/               # 路由模块
    │   ├── auth.py            # 登录认证
    │   ├── users.py           # 用户相关
    │   ├── tasks.py           # 任务相关
    │   ├── jobs.py            # 岗位相关
    │   ├── favorites.py       # 收藏相关
    │   ├── applications.py    # 投递相关
    │   └── statistics.py      # 统计相关
    └── services/              # 业务逻辑层
        ├── auth_service.py    # JWT 相关
        └── redis_service.py   # Redis 缓存相关
```

> **关于目录结构的说明**：老师要求的提交结构是 `README.md`、`api_test_checklist.md`、`screenshots/`、`demo_video_link.txt`。为了让项目能够被老师和面试官直接运行，我额外保留了 `项目代码/` 和 `docker-compose.yml`，这样拿到文件夹后可以一键启动后端服务。

## 快速启动

### 1. 启动 Docker 容器

确保 Docker Desktop 已打开，然后在 `week04_day04/` 目录执行：

```bash
cd week04_day04
docker compose up -d
```

验证容器是否运行：

```bash
docker ps
```

应该能看到 `ai_mysql` 和 `ai_redis` 两个容器。

### 2. 配置环境变量

进入 `项目代码/` 目录，复制环境变量模板：

```bash
cd 项目代码
cp .env.example .env
```

然后编辑 `.env` 文件，填写正确的数据库密码。

### 3. 激活虚拟环境并安装依赖

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

### 4. 启动 FastAPI 服务

```bash
uvicorn main:app --reload
```

启动成功后访问：

```text
http://127.0.0.1:8000/docs
```

## 环境变量

`.env` 文件示例：

```text
DATABASE_URL=mysql+pymysql://root:root@localhost:3306/ai_class?charset=utf8mb4
SECRET_KEY=your-secret-key
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```

> 注意：`.env` 文件包含数据库密码等敏感信息，已加入 `.gitignore`，请勿提交到 Git。

## 接口文档

启动项目后，Swagger 自动生成接口文档：

```text
http://127.0.0.1:8000/docs
```

接口分组包括：
- `auth`：登录认证
- `users`：用户注册、获取当前用户
- `tasks`：任务增删改查
- `jobs`：岗位增删查
- `favorites`：岗位收藏
- `applications`：投递记录
- `statistics`：学习进度统计

## 测试账号

- 用户名：`xiaoling`
- 密码：`123456`

## 项目亮点

1. **模块化路由设计**：按功能拆分路由文件，结构清晰，便于维护。
2. **JWT 用户认证**：登录后返回 Token，保护用户私有数据。
3. **数据隔离**：任务、收藏、投递等数据都按用户 ID 隔离，只能查看自己的数据。
4. **Redis 缓存**：学习进度统计接口使用 Redis 缓存，减少数据库查询压力。
5. **Docker 一键启动**：通过 `docker-compose.yml` 快速搭建 MySQL 和 Redis 环境。

## 后续优化

1. 增加岗位搜索和筛选功能。
2. 增加技能标签模块。
3. 添加单元测试，提高代码稳定性。
4. 完善异常处理和日志记录。
5. 增加数据分页，避免查询大量数据时接口过慢。

---

## 今天学了什么

今天学习了项目包装的完整流程：

1. **Swagger 接口测试**：学会用 Swagger 验证每个接口的正常和异常情况。
2. **接口测试清单整理**：把每个接口的 Method、URL、Token 需求、正常测试、异常测试整理成文档。
3. **README 写作**：理解 README 是项目的"说明书"，要写清楚项目介绍、技术栈、运行方式、遇到的问题等。
4. **演示视频准备**：学习如何规划视频内容，在 3 到 5 分钟内讲清楚项目价值。

## 遇到的问题和解决方法

### 问题 1：虚拟环境路径不对

**现象**：运行 `uvicorn` 时，系统使用的是 `week03_day05_project/.venv/` 里的 `uvicorn`。

**解决**：在 `week04_day04/项目代码/` 下重新创建并激活虚拟环境，安装依赖。

### 问题 2：DATABASE_URL 未设置

**现象**：启动项目时报错 `ValueError: DATABASE_URL 未设置`。

**解决**：复制 `.env.example` 为 `.env`，并填写正确的数据库连接地址。

### 问题 3：Docker Desktop 没打开

**现象**：执行 `docker compose up -d` 时报错，提示连接不上 Docker daemon。

**解决**：打开 Docker Desktop，等待引擎启动完成后再执行命令。

### 问题 4：本机 MySQL 占用了 3306 端口

**现象**：`ai_mysql` 容器启动失败，提示端口被占用。

**解决**：在 `services.msc` 中停止本机 MySQL 服务，释放 3306 端口。

### 问题 5：`routers/jobs.py` 缩进错误

**现象**：启动项目时报 `IndentationError`，`create_job` 函数体缩进不对。

**解决**：将函数体统一缩进 4 个空格，并把 `Job(...)` 的闭合括号对齐。

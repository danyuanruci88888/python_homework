# AI 就业陪跑任务管理系统后端

## 项目介绍

本项目面向应届生 AI 应用开发求职准备场景，提供学习任务管理、岗位收藏、投递记录、技能标签管理和学习进度统计等能力，帮助学生系统化管理学习和求职过程。

通过本项目，用户可以注册登录后管理自己的学习任务、收藏感兴趣的岗位、记录投递进度、维护个人技能标签，并通过统计模块查看学习完成情况。

## 技术栈

- **Python 3.11**
- **FastAPI**：Web 框架，自动生成 Swagger 接口文档
- **SQLAlchemy**：ORM 框架，操作 MySQL 数据库
- **MySQL 8**：持久化存储用户、任务、岗位、收藏、投递、标签等数据
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

### 6. 技能标签模块
- 创建技能标签
- 查询我的技能标签
- 删除技能标签

### 7. 统计模块
- 查询学习进度统计
- 返回任务完成率、投递数量、技能标签数量
- Redis 缓存加速

## 项目结构

```
stage01_final_project/
├── README.md                  # 本文件
├── docker-compose.yml         # 启动 MySQL 和 Redis
├── requirements.txt           # Python 依赖
├── .env.example               # 环境变量模板
├── .gitignore                 # Git 忽略规则
├── app/                       # FastAPI 后端项目
│   ├── main.py                # 应用入口
│   ├── database.py            # 数据库连接
│   ├── models.py              # 数据库模型
│   ├── schemas.py             # 数据校验模型
│   ├── routers/               # 路由模块
│   │   ├── auth.py            # 登录认证
│   │   ├── users.py           # 用户相关
│   │   ├── tasks.py           # 任务相关
│   │   ├── tags.py            # 技能标签相关
│   │   ├── jobs.py            # 岗位相关
│   │   ├── favorites.py       # 收藏相关
│   │   ├── applications.py    # 投递相关
│   │   └── statistics.py      # 统计相关
│   └── services/              # 业务逻辑层
│       ├── auth_service.py    # JWT 相关
│       └── redis_service.py   # Redis 缓存相关
├── docs/                      # 项目文档
│   ├── api_test_checklist.md  # 接口测试清单
│   ├── resume_description.md  # 简历项目描述
│   └── defense_script.md      # 答辩稿
├── screenshots/               # Swagger 测试截图
└── demo_video_link.txt        # 演示视频链接
```

## 快速启动

### 1. 启动 Docker 容器

确保 Docker Desktop 已打开，然后在 `stage01_final_project/` 目录执行：

```bash
cd stage01_final_project
docker compose up -d
```

验证容器是否运行：

```bash
docker ps
```

应该能看到 `ai_mysql` 和 `ai_redis` 两个容器。

### 2. 配置环境变量

进入 `app/` 目录，复制环境变量模板：

```bash
cd app
cp .env.example .env
```

然后编辑 `.env` 文件，填写正确的数据库密码。

### 3. 激活虚拟环境并安装依赖

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r ../requirements.txt
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
- `认证`：登录认证
- `用户`：用户注册、获取当前用户
- `任务`：任务增删改查
- `标签`：技能标签管理
- `岗位`：岗位增删查
- `收藏`：岗位收藏
- `投递`：投递记录
- `统计`：学习进度统计

## 测试账号

- 用户名：`xiaoling`
- 密码：`123456`

## 项目亮点

1. **模块化路由设计**：按功能拆分路由文件，结构清晰，便于维护。
2. **JWT 用户认证**：登录后返回 Token，保护用户私有数据。
3. **数据隔离**：任务、收藏、投递、标签等数据都按用户 ID 隔离，只能查看自己的数据。
4. **Redis 缓存**：学习进度统计接口使用 Redis 缓存，减少数据库查询压力。
5. **Docker 一键启动**：通过 `docker-compose.yml` 快速搭建 MySQL 和 Redis 环境。
6. **技能标签模块**：支持用户维护个人技能标签，为后续 AI 岗位匹配和学习计划生成打下基础。
7. **完整求职跟踪链路**：实现岗位收藏、投递记录、投递状态变更，覆盖求职准备核心场景。

## 后续优化

1. 增加岗位搜索和筛选功能。
2. 增加 AI 简历优化助手。
3. 增加岗位 JD 匹配系统。
4. 增加 AI 面试题生成系统。
5. 增加 RAG 就业知识库。
6. 添加单元测试，提高代码稳定性。
7. 完善异常处理和日志记录。
8. 增加数据分页，避免查询大量数据时接口过慢。

## 演示视频

项目演示视频已上传到夸克网盘：

- 链接：https://pan.quark.cn/s/2411c39dfe22

> 视频时长约 3-5 分钟，展示了项目目录、技术栈、服务启动、Swagger 接口测试（注册、登录、任务、岗位、收藏、投递、标签、统计）以及项目亮点说明。

---

## 今天学了什么

今天是第一阶段最后一天，学习了项目最终包装和交付：

1. **阶段项目最终检查**：对照最终功能清单，确认项目包含用户、任务、岗位、收藏、投递、标签、统计等模块。
2. **项目答辩准备**：整理答辩稿，按项目背景、技术栈、功能、数据库、鉴权、缓存、Docker、难点、AI 升级等顺序组织内容。
3. **简历项目描述**：学会把项目写进简历，突出技术栈和项目亮点，而不是只写"做了一个 FastAPI 项目"。
4. **项目亮点提炼**：总结项目的核心优势，如分层架构、JWT 鉴权、数据隔离、Redis 缓存、Docker 部署等。
5. **后续优化计划**：思考如何把后端底座升级为 AI 项目，包括 AI 简历优化、JD 匹配、面试题生成等方向。

## 遇到的问题和解决方法

### 问题 1：阶段项目目录结构不清楚

**现象**：不知道应该把最终项目放在哪里，代码应该叫 `app/` 还是 `项目代码/`。

**解决**：按照课程要求创建 `stage01_final_project/` 文件夹，代码统一放在 `app/` 目录下。

### 问题 2：新增技能标签模块时外键写错

**现象**：`Tag` 模型的 `user_id` 外键写成 `ForeignKey('user.id')`，启动后数据库报错。

**解决**：改成 `ForeignKey('users.id')`，与实际用户表名一致。

### 问题 3：统计接口返回字段和 schema 对不上

**现象**：`ProgressResponse` 里字段名拼写错误，导致接口返回数据校验失败。

**解决**：统一字段名为 `application_count` 和 `tag_count`，确保 schema、路由、数据库查询一致。

### 问题 4：标签路由拼写错误较多

**现象**：新建 `tags.py` 时出现 `aqlalchemy`、`datebase`、`reouter` 等拼写错误。

**解决**：逐行检查报错信息，对照正确模块名和函数名修正。

### 问题 5：旧项目和新项目虚拟环境不共用

**现象**：`stage01_final_project/app/` 目录下没有 `.venv`，无法直接启动。

**解决**：在新目录下重新创建虚拟环境并安装依赖。

### 问题 6：MySQL 连接断开

**现象**：Swagger 测试时接口返回 500，报错 `MySQL server has gone away`。

**解决**：检查 Docker 容器状态，重启 FastAPI 服务恢复数据库连接。

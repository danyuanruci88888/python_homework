# Week04 Day02 Redis 缓存练习

## 1. 今天学了什么

今天主要学习了以下内容：

- **Redis 是什么**：一个基于内存的 key-value 数据库，读写速度很快，适合用来做缓存。
- **缓存的基本流程**：请求进来先查 Redis，命中直接返回；未命中则查 MySQL，写入 Redis 后再返回。
- **设置缓存过期时间**：用 `ex=秒数` 给 key 设置过期时间。
- **在 FastAPI 中使用 Redis**：通过 `redis` 包连接 Redis，实现缓存读写。
- **给学习进度统计加缓存**：新增 `GET /statistics/progress` 接口，把统计结果缓存到 Redis。

## 2. Redis 和 MySQL 的区别

| 对比项 | MySQL | Redis |
|---|---|---|
| 数据存储位置 | 磁盘，适合长期保存 | 内存，读写速度极快 |
| 访问速度 | 相对较慢 | 非常快 |
| 主要用途 | 持久化存储业务数据 | 缓存、临时数据、热点数据 |
| 数据结构 | 关系型表结构 | key-value 键值对 |
| 是否适合复杂查询 | 适合 | 不适合 |

简单来说：**MySQL 是仓库，适合存重要资料；Redis 是小黑板，适合临时写常用数据。**

## 3. 什么是缓存命中

**缓存命中**是指：请求进来后，先去 Redis 查数据，如果 Redis 里有，就直接返回，不用访问 MySQL。

**缓存未命中**是指：Redis 里没有数据，只能去 MySQL 查询，然后把结果写入 Redis，下次再查时就能命中。

本项目的缓存流程：

```
请求 GET /statistics/progress
    ↓
先查 Redis
    ↓
命中 → 直接返回缓存结果
未命中 → 查 MySQL 计算 → 写入 Redis → 返回结果
```

## 4. 缓存 key 怎么设计

为了保证每个用户的数据互不干扰，缓存 key 设计为：

```text
user:{user_id}:progress
```

例如用户 ID 为 5，对应的 key 就是：

```text
user:5:progress
```

value 中存储的是一个 JSON 对象：

```json
{
  "total": 4,
  "completed": 2,
  "completion_rate": 50.0
}
```

## 5. 作业怎么运行

```bash
# 1. 进入项目代码目录
cd 项目代码

# 2. 激活虚拟环境
source ../.venv/Scripts/activate

# 3. 启动服务
uvicorn main:app --reload
```

启动后访问 Swagger：`http://127.0.0.1:8000/docs`

测试步骤：

1. 注册并登录用户，获取 token。
2. 点击 Authorize，输入 `Bearer token`。
3. 创建几个任务，其中一部分 `status` 填 `"已完成"`。
4. 调用 `GET /statistics/progress` 两次：
   - 第一次从 MySQL 查询并写入 Redis。
   - 第二次从 Redis 缓存直接返回。

## 6. 遇到的问题和解决方法

### 问题 1：复制 week03 代码时命令报错

**现象：** 执行 `cp -r week03_day05_project/* week04_day02/项目代码/` 时报错 `No such file or directory`，后来还误把 `cp` 写成了 `cd`。

**原因：** 第一次 `*` 通配符展开失败，第二次把复制命令写成了切换目录命令。

**解决：** 改用 `cp -r week03_day05_project/. week04_day02/项目代码/` 复制整个目录内容。

### 问题 2：创建 README.md 时命令报错

**现象：** 输入 `tpye nul > README.md` 报错 `command not found`。

**原因：** `type` 拼写成了 `tpye`，而且 `type nul > 文件名` 是 CMD 语法，Git Bash 不支持。

**解决：** 在 Git Bash 里用 `touch README.md` 创建空文件。

### 问题 3：在错误目录运行 uvicorn

**现象：** 在 `week04_day02` 根目录运行 `uvicorn main:app --reload` 报错 `Could not import module "main"`。

**原因：** `main.py` 在 `项目代码/` 子目录里，不在当前目录。

**解决：** 先 `cd 项目代码`，再运行 `uvicorn main:app --reload`。

### 问题 4：git add 时把虚拟环境加进去了

**现象：** `git add 项目代码/` 后出现大量 `.venv/` 文件的 warning。

**原因：** `.venv/` 被加到了 Git 暂存区。

**解决：** 执行 `git reset` 取消 add，然后逐个 add 需要的文件，确保 `.venv/` 和 `.env` 被 `.gitignore` 忽略。

### 问题 5：第一次调用接口后 Redis 没有缓存

**现象：** 调用 `GET /statistics/progress` 返回 200，但 Redis 里没有 `user:*` 的 key。

**原因：** 启动 uvicorn 时加载的是旧代码，修改后的缓存逻辑没有生效。

**解决：** 停止 uvicorn，重新启动项目，再调用接口。

### 问题 6：重启后调用接口报 401

**现象：** 重启 uvicorn 后调用 `GET /statistics/progress` 返回 `401 Unauthorized`。

**原因：** 重启后 Swagger 的 Authorize token 失效了。

**解决：** 重新登录获取 token，再点击 Authorize 输入 `Bearer token`。

### 问题 7：终端找不到 redis-cli 命令

**现象：** 输入 `redis-cli` 报错 `command not found`，但任务管理器显示 Redis 正在运行。

**原因：** Redis 已作为 Windows 服务运行，但安装路径没有加到系统 PATH 环境变量里。

**解决：** 用 Python 脚本检查 Redis 缓存，例如：

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
print(r.keys('user:*'))
print(r.get('user:5:progress'))
```

## 7. 项目接口说明

- `POST /users/register`：用户注册
- `POST /auth/login`：用户登录
- `GET /statistics/progress`：获取当前用户学习进度统计（需要登录，结果缓存到 Redis）

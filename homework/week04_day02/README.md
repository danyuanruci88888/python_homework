# Week04 Day02 Redis 缓存练习

## 1. Redis 和 MySQL 的区别

| 对比项 | MySQL | Redis |
|---|---|---|
| 数据存储位置 | 磁盘，适合长期保存 | 内存，读写速度极快 |
| 访问速度 | 相对较慢 | 非常快 |
| 主要用途 | 持久化存储业务数据 | 缓存、临时数据、热点数据 |
| 数据结构 | 关系型表结构 | key-value 键值对 |
| 是否适合复杂查询 | 适合 | 不适合 |

简单来说：**MySQL 是仓库，适合存重要资料；Redis 是小黑板，适合临时写常用数据。**

## 2. 什么是缓存命中

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

## 3. 缓存 key 怎么设计

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

## 4. 项目运行方式

```bash
# 1. 进入项目代码目录
cd 项目代码

# 2. 激活虚拟环境
source ../.venv/Scripts/activate

# 3. 启动服务
uvicorn main:app --reload
```

启动后访问 Swagger：`http://127.0.0.1:8000/docs`

## 5. 接口说明

- `POST /users/register`：用户注册
- `POST /auth/login`：用户登录
- `GET /statistics/progress`：获取当前用户学习进度统计（需要登录，结果缓存到 Redis）

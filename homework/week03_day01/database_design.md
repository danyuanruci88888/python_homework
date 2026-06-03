# 数据库表设计

## 一、users 表（用户表）

| 字段名        | 类型         | 说明               | 键         |
|---------------|--------------|--------------------|------------|
| id            | INTEGER      | 用户唯一标识，自增 | 主键 PK    |
| username      | VARCHAR(50)  | 用户名，唯一       |            |
| password_hash | VARCHAR(255) | 密码哈希值，不存明文 |          |
| created_at    | DATETIME     | 注册时间           |            |

---

## 二、tasks 表（任务表）

| 字段名     | 类型         | 说明                          | 键                   |
|------------|--------------|-------------------------------|----------------------|
| id         | INTEGER      | 任务唯一标识，自增            | 主键 PK              |
| title      | VARCHAR(200) | 任务标题                      |                      |
| status     | VARCHAR(20)  | 任务状态（如 pending / done） |                      |
| user_id    | INTEGER      | 所属用户 ID                   | 外键 FK → users.id   |
| created_at | DATETIME     | 创建时间                      |                      |
| updated_at | DATETIME     | 最后更新时间                  |                      |

---

## 三、job_favorites 表（岗位收藏表）

| 字段名       | 类型         | 说明               | 键                   |
|--------------|--------------|--------------------|----------------------|
| id           | INTEGER      | 收藏记录唯一标识，自增 | 主键 PK           |
| user_id      | INTEGER      | 收藏该岗位的用户 ID | 外键 FK → users.id  |
| company_name | VARCHAR(100) | 公司名称           |                      |
| job_title    | VARCHAR(100) | 岗位名称           |                      |
| salary       | VARCHAR(50)  | 薪资范围（如 15k-20k） |                  |
| city         | VARCHAR(50)  | 工作城市           |                      |
| created_at   | DATETIME     | 收藏时间           |                      |

---

## 四、表与表之间的关系说明

**users 与 tasks：​** 一对多关系。一个用户可以拥有多个任务，但每个任务只属于一个用户。`tasks.user_id` 是外键，指向 `users.id`。

**users 与 job_favorites：​** 一对多关系。一个用户可以收藏多个岗位，但每条收藏记录只属于一个用户。`job_favorites.user_id` 是外键，指向 `users.id`。

**tasks 与 job_favorites：​** 两者之间没有直接关系，均独立挂载在 `users` 表下。

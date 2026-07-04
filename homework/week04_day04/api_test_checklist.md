# 接口测试清单

## 一、用户模块

### 1. 用户注册

- **Method**: POST
- **URL**: `/users/register`
- **是否需要 Token**: 否
- **正常测试**: 用户名 `xiaoling2`，密码 `123456`，返回 200 和用户信息
- **异常测试**: 再次使用 `xiaoling2` 注册，返回 400，提示 `Username already registered`

### 2. 用户登录

- **Method**: POST
- **URL**: `/auth/login`
- **是否需要 Token**: 否
- **正常测试**: 用户名 `xiaoling`，密码 `123456`，返回 `access_token`
- **异常测试**: 密码输入错误，返回 401，提示 `Incorrect username or password`

### 3. 获取当前用户

- **Method**: GET
- **URL**: `/users/me`
- **是否需要 Token**: 是
- **正常测试**: 携带 Token，返回当前用户信息
- **异常测试**: 不携带 Token，返回 401

---

## 二、任务模块

### 4. 创建任务

- **Method**: POST
- **URL**: `/tasks/`
- **是否需要 Token**: 是
- **正常测试**: 传入 `title` 和 `status`，返回创建的任务
- **异常测试**: 不携带 Token，返回 401

### 5. 查询任务列表

- **Method**: GET
- **URL**: `/tasks/`
- **是否需要 Token**: 是
- **正常测试**: 返回当前用户的所有任务
- **异常测试**: 不携带 Token，返回 401

### 6. 修改任务状态

- **Method**: PUT
- **URL**: `/tasks/{task_id}`
- **是否需要 Token**: 是
- **正常测试**: 将任务状态改为 `"已完成"`，返回更新后的任务
- **异常测试**: 修改不存在的 `task_id`，返回 404

### 7. 删除任务

- **Method**: DELETE
- **URL**: `/tasks/{task_id}`
- **是否需要 Token**: 是
- **正常测试**: 删除存在的任务，返回删除成功
- **异常测试**: 删除不存在的 `task_id`，返回 404

---

## 三、岗位模块

### 8. 创建岗位

- **Method**: POST
- **URL**: `/jobs/`
- **是否需要 Token**: 是
- **正常测试**: 传入 `title`、`company` 等信息，返回创建的岗位
- **异常测试**: 不携带 Token，返回 401

### 9. 查询岗位列表

- **Method**: GET
- **URL**: `/jobs/`
- **是否需要 Token**: 是
- **正常测试**: 返回岗位列表
- **异常测试**: 不携带 Token，返回 401

---

## 四、收藏模块

### 10. 收藏岗位

- **Method**: POST
- **URL**: `/favorites/`
- **是否需要 Token**: 是
- **正常测试**: 传入存在的 `job_id`，返回收藏记录
- **异常测试**: 收藏不存在的 `job_id`，返回 404

### 11. 查询收藏

- **Method**: GET
- **URL**: `/favorites/`
- **是否需要 Token**: 是
- **正常测试**: 返回当前用户的收藏列表
- **异常测试**: 不携带 Token，返回 401

---

## 五、投递模块

### 12. 新增投递记录

- **Method**: POST
- **URL**: `/applications/`
- **是否需要 Token**: 是
- **正常测试**: 传入存在的 `job_id`，返回投递记录
- **异常测试**: 投递不存在的 `job_id`，返回 404

### 13. 修改投递状态

- **Method**: PUT
- **URL**: `/applications/{application_id}`
- **是否需要 Token**: 是
- **正常测试**: 修改 `status` 为 `"面试中"`，返回更新后的记录
- **异常测试**: 修改不存在的 `application_id`，返回 404

---

## 六、统计模块

### 14. 查询学习进度

- **Method**: GET
- **URL**: `/statistics/progress`
- **是否需要 Token**: 是
- **正常测试**: 返回 `total`、`completed`、`completion_rate`
- **异常测试**: 不携带 Token，返回 401

### 15. Redis 缓存生效

- **Method**: GET
- **URL**: `/statistics/progress`
- **是否需要 Token**: 是
- **正常测试**: 第一次调用从 MySQL 查询并写入 Redis；第二次调用从 Redis 缓存直接返回
- **验证方式**: Redis 中存在 `user:{user_id}:progress` 的 key

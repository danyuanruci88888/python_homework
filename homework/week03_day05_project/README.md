# Week03 Day05 - JWT 登录与用户隔离任务系统

## 一、今天学了什么

### 1. JWT（JSON Web Token）是什么
JWT 就是一张"临时通行证"。用户登录成功后，服务器发一张 Token 给前端，前端以后每次请求都带上这张 Token，服务器就知道"你是谁"了。Token 有过期时间，过期后就失效，需要重新登录。


---

## 二、项目结构

```
week03_day05_project/
├── main.py                  # FastAPI 入口，注册路由
├── database.py              # 数据库连接配置
├── models.py                # ORM 模型（User、Task）
├── schemas.py               # Pydantic 数据模型
├── routers/
│   ├── auth.py              # 登录接口 + 依赖注入（get_current_user）
│   ├── users.py             # 注册接口 + 当前用户
│   └── tasks.py             # 任务 CRUD（需登录）
├── services/
│   └── auth_service.py      # JWT Token 生成
├── requirements.txt         # 依赖清单
├── README.md                # 项目说明
└── 测试截图/                 # API 测试截图
```

---

## 三、作业怎么运行

### 环境准备

1. **进入项目目录**
   ```bash
   cd week03_day05_project
   ```

2. **激活虚拟环境**
   ```bash
   source .venv/Scripts/activate
   ```

3. **安装依赖**
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql python-dotenv passlib[bcrypt]
   pip install python-jose[cryptography] python-multipart
   pip install bcrypt==4.0.1
   ```

4. **配置数据库密码**
   在项目根目录创建 `.env` 文件：
   ```
   DATABASE_PASSWORD=你的MySQL密码
   ```

### 启动项目

```bash
uvicorn main:app --reload
```

浏览器打开 `http://127.0.0.1:8000/docs` 进行测试。

---

## 四、接口使用说明

### 1. 注册

1. 找到 `POST /users/register`，点 **Try it out**
2. 输入：
   ```json
   {
     "username": "xiaoli",
     "password": "123456"
   }
   ```
3. 点 **Execute**
4. 成功返回：`{"id": 3, "username": "xiaoling"}`

### 2. 登录

1. 找到 `POST /auth/login`，点 **Try it out**
2. 输入：
   ```json
   {
     "username": "xiaoli",
     "password": "123456"
   }
   ```
3. 点 **Execute**
4. 成功返回 Token：
   ```json
   {
     "access_token": "eyJhbGciOiJIUzI1NiIs...",
     "token_type": "bearer"
   }
   ```

### 3. 如何在 Swagger 中带 Token

1. 点页面右上角的 **Authorize** 按钮
2. 在弹框中输入：
   - **username**：`xiaoli`
   - **password**：`123456`
   - **client_id**：留空
   - **client_secret**：留空
3. 点 **Authorize** → **Close**
4. 现在所有需要登录的接口都会自动带上 Token

### 4. 如何证明用户数据隔离成功

**测试步骤：**

1. **用户 A 创建任务**
   - 用 `xiaoli` 登录
   - `POST /tasks` 创建任务
   - `GET /tasks` 能查到这个任务

2. **用户 B 看不到用户 A 的任务**
   - 点 **Authorize** → **Logout** 清除 Token
   - 用另一个账号（如 `xiaol`）重新登录
   - `GET /tasks` 返回空数组 `[]`
   - **这就证明了用户隔离生效！**

3. **不带 Token 无法访问**
   - 点 **Authorize** → **Logout**
   - 调用 `GET /tasks`
   - 返回 401：`"Could not validate credentials"`

---

## 五、我遇到的问题 & 我是怎么解决的

### 问题 1：虚拟环境每天需要重新激活
**现象：** 昨天创建的虚拟环境，今天打开终端发现 `(.venv)` 不见了。  
**解决：** 虚拟环境不会消失，只是没激活。每天进入项目后执行 `source .venv/Scripts/activate` 即可。

### 问题 2：代码大量拼写错误
**现象：** 手敲代码时出现 `rroot`（多了一个 r）、`form_data.password` 写成匹配用户名、`from_data` 少了 `m` 等错误，导致服务器启动失败或返回 401。  
**解决：** 对照正确代码逐行检查，特别注意变量名、函数名、缩进和冒号。

### 问题 3：Swagger Authorize 弹框报错 422 / 401
**现象：** 点击 Authorize 按钮输入用户名密码后，显示 `Auth Error Error: Unprocessable Entity` 或 `Unauthorized`。  
**原因：** 原来的 `/auth/login` 接口接收 JSON 格式，但 Swagger 的 OAuth2 弹框发送的是表单格式，两者不匹配。  
**解决：** 修改 `routers/auth.py`，把登录参数从 `user_data: UserLogin` 改成 `form_data: OAuth2PasswordRequestForm = Depends()`，让接口接收表单数据，这样 Swagger 弹框就能正常工作了。

### 问题 4：登录返回 401，但用户名密码肯定是对的
**现象：** 终端显示 `POST /auth/login 401 Unauthorized`，但密码明明没错。  
**原因：** `auth.py` 第 22 行把 `form_data.username` 写成了 `form_data.password`，导致用密码去查询用户名字段，永远找不到用户。  
**解决：** 改回 `form_data.username`。

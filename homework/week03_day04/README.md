# Week03 Day04 - SQLAlchemy 用户注册密码哈希

## 一、今天学了什么

### 1. 把 MySQL 接进 FastAPI
前几天直接写 SQL，今天开始用 Python 代码操作数据库。真实项目里经常用 ORM 来连接数据库，而不是手写 SQL。

### 2. ORM 是什么
ORM 是 **Object Relational Mapping（对象关系映射）**，可以先理解成**翻译官**。

我写 Python 的类和对象，ORM 帮我在底层自动翻译成 SQL 语句去操作数据库。比如：
- 我写 `db.query(User).filter(User.username == "xiaolin")`
- ORM 自动翻译成 `SELECT * FROM users WHERE username = 'xiaolin'`

今天用到的 SQLAlchemy 核心组件：
- `create_engine`：创建数据库引擎（连接数据库的入口）
- `sessionmaker`：创建数据库会话（和数据库的一次对话）
- `declarative_base`：创建 ORM 基类，后面定义模型类都要继承它
- `Column`、`Integer`、`String`、`ForeignKey`、`DateTime`：定义表字段的类型

### 3. 使用 SQLAlchemy 连接 MySQL
在 `database.py` 里配置数据库连接：
- 用 `create_engine(DATABASE_URL)` 创建引擎
- 用 `sessionmaker()` 创建会话类
- 写 `get_db()` 函数提供数据库会话，用完自动关闭

### 4. 定义 User 和 Task 模型
在 `models.py` 里用类定义数据库表结构：
- `class User(Base)` 对应 `users` 表
- `class Task(Base)` 对应 `tasks` 表
- 用 `Column(...)` 定义每个字段的类型、约束（主键、唯一、非空等）
- `__tablename__` 指定类对应的数据库表名

### 5. 密码为什么不能明文存
如果数据库里直接存 `password = 123456`，一旦数据库被黑客拖走，所有人的密码直接暴露。而且很多人在不同网站用同一个密码，一个网站泄露等于所有账号都危险。

**正确做法是保存密码哈希。**
哈希可以理解成把密码打碎成一串不可直接看懂的字符串。同样输入永远得到同样输出，方便验证；但从输出无法反推原始密码。

### 6. 使用密码哈希
用 `passlib` 的 `CryptContext` 配合 `bcrypt` 算法：
- `hash_password()`：把原始密码变成哈希值
- `verify_password()`：把用户输入的密码和数据库里的哈希值对比，验证是否正确

### 7. 完成用户注册接口
实现了 `POST /users/register`，逻辑包括：
- 接收 `username` 和 `password`
- 查询数据库，判断用户名是否已存在
- 把密码用 `hash_password()` 哈希后存入数据库
- 注册成功返回用户的 `id` 和 `username`
- 不返回任何密码相关信息

### 8. 用环境变量管理密码
把数据库密码放到 `.env` 文件里，代码里通过 `os.getenv()` 读取。这样密码不会暴露在代码中，也不会被提交到 GitHub。

---

## 二、文件结构

```
week03_day04/
├── main.py              # FastAPI 入口
├── database.py          # 数据库连接配置
├── models.py            # ORM 模型
├── schemas.py           # Pydantic 数据模型
├── routers/
│   └── users.py         # 用户路由（注册接口 + 密码哈希）
├── requirements.txt     # 依赖清单
├── .env                 # 环境变量（密码，不上传 GitHub）
├── .gitignore           # 忽略 .env 文件
└── Swagger 测试截图/     # API 测试截图
```

---

## 三、作业怎么运行

### 环境准备

1. **安装依赖**
   ```bash
   pip install fastapi uvicorn sqlalchemy pymysql python-dotenv passlib[bcrypt]
   pip install bcrypt==4.0.1
   ```

2. **创建 .env 文件**
   在 `week03_day04/` 下创建 `.env`，内容：
   ```
   DATABASE_PASSWORD=你的MySQL密码
   ```

3. **确保 .env 不上传 GitHub**
   项目根目录 `.gitignore` 里加上：
   ```
   .env
   ```

4. **清理旧表（如果结构不一致）**
   ```sql
   USE ai_class;
   DROP TABLE IF EXISTS tasks, users;
   ```

### 启动项目

```bash
cd week03_day04
source .venv/Scripts/activate
uvicorn main:app --reload
```

看到 `http://127.0.0.1:8000` 就是启动成功。

### 测试注册接口

1. 浏览器打开 `http://127.0.0.1:8000/docs`
2. 找到 **POST /users/register**，点 **Try it out**
3. 填写参数：
   ```json
   {
     "username": "xiaoling",
     "password": "123456"
   }
   ```
4. 点 **Execute**

**成功返回（Code 200）：**
```json
{"id": 0, "username": "xiaolin"}
```

**用户名已存在（Code 400）：**
```json
{"detail": "Username already registered"}
```

---

## 四、我遇到的问题 & 我是怎么解决的

### 问题 1：main.py 导入路径写错
**现象：** 写了 `from homework.week03_day04.database import Base`，运行时报错 `No module named 'homework'`。  
**解决：** 改成相对导入：`from models import Base` 和 `from database import engine`。

### 问题 2：忘记加自动建表代码
**现象：** 删完旧表后启动项目，数据库没有自动创建 `users` 和 `tasks` 表。  
**解决：** 在 `main.py` 里加上 `Base.metadata.create_all(bind=engine)`，放在 `app = FastAPI()` 之后。

### 问题 3：`app = FastAPI` 少了括号
**现象：** 写成了 `app = FastAPI`，运行时报错或行为异常。  
**解决：** 改成 `app = FastAPI()`，加括号创建实例。

### 问题 4：数据库密码直接写在代码里，担心上传 GitHub 泄露
**现象：** `database.py` 里直接写了明文密码，害怕提交到 GitHub 后被别人看到。  
**解决：**
1. 创建 `.env` 文件存密码
2. `database.py` 里用 `python-dotenv` 加载，通过 `os.getenv("DATABASE_PASSWORD")` 读取
3. `.gitignore` 里加上 `.env`，确保不上传

### 问题 5：不知道 .gitignore 怎么配置
**现象：** 不清楚怎么让 Git 忽略 `.env` 文件。  
**解决：** 在 Trae 里打开项目根目录的 `.gitignore` 文件，检查里面有没有 `.env`，没有就加上一行。

### 问题 6：bcrypt 版本兼容性问题（导致 500 错误）
**现象：** 注册接口返回 500，终端报错：
- `(trapped) error reading bcrypt version`
- `AttributeError: module 'bcrypt' has no attribute '__about__'`
- `ValueError: password cannot be longer than 72 bytes`  
**解决：** 安装兼容版本 `pip install bcrypt==4.0.1`，然后重启 uvicorn。

### 问题 7：不知道如何在 MySQL 里执行 DROP TABLE
**现象：** 不清楚在哪里输入和执行删表 SQL。  
**解决：** 在 Trae 的 Database 面板里，右键 `ai_class` 数据库 → New Query，打开 SQL 输入框执行 `DROP TABLE IF EXISTS tasks, users;`。

### 问题 8：uvicorn 命令报错
**现象：**
1. 粘贴命令时带入了垃圾字符 `[200~`
2. 运行时报 `command not found`，因为依赖没安装  
**解决：**
1. 手动输入命令，不要粘贴
2. 先执行 `pip install fastapi uvicorn sqlalchemy pymysql python-dotenv passlib[bcrypt]` 安装依赖
3. 确认虚拟环境已激活（终端前有 `(.venv)`）

### 问题 9：routers/users.py 大量拼写错误
**现象：** 手写代码时出现各种拼写错误：`CrytContext`（少 p）、`schmes`（少 e）、`Userponse`（少 Re）、`if _name_ == _main_`（下划线数量不对）、`db,close()`（逗号）、`Colummn`（多 m）等。  
**解决：** 逐字检查代码，对照正确写法修正。以后注意 Python 大小写敏感、下划线数量、标点符号。

---



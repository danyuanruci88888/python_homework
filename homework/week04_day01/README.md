# Week04 Day01 Git 规范提交练习

## 1. Git 是什么

Git 是一个分布式版本控制系统，可以理解成项目的"时间机器"。

每次提交代码，Git 都会记录一次项目状态。以后代码写坏了，可以回退到之前的版本。多人协作时，也能看到每个人做了什么修改。

## 2. 今天学了什么

今天主要学习了以下内容：

- **Git 初始化**：用 `git init` 把普通文件夹变成 Git 仓库。
- **Git 提交**：用 `git add` 把文件加入暂存区，用 `git commit -m "提交信息"` 正式提交。
- **规范提交信息**：提交信息要让别人一眼看懂，比如 `feat:`、`fix:`、`docs:`、`chore:` 等前缀。
- **分次提交**：不要把所有功能一次性提交完，完成一个功能就提交一次。
- **.gitignore**：用来告诉 Git 哪些文件不要提交，比如虚拟环境、缓存文件、数据库密码文件。

## 3. 本项目提交记录

本项目一共提交了 5 次：

| 次数 | 提交信息 | 说明 |
|---|---|---|
| 1 | `chore: 初始化项目结构并添加 .gitignore` | 配置项目基础环境 |
| 2 | `feat: 添加数据库连接和 SQLAlchemy 模型` | 创建数据库和模型 |
| 3 | `feat: 添加用户注册、登录和 JWT 认证模块` | 实现用户认证 |
| 4 | `feat: 添加任务 CRUD 接口并集成到主应用` | 实现任务管理 |
| 5 | `docs: 补充 README 和 Swagger 测试截图` | 完善项目文档 |

## 4. 哪一次提交最重要

我觉得第 1 次提交最重要。

因为 `.gitignore` 配置好了之后，虚拟环境、缓存文件、数据库密码都不会被提交到 Git 中。这是项目安全的基础，也是真实工作中必须养成的习惯。如果没有这一步，后面代码写得再好，也可能把敏感信息泄露出去。

## 5. 作业怎么运行

```bash
# 1. 进入项目代码目录
cd 项目代码

# 2. 创建并激活虚拟环境
python -m venv .venv
source .venv/Scripts/activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置数据库密码
echo DATABASE_PASSWORD=你的密码 > .env

# 4. 启动服务
uvicorn main:app --reload
```

启动后访问：`http://127.0.0.1:8000/docs`

## 6. 遇到的问题和解决方法

### 问题 1：复制代码时命令写错

**现象：** 输入 `cp -r week03_day05_project/* week04_day01/` 时报错 `No such file or directory`。

**原因：** 第一次是 `*` 通配符展开失败，第二次直接把 `cp` 写成了 `cd`。

**解决：** 改用 `cp -r week03_day05_project/. week04_day01/` 复制整个目录内容。

### 问题 2：`services` 文件夹拼写错误

**现象：** 输入 `git add service/` 和 `git add service/` 都报错 `pathspec 'service/' did not match any files`。

**原因：** 文件夹实际叫 `services`（末尾有 s），我少写了 s。

**解决：** 改成 `git add services` 就成功了。

### 问题 3：`git commit` 时忘记闭合引号

**现象：** 输入 `git commit -m "feat: 添加用户注册和登录以及 JWT 认证模块` 后，终端一直显示 `>`，没有返回值。

**原因：** 提交信息最后的右引号 `"` 没有写，Git 以为命令还没结束。

**解决：** 按 `Ctrl + C` 取消当前命令，重新输入完整的 `git commit -m "feat: 添加用户注册、登录和 JWT 认证模块"`。

### 问题 4：漏提交了一个文件

**现象：** 第三次提交后，发现漏了 `routers/auth.py` 没有提交进去。

**原因：** 当时只 add 了 `schemas.py`、`services/`、`routers/users.py`，忘记 add `routers/auth.py`。

**解决：** 用 `git reset --soft HEAD~1` 撤回最后一次提交，重新把所有相关文件 add 进去，再重新 commit。



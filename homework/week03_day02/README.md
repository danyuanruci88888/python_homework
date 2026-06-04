# Week03 Day02 - SQL 增删改查
## 今天学了什么
今天正式开始写 SQL，学习了数据库的四个核心操作 CRUD：
- **CRUD 是什么：
​** Create（INSERT 新增）、Read（SELECT 查询）、Update（UPDATE 修改）、Delete（DELETE 删除）。任务管理系统本质上就是围绕数据做这四件事。
- **创建数据库和表：
​** 学会用 `CREATE DATABASE` 创建数据库，用 `CREATE TABLE` 建表，并设置字段类型、主键、外键等约束。
- **INSERT 新增：
​** 向 `users` 表和 `tasks` 表插入用户和任务数据。
- **SELECT 查询：
​** 用 `SELECT * FROM` 查询所有数据，用 `WHERE` 条件筛选特定用户的任务。
- **UPDATE 修改：
​** 把某条任务的状态从 `todo` 改成 `done`。- **DELETE 删除：​** 删除指定 id 的任务。- **WHERE 为什么重要：​** `WHERE` 是限定操作范围的条件。`UPDATE` 和 `DELETE` 如果不加 `WHERE`，会把整张表的数据全部修改或删除，且无法恢复，非常危险。

## 文件结构
week03_day02/
├── day02_crud.sql     # 完整 SQL 脚本，包含建表、增删改查
├── README.md          # 本文件
└── 数据库运行截图.png  # 命令行运行结果截图

## 作业怎么运行
本机环境：Windows 系统，MySQL 8.0，使用 Trae 编辑器 + MySQL 插件。
**方式一（推荐）：在 Trae 中运行**1. 打开 `day02_crud.sql` 文件2. 全选代码（`Ctrl + A`）3. 点击右上角"执行（不解析）"按钮，所有语句按顺序执行
**方式二：在命令行中运行
      bashmysql -u root -p
登录后执行：
sql复制
USE ai_class;
SELECT * FROM users;
SELECT * FROM tasks;

## 遇到了什么问题
1.MySQL 未安装：​ 一开始运行 mysql --version 报错 CommandNotFoundException，发现本机没有安装 MySQL。
2.安装时数据库初始化失败：​ MySQL 安装过程中 Initializing database 步骤出现红叉，安装没有完全成功。
3.密码错误导致登录失败：​ 出现 ERROR 1045: Access denied for user 'root'@'localhost'，无法登录数据库。
4.重复插入报错：​ 多次运行脚本时出现 Duplicate entry 'fake_hash_xiaolin' for key 'users.password_hash'，数据重复插入报错。
5.No database selected 报错：​ USE ai_class 语句没有生效，导致建表时提示未选择数据库。
6.最容易写错的 SQL：​ INSERT INTO 语句，容易把表名 users 写成 user，以及漏写末尾的分号。

我是怎么解决的

1.安装 MySQL：​ 去官网下载 Windows MSI 安装包，重新安装 MySQL 8.0，并手动将 bin 目录添加到系统环境变量。
2.重置 root 密码：​ 通过 mysqld --skip-grant-tables 跳过密码验证启动 MySQL，进入后用 ALTER USER 重置了 root 密码。
3.解决重复插入报错：​ 在 SQL 脚本开头加上 DROP TABLE IF EXISTS tasks; DROP TABLE IF EXISTS users;，每次运行前先清空旧表，再重新建表插入数据。
4.解决 No database selected：​ 把 USE ai_class; 全部改为大写，并配合全选执行，确保 USE 在建表之前生效。
5.修复 SQL 笔误：​ 仔细检查并修正了 PRIMAPY（应为 PRIMARY）、NUIQUE（应为 UNIQUE）、user（应为 users）等多处拼写错误，以及补全了缺失的分号。
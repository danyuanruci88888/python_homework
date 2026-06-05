# Week03 Day03 - SQL 查询进阶

## 一、今天学了什么

今天学习了数据库的进阶查询操作，主要包括以下内容：

### 1. 排序 ORDER BY
用 `ORDER BY` 对查询结果进行排序：
- `DESC` 表示倒序（从新到旧），比如查看最新创建的任务
- `ASC` 表示正序（从旧到新），比如查看最早创建的任务

### 2. 分页 LIMIT / OFFSET
用 `LIMIT` 控制每次返回多少条数据，配合 `OFFSET` 实现"翻页"效果：
- `LIMIT 3` = 只拿前 3 条
- `LIMIT 3 OFFSET 3` = 跳过前 3 条，再拿 3 条（也就是第 2 页）

**分页为什么重要？**
想象一本电话簿有 10 万条记录，如果一次性全部显示出来，电脑会卡死，人也看不过来。分页就像是把电话簿拆成一页一页的，每次只看 10 条、20 条，想看下一页就翻一页，既省资源又看得清楚。

### 3. 模糊搜索 LIKE
用 `LIKE` 配合 `%` 进行模糊搜索，不需要标题完全一模一样，只要包含关键词就能找到：
- `%Python%` = 标题里随便哪个位置有"Python"三个字都能搜到
- `%SQL%` = 标题里带"SQL"的都能搜到

### 4. JOIN 关联查询
把两张表按照某个相同的信息（比如用户编号）拼在一起查。

**JOIN 是为了解决什么问题？**
`tasks` 任务表里只存了 `user_id`（用户编号），没有存用户名。如果想在查任务的时候顺便看到是谁的任务，就要把 `tasks` 表和 `users` 表"拼"在一起。JOIN 就是干这个事的——让两张表的信息合到一张结果里显示。

打个比方：作业登记本上只写了学号，没写名字。JOIN 就是自动把学号对应的名字从花名册上抄过来，让你一眼就能看清楚。

### 5. 事务 TRANSACTION
把多个操作打包成"一套"，用 `START TRANSACTION` 开始，`COMMIT` 确认生效，`ROLLBACK` 撤销反悔。

**事务适合什么场景？**
事务适合那种"必须一起做，不能做一半"的操作。最典型的例子就是转账：
- 从 A 账户扣 100 块
- 给 B 账户加 100 块

这两步必须一起成功。如果只扣了 A 的钱，B 没收到，那 100 块就凭空消失了，出大问题！

事务就是保证：要么两步都成功（`COMMIT`），要么两步都不算数（`ROLLBACK`），绝不允许做一半。

**事务的流程口诀：**
> `START TRANSACTION` = 铺上草稿纸（临时记录）  
> `UPDATE` = 在草稿纸上写修改  
> `COMMIT` = 签字盖章，正式生效（再也不能反悔）  
> `ROLLBACK` = 撕掉草稿纸，全部作废（必须在盖章之前用）

---

## 二、文件结构

```
week03_day03/
├── day03_query.sql         # 完整 SQL 查询脚本
├── README.md               # 本文件
└── 查询结果截图/            # SQL 运行结果截图
```

---

## 三、作业怎么运行

本机环境：Windows 系统，MySQL 8.0，使用 Trae 编辑器 + MySQL 插件。

**方式一（推荐）：在 Trae 中运行**
1. 打开 `day03_query.sql` 文件
2. 选中想要执行的某一段 SQL（鼠标拖蓝）
3. 点击语句左侧或右上角的"执行（Run）"按钮
4. 下方会弹出结果标签页（Result1、Result2 等），点击切换查看不同查询的结果

**方式二：在命令行中运行**
```bash
mysql -u root -p
```
登录后执行：
```sql
USE ai_class;
SOURCE D:/xuexi/AI/python_homework/homework/week03_day03/day03_query.sql;
```

> **注意字段名：** `week03_day02` 建表时把时间字段写成了 `creatd_at`（拼写错误），本文件使用的是标准写法 `created_at`。运行前请先执行以下语句修正字段名：
> ```sql
> ALTER TABLE tasks CHANGE creatd_at created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
> ```

---

## 四、遇到了什么问题

### 问题 1：字段名拼写不一致
`week03_day02` 建表时把时间字段写成了 `creatd_at`（少了一个字母 `e`），但教程和作业里用的是标准写法 `created_at`。导致一开始执行排序查询时报错：`Unknown column 'created_at'`。

### 问题 2：SQL 语法缺少空格
自己手写 SQL 时容易漏掉空格：
- `SELECT *FROM tasks`（`*` 和 `FROM` 之间没空格）
- `WHERE title LIKE'%python%'`（`LIKE` 和 `%` 之间没空格）

虽然有时候 MySQL 也能跑，但养成加空格的习惯更规范。

### 问题 3：JOIN 查询中字段名引用错误
在写 JOIN 查询时，想把用户名也查出来，但一开始写成了 `tasks.username`，报错说找不到这个字段。后来又写成了 `tasks.users.username`，还是报错。

原因是没有理解清楚：`username` 是在 `users` 那张表里的，不是在 `tasks` 表里。正确写法应该是 `users.username`。

### 问题 4：执行 UPDATE / 事务后看不到变化
执行完事务（`START TRANSACTION` → `UPDATE` → `COMMIT`）之后，以为 IDE 会自动显示修改后的最新数据，但结果表格里还是老样子。

后来发现：IDE 不会自动刷新结果，必须自己再执行一次 `SELECT * FROM tasks` 才能看到最新的状态。

### 问题 5：ROLLBACK 在 COMMIT 之后执行无效
执行完事务并 `COMMIT` 之后，又执行了 `ROLLBACK`，但数据没有恢复原样。

后来才明白：`ROLLBACK` 只能在 `COMMIT` 之前执行。一旦点了 `COMMIT`（签字盖章），事务就已经正式生效了，这时候再 `ROLLBACK` 就没用了。就像网购付款后不能再简单"取消订单"一样。

### 问题 6：LIKE 模糊搜索返回空结果
执行 `WHERE title LIKE '%Python%'` 时，返回空结果。原因是数据库里现有的任务标题中没有带"Python"的。这不是 SQL 写错了，而是数据本身的问题。

---

## 五、我是怎么解决的

### 解决字段名问题
使用 `ALTER TABLE` 语句把 `creatd_at` 改名为 `created_at`：
```sql
ALTER TABLE tasks CHANGE creatd_at created_at DATETIME DEFAULT CURRENT_TIMESTAMP;
```
改完后用 `DESCRIBE tasks;` 验证，确认字段名已经变过来了。

### 解决 SQL 空格问题
重新检查并修正了所有缺少空格的 SQL 语句：
- `SELECT * FROM tasks`
- `WHERE title LIKE '%python%'`

### 解决 JOIN 字段引用错误
理解了"哪张表里的字段就用哪张表的名字"：
- `tasks.id`、`tasks.title`、`tasks.status` 是任务表里的，用 `tasks.` 开头
- `users.username` 是用户表里的，用 `users.` 开头

最终正确的 JOIN 查询：
```sql
SELECT
    tasks.id,
    tasks.title,
    tasks.status,
    users.username
FROM tasks
JOIN users ON tasks.user_id = users.id;
```

### 解决"看不到变化"的问题
记住了口诀：**改完要查，不然白搭！**

执行 UPDATE 或事务之后，必须自己再执行一次 `SELECT * FROM tasks` 才能看到最新状态。IDE 不会自动刷新给你看。

### 解决 ROLLBACK 时机问题
理解了事务的完整流程：`START TRANSACTION` → 修改 → `COMMIT` 或 `ROLLBACK`。

`ROLLBACK` 必须在 `COMMIT` 之前使用。一旦 `COMMIT` 确认生效，数据就真的改了，再想恢复只能手动写 UPDATE 改回去。

### 解决 LIKE 空结果问题
明白了 `LIKE` 是"包含"的意思，数据里没有 Python 相关任务只是数据问题，SQL 语法本身是正确的。如果需要看到结果，可以先插入几条带"Python"关键词的测试数据。

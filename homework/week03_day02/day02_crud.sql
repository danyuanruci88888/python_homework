CREATE DATABASE IF NOT EXISTS ai_class;
USE ai_class;

DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;


CREATE TABLE IF NOT EXISTS users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL ,
    create_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tasks(
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL,
    user_id INT NOT NULL,
    creatd_at DATETIME DEFAULT  CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

INSERT INTO users(username,password_hash)
VALUES('xiaolin','fake_hash_xiaolin');

INSERT INTO users(username,password_hash)
VALUES ('xiaoling','fake_hash_xiaoling');

INSERT INTO tasks (title,status,user_id)
VALUES ('学习 SQL 增删改查','todo',1);

INSERT INTO tasks (title,status,user_id)
VALUES ('完成数据库表设计作业','todo',1);

INSERT INTO tasks (title,status,user_id)
VALUES ('复习外键概念','todo',2);

INSERT INTO tasks (title,status,user_id)
VALUES ('练习 SELECT 查询','todo',2);

INSERT INTO tasks (title,status,user_id)
VALUES ('提交 week03 作业','todo',1);

SELECT * FROM users;

SELECT * FROM tasks;

SELECT * FROM tasks WHERE user_id = 1;

UPDATE tasks
SET status = 'done'
WHERE id = 1;

DELETE FROM tasks
WHERE id = 5;
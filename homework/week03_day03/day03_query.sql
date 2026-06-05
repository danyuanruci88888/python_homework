USE  ai_class

SELECT * FROM tasks
ORDER BY created_at DESC
LIMIT 5;

SELECT * FROM tasks
ORDER BY created_at ASC
LIMIT 5;

SELECT *FROM tasks
LIMIT 3;

SELECT *FROM tasks
LIMIT 3 OFFSET 3;

SELECT *FROM tasks
WHERE title LIKE '%python%';

SELECT *FROM tasks
WHERE title LIKE '%sql%';

SELECT 
    tasks.id,
    tasks.title,
    tasks.status,
    users.username
FROM tasks
JOIN users ON tasks.user_id = users.id;

START TRANSACTION;

UPDATE tasks SET status = 'doing' WHERE id = 1;
UPDATE tasks SET status = 'done' WHERE id = 2;

COMMIT;


SELECT * FROM tasks;

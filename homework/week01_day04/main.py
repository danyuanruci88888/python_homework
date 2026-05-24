from task_storage import load_tasks,add_task,save_tasks,show_tasks

tasks = load_tasks()
add_task(tasks,"学习JSON文件保存")
save_tasks(tasks)
show_tasks(tasks)
print("保存完成")
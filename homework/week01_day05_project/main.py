# from task_storage import load_tasks, show_tasks, add_task, complete_task, show_menu

# def main():
#     tasks = load_tasks()
#     while True:
#         show_menu()
#         choice = input("请选择：")
#         if choice == "1":
#             show_tasks(tasks)
#         elif choice == "2":
#             add_task(tasks)
#         elif choice == "3":
#             complete_task(tasks)
#         elif choice == "0":
#             print("再见！")
#             break
#         else:
#             print("无效输入，请重新选择")

# main()


from task_storage import load_tasks, show_tasks, add_task, complete_task, show_menu

def main():
    tasks = load_tasks()
    while True:
            show_menu()
            choice = input("请选择:")
            if choice == "1":
                show_tasks(tasks)
            elif choice == "2":
               add_task(tasks)
            elif choice == "3":
                complete_task(tasks)
            elif choice == "0":
                print ("再见!")
                break
            else:
                print("无效输入,请重新选择")

main ()
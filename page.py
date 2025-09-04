print("Welcome to your To Do List App")

task_list = []

def add_task():
    task_to_add = input("What task would you like to add?")
    task_list.append(task_to_add)
    print(f" {task_to_add} has been added to your To Do List")

def view_task():
    if task_list == True:
        for i, t in enumerate(task_list, start = 1):
            print(f"{i}. {t}")
    else:
        print("You don't have any tasks in your task list yet")

def delete_task():
    view_task()
    try:
        task_to_delete = int(input("Please write the number of the task you would like to delete: "))
        removed_task = task_list.pop(task_to_delete - 1)
        print(f"{removed_task} has been deleted")
    except(IndexError, ValueError):
        print("Please make sure your typing the right number")

def quit_app():
    print("Goodbye!")
    exit()

while True:
    choice = input("""
    Please enter which task you would like to perform from the options below:
    1. Add Task
    2. View Task
    3. Delete Task
    4. Quit
    > """).strip().lower()

    if choice in ["1", "add", "add task", "1.add task"]:
        add_task()
    elif choice in ["2", "view", "view task", "2. view task"]:
        view_task()
    elif choice in ["3", "delete", "delete task", "3. delete task"]:
        delete_task()
    elif choice in ["4", "quit", "quit task", "4. quite task"]:
        quit_app()
    else:
        print("I don't understand what you entered. Try entering only the number of the task you would like to perform")




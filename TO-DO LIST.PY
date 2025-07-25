# todo_cli.py

todo_list = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for index, task in enumerate(todo_list):
            status = "Done" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['title']} [{status}]")

def add_task():
    title = input("Enter task title: ")
    todo_list.append({"title": title, "completed": False})
    print("Task added successfully.")

def complete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to mark as completed: ")) - 1
        todo_list[task_num]["completed"] = True
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid input.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter task number to delete: ")) - 1
        del todo_list[task_num]
        print("Task deleted successfully.")
    except (IndexError, ValueError):
        print("Invalid input.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        complete_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Please select a valid option.")

def main():
    task_list = []

    while True:
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. View Tasks")
        print("6. Sort Tasks")
        print("7. Exit")

        try:
            Eingabe = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if Eingabe == 1:
            add_task(task_list)
        elif Eingabe == 2:
            edit_task(task_list)
        elif Eingabe == 3:
            delete_task(task_list)
        elif Eingabe == 4:
            mark_task_completed(task_list)
        elif Eingabe == 5:
            view_tasks(task_list)
        elif Eingabe == 6:
            sort_tasks(task_list)
        elif Eingabe == 7:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_task(task_list):
    task = input("Enter new task: ")
    task_list.append({'task': task, 'completed': False})
    print("Task added.")

def edit_task(task_list):
    view_tasks(task_list)
    try:
        index = int(input("Enter task number to edit: ")) - 1
        if 0 <= index < len(task_list):
            new_task = input("Enter new task description: ")
            task_list[index]['task'] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task(task_list):
    view_tasks(task_list)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(task_list):
            task_list.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def mark_task_completed(task_list):
    view_tasks(task_list)
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(task_list):
            task_list[index]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks found.")
    else:
        for idx, task in enumerate(task_list, 1):
            status = "Done" if task['completed'] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")

def sort_tasks(task_list):
    task_list.sort(key=lambda x: (x['completed'], x['task']))
    print("Tasks sorted (Pending first, then alphabetical).")

if __name__ == "__main__":
    main()

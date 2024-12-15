# A simple to-do list app

# Initialize an empty list to store tasks
tasks = []

def view_tasks():
    """Function to view all tasks"""
    if len(tasks) == 0:
        print("No tasks to show!")
    else:
        for i, task in enumerate(tasks, 1):
            status = '✔' if task['completed'] else '✘'
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    """Function to add a new task"""
    task_title = input("Enter the task: ")
    tasks.append({"title": task_title, "completed": False})
    print(f"Task '{task_title}' added!")

def complete_task():
    """Function to mark a task as completed"""
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Task '{tasks[task_num - 1]['title']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    """Function to delete a task"""
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task['title']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    """Main menu to navigate the app"""
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a new task")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main_menu()

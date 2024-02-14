import json
from datetime import datetime, timedelta

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to add a new task
def add_task(tasks, task_name, priority, due_date):
    new_task = {
        "name": task_name,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{task_name}' added successfully.")

# Function to remove a task
def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['name']}' removed successfully.")
    else:
        print("Invalid task index.")

# Function to mark a task as completed
def mark_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['name']}' marked as completed.")
    else:
        print("Invalid task index.")

# Function to display tasks in a list
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Task List:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']} - Status: {status}")

# Main function to run the application
def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, task_name, priority, due_date)

        elif choice == "2":
            task_index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, task_index)

        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: ")) - 1
            mark_completed(tasks, task_index)

        elif choice == "4":
            display_tasks(tasks)

        elif choice == "5":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")
main()
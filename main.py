import json
import os
from datetime import datetime

def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, default=str)

def add_task(tasks):
    task = input("Enter a new task: ")
    priority = input("Enter priority (High, Medium, Low): ")
    due_date = input("Enter due date (DD-MM-YYYY): ") # idk why you would want MM-DD-YYYY
    category = input("Enter category: ")
    tasks.append({
        'task': task,
        'completed': False,
        'priority': priority,
        'due_date': due_date,
        'category': category
    })

def remove_task(tasks):
    list_tasks(tasks)
    task_no = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks.pop(task_no)

def mark_task_completed(tasks):
    list_tasks(tasks)
    task_no = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_no < len(tasks):
        tasks[task_no]['completed'] = True

def edit_task(tasks):
    list_tasks(tasks)
    task_no = int(input("Enter task number to edit: ")) - 1
    if 0 <= task_no < len(tasks):
        task = tasks[task_no]
        task['task'] = input(f"Enter new task description (current: {task['task']}): ") or task['task']
        task['priority'] = input(f"Enter new priority (current: {task['priority']}): ") or task['priority']
        task['due_date'] = input(f"Enter new due date (current: {task['due_date']}): ") or task['due_date']
        task['category'] = input(f"Enter new category (current: {task['category']}): ") or task['category']

def list_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i+1}. {task['task']} - {status} - Priority: {task['priority']} - Due: {task['due_date']} - Category: {task['category']}")

def search_tasks(tasks, keyword):
    results = [task for task in tasks if keyword.lower() in task['task'].lower()]
    for i, task in enumerate(results):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i+1}. {task['task']} - {status} - Priority: {task['priority']} - Due: {task['due_date']} - Category: {task['category']}")

def main():
    filename = 'tasks.json'
    tasks = load_tasks(filename)
    while True:
        print("\nTo-Do List Manager")
        print("1. Add task")
        print("2. Remove task")
        print("3. Mark task as completed")
        print("4. Edit task")
        print("5. List tasks")
        print("6. Search tasks")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            edit_task(tasks)
        elif choice == '5':
            list_tasks(tasks)
        elif choice == '6':
            keyword = input("Enter keyword to search: ")
            search_tasks(tasks, keyword)
        elif choice == '7':
            save_tasks(filename, tasks)
            break
        else:
            print("I don't know what that choice is...")

if __name__ == "__main__":
    main()

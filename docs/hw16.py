import json

FILE_NAME = "tasks.json"

# Load tasks from file
try:
    with open(FILE_NAME, "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


def add_task():
    description = input("Enter task description: ")

    while True:
        priority = input("Enter priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            break
        print("Invalid priority. Try again.")

    task_id = max(t["id"] for t in tasks) + 1 if tasks else 1

    task = {
        "id": task_id,
        "description": description,
        "priority": priority,
        "status": "pending"
    }

    tasks.append(task)
    print("Task added successfully!")


def list_tasks():
    if not tasks:
        print("No tasks available.")
        return

    order = {"high": 0, "medium": 1, "low": 2}

    sorted_tasks = sorted(
        tasks,
        key=lambda t: order[t["priority"]]
    )

    print("\n------ TO-DO LIST ------")
    for task in sorted_tasks:
        print(
            f"ID: {task['id']} | "
            f"Task: {task['description']} | "
            f"Priority: {task['priority']} | "
            f"Status: {task['status']}"
        )
    print()


def mark_done():
    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID to mark as done: "))

        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                print("Task marked as done!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    if not tasks:
        print("No tasks available.")
        return

    try:
        task_id = int(input("Enter task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                print("Task deleted successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")


def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        mark_done()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        save_tasks()
        print("Tasks saved to tasks.json")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

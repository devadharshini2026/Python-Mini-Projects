import os

TODO_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from file."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


def save_tasks(tasks):
    """Save tasks to file."""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))


def show_tasks(tasks):
    """Display tasks."""
    if not tasks:
        print("\n✅ No tasks found!")
        return
    print("\n=== To-Do List ===")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def menu():
    """Main menu loop."""
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("✅ Task added!")

        elif choice == "3":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to mark done: "))
                tasks[num - 1] = f"✔️ {tasks[num - 1]}"
                save_tasks(tasks)
                print("🎉 Task marked as done!")
            except (ValueError, IndexError):
                print("❌ Invalid task number.")

        elif choice == "4":
            show_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"🗑️ Deleted: {removed}")
            except (ValueError, IndexError):
                print("❌ Invalid task number.")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    menu()

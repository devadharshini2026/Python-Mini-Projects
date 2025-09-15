import os

TODO_FILE = "tasks.txt"


def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]


def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n=== To-Do List ===")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def main():
    tasks = load_tasks()

    while True:
        print("\nOptions: [add] [done] [list] [exit]")
        choice = input("Enter choice: ").lower()

        if choice == "add":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "done":
            show_tasks(tasks)
            try:
                idx = int(input("Enter task number to mark done: ")) - 1
                tasks.pop(idx)
                save_tasks(tasks)
            except (ValueError, IndexError):
                print("Invalid selection!")
        elif choice == "list":
            show_tasks(tasks)
        elif choice == "exit":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()

# Simple To-Do List App

tasks = []

def show_menu():
    print("\n==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("✅ Task added!")

def view_tasks():
    if len(tasks) == 0:
        print("📭 No tasks yet.")
    else:
        print("\n📋 Your Tasks:")
        for i in range(len(tasks)):
            print(f"{i+1}. {tasks[i]}")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return

    try:
        number = int(input("Enter task number to delete: "))
        removed = tasks.pop(number - 1)
        print(f"❌ Deleted: {removed}")
    except:
        print("⚠ Invalid input!")

# Main program loop
while True:
    show_menu()
    choice = input("Choose (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("⚠ Please choose a valid option!")

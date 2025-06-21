import json
import os

class ToDoList:
    def __init__(self, filename='todo_data.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_name):
        task = {"task": task_name, "done": False}
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "✔️ Done" if task['done'] else "❌ Not Done"
            print(f"{i}. {task['task']} [{status}]")

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['done'] = True
            self.save_tasks()
            print("✅ Task marked as done.")
        else:
            print("⚠️ Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"🗑️ Task '{deleted['task']}' deleted.")
        else:
            print("⚠️ Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            todo.view_tasks()
        elif choice == '2':
            task_name = input("Enter the task: ")
            todo.add_task(task_name)
        elif choice == '3':
            todo.view_tasks()
            index = int(input("Enter task number to mark as done: ")) - 1
            todo.mark_done(index)
        elif choice == '4':
            todo.view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(index)
        elif choice == '5':
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()

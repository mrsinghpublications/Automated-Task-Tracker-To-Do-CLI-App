import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Tasks ko JSON file se load karta hai."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    """Tasks ko JSON file mein save karta hai."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "title": title, "status": "Pending"}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task Add ho gaya: '{title}'")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("ℹ️ Abhi koi task nahi hai.")
        return
    print("\n📋 AAPKE TASKS:")
    print("-" * 40)
    for task in tasks:
        status_icon = "✔️" if task["status"] == "Completed" else "⏳"
        print(f"[{task['id']}] {task['title']} - {status_icon} {task['status']}")
    print("-" * 40)

def mark_completed(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            save_tasks(tasks)
            print(f"🎉 Task #{task_id} complete mark ho gaya hai!")
            return
    print("❌ Task ID nahi mili.")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == len(updated_tasks):
        print("❌ Task ID nahi mili.")
    else:
        # Re-index task IDs
        for index, task in enumerate(updated_tasks, start=1):
            task["id"] = index
        save_tasks(updated_tasks)
        print(f"🗑️ Task #{task_id} delete kar diya gaya hai.")

def main():
    while True:
        print("\n--- 🐍 PYTHON TASK MANAGER ---")
        print("1. Naya Task Add Karein")
        print("2. Sabhi Tasks Dekhein")
        print("3. Task Completed Mark Karein")
        print("4. Task Delete Karein")
        print("5. Exit")
        
        choice = input("Apna option chunein (1-5): ").strip()

        if choice == "1":
            title = input("Task ka naam daalein: ").strip()
            if title:
                add_task(title)
            else:
                print("❌ Task ka naam khali nahi ho sakta!")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_id = int(input("Kom sa task complete ho gaya? (ID daalein): "))
                mark_completed(task_id)
            except ValueError:
                print("❌ Sahi number daalein.")
        elif choice == "4":
            view_tasks()
            try:
                task_id = int(input("Kaun sa task delete karna hai? (ID daalein): "))
                delete_task(task_id)
            except ValueError:
                print("❌ Sahi number daalein.")
        elif choice == "5":
            print("👋 Bye! Program band ho raha hai.")
            break
        else:
            print("❌ Galat option! Phir se try karein.")

if __name__ == "__main__":
    main()

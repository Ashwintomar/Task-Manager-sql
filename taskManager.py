import sqlite3

# Initialize the database connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date DATE
    )
''')
conn.commit()

def add_task(title, description, due_date):
    cursor.execute('INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)',
                   (title, description, due_date))
    conn.commit()

def view_tasks():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Due Date: {task[3]}")

def delete_task(task_id):
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()

def main():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(title, description, due_date)
            print("Task added successfully!")

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
            print("Task deleted successfully!")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()
    print("Task Manager closed.")

if __name__ == '__main__':
    main()

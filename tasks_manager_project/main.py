from task import Task
from admin_task import AdminTask
from task_manager import TaskManager
from notifications import Notifications
from datetime import datetime


def main():
    task_manager = TaskManager()
    # Load tasks from file system
    task_manager.load_tasks()

    while True:
        # The options menu showing the possible selections
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. Search Task")
        print("4. Mark Task as Completed")
        print("5. Admin Options")
        print("6. Exit")

        # Get user's input about their choice
        choice = input("Enter your choice: ")

        # Option 1 adds a task to the task list
        if choice == "1":
            task = Task.get_task_details()
            task_manager.add_task(task)

        # Option 2 lists all tasks
        elif choice == "2":
            tasks = task_manager.get_all_tasks()
            if tasks:
                for task in tasks:
                    print(task)
            else:
                print("No tasks found.")

        # Option 3 searched by ID, NAME or DEADLINE
        elif choice == "3":
            search_type = input(
                "Insert which parameter to searh by - ID, NAME, or DEADLINE: "
            ).upper()
            task = None
            if search_type == "ID":
                task_id = int(input("Enter task ID: "))
                task = task_manager.find_task(task_id=task_id)
            if search_type == "NAME":
                name = input("Enter task name: ")
                task = task_manager.find_task(name=name)
            if search_type == "DEADLINE":
                deadline_str = input("Enter deadline (YYYY-MM-DD): ")
                deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
                task = task_manager.find_task(deadline=deadline)

            # Print the task or tasks if found
            if task:
                print(task)
            else:
                print("Task not found.")

        # Option 4 marks a task as completed, by changing the value from
        # False to True
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as completed: "))
            if task_manager.mark_task_as_completed(task_id):
                print("Task marked as completed.")
            else:
                print("Task not found.")

        # Option for the ADMIN functionality.
        elif choice == "5":
            username = input("Username: ")
            password = input("Password: ")
            if AdminTask.check_admin_status(username, password):
                print("Admin Logged in")
                while True:
                    print("1. Extend Deadline")
                    print("2. Delete Task")
                    print("3. Review Completed Tasks")
                    print("4. Logout")
                    admin_choice = input("Choose an option: ")

                    # This enables extending a task's deadline
                    if admin_choice == "1":
                        task_id = int(input("Task ID: "))
                        task = task_manager.find_task(task_id=task_id)
                        if task:
                            AdminTask.extend_deadline(task)
                        else:
                            print("Task not found.")

                    # This enables deleting a task
                    elif admin_choice == "2":
                        task_id = int(input("Task ID: "))
                        task = task_manager.find_task(task_id=task_id)
                        if task:
                            task_manager.tasks.remove(task)
                            print("Task deleted.")
                        else:
                            print("Task not found.")

                    # This enables marking a task as "REVIEWED"
                    elif admin_choice == "3":
                        for task in task_manager.get_all_tasks():
                            AdminTask.review_completed_task(task)

                    # Exit option from the admin menu.
                    elif admin_choice == "4":
                        break
                    else:
                        print("Invalid choice. Please choose again.")
            else:
                print("Invalid credentials.")

        # Quit the program and save the "File_System.txt" file
        elif choice == "6":
            task_manager.save_tasks()  # Save tasks to file system
            print("Exiting Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose again.")

        Notifications.send_reminders(task_manager)  # Send reminders
        Notifications.check_deadlines(task_manager)  # Check missed deadlines


if __name__ == "__main__":
    main()

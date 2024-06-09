from datetime import datetime


class Notifications:
    # A function to generate a reminder message of approaching deadline
    def send_reminders(task_manager):
        now = datetime.now().date()  # Convert to datetime.date object
        for task in task_manager.get_all_tasks():
            if not task.completed and task.reminder and task.reminder <= now:
                print(
                    f"Reminder: Task '{task.name}' is approaching its deadline at {task.deadline}"
                )

    # A function to generate a notification message of missed deadline
    def check_deadlines(task_manager):
        now = datetime.now().date()  # Convert to datetime.date object
        for task in task_manager.get_all_tasks():
            if not task.completed and task.deadline <= now:
                print(
                    f"Notification: Task '{task.name}' has missed its deadline!"
                )

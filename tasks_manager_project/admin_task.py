from task import Task
from datetime import datetime, timedelta


# the class inherits from the Task class
class AdminTask(Task):
    def __init__(self, name, description, deadline, reminder=None):
        super().__init__(name, description, deadline, reminder)
        self.is_admin = True

    # check admin credentials - user and password. Default to "ADMIN" and "password"
    def check_admin_status(username, password):
        user_name = username.strip().upper()
        password_input = password.strip().lower()
        if user_name == "ADMIN" and password_input == "password":
            print("Admin access granted.")
            return True
        else:
            print("Either your username or password is wrong!")
            return False

    # The function to extend the deadline by 3 days if deadline is close.
    def extend_deadline(task, additional_days=3):
        if isinstance(task.deadline, str):
            task.deadline = datetime.strptime(task.deadline, "%Y-%m-%d").date()

        if (task.deadline - datetime.now().date()).days <= 1:
            extend = (
                input("Do you want to extend the deadline by 3 days? Y or N? ")
                .strip()
                .upper()
            )
            if extend == "Y":
                task.deadline += timedelta(days=additional_days)
                print(f"Deadline extended to: {task.deadline}")
                return True
            else:
                print("Deadline not extended.")
                return False
        else:
            print("Deadline is not due yet.")
            return False

    # A function to mark a task as "REVIEWED"
    def review_completed_task(self):
        if self.completed and not self.description.endswith("- REVIEWED"):
            self.description += "- REVIEWED"
            print(f"Task {self.task_id} marked as REVIEWED.")
        elif self.completed and self.description.endswith("- REVIEWED"):
            self.description
            print(f"Task {self.task_id} has already been REVIEWED.")
        else:
            pass

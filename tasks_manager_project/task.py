from datetime import (
    datetime,
    timedelta,
)  # Needed for the deadline calculations


class Task:
    # I want an ID counter to start from 1 and increment for each new task created
    task_id_counter = 1

    # The constructor
    def __init__(
        self,
        name="",
        description="",
        deadline=datetime.today().date(),
        reminder=None,
    ):
        self.name = name
        self.description = description
        self.deadline = deadline
        # The reminder can be left blank and will default to 2 days before deadline
        self.reminder = reminder if reminder else deadline - timedelta(days=2)
        # Initially all tasks are incomplete after creation
        self.completed = False
        # Incrementing the ID counter
        self.task_id = Task.task_id_counter
        Task.task_id_counter += 1

    # The function to get the task details.
    def get_task_details():
        name = input("Provide task name: ")
        description = input("Provide task description: ")
        deadline_str = input("Provide task deadline (YYYY-MM-DD): ")
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        reminder_str = input(
            "Provide reminder time before deadline in days (optional, press enter to skip): "
        )
        reminder = None
        if reminder_str:
            reminder_days = int(reminder_str)
            reminder = deadline - timedelta(days=reminder_days)
        return Task(name, description, deadline, reminder)

    # Representation of the object as a string
    def __str__(self):
        return (
            f"Task ID: {self.task_id}\nName: {self.name}\nDescription: {self.description}\n"
            f"Deadline: {self.deadline}\nReminder: {self.reminder}\nCompleted: {self.completed}"
        )

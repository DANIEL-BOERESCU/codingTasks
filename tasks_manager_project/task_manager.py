from datetime import datetime
from task import Task


class TaskManager:
    # I initialize the tasks list as an empty list first
    def __init__(self):
        self.tasks = []

    # Function to add task to the tasks list
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    # Function to list all tasks
    def get_all_tasks(self):
        return self.tasks

    # Function to search for a task by task_id, name, or deadline.
    def find_task(self, task_id=None, name=None, deadline=None):
        for task in self.tasks:
            if task_id is not None and task.task_id == task_id:
                return task
            elif name is not None and task.name == name:
                print(task)
            elif deadline is not None and task.deadline == deadline:
                print(task)
        return None

    # Function to mark a task as completed, based on the task_id
    def mark_task_as_completed(self, task_id):
        task = self.find_task(task_id=task_id)
        if task:
            task.completed = True
            self.save_tasks()
            return True
        else:
            return False

    # Function to save tasks to a file
    def save_tasks(self):
        with open("File_System.txt", "w") as file:
            for task in self.tasks:
                file.write(str(task) + "\n")

    # Function to get the tasks from a file
    def load_tasks(self):
        self.tasks = []
        try:
            with open("File_System.txt", "r") as file:
                task_lines = file.readlines()
                for i in range(
                    0, len(task_lines), 6
                ):  # Assuming 6 lines per each task
                    task_data = {}
                    for j in range(6):
                        line = task_lines[i + j].strip()
                        key, value = line.split(": ", 1)
                        task_data[key] = value

                    # Loading each task properly to be viewed
                    # correctly
                    task = Task(
                        name=task_data["Name"],
                        description=task_data["Description"],
                        deadline=datetime.strptime(
                            task_data["Deadline"], "%Y-%m-%d"
                        ).date(),
                        reminder=(
                            datetime.strptime(
                                task_data["Reminder"], "%Y-%m-%d"
                            ).date()
                            if task_data["Reminder"] != "None"
                            else None
                        ),
                    )
                    task.task_id = int(task_data["Task ID"])
                    task.completed = task_data["Completed"] == "True"
                    # Appending to the tasks list
                    self.tasks.append(task)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading tasks: {e}")

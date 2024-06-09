import unittest
from datetime import datetime, timedelta
from task import Task


class TestTask(unittest.TestCase):

    def test_task_creation_default(self):
        task = Task()
        today = datetime.today().date()
        self.assertEqual(task.name, "")
        self.assertEqual(task.description, "")
        self.assertEqual(task.deadline, today)
        self.assertEqual(task.reminder, today - timedelta(days=2))
        self.assertFalse(task.completed)
        self.assertEqual(task.task_id, 1)

    def test_task_string_representation(self):
        task = Task(
            name="Sample Task",
            description="Sample Description",
            deadline=datetime(2024, 12, 31).date(),
        )
        expected_str = (
            f"Task ID: {task.task_id}\nName: {task.name}\nDescription: {task.description}\n"
            f"Deadline: {task.deadline}\nReminder: {task.reminder}\nCompleted: {task.completed}"
        )
        self.assertEqual(str(task), expected_str)


if __name__ == "__main__":
    unittest.main()

import unittest
from datetime import datetime
from task import Task
from task_manager import TaskManager
import os


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.task_manager = TaskManager()
        self.task1 = Task(
            name="Task 1",
            description="Description 1",
            deadline=datetime(2024, 12, 31).date(),
        )
        self.task2 = Task(
            name="Task 2",
            description="Description 2",
            deadline=datetime(2024, 11, 30).date(),
        )
        self.task_manager.add_task(self.task1)
        self.task_manager.add_task(self.task2)

    def tearDown(self):
        if os.path.exists("File_System.txt"):
            os.remove("File_System.txt")

    def test_add_task(self):
        task = Task(
            name="Task 3",
            description="Description 3",
            deadline=datetime(2024, 10, 31).date(),
        )
        self.task_manager.add_task(task)
        self.assertIn(task, self.task_manager.get_all_tasks())

    def test_get_all_tasks(self):
        tasks = self.task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn(self.task1, tasks)
        self.assertIn(self.task2, tasks)

    def test_find_task_by_id(self):
        task = self.task_manager.find_task(task_id=self.task1.task_id)
        self.assertEqual(task, self.task1)

    def test_mark_task_as_completed(self):
        result = self.task_manager.mark_task_as_completed(self.task1.task_id)
        self.assertTrue(result)
        self.assertTrue(self.task1.completed)

    def test_save_tasks(self):
        self.task_manager.save_tasks()
        self.assertTrue(os.path.exists("File_System.txt"))

    def test_load_tasks(self):
        self.task_manager.save_tasks()
        new_task_manager = TaskManager()
        new_task_manager.load_tasks()
        tasks = new_task_manager.get_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0].name, "Task 1")
        self.assertEqual(tasks[1].name, "Task 2")


if __name__ == "__main__":
    unittest.main()

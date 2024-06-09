import unittest
from datetime import datetime, timedelta
from admin_task import AdminTask
from task import Task


class TestAdminTask(unittest.TestCase):

    def setUp(self):
        Task.task_id_counter = (
            1  # Resetting the task_id_counter for consistency in tests
        )

    def test_admin_task_creation(self):
        deadline = datetime(2024, 12, 31).date()
        admin_task = AdminTask(
            name="Admin Task",
            description="Admin Task Description",
            deadline=deadline,
        )
        self.assertEqual(admin_task.name, "Admin Task")
        self.assertEqual(admin_task.description, "Admin Task Description")
        self.assertEqual(admin_task.deadline, deadline)
        self.assertTrue(admin_task.is_admin)
        self.assertEqual(admin_task.task_id, 1)

    def test_check_admin_status_valid(self):
        self.assertTrue(AdminTask.check_admin_status("ADMIN", "password"))

    def test_check_admin_status_invalid(self):
        self.assertFalse(AdminTask.check_admin_status("USER", "password"))
        self.assertFalse(
            AdminTask.check_admin_status("ADMIN", "wrongpassword")
        )

    def test_extend_deadline(self):
        task = AdminTask("Test Task", "Description", datetime.now().date())
        original_deadline = task.deadline
        task.deadline = original_deadline
        self.assertTrue(AdminTask.extend_deadline(task))
        self.assertEqual(task.deadline, original_deadline + timedelta(days=3))

    def test_review_completed_task(self):
        admin_task = AdminTask(
            name="Review Task",
            description="Review Description",
            deadline=datetime(2024, 12, 31).date(),
        )
        admin_task.completed = True
        admin_task.review_completed_task()
        self.assertIn("REVIEWED", admin_task.description)


if __name__ == "__main__":
    unittest.main()

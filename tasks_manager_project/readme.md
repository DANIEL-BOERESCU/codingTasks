Table of contents for the "Task Manager" readme:
  - Description of the "Task Manager" program
  - Note about "requirements.txt"
  - How to use the program
  - Credits

I am building a "Task Manager" program project using OOP modules.

Structure:
A class Task allows the user to create tasks by getting input for name, description, deadline, reminder, completed.
Deadline is of type DATE, reminder is of type DATE and if not set by the user it will be defaulted to 48 hrs before deadline.
Completed is a BOOL and initially when creating new tasks, it will be set as FALSE by default.

Another class AdminTask would have extra Admin privileges, such as delete tasks, extend deadlines, review completed tasks.
Class AdminTask inherits from class Task.
There is a function implementation to check whether the user is an ADMIN or not.
If user is ADMIN, then a user_name (default "ADMIN") and password (default "password") need to be supplied in order to access the admin menu.
Once credentials are correctly provided, the ADMIN is able to access the functionality of the class AdminTask, and can extend the task deadline, delete a task, review completed tasks.

A class Task Manager allows the user to add a task to the task list, to get the list of all tasks, to search and display a particular task based on the task_ID, or name, or deadline.
The class Task Manager will also allow users to mark tasks as completed, and it also has functionality to interact with the storage file. 

A File System module has to enable read and write from a storage file of type .txt, named "File_System.txt". 
Once tasks are created, they are added / written to the text file.
Once the user makes a query the File System the file is read to allow retrieval of the required information.

A Notifications class would send a reminder of approaching deadline one day before deadline, plus a notification of any missed deadlines. 

The main.py file operates the program when run.

The purpose of this task was to help us learn the importance of OOP Modules by establishing a robust foundation that ensures code quality, maintainability, and collaboration.
The main advantages of OOP Modules are:
  - modularisation by encapsulating classes, functions and other variables within modules, ensuring code is organized and reusable
  - separation of concerns,
  - maintainability.

Please refer to the "requirements.txt" for any packages that need to be installed to run the program.

How to use the program

Main.py file will prompt these options when it is accessed/ run.
![Task Manager Menu](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/22ef4c81-ade5-44f5-8537-880b94442444)

Selecting Option 1. Add Task, allows adding a new task:
![Option 1](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/85f97916-3dfe-48cb-986f-e8165583abf5)

Creating or having tasks with approaching deadline will trigger a Reminder and a Notification for failed tasks:
![Reminder and Notification](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/a4b6c187-d7d1-443b-890c-99cba4adee35)

Selecting Option 2. List all tasks, displays all tasks in the storage file:
![Option 2](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/2d058d23-20ae-4c87-b00f-1744ff03b9a3)

Selecting Option 3. Search Task, allows for search based on ID, NAME or DEADLINE of a task:
![Option 3](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/e039460e-58f7-4839-9825-4a3ddf964d51)

Selecting Option 4. Mark Task as Completed, allows to mark a task as completed:
![Option 4](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/6f2888ac-c7ed-44f0-8a09-8a8cd70e7869)

If Option 2 is selected again after Option 4, the task with ID 4 would appear as Completed - “Completed: True”:
![Confimation of task marked as COMPLETED](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/43ff4777-3ca3-45ba-a98e-3e4357b5e2a1)

Selecting Option 5. Admin Options, prompts for input of the user and password credentials to be granted access. Once done, a submenu appears with options accessible only to an admin user:
![Option 5](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/c5e93960-8827-4bb9-9ea8-256613a258c5)

Selecting Admin Option 1. Extend Deadline, allows the admin to extend the deadline of a task if it is close enough, or has passed.
![Admin Option 1 deadline extended](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/9093b35e-543b-4d4c-9ddb-bb4e078045df)

Otherwise a message is diplayed saying: "Deadline is not due yet."
![Admin Option 1](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/25d9025f-3104-402b-85bc-91d756508784)
    
Selecting Admin Option 2. Delete Task, allows the admin to delete a task
![Admin Option 2](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/e95454d1-8847-42d8-aa28-53d5cecb46af)

Selecting Admin Option 3. Review Completed Tasks, allows the admin to mark a completed task as REVIEWED, by adding “- REVIEWED” at the end of the task name. Once it’s been reviewed previously, the code displays “Task {ID} has already been REVIEWED.”
![Admin Option 3](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/9d8cf868-77d4-40be-bf1d-bf94a3378eb3)

Selecting Admin Option 4. Logout - allows the admin to exit the admin submenu and return to the main menu.

Finally, selecting Option 6. Exit in the main menu, quits the program and saves all the changes to the "File_System.txt" file that contains the stored tasks.
![Exit program](https://github.com/DANIEL-BOERESCU/codingTasks/assets/164760774/64cf9381-734c-4be5-ae74-d599768c9db3)

Credits:
![HiperionDev / CoGrammar -](https://www.hyperiondev.com/)




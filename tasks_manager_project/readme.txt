I am building a task manager project using modules.

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

The main file operates the program when run.

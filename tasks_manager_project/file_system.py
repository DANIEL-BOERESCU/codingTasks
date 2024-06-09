class FileSystem:
    # The function for reading tasks from the "File_System.txt" file
    def read_tasks(file_name="File_System.txt"):
        tasks = []
        try:
            with open(file_name, "r") as file:
                for line in file:
                    tasks.append(eval(line.strip()))
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error reading tasks: {e}")
        return tasks

    # The function for writing tasks to the "File_System.txt" file
    def write_tasks(tasks, file_name="File_System.txt"):
        with open(file_name, "w") as file:
            for task in tasks:
                file.write(str(task) + "\n")

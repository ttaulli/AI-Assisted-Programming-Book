# src/models.py

# Define the Task class to represent individual tasks
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"Task: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\n"

# Define the TodoList class to represent a collection of tasks
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks

    def __str__(self):
        if len(self.tasks) == 0:
            return "No tasks in the to-do list."
        else:
            tasks_str = ""
            for task in self.tasks:
                tasks_str += str(task) + "\n"
            return tasks_str
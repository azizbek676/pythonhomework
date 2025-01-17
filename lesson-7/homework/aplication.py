import json
import csv
from abc import ABC, abstractmethod

class Task:
    def __init__(self, name, completed=False, due_date=None):
        self.name = name
        self.completed = completed
        self.due_date = due_date

    def __str__(self):
        return f"Task: {self.name}, Completed: {self.completed}, Due: {self.due_date}"

class FileHandler(ABC):
    @abstractmethod
    def load_tasks(self, filename):
        """Load tasks from the specified file."""
        pass
    
    @abstractmethod
    def save_tasks(self, tasks, filename):
        """Save tasks to the specified file."""
        pass

class CSVFileHandler(FileHandler):
    def load_tasks(self, filename):
        tasks = []
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task = Task(name=row['name'], completed=row['completed'] == 'True', due_date=row['due_date'])
                    tasks.append(task)
        except FileNotFoundError:
            print(f"{filename} not found, starting with an empty task list.")
        return tasks

    def save_tasks(self, tasks, filename):
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['name', 'completed', 'due_date']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for task in tasks:
                writer.writerow({'name': task.name, 'completed': task.completed, 'due_date': task.due_date})

class JSONFileHandler(FileHandler):
    def load_tasks(self, filename):
        tasks = []
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for task_data in data:
                    task = Task(name=task_data['name'], completed=task_data['completed'], due_date=task_data['due_date'])
                    tasks.append(task)
        except FileNotFoundError:
            print(f"{filename} not found, starting with an empty task list.")
        return tasks

    def save_tasks(self, tasks, filename):
        with open(filename, 'w') as file:
            data = [{'name': task.name, 'completed': task.completed, 'due_date': task.due_date} for task in tasks]
            json.dump(data, file, indent=4)

class ToDoApp:
    def __init__(self, file_handler: FileHandler):
        self.tasks = []
        self.file_handler = file_handler

    def add_task(self, name, completed=False, due_date=None):
        task = Task(name, completed, due_date)
        self.tasks.append(task)

    def remove_task(self, name):
        self.tasks = [task for task in self.tasks if task.name != name]

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def save_tasks(self, filename):
        self.file_handler.save_tasks(self.tasks, filename)

    def load_tasks(self, filename):
        self.tasks = self.file_handler.load_tasks(filename)
file_handler = CSVFileHandler()  
app = ToDoApp(file_handler)
app.load_tasks('tasks.csv') 
app.add_task('Buy groceries', completed=False, due_date='2025-01-18')
app.add_task('Finish homework', completed=False, due_date='2025-01-20')
print("All tasks:")
app.list_tasks()
app.save_tasks('tasks.csv') 
app.remove_task('Buy groceries')
print("\nTasks after removal:")
app.list_tasks()

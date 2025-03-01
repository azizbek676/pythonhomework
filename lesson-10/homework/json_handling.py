import json 
import csv

def load_tasks(file):
    with open(file) as f:
        return json.load(f)

def save_tasks(file, tasks):
    with open(file, 'w') as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    for t in tasks:
        print(f"{t['id']}: {t['task']} - {'T' if t['completed'] else 'X'} (Priority: {t['priority']})")

def calculate_stats(tasks):
    total, completed = len(tasks), sum(t['completed'] for t in tasks)
    print(f"Total: {total}, Completed: {completed}, Pending: {total - completed}, Avg Priority: {sum(t['priority'] for t in tasks) / total:.1f}")

def convert_to_csv(json_file, csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        writer.writerows([[t['id'], t['task'], t['completed'], t['priority']] for t in load_tasks(json_file)])
tasks = load_tasks('tasks.json')
display_tasks(tasks)
calculate_stats(tasks)
convert_to_csv('tasks.json', 'tasks.csv')

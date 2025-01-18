import json
import csv
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    except FileNotFoundError:
        print("tasks.json file not found.")
        return []
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)
def display_tasks(tasks):
    print(f"{'ID':<5} {'Task':<20} {'Completed':<10} {'Priority':<10}")
    print('-' * 45)
    for task in tasks:
        print(f"{task['id']:<5} {task['task']:<20} {str(task['completed']):<10} {task['priority']:<10}")
def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task['completed']])
    pending_tasks = total_tasks - completed_tasks
    average_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Completion Stats:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {average_priority:.2f}")
def convert_to_csv(tasks):
    with open('tasks.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'task', 'completed', 'priority'])
        writer.writeheader()
        writer.writerows(tasks)
    print("\nTasks have been written to tasks.csv.")
def main():
    tasks = load_tasks()
    if tasks:
        display_tasks(tasks)
        calculate_statistics(tasks)
        tasks[0]['completed'] = True  
        save_tasks(tasks)
        print("\nUpdated tasks have been saved to tasks.json.")
        convert_to_csv(tasks)
    else:
        print("No tasks to process.")
if __name__ == "__main__":
    main()

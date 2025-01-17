class Employee:
    employee_registry = {} 
    def __init__(self, emp_id, name, salary):
        """Initialize the employee with a unique ID, name, and salary."""
        if emp_id in Employee.employee_registry:
            raise ValueError(f"Employee ID {emp_id} already exists.")
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        Employee.employee_registry[emp_id] = self

    def __str__(self):
        """String representation of the employee."""
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def get_all_employees(cls):
        """Return all employees."""
        return list(cls.employee_registry.values())

    @classmethod
    def sort_employees(cls, key='salary', reverse=False):
        """Sort employees by a given key ('salary' or 'name')."""
        if key == 'salary':
            return sorted(cls.get_all_employees(), key=lambda e: e.salary, reverse=reverse)
        elif key == 'name':
            return sorted(cls.get_all_employees(), key=lambda e: e.name, reverse=reverse)
        else:
            raise ValueError("Sort key must be 'salary' or 'name'.")
try:
    emp1 = Employee(1, "Alice", 50000)
    emp2 = Employee(2, "Bob", 60000)
    emp3 = Employee(3, "Charlie", 55000)
    print("All Employees:")
    for emp in Employee.get_all_employees():
        print(emp)
    print("\nEmployees sorted by salary:")
    for emp in Employee.sort_employees('salary'):
        print(emp)
    print("\nEmployees sorted by name:")
    for emp in Employee.sort_employees('name'):
        print(emp)

except ValueError as e:
    print(e)

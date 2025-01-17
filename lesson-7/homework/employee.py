import os
class Employee:
    def __init__(self, emp_id, name, title, salary):
        self.emp_id = emp_id
        self.name = name
        self.title = title
        self.salary = salary

    def display_info(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Title: {self.title}, Salary: ${self.salary}")

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.title},{self.salary}"
class EmployeeManager:
    def __init__(self, filename="employees.txt"):
        self.filename = filename
        self.employees = []
        self.load_employees()

    def load_employees(self):
        """Load employee records from file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                for line in file:
                    emp_id, name, title, salary = line.strip().split(',')
                    self.employees.append(Employee(emp_id, name, title, float(salary)))

    def save_employees(self):
        """Save employee records to file"""
        with open(self.filename, 'w') as file:
            for employee in self.employees:
                file.write(str(employee) + "\n")

    def add_employee(self, emp_id, name, title, salary):
        """Add a new employee"""
        employee = Employee(emp_id, name, title, salary)
        self.employees.append(employee)
        self.save_employees()

    def remove_employee(self, emp_id):
        """Remove an employee by ID"""
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]
        self.save_employees()

    def display_all_employees(self):
        """Display all employees"""
        if self.employees:
            for employee in self.employees:
                employee.display_info()
        else:
            print("No employees found.")

    def search_employee(self, emp_id):
        """Search for an employee by ID"""
        for employee in self.employees:
            if employee.emp_id == emp_id:
                employee.display_info()
                return
        print("Employee not found.")
def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Records Manager")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. View All Employees")
        print("4. Search Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            title = input("Enter Employee Title: ")
            salary = float(input("Enter Employee Salary: "))
            manager.add_employee(emp_id, name, title, salary)

        elif choice == '2':
            emp_id = input("Enter Employee ID to remove: ")
            manager.remove_employee(emp_id)

        elif choice == '3':
            manager.display_all_employees()

        elif choice == '4':
            emp_id = input("Enter Employee ID to search: ")
            manager.search_employee(emp_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

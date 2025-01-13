import os
FILE_NAME = "employee_records.txt"
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")
    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id},{name},{department},{salary}\n")
    print("Employee record added successfully.")
def display_employees():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return

    with open(FILE_NAME, "r") as file:
        records = file.readlines()
        if records:
            print("Employee ID | Name | Department | Salary")
            print("-" * 50)
            for record in records:
                emp_id, name, department, salary = record.strip().split(',')
                print(f"{emp_id} | {name} | {department} | {salary}")
        else:
            print("No employee records found.")
def update_employee():
    emp_id = input("Enter the Employee ID to update: ")
    found = False
    updated_records = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        for record in records:
            record_data = record.strip().split(',')
            if record_data[0] == emp_id:
                found = True
                print(f"Current Record: {record.strip()}")
                name = input("Enter new name (leave empty to keep the same): ") or record_data[1]
                department = input("Enter new department (leave empty to keep the same): ") or record_data[2]
                salary = input("Enter new salary (leave empty to keep the same): ") or record_data[3]
                updated_records.append(f"{emp_id},{name},{department},{salary}\n")
            else:
                updated_records.append(record)

        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record updated successfully.")
        else:
            print("Employee ID not found.")
    else:
        print("No employee records found.")
def delete_employee():
    emp_id = input("Enter the Employee ID to delete: ")
    found = False
    updated_records = []
    
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        for record in records:
            if record.split(',')[0] != emp_id:
                updated_records.append(record)
            else:
                found = True
        
        if found:
            with open(FILE_NAME, "w") as file:
                file.writelines(updated_records)
            print("Employee record deleted successfully.")
        else:
            print("Employee ID not found.")
    else:
        print("No employee records found.")
def main_menu():
    while True:
        print("\nEmployee Records Manager")
        print("1. Add New Employee")
        print("2. Display All Employees")
        print("3. Update Employee Record")
        print("4. Delete Employee Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main_menu()

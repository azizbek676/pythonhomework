import csv
def read_grades(file_name):
    grades = []
    with open(file_name, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grades.append({
                'Name': row['Name'],
                'Subject': row['Subject'],
                'Grade': int(row['Grade'])
            })
    return grades
def calculate_average_grades(grades):
    subject_grades = {}
    for grade in grades:
        subject = grade['Subject']
        if subject not in subject_grades:
            subject_grades[subject] = []
        subject_grades[subject].append(grade['Grade'])
    average_grades = []
    for subject, grades_list in subject_grades.items():
        average = sum(grades_list) / len(grades_list)
        average_grades.append({
            'Subject': subject,
            'Average Grade': round(average, 2)  
        })
    
    return average_grades
def write_average_grades(file_name, average_grades):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Subject', 'Average Grade'])
        writer.writeheader()
        writer.writerows(average_grades)
    print(f"Average grades have been written to {file_name}")
def main():
    grades = read_grades('grades.csv')
    average_grades = calculate_average_grades(grades)
    write_average_grades('average_grades.csv', average_grades)
if __name__ == "__main__":
    main()

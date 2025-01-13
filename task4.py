def enrollment_stats():
    universities = []
    while True:
        name = input("Enter universities name or enter the exit: ")
        if name.lower() == 'exit':
            break
        enrollment = int(input(f"{name} number of students: "))
        tuition = int(input(f"{name} university study cost: "))
        universities.append([name, enrollment, tuition])
    
    student_enrollments = []
    tuition_fees = []
    
    for university in universities:
        student_enrollments.append(university[1])  
        tuition_fees.append(university[2])  
    return student_enrollments, tuition_fees
def mean(values):
    return sum(values) / len(values)
def median(values):
    values.sort()  
    n = len(values)
    if n % 2 == 1:  
        return values[n // 2]
    else:  
        mid1 = values[n // 2 - 1]
        mid2 = values[n // 2]
        return (mid1 + mid2) / 2
student_enrollments, tuition_fees = enrollment_stats()
total_students = sum(student_enrollments)
total_tuition = sum(tuition_fees)
mean_students = mean(student_enrollments)
median_students = median(student_enrollments)

mean_tuition = mean(tuition_fees)
median_tuition = median(tuition_fees)
print(f"Total number of students: {total_students}")
print(f"Total tuition fees: ${total_tuition}")
print(f"Average number of students: {mean_students}")
print(f"Median number of students: {median_students}")
print(f"Average tuition fee: ${mean_tuition}")
print(f"Median tuition fee: ${median_tuition}")
import csv
from collections import defaultdict

def read_grades(filename):
    with open(filename, newline='') as csvfile:
        return [{**row, 'Grade': int(row['Grade'])} for row in csv.DictReader(csvfile)]

def calculate_average(grades):
    subjects = defaultdict(list)
    for row in grades:
        subjects[row['Subject']].append(row['Grade'])
    return {s: sum(g)/len(g) for s, g in subjects.items()}

def write_averages(filename, averages):
    with open(filename, 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows([["Subject", "Average Grade"]] + [[s, round(a, 1)] for s, a in averages.items()])

grades = read_grades('grades.csv')
write_averages('average_grades.csv', calculate_average(grades))
print("Averages saved to 'average_grades.csv'")

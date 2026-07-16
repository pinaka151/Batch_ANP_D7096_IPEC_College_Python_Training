# Student Result Management

students = {}

# Input details of 10 students
for i in range(10):
    roll = input("Enter Roll Number: ")
    marks = float(input("Enter Marks: "))
    students[roll] = marks

# Find topper
topper = max(students, key=students.get)
print("\nTopper Roll Number:", topper)
print("Topper Marks:", students[topper])

# Find average marks
average = sum(students.values()) / len(students)
print("Average Marks:", average)

# Display students scoring above average
print("\nStudents Scoring Above Average:")
for roll, marks in students.items():
    if marks > average:
        print("Roll No:", roll, "Marks:", marks)

# Count failed students
failed = 0
for marks in students.values():
    if marks < 35:
        failed += 1

print("Number of Failed Students:", failed)

# Display grades
print("\nStudent Grades:")
for roll, marks in students.items():

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 35:
        grade = "D"
    else:
        grade = "Fail"

    print("Roll No:", roll, "Marks:", marks, "Grade:", grade)
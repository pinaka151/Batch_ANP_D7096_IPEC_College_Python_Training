'''------------------------------ Student Marks Management -------------------------------------'''

# Dictionary of student names and marks
marks = {
    "karan": 34,
    "lokesh": 23,
    "brijesh": 78,
    "radhe": 99,
    "shyam": 98
}

# Display all students and their marks
print("Student Marks:")
for key in marks:
    print(f"{key} : {marks[key]}")

# Add a new student
name = input("\nEnter new student name: ")
score = int(input("Enter marks: "))
marks[name] = score

print("\nAfter Adding Student:")
print(marks)

# Update marks of an existing student
name = input("\nEnter student name to update: ")

if name in marks:
    score = int(input("Enter new marks: "))
    marks[name] = score
    print("Marks updated successfully.")
else:
    print("Student not found.")

print("\nAfter Updating:")
print(marks)

# Delete a student
name = input("\nEnter student name to delete: ")

if name in marks:
    del marks[name]
    print("Student deleted successfully.")
else:
    print("Student not found.")

print("\nAfter Deleting:")
print(marks)

# Find the highest scorer
high = 0
top_student = ""

for key in marks:
    if marks[key] > high:
        high = marks[key]
        top_student = key

print("\nHighest Scorer")
print("Student Name :", top_student)
print("Marks :", high)
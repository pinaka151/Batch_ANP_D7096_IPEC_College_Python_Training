# Tuple Operations

students = (
    "Aman", "Riya", "Rahul", "Priya", "Neha",
    "Karan", "Simran", "Arjun", "Pooja", "Rohan",
    "Ankit", "Sneha", "Rahul", "Meena", "Ravi"
)

# Count total students
print("Total Students:", len(students))

# Display first five students
print("First Five Students:", students[:5])

# Display last five students
print("Last Five Students:", students[-5:])

# Search a student name
name = input("Enter student name to search: ")

if name in students:
    print(name, "is present in the tuple.")
else:
    print(name, "is not present in the tuple.")

# Count occurrences of a given name
search_name = input("Enter student name to count: ")
print("Occurrences of", search_name, ":", students.count(search_name))

# Convert tuple into list and sort alphabetically
student_list = list(students)
student_list.sort()

print("Students in Alphabetical Order:")
print(student_list)
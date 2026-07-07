'''----------------------Dictionary Search System----------------------'''

# Function to search student
def search_student(student_dict, roll_no):

    if roll_no in student_dict:
        return student_dict[roll_no]

    else:
        return "Student Not Found"


# Create Dictionary
dict = {}

# Accept details of 5 students
for i in range(5):

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    dict[roll_no] = name


print("\nStudent Dictionary")
print(dict)


# Search Student
search_roll = input("\nEnter Roll Number to Search: ")

result = search_student(dict, search_roll)

print("Result :", result)
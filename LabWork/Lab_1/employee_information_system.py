'''----------------------Employee Information System----------------------'''

# Create an empty dictionary
dict = {}

Adding = True

# Taking employee details
while (Adding):

    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_department = input("Enter Employee Department: ")
    emp_salary = float(input("Enter Employee Salary: "))

    dict[emp_id] = {
        "Name": emp_name,
        "Department": emp_department,
        "Salary": emp_salary
    }

    user_choice = input("Do you want to add more employees: ")

    if(user_choice.lower() == "yes"):
        Adding = True
    else:
        Adding = False


# Display all employee details
print("\nDisplay all Employee Details")
for i in dict:
    print(i, "->", dict[i])


# Search employee using Employee ID
print("\nSearch Employee")
search_id = input("Enter Employee ID: ")

if search_id in dict:
    print(search_id, "->", dict[search_id])

else:
    print("Employee not found !!!")


# Increase salary of all employees by 10%
print("\nIncrease Salary by 10%")

for i in dict:
    dict[i]["Salary"] = dict[i]["Salary"] + (dict[i]["Salary"] * 10 / 100)

print("Updated Employee Details")

for i in dict:
    print(i, "->", dict[i])


# Display employees of a specific department
print("\nEmployees of Specific Department")

department = input("Enter Department Name: ")

count = 0

for i in dict:

    if(dict[i]["Department"].lower() == department.lower()):

        print(i, "->", dict[i])
        count += 1

if(count == 0):
    print("No Employee belongs to this department.")
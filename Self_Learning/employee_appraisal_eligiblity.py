'''----------Program to store employee details and check appraisal eligibility---------------'''

# Creating 4 empty lists to store employee data
employee_name = []
employee_id = []
employee_performance = []
employee_attandance = []

count = 0

# taking input of number of employees
number = int(input("Enter the number of employees: "))

# Taking user input of name , id ,  attandance, performance of each employee
for i in range(number):
    print(f"Enter the details of employee {i+1}")
    employee_name.append(input(f"Enter the name of Employee {i +1}: "))
    employee_id.append(int(input(f"Enter the id of Employee {i +1}: ")))
    employee_attandance.append(int(input(f"Enter the attandance of Employee {i +1} (in %): ")))
    employee_performance.append(int(input(f"Enter the performance of Employee {i +1} (out of 10): ")))

print("------------------------------------------------------------------------------------")
# validating condtion to allot Appraisal to employee
for i in range(number):
    if employee_performance[i] > 5 and employee_attandance[i] > 75 :
        print (f"Employee Name: {employee_name[i]} , Employee ID:  {employee_id[i]} , Employee Attandance: {employee_attandance[i]} , Employee Performance: {employee_performance[i]} , Appraisal Status : Eligible")
        count = count + 1        
    
if count == 0 :
    print("No employee qualifies for the appraisal.")



    ''' Output:
    Enter the details of employee 2
Enter the name of Employee 2: vaibhav
Enter the id of Employee 2: 7899
Enter the attandance of Employee 2 (in %): 45
Enter the performance of Employee 2 (out of 10): 8
Enter the details of employee 3
Enter the name of Employee 3: kartik
Enter the id of Employee 3: 567
Enter the attandance of Employee 3 (in %): 90
Enter the performance of Employee 3 (out of 10): 4
Enter the details of employee 4
Enter the name of Employee 4: suraj
Enter the id of Employee 4: 76
Enter the attandance of Employee 4 (in %): 89
Enter the performance of Employee 4 (out of 10): 5
Enter the details of employee 5
Enter the name of Employee 5: sagar
Enter the id of Employee 5: 6789
Enter the attandance of Employee 5 (in %): 56
Enter the performance of Employee 5 (out of 10): 8
------------------------------------------------------------------------------------
Employee Name: vipin , Employee ID:  789 , Employee Attandance: 78 , Employee Performance: 7 , Appraisal Status : Eligible
'''
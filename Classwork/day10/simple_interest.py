'''--------------------Program to calculate Simple Interest----------------------'''


def Calculate_Simple_Interest(principal,rate,time):
    return (principal*rate*time)/100



# Taking user input of principal, rate, time

principal = float(input("Enter the principal amount (in Rs): "))
rate = float(input("Enter the rate of interest (in %): "))
time = int(input("Enter the time  (in years): "))


# Display the simple interest
print("Simple Interest: Rs", Calculate_Simple_Interest(principal,rate, time))



'''Output: 
Enter the principal amount (in Rs): 200
Enter the rate of interest (in %): 10.25
Enter the time  (in years): 2
Simple Interest: Rs 41.0
'''
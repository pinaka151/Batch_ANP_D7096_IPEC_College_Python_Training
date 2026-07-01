''' Electricity Bill Analysis '''
# user input of units consumed in a month

houses = int(input("Enter the total number of houses: "))
if(houses <=0):
    exit("Please enter valid number")

total_consumed_units = 0
for i in range (1,houses + 1):
    user = int(input(f"Enter total units consumed in a month by user{i}:"))
    total_consumed_units += user

 


average_units_consumed = total_consumed_units/houses


print("Total number of units consumed by all users = ", total_consumed_units)

print("Average units consumed by each house: ",average_units_consumed )




















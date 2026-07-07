'''----------------------List Analysis using Functions----------------------'''

# Function to find maximum value
def find_max(numbers):

    high = numbers[0]

    for i in numbers:
        if(i > high):
            high = i

    return high


# Function to find minimum value
def find_min(numbers):

    low = numbers[0]

    for i in numbers:
        if(i < low):
            low = i

    return low


# Function to find average
def find_average(numbers):

    total = 0

    for i in numbers:
        total = total + i

    average = total / len(numbers)

    return average


# Accept 10 integers from the user
list1 = []

for i in range(10):

    num = int(input("Enter number: "))
    list1.append(num)


# Call Functions
maximum = find_max(list1)
minimum = find_min(list1)
average = find_average(list1)


# Display Results
print("\nList:", list1)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
print("Average:", average)
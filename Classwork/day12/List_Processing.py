# List Processing

numbers = []

# Accept 20 integers
for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# a) Largest number
print("Largest Number:", max(numbers))

# b) Second largest number
unique = list(set(numbers))
unique.sort()
print("Second Largest Number:", unique[-2])

# c) Smallest number
print("Smallest Number:", min(numbers))

# d) Remove duplicate elements
duplicate_removed = list(set(numbers))
print("List after removing duplicates:", duplicate_removed)

# e) Print even numbers
print("Even Numbers:", end=" ")
for i in numbers:
    if i % 2 == 0:
        print(i, end=" ")

# f) Print numbers divisible by both 3 and 5
print("\nNumbers divisible by both 3 and 5:", end=" ")
for i in numbers:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")

# g) Reverse the list without using reverse()
reversed_list = numbers[::-1]
print("\nReversed List:", reversed_list)
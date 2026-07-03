# Create a empty list
l1 = []

# Taking user input of 15 numbers
print("Enter the 15 numbers")
for i in range(15):
    user = int(input(f"{i +1} number: "))
# adding element to list
    l1.append(user)

# converting the list into tuple 
tup = tuple(l1)
print("The given tuple is: ", tup)
print("----------------------------------------------")
# validatin the program to get only odd numbes
for i in tup:
    if i % 2 != 0:
        print(i,end=" ")


'''Output: 
Enter the 15 numbers
1 number: 1
2 number: 2
3 number: 3
4 number: 4
5 number: 5
6 number: 6
7 number: 7
8 number: 8
9 number: 89
10 number: 43
11 number: 2
12 number: 3
13 number: 5
14 number: 23
15 number: 5
The given tuple is:  (1, 2, 3, 4, 5, 6, 7, 8, 89, 43, 2, 3, 5, 23, 5)
----------------------------------------------
1 3 5 7 89 43 3 5 23 5 
  '''
        


      

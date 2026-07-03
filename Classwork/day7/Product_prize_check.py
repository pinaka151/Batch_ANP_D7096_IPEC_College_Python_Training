# Taking 10 products with it's prize
tup = (
    ("Banana", 2000),
    ("Apple", 8000),
    ("Orange", 1000),
    ("Mango", 2000),
    ("Grapes", 7000),
    ("Pineapple", 1000),
    ("Watermelon", 1000),
    ("Papaya", 500),
    ("Strawberry", 5000),
    ("Kiwi", 8000)
)



# setting default max and min as first element of the tuple and count 0
max = tup[0][1]
min = tup[0][1]
count = 0


# comparing max and min value using loop also counting products having prize range above 4000
for i in range(10):
    if(tup[i][1]>4000):
        count = count + 1  
    
    if (tup[i][1]>max):
        max = tup[i][1]
    else:
        min =tup[i][1]    

# Printing the highest prize of product with it's name and prize 
for i in range(10):
    if(tup[i][1] >=max):
        print("The highest prize of product is: " , tup[i])


print("-----------------------------------------------------")

# printing highest prize and lowest prize from the tuple
print("The highest prize is: ", max)        
print("The lowest prize is: ", min)  

print("-----------------------------------------------------")


# printing the total count of products having prize more than 4000
print("The total number of products have prize greater than 4000 is: ",count)

print("-----------------------------------------------------")





'''------------output-----------------------------
The highest prize of product is:  ('Apple', 8000)
The highest prize of product is:  ('Kiwi', 8000)
-----------------------------------------------------
The highest prize is:  8000
The lowest prize is:  8000
-----------------------------------------------------
The total number of products have prize greater than 4000 is:  4
-----------------------------------------------------
'''






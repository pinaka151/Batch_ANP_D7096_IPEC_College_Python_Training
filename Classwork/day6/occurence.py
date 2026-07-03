# User input of 20 numbers and adding it to list
list = []

for i in range(20):
    num = int(input(f"Enter {i} number here: "))
    list.append(num)
    # printing the list
print("The Entered List is : ", list)



# Taking user input for counting the numbre occurencing
element = int(input("Enter the the number to count occurences: "))

print(f"Removing duplicate values of {element} ")
# Counting the occurances of the element
counting = list.count(element)




# validating the conditions whether element has duplicate values or not

if(counting == 1):
    print(f"{element} doesn't have any duplicate value")

elif (counting == 0):
    print(f"{element} is not present in the list")



else :
    # reverse the list so that we can delete the duplicate elements but  not the element which is on first occurance
    list.reverse()

    # using remove method counting -1 times so that except first element all elements are deleted
    for i in range(counting-1):
        list.remove(element)

# again reverse method so that all elements arranged in as before
list.reverse()


print(list)


                         
                         








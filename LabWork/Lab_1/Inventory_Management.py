'''--------------------------Inventory Management----------------------'''

# Create an empty dictionary
dict = {}
Adding = True # using while loop to add products , so that we can ask  user whether he wants to add more or not
while (Adding):
    user1 = input("Enter the Product name: ")
    user2 = int(input("Enter the Product stock: "))
    dict[user1] =user2
    user_choice = input("Do you want to add more items: ")
    if (user_choice.lower() == "yes"):
        Adding = True
    else:
        Adding = False    

print(dict)




# adding a new product
print("Enter new product name to  add")
new_product = input("Enter product name: ")
new_product_stock = int(input("Enter the stock: "))

dict[new_product] = new_product_stock
print(dict)


#Updating stock of an existing element
print("Update the stock of an existing element")
update_product = input("Enter product name: ")
if update_product in dict :
    update_product_stock = int(input("Enter the stock: "))
    dict[update_product] = update_product_stock

else:
    print("Product is not present !!!")   


print(dict)    

# remove a product from inventory
print("Remove an existing element")
remove_pdt = input("Enter the product name: ")
if remove_pdt in dict:
    dict.pop(remove_pdt)
    print(dict)

else:
    print("Product is not present!!!")    


# Display products having stock less than 20.
print("Display products having stock less than 20")
stock_less_20 = 0
for i in dict:
    if (dict[i] < 20):
        print(i,"->", dict[i])
        stock_less_20 +=1

if stock_less_20 == 0:
    print("No Product has stock less than 20")        



# Display the total number of items available in the inventory.  

print("Total numbers of items: ", len(dict))



'''---------------Output---------------------------------
Enter the Product name: Mouse
Enter the Product stock: 23
Do you want to add more items: yes
Enter the Product name: Keyboard
Enter the Product stock: 34
Do you want to add more items: yes
Enter the Product name: Charger
Enter the Product stock: 13
Do you want to add more items: yes
Enter the Product name: Headphone 
Enter the Product stock: 18
Do you want to add more items: no
{'Mouse': 23, 'Keyboard': 34, 'Charger': 13, 'Headphone': 18}
Enter new product name to  add
Enter product name: Ram
Enter the stock: 27
{'Mouse': 23, 'Keyboard': 34, 'Charger': 13, 'Headphone': 18, 'Ram': 27}
Update the stock of an existing element
Enter product name: ram
Product is not present !!!
{'Mouse': 23, 'Keyboard': 34, 'Charger': 13, 'Headphone': 18, 'Ram': 27}
Remove an existing element
Enter the product name: Ram
{'Mouse': 23, 'Keyboard': 34, 'Charger': 13, 'Headphone': 18}
Display products having stock less than 20
Charger -> 13
Headphone -> 18
Total numbers of items:  4
---------------------------------------------------------
'''
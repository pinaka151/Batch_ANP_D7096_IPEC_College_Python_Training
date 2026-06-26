'''------- Problem Statement: Electricity Bill Discount 

An electricity provider offers a 10% discount on the total bill amount if the customer's bill is ₹5,000 or more.
 Otherwise, no discount is applied.
  
 Write a Python program to accept the total bill amount from the user and 
 display the final amount to be paid. 
'''

# ------Coding-------

#input of bill from the user
bill = int(input("Enter the bill amount (in Rs): "))

#validate the bill
if(bill>=0):
    if(bill>=5000):
         discounted_amount = bill/10
         bill = bill - discounted_amount
         print("Your discounted bill (in Rs): ", bill)
    else:
         print("Your bill (in Rs): ",bill)

else:
     print("Please enter valid amount !!!")
     
#----------------------------------------------------
'''Output : 
Enter the bill amount (in Rs): 8762
--------------------------------------------
Your discounted bill (in Rs):  7885.8
--------------------------------------------'''



   









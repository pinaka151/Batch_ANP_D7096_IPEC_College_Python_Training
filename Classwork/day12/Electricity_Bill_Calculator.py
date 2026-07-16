# Electricity Bill Calculator

units = int(input("Enter total units consumed: "))

# Calculate bill amount
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Apply surcharge
final_bill = bill
if bill > 2000:
    final_bill = bill + (bill * 0.05)

# Apply minimum bill
if final_bill < 500:
    final_bill = 500

# Display result
print("\n----- Electricity Bill -----")
print("Total Units Consumed :", units)
print("Bill Amount          : ₹", bill)
print("Final Payable Amount : ₹", final_bill)
# importing module

import numeric_calculation

a = 5
b = 10

print(f"Sum of {a} and {b} = ",numeric_calculation.Calculation_addition(a,b))
print(f"Differnce between {a} and {b} = ",numeric_calculation.Calculation_subtraction(a,b))
print(f"Multiplication of {a} and {b} = ",numeric_calculation.Calculation_multiplication(a,b))
print(f"Divition of {a} with {b} = ",numeric_calculation.Calculation_divition(a,b))
print(f"Remainder of {a} when divide by {b} = ",numeric_calculation.Calculation_remainder(a,b))

'''-------------Output--------------------------
Sum of 5 and 10 =  15
Differnce between 5 and 10 =  -5
Multiplication of 5 and 10 =  50
Divition of 5 with 10 =  0.5
Remainder of 5 when divide by 10 =  5
------------------------------------------------
'''
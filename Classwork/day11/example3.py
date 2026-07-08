# importing module's specific content 

from numeric_calculation import Calculation_addition

a = 5
b = 10

print(f"Sum of {a} and {b} = ",Calculation_addition(a,b))
print(f"Differnce between {a} and {b} = ",Calculation_subtraction(a,b))

'''-------------Output--------------------------
Sum of 5 and 10 =  15

------error for subtraction---------------------

 print(f"Differnce between {a} and {b} = ",Calculation_subtraction(a,b))
 NameError: name 'Calculation_subtraction' is not defined. Did you mean: 'Calculation_addition'?


------------------------------------------------
'''
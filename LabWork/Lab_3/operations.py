# importing all functions from the twodfigures module
from twodfigures import *

# Initializing variable to True so that the loop starts
more = True

# Loop will continue until the user chooses to stop
while more == True:
     
     # Displaying the menu of available 2D figures
     print("To Select any twodfigures from the given menu type any one of these: Square  Circle  Triangle  Rectangle ")
     
     # Taking the user's choice of figure
     user_Choice1 = input("Enter your twodfigure Choice: ")
     
     
     # Checking if the user selected Square
     if user_Choice1.lower() == "square":
         
         # Taking the dimension of the square
         print("Enter Dimensions of a Square: ")
         side = float(input("Enter the side of square: "))
         
         # Asking whether to calculate Area or Perimeter
         user_Choice2 = input("Enter The choice between Area and Perimeter: ")
          
         # Calculating the area of the square
         if user_Choice2.lower() == "area":
             print(f"The area of a Square is = ", Area_Square(side))
         
         # Calculating the perimeter of the square
         elif user_Choice2.lower() == "perimeter":
              print(f"The perimeter of a Square is = ", Peri_Square(side))
     
     


     # Checking if the user selected Triangle
     elif user_Choice1.lower() == "triangle":
         
         # Taking the three sides of the triangle
         print("Enter Dimensions of a Triangle: ")
         side1 = float(input("Enter the side1 of Circle: "))
         side2 = float(input("Enter the side2 of Circle: "))
         side3 = float(input("Enter the side3 of Circle: "))
         
         # Asking whether to calculate Area or Perimeter
         user_Choice2 = input("Enter The choice between Area and Perimeter: ")
          
         # Calculating the area of the triangle using Heron's formula
         if user_Choice2.lower() == "area":
             print(f"The area of a triangle is = ", Area_Traingle(side1,side2,side3))
         
         # Calculating the perimeter of the triangle
         elif user_Choice2.lower() == "perimeter":
              print(f"The perimeter of a triangle is = ", Peri_Traingle(side1,side2,side3))
            
     
     
     # Checking if the user selected Rectangle
     elif user_Choice1.lower() == "rectangle":
         
         # Taking the length and breadth of the rectangle
         print("Enter Dimensions of a rectangle: ")
         length = float(input("Enter the length of Rectahgle: "))
         breadth = float(input("Enter the breadth of rectangle: "))
         
         # Asking whether to calculate Area or Perimeter
         user_Choice2 = input("Enter The choice between Area and Perimeter: ")
          
         # Calculating the area of the rectangle
         if user_Choice2.lower() == "area":
             print(f"The area of a rectangle is = ", Area_Rectangle(length,breadth))
         
         # Calculating the perimeter of the rectangle
         elif user_Choice2.lower() == "perimeter":
              print(f"The perimeter of a rectangle is = ", Peri_Rectangle(length,breadth))
     
         
     # Checking if the user selected Circle
     elif user_Choice1.lower() == "circle":
         
         # Taking the radius of the circle
         print("Enter Dimensions of a circle: ")
         radius = float(input("Enter the radius of Circle: "))
         
         # Asking whether to calculate Area or Perimeter
         user_Choice2 = input("Enter The choice between Area and Perimeter: ")
          
         # Calculating the area of the circle
         if user_Choice2.lower() == "area":
             print(f"The area of a circle is = ", Area_Circle(radius))
         
         # Calculating the circumference (perimeter) of the circle
         elif user_Choice2.lower() == "perimeter":
              print(f"The perimeter of a circle is = ", Peri_Circle(radius))    
     
     
     # Executed if the user enters an invalid figure name
     else:
         print("Enter correct Choice")


     # Asking the user whether they want to continue
     user = input("Do you want to continue?")     
     
     # If the user enters "yes", continue the loop
     if user.lower() == "yes":
         more = True

     # Otherwise, terminate the loop
     else:
         more = False
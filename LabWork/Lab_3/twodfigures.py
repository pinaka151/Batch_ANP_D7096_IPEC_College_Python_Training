
# Function to calculate the area of a circle
def Area_Circle(radius):
            # Formula: π × r²
            return 3.14*radius*radius
        
# Function to calculate the perimeter (circumference) of a circle
def Peri_Circle(radius):
         # Formula: 2 × π × r
         return 2*3.14*radius
        

# Function to calculate the area of a square
def Area_Square(side):
            # Formula: side × side
            return side*side
        
# Function to calculate the perimeter of a square
def Peri_Square(side):
            # Formula: 4 × side
            return 4*side
        

# Function to calculate the area of a rectangle
def Area_Rectangle(l,b):
            # Formula: length × breadth
            return l*b

# Function to calculate the perimeter of a rectangle
def Peri_Rectangle(l,b):
            # Formula: 2 × (length + breadth)
            return 2*(l+b)
        

# Function to calculate the area of a triangle
# (Using Heron's formula)
def Area_Traingle(side1,side2,side3,height):
            # Returns the area of the triangle
            return (side1 * (side1 - side2) * (side1 - side2) * (side1 - side3))**0.5


# Function to calculate the perimeter of a triangle
def Peri_Traingle(side1,side2,side3):
            # Formula: side1 + side2 + side3
            return side1+side2+side3




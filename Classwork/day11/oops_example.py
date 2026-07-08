class  Rectangle:
    # member variable
    length = 0
    breadth = 0

    # Method  to initialize data
    def initialize (self,l,b):
        self.length = l
        self.breadth = b
    
    
    # method to display data
    def display_data(self):
        print("-------------rectagle-----------")
        print(f"Length: {self.length} cm")
        print(f"Breadth: {self.breadth} cm")

        
# Main program
rect = Rectangle()
rect.initialize(20, 50)
rect.display_data()     
    
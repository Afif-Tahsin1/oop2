class rectangle_area:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def  rectangle_Area(self):
        return  self.length * self.width
    
l = int(input("Input the length of the rectangle: "))
w = int(input("Input the width of the rectangle: "))
rect = rectangle_area(l,w)
print(f"The area of the rectangle is {rect.rectangle_Area()}")
    
class rectangle_perimiter:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def  rectangle_perimiter(self):
        return  self.length + self.width + self.length + self.width
    
l = int(input("Input the length of the rectangle: "))
w = int(input("Input the width of the rectangle: "))
rect = rectangle_perimiter(l,w)
print(f"The perimiter of the rectangle is {rect.rectangle_perimiter()}")


    
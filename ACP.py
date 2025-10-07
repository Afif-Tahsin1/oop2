class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def circleArea(self):
        return 3.14159 * self.radius**2
    
    def circlePerimiter(self):
        return 2*3.14159*self.radius

circle = Circle(5)
print(f"The area of the circle is: {circle.circleArea()}")
print(f"The perimiter of the circle is: {circle.circlePerimiter()}")
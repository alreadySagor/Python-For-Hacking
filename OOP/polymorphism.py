# Polymorphism

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.1416 * self.radius ** 2 # Exponentiation (self.radius ** 2) means self.radius * self.radius
shapes = [Rectangle(4, 3), Circle(3)]

for shape in shapes:
    print(f"Area --> {shape.area()}")
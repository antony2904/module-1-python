#Write a function area() that works differently for Square and Rectangle classes. 
# Demonstrate method overriding for calculating area.
class  shape:

    def area(self):
        return 0


class Rectangle(shape):

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(shape):

    def __init__(self,side:float):
        self.side = side

    def area(self):
        return self.side **2

Mesurements = [Rectangle(length = 8, width = 5), Square(side=6)]

for shape in Mesurements:
    print(f"{shape.__class__.__name__} area : {shape.area()}")
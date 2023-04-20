"""
Create a class called Shape that has the following attributes and methods:

Attributes:
name (a string representing the name of the shape)
sides (an integer representing the number of sides the shape has)

Methods:
area() (returns the area of the shape)
perimeter() (returns the perimeter of the shape)

Create two subclasses of Shape called Square and Triangle. The Square class should have an additional attribute called side_length (an integer representing the length of one side of the square), while the Triangle class should have additional attributes called base (an integer representing the length of the base of the triangle) and height (an integer representing the height of the triangle).

Implement the area() and perimeter() methods for each subclass, and make sure they return the correct values. Test your implementation by creating instances of each class and calling their methods.

"""

import math

class Shape:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
class Square(Shape):
    def __init__(self, name, sides, side_length):
        super().__init__(name, sides)
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
        return self.side_length * 4
    
class Triangle(Shape):
    def __init__(self, name, sides, base, height):
        super().__init__(name, sides)
        self.base = base
        self.height = height
    
    def area(self):
        return (self.base * self.height) / 2
    
    def perimeter(self):
        a = self.base
        b = self.height
        c = math.sqrt(a**2 + b**2)
        return a + b + c

# Testing
square = Square("Square", 4, 5)
print(f"{square.name}: area = {square.area()}, perimeter = {square.perimeter()}")

triangle = Triangle("Triangle", 3, 4, 3)
print(f"{triangle.name}: area = {triangle.area()}, perimeter = {triangle.perimeter()}")




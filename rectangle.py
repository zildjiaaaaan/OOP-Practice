"""
Create a class called Rectangle with the following attributes:

length (a float): represents the length of the rectangle.
width (a float): represents the width of the rectangle.
The class should also have the following methods:

area(): returns the area of the rectangle (length times width).
perimeter(): returns the perimeter of the rectangle (twice the sum of length and width).
is_square(): returns True if the rectangle is a square (i.e., length and width are equal), otherwise returns False.

"""

class Rectangle():

    def __init__(self, len, wid):
        if len <= 0 or wid <= 0:
            raise ValueError("Values cannot be less than 0")
        self.length = len
        self.width = wid
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    def is_square(self):
        if self.length == self.width:
            return True
        return False
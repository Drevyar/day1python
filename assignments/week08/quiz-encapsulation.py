"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        
    def get_area(self):
        return self.__length * self.__width
    
    def getPerimeter(self):
        return 2 * (self.__length + self.__width)
    
    def issquare(self):
        return self.__length == self.__width
    
r = Rectangle(4, 8)
print(r.get_area())
print(r.getPerimeter())
print(r.issquare())
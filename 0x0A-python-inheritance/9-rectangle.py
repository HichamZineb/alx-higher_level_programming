#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle"""

    def __init__(self, width, height):
        """Instantiation with width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """print() should print, and str() should return"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """The area method"""

        return self.__width * self.__height

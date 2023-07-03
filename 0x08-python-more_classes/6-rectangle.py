#!/usr/bin/python3

"""class Rectangle that defines a rectangle"""


class Rectangle:
    """Define Width and Height of rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width property setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height property setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rectangle = ""
        if self.__width is 0 or self.__height is 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += "#" * self.__width + "\n"
        rectangle += "#" * self.__width

        return rectangle

    def __repr__(self):
        rectangle = "Rectangle({}, {})".format(self.__width, self.__height)
        return rectangle

    def __del__(self):
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

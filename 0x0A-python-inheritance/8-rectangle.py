#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """class rectangle"""

    def __init__(self, width, height):
        """Instantiation with width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

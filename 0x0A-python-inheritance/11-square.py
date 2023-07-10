#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiation with size"""

    def __init__(self, size):
        """set size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))

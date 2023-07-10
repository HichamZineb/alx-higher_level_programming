#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """Public instance method"""
    def area(self):
        """Raises Exception message"""
        raise Exception("area() is not implemented")

    """Public instance method"""
    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

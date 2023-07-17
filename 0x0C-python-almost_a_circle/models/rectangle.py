#!/usr/bin/python3
"""class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""

        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""

        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""

        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""

        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance."""

        return self.width * self.height

    def display(self):
        """Prints the rectangle in stdout using #"""

        for i in range(self.y):
            print()

        for j in range(self.height):
            print(" " * self.x, end="")
            print('#' * self.width)

    def __str__(self):
        """Overrides the __str__ method"""

        rec = "[Rectangle] "
        ID = "({}) ".format(self.id)
        xy = "{}/{} - ".format(self.x, self.y)
        wh = "{}/{}".format(self.width, self.height)

        return rec + ID + xy + wh

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Updates instance attributes'''

        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""

        if args:
            self.__update(*args)
        if kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns the dictionary representation Rectangle."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }

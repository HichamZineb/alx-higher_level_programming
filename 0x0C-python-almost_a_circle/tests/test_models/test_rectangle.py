#!/usr/bin/python3
"""unittest tests for rectangle.py"""

import unittest
from io import StringIO
from unittest.mock import patch
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base


class Test_rectangle(unittest.TestCase):
    """class rectangle tests"""

    def setUp(self):
        """Works before every test"""

        Base._Base__nb_objects = 0

    def test_id_rectangle(self):
        """Test id creation for rectangle"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_type(self):
        """Test if value is int"""

        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
            r2 = Rectangle(1, "2")

    def test_value(self):
        """Test if value is > 0"""

        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 1)
            r2 = Rectangle(1, -1)
            r3 = Rectangle(1, 1, -1, 0, 2)
            r4 = Rectangle(1, 2, 3, -3, 4)

    def test_area(self):
        """Test the area of the rectangle"""

        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test rectangle print in stdout"""

        r1 = Rectangle(2, 3, 2, 2)
        output = "\n\n  ##\n  ##\n  ##\n"

        with patch('sys.stdout', new=StringIO()) as xout:
            r1.display()
            self.assertEqual(xout.getvalue(), output)

    def test_str(self):
        """Test if str was overriden"""

        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)

        str1 = "[Rectangle] (12) 2/1 - 4/6"
        str2 = "[Rectangle] (1) 1/0 - 5/5"

        self.assertEqual(str(r1), str1)
        self.assertEqual(str(r2), str2)

    def test_update_args(self):
        """Test if args update was done"""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)

        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r1))

    def test_update_kwargs(self):
        """Test if kwargs update was done"""

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(id=89, x=1, height=2, y=3, width=4)

        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r1))


if __name__ == "__main__":
    unittest.main()

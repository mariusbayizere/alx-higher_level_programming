#!/usr/bin/python3
"""Define rectangle class called Rectangle"""


class Rectangle:
    """Represent a rectangle."""
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the attribute of  class Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set value to the width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """To setter value to the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """To calculate the area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the area of parameter of Rectangle"""
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        print the rectangle using # character
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        new = []
        for x in range(self.__height):
            [new.append(str(self.print_symbol)) for j in range(self.__width)]
            if x != self.__height - 1:
                new.append("\n")
        return ("".join(new))

    def __repr__(self):
        """return string concatnetion"""
        newlist = "Rectangle(" + str(self.__width)
        newlist += ", " + str(self.__height) + ")"
        return (newlist)

    def __del__(self):
        """Print the message for delete rectangle"""
        type(self).number_of_instances += 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest rectangle
        args:
            rect_1 (Rectangle): receiving the first parameter
            rect_2 (Rectangle): receiving the second paramter
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """return new rectangle with equal side
        args:
            size : receiving size which is width and height
        """
        return (cls(size, size))

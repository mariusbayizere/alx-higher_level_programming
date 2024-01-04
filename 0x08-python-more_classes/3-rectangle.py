#!/usr/bin/python3
"""Define rectangle class called Rectangle"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the attribute of  class Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
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
        """Function that has responsible for printing the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return " "
        newlist = []
        for x in range(self.__height):
            [newlist.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                newlist.append("\n")
        return ("".join(newlist))

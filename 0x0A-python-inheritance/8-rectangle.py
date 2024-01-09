#!/usr/bin/python3
"""Define the class called BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define class that enherte property of this class BaseGeometry"""
    def __init__(self, width, height):
        """initialze class Rectangle property.

        Args:
            width (int): width of the Rectangle must be integer type.
            height (int): height of the Rectangle must be integer type.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

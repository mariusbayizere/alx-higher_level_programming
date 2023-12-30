#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    Represent Square class
    """
    def __init__(self, size=0):
        """
        Initializes an instance of Square Class with a specified size.
        args:
        - size (int): The size of the instance. Should be a positive integer.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def validation_(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False

    @property
    def size(self):
        """getter the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter the size value"""
        if self.validation_(value):
            self.__size = value

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2

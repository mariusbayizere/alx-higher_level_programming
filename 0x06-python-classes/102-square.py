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

    def __eq__(self, other):
        """
        using to compare two value area() and other object
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        used to check if two value are not equal
        """
        return (self.area() != other.area())

    def __lt__(self, other):
        """
        used to check if self.area() are lessthan other.area()
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        usied to check if self.ara() are lessthan or equal
        """
        return (self.area() <= other.area())

    def __gt__(self, other):
        """
        used to compore if the self.area() are greather than
        the other.area()
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        used to compare if the self.area() are greather or
        equal to the other.area()
        """
        return (self.area() >= other.area())

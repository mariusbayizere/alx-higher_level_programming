#!/usr/bin/python3


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
    
    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2

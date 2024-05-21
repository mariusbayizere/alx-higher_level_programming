#!/usr/bin/python3


class Square:
    """
    Represent Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an instance of Square Class with a specified size.
        args:
        - size (int): The size of the instance. Should be a positive integer.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif self.position_(position):
            self.__position = position
        else:
            self.__size = size

    def validation_(self, size):
        """
        validates the size, checking for errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True

    def position_(self, position):
        """position validation """
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
        return False
    return True
    
    @property
    def position(self):
        """getter postion value"""
    return self.__position

    @position.setter
    def position(self, value):
        """setter the value to the position"""
    if self.position_(value):
        self.__position = value

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

    def my_print(self):
        """printing current square """
        y = 0
        if self.__size == 0:
            print()
            return
        y = 0
        for y in range(0, self.__position[1]):
            for y in range(0, self.__size):
                xx = 0
                for xx in range(0, self.__position[0]):
                    print(" ", end="")
                    x = 0
                    for x in range(0, self.__size):
                        print("#", end='')
                        print()

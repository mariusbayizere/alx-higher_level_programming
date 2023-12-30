#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialization function for our square clasee
        """
        if self.validation_(size):
            self.__size = size
        if self.position_size(position):
            self.__position = position

    def __str__(self):
        """
        used by print and str.
        returns a string of user friendly printable
        """
        x = 0
        string = ""
        if self.__size == 0:
            string += '\n'
            return
        for x in range(0, self.__position[1]):
            string += '\n'
        x = 0
        for x in range(0, self.__size):
            y = 0
            xx = 0
            for xx in range(0, self.__position[0]):
                string += ' '
            for y in range(0, self.__size):
                string += '#'
            string += '\n'
        return string

    @property
    def size(self):
        """
        getter for size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size attribute
        """
        if self.validation_(value):
            self.__size = value

    @property
    def position(self):
        """
        getter for position attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position attribute
        """
        if self.position_size(value):
            self.__position = value

    def area(self):
        """
        calculates the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        method that will prints the square using '#' character
        also takes into checking position
        """
        z = 0
        if self.__size == 0:
            print()
            return
        for z in range(0, self.__position[1]):
            print()
        z = 0
        for z in range(0, self.__size):
            x = 0
            xx = 0
            for xx in range(0, self.__position[0]):
                print(" ", end='')
            for x in range(0, self.__size):
                print("#", end='')
            print()

    def validation_(self, size):
        """
        validation the size, checkup for Error in the class
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False

    def position_size(self, position):
        """
        validation the position, looking for type error
        """
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        return True

#!/usr/bin/python3
"""Define class square which inhert property of the Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent class square which inherts property of this Rectangle"""

    def __init__(self, size):
        """initalize the square class .
        Args:
            size: The size of the square class.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

#!/usr/bin/python3
"""define rectangle class"""
from models.base import Base


class Rectangle(Base):
    """represent the class rectangle which inhert class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Parameters:
            - width (int): The width of the rectangle.
            - height (int): The height of the rectangle.
            - x (int, optional): The x-coordinate of the top-left corner.
            - y (int, optional): The y-coordinate of the top-left corner.
            - id (any, optional): An identifier for the rectangle.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set value the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """TO set value to the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """To get value of the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """to setter to value to x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """To get value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """to setting value to the y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """funtion that will calculate the area of the rectangle"""
        return self.height * self.width

    def to_dictionary(self):
        """function that will return dictionary of the Square class."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }

    def display(self):
        """Display Rectangle using the # character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for p in range(self.y)]
        for z in range(self.height):
            [print(" ", end="") for a in range(self.x)]
            [print("#", end="") for f in range(self.width)]
            print("")

    def __str__(self):
        """this function return and printing the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """update class rectangle.

        parameter:
            *args (ints): New attribute values.
                    1st argument should be the id attribute
                    2nd argument should be the width attribute
                    3rd argument should be the height attribute
                    4th argument should be the x attribute
                    5th argument should be the y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

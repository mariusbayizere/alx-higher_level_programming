#!/usr/bin/python3
"""represent a square class which inherts property of rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize Square class.

        parameter:
            size (int): size of the class Square.
            x (int): x coordinate of class Square.
            y (int): y coordinate of class Square.
            id (int): identity of class Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        function that have responsible to print the string
        representation of this class a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """
        Modify the attributes of the Square.

        Parameters:
            *args (ints): New attribute values.
                - 1st argument: id attribute
                - 2nd argument: size attribute
                - 3rd argument: x attribute
                - 4th argument: y attribute

        **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            p = 0
            for arg in args:
                if p == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif p == 1:
                    self.size = arg
                elif p == 2:
                    self.x = arg
                elif p == 3:
                    self.y = arg
                p += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """function that will return dictionary of the Square class."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

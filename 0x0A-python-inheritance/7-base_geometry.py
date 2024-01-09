#!/usr/bin/python3
"""Define the class called BaseGeometry"""


class BaseGeometry:
    """represent the empty class named BaseGeometry"""

    def area(self):
        """Function that raise Exception in case area are not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate and ensure that a given value is an integer.

        Args:
            self: An instance of the class.
            name (str): The name or identifier of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If value must be greater than 0
            """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

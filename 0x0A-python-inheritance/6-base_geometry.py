#!/usr/bin/python3
"""Define the class called BaseGeometry"""


class BaseGeometry:
    """represent the empty class named BaseGeometry"""
    
    def area(self):
        """Function that raise Exception in case area are not implemented"""
        raise Exception("area() is not implemented")

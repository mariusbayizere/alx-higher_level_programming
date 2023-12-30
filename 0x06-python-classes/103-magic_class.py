#!/usr/bin/python3
"""Define a class MagicClass."""
import math
import dis


class MagicClass:
    """circle"""
    def __init__(self, radius=0):
        """initialize magic classi
        Arg:
        radius: must be integer and float in magic class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("raidus must be int or float")
        self.__radius = radius

    def area(self):
        """return the area of magic class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return circumference of magic class"""
        return (self.__radius * 2 * math.pi)

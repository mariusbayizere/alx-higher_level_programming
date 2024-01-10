#!/usr/bin/python3
"""Student class module"""


class Student:
    """represent  class student"""
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Person object with the provided attributes.

        Parameters:
            - first_name (str): The first name of the person.
            - last_name (str): The last name of the person.
            - age (int): The age of the person.

        Returns:
            None
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function for retrieves a dictionary representation"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {g: getattr(self, g) for g in attrs if hasattr(self, g)}
        return self.__dict__

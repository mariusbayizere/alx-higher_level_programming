#!/usr/bin/python3
"""Define class MyInt which inhert property of the int"""


class MyInt(int):
    """represent class Myint which inherts property of this int"""
    def __eq__(self, data):
        """funtion that compare two value"""
        return self.real == data

    def __ne__(self, data):
        """function compare two value"""
        return self.real != data

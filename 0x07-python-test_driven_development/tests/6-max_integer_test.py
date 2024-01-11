#!/usr/bin/python3
"""unit test module for the tests/6-max_integer_test.py"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """class for testing the 6-max_integer_test.py"""

    def test_max_integer(self):
        """test list of integers"""
        new_list = [1, 3, 6, 2, 4]
        self.assertEqual(max_integer(new_list), 6)

    def test_max_integer_neg(self):
        """test case for list of integers (negatives)"""
        new_list = [1, 2, 3, 8, 5, -40, -300, -12, 0]
        self.assertEqual(max_integer(new_list), 8)

    def test_max_integer_empty(self):
        """test case for empty list"""
        self.assertEqual(max_integer([]), None)

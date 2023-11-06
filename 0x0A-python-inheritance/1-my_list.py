#!/usr/bin/python3
"""Module with a simple class inheriting from list"""


class MyList(list):
    """Prints a list in ascending order"""
    def print_sorted(self):
        print(sorted(self))

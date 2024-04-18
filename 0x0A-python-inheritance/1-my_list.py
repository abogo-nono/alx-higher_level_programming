#!/usr/bin/python3
""" A class that inherits from list
"""


class MyList(list):
    """MyList class inheriting from list"""
    def __init__(self):
        """__init__ init method
        """
        pass

    def print_sorted(self):
        """print_sorted print the sorted list
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)

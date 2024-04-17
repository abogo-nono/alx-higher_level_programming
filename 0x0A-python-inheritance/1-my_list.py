#!/usr/bin/python3
"""
A class that inherits from list
"""


class MyList(list):
    def __init__(self):
        """
        Init the class

        Args:
            self: the instance
        """
        pass

    def print_sorted(self):
        """
        Print sort and print the list

        Args:
            self: the object
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)

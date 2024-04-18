#!/usr/bin/python3
"""
get the attributes and methods of an object
"""


def lookup(obj):
    """lookup Return the attributes and methods an object

    Args:
        obj (object): the object

    Returns:
        list: the list of attributes and methods
    """
    return dir(obj)

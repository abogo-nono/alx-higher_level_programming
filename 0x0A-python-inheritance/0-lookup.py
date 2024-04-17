#!/usr/bin/python3
"""
get the attributes and methodes of an object
"""

def lookup(obj):
    """
    Return the attributes and methods an object

    Args:
        obj (object): the object

    Returns:
        list: list of attributes and methods
    """
    return dir(obj)


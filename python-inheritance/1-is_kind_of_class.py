"""
Module: 1-is_kind_of_class

This module contains a function that checks if an object is an instance of, or if
the object is an instance of a class that inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
    - obj: The object to check.
    - a_class: The class to compare against.

    Returns:
    - True if obj is an instance of a_class or inherited from it; False otherwise.
    """
    return isinstance(obj, a_class)

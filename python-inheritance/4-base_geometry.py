"""
Module: 4-base_geometry

This module contains the definition of the BaseGeometry class with an area() method.
"""

class BaseGeometry:
    """
    Base class definition for geometry.
    """

    def __init_subclass__(cls):
        pass

    def area(self):
        """
        Calculate the area.

        Raises:
        - Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

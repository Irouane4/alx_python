"""
Module: 5-base_geometry

This module contains the definition of the BaseGeometry class with area() and integer_validator() methods.
"""

class BaseGeometry:
    """
    Base class definition for geometry.
    """

    def area(self):
        """
        Calculate the area.

        Raises:
        - Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value.

        Args:
        - name: A string representing the name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

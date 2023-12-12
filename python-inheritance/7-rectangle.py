"""
Module: 7-rectangle

This module contains the definition of the Rectangle class, inheriting from BaseGeometry.
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

class Rectangle(BaseGeometry):
    """
    Rectangle class definition, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the given width and height.

        Args:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        - The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        - A string in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

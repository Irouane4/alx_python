#!/usr/bin/python3
"""
Module containing the Rectangle class.
"""
try:
    from models.base import Base
except ImportError:
    pass
class Rectangle(Base):
    """
    Rectangle class, inherits from Base.

    Attributes:
        __width (int): Private instance attribute for the width of the rectangle.
        __height (int): Private instance attribute for the height of the rectangle.
        __x (int): Private instance attribute for the x-coordinate of the rectangle.
        __y (int): Private instance attribute for the y-coordinate of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Constructor method for Rectangle class.
        width(self): Getter method for __width attribute.
        width(self, value): Setter method for __width attribute.
        height(self): Getter method for __height attribute.
        height(self, value): Setter method for __height attribute.
        x(self): Getter method for __x attribute.
        x(self, value): Setter method for __x attribute.
        y(self): Getter method for __y attribute.
        y(self, value): Setter method for __y attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle (default is 0).
            y (int): y-coordinate of the rectangle (default is 0).
            id (int): ID of the rectangle (default is None).

        Note:
            This constructor calls the constructor of the Base class with id.
            It assigns each argument width, height, x, and y to the respective attribute.
        """
        super().__init__(id)  # Call the constructor of the Base class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        self.__y = value

if __name__ == "__main__":
    # Test cases
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

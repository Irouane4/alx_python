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
        area(self): Public method that returns the area value of the Rectangle instance.
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
        super().__init__(id)
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
        self.validate_integer("width", value, positive=True)
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        self.validate_integer("height", value, positive=True)
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        self.validate_integer("x", value, non_negative=True)
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        self.validate_integer("y", value, non_negative=True)
        self.__y = value

    def area(self):
        """
        Public method that returns the area value of the Rectangle instance.

        Returns:
            int: Area of the Rectangle.
        """
        return self.__width * self.__height

    def validate_integer(self, name, value, positive=False, non_negative=False):
        """
        Validate if a value is an integer and satisfies additional conditions.

        Args:
            name (str): Name of the attribute.
            value: Value to be validated.
            positive (bool): Whether the value must be positive.
            non_negative (bool): Whether the value must be non-negative.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If additional conditions are not satisfied.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if non_negative and value < 0:
            raise ValueError("{} must be >= 0".format(name))

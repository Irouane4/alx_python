"""
Module containing the Rectangle class.
"""
try:
    from models.base import Base
except ImportError:
    Base = None

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
        display(self): Public method that prints in stdout the Rectangle instance with the character #.
        __str__(self): Override of the __str__ method to return a formatted string.
        validate_integer(self, value, attr_name): Private method to validate if a value is an integer.
        validate_positive(self, value, attr_name): Private method to validate if a value is positive.
        validate_non_negative(self, value, attr_name): Private method to validate if a value is non-negative.
        update(self, *args): Public method to update attributes based on a sequence of arguments.

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
        self.validate_integer(value, "width")
        self.validate_positive(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        self.validate_integer(value, "height")
        self.validate_positive(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        self.validate_integer(value, "x")
        self.validate_non_negative(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        self.validate_integer(value, "y")
        self.validate_non_negative(value, "y")
        self.__y = value

    def area(self):
        """Public method that returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Public method that prints in stdout the Rectangle instance with the character #."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Override of the __str__ method to return a formatted string."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """
        Public method to update attributes based on a sequence of arguments.

        Args:
            *args: Variable-length argument list.
                1st argument should be the id attribute.
                2nd argument should be the width attribute.
                3rd argument should be the height attribute.
                4th argument should be the x attribute.
                5th argument should be the y attribute.

        Note:
            This method updates the attributes in the specified order, and the number of arguments
            must match the number of attributes to be updated.
        """
        attributes = ["id", "width", "height", "x", "y"]

        for attr, value in zip(attributes, args):
            setattr(self, attr, value)

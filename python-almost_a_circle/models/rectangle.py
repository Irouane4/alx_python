"""
Module containing the Rectangle class.
"""
try:
    from models.base import Base
except ImportError:
    pass

class Rectangle(Base):
    """
    ... (rest of the class documentation remains the same)
    """

    def update(self, *args):
        """
        Public method that assigns arguments to each attribute.

        Args:
            args: Variable number of arguments in the order (id, width, height, x, y).

        Note:
            This method updates the attributes with the values provided in the arguments.
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        ... (rest of the constructor method remains the same)
        """

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

    def validate_integer(self, value, attr_name):
        """Private method to validate if a value is an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))

    def validate_positive(self, value, attr_name):
        """Private method to validate if a value is positive."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))

    def validate_non_negative(self, value, attr_name):
        """Private method to validate if a value is non-negative."""
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr_name))

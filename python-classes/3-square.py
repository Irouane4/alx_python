"""Defines a Square class."""
class Square:
    """Represents a square.
    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Initializes a new Square instance.
        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size
    @size.setter
    def size(self, value):
        """Setter method to set the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)

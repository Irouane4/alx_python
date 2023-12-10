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
    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))
    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)
    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)
    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))

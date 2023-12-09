class Square:
    """A class that defines a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initialize a square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

if __name__ == "__main__":
    my_square = Square(3)

    print(type(my_square))

    print(my_square.__dict__)

    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)

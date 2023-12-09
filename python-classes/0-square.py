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

# Test the Square class
if __name__ == "__main__":
    my_square = Square(3)

    # Print the type of my_square
    print(type(my_square))

    # Print the dictionary representation of my_square
    print(my_square.__dict__)

    # Attempt to access the size attribute (should raise an error)
    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    # Attempt to access the __size attribute (should raise an error)
    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)

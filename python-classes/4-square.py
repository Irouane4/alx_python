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
    def my_print(self):
        """Prints the square using '#' characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()
    print("--")
    my_square.size = 10
    my_square.my_print()
    print("--")
    my_square.size = 0
    my_square.my_print()
    print("--")

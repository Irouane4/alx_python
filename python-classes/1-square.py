class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes a new Square instance.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size
        # Validate the size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

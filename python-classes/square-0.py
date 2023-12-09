Square = __import__('0-square').Square

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

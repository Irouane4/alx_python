# is_same_class.py

def is_same_class(obj, a_class):
    """
    Checks if the given object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class; otherwise, False.
    """
    return type(obj) is a_class

# Test cases
if __name__ == "__main__":
    # Test case 1
    a = 1
    print(is_same_class(a, int))

    # Test case 2
    a = True
    print(is_same_class(a, int))

    # Test case 3
    a = 3.14
    print(is_same_class(a, int))

    # Test case 4
    a = True
    print(is_same_class(a, object))

    # Test case 5
    a = None
    print(is_same_class(a, object))

    # Test case 6
    a = None
    print(is_same_class(a, list))

    # Test case 7
    a = [1, 2, 3]
    print(is_same_class(a, list))

    # Test case 8
    a = [1, 2, 3]
    print(is_same_class(a, object))


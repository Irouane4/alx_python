def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: Object to be checked.
        a_class: Class to compare against.

    Returns:
        True if obj is an instance of a_class; otherwise, False.
    """
    return type(obj) == a_class

if __name__ == "__main__":
    # Test cases
    a = 1
    print(is_same_class(a, int))  # True

    a = True
    print(is_same_class(a, int))  # False

    a = 3.14
    print(is_same_class(a, int))  # False

    a = True
    print(is_same_class(a, object))  # False

    a = None
    print(is_same_class(a, object))  # False

    a = None
    print(is_same_class(a, list))  # False

    a = [1, 2, 3]
    print(is_same_class(a, list))  # False

    a = [1, 2, 3]
    print(is_same_class(a, object))  # False

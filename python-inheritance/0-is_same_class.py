def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise, it returns False and prints a message.

    :param obj: The object to check.
    :param a_class: The class to compare with.
    :return: True if obj is an instance of a_class; otherwise False.
    """
    if type(obj) is a_class:
        print("{} is an instance of the class {}".format(obj, a_class.__name__))
        return True
    else:
        return False

# Example usage:
a = 1
print(is_same_class(a, int))


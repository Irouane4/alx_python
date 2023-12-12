# 1-is_kind_of_class.py

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a_class or its subclasses; otherwise, False.
    """
    return isinstance(obj, a_class)

if __name__ == "__main__":
    # Example usage
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))

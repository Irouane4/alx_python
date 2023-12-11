def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if obj is an instance of a_class; otherwise False.
    """
    return type(obj) is a_class

# Test cases
a = 1
print(is_same_class(a, int))  # Expected output: True

a = True
print(is_same_class(a, int))  # Expected output: False

a = 3.14
print(is_same_class(a, int))  # Expected output: False

a = True
print(is_same_class(a, object))  # Expected output: False

a = None
print(is_same_class(a, object))  # Expected output: False

a = None
print(is_same_class(a, list))  # Expected output: False

a = [1, 2, 3]
print(is_same_class(a, list))  # Expected output: True

a = [1, 2, 3]
print(is_same_class(a, object))  # Expected output: False

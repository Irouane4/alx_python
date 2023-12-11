def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    """
    return type(obj) is a_class or issubclass(type(obj), a_class)

a = 1
if is_kind_of_class(a, int):
    print("True")
if is_kind_of_class(a, float):
    print("True")
if is_kind_of_class(a, object):
    print("True")

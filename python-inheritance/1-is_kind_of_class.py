def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) or type(obj) is a_class

a = 1
result = is_kind_of_class(a, int)

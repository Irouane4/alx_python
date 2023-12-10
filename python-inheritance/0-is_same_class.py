def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class."""
    return type(obj) is a_class

# Example usage:
a = 1
print(is_same_class(a, int))

a = True
print(is_same_class(a, int))

a = 3.14
print(is_same_class(a, int))

a = True
print(is_same_class(a, object))

a = None
print(is_same_class(a, object))

a = None
print(is_same_class(a, list))

a = [1, 2, 3]
print(is_same_class(a, list))

a = [1, 2, 3]
print(is_same_class(a, object))


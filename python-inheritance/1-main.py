#!/usr/bin/python3
is_kind_of_class = __import__('1-is_kind_of_class').is_kind_of_class

if __name__ == "__main__":
    a = 1
    print(is_kind_of_class(a, int))

    a = True
    print(is_kind_of_class(a, int))
    print(is_kind_of_class(a, object))

    a = 3.14
    print(is_kind_of_class(a, int))
    print(is_kind_of_class(a, object))

    a = None
    print(is_kind_of_class(a, object))
    print(is_kind_of_class(a, list))

    a = [1, 2, 3]
    print(is_kind_of_class(a, list))
    print(is_kind_of_class(a, object))

import importlib
a = 1
b = 2

add = importlib.import_module('add_0').add
print("{} + {} = {}".format(a, b, add(a, b)))


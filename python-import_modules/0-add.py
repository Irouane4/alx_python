import importlib
a = 1
b = 2

add_0 = importlib.import_module('add_0')
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add_0.add(a, b)))

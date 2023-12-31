Rectangle = __import__('6-rectangle').Rectangle
BaseGeometry = __import__('6-rectangle').BaseGeometry

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r._Rectangle__width, r._Rectangle__height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
print(issubclass(Rectangle, BaseGeometry))

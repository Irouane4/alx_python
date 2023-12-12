BaseGeometry = __import__('3-base_geometry').BaseGeometry

bg = BaseGeometry()

expected_output = [
    '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
    '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
    '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'
]

if all(attr in dir(bg) for attr in expected_output):
    print("Output matches the expected output!")
else:
    print("Output does not match the expected output.")

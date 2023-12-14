#!/usr/bin/python3
BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()

# Get the actual output from dir(bg)
actual_output = dir(bg)

# Remove '__init_subclass__' from the actual output
actual_output = [attr for attr in actual_output if attr != '__init_subclass__']

# Exclude '__init_subclass__' from the expected output
expected_output = [
    '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
    '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
    '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
    '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    'area'
]

# Check if the output matches the expected output
if actual_output == expected_output:
    print("Output matches the expected output!")
else:
    print("Output does not match the expected output.")

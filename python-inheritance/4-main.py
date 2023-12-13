BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()

expected_output = set(['__class__', '__dir__', '__doc__', 'area'])
actual_output = set(dir(bg))

if expected_output.issubset(actual_output) and actual_output.issubset(expected_output):
    print("Output matches the expected output!")
else:
    print("Output does not match the expected output.")


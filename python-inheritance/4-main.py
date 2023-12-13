BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()

expected_output = ['__class__', '__dir__', '__doc__', 'area']

if sorted(dir(bg)) == sorted(expected_output):
    print("Output matches the expected output!")
else:
    print("Output does not match the expected output.")

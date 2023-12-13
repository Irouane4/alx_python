#!/usr/bin/python3
BaseGeometry = __import__('4-base_geometry').BaseGeometry

bg = BaseGeometry()

# Get the actual output from dir(bg)
actual_output = dir(bg)

# Exclude '__init_subclass__' from the expected output
expected_output = [attr for attr in actual_output if attr != '__init_subclass__']

# Check if the output matches the expected output
if actual_output == expected_output:
    print("Output matches the expected output!")
else:
    print("Output does not match the expected output.")

for i in range(10):
    for j in range(i + 1, 10):
        is_last_number = i == 8 and j == 9  # Check if it's the last number (89)
        print("{:02d}".format(i * 10 + j), end="" if is_last_number else ", ")
print()
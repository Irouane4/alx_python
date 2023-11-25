for i in range(9):
    for j in range(i + 1, 10):
        print("{:02d}, {:02d}, ".format(i, j), end="")
print("{:02d}".format(9))

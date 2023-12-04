# 1-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row in matrix:
        for i, element in enumerate(row):
            if i == len(row) - 1:
                print("{:d}".format(element), end="")
            else:
                print("{:d} ".format(element), end="")
        print()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()

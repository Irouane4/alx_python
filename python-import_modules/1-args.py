from sys import argv
def print_arguments():
    num_args = len(argv) - 1
    arg_plural = "s" if num_args != 1 else ""

    if num_args == 0:
        print("{} argument{}.".format(num_args, arg_plural))
    else:
        print("{} argument{}:".format(num_args, arg_plural))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))

if __name__ == "__main__":
    print_arguments()
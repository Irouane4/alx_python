count = 0
for num in range(1, 100):
    first_digit = num // 10
    second_digit = num % 10
    if first_digit != second_digit:
        if count > 0:
            print(", ", end="")
        print("{:02d}".format(num), end="")
        count += 1
print()
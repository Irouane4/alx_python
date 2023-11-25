import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number <= 0 and number > -10000:
    negative_digit = (-last_digit)
    if -last_digit < 6 and -last_digit != 0:
        print(f"Last digit of {number} is {-last_digit} and is less then 6 and not 0")
if number > 0 and number < 10000:
    if last_digit > 5:
        print(f"The string Last digit of {number} is {last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"The string Last digit of {number} is {last_digit} and is 0")
    elif last_digit < 6 and last_digit > 0:
        print(f"Last digit of {number} is {last_digit} and is less then 6 and not 0")



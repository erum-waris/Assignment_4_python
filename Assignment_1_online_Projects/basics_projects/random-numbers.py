# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could include 1 and could include 6:

# value = random.randint(1, 6)

import random



N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100


def main():
    # Generate 10 random numbers between 1 to 100
    numbers = []
    for i in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        numbers.append(number)

    print(f"The List of random numbers is :{" ".join(map(str, numbers))}")

if __name__ == "__main__":
    main()


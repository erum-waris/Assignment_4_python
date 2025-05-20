# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random


def rolling_dice():
    user_1 = random.randint(1 , 6)
    user_2 = random.randint(1 , 6)
    print(f"User Die 1 is : {user_1}")
    print(f"User Die 2 is : {user_2}")
    dies_total = user_1 + user_2
    print(f"Dies Total:{dies_total}")

def main():
    die_main = 10 
    print(f"die in main() is starts as: {die_main}")
    rolling_dice()
    rolling_dice()
    rolling_dice()
    print(f"Now Die in is main() is {die_main} ")

if __name__ == "__main__":
    main()


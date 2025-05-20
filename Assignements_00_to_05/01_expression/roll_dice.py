


# Rolling Dice 
import random

#random.seed(1) it will always give you same output as in my case it is generating 2 and 5 only,, easy for debugging
#  ✅ Use random.seed() → when you want repeatable results (e.g., for testing or demos).

# 🚫 Remove random.seed() → when you want true randomness (e.g., for gameplay). bascically It will generate the same sequence of random numbers every time you run the program.

def roll():
 
    dice_1: int = random.randint(1, 6)
    dice_2: int = random.randint(1, 6)

    sum_of_dices: int = dice_1 + dice_2

    print(f" Dice_1: {dice_1} \n Dice_2: {dice_2} \n Sum of Dices = {sum_of_dices}")

if __name__ == "__main__":
    roll()

# Number Guessing Game by user

import random 

def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while (guess != random_number):
        guess = int(input("Enter a Number to Guess 1 to 10:"))
        if guess < random_number:
            print(f"Guessed_Number is Low {guess}, Try again!")
        elif guess > random_number:
            print(f"Guessed_Number is High {guess}, Try again!")
    
    print(f"User Guessed_Number is Perfect {random_number}, Congratulations!")

guess_number(10)
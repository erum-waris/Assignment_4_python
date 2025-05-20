# Guess the number game

import random

def main():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    print("Welcome to the Guess the Number game!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Guess a number between 1 and 100: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            if guess < secret_number:
                print("Guessed Number is low!")
            elif guess > secret_number:
                print("Guessed Number is high!")
            else:
                print(f"Congratulations! You've guessed the number correctly secret number is  {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter Only Numbers.")


    if attempts == max_attempts:
        print(f"Sorry! You've used all {max_attempts} attempts. The secret number was {secret_number}.")
if __name__ == "__main__":
    main()

# Hangman game
from words import words
import random
import string

def get_word(word_list):
    """Get a valid word from the list without spaces or hyphens."""
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    # Game initialization
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Display game status
        print(f"\nYou have {lives} lives remaining")
        print("Used letters:", " ".join(sorted(used_letters)))
        current_word = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", " ".join(current_word))

        # Get and validate user input
        user_input = input("Guess a letter: ").upper()
        
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            
            if user_input in word_letters:
                word_letters.remove(user_input)
                print(f"Good guess! '{user_input}' is in the word!")
            else:
                lives -= 1
                print(f"Oops! '{user_input}' is not in the word. You lose a life.")
                
        elif user_input in used_letters:
            print(f"You've already used '{user_input}'. Try another letter.")
        else:
            print("Invalid input. Please enter a single uppercase letter.")

    # Final result
    if lives > 0:
        print(f"\nCongratulations! You guessed the Correct word: {word}")
    else:
        print(f"\nGame over! The Correct word was: {word}")

if __name__ == "__main__":
    print("Welcome to Hangman!")
    hangman()



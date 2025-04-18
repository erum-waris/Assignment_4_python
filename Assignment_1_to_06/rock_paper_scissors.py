# Rock Paper Scissors
import random

def play():
    computer_choice = random.choice(["r","p", "s"])
    user_choice = input("Enter your choice (r, p, s): ").lower()

    e = exit
    while user_choice != e:
         if user_choice == computer_choice:
               print(f"User choose : {user_choice}")
               print(f"Computer choose : {computer_choice}")
               print("It's a tie!")
         
         # rock beats scissors, scissors beats paper, paper beats rock
         elif (user_choice == "r" and computer_choice == "s") or (user_choice == "p" and computer_choice == "r") or (user_choice == "s" and computer_choice == "p"):
             print(f"User choose : {user_choice}")
             print(f"Computer choose : {computer_choice}")
             print("You Won 🏆 Computer lose 😢!")
         else:
               print(f"User choose : {user_choice}")
               print(f"Computer choose : {computer_choice}")
               print("Computer Won 🏆 You lose 😢!")
         
         # Ask the user if they want to play again
         play_again = input("Do you want to play again? (y/n): ").lower()
         if play_again == "y":
               play()
         elif play_again == "n":
               print("Goodbye! Thanks for playing! See you next time!")
               break
         else:
               print("Playing Great 😎 ! you can exit 👍 the game by typing 'e' otherwise you can continue playing 🤞")
               play()
    
play()



















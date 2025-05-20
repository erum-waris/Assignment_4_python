
# Problem Statement
# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.


# Constants
JOKE = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"   
SORRY = "Sorry I only tell jokes"

def main():
    print("Joke Bot :)")
    while True:
        PROMPT = input("What do you want? type 'joke' for a joke: ").strip().lower()
        if PROMPT == "joke":
            print("Here is a joke for you! " + JOKE)
            
        else:
            print(SORRY)
            break
    
   






if __name__ == '__main__':
    main()
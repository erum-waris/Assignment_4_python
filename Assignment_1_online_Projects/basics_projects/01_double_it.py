# Problem Statement
# Write a program that asks a user to enter a number. Your program will make double number of that number and print out the result. It will repeat that process until the value is 100 or greater.


def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            doubled = number * 2
            print(f"The double of {number} is: {doubled}")
            if doubled >= 100:
                print(f"We stop at {doubled} because that value is greater than or equal to 100.")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()

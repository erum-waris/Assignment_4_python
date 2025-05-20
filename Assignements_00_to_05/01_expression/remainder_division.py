# Problem Statement
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

def main():
    try:
        # Get user input for the first number
        num1 = int(input("Please enter an integer to be divided: "))

        # Get user input for the second number
        num2 = int(input("Please enter an integer to divide by: "))

        # Perform division and calculate remainder
        result = num1 // num2
        remainder = num1 % num2

        # Print the result and remainder
        print(f"The result of this division is {result} with a remainder of {remainder}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid integers.")
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the division program.")

if __name__ == "__main__":
    main()
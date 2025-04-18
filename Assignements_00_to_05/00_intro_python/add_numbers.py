# Problem Statement

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.


# my solution

#user input
user_input1 = int(input("Enter the first number: ")) #int function will convert string input into integer
user_input2 = int(input("Enter the second number: "))

def addition(num1,num2):
 # program for sum of numbers logic
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} = {sum}.")

addition(user_input1,user_input2)

#given solution

# def main():
#     print("This program adds two numbers.")
#     num1 : str = input("Enter first number: ")
#     num1 : int = int(num1)
#     num2  : str = input("Enter second number: ")
#     num2 : int = int(num2)
#     total : int = num1 + num2
#     print("The total is " + str(total) + ".")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()
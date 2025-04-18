# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C


#input in Fahrenheit
# Prompt the user to enter a temperature in Fahrenheit
F = float(input("Enter Temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using the formula
Celsius = (F - 32) * 5.0 / 9.0

# Display the result
print(f"Temperature: {F}°F = {Celsius:.2f}°C")

def main():
    print("This program converts Fahrenheit to Celsius.")
    # take user input in Fahrenheit
    fahrenheit : str = input("Enter temperature in Fahrenheit: ")
    fahrenheit : float = float(fahrenheit) # convert to float
    # convert to Celsius using the formula
    celsius : float = (fahrenheit - 32) * 5.0 / 9.0
    # print the result
    print(f"Temperature: {fahrenheit}°F = {celsius:.2f}°C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
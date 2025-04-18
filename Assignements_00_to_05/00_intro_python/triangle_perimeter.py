# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

#user input for 3 side of Triangle:

def main():
    triangle_side1 = float(input('Enter the length of side 1: '))
    triangle_side2 = float(input('Enter the length of side 2: '))
    triangle_side3 = float(input('Enter the length of side 3: '))

    sum_of_sides = triangle_side1 + triangle_side2 + triangle_side3
    print(f'The perimeter of the triangle is {sum_of_sides}')

if __name__ == '__main__':
    main()
# The program calculates the perimeter of a triangle by summing the lengths of its three sides.
    
#given out put
# def main():
#     # Get the 3 side lengths of the triangle
#     side1: float = float(input("What is the length of side 1? "))
#     side2: float = float(input("What is the length of side 2? "))
#     side3: float = float(input("What is the length of side 3? "))

#     # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
#     print("The perimeter of the triangle is " + str(side1 + side2 + side3))
#     print(f"The perimeter is {side1 + side2 + side3}")  # f-string (modern preferred way)


# # There is no need to edit code beyond this point

# if __name__ == '__main__':
#     main()
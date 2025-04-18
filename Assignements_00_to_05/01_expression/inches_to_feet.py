# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# 1 feet == 12 inch

foot_1 = 12

def main():
    feet_input = float(input("Enter number in feet:"))  

    #float type can handle int by passing .0 but integer can not handle float it will raise an error if user will put any decimal value integer input will raise an error and program will crash

    conversion_in_inches = feet_input * foot_1   # input multiply by foot value can convert feet input value into inches
    
    print(f"""Feet to Inches: {conversion_in_inches}" """) # double quote " is a sign to represent inch

if __name__ == "__main__":
    main()

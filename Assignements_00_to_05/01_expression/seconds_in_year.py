# Problem Statement
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

def main():
    #CONSTANTS
    DAYS_IN_YEAR = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60

    print("Calculating the number of seconds in a year...")
    print(f"There are {DAYS_IN_YEAR} days in a year.")
    print(f"There are {HOURS_IN_DAY} hours in a day.")
    print(f"There are {MINUTES_IN_HOUR} minutes in an hour.")
    print(f"There are {SECONDS_IN_MINUTE} seconds in a minute.")
    print(f"There are {DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE} seconds in a year!")

if __name__ == "__main__":
    main()




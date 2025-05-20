#Problem Statement
# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!


def main():
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Liftoff!")

if __name__ == "__main__":
    main()

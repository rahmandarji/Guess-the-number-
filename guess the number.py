import random

guess = 0
computer = random.randint(1, 100)

while True:
    user = int(input("Enter a number (0 to quit): "))

    if user == 0:
        print("Thanks for playing!")
        break

    guess += 1

    if user > computer:
        print("Too high")
    elif user < computer:
        print("Too low")
    else:
        print("You won!")
        print(f"You guessed {guess} times")
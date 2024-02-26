from random import *

name = input("What's your name? ")

print("Good Lucky!", name)

number = str(randrange(99999))

print("Guess the numers")

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in number:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")

            failed += 1

    if failed == 0:
        print("You Win")

        print("The numer is: ", number)
        break

    print()
    guess = str(input("Guess the number "))

    guesses += guess

    if guess not in number:
        turns -= 1

        print("Wrong")

        print("You have", turns, 'more guesses')

        if turns == 0:
            print("You loose")

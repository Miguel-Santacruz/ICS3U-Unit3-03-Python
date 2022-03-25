#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: Mar 2022
# This program is a number guessing game

import random


def main():
    # This function checks the number

    RANDOM_NUMBER = random.randint(1, 9)

    # input
    number = int(input("Enter number between 0 - 9: "))

    # process & output
    print("")
    if number == RANDOM_NUMBER:
        print("You guessed right!")
    else:
        print("you guessed wrong! The right number was {}".format(RANDOM_NUMBER))

    print("\nDone.")


if __name__ == "__main__":
    main()

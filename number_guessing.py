"""
This file contains an incomplete function definition.  
Your task is to complete the incomplete function definition. so that it behaves as indicated in the documentation.

Do not run this file directly.
Rather, call this function from main.py and run that file.
"""

import random


def guess_number(low, high, num_attempts):
    target = random.randint(low, high)
    print(f"Guess the number between {low} and {high}. You have {num_attempts} attempts.")
    for attempt in range(num_attempts):
        try:
            guess = int(input("Enter your guess: "))
            if guess == target:
                print("Congratulations! You guessed the correct number!")
                return True
            else:
                print("Wrong guess. Try again.")
        except ValueError:
            print("That's not a valid number. Please enter a numeric guess.")
    print("Sorry, all attempts used. Better luck next time!")
    return False

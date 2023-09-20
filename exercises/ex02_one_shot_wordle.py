"""EX02 - One-shot Wordle - Loops."""

__author__ = "730718451"

secret_word: str = "python"
six_letter_guess: str = input("What is your 6-letter guess?")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(six_letter_guess) != 6:
    six_letter_guess = str(input("That was not six letters! Try again:"))

while six_letter_guess != len(secret_word):
    if six_letter_guess [0] == secret_word [0]:
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)

if six_letter_guess != secret_word:
    print("Not quite. Play again soon!")
    exit()

if six_letter_guess == secret_word:
    print("Woo! You got it!")


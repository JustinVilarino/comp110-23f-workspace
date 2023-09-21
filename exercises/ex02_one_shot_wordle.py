"""EX02 - One-shot Wordle - Loops."""

__author__ = "730718451"

secret_word: str = "python"

letter_index: int = 0

emoji: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

six_letter_guess: str = input("What is your 6-letter guess?")

while len(six_letter_guess) != 6:
    six_letter_guess = str(input("That was not six letters! Try again:"))

while letter_index < len(secret_word):
    if six_letter_guess[letter_index] == secret_word[letter_index]:
        letter_index = letter_index + 1
        emoji = emoji + GREEN_BOX
    else:
        letter_index = letter_index + 1
        emoji = emoji + WHITE_BOX
print(emoji)

if six_letter_guess != secret_word:
    print("Not quite. Play again soon!")
    exit()

if six_letter_guess == secret_word:
    print("Woo! You got it!")
    exit()
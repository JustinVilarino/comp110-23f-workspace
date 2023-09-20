"""EX02 - One-shot Wordle - Loops."""

__author__ = "730718451"

secret_word: str = "python"
six_letter_guess: str = input("What is your 6-letter guess?")

guess_index: str = six_letter_guess.index
lower_letter: str = (six_letter_guess[0])

semi_correct: False
secret_index: str = (secret_word[0])

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(six_letter_guess) != 6:
    six_letter_guess = str(input("That was not six letters! Try again:"))

while guess_index != len(secret_word):
    current_letter: str = (lower_letter)
    if guess_index == secret_word [0]:
        guess_index = lower_letter + 1
        print(GREEN_BOX)
    else:
        print(WHITE_BOX)

while (semi_correct = false) and (secret_index < len(secret_word))
    if guess_index == secret_index:
        semi_correct == True
        print(YELLOW_BOX)
    else:
        semi_correct == False
if six_letter_guess != secret_word:
    print("Not quite. Play again soon!")
    exit()

if six_letter_guess == secret_word:
    print("Woo! You got it!")


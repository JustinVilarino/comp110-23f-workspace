"""EX03 - Wordle."""

__author__ = "730718451"


def contains_char(word_index: str, letter_idx: str) -> bool:
    """Determines if the word contains the character being searched for."""
    # This function will check the word for the letter we are looking for.
    assert len(letter_idx) == 1
    i = 0
    while i < len(word_index):
        if letter_idx == word_index[i]:
            return True
        i = i + 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Replaces characters with the correct emojis."""
    # This functions incorporates the Wordle emojis.
    emoji: str = ""
    assert len(guess_word) == len(secret_word)
    i = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while i < len(secret_word):
        if (contains_char(secret_word, guess_word[i]) is True) and (guess_word[i] == secret_word[i]):
            emoji = emoji + GREEN_BOX
        if (contains_char(secret_word, guess_word[i]) is False):
            emoji = emoji + WHITE_BOX
        if (contains_char(secret_word, guess_word[i]) is True) and (guess_word[i] != secret_word[i]):
            emoji = emoji + YELLOW_BOX
        i = i + 1
    return emoji


def input_guess(guess_length: int) -> str:
    """Ensure that the guess has exactly 5 characters."""
    # Checks to see if the guessed word has the expected length.
    guess: str = input(f"What is your {guess_length}-letter guess?")
    while guess_length != len(guess):
        guess = str(input(f"That wasn't {guess_length}-letters! Try again:"))
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Combines all of the functions.
    guessing_word: str = ""
    answer: str = "codes"
    turn: int = 1
    while guessing_word != answer:
        print(f"=== Turn {turn}/6 ===")
        guessing_word = input_guess(len(answer))
        print(emojified(guessing_word, answer))
        if (guessing_word == answer) and (turn >= 1):
            print(f"You won in {turn}/6 turns!")
        if (guessing_word != answer) and (turn <= 6):
            turn = turn + 1
        if turn == 7:
            print("X/6 - Sorry, try again tomorrow!")
            return None


if __name__ == "__main__":
    main()
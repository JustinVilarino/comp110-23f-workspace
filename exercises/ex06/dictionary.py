"""Creating a dictionary."""

__author__ = "730718451"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary."""
    # The function should invert the contents of the dictionary.
    dictionary: dict[str, str] = {}
    for input_key in input:
        dictionary[input[input_key]] = input_key
    if len(input) != len(dictionary) or (len(input) == 0):
        raise KeyError("KeyError")
    return dictionary


def favorite_colors(name: dict[str, str]) -> str:
    """Points out the most popular color."""
     # The function should return the most frequent color.
    dictionary: dict[str, int] = {}
    for color in name:
        if name[color] in dictionary:
            dictionary[name[color]] += 1
        else:
            dictionary[name[color]] = 1
    # If there are no duplicate colors, it should return the first color.
    highest: int = 0
    favorite: str = ""
    for max in dictionary:
        if dictionary[max] > highest:
            highest = dictionary[max]
            favorite = max
    return favorite


def count(Freq_values: list[str]) -> dict[str, int]:
    """Counts the frequencies."""
    # The function should count the number of frequencies in the dictionary.
    dictionary: dict[str, int] = {}
    for number in Freq_values:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
    return dictionary


def alphabetizer(alph: list[str]) -> dict[str, list[str]]:
    """Alphabetizes the list."""
    # The function should seperate the words into alphabetical groups.
    dictionary: dict[str, list[str]] = {}
    for word in alph:
        letter: str = word[0].lower()
        if letter in dictionary:
            dictionary[letter].append(word)
        else:
            dictionary[letter] = [word]
    return dictionary


def update_attendance(week: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Creates a dictionary that can be mutated."""
    # The function should allow itself to be updated.
    if day in week:
        week[day].append(student)
    else:
        week[day] = [student]
    return week
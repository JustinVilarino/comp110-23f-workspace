"""EX04 - List Utils."""

__author__ = "730718451"


def all(number_list: list[int], input: int) -> bool:
    """Determines if the given list contains the input."""
    # This will check if all the numbers in the list are the same as the given number.
    index: int = 0
    while index < len(number_list):
        if number_list[index] == input:
            index = index + 1
        else:
            index = index + 1
            return False
    return True
# If we made it here, that means all the numbers in the list are the same as the given number.


def max(max_list: list[int]) -> int:
    """Determines the maximum number."""
    # This will search for the largest number in the list.
    if len(max_list) == 0:
        raise ValueError("max() arg is an empty List")
    # If the list is empty the message above will appear.
    max_number: int = max_list[0]
    max_index: int = 0
    while max_index < len(max_list):
        if max_number < max_list[max_index]:
            max_number = max_list[max_index]
        max_index = max_index + 1
    return max_number
# If we made it here, that means the maximum number has been found.


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Determines if the lists are equal."""
    # This will determine if both lists are the same.
    number: int = 0
    if len(first_list) != len(second_list):
        return False
    # If we made it here, that means the lists are not the same length.
    while number < len(first_list):
        if first_list[number] == second_list[number]:
            number = number + 1
        else:
            number = number + 1
            return False
        # If we made it here, that means both lists have the same length, but are still not the same.
    return True
# If we made it here, that means both lists are the same.
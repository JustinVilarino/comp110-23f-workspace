"""Test the Dictionary Functions."""

__author__ = "730718451"


from exercises.ex06.dictionary import invert

from exercises.ex06.dictionary import favorite_color

from exercises.ex06.dictionary import count

from exercises.ex06.dictionary import alphabetizer

from exercises.ex06.dictionary import update_attendance


def test_empty_invert() -> None:
    """Invert of empty list should be empty."""
    test_empty_i: list[str] = ["", ""]
    test_empty_i_values: list[str] = ["", ""]
    assert invert({}) == {}


def test_invert_one_case() -> None:
    """Testing Invert with one use case."""
    test_invert_a: list[str] = ["lebron", "james"]
    test_invert_b: list[str] = ["michael", "jordan"]
    assert invert({"lebron": "james", "michael": "jordan"}) == {"james": "lebron", "jordan": "michael"}


def test_invert_two_cases() -> None:
    """Testing Invert with two use cases."""
    test_invert_a2: list[str] = ["spongebob", "patrick"]
    test_invert_b2: list[str] = ["squidward", "mr.krabs"]
    assert invert({"spongebob": "patrick", "squidward": "mr.krabs"}) == {"patrick": "spongebob", "mr.krabs": "squidward"}


def test_empty_favorite_color() -> None:
    """Favorite color empty list should be empty."""
    test_empty_f: list[str] = ["", ""]
    test_empty_f_values: list[str] = ["", ""]
    assert favorite_color({}) == ""


def test_favorite_color_one_case() -> None:
    """Testing Favorite color with one use case."""
    test_favorite_color_a: list[str] = ["Marc", "blue"]
    test_favorite_color_b: list[str] = ["Kris", "blue"]
    assert favorite_color({"Marc": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_two_cases() -> None:
    """Testing Favorite color with two use cases."""
    test_favorite_color_a2: list[str] = ["George", "green"]
    test_favorite_color_b2: list[str] = ["Robert", "green"]
    assert favorite_color({"George": "green", "Robert": "green"}) == "green"


def test_empty_count() -> None:
    """Count empty list should be empty."""
    test_empty_c: list[str] = ["", ""]
    test_empty_c_values: list[int] = []
    assert count({}) == {}


def test_count_one_case() -> None:
    """Testing Count with one use case."""
    test_count_a: list[str] = ["bananas", "apples", "bananas"]
    assert count(test_count_a) == {"bananas": 2, "apples": 1}


def test_count_two_cases() -> None:
    """Testing Count with two use cases."""
    test_count_a2: list[str] = ["cars", "cars", "airplanes"]
    assert count(test_count_a2) == {"cars": 2, "airplanes": 1}


def test_empty_alphabetizer() -> None:
    """Alphabetizer empty list should be empty."""
    test_empty_a: list[str] = ["", ""]
    test_empty_a_values: list[str] = ["", ""]
    assert alphabetizer([]) == {}


def test_alphabetizer_one_case() -> None:
    """Testing Alphabetizer with one use case."""
    test_alphabetizer_a: list[str] = ["apple", "cat"]
    test_alphabetizer_b: list[str] = ["car", "angry"]
    assert alphabetizer(test_alphabetizer_b) == {"c": ["car"], "a": ["angry"]}


def test_alphabetizer_two_cases() -> None:
    """Testing Alphabetizer with two use cases."""
    test_alphabetizer_a2: list[str] = ["bear", "dog"]
    test_alphabetizer_b2: list[str] = ["deer", "bee"]
    assert alphabetizer(test_alphabetizer_a2) == {"b": ["bear"], "d": ["dog"]}


def test_empty_update_attendance() -> None:
    """Update attendance empty list should be empty."""
    test_empty_u: str = "Sunday"
    test_empty_u_values: str = "Joe"
    assert update_attendance({}, test_empty_u, test_empty_u_values) == {"Sunday": ["Joe"]}


def test_update_attendance_one_case() -> None:
    """Testing Update attendance with one use case."""
    att: dict[str, list[str]] = {}
    test_update_attendance_a: str = "Monday"
    test_update_attendance_b: str = "Mike"
    assert update_attendance(att, test_update_attendance_a, test_update_attendance_b) == {"Monday": ["Mike"]}


def test_update_attendance_two_cases() -> None:
    """Testing Update attendance with two use cases."""
    att2: dict[str, list[str]] = {}
    test_update_attendance_a2: str = "Tuesday"
    test_update_attendance_b2: str = "Fritz"
    assert update_attendance(att2, test_update_attendance_a2, test_update_attendance_b2) == {"Tuesday": ["Fritz"]}
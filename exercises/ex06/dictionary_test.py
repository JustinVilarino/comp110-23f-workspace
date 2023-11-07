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
    assert invert(test_empty_i, test_empty_i_values) == {"KeyError"}


def test_invert_one_case() -> None:
    """Testing Invert with one use case."""
    test_invert_a: list[str] = ["lebron", "james"]
    test_invert_b: list[str] = ["michael", "jordan"]
    assert invert(test_invert_a, test_invert_b) == {"james": "lebron", "jordan": "michael"}


def test_invert_two_cases() -> None:
    """Testing Invert with two use cases."""
    test_invert_a2: list[str] = ["spongebob", "patrick"]
    test_invert_b2: list[str] = ["squidward", "mr.krabs"]
    assert invert(test_invert_a2, test_invert_b2) == {"patrick": "spongebob", "mr.krabs": "squidward"}


def test_empty_favorite_color() -> None:
    """Favorite color empty list should be empty."""
    test_empty_f: list[str] = ["", ""]
    test_empty_f_values: list[str] = ["", ""]
    assert favorite_color(test_empty_f, test_empty_f_values) == {}


def test_favorite_color_one_case() -> None:
    """Testing Favorite color with one use case."""
    test_favorite_color_a: list[str] = ["Marc", "blue"]
    test_favorite_color_b: list[str] = ["Kris", "blue"]
    assert favorite_color(test_favorite_color_a, test_favorite_color_b) == {"blue"}


def test_favorite_color_two_cases() -> None:
    """Testing Favorite color with two use cases."""
    test_favorite_color_a2: list[str] = ["George", "green"]
    test_favorite_color_b2: list[str] = ["Robert", "green"]
    assert favorite_color(test_favorite_color_a2, test_favorite_color_b2) == {"green"}


def test_empty_count() -> None:
    """Count empty list should be empty."""
    test_empty_c: list[str] = ["", ""]
    test_empty_c_values: list[int] = []
    assert count(test_empty_c, test_empty_c_values) == {}


def test_count_one_case() -> None:
    """Testing Count with one use case."""
    test_count_a: list[str] = ["bananas", "apples"]
    test_count_b: list[int] = [1]
    assert count(test_count_a, test_count_b) == {1}


def test_count_two_cases() -> None:
    """Testing Count with two use cases."""
    test_count_a2: list[str] = ["cars", "cars"]
    test_count_b2: list[int] = [2]
    assert count(test_count_a2, test_count_b2) == {2}


def test_empty_alphabetizer() -> None:
    """Alphabetizer empty list should be empty."""
    test_empty_a: list[str] = ["", ""]
    test_empty_a_values: list[str] = ["", ""]
    assert alphabetizer(test_empty_a, test_empty_a_values) == {}


def test_alphabetizer_one_case() -> None:
    """Testing Alphabetizer with one use case."""
    test_alphabetizer_a: list[str] = ["apple", "cat"]
    test_alphabetizer_b: list[str] = ["car", "angry"]
    assert alphabetizer(test_alphabetizer_a, test_alphabetizer_b) == {"c": "cat" "car", "a": "apple" "angry"}


def test_alphabetizer_two_cases() -> None:
    """Testing Alphabetizer with two use cases."""
    test_alphabetizer_a2: list[str] = ["bear", "dog"]
    test_alphabetizer_b2: list[str] = ["deer", "bee"]
    assert alphabetizer(test_alphabetizer_a2, test_alphabetizer_b2) == {"b": "bear" "bee", "d": "dog" "deer"}


def test_empty_update_attendance() -> None:
    """Update attendance empty list should be empty."""
    test_empty_u: list[str] = [""]
    test_empty_u_values: list[str] = ["", ""]
    assert update_attendance(test_empty_u, test_empty_u_values) == {}


def test_update_attendance_one_case() -> None:
    """Testing Update attendance with one use case."""
    test_update_attendance_a: list[str] = ["Monday"]
    test_update_attendance_b: list[str] = ["Mike", "Jeremy"]
    assert update_attendance(test_update_attendance_a, test_update_attendance_b) == {"Monday": ["Mike", "Jeremy"]}


def test_update_attendance_two_cases() -> None:
    """Testing Update attendance with two use cases."""
    test_update_attendance_a2: list[str] = ["Tuesday"]
    test_update_attendance_b2: list[str] = ["Fritz", "William"]
    assert update_attendance(test_update_attendance_a2, test_update_attendance_b2) == {"Tuesday": ["Fritz", "William"]}
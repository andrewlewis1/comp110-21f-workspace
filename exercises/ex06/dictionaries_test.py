"""Unit tests for dictionary functions."""

__author__ = "730384041"
from exercises.ex06.dictionaries import invert, favorite_color, count


def test_invert_empty_dict() -> None:
    """Tests invert with an input of an empty dictionary."""
    x: dict[str, str] = {}
    assert invert(x) == {}


def test_invert_one_item() -> None:
    """Tests invert with an input of a dictionary with one key and one value."""
    x: dict[str, str] = {"Andrew": "Lewis"}
    assert invert(x) == {"Lewis": "Andrew"}


def test_invert_three_items() -> None:
    """Tests invert with an input of a dictionary with three keys and three values."""
    x: dict[str, str] = {"Andrew": "Lewis", "John": "Doe", "Jane": "Smith"}
    assert invert(x) == {"Lewis": "Andrew", "Doe": "John", "Smith": "Jane"}


def test_favorite_color_all_appear_once() -> None:
    """Tests favorite_color with an input of a dictionary with three different favorite colors that all appear once."""
    x: dict[str, str] = {"Andrew": "red", "James": "blue", "Lewis": "green"}
    assert favorite_color(x) == "red"


def test_favorite_color_two_colors() -> None:
    """Tests favorite_color with an input of a dictionary with two different favorite colors, one of which appears twice."""
    x: dict[str, str] = {"Andrew": "blue", "James": "yellow", "Lewis": "blue"}
    assert favorite_color(x) == "blue"


def test_favorite_color_three_colors() -> None:
    """Tests favorite_color with an input of a dictionary with three different favorite colors, one of which appears twice."""
    x: dict[str, str] = {"Andrew": "orange", "James": "purple", "Lewis": "red", "John": "purple"}
    assert favorite_color(x) == "purple"


def test_count_empty_list() -> None:
    """Tests count with an input of an empty list."""
    x: list[str] = []
    assert count(x) == {}


def test_count_three_items() -> None:
    """Tests count with an input of a list with two different items, one of which appears twice."""
    x: list[str] = ["Andrew", "James", "Andrew"]
    assert count(x) == {"Andrew": 2, "James": 1}


def test_count_five_items() -> None:
    """Tests count with an input of a list with three different items, one of which appears once and one of which appears thrice."""
    x: list[str] = ["Andrew", "James", "Andrew", "Lewis", "Andrew", "James"]
    assert count(x) == {"Andrew": 3, "James": 2, "Lewis": 1}
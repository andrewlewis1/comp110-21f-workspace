"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests

__author__ = "730384041"
from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_all_odds() -> None:
    """This tests only_evens with a list of all odd numbers."""
    x: list[int] = [1, 5, 7, 13]
    assert only_evens(x) == []


def test_only_evens_all_evens() -> None:
    """This tests only_evens with a list of all even numbers."""
    x: list[int] = [2, 4, 8]
    assert only_evens(x) == [2, 4, 8]


def test_only_evens_odds_and_evens() -> None:
    """This tests only_evens with a list of a mixture of even and odd numbers."""
    x: list[int] = [1, 4, 3, 6, 7]
    assert only_evens(x) == [4, 6]


def test_sub_negative_start_zero_end() -> None:
    """This tests sub with a negative start value and an end value of zero."""
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, -2, 0) == []


def test_sub_negative_start_greater_end() -> None:
    """This tests sub with a negative start value and an end value greater than the length of the list."""
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, -1, 7) == [1, 5]


def test_sub_normal() -> None:
    """This tests sub with a start value less than the end value, which are both within the indexes of the list."""
    x: list[int] = [1, 2, 3, 4, 5]
    assert sub(x, 2, 4) == [3, 4]


def test_concat_both_empty() -> None:
    """This tests concat with two empty lists."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_empty_y() -> None:
    """This tests concat with an empty second list."""
    x: list[int] = [10, 20, 30, 40]
    y: list[int] = []
    assert concat(x, y) == x


def test_concat_normal_lists() -> None:
    """This tests concat with two nonempty lists."""
    x: list[int] = [10, 20, 30, 40]
    y: list[int] = [50, 60, 70]
    assert concat(x, y) == [10, 20, 30, 40, 50, 60, 70]
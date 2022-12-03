"""Tests for AoC 1, 2022: Calorie Counting."""

# Standard library imports
import pathlib

# Third party imports
import aoc202201
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202201.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202201.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        "7213",
        "5812",
        "5693",
        "",
        "6447",
        "34832",
        "",
        "14207",
        "",
        "1",
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202201.part1(example1) == 41279


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202201.part2(example1) == 74204


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202201.part2(example2) == 92385
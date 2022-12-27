"""Tests for AoC 5, 2022: Supply Stacks."""

# Standard library imports
import pathlib

# Third party imports
import aoc202205
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202205.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202205.parse_data(puzzle_input)


@pytest.fixture
def lines():
    return (PUZZLE_DIR / "example1.txt").read_text().rstrip().split('\n')


@pytest.fixture
def number_of_stacks(lines):
    floor = aoc202205.get_row_of_floor(lines)
    return (len(lines[floor])-3) // 4 + 1


@pytest.fixture
def stack_string(lines):
    floor = aoc202205.get_row_of_floor(lines)
    return lines[0:floor]

@pytest.fixture
def floor_of_stacks(lines):
    return aoc202205.get_row_of_floor(lines)


@pytest.fixture
def stacks():
    return aoc202205.process_stacks(number_of_stacks, stack_string)

@pytest.fixture
def instruction_string(floor_of_stacks, lines):
    return lines[floor_of_stacks+2::]


def test_get_row_of_floor(lines):
    assert aoc202205.get_row_of_floor(lines) == 3


def test_process_stacks(number_of_stacks, stack_string):
    function_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip().split('\n')
    assert aoc202205.process_stacks(number_of_stacks, stack_string) == [['Z','N'], ['M','C','D'], ['P']]


def test_process_instructions(instruction_string):
    assert aoc202205.process_instructions(instruction_string) == [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)]


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ([['Z','N'], ['M','C','D'], ['P']], [(1, 2, 1), (3, 1, 3), (2, 2, 1), (1, 1, 2)])


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202205.part1(example1) == "CMZ"


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202205.part2(example1) == "MCD"


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202205.part2(example2) == ...

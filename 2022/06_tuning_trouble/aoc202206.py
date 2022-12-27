"""AoC 6, 2022: Tuning Trouble."""

# Standard library imports
import pathlib
import sys

from collections import Counter


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data, k = 4):
    """Solve part 1."""
    for i in range(0, len(data)-k):
        tokens = data[i:i+k]
        collection = Counter(tokens)
        if len(collection) == k:
            return i + k



def part2(data):
    """Solve part 2."""
    return part1(data, k = 14)



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))

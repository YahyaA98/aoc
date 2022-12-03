"""AoC 1, 2022: Calorie Counting."""

# Standard library imports
import pathlib
import sys

from heapq import heappush, heappop


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1."""
    current_max, count = float("-inf"), 0
    for line in data:
        if line == "":
            current_max = max(current_max, count)
            count = 0
        else:
            count = count + int(line)
    return current_max


def part2(data):
    """Solve part 2."""
    h, count = [], 0
    for line in data:
        if line == "":
            heappush(h, count)
            count = 0
        else:
            count = count - int(line)

    return sum(heappop(h) for i in range(3)) * -1


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))

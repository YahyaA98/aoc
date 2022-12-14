"""AoC 4, 2022: Camp Cleanup."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    output = []
    for item in puzzle_input.split("\n"):
        elfA, elfB = item.split(",")
        pair = list(map(int, elfA.split("-"))), list(map(int, elfB.split("-")))
        output.append(pair)
    return output


def part1(data):
    """Solve part 1."""
    count = 0
    for pair in data:
        if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]:
            count += 1
        elif pair[0][0] < pair[1][0] and pair[0][1] > pair[1][1]:
            count += 1
        elif pair[0][0] > pair[1][0] and pair[0][1] < pair[1][1]:
            count += 1
    return count


def part2(data):
    """Solve part 2."""
    overlap = 0
    for pair in data:
        if pair[0][0] == pair[1][0] or pair[0][1] == pair[1][1]:
            overlap += 1
        elif pair[0][0] < pair[1][0] and pair[1][0] <= pair[0][1]:
            overlap += 1
        elif pair[0][0] > pair[1][0] and pair[0][0] <= pair[1][1]:
            overlap += 1
    return overlap


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

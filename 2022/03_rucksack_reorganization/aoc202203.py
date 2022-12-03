"""AoC 3, 2022: Rucksack Reorganization."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split('\n')

def part1(data):
    """Solve part 1."""
    total = 0
    for line in data:
        item_types = set()
        for i in range(0, int(len(line)/2)):
            if line[i] not in item_types:
                item_types.add(line[i])
        for j in range(int(len(line)/2), len(line)):
            if line[j] in item_types:
                if ord(line[j]) <= 90:
                    total += ord(line[j]) - ord('A') + 27
                else:
                    total += ord(line[j]) - ord('a') + 1
                break
    return total

def part2(data):
    """Solve part 2."""
    total = 0
    for i, line in enumerate(data):
        if i % 3 == 0:
            collected = set(line)
        elif i % 3 == 1:
            collected = set.intersection(set(line), collected)
        else:
            collected = set.intersection(set(line), collected)
            for item in collected:         
                if ord(item) <= 90:
                    total += ord(item) - ord('A') + 27
                else:
                    total += ord(item) - ord('a') + 1
                break
    return total

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

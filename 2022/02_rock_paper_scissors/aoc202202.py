"""AoC 2, 2022: Rock Paper Scissors."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [(game[0], game[2]) for game in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1."""
    score = 0
    object_score = {"X": 1, "Y": 2, "Z": 3}
    mapping = {"A": "X", "B": "Y", "C": "Z"}
    rules = {"A": "Z", "C": "Y", "B": "X"}
    for round in data:
        score = score + object_score[round[1]]
        if mapping[round[0]] == round[1]:
            score = score + 3
        elif rules[round[0]] != round[1]:
            score = score + 6
    return score


def part2(data):
    """Solve part 2."""
    score = 0
    outcome = {"X": 0, "Y": 3, "Z": 6}
    score_map = {"A": 1, "B": 2, "C": 3}
    lose_rule = {"A": "C", "B": "A", "C": "B"}
    win_rule = {"A": "B", "B": "C", "C": "A"}
    for round in data:
        score = score + outcome[round[1]]
        if round[1] == "X":
            score = score + score_map[lose_rule[round[0]]]
        elif round[1] == "Y":
            score = score + score_map[round[0]]
        else:
            score = score + score_map[win_rule[round[0]]]
    return score


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

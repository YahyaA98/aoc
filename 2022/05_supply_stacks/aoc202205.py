"""AoC 5, 2022: Supply Stacks."""

# Standard library imports
import pathlib
import sys


def process_stacks(number_of_stacks, stack_string):
    """Parses the block of strings containing the stacks to a list of stacks"""
    stacks = []
    for letter_idx in range(1, number_of_stacks*4, 4):
        stack = []
        for line in stack_string[::-1]:
            if line[letter_idx] != " ":
                stack.append(line[letter_idx])
        stacks.append(stack)
    return stacks


def process_instructions(instructions_string):
    """Given the block of instructions, get the tokens"""
    instructions = []
    for line in instructions_string:
        tokens = line.split(" ")
        instructions.append((int(tokens[1]), int(tokens[3]), int(tokens[5])))
    return instructions


def get_row_of_floor(lines):
    """Given the input as a list of lines, find the floor"""
    row_of_stack_id = 0
    while True:
        line = lines[row_of_stack_id]
        if line[0] == '[':
            while True:
                line = lines[row_of_stack_id]
                if line[0] != '[':
                    break
                row_of_stack_id +=1
            break
        row_of_stack_id +=1
    return row_of_stack_id
    

def parse_data(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    row_of_floor = get_row_of_floor(lines)
    number_of_stacks = (len(lines[row_of_floor])-3) // 4 + 1
    stacks = process_stacks(number_of_stacks, lines[0:row_of_floor])
    instructions = process_instructions(lines[row_of_floor+2::])
    return stacks, instructions
    

def part1(data):
    """Solve part 1."""
    stacks, instructions = data
    for step in instructions:
        for _ in range(0, step[0]):
            token = stacks[step[1]-1].pop()
            stacks[step[2]-1].append(token)
    
    output = ""
    for stack in stacks:
        top_token = stack.pop()
        output+=top_token
    
    return output


def part2(data):
    """Solve part 2."""
    stacks, instructions = data
    for step in instructions:
        temp_stack = []
        for _ in range(0, step[0]):
            token = stacks[step[1]-1].pop()
            temp_stack.append(token)
        stacks[step[2]-1].extend(temp_stack[::-1])

    output = ""
    for stack in stacks:
        if stack != []:
            top_token = stack.pop()
            output+=top_token
        else:
            output+= " "
    
    return output


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    data = parse_data(puzzle_input)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))

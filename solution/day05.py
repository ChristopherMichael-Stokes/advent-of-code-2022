from typing import List, Deque, Tuple
from collections import deque
from dataclasses import dataclass


@dataclass
class Instruction:
    amount: int
    from_index: int
    to_index: int


def parse_input(data: List[str]) -> Tuple[List[Deque[str]], List[Instruction]]:
    # Find the the newline that seperates instructions from the rest of the input
    instructions_start = -1
    for i, line in enumerate(data):
        if line.isspace():
            instructions_start = i
            break

    # Figure out how many queues we need
    n_bins = len(data[instructions_start - 1].split())
    bins: List[Deque[str]] = [deque() for _ in range(n_bins)]

    # Add boxes to the correct stacks
    for line in data[0: instructions_start - 1]:
        # Only look at the indices where we know characters should be 
        for i in range(1, len(line), 4):
            if line[i].isalpha():
                bins[i // 4].appendleft(line[i])

    # Parse instructions
    instructions = []
    for line in data[instructions_start::]:
        if line.isspace():
            continue

        quantities = [int(x) for x in line.split() if x.isnumeric()]
        instructions.append(Instruction(
            amount=quantities[0], from_index=quantities[1] - 1, to_index=quantities[2] - 1))

    return bins, instructions


def part1(data: List[str]) -> str:
    bins, instructions = parse_input(data)

    # Start solution
    for instruction in instructions:
        for _ in range(instruction.amount):
            # Move boxes one at a time
            box = bins[instruction.from_index].pop()
            bins[instruction.to_index].append(box)

    # Get top boxes
    top = ''
    for bin_ in bins:
        top += bin_.pop()

    return top


def part2(data: List[str]) -> str:
    bins, instructions = parse_input(data)

    # Start solution
    for instruction in instructions:
        temp_stack: Deque[str] = deque()

        for _ in range(instruction.amount):
            # Move boxes one at a time to a temp queue
            box = bins[instruction.from_index].pop()
            temp_stack.appendleft(box)
            
        bins[instruction.to_index].extend(temp_stack)

    # Get top boxes
    top = ''
    for bin_ in bins:
        top += bin_.pop()

    return top


if __name__ == '__main__':
    # Read input
    with open('input/day05.txt', 'r') as f:
        data = f.readlines()

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

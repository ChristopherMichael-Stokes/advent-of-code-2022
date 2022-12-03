import os
import os.path as osp
from typing import List
from enum import Enum


class Moves(Enum):
    rock = 1
    paper = 2
    scissors = 3


class States(Enum):
    lose = 0
    draw = 3
    win = 6


def parse_input(data: List[str]) -> List[List[str]]:
    return [line.strip().split(' ') for line in data if not line.isspace()]


def part1(data: List[str]) -> int:
    strategy = parse_input(data)

    move_set = {
        'A': Moves.rock,
        'B': Moves.paper,
        'C': Moves.scissors,
        'X': Moves.rock,
        'Y': Moves.paper,
        'Z': Moves.scissors
    }

    total_score = 0

    for turn in strategy:
        move1, move2 = move_set[turn[0]], move_set[turn[1]]
        if move1 == move2:
            # Draw
            total_score += move1.value + 3
        else:
            # Winning moves
            if (move1 == Moves.rock and move2 == Moves.paper) or (move1 == Moves.paper and move2 == Moves.scissors) or (move1 == Moves.scissors and move2 == Moves.rock):
                total_score += move2.value + 6
            else:
                # Losing move
                total_score += move2.value

    return total_score


def part2(data: List[str]) -> int:
    strategy = parse_input(data)

    move_set = {
        'A': Moves.rock,
        'B': Moves.paper,
        'C': Moves.scissors,
        'X': States.lose,
        'Y': States.draw,
        'Z': States.win
    }

    total_score = 0

    for turn in strategy:
        move, result = move_set[turn[0]], move_set[turn[1]]

        total_score += result.value

        if result == States.draw:
            total_score += move.value
        elif result == States.win:
            if move == Moves.rock:
                total_score += Moves.paper.value
            elif move == Moves.paper:
                total_score += Moves.scissors.value
            elif move == Moves.scissors:
                total_score += Moves.rock.value
        elif result == States.lose:
            if move == Moves.rock:
                total_score += Moves.scissors.value
            elif move == Moves.paper:
                total_score += Moves.rock.value
            elif move == Moves.scissors:
                total_score += Moves.paper.value

    return total_score


if __name__ == '__main__':
    # Read input
    with open('input/day02.txt', 'r') as f:
        data = f.readlines()

    print(f'Part 1, total score: {part1(data)}')
    print(f'Part 2, total score: {part2(data)}')

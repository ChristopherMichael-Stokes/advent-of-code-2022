from typing import List, Tuple, Set
from functools import reduce
from operator import and_


def get_item_value(item: str) -> int:
    if item.isupper():
        return ord(item) - (ord('A') - 1)  + 26
    else:
        return ord(item) - (ord('a') - 1)


def part1(data: List[str]) -> int:
    bags: List[Tuple[Set[str], Set[str]]] = []

    for line in data:
        bags.append((set(line[0:len(line)//2]), set(line[len(line)//2: len(line)])))

    priority_sum = 0

    for bag in bags:
        shared_items = bag[0] & bag[1]
        
        priorities = 0 
        for item in shared_items:
            priorities += get_item_value(item)

        priority_sum += priorities

    return priority_sum


def part2(data: List[str]) -> int:
    group_size, groups = 3, []

    for i in range(group_size):
        groups.append(data[i::group_size])

    groups = list(zip(*groups)) # type: ignore

    badge_id_sum = 0
    for group in groups:
        unique_values = reduce(and_, [set(bag) for bag in group])
            
        # As per the input, we should only expect a single
        # unique value
        badge_id = unique_values.pop()
        badge_id_sum += get_item_value(badge_id)

    return badge_id_sum


if __name__ == '__main__':
    # Read input
    with open('input/day03.txt', 'r') as f:
        data = [line.strip() for line in f.readlines() if not line.isspace()]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

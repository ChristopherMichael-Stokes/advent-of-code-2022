from typing import List


def get_overlaps(data: List[str], overlap_func) -> int:
    pairs = [line.split(',') for line in data]
    
    overlaps = 0

    for pair in pairs:
        # Parse A-B to integer pairs
        first = [int(x) for x in pair[0].split('-')]
        second = [int(x) for x in pair[1].split('-')]

        # Check overlaps for both pairs
        if overlap_func(first, second) or overlap_func(second, first):
            overlaps += 1

    return overlaps 


def part1(data: List[str]) -> int:
    # Find if one range is a complete subset of another
    is_superset = lambda x, y: max(x) >= max(y) and min(x) <= min(y)

    return get_overlaps(data, is_superset)


def part2(data: List[str]) -> int:
    # Find if there's any point of intersection between
    # two ranges
    is_intersecting = lambda x, y: max(x) >= min(y) and min(x) <= max(y)

    return get_overlaps(data, is_intersecting)


if __name__ == '__main__':
    # Read input
    with open('input/day04.txt', 'r') as f:
        data = [line.strip() for line in f.readlines() if not line.isspace()]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

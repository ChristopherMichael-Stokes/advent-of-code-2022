from typing import List


def find_groups(data: List[str]) -> List[List[int]]:
    # Find the set of grouped consecutive items that leads to the biggest sum
    new_group_flag = True
    groups: List[List[int]] = []

    for value in data:
        if not value.isspace():
            if new_group_flag:
                groups.append([])
                new_group_flag = False

            groups[-1].append(int(value))
        else:
            new_group_flag = True

    return groups


def part1(data: List[str]) -> int:
    groups = find_groups(data)

    # Find top valued group
    return max([sum(group) for group in groups])


def part2(data: List[str]) -> int:
    groups = find_groups(data)

    # Find all group sums
    groups = [sum(group) for group in groups]
    groups.sort()
    
    # Get largest three values
    return sum(groups[-3:])


if __name__=='__main__':

    input_file = 'input/day01.txt'

    with open(input_file, 'r') as f:
        data = f.readlines()

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

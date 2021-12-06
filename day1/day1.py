from typing import List


def read_puzzle_input(path_to_puzzle: str) -> List[int]:
    with open(path_to_puzzle, "r") as data:
        depths = [int(depth.strip("\n")) for depth in data]
    return depths


def count_how_many_increases(depths: List) -> int:
    count = 0
    for index, depth in enumerate(depths):
        if index == 0:
            pass
        elif depth > depths[index - 1]:
            count += 1
    return count


def solve_part_1(path_to_puzzle: str) -> int:
    return count_how_many_increases(read_puzzle_input(path_to_puzzle))


def calculate_groups_of_3(depths: List[int]) -> List[int]:
    grouped_depths = []
    for index, depth in enumerate(depths):
        if index == len(depths) - 2:
            return grouped_depths
        grouped_depths.append(sum(depths[index : index + 3]))


def solve_part_2(path_to_puzzle):
    grouped_depths = calculate_groups_of_3(read_puzzle_input(path_to_puzzle))
    return count_how_many_increases(grouped_depths)


if __name__ == "__main__":
    print(solve_part_1("day1/puzzle-input.txt"))

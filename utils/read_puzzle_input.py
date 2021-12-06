from typing import List


def read_puzzle_input(path_to_puzzle: str) -> List[int]:
    with open(path_to_puzzle, "r") as data:
        items = [int(item.strip("\n")) for item in data]
    return items

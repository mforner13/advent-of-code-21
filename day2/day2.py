from typing import List


def read_puzzle_input(path_to_puzzle: str) -> List[int]:
    with open(path_to_puzzle, "r") as data:
        items = [item.strip("\n") for item in data]
    return items


class Position:
    def __init__(self) -> None:
        self.horizontal = 0
        self.depth = 0

    def forward(self, amount):
        # increases the horizontal position by X units
        self.horizontal += amount
        return None

    def up(self, amount):
        # decreases the depth by X units.
        self.depth -= amount
        return None

    def down(self, amount):
        # increases the depth by X units.
        self.depth += amount
        return None

    def read_command(self, command):
        # apply a function depending on the string passed
        direction, amount = command.split(" ")
        func_to_call = getattr(self, direction)
        func_to_call(int(amount))
        return None


def solve(path_to_input):
    position = Position()
    commands = read_puzzle_input(path_to_input)
    for command in commands:
        position.read_command(command)
    return [position.horizontal, position.depth]


if __name__ == "__main__":
    print(solve("day2/puzzle-input.txt"))

april = [1, 2, 3, 4]

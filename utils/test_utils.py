import pytest

from utils.read_puzzle_input import read_puzzle_input


@pytest.fixture
def list_of_depths():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_read_puzzle_input(list_of_depths):
    expected_output = list_of_depths
    assert read_puzzle_input("./day1/tests/fixtures.txt") == expected_output

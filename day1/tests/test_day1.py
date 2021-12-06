import pytest
from ..day1 import (
    read_puzzle_input,
    count_how_many_increases,
    calculate_groups_of_3,
)


@pytest.fixture
def list_of_depths():
    return [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_read_puzzle_input(list_of_depths):
    expected_output = list_of_depths
    assert read_puzzle_input("./day1/tests/fixtures.txt") == expected_output


def test_count_how_many_increases(list_of_depths):
    assert count_how_many_increases(list_of_depths) == 7


def test_calculate_groups_of_3(list_of_depths):
    grouped_depths = [607, 618, 618, 617, 647, 716, 769, 792]
    assert calculate_groups_of_3(list_of_depths) == grouped_depths

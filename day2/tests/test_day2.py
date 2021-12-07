import pytest

from ..day2 import Position


@pytest.fixture
def position():
    return Position()


def test_forward(position):
    # increases the horizontal position by X units
    position.forward(5)
    assert position.horizontal == 5


def test_up(position):
    # decreases the depth by X units.
    position.up(5)
    assert position.depth == -5


def test_down(position):
    # increases the depth by X units.
    position.down(5)
    assert position.depth == 5


@pytest.mark.parametrize(
    "command, direction, expected_value",
    (("forward 5", "horizontal", 5), ("up 5", "depth", -5), ("down 5", "depth", 5)),
)
def test_read_command(position, command, direction, expected_value):
    position.read_command(command)
    assert getattr(position, direction) == expected_value

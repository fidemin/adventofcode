import pytest

from day02.solution1 import parse_row_and_max_cube_count


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', (1, 4, 2, 6)),
        ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', (3, 20, 13, 6)),
        ('Game 4: 8 green, 6 blue, 20 red', (4, 20, 8, 6)),
        ('Game 5: 8 green', (5, 0, 8, 0)),
    ]
)
def test_parse_row_and_max_cube_count(test_input, expected):
    actual = parse_row_and_max_cube_count(test_input)
    assert actual == expected

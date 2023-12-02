import pytest

from day01.solution2 import extract_digit


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ('nodigitstring', (None, None)),
        ('eightwothree', (8, 3)),
        ('abcone2threexyz', (1, 3)),
        ('abctwothreeandoneandthreexyz', (2, 3)),
        ('zoneight234', (1, 4))

    ]
)
def test_extract_digit(test_input, expected):
    first = extract_digit(test_input)
    last = extract_digit(test_input, first=False)
    assert (first, last) == expected

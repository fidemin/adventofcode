import os

import pytest

from . import main


def assert_list(actual, expected):
    assert len(actual) == len(expected)
    for a, b in zip(actual, expected):
        if isinstance(a, list) and isinstance(b, list):
            assert_list(a, b)
        else:
            assert a == b


def test_input_of_calories():
    test_file_name = os.path.join(os.path.dirname(__file__), 'test.txt')
    actual = main.parse_input_of_calories(test_file_name)
    expected = [[100], [200, 300], [20, 30, 50]]
    assert_list(actual, expected)


@pytest.mark.parametrize(
    "test_input,expected", [([], 0), ([[100]], 100), ([[100, 200], [50], [100, 300]], 400)]
)
def test_extract_max_calories(test_input, expected):
    assert main.extract_max_calories(test_input) == expected


import pytest

from . import main


@pytest.mark.parametrize(
    "test_input,expected", [([], 0), ([[100]], 100), ([[100, 200], [50], [100, 300]], 400)]
)
def test_extract_max_calories(test_input, expected):
    assert main.extract_max_calories(test_input) == expected


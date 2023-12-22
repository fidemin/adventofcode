import pytest

from day06.solution1 import number_of_wins


@pytest.mark.parametrize('test_t,test_d,expected', [
    (7, 9, 4),
    (15, 40, 8),
    (30, 200, 9)
])
def test_number_of_wins(test_t, test_d, expected):
    actual = number_of_wins(test_t, test_d)
    assert actual == expected

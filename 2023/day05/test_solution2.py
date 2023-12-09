import pytest

from day05.solution2 import parse_seeds_row, parse_numbers_str, parse_map_strs, RangeConverter, RangeUtil


@pytest.mark.parametrize('test_input,expected', [
    ([[1, 2], [10, 11]], [[1, 2]]),
    ([[1, 2], [2, 11]], [[1, 1], [2, 2]]),
    ([[1, 10], [4, 5]], [[1, 3], [4, 5], [6, 10]]),
    ([[1, 10], [4, 10]], [[1, 3], [4, 10]]),
    ([[4, 10], [1, 2]], [[4, 10]]),
    ([[4, 10], [1, 4]], [[4, 4], [5, 10]]),
    ([[4, 10], [1, 5]], [[4, 5], [6, 10]]),
])
def test_cut(test_input, expected):
    r = test_input[0]
    cutter = test_input[1]

    actual = RangeUtil.cut_one(r, cutter)
    _assert_list(actual, expected)


class TestRangeConverter:
    def test_init(self):
        map_ranges = [[50, 98, 2], [52, 50, 48]]

        converter = RangeConverter(map_ranges)

        expected_ranges = [[98, 99, 50], [50, 97, 52]]

        _assert_list(converter.ranges, expected_ranges)

    @pytest.mark.parametrize('test_input,expected', [
        ([3, 4], [3, 4]),
        ([48, 49], [48, 49]),
        ([50, 51], [52, 53]),
        ([97, 97], [99, 99]),
        ([98, 99], [50, 51]),
        ([100, 120], [100, 120]),
    ])
    def test_convert(self, test_input, expected):
        map_ranges = [[50, 98, 2], [52, 50, 48]]

        converter = RangeConverter(map_ranges)

        actual = converter.convert(test_input)

        _assert_list(actual, expected)


@pytest.mark.parametrize('test_input,expected', [
    ('79', [79]),
    ('79 14 55 13', [79, 14, 55, 13]),
    # random spaces
    ('79    14   55', [79, 14, 55])
])
def test_parse_numbers_str(test_input, expected):
    actual = parse_numbers_str(test_input)

    assert len(actual) == len(expected)
    assert all([actual[i] == expected[i] for i in range(len(expected))])


@pytest.mark.parametrize('test_input,expected', [
    ('seeds: 79 14 55 13', [[79, 92], [55, 67]]),
])
def test_parse_seeds_row(test_input, expected):
    actual = parse_seeds_row(test_input)

    print(actual)
    assert len(actual) == len(expected)
    for i in range(len(actual)):
        _assert_list(actual[i], expected[i])


def test_parse_map_strs():
    test_input = [
        'light-to-temperature map:',
        '45 77 23',
        '81 45 19',
        '68 64 13'
    ]

    expected = ('light', 'temperature', [[45, 77, 23], [81, 45, 19], [68, 64, 13]])

    actual = parse_map_strs(test_input)

    assert expected[0] == actual[0]
    assert expected[1] == actual[1]
    actual_map_ranges = actual[2]
    expected_map_ranges = expected[2]

    assert len(actual_map_ranges) == len(expected_map_ranges)
    for i in range(len(actual_map_ranges)):
        _assert_list(expected_map_ranges[i], actual_map_ranges[i])


def _assert_list(l1, l2):
    if type(l1) != type(l2):
        raise AssertionError(f'{l1} and {l2} types are not equal')
    if not isinstance(l1, list) and not isinstance(l2, list):
        assert l1 == l2
        return

    assert len(l1) == len(l2)
    [_assert_list(l1[i], l2[i]) for i in range(len(l1))]

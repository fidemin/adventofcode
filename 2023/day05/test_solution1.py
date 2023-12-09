import pytest

from day05.solution1 import parse_seeds_row, parse_numbers_str, parse_map_strs, RangeConverter


class TestRangeConverter:
    def test_init(self):
        map_ranges = [[50, 98, 2], [52, 50, 48]]

        converter = RangeConverter(map_ranges)

        expected_ranges = [[98, 99, 50], [50, 97, 52]]

        assert len(converter.ranges) == len(expected_ranges)
        for i in range(len(expected_ranges)):
            _assert_list(converter.ranges[i], expected_ranges[i])

    @pytest.mark.parametrize('test_input,expected', [
        (3, 3),
        (49, 49),
        (50, 52),
        (51, 53),
        (97, 99),
        (98, 50),
        (99, 51),
        (100, 100),
        (120, 120)
    ])
    def test_convert(self, test_input, expected):
        map_ranges = [[50, 98, 2], [52, 50, 48]]

        converter = RangeConverter(map_ranges)

        actual = converter.convert(test_input)

        assert actual == expected


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
    ('seeds: 79', [79]),
    ('seeds: 79 14 55 13', [79, 14, 55, 13]),
    # random spaces
    ('seeds: 79    14   55', [79, 14, 55])
])
def test_parse_seeds_row(test_input, expected):
    actual = parse_seeds_row(test_input)

    assert len(actual) == len(expected)
    assert all([actual[i] == expected[i] for i in range(len(expected))])


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
    assert len(l1) == len(l2)
    assert all([l1[i] == l2[i] for i in range(len(l1))])

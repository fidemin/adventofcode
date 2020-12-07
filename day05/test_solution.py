from .solution import calculate_seat_id


def test_calculate_seat_id():
    chars = 'BFFFBBFRRR'
    assert 567 == calculate_seat_id(chars)
    chars = 'FFFBBBFRRR'
    assert 119 == calculate_seat_id(chars)
    chars = 'BBFFBBFRLL'
    assert 820 == calculate_seat_id(chars)




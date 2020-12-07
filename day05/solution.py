

def binary_chars_to_int(left_char: str, right_char: str, chars: str):
    min_value = 0
    max_value = 2 ** len(chars) - 1
    for char in chars:
        if char == left_char:
            max_value = (min_value + max_value) // 2
        elif char == right_char:
            min_value = (min_value + max_value) // 2 + 1
        else:
            assert False, f'{left_char}, {right_char} is only accepted. not {char}'
    assert min_value == max_value
    return min_value


def calculate_seat_id(seat_chars: str):
    row_num = binary_chars_to_int('F', 'B', seat_chars[:7])
    col_num = binary_chars_to_int('L', 'R', seat_chars[7:])
    return row_num * 8 + col_num


if __name__ == '__main__':
    max_seat_id = 0
    with open('input.txt', 'r') as f:
        for row in f:
            seat_id = calculate_seat_id(row.strip())
            max_seat_id = max(max_seat_id, seat_id)

    print(max_seat_id)

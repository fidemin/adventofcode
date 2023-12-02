from day01.common import preprocess


def extract_digits_of_int(string: str):
    """
    extract first and last digits in string

    :param string:
    :return:
    """
    first_pos_digit = extract_digit(string)
    last_pos_digit = extract_digit(string, first=False)
    return first_pos_digit, last_pos_digit


def extract_digit(string: str, first=True):
    length = len(string)

    start = 0
    end = length
    step = 1

    if not first:
        start = length - 1
        end = -1
        step = -1

    for i in range(start, end, step):
        char = string[i]

        try:
            digit = int(char)
            return digit
        except ValueError:
            continue

    return None


def extract_calibration_value(string: str):
    first_digit, last_digit = extract_digits_of_int(string)
    return first_digit * 10 + last_digit


def solve(filename):
    with open(filename, 'r') as f:
        rows = preprocess(f)

    total = 0
    for row in rows:
        calibration_value = extract_calibration_value(row)
        total += calibration_value

    return total

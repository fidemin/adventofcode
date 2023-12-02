from common import preprocess


def extract_digits(string: str):
    """
    extract first and last digits in string

    :param string:
    :return:
    """
    first_digit = extract_digit(string)
    last_digit = extract_digit(string, first=False)
    return first_digit, last_digit


def extract_digit(string: str, first=True):
    length = len(string)

    digit = None
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
        except ValueError:
            continue

        break
    return digit


def extract_calibration_value(string: str):
    first_digit, last_digit = extract_digits(string)
    return first_digit * 10 + last_digit


def solution1(filename):
    with open(filename, 'r') as f:
        rows = preprocess(f)

    total = 0
    for row in rows:
        calibration_value = extract_calibration_value(row)
        total += calibration_value

    return total

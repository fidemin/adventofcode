from day01.common import preprocess

digit_string_to_digit = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

digit_string_tree = {
    'o': ['one'],
    't': ['two', 'three'],
    'f': ['four', 'five'],
    's': ['six', 'seven'],
    'e': ['eight'],
    'n': ['nine']
}

reversed_digit_string_tree = {
    'e': ['one', 'three', 'five', 'nine'],
    'o': ['two'],
    'r': ['four'],
    'x': ['six'],
    'n': ['seven'],
    't': ['eight']
}


def extract_digit_of_string_from_current_as_start(string: str, current: int):
    char = string[current]

    if char not in digit_string_tree:
        return None

    digit_strs = digit_string_tree[char]
    str_start = current

    for digit_str in digit_strs:
        str_end = str_start + len(digit_str)
        if str_end > len(string):
            return None
        possible_digit_str = string[str_start:str_end]
        if digit_str == possible_digit_str:
            return digit_string_to_digit[digit_str]


def extract_digit_of_string_from_current_as_end(string: str, current: int):
    char = string[current]

    if char not in reversed_digit_string_tree:
        return None

    digit_strs = reversed_digit_string_tree[char]
    str_end = current + 1

    for digit_str in digit_strs:
        str_start = str_end - len(digit_str)
        if str_start < 0:
            return None
        possible_digit_str = string[str_start:str_end]
        if digit_str == possible_digit_str:
            return digit_string_to_digit[digit_str]


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
            # deal with digit of int
            digit = int(char)
            return digit
        except ValueError:
            # deal with digit of string
            if first:
                first_digit = extract_digit_of_string_from_current_as_start(string, i)
                if first_digit is not None:
                    return first_digit
            else:
                last_digit = extract_digit_of_string_from_current_as_end(string, i)
                if last_digit is not None:
                    return last_digit

    return None


def extract_digits(string: str):
    """
    extract first and last digits in string

    :param string:
    :return:
    """
    first_digit = extract_digit(string)
    last_digit = extract_digit(string, first=False)
    return first_digit, last_digit


def extract_calibration_value(string: str):
    first_digit, last_digit = extract_digits(string)

    return first_digit * 10 + last_digit


def solve(filename):
    with open(filename, 'r') as f:
        rows = preprocess(f)

    total = 0
    for row in rows:
        calibration_value = extract_calibration_value(row)
        total += calibration_value

    return total

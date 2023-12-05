def preprocess(file):
    for line in file:
        yield line.strip()


def get_number_of_winning_numbers_matched(wining_numbers: list[int], numbers: list[int]):
    winning_set = set(wining_numbers)
    count = 0
    for number in numbers:
        if number in winning_set:
            count += 1

    return count


def calculate_point(number_of_wins: int):
    if number_of_wins == 0:
        return 0
    return 2 ** (number_of_wins - 1)


def numbers_str_to_list(nums_str: str):
    result = []
    for num_str in nums_str.strip().split(' '):
        if num_str != '':
            result.append(int(num_str))
    return result


def parse_row(row: str):
    """
    :param row: e.g. 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'
    :return:
    """

    _, numbers_pair_str = row.split(': ')
    winning_numbers_str, numbers_str = numbers_pair_str.split(' | ')
    winning_numbers = numbers_str_to_list(winning_numbers_str)
    numbers = numbers_str_to_list(numbers_str)
    return winning_numbers, numbers


def solve(filepath):
    total = 0
    with open(filepath, 'r') as f:
        for row in preprocess(f):
            winning_numbers, numbers = parse_row(row)
            number_of_winnings = get_number_of_winning_numbers_matched(winning_numbers, numbers)
            total += calculate_point(number_of_winnings)

    return total

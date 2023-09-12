import sys


def parse_input_of_calories(filename):
    with open(filename, 'r') as f:
        calories_for_elfs = []
        calories_for_elf = []
        for row in f:
            row = row.strip()
            if len(row) == 0:
                calories_for_elfs.append(calories_for_elf)
                calories_for_elf = []
            else:
                calories_for_elf.append(int(row))

        if len(calories_for_elf) != 0:
            calories_for_elfs.append(calories_for_elf)
        return calories_for_elfs


def extract_max_calories(calories_for_elfs):
    """
    :param calories_for_elfs: calories for elfs. e.g. [[100, 200], [100], [300, 400]]
    :return: max calories for one elf
    """
    current_max = 0

    for calories_for_elf in calories_for_elfs:
        current_max = max(current_max, sum(calories_for_elf))

    return current_max


if __name__ == '__main__':
    """
    e.g.)
    python main.py p1 input1.txt
    python main.py p2 input2.txt
    """
    arguments = sys.argv
    part = arguments[1]  # should be p1 or p2
    input_file_name = arguments[2]

    if part == 'p1':
        calories = parse_input_of_calories(input_file_name)
        print('Result')
        print(extract_max_calories(calories))
    elif part == 'p2':
        raise NotImplementedError('p2 is not implemented yet')
    else:
        raise RuntimeError('{part} is not proper problem argument'.format(part=part))

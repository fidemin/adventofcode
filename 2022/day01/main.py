

def extract_max_calories(calories_for_elfs):
    """
    :param calories_for_elfs: calories for elfs. e.g. [[100, 200], [100], [300, 400]]
    :return: max calories for one elf
    """
    current_max = 0

    for calories_for_elf in calories_for_elfs:
        current_max = max(current_max, sum(calories_for_elf))

    return current_max



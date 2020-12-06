
def extract_key_set(input_str: str) -> set:
    input_str = input_str.strip().replace('\n', ' ')
    key_value_strs = [key_value_str for key_value_str in input_str.split(' ') if key_value_str]

    key_set = set()
    for key_value_str in key_value_strs:
        key_value = key_value_str.split(':')
        key_set.add(key_value[0].strip())
    return key_set


def is_valid_passport(input_str: str):
    valid_passport_key_set = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    key_set = extract_key_set(input_str)
    if valid_passport_key_set - key_set:
        return False
    return True


def passport_parser(file) -> iter:
    passport_str_lst = []
    for row in file:
        if row == '\n':
            yield ' '.join(passport_str_lst)
            passport_str_lst = []
        else:
            passport_str_lst.append(row.strip())
    if passport_str_lst:
        yield ' '.join(passport_str_lst)


if __name__ == '__main__':
    count = 0
    with open('input.txt', 'r') as f:
        for passport_str in passport_parser(f):
            if is_valid_passport(passport_str):
                count += 1
    print(count)

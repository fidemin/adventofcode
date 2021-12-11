from .solution import extract_key_set, is_valid_passport


def test_extract_key_set():
    input_string = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017\ncid:147 hgt:183cm\n'
    result = extract_key_set(input_string)
    assert {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'} == result


def test_is_valid_passport():
    input_str = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm'
    assert is_valid_passport(input_str)
    input_str = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929'
    assert not is_valid_passport(input_str)




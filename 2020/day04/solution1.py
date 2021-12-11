import re


class Passport:
    @staticmethod
    def from_str(passport_str: str):
        input_str = passport_str.strip().replace('\n', ' ')
        key_value_strs = [key_value_str for key_value_str in input_str.split(' ') if key_value_str]

        input_dict = {}
        for key_value_str in key_value_strs:
            key_value = key_value_str.split(':')
            key = key_value[0].strip()
            value = key_value[1].strip()
            input_dict[key] = value
        return Passport(**input_dict)

    def __init__(self, *, byr=None, iyr=None, eyr=None, hgt=None, hcl=None, ecl=None, pid=None, cid=None):
        self._byr = byr
        self._iyr = iyr
        self._eyr = eyr
        self._hgt = hgt
        self._hcl = hcl
        self._ecl = ecl
        self._pid = pid

    def is_valid(self):
        return self._is_valid_byr() and self._is_valid_ecl() and self._is_valid_eyr() \
            and self._is_valid_hcl() and self._is_valid_hgt() and self._is_valid_iyr() \
            and self._is_valid_pid()

    def _is_valid_byr(self):
        if self._byr is None:
            return False
        try:
            byr_int = int(self._byr)
        except ValueError:
            return False
        return 1920 <= byr_int <= 2002

    def _is_valid_iyr(self):
        if self._iyr is None:
            return False
        try:
            iyr_int = int(self._iyr)
        except ValueError:
            return False
        return 2010 <= iyr_int <= 2020

    def _is_valid_eyr(self):
        if self._eyr is None:
            return False
        try:
            eyr_int = int(self._eyr)
        except ValueError:
            return False
        return 2020 <= eyr_int <= 2030

    def _is_valid_hgt(self):
        if self._hgt is None:
            return False
        hgt_unit = self._hgt[-2:]
        try:
            hgt_int = int(self._hgt.rstrip(hgt_unit))
        except ValueError:
            return False
        if hgt_unit == 'cm':
            return 150 <= hgt_int <= 193
        else:
            return 59 <= hgt_int <= 76

    def _is_valid_hcl(self):
        if self._hcl is None:
            return False

        return re.match(r'^#[0-9a-f]{6}$', self._hcl) is not None

    def _is_valid_ecl(self):
        if self._ecl is None:
            return False
        return self._ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def _is_valid_pid(self):
        if self._pid is None:
            return False

        return re.match(r'^[0-9]{9}$', self._pid) is not None


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
            passport = Passport.from_str(passport_str)

            if passport.is_valid():
                count += 1
    print(count)

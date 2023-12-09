def preprocess(file):
    return [line.strip() for line in file]


def parse_numbers_str(numbers_str: str):
    numbers = []
    for num_str in numbers_str.strip().split(' '):
        if num_str.strip():
            numbers.append(int(num_str.strip()))
    return numbers


class RangeUtil:
    @staticmethod
    def cut_one(r, cutter):
        c1 = cutter[0]

        if c1 <= r[0]:
            temp_ranges = [r]
        elif c1 == r[0]:
            temp_ranges = [r]
        elif r[1] >= c1 > r[0]:
            temp_ranges = [[r[0], c1 - 1], [c1, r[1]]]
        else:  # c1 > r[1]:
            temp_ranges = [r]

        second_result = []

        c2 = cutter[1]
        for r in temp_ranges:
            if c2 < r[0]:
                second_result.append(r)
            elif r[1] > c2 >= r[0]:
                second_result.extend([[r[0], c2], [c2 + 1, r[1]]])
            else:  # c2 >= r[1]:
                second_result.append(r)

        return second_result


def parse_seeds_row(row: str):
    _, numbers_str = row.split(': ')
    nums = parse_numbers_str(numbers_str)

    # pair -> inclusive range [start, end]
    pair = None
    seeds = []
    for i, num in enumerate(nums):
        if i % 2 == 0:
            pair = [num, None]
        else:
            pair[1] = pair[0] + num - 1
            seeds.append(pair)
    return seeds


def parse_map_strs(map_strs: list[str]):
    first_row = map_strs[0]
    source_to_dest_str = first_row.split(' ')[0].strip()
    source, dest = source_to_dest_str.split('-to-')

    map_ranges = []
    for i in range(1, len(map_strs)):
        map_ranges.append(parse_numbers_str(map_strs[i]))

    return source, dest, map_ranges


def parse(rows):
    first_row = rows[0]
    seeds = parse_seeds_row(first_row)

    map_strs = []
    map_tuples = []
    for i in range(1, len(rows)):
        row = rows[i]
        if len(row.strip()) == 0:
            if map_strs:
                map_tuple = parse_map_strs(map_strs)
                map_tuples.append(map_tuple)
                map_strs = []
            continue

        map_strs.append(row)

    if map_strs:
        map_tuple = parse_map_strs(map_strs)
        map_tuples.append(map_tuple)

    return seeds, map_tuples


class RangeMapElement:
    def __init__(self, source, dest, map_ranges):
        self.source = source
        self.dest = dest
        self.range_converter = RangeConverter(map_ranges)

    def get_dest_value(self, source_value_ranges):
        cut_source_value_ranges = self.range_converter.cut(source_value_ranges)
        dests = []

        for value_range in cut_source_value_ranges:
            dests.append(self.range_converter.convert(value_range))

        return dests


class RangeConverter:
    def __init__(self, map_ranges):
        self.ranges = [self._map_range_to_ranges(map_range) for map_range in map_ranges]

    @staticmethod
    def _map_range_to_ranges(map_range):
        dest_start, source_start, length = map_range
        source_end = source_start + length - 1
        return [source_start, source_end, dest_start]

    def cut(self, value_ranges):
        ranges = value_ranges

        for source_start, source_end, _ in self.ranges:
            new_ranges = []
            for r in ranges:
                new_ranges.extend(RangeUtil.cut_one(r, [source_start, source_end]))

            # pass new ragnes to next source range's input
            ranges = new_ranges
        return ranges

    def convert(self, value_range):
        for source_start, source_end, dest_start in self.ranges:
            value_range0_check = source_start <= value_range[0] <= source_end
            value_range1_check = source_start <= value_range[1] <= source_end
            if value_range0_check != value_range1_check:
                raise ValueError(f'{value_range} is not proper value')
            if value_range0_check <= source_end and value_range1_check:
                return [dest_start + value_range[0] - source_start, dest_start + value_range[1] - source_start]
        return value_range


def create_range_map(map_tuples: list):
    range_map = {}

    for map_tuple in map_tuples:
        source, dest, map_ranges = map_tuple
        ele = RangeMapElement(source, dest, map_ranges)
        range_map[source] = ele
    return range_map


def solve(filepath):
    with open(filepath, 'r') as f:
        rows = preprocess(f)

    seeds, map_tuples = parse(rows)
    range_map = create_range_map(map_tuples)

    source_values = seeds
    source = 'seed'

    while True:
        range_map_ele = range_map[source]
        dest = range_map_ele.dest
        dest_values = range_map_ele.get_dest_value(source_values)
        # print(source, dest, source_values, dest_values)
        if dest == 'location':
            dest_values.sort()
            return dest_values[0][0]
        source = dest
        source_values = dest_values

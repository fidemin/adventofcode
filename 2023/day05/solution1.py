def preprocess(file):
    return [line.strip() for line in file]


def parse_numbers_str(numbers_str: str):
    numbers = []
    for num_str in numbers_str.strip().split(' '):
        if num_str.strip():
            numbers.append(int(num_str.strip()))
    return numbers


def parse_seeds_row(row: str):
    _, numbers_str = row.split(': ')

    return parse_numbers_str(numbers_str)


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

    def get_dest_value(self, source_value: int) -> int:
        return self.range_converter.convert(source_value)


class RangeConverter:
    def __init__(self, map_ranges):
        self.ranges = [self._map_range_to_ranges(map_range) for map_range in map_ranges]

    @staticmethod
    def _map_range_to_ranges(map_range):
        dest_start, source_start, length = map_range
        source_end = source_start + length - 1
        return [source_start, source_end, dest_start]

    def convert(self, source_value):
        for source_start, source_end, dest_start in self.ranges:
            if source_start <= source_value <= source_end:
                return dest_start + source_value - source_start

        return source_value


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

    result = float('inf')

    for seed in seeds:
        source_value = seed
        source = 'seed'

        while True:
            range_map_ele = range_map[source]
            dest = range_map_ele.dest
            dest_value = range_map_ele.get_dest_value(source_value)
            if dest == 'location':
                result = min(result, dest_value)
                break

            source = dest
            source_value = dest_value

    return result

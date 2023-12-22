import math
import re


def number_of_wins(t: int, d: int):
    t = t * 1.0
    d = d * 1.0

    # solve this mathematically (t +- sqrt(t^2 - 4d)) / 2
    raw_min = (t - math.sqrt(t ** 2 - 4 * d)) / 2.0
    raw_max = (t + math.sqrt(t ** 2 - 4 * d)) / 2.0
    # print(raw_max, raw_min)

    min_, max_ = math.ceil(raw_min), int(raw_max)
    if min_ == raw_min:
        min_ = min_ + 1
    if max_ == raw_max:
        max_ = max_ - 1
    # print(max_, min_)

    return max_ - min_ + 1


def preprocess(f):
    return [line.strip() for line in f]


def parse_row(r: str):
    _, ints_str = r.split(':')

    int_str_list = re.split(r'\W+', ints_str.strip())
    return [int(s) for s in int_str_list]


def solve(filepath):
    with open(filepath, 'r') as f:
        rows = preprocess(f)

    time_row = rows[0]
    times = parse_row(time_row)
    distance_row = rows[1]
    distances = parse_row(distance_row)

    result = 1

    for t, d in zip(times, distances):
        result *= number_of_wins(t, d)

    return result

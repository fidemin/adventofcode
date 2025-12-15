
def solve_part1(inputs):
    result = 0

    for range_str in inputs:
        min_str = range_str[0]
        max_str = range_str[1]

        n1 = len(min_str)
        n2 = len(max_str)

        for i in range(n1, n2+1):
            if i % 2 == 1:
                continue

            if i == n1:
                start_str = min_str
            else:
                start_str = "1" + "0" * (i - 1)

            if i == n2:
                end_str = max_str
            else:
                end_str = "9" * i

            half_str = start_str[:len(start_str)//2]

            while True:
                if int(half_str * 2) < int(start_str):
                    half_int = int(half_str)
                    half_int += 1
                    half_str = str(half_int)
                    continue


                if int(half_str * 2) > int(end_str):
                    break

                result += int(half_str * 2)

                if int(half_str * 2) == int(end_str):
                    break

                half_int = int(half_str)
                half_int += 1
                half_str = str(half_int)










        min_val = int(min_str)
        max_val = int(max_str)

    return result


def solve_part2(inputs):
    raise NotImplementedError


def solve(part, sample=False):
    if sample:
        file_path = 'aoc2025/day02/sample.txt'
    else:
        file_path = 'aoc2025/day02/input.txt'

    inputs = []
    with open(file_path) as f:
        row = f.readline().strip()
        inputs = [range.split("-") for range in row.split(",")]

    if part == 'part1':
        result = solve_part1(inputs)
    else:
        result = solve_part2(inputs)

    return result

from day02.common import preprocess, parse_row_and_max_cube_count


def solve(filename):
    with open(filename) as f:
        rows = preprocess(f)

    # only 12 red cubes, 13 green cubes, and 14 blue cube
    red_count = 12
    green_count = 13
    blue_count = 14

    total = 0
    for row in rows:
        game_id, max_red, max_green, max_blue = parse_row_and_max_cube_count(row)

        if red_count >= max_red and green_count >= max_green and blue_count >= max_blue:
            total += game_id

    return total

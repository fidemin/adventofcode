from day02.common import preprocess, parse_row_and_max_cube_count


def solve(filename):
    with open(filename) as f:
        rows = preprocess(f)

    total = 0
    for row in rows:
        game_id, max_red, max_green, max_blue = parse_row_and_max_cube_count(row)
        set_total_count = max_red * max_green * max_blue
        total += set_total_count

    return total

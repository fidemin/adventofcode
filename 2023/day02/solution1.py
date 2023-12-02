from day02.common import preprocess


def parse_row_and_max_cube_count(row: str):
    """
    :param row: e.g. "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    :return:
    """

    game_str, cubes_str = row.split(': ')
    _, game_id_str = game_str.split(' ')
    game_id = int(game_id_str)

    # sets_str = ['3 blue, 4 red', '1 red, 2 green, 6 blue' ,'2 green']
    sets_str = cubes_str.strip().split('; ')

    max_red = 0
    max_green = 0
    max_blue = 0

    for set_str in sets_str:
        # e.g. set_str = '3 blue, 4 red'

        num_and_cubes = set_str.split(', ')

        for num_cube in num_and_cubes:
            # e.g. num_cube = '3 blue'
            count_str, color = num_cube.split(' ')
            count = int(count_str)

            if color == 'red':
                max_red = max(max_red, count)
            elif color == 'blue':
                max_blue = max(max_blue, count)
            elif color == 'green':
                max_green = max(max_green, count)
            else:
                raise RuntimeError(f'{color} is not wrong color.')

    return game_id, max_red, max_green, max_blue


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

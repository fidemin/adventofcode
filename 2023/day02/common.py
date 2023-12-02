def preprocess(file):
    rows = []
    for line in file:
        rows.append(line.strip())

    return rows


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

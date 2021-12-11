

def parse(command_str: str):
    op = command_str[0]
    arg = int(command_str[1:])
    return op, arg


def run():
    # directions = ['E', 'S', 'W', 'N']
    direction_forward = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    current_direction_pos = 0
    current_location = [0, 0]

    with open('input.txt') as f:
        for row in f:
            op, arg = parse(row)

            if op == 'N':
                current_location[1] += arg
            elif op == 'S':
                current_location[1] -= arg
            elif op == 'E':
                current_location[0] += arg
            elif op == 'W':
                current_location[0] -= arg
            elif op == 'R':
                current_direction_pos = (current_direction_pos + arg // 90) % 4
            elif op == 'L':
                current_direction_pos = (current_direction_pos - arg // 90) % 4
            elif op == 'F':
                current_location[0] += direction_forward[current_direction_pos][0] * arg
                current_location[1] += direction_forward[current_direction_pos][1] * arg
        print(current_location)
        print(abs(current_location[0]) + abs(current_location[1]))


if __name__ == '__main__':
    run()
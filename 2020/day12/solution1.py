

def parse(command_str: str):
    op = command_str[0]
    arg = int(command_str[1:])
    return op, arg


def rotate(way_point: list, degree: int):
    rotate_count = (degree // 90) % 4
    if rotate_count < 0:
        rotate_count += 4

    for _ in range(rotate_count):
        next_x = way_point[1]
        next_y = way_point[0] * -1
        way_point[0] = next_x
        way_point[1] = next_y


def run():
    way_point = [10, 1]
    current_location = [0, 0]

    with open('input.txt') as f:
        for row in f:
            op, arg = parse(row)

            if op == 'N':
                way_point[1] += arg
            elif op == 'S':
                way_point[1] -= arg
            elif op == 'E':
                way_point[0] += arg
            elif op == 'W':
                way_point[0] -= arg
            elif op == 'R':
                rotate(way_point, arg)
            elif op == 'L':
                rotate(way_point, -arg)
            elif op == 'F':
                current_location[0] += way_point[0] * arg
                current_location[1] += way_point[1] * arg

            print('way_point: ', way_point)
            print('current location: ', current_location)

        print(current_location)
        print(abs(current_location[0]) + abs(current_location[1]))


if __name__ == '__main__':
    run()

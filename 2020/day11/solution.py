from copy import deepcopy


def run():
    seats = []

    with open('input.txt') as f:
        for row in f:
            seats.append(list(row.strip()))

    num_of_rows = len(seats)
    num_of_cols = len(seats[0])

    next_round_seats = deepcopy(seats)

    while True:
        for row_i in range(num_of_rows):
            for col_i in range(num_of_cols):
                this_value = seats[row_i][col_i]
                if this_value == '.':
                    continue
                num_occupied = 0
                offsets = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1))
                for offset in offsets:
                    adj_row_i = row_i + offset[0]
                    adj_col_i = col_i + offset[1]
                    if (0 <= adj_row_i < num_of_rows) and (0 <= adj_col_i < num_of_cols):
                        adj_value = seats[adj_row_i][adj_col_i]
                        if adj_value == '#':
                            num_occupied += 1

                if this_value == 'L' and num_occupied == 0:
                    next_round_seats[row_i][col_i] = '#'
                if this_value == '#' and num_occupied >= 4:
                    next_round_seats[row_i][col_i] = 'L'

        # print(next_round_seats)
        if seats == next_round_seats:
            total_number_of_occupied = 0
            for row_i in range(num_of_rows):
                for col_i in range(num_of_cols):
                    if next_round_seats[row_i][col_i] == '#':
                        total_number_of_occupied += 1
            print(total_number_of_occupied)
            break

        seats = next_round_seats
        next_round_seats = deepcopy(seats)


run()

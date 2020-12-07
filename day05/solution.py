from common import calculate_seat_id


if __name__ == '__main__':
    max_seat_id = 0
    with open('input.txt', 'r') as f:
        for row in f:
            seat_id = calculate_seat_id(row.strip())
            max_seat_id = max(max_seat_id, seat_id)

    print(max_seat_id)

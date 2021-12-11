from common import calculate_seat_id


if __name__ == '__main__':
    seat_id_list = []
    with open('input.txt', 'r') as f:
        for row in f:
            seat_id = calculate_seat_id(row.strip())
            seat_id_list.append(seat_id)

    seat_id_list.sort()
    before_seat_id = seat_id_list[0] - 1
    for i, seat_id in enumerate(seat_id_list):
        if seat_id != before_seat_id + 1:
            print(seat_id - 1)
            break
        before_seat_id = seat_id




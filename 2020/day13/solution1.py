

def run():
    with open('input.txt') as f:
        current_timestamp = int(f.readline())
        bus_ids_str = f.readline().rstrip()
        bus_id_and_minute_tuple = [[int(bus_id), i] for i, bus_id in enumerate(bus_ids_str.split(',')) if bus_id != 'x']
        print(bus_id_and_minute_tuple)
        bus_id_and_minute_tuple.sort(key=lambda x: x[0], reverse=True)

        max_bus_id = 0
        minute_with_max_bus_id = None
        for bus_id, minute in bus_id_and_minute_tuple:
            if bus_id > max_bus_id:
                max_bus_id = bus_id
                minute_with_max_bus_id = minute

        success_count_required = len(bus_id_and_minute_tuple)
        count = 1
        while True:
            success_count = 0
            target_timestamp = max_bus_id * count
            for bus_id, minute in bus_id_and_minute_tuple:
                if (target_timestamp + minute - minute_with_max_bus_id) % bus_id == 0:
                    success_count += 1
                else:
                    break
            if success_count_required == success_count:
                break
            count += 1

        print(target_timestamp - minute_with_max_bus_id)


if __name__ == '__main__':
    run()

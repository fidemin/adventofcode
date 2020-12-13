

def run():
    with open('input.txt') as f:
        current_timestamp = int(f.readline())
        bus_ids_str = f.readline().rstrip()
        bus_ids = [int(bus_id) for bus_id in bus_ids_str.split(',') if bus_id != 'x']
        min_timestamp = 1234567890
        min_bus_id = 123456789
        for bus_id in bus_ids:
            next_timestamp = (current_timestamp // bus_id) * bus_id + bus_id
            if next_timestamp < min_timestamp:
                min_bus_id = bus_id
                min_timestamp = next_timestamp

        print(min_timestamp)
        print(min_bus_id)
        print((min_timestamp - current_timestamp) * min_bus_id)


if __name__ == '__main__':
    run()

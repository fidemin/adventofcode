from common import LuggageRule


class BagCounter:
    def __init__(self):
        self.count = 0


def count_bags(bag_counter: BagCounter, index, num_of_target_bags, target_bag_color):
    for num_of_bags, bag_color in index[target_bag_color]:
        this_number_of_bags = num_of_target_bags * num_of_bags
        bag_counter.count += this_number_of_bags
        count_bags(bag_counter, index, this_number_of_bags, bag_color)


if __name__ == '__main__':
    index = {}
    with open('input.txt') as f:
        for row in f:
            rule = LuggageRule.from_str(row)
            assert rule.main_bag_color not in index
            index[rule.main_bag_color] = rule.inner_bags
    bag_counter = BagCounter()
    count_bags(bag_counter, index, 1, 'shiny gold')
    print(bag_counter.count)




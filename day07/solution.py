from collections import defaultdict

from common import LuggageRule


def find_all_bag_colors_contains_the_bag(bag_set: set, inverse_index: dict, target_bag_color: str):
    bags_contain_directly = inverse_index[target_bag_color]
    for bag_color in bags_contain_directly:
        bag_set.add(bag_color)
        find_all_bag_colors_contains_the_bag(bag_set, inverse_index, bag_color)


if __name__ == '__main__':
    inverse_index = defaultdict(set)
    bags_contain_shiny_gold = set()
    with open('input.txt') as f:
        for row in f:
            rule = LuggageRule.from_str(row)
            for inner_bag in rule.inner_bags:
                inverse_index[inner_bag[1]].add(rule.main_bag_color)

    bag_set = set()
    find_all_bag_colors_contains_the_bag(bag_set, inverse_index, 'shiny gold')
    print(len(bag_set))

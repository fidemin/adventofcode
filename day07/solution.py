import re
from collections import defaultdict


class LuggageRule:
    @classmethod
    def from_str(cls, luggage_rule_str: str):
        luggage_rule_str = luggage_rule_str.strip().rstrip('.')
        main_bag_str, mini_bags_str = luggage_rule_str.split(' contain ')
        inner_bag_str_list = mini_bags_str.split(', ')
        main_bag_color = cls._extract_bag_color(main_bag_str)
        inner_bag_color_list = []
        for inner_bag_str in inner_bag_str_list:
            bag_color = cls._extract_bag_color(inner_bag_str)
            if not bag_color:
                break
            inner_bag_color_list.append(bag_color)
        return LuggageRule(main_bag_color, inner_bag_color_list)

    @staticmethod
    def _extract_bag_color(bag_str) -> str:
        """
        :param bag_str:
            e.g. 1 bright white bag
            e.g. 2 muted yellow bags
            e.g. gold shiny bags
            e.g. no other bags
        :return:
            e.g. bright white
            e.g. muted yellow
            e.g. gold shiny
            e.g. None
        """
        if bag_str == 'no other bags':
            return None

        regex = r'^([0-9]+ )?([a-z]+ [a-z]+) bags?$'
        matched = re.match(regex, bag_str)
        if matched:
            return matched.groups()[1]
        assert False, f'{bag_str} is not proper bag_str'

    def __init__(self, main_bag_color: str, inner_bag_colors: [str]):
        self.main_bag_color = main_bag_color
        self.inner_bag_colors = inner_bag_colors

    def __str__(self):
        return f'{self.main_bag_color}: {self.inner_bag_colors}'


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
            for mini_bag_color in rule.inner_bag_colors:
                inverse_index[mini_bag_color].add(rule.main_bag_color)

    bag_set = set()
    find_all_bag_colors_contains_the_bag(bag_set, inverse_index, 'shiny gold')
    print(len(bag_set))

import re


class LuggageRule:
    @classmethod
    def from_str(cls, luggage_rule_str: str):
        luggage_rule_str = luggage_rule_str.strip().rstrip('.')
        main_bag_str, mini_bags_str = luggage_rule_str.split(' contain ')
        inner_bag_str_list = mini_bags_str.split(', ')
        _, main_bag_color = cls._extract_bag_color(main_bag_str)
        inner_bag_list = []
        for inner_bag_str in inner_bag_str_list:
            num_of_bags, bag_color = cls._extract_bag_color(inner_bag_str)
            if not bag_color:
                break
            inner_bag_list.append((num_of_bags, bag_color))
        return LuggageRule(main_bag_color, inner_bag_list)

    @staticmethod
    def _extract_bag_color(bag_str) -> tuple:
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
            return None, None

        regex = r'^([0-9]+ )?([a-z]+ [a-z]+) bags?$'
        matched = re.match(regex, bag_str)
        if matched:
            groups = matched.groups()
            return int(groups[0]) if groups[0] else None, groups[1]
        assert False, f'{bag_str} is not proper bag_str'

    def __init__(self, main_bag_color: str, inner_bags: [tuple]):
        self.main_bag_color = main_bag_color
        self.inner_bags = inner_bags

    def __str__(self):
        return f'{self.main_bag_color}: {self.inner_bags}'

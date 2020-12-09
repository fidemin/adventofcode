import re


class LuggageRule:
    @classmethod
    def from_str(cls, luggage_rule_str: str):
        luggage_rule_str = luggage_rule_str.strip().rstrip('.')
        main_bag_str, mini_bags_str = luggage_rule_str.split(' contain ')
        mini_bag_str_list = mini_bags_str.split(', ')
        main_bag_color = cls._extract_bag_color(main_bag_str)
        mini_bag_color_list = []
        for mini_bag_str in mini_bag_str_list:
            bag_color = cls._extract_bag_color(mini_bag_str)
            if not bag_color:
                break
            mini_bag_color_list.append(bag_color)
        return LuggageRule(main_bag_color, mini_bag_color_list)

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


if __name__ == '__main__':
    with open('sample_input.txt') as f:
        for row in f:
            print(LuggageRule.from_str(row))

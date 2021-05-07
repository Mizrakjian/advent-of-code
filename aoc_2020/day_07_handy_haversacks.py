"""
AoC 2020.7: Handy Haversacks

Created on Fri Dec 18 17:47 2020
"""
import re


def init() -> dict:
    """
    Return dict of bag rules from text input file.
    Format: bag color : list of tuples of contained bags amount and color.

    Example:
        "dotted salmon bags contain 2 dark lavender bags, 1 muted red bag, \
            1 vibrant magenta bag."

    becomes:

        {'dotted salmon': [(2, 'dark lavender'), (1, 'muted red'), (1, 'vibrant magenta')]}
    """
    bags = {}
    with open("input/day_07_input.txt") as rules:
        for rule in rules:
            color, contents = rule.split(" bags contain")
            inside = re.findall(r"(\d+) (.+?) bag", contents)
            bags[color] = [(int(n), c) for n, c in inside]
    return bags


def has_color(target: str, bags: dict) -> int:
    """Return the number of bags that could contain target."""
    count = 0
    for bag in bags:
        searching = set([bag])
        while searching:
            color = searching.pop()
            inside = set(c for n, c in bags[color])
            searching |= inside
            if target in searching:
                count += 1
                break
    return count


def part_1(bags: dict) -> int:
    """
    You have a shiny gold bag. If you wanted to carry it in at least one other bag,
    how many different bag colors would be valid for the outermost bag?
    (In other words: how many colors can, eventually, contain at least one shiny gold bag?)
    """
    return has_color("shiny gold", bags)


def count_bags_in(target: str, bags: dict) -> int:
    """Return the number of bags that target must contain."""
    count = 0
    searching = [[1, target]]
    while searching:
        mult, color = searching.pop()
        for num, inner_bag in bags[color]:
            amount = mult * num
            searching.append([amount, inner_bag])
            count += amount
    return count


def part_2(bags: dict) -> int:
    """
    Of course, the actual rules have a small chance of going several levels deeper than
    this example; be sure to count all of the bags, even if the nesting becomes
    topologically impractical!

    How many individual bags are required inside your single shiny gold bag?
    """
    return count_bags_in("shiny gold", bags)


def main():
    """
    Due to recent aviation regulations, many rules (your puzzle input) are being enforced
    about bags and their contents; bags must be color-coded and must contain specific
    quantities of other color-coded bags. Apparently, nobody responsible for these
    regulations considered how long they would take to enforce!
    """
    print(__doc__.splitlines()[1], "\n")

    bags = init()

    print(f"  Bags that can contain shiny gold: {part_1(bags)}")
    print(f"    Bags contained in a shiny gold: {part_2(bags)}")


if __name__ == "__main__":
    main()

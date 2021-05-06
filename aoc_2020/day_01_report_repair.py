"""
AoC2020.1: Report Repair

Created on Thu Dec 3 19:26:00 2020
"""
from itertools import combinations
from math import prod


def init() -> set:
    """Return set of ints from puzzle input file."""
    with open("input/day_01_input.txt") as file:
        return {int(entry) for entry in file}


def x_sum_prod(array: set, items: int, target: int) -> int:
    """
    Return the product of items number of array elements that sum to target.
    If not found, return -1.
    """
    for combo in combinations(array, r=items - 1):
        result = target - sum(combo)
        if result in array:
            return result * prod(combo)
    return -1


YEAR = 2020


def part_1(expenses: set) -> int:
    """Return the product of 2 expenses items that sum to YEAR. If not found, return -1."""
    return x_sum_prod(expenses, 2, YEAR)


def part_2(expenses: set) -> int:
    """Return the product of 3 expenses items that sum to YEAR. If not found, return -1."""
    return x_sum_prod(expenses, 3, YEAR)


def main():
    """
    Before you leave, the Elves in accounting just need you to fix your expense report
    (your puzzle input); apparently, something isn't quite adding up.

    Part 1:
    Specifically, they need you to find the two entries that sum to 2020 and then
    multiply those two numbers together.

    Part 2:
    In your expense report, what is the product of the three entries that sum to 2020?
    """
    print(__doc__.splitlines()[1], "\n")

    expenses = init()

    print(f"  2-sum {YEAR} product: {part_1(expenses)}")
    print(f"  3-sum {YEAR} product: {part_2(expenses)}")

    # for items in [2, 3]:
    #     print(f"  {items}-sum {YEAR} product:", x_sum_prod(expenses, items, YEAR))


if __name__ == "__main__":
    main()

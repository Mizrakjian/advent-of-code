"""
AoC2020.1: Report Repair

Created on Thu Dec 3 19:26:00 2020
"""
from itertools import combinations
from math import prod


def x_sum_prod(array: list, items: int, target: int) -> int:
    """Return the product of array items that sum to target. If not found, return -1."""
    for combo in combinations(array, r=items):
        if sum(combo) == target:
            return prod(combo)
    return -1


def init() -> list:
    """Return list of ints from puzzle input file."""
    with open("input/day_01_input.txt") as file:
        return [int(entry) for entry in file]


YEAR = 2020


def part_1(data: list) -> int:
    return x_sum_prod(data, 2, YEAR)


def part_2(data: list) -> int:
    return x_sum_prod(data, 3, YEAR)


def main():
    print(__doc__.splitlines()[1], "\n")

    expenses = init()

    for items in [2, 3]:
        print(f"  {items}-sum {YEAR} product:", x_sum_prod(expenses, items, YEAR))


if __name__ == "__main__":
    main()

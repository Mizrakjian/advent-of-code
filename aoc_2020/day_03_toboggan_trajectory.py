"""
AoC2020.3: Toboggan Trajectory

Created on Sun Dec 13 13:18:00 2020
"""
import math


def check_slope(tree_map: list, slope: tuple) -> int:
    """Return number of trees found in tree_map on slope(right, down)."""
    right, down = slope
    position = trees_found = 0
    width = len(tree_map[0])

    for elevation in tree_map[::down]:
        if elevation[position % width] == "#":
            trees_found += 1
        position += right

    return trees_found


def init() -> list:
    """Return a list of stripped lines (ASCII tree map) from file."""
    with open("input/day_03_input.txt") as file:
        return [elevation.strip() for elevation in file]


def part_1(tree_map: list) -> int:
    """Return number of trees found on slope (3, 1) in tree_map."""
    slope = (3, 1)
    return check_slope(tree_map, slope)


def part_2(tree_map: list) -> int:
    """Return product of trees found on slopes in tree_map."""
    slopes = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
    return math.prod(check_slope(tree_map, slope) for slope in slopes)


def main():
    print(__doc__.splitlines()[1], "\n")

    data = init()

    print(f"    Slope (3, 1) trees hit: {part_1(data)}")
    print(f"  Mutli-slope tree product: {part_2(data)}")


if __name__ == "__main__":
    main()

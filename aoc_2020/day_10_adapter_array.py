"""
AoC 2020.10: Adapter Array

Created on Sat Jan 23 11:59 2021
"""
from collections import Counter


def adapter_perms(diffs: list) -> int:
    """Return the total possible ways to connect adapters."""
    mult = lambda i: int(3 * 2 ** (i - 3) + 1)  # this seems right, but might not be
    total = 1
    count = 0
    for i in diffs:
        if i == 1:
            count += 1
        else:
            if count > 1:
                total *= mult(count)
            count = 0
    if count > 1:
        total *= mult(count)
    return total


def init() -> list:
    """Return the joltage differences between a sorted list of adapters from a file."""
    with open("input/day_10_input.txt") as file:
        adapters = sorted(int(line) for line in file)
    adapters.append(adapters[-1] + 3)
    return [b - a for a, b in zip((0, *adapters), adapters)]


def part_1(diffs: list) -> int:
    """
    Find a chain that uses all of your adapters to connect the charging outlet to
    your device's built-in adapter and count the joltage differences between the
    charging outlet, the adapters, and your device. What is the number of 1-jolt
    differences multiplied by the number of 3-jolt differences?
    """
    jolts = Counter(diffs)
    return jolts[1] * jolts[3]


def part_2(diffs: list) -> int:
    """
    You glance back down at your bag and try to remember why you brought so many
    adapters; there must be more than a trillion valid ways to arrange them! Surely,
    there must be an efficient way to count the arrangements. What is the total number
    of distinct ways you can arrange the adapters to connect the charging outlet
    to your device?
    """
    return adapter_perms(diffs)


def main():
    print(__doc__.splitlines()[1], "\n")

    diffs = init()

    print(f"  1-jolts * 3-jolts: {part_1(diffs)}")
    print(f"     Configurations: {part_2(diffs)}")


if __name__ == "__main__":
    main()

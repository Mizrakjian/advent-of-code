"""
AoC 2020.9: Encoding Error

Created on Mon Jan 11 17:42 2021
"""


def find_anomoly(xmas: tuple) -> int:
    """Return the first element that isn't a two sum from the 25 previous elements."""
    for index, target in enumerate(xmas[25:], 25):
        check = xmas[index - 25 : index]
        if not any(i for i in check if target - i in check):
            return target
    return -1


def find_weakness(xmas: tuple, target: int) -> int:
    """Return the sum of the min and max elements of the slice that sums to target."""

    left = right = next(i for i, x in enumerate(xmas) if x >= target // 2)
    current = xmas[left]

    while current != target:
        if current > target:
            current -= xmas[right]
            right -= 1
        left -= 1
        current += xmas[left]

    return min(xmas[left : right + 1]) + max(xmas[left : right + 1])


def init() -> tuple:
    with open("input/day_09_input.txt") as file:
        return tuple(int(line) for line in file)


def part_1(xmas: tuple) -> int:
    """
    The first step of attacking the weakness in the XMAS data is to find the first
    number in the list (after the preamble) which is not the sum of two of the 25
    numbers before it. What is the first number that does not have this property?
    """
    return find_anomoly(xmas)


def part_2(xmas: tuple) -> int:
    """
    The final step in breaking the XMAS encryption relies on the invalid number you
    just found: you must find a contiguous set of at least two numbers in your list
    which sum to the invalid number from step 1.
    """
    return find_weakness(xmas, find_anomoly(xmas))


def main():
    """
    XMAS starts by transmitting a preamble of 25 numbers. After that, each number you
    receive should be the sum of any two of the 25 immediately previous numbers.
    The two numbers will have different values, and there might be more than one such pair.
    """
    print(__doc__.splitlines()[1], "\n")

    xmas = init()

    print(f"  First non-sum entry: {part_1(xmas)}")
    print(f"  Encryption weakness: {part_2(xmas)}")


if __name__ == "__main__":
    main()

"""
AoC 2020.6: Custom Customs

Created on Thu Dec 17 17:50 2020
"""


def init() -> list:
    with open("input/day_06_input.txt") as file:
        return [
            [set(person) for person in group.split("\n") if person]
            for group in file.read().split("\n\n")
        ]


def part_1(groups: list) -> int:
    """Return sum of all answers in groups."""
    return sum(len(set.union(*g)) for g in groups)


def part_2(groups: list) -> int:
    """Return sum of common answers in groups."""
    return sum(len(set.intersection(*g)) for g in groups)


def main():
    print(__doc__.splitlines()[1], "\n")

    groups = init()

    print(f"  Unique answers: {part_1(groups)}")
    print(f"  Shared answers: {part_2(groups)}")


if __name__ == "__main__":
    main()

"""
AoC2020.2: Password Philosophy

Created on Thu Dec 3 20:46:00 2020
"""
import re

# with open("./input/day_2_input.txt") as file:
#     passwords = [[entry.strip(":\n") for entry in line.split(" ")] for line in file]
# passwords = [
#     list(map(int, policy.split("-"))) + [char, password]  # type: ignore
#     for policy, char, password in passwords
# ]

# passwords = []
# with open("./input/day_2_input.txt") as file:
#     for line in file:
#         policy, char, password = [field.strip(":\n") for field in line.split(" ")]
#         passwords.append(policy.split("-") + [char, password])


def init() -> list:
    with open("input/day_02_input.txt") as file:
        return re.findall(r"(\d+)-(\d+) (\w): (\w+)", file.read())


def part_1(passwords: list) -> int:
    """Return count of passwords that have the right amount of pchr."""

    def correct_count(password: tuple) -> bool:
        cmin, cmax, pchr, pword = password
        return int(cmin) <= pword.count(pchr) <= int(cmax)

    return sum(map(correct_count, passwords))


def part_2(passwords: list) -> int:
    """Return count of passwords that have pchr in only one correct position (XOR)."""

    def correct_xor_pos(password: tuple) -> bool:
        cmin, cmax, pchr, pword = password
        return (pword[int(cmin) - 1] == pchr) ^ (pword[int(cmax) - 1] == pchr)

    return sum(map(correct_xor_pos, passwords))


def main():
    print(__doc__.splitlines()[1], "\n")

    data = init()
    old = part_1(data)
    otcp = part_2(data)

    print("   Valid passwords (old method):", old)
    print("  Valid passwords (OTCP method):", otcp)


if __name__ == "__main__":
    main()

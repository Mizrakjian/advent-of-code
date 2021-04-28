"""
AoC 2020.5: Binary Boarding

Created on Thu Dec 17 14:18 2020
"""


def id_seat(boarding_pass: str) -> int:
    """Return int seat ID from str boarding pass binary space partitioning seat code."""
    index_bsp = enumerate(reversed(boarding_pass.strip()))
    return sum((bit in "BR") << exp for exp, bit in index_bsp)


def init() -> set:
    with open("input/day_05_input.txt") as boarding_passes:
        seat_ids = {*map(id_seat, boarding_passes)}
        return seat_ids


def part_1(seat_ids: set) -> int:
    """Return the max seat ID."""
    return max(seat_ids)


def part_2(seat_ids: set) -> int:
    """Return "your" seat ID - inside the range of all IDs but not in the set."""
    seat_min, seat_max = min(seat_ids), max(seat_ids)
    return (seat_ids ^ {*range(seat_min, seat_max + 1)}).pop()


def main():
    print(__doc__.splitlines()[1], "\n")

    seat_ids = init()

    print(f"  Highest seat ID: {part_1(seat_ids)}")
    print(f"     Your seat ID: {part_2(seat_ids)}")


if __name__ == "__main__":
    main()

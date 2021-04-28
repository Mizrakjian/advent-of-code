"""
AoC 2020.5: Binary Boarding

Created on Thu Dec 17 14:18 2020
"""
print(__doc__.splitlines()[1], "\n")


def id_seat(boarding_pass: str) -> int:
    """Return int seat ID from str boarding pass binary space partitioning seat code."""
    index_bsp = enumerate(reversed(boarding_pass.strip()))
    return sum((bit in "BR") << exp for exp, bit in index_bsp)


with open("./input/2020_day_5_input.txt") as boarding_passes:
    seat_ids = {*map(id_seat, boarding_passes)}

seat_min, seat_max = min(seat_ids), max(seat_ids)
print(f"  Highest seat ID: {seat_max}")

your_seat = (seat_ids ^ {*range(seat_min, seat_max + 1)}).pop()
print(f"     Your seat ID: {your_seat}")

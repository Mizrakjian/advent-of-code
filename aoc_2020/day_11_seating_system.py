"""
AoC 2020.11: Seating System

Created on Sun Jan 24 02:29 2021
"""
from itertools import product
from typing import Callable


def nearby(seats: dict, x: int, y: int) -> int:
    """Return count of nearby occupied seats (incluing origin seat if occupied)."""
    occupied = 0

    for x_move, y_move in product((-1, 0, 1), repeat=2):
        nearby = x + x_move, y + y_move
        while seats.get(nearby) == ".":
            nearby = nearby[0] + x_move, nearby[1] + y_move
        occupied += seats.get(nearby) == "#"

    return occupied


def adjacent(seats: dict, x: int, y: int) -> int:
    """Return count of adjacent occupied seats (incluing origin seat if occupied)."""
    adjacent = product(range(x - 1, x + 2), range(y - 1, y + 2))
    return sum(seats.get(spot) == "#" for spot in adjacent)


def update(seats: dict, count_neighbors: Callable) -> dict:
    """Return dict of new seat state after simulating seat occupancy."""
    state = seats.copy()
    floor, empty, taken = ".L#"
    max_occupancy = 5 - (count_neighbors is adjacent)

    for seat, status in seats.items():
        if status == floor:
            continue
        neighbors = count_neighbors(seats, *seat)
        if status == empty and neighbors == 0:
            state[seat] = taken
        elif status == taken and neighbors > max_occupancy:
            state[seat] = empty

    return state


def find_equilibrium(seat_map: dict, *, count_neighbors: Callable) -> int:
    """
    Return count of total occupied seats when count stabilizes using one of two
    count_neighbors simulation methods:
        count_neighbors=adjacent only counts immediately adjacent seats.
        count_neighbors=nearby searches in eight directions for seats at
        any distance up until the search goes out of bounds.
    """
    seats = seat_map.copy()
    occupied = {}

    while occupied != seats:
        occupied = seats
        seats = update(seats, count_neighbors)

    return [*occupied.values()].count("#")


def init() -> dict:
    """Return a dict of location keys and seat/floor status values from input file."""
    with open("input/day_11_input.txt") as file:
        return {
            (x, y): seat
            for y, line in enumerate(file)
            for x, seat in enumerate(line.strip())
        }


def part_1(seats: dict) -> int:
    """
    You need to model people sitting in a waiting area. The following rules are
    applied to every seat simultaneously:
        - If a seat is empty (L) and there are no occupied seats adjacent to it,
          the seat becomes occupied.
        - If a seat is occupied (#) and four or more seats adjacent to it are also
          occupied, the seat becomes empty.
        - Otherwise, the seat's state does not change.

    Simulate your seating area by applying the seating rules repeatedly until no seats
    change state. How many seats end up occupied?
    """
    return find_equilibrium(seats, count_neighbors=adjacent)


def part_2(seats: dict) -> int:
    """
    As soon as people start to arrive, you realize your mistake. People don't just
    care about adjacent seats - they care about the first seat they can see in each
    of those eight directions! Now, instead of considering just the eight immediately
    adjacent seats, consider the first seat in each of those eight directions.

    Also, people seem to be more tolerant than you expected: it now takes five or
    more visible occupied seats for an occupied seat to become empty (rather than
    four or more from the previous rules). The other rules still apply.

    Given the new visibility method and the rule change for occupied seats becoming
    empty, once equilibrium is reached, how many seats end up occupied?
    """
    return find_equilibrium(seats, count_neighbors=nearby)


def main():
    print(__doc__.splitlines()[1], "\n")

    seat_map = init()

    print(f"  Adjacent equilibrium: {part_1(seat_map)}")
    print(f"   Visible equilibrium: {part_2(seat_map)}")


if __name__ == "__main__":
    main()

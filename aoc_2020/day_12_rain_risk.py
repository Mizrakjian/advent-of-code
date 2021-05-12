"""
AoC 2020.12: Rain Risk

Created on Sun Feb 07 12:02 2021
"""


def manhattan_distance(location: complex) -> int:
    """Return int Manhattan distance from complex location vector to (0, 0)."""
    return int(abs(location.real) + abs(location.imag))


def init() -> list:
    """Return list of (str, int) tuples of actions and values from input file."""
    with open("input/day_12_input.txt") as file:
        return [(i[0], int(i[1:])) for i in file]


MOVE = {"N": 0 - 1j, "S": 0 + 1j, "E": 1 + 0j, "W": -1 + 0j}


def part_1(steps: list) -> int:
    """
    Part 1: Inferred Instructions
    The navigation instructions (your puzzle input) consists of a sequence of
    single-character actions paired with integer input values. After staring at
    them for a few minutes, you work out what they probably mean:

        - Action N means to move north by the given value.
        - Action S means to move south by the given value.
        - Action E means to move east by the given value.
        - Action W means to move west by the given value.
        - Action L means to turn left the given number of degrees.
        - Action R means to turn right the given number of degrees.
        - Action F means to move forward by the given value in the direction
          the ship is currently facing.

    The ship starts by facing east. Only the L and R actions change the direction
    the ship is facing.

    Figure out where the navigation instructions lead. What is the Manhattan
    distance between that location and the ship's starting position?
    """
    location = 0 + 0j
    heading = 0
    forward = {270: "N", 90: "S", 0: "E", 180: "W"}
    for action, value in steps:
        if action in MOVE:
            location += MOVE[action] * value
        elif action in "LR":
            heading += value if action == "R" else -value
            heading %= 360
        elif action == "F":
            location += MOVE[forward[heading]] * value
    return manhattan_distance(location)


def part_2(steps: list) -> int:
    """
    Part 2: Actual Instructions
    Before you can give the destination to the captain, you realize that the
    actual action meanings were printed on the back of the instructions the
    whole time.

    Almost all of the actions indicate how to move a waypoint which is relative
    to the ship's position:

        - Action N means to move the waypoint north by the given value.
        - Action S means to move the waypoint south by the given value.
        - Action E means to move the waypoint east by the given value.
        - Action W means to move the waypoint west by the given value.
        - Action L means to rotate the waypoint around the ship left
          (counter-clockwise) the given number of degrees.
        - Action R means to rotate the waypoint around the ship right
          (clockwise) the given number of degrees.
        - Action F means to move forward to the waypoint a number of times
          equal to the given value.

    The waypoint starts 10 units east and 1 unit north relative to the ship.
    The waypoint is relative to the ship; that is, if the ship moves,
    the waypoint moves with it.

    Figure out where the navigation instructions actually lead. What is the
    Manhattan distance between that location and the ship's starting position?
    """
    location = 0 + 0j
    waypoint = 10 - 1j
    for action, value in steps:
        if action in MOVE:
            waypoint += MOVE[action] * value
        elif action in "LR":
            if value == 180:
                waypoint *= -1
                continue
            waypoint = complex(-waypoint.imag, waypoint.real)  # rotate 90 deg right
            if (value == 270) ^ (action == "L"):
                waypoint *= -1  # if 270 deg xor left: flip the previous quarter turn
        elif action == "F":
            location += waypoint * value
    return manhattan_distance(location)


def main():
    print(__doc__.splitlines()[1], "\n")

    steps = init()

    print(f"  Distance (inferred rules): {part_1(steps)}")
    print(f"    Distance (actual rules): {part_2(steps)}")


if __name__ == "__main__":
    main()

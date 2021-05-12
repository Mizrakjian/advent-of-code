"""
AoC 2020.13: Shuttle Search

Created on Wed Feb 10 13:37 2021
"""


def init() -> tuple:
    with open("input/day_13_input.txt") as schedule:
        time = int(next(schedule))
        shuttles = []
        for offset, bus in enumerate(next(schedule).split(",")):
            if bus != "x":
                shuttles.append((int(bus), offset))
    return time, shuttles


def earliest_bus(schedule: tuple) -> int:
    """Return product of wait time and bus ID for bus which arrives closest to time."""
    time, shuttles = schedule
    wait, bus = min((bus - time % bus, bus) for bus, _ in shuttles)
    return wait * bus


def earliest_time(schedule: tuple) -> int:
    """Return earliest timestamp where buses depart at offsets matching the bus ID list."""
    _, shuttles = schedule
    timetable = sorted(shuttles, reverse=True)
    bus, offset = timetable.pop(0)
    start, step = bus - offset, bus
    for bus, offset in timetable:
        while (start + offset) % bus:
            start += step
        step *= bus
    return start


def part_1(schedule: tuple) -> int:
    """Call earliest_bus and return result."""
    return earliest_bus(schedule)


def part_2(schedule: tuple) -> int:
    """Call earliest_time and return result."""
    return earliest_time(schedule)


def main():
    print(__doc__.splitlines()[1], "\n")

    schedule = init()

    print(f"   Earliest bus: {part_1(schedule)}")
    print(f"  Earliest time: {part_2(schedule)}")


if __name__ == "__main__":
    main()

"""
AoC 2020.0: Test and Run AoC 2020 Solutions

Created on Mon Apr 26 18:45 2021
"""

print(__doc__.splitlines()[1])

import pkgutil
from math import log10
from time import perf_counter_ns
from typing import Callable


def scale(time: int, precision: int = 0) -> str:
    """Return a scaled timing string."""
    unit = {0: "ns", 3: "µs", 6: "ms", 9: "seconds"}
    scale = int(log10(time) // 3 * 3)
    if scale >= 9:  # max scale is seconds with 3 digits of precision
        scale = 9
        precision = 3
    return f"{time / 10 ** scale:,.{precision}f} {unit[scale]}"


def print_time(msg: str, func: Callable, data="") -> int:
    """Return int results from func after printing msg, results, and runtime of func."""
    print(f"  {msg}", end="", flush=True)

    start = perf_counter_ns()
    result = func(data) if data else func()
    runtime = perf_counter_ns() - start

    msg = f" {str(result)}" if data else ""
    print(f"{msg} [{scale(runtime)}]")
    return result


search_path = ["."]  # set to None to see all modules importable from sys.path
aoc_2020 = [x[1] for x in pkgutil.iter_modules(path=search_path)]

print(aoc_2020)

for day in aoc_2020:
    day = __import__(day)
    print("\n" + day.__doc__.splitlines()[1])

    data = print_time("Init", day.init)

    print_time("Part 1:", day.part_1, data)
    print_time("Part 2:", day.part_2, data)

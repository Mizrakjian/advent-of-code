"""
AoC 2020.15: Rambunctious Recitation

Created on Wed Feb 17 15:59 2021
"""
from numba import njit


@njit(cache=True)  # type:ignore
def memory_game(seed: list[int], steps: int) -> int:
    """
    Return the number found after steps iterations of a Van Eck sequence initialized
    with the numbers found in seed.

    Each step of a Van Eck sequence consists of considering the most recently recorded
    number:
        - If that was the first time the number has appeared, the current number is 0.
        - Otherwise, the number had appeared before; the current number is how many
          steps apart the prior number is from when it was previously seen.
    """
    history = [0] * steps

    for step, term in enumerate(seed, 1):
        history[term] = step

    age = 0  # previous term was new

    for step in range(len(seed) + 1, steps):
        term = age  # current term is age of previous term
        age = step - (history[term] or step)  # get current term age
        history[term] = step

    return age


def init() -> list[int]:
    starting_numbers = [9, 6, 0, 10, 18, 2, 1]
    return starting_numbers


def part_1(starting: list[int]) -> int:
    return memory_game(starting, 2020)


def part_2(starting: list[int]) -> int:
    return memory_game(starting, 30_000_000)


def main():
    print(__doc__.splitlines()[1], "\n")

    starting = init()

    for turns in [2020, 30_000_000]:
        print(f"{turns:>12,}th number spoken: {memory_game(starting, turns)}")


if __name__ == "__main__":
    main()

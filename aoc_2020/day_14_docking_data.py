"""
AoC 2020.14: Docking Data

Created on Thu Feb 11 00:16 2021
"""
from itertools import combinations

Program = dict[tuple[int, int], list[tuple[int, int]]]


def init() -> Program:
    """Return dict of {int masks tuple: list of int operation tuples} from text file."""
    prog = {}
    with open("input/day_14_input.txt") as file:
        for line in file:
            if "mask" in line:
                mask = show = 0
                for i, bit in enumerate(reversed(line[7:-1])):
                    if bit == "1":
                        mask += 1 << i
                    elif bit == "X":
                        show += 1 << i
                prog[mask, show] = []
            else:
                addr, val = line.split("] = ")
                addr, val = int(addr[4:]), int(val)
                prog[mask, show].append((addr, val))  # type: ignore
    return prog


def part_1(p: Program) -> int:
    """
    Return the sum of all values in memory created from a dict of masks, addresses
    and values. Two bitmasks, show and mask, are applied to values immediately before
    writing values to memory:
        - Set bits in show leave the corresponding bits in value unchanged.
        - Set bits in mask overwrite the corresponding bits in value.

    {address: value & show | mask}
    """
    return sum({a: v & s | m for (m, s) in p for a, v in p[m, s]}.values())  # golfing


def part_2(prog: Program) -> int:
    """
    Return the sum of all values in memory created from a dict of masks, addresses
    and values. Two bitmasks, show and mask, are applied to addresses immediately
    before writing values to memory.
        - Set bits in show will become "floating bits" in the address.
        - Set bits in mask overwrite the corresponding bit in the address

    Floating bits take on all possible states, so value is written to each possible
    address created using floating bits.

    {address & ~show | mask | floating_bits_combo: value}
    """
    mem = {}
    for (mask, show), ops in prog.items():
        floating_bits = [1 << bit for bit in range(36) if show >> bit & 1]
        floating_sets = [
            sum(state)
            for count in range(len(floating_bits) + 1)
            for state in combinations(floating_bits, count)
        ]
        for addr, value in ops:
            partial_addr = addr & ~show | mask
            for floating_mask in floating_sets:
                mem[partial_addr | floating_mask] = value

    return sum(mem.values())


def main():
    print(__doc__.splitlines()[1], "\n")

    prog = init()

    for i, ver in enumerate([part_1, part_2], 1):
        print(f"  decoder v{i}.0 sum: {ver(prog)}")


if __name__ == "__main__":
    main()
